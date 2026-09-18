"""Verify archive paths, required content, forbidden files and every manifest hash."""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", nargs="?")
    args = parser.parse_args()
    archive_path = Path(args.archive) if args.archive else max((ROOT / "dist").glob("*.zip"), key=lambda p: p.stat().st_mtime)
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        for name in names:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts:
                raise SystemExit(f"Unsafe archive path: {name}")
            lowered = name.lower()
            if any(part in {".git", "node_modules", ".next", "__pycache__"} for part in path.parts):
                raise SystemExit(f"Forbidden directory: {name}")
            if path.name in {".env", ".env.local"} or path.suffix in {".pem", ".key"}:
                raise SystemExit(f"Forbidden secret file: {name}")
        manifest_name = next((name for name in names if name.endswith("/PACKAGE_MANIFEST.json")), None)
        if manifest_name is None:
            raise SystemExit("PACKAGE_MANIFEST.json is missing")
        prefix = manifest_name.removesuffix("PACKAGE_MANIFEST.json")
        manifest = json.loads(archive.read(manifest_name))
        for required in ("README.md", "GETTING_STARTED.md", "docker-compose.yml", "requirements/SRS_InsightHub_v2.4.md"):
            if prefix + required not in names:
                raise SystemExit(f"Required file is missing: {required}")
        for relative, expected in manifest["files"].items():
            actual = sha256(archive.read(prefix + relative))
            if actual != expected:
                raise SystemExit(f"Checksum mismatch: {relative}")
        srs_path = manifest["requirements"]["path"]
        if sha256(archive.read(prefix + srs_path)) != manifest["requirements"]["sha256"]:
            raise SystemExit("SRS checksum mismatch")
    checksum_file = archive_path.with_suffix(archive_path.suffix + ".sha256")
    if not checksum_file.is_file() or not checksum_file.read_text().startswith(sha256(archive_path.read_bytes())):
        raise SystemExit("Archive checksum file is missing or invalid")
    print(f"PASS: {archive_path}")


if __name__ == "__main__":
    main()
