"""Persisted idempotency records and operation replay."""

import hashlib
import json
from contextlib import contextmanager

from psycopg.types.json import Jsonb

from app.core.config import get_settings
from app.core.db import get_conn
from app.core.errors import IdempotencyConflict, IdempotencyKeyRequired


def validate_key(value: str | None) -> str:
    if not isinstance(value, str) or not 1 <= len(value.strip()) <= 128:
        raise IdempotencyKeyRequired()
    return value.strip()


def fingerprint(value) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()


@contextmanager
def serialized_operation(operation_type: str, key: str, request_fingerprint: str):
    """Serialize equal keys. The caller receives a replay tuple or an operation id."""
    key = validate_key(key)
    lock_name = f"insighthub:{operation_type}:{key}"
    with get_conn() as lock_conn:
        original_autocommit = lock_conn.autocommit
        lock_conn.autocommit = True
        lock_conn.execute("SELECT pg_advisory_lock(hashtextextended(%s, 0))", (lock_name,))
        try:
            with lock_conn.transaction():
                row = lock_conn.execute(
                    "SELECT id, request_fingerprint, status, http_status, response_body "
                    "FROM operation_records WHERE operation_type=%s AND operation_key=%s "
                    "AND expires_at > now() FOR UPDATE",
                    (operation_type, key),
                ).fetchone()
                if row is not None:
                    if row[1] != request_fingerprint:
                        raise IdempotencyConflict()
                    if row[2] in {"succeeded", "failed"}:
                        replay = {"replay": True, "id": row[0], "status": row[3], "body": row[4]}
                        created = None
                    else:
                        created = row[0]
                        lock_conn.execute(
                            "UPDATE operation_records SET updated_at=now(), expires_at=now() + (%s * interval '1 hour') WHERE id=%s",
                            (get_settings().idempotency_ttl_hours, created),
                        )
                else:
                    created = lock_conn.execute(
                        "INSERT INTO operation_records(operation_type, operation_key, request_fingerprint, status, expires_at) "
                        "VALUES (%s,%s,%s,'processing',now() + (%s * interval '1 hour')) RETURNING id",
                        (operation_type, key, request_fingerprint, get_settings().idempotency_ttl_hours),
                    ).fetchone()[0]
            if created is None:
                yield replay
            else:
                yield {"replay": False, "id": created}
        finally:
            lock_conn.execute("SELECT pg_advisory_unlock(hashtextextended(%s, 0))", (lock_name,))
            lock_conn.autocommit = original_autocommit


def complete_operation(operation_id: int, status: int, body: dict, *, error_code: str | None = None):
    state = "succeeded" if status < 400 else "failed"
    with get_conn() as conn:
        conn.execute(
            "UPDATE operation_records SET status=%s,http_status=%s,response_body=%s,error_code=%s,updated_at=now() WHERE id=%s",
            (state, status, Jsonb(body), error_code, operation_id),
        )
