"""Session advisory locks coordinate chat reads with document deletion."""

from contextlib import contextmanager

from app.core.db import get_conn


@contextmanager
def shared_document_locks(document_ids: list[int]):
    ordered = sorted(set(document_ids))
    with get_conn() as conn:
        original_autocommit = conn.autocommit
        conn.autocommit = True
        try:
            for document_id in ordered:
                conn.execute("SELECT pg_advisory_lock_shared(hashtextextended(%s,0))", (f"document:{document_id}",))
            yield
        finally:
            for document_id in reversed(ordered):
                conn.execute("SELECT pg_advisory_unlock_shared(hashtextextended(%s,0))", (f"document:{document_id}",))
            conn.autocommit = original_autocommit
