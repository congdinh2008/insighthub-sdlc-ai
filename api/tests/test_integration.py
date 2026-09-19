"""Opt in with RUN_DB_TESTS=1 and mount init.sql as TEST_SCHEMA_PATH in Docker.

Each test run owns a random PostgreSQL schema. Only that schema is truncated/dropped.
No paid providers are called. A missing DB/schema fixture fails an opted-in run.
"""

import concurrent.futures
import os
from pathlib import Path
import threading
import unittest
import uuid
from unittest.mock import patch

from support import configured, real_config
import psycopg
from psycopg import sql
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool
from fastapi.testclient import TestClient

from app.core import db
from app.core.db import recover_interrupted_operations
from app.core.config import get_settings
from app.core.errors import (
    DocumentConflict,
    IndexIdentityConflict,
    ProviderError,
    SchemaMismatch,
)
from app.core.index import check_schema
from app.core.migrations import run_migrations
from app.main import app
from app.services.embeddings import _local_embed
from app.services.ingestion import process_document
from app.services.retrieval import retrieve


@unittest.skipUnless(
    os.environ.get("RUN_DB_TESTS") == "1",
    "Set RUN_DB_TESTS=1 for isolated PostgreSQL integration tests",
)
class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dsn = os.environ.get("TEST_DATABASE_URL") or get_settings().database_url
        cls.schema = "test_insighthub_" + uuid.uuid4().hex
        source = Path(
            os.environ.get(
                "TEST_SCHEMA_PATH",
                str(Path(__file__).resolve().parents[2] / "infra/db/init.sql"),
            )
        )
        cls.schema_sql = source.read_text()
        cls.old_pool = db._pool
        with psycopg.connect(cls.dsn, autocommit=True) as conn:
            # Extension must be installed by the DB bootstrap, never by the test run.
            if not conn.execute(
                "SELECT 1 FROM pg_extension WHERE extname = 'vector'"
            ).fetchone():
                raise RuntimeError(
                    "Initialize pgvector using infra/db/init.sql before integration tests"
                )
            conn.execute(sql.SQL("CREATE SCHEMA {}").format(sql.Identifier(cls.schema)))
        cls.addClassCleanup(cls.cleanup_schema)
        with psycopg.connect(
            cls.dsn, options=f"-csearch_path={cls.schema},public"
        ) as conn:
            conn.execute(cls.schema_sql)
        db._pool = ConnectionPool(
            conninfo=cls.dsn,
            min_size=2,
            max_size=10,
            configure=db._configure,
            kwargs={"options": f"-csearch_path={cls.schema},public"},
            open=True,
        )
        db._pool.wait(timeout=15)

    @classmethod
    def cleanup_schema(cls):
        if db._pool is not cls.old_pool:
            db._pool.close()
        db._pool = cls.old_pool
        with psycopg.connect(cls.dsn, autocommit=True) as conn:
            conn.execute(
                sql.SQL("DROP SCHEMA {} CASCADE").format(sql.Identifier(cls.schema))
            )

    def setUp(self):
        self.config = configured()
        self.config.__enter__()
        self.addCleanup(self.config.__exit__, None, None, None)
        with db.get_conn() as conn:
            conn.execute(
                "TRUNCATE operation_records, chunks, documents, embedding_index RESTART IDENTITY CASCADE"
            )
        self.client = TestClient(app)
        self.key_index = 0

    def headers(self):
        self.key_index += 1
        return {"Idempotency-Key": f"test-{self._testMethodName}-{self.key_index}"}

    def create_document(self, filename="test.txt"):
        with db.get_conn() as conn:
            return conn.execute(
                "INSERT INTO documents(filename) VALUES (%s) RETURNING id",
                (filename,),
            ).fetchone()[0]

    def state(self, document_id):
        with db.get_conn() as conn:
            return conn.execute(
                "SELECT status, chunk_count, content_sha256, error_code, "
                "(SELECT count(*) FROM chunks WHERE document_id = documents.id) "
                "FROM documents WHERE id = %s",
                (document_id,),
            ).fetchone()

    def test_fixture_upload_retrieve_chat_metrics_delete_end_to_end(self):
        self.assertEqual(self.client.get("/readyz").status_code, 200)
        self.assertEqual(
            self.client.post("/chat", headers=self.headers(), json={"question": "RAG?"}).status_code, 422
        )
        response = self.client.post(
            "/documents", headers=self.headers(), files={"file": ("rag.txt", b"RAG uses retrieved documents.")}
        )
        self.assertEqual(response.status_code, 201, response.text)
        document = response.json()
        self.assertEqual(document["mode"], "fixture")
        self.assertEqual(document["chunk_count"], 1)
        self.assertEqual(self.client.get("/documents").json()[0]["status"], "ready")
        chat = self.client.post(
            "/chat", headers=self.headers(), json={"question": "RAG uses retrieved documents."}
        )
        self.assertEqual(chat.status_code, 200, chat.text)
        self.assertIn("FIXTURE", chat.json()["answer"])
        self.assertEqual(chat.json()["sources"], ["rag.txt"])
        self.assertAlmostEqual(chat.json()["contexts"][0]["similarity"], 1, places=3)
        self.assertEqual(chat.json()["usage"]["source"], "unavailable")
        metrics = self.client.get("/metrics")
        self.assertEqual(metrics.status_code, 200)
        self.assertIn('insighthub_documents_total{status="ready"} 1.0', metrics.text)
        self.assertEqual(
            self.client.delete(f"/documents/{document['id']}", headers={"Idempotency-Key": "delete-e2e"}).status_code, 204
        )
        with db.get_conn() as conn:
            self.assertEqual(
                conn.execute("SELECT count(*) FROM chunks").fetchone()[0], 0
            )
        self.assertIn(
            'insighthub_documents_total{status="ready"} 0.0',
            self.client.get("/metrics").text,
        )

    def test_successful_retry_is_noop_and_conflicting_payload_is_409(self):
        document_id = self.create_document()
        first = process_document(document_id, "test.txt", b"hello world")
        with patch("app.services.ingestion.embed") as provider:
            self.assertEqual(
                process_document(document_id, "test.txt", b"hello world"), first
            )
            provider.assert_not_called()
        for filename, content in (
            ("test.txt", b"changed"),
            ("other.txt", b"hello world"),
        ):
            with self.assertRaises(DocumentConflict):
                process_document(document_id, filename, content)
        state = self.state(document_id)
        self.assertEqual((state[0], state[1], state[4]), ("ready", first, first))
        self.assertIsNotNone(state[2])

    def test_concurrent_successful_retries_call_provider_once(self):
        document_id = self.create_document()
        started, release = threading.Event(), threading.Event()

        def slow_embed(texts, input_type):
            started.set()
            self.assertTrue(release.wait(timeout=5))
            return _local_embed(texts, 1024)

        with patch("app.services.ingestion.embed", side_effect=slow_embed) as provider:
            with concurrent.futures.ThreadPoolExecutor(2) as executor:
                first = executor.submit(
                    process_document, document_id, "test.txt", b"same"
                )
                self.assertTrue(started.wait(timeout=3))
                second = executor.submit(
                    process_document, document_id, "test.txt", b"same"
                )
                release.set()
                self.assertEqual(first.result(timeout=5), second.result(timeout=5))
            self.assertEqual(provider.call_count, 1)
        self.assertEqual(self.state(document_id)[4], 1)

    def test_failed_attempt_and_concurrent_retry_end_ready(self):
        document_id = self.create_document()
        started, release = threading.Event(), threading.Event()
        calls = []

        def fail_once(texts, input_type):
            calls.append(True)
            if len(calls) == 1:
                started.set()
                release.wait(timeout=5)
                raise ProviderError()
            return _local_embed(texts, 1024)

        with patch("app.services.ingestion.embed", side_effect=fail_once):
            with concurrent.futures.ThreadPoolExecutor(2) as executor:
                first = executor.submit(
                    process_document, document_id, "test.txt", b"same"
                )
                self.assertTrue(started.wait(timeout=3))
                second = executor.submit(
                    process_document, document_id, "test.txt", b"same"
                )
                release.set()
                with self.assertRaises(ProviderError):
                    first.result(timeout=5)
                self.assertEqual(second.result(timeout=5), 1)
        self.assertEqual(self.state(document_id)[0], "ready")
        self.assertEqual(self.state(document_id)[4], 1)
        self.assertIsNone(self.state(document_id)[3])

    def test_failed_vectors_are_atomic_and_can_retry(self):
        document_id = self.create_document()
        for invalid in ([], [[float("nan")] * 1024], [[1.0] * 1023]):
            with (
                patch("app.services.ingestion.embed", return_value=invalid),
                self.assertRaises(ProviderError),
            ):
                process_document(document_id, "test.txt", b"content")
            state = self.state(document_id)
            self.assertEqual((state[0], state[1], state[4]), ("failed", 0, 0))
            self.assertEqual(state[3], "provider_error")
            with db.get_conn() as conn:
                self.assertEqual(
                    conn.execute("SELECT count(*) FROM embedding_index").fetchone()[0],
                    0,
                )
        self.assertEqual(process_document(document_id, "test.txt", b"content"), 1)

    def test_mid_insert_database_failure_rolls_back_all_chunks(self):
        document_id = self.create_document()
        with db.get_conn() as conn:
            conn.execute(
                "CREATE FUNCTION reject_second() RETURNS trigger LANGUAGE plpgsql AS $$ "
                "BEGIN IF NEW.chunk_index = 1 THEN RAISE EXCEPTION 'secret'; END IF; "
                "RETURN NEW; END $$"
            )
            conn.execute(
                "CREATE TRIGGER reject_second BEFORE INSERT ON chunks "
                "FOR EACH ROW EXECUTE FUNCTION reject_second()"
            )
        try:
            with configured(chunk_size=4, chunk_overlap=0):
                with self.assertRaises(Exception) as raised:
                    process_document(document_id, "test.txt", b"a b c d e f")
                self.assertNotIn("secret", str(raised.exception))
        finally:
            with db.get_conn() as conn:
                conn.execute("DROP TRIGGER reject_second ON chunks")
                conn.execute("DROP FUNCTION reject_second()")
        state = self.state(document_id)
        self.assertEqual((state[0], state[1], state[4]), ("failed", 0, 0))

    def test_empty_extracted_text_is_failed_and_422(self):
        response = self.client.post(
            "/documents", headers=self.headers(), files={"file": ("empty.txt", b" \n ")}
        )
        self.assertEqual(response.status_code, 422, response.text)
        document = self.client.get("/documents").json()[0]
        self.assertEqual(document["status"], "failed")
        self.assertEqual(document["chunk_count"], 0)

    def test_index_identity_change_rejects_query_upload_and_readiness(self):
        self.client.post("/documents", headers=self.headers(), files={"file": ("test.txt", b"content")})
        with (
            configured(embedding_revision="2"),
            patch("app.services.retrieval.embed") as provider,
        ):
            with self.assertRaises(IndexIdentityConflict):
                retrieve("question")
            provider.assert_not_called()
            response = self.client.post(
                "/documents", headers=self.headers(), files={"file": ("new.txt", b"new content")}
            )
            self.assertEqual(response.status_code, 409, response.text)
            self.assertEqual(self.client.get("/readyz").status_code, 503)
        with db.get_conn() as conn:
            self.assertEqual(
                conn.execute("SELECT count(*) FROM chunks").fetchone()[0], 1
            )

    def test_same_dimension_real_provider_cannot_query_fixture_index(self):
        self.client.post("/documents", headers=self.headers(), files={"file": ("test.txt", b"content")})
        with real_config(), patch("app.services.retrieval.embed") as provider:
            with self.assertRaises(IndexIdentityConflict):
                retrieve("question")
        provider.assert_not_called()

    def test_dimension_mismatch_is_rejected_before_provider(self):
        with configured(embedding_dim=768), db.get_conn() as conn:
            with self.assertRaises(SchemaMismatch):
                check_schema(conn)

    def test_real_gateway_full_pipeline_with_mock_http(self):
        def embedding_response(*args, **kwargs):
            return {
                "data": [
                    {"index": i, "embedding": [1.0] * 1024}
                    for i in range(len(kwargs["payload"]["input"]))
                ],
                "usage": {"prompt_tokens": 5},
            }

        with (
            real_config(),
            patch(
                "app.services.embeddings.post_json",
                side_effect=embedding_response,
            ),
            patch(
                "app.services.llm.post_json",
                return_value={
                    "choices": [
                        {"message": {"content": '{"status":"Answered","claims":[{"text":"Supported answer","citation_ids":["chunk:1"]}]}'}}
                    ],
                    "usage": {"prompt_tokens": 12, "completion_tokens": 8},
                },
            ),
        ):
            upload = self.client.post(
                "/documents", headers=self.headers(), files={"file": ("real.txt", b"content")}
            )
            self.assertEqual(upload.status_code, 201, upload.text)
            chat = self.client.post("/chat", headers=self.headers(), json={"question": "question"})
            self.assertEqual(chat.status_code, 200, chat.text)
            self.assertEqual(chat.json()["mode"], "real")
            self.assertEqual(chat.json()["usage"]["input_tokens"], 12)
            self.assertEqual(chat.json()["usage"]["source"], "provider")

    def test_provider_failure_is_502_and_metadata_truthful(self):
        with (
            real_config(),
            patch("app.services.embeddings.post_json", side_effect=ProviderError()),
        ):
            response = self.client.post(
                "/documents", headers=self.headers(), files={"file": ("real.txt", b"content")}
            )
        self.assertEqual(response.status_code, 502, response.text)
        document = self.client.get("/documents").json()[0]
        self.assertEqual(
            (document["status"], document["chunk_count"], document["error_code"]),
            ("failed", 0, "provider_error"),
        )

    def test_upload_idempotency_conflict_and_content_deduplication(self):
        headers = {"Idempotency-Key": "same-upload-key"}
        first = self.client.post("/documents", headers=headers, files={"file": ("same.txt", b"same bytes")})
        replay = self.client.post("/documents", headers=headers, files={"file": ("same.txt", b"same bytes")})
        conflict = self.client.post("/documents", headers=headers, files={"file": ("same.txt", b"different")})
        duplicate = self.client.post(
            "/documents", headers={"Idempotency-Key": "different-key"},
            files={"file": ("renamed.txt", b"same bytes")},
        )
        self.assertEqual((first.status_code, replay.status_code, conflict.status_code, duplicate.status_code), (201, 201, 409, 201))
        self.assertEqual(first.json()["id"], replay.json()["id"])
        self.assertEqual(first.json()["id"], duplicate.json()["id"])
        self.assertTrue(duplicate.json()["deduplicated"])
        self.assertEqual(len(self.client.get("/documents").json()), 1)
        operation = self.client.get("/operations/upload/same-upload-key")
        self.assertEqual(operation.status_code, 200)
        self.assertEqual(operation.json()["response"]["id"], first.json()["id"])
        retry_ready = self.client.post(
            f"/documents/{first.json()['id']}/retry",
            headers={"Idempotency-Key": "retry-ready"},
            files={"file": ("same.txt", b"same bytes")},
        )
        self.assertEqual(retry_ready.status_code, 409)

    def test_evidence_gate_returns_no_evidence_without_llm_call(self):
        document = self.client.post(
            "/documents",
            headers=self.headers(),
            files={"file": ("evidence.txt", b"Only release procedures are documented.")},
        ).json()
        with (
            configured(retrieval_min_similarity=1.0),
            patch("app.routers.chat.generate") as generate,
        ):
            response = self.client.post(
                "/chat",
                headers=self.headers(),
                json={
                    "question": "What is the weather tomorrow?",
                    "document_ids": [document["id"]],
                },
            )
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["status"], "NoEvidence")
        self.assertEqual(response.json()["retrieval"]["context_count"], 0)
        generate.assert_not_called()

    def test_delete_is_idempotent_and_reconciled(self):
        first = self.client.post(
            "/documents", headers=self.headers(), files={"file": ("one.txt", b"one")}
        ).json()
        second = self.client.post(
            "/documents", headers=self.headers(), files={"file": ("two.txt", b"two")}
        ).json()
        headers = {"Idempotency-Key": "delete-replay"}
        original = self.client.delete(f"/documents/{first['id']}", headers=headers)
        replay = self.client.delete(f"/documents/{first['id']}", headers=headers)
        conflict = self.client.delete(f"/documents/{second['id']}", headers=headers)
        self.assertEqual((original.status_code, replay.status_code, conflict.status_code), (204, 204, 409))
        operation = self.client.get("/operations/delete/delete-replay").json()
        self.assertEqual(operation["status"], "succeeded")
        self.assertEqual(operation["response"]["document_id"], first["id"])

    def test_delete_waits_until_chat_result_is_committed(self):
        document = self.client.post(
            "/documents", headers=self.headers(), files={"file": ("lock.txt", b"lock evidence")}
        ).json()
        started, release = threading.Event(), threading.Event()

        def blocked_generate(_question, contexts):
            started.set()
            release.wait(timeout=5)
            return {
                "status": "Answered",
                "answer": "supported",
                "claims": [{"text": "supported", "citation_ids": [contexts[0]["context_id"]]}],
                "citation_ids": [contexts[0]["context_id"]],
                "sources": [contexts[0]["source"]],
                "mode": "fixture",
                "provider": "fixture",
                "model": "extractive-fixture-v1",
                "prompt_version": "test",
                "usage": {"input_tokens": None, "output_tokens": None, "source": "unavailable"},
            }

        with patch("app.routers.chat.generate", side_effect=blocked_generate):
            with concurrent.futures.ThreadPoolExecutor(2) as executor:
                chat = executor.submit(
                    self.client.post,
                    "/chat",
                    headers={"Idempotency-Key": "chat-lock"},
                    json={"question": "lock", "document_ids": [document["id"]]},
                )
                self.assertTrue(started.wait(timeout=3))
                delete = executor.submit(
                    self.client.delete,
                    f"/documents/{document['id']}",
                    headers={"Idempotency-Key": "delete-lock"},
                )
                self.assertFalse(delete.done())
                release.set()
                self.assertEqual(chat.result(timeout=5).status_code, 200)
                self.assertEqual(delete.result(timeout=5).status_code, 204)

    def test_expired_operation_key_can_be_reused(self):
        with db.get_conn() as conn:
            conn.execute(
                "INSERT INTO operation_records(operation_type,operation_key,request_fingerprint,status,expires_at) "
                "VALUES ('upload','expired-key','old','failed',now() - interval '1 minute')"
            )
        response = self.client.post(
            "/documents",
            headers={"Idempotency-Key": "expired-key"},
            files={"file": ("fresh.txt", b"fresh")},
        )
        self.assertEqual(response.status_code, 201, response.text)
        with db.get_conn() as conn:
            self.assertEqual(
                conn.execute(
                    "SELECT count(*) FROM operation_records WHERE operation_type='upload' AND operation_key='expired-key'"
                ).fetchone()[0],
                1,
            )

    def test_document_list_has_stable_cursor_pagination(self):
        for index in range(3):
            self.client.post(
                "/documents", headers=self.headers(),
                files={"file": (f"page-{index}.txt", f"content-{index}".encode())},
            )
        first = self.client.get("/documents?limit=2")
        self.assertEqual(len(first.json()), 2)
        cursor = first.headers.get("X-Next-Cursor")
        self.assertIsNotNone(cursor)
        second = self.client.get(f"/documents?limit=2&after_id={cursor}")
        self.assertEqual(len(second.json()), 1)
        self.assertTrue(set(item["id"] for item in first.json()).isdisjoint(item["id"] for item in second.json()))

    def test_startup_recovery_fences_interrupted_attempt_and_operation(self):
        document_id = self.create_document()
        with db.get_conn() as conn:
            conn.execute(
                "INSERT INTO ingestion_attempts(document_id,operation_key,request_fingerprint,status,deadline_at) "
                "VALUES (%s,'crashed','fingerprint','processing',now() + interval '1 minute')",
                (document_id,),
            )
            conn.execute(
                "INSERT INTO operation_records(operation_type,operation_key,request_fingerprint,status) "
                "VALUES ('upload','crashed','fingerprint','processing')"
            )
            recover_interrupted_operations(conn)
        with db.get_conn() as conn:
            self.assertEqual(conn.execute("SELECT status,error_code FROM documents WHERE id=%s", (document_id,)).fetchone(), ("failed", "interrupted"))
            self.assertEqual(conn.execute("SELECT status,error_code FROM ingestion_attempts").fetchone(), ("failed", "interrupted"))
            self.assertEqual(conn.execute("SELECT status,error_code,http_status FROM operation_records").fetchone(), ("failed", "interrupted", 500))

    def test_forward_migration_preserves_legacy_document_and_chunk(self):
        schema = "migration_" + uuid.uuid4().hex
        legacy = (Path(__file__).with_name("legacy_schema.sql")).read_text()
        with psycopg.connect(self.dsn, autocommit=True) as admin:
            admin.execute(sql.SQL("CREATE SCHEMA {}").format(sql.Identifier(schema)))
        try:
            with psycopg.connect(self.dsn, options=f"-csearch_path={schema},public") as conn:
                conn.execute(legacy)
                identity = get_settings().embedding_identity_id
                conn.execute(
                    "INSERT INTO embedding_index(singleton,identity_id,identity,dimension) VALUES(TRUE,%s,%s,1024)",
                    (identity, Jsonb(get_settings().embedding_identity)),
                )
                document_id = conn.execute(
                    "INSERT INTO documents(filename,status,chunk_count,content_sha256,pipeline_id,embedding_identity_id) "
                    "VALUES('legacy.txt','ready',1,'sha','pipeline',%s) RETURNING id", (identity,),
                ).fetchone()[0]
                vector = "[" + ",".join(["1"] + ["0"] * 1023) + "]"
                conn.execute(
                    "INSERT INTO chunks(document_id,chunk_index,chunk_text,embedding,embedding_identity_id) "
                    "VALUES(%s,0,'legacy content',%s::vector,%s)", (document_id, vector, identity),
                )
                run_migrations(conn)
                self.assertEqual(conn.execute("SELECT filename,status,chunk_count FROM documents").fetchone(), ("legacy.txt", "ready", 1))
                self.assertEqual(conn.execute("SELECT chunk_text FROM chunks").fetchone()[0], "legacy content")
                self.assertIsNotNone(conn.execute("SELECT to_regclass('document_sources')").fetchone()[0])
        finally:
            with psycopg.connect(self.dsn, autocommit=True) as admin:
                admin.execute(sql.SQL("DROP SCHEMA {} CASCADE").format(sql.Identifier(schema)))

    def test_failed_document_retry_preserves_attempt_history_and_source(self):
        with patch("app.services.ingestion.embed", side_effect=ProviderError()):
            failed = self.client.post(
                "/documents", headers={"Idempotency-Key": "failed-upload"},
                files={"file": ("retry.md", b"# Heading\n\nRetry content")},
            )
        self.assertEqual(failed.status_code, 502, failed.text)
        document_id = failed.json()["document_id"]
        retried = self.client.post(
            f"/documents/{document_id}/retry", headers={"Idempotency-Key": "retry-once"},
            files={"file": ("retry.md", b"# Heading\n\nRetry content")},
        )
        self.assertEqual(retried.status_code, 200, retried.text)
        detail = self.client.get(f"/documents/{document_id}").json()
        self.assertEqual(detail["status"], "ready")
        self.assertEqual([item["status"] for item in detail["attempts"]], ["succeeded", "failed"])
        self.assertEqual(detail["attempts"][0]["previous_attempt_id"], detail["attempts"][1]["id"])
        with db.get_conn() as conn:
            segment_id = conn.execute("SELECT id FROM source_segments WHERE document_id=%s", (document_id,)).fetchone()[0]
        source = self.client.get(f"/documents/{document_id}/source?segment_id={segment_id}")
        self.assertEqual(source.status_code, 200)
        self.assertIn("Retry content", source.json()["content"])

    def test_chat_source_scope_and_idempotent_replay(self):
        first = self.client.post("/documents", headers=self.headers(), files={"file": ("one.txt", b"alpha source")}).json()
        second = self.client.post("/documents", headers=self.headers(), files={"file": ("two.txt", b"beta source")}).json()
        headers = {"Idempotency-Key": "chat-replay"}
        payload = {"question": "alpha source", "document_ids": [first["id"]]}
        answer = self.client.post("/chat", headers=headers, json=payload)
        replay = self.client.post("/chat", headers=headers, json=payload)
        conflict = self.client.post("/chat", headers=headers, json={"question": "other", "document_ids": [second["id"]]})
        self.assertEqual((answer.status_code, replay.status_code, conflict.status_code), (200, 200, 409))
        self.assertEqual(answer.json(), replay.json())
        self.assertEqual({item["document_id"] for item in answer.json()["contexts"]}, {first["id"]})
        self.assertEqual(answer.json()["citations"][0]["document_id"], first["id"])
