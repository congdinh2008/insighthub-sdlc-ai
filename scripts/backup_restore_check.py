"""Create a PostgreSQL backup and verify it in an isolated temporary database."""

import argparse
import hashlib
import json
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = (
    "schema_migrations",
    "embedding_index",
    "documents",
    "document_sources",
    "source_segments",
    "chunks",
    "ingestion_attempts",
    "operation_records",
)


def run(command: list[str], *, capture=False):
    return subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        capture_output=capture,
        text=capture,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--env-file", default=".env.example")
    parser.add_argument("--output-dir", default="reports/backup-restore")
    args = parser.parse_args()
    compose = ["docker", "compose", "--env-file", args.env_file, "-p", args.project]
    suffix = uuid.uuid4().hex[:12]
    restore_database = "insighthub_restore_" + suffix
    container_dump = f"/tmp/insighthub-{suffix}.dump"
    output_dir = ROOT / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    local_dump = output_dir / f"insighthub-{suffix}.dump"
    report_path = output_dir / f"backup-restore-{suffix}.json"
    sql = " UNION ALL ".join(
        f"SELECT '{table}', count(*)::text FROM {table}" for table in TABLES
    ) + " ORDER BY 1"

    def counts(database: str):
        result = run(
            compose + ["exec", "-T", "postgres", "psql", "-U", "insighthub", "-d", database, "-At", "-F", "=", "-c", sql],
            capture=True,
        )
        return dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line)

    try:
        source_counts = counts("insighthub")
        run(compose + ["exec", "-T", "postgres", "pg_dump", "-U", "insighthub", "-d", "insighthub", "-Fc", "-f", container_dump])
        run(compose + ["cp", f"postgres:{container_dump}", str(local_dump)])
        run(compose + ["exec", "-T", "postgres", "createdb", "-U", "insighthub", restore_database])
        run(compose + ["exec", "-T", "postgres", "pg_restore", "-U", "insighthub", "-d", restore_database, container_dump])
        restored_counts = counts(restore_database)
        artifact = {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "compose_project": args.project,
            "backup_sha256": hashlib.sha256(local_dump.read_bytes()).hexdigest(),
            "source_counts": source_counts,
            "restored_counts": restored_counts,
            "passed": source_counts == restored_counts and set(source_counts) == set(TABLES),
        }
        report_path.write_text(json.dumps(artifact, indent=2) + "\n")
        print(report_path)
        print("PASS" if artifact["passed"] else "FAIL")
        if not artifact["passed"]:
            raise SystemExit(1)
    finally:
        subprocess.run(compose + ["exec", "-T", "postgres", "dropdb", "-U", "insighthub", "--if-exists", restore_database], cwd=ROOT)
        subprocess.run(compose + ["exec", "-T", "postgres", "rm", "-f", container_dump], cwd=ROOT)


if __name__ == "__main__":
    main()
