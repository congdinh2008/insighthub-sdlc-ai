"""Verify archive paths, required content, forbidden files and every manifest hash."""

import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = {
    "private key": re.compile(("-----BEGIN " + r"[A-Z ]*" + "PRIVATE KEY-----").encode()),
    "Google API key": re.compile(rb"AIza[0-9A-Za-z_-]{30,}"),
    "OpenAI-style API key": re.compile(rb"sk-[0-9A-Za-z_-]{20,}"),
    "Slack token": re.compile(rb"xox[baprs]-[0-9A-Za-z-]{20,}"),
    "AWS access key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "GitHub token": re.compile(rb"(?:gh[pousr]_[0-9A-Za-z]{30,}|github_pat_[0-9A-Za-z_]{40,})"),
}


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
        if manifest.get("working_tree_dirty"):
            raise SystemExit("Release archive must be created from a clean working tree")
        required_files = (
            "README.md",
            "GETTING_STARTED.md",
            "docker-compose.yml",
            "docs/Model_Profiles_And_Reranking.md",
            "docs/Runbook_Starter_v1.md",
            "docs/release/SBOM.cdx.json",
            "evaluation/AEV-01.json",
            "scripts/run_aev.py",
            "scripts/check_project.py",
            "scripts/backup_restore_check.py",
            "api/migrations/002_operation_deadlines.sql",
            "starter.manifest.json",
        )
        delivery = json.loads(archive.read(prefix + 'starter.manifest.json'))
        required_files += tuple(delivery[key] for key in ('requirements_baseline', 'learner_requirements', 'api_schema_reference'))
        if manifest['requirements']['path'] != delivery['requirements_baseline']:
            raise SystemExit('Package SRS path differs from delivery metadata')
        if manifest.get('documentation_revision') != delivery['documentation_revision']:
            raise SystemExit('Documentation revision mismatch')
        for required in required_files:
            if prefix + required not in names:
                raise SystemExit(f"Required file is missing: {required}")
        expected_names = {prefix + relative for relative in manifest["files"]}
        expected_names.add(manifest_name)
        if set(names) != expected_names:
            raise SystemExit("Archive file list does not match manifest")
        for relative, expected in manifest["files"].items():
            if 'archive' in PurePosixPath(relative).parts:
                raise SystemExit(f'Archived content must not be delivered: {relative}')
            payload = archive.read(prefix + relative)
            actual = sha256(payload)
            if actual != expected:
                raise SystemExit(f"Checksum mismatch: {relative}")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(payload):
                    raise SystemExit(f"Possible {label} found in: {relative}")
            if relative == delivery['api_schema_reference']:
                with zipfile.ZipFile(io.BytesIO(payload)) as reference:
                    reference_manifest = json.loads(reference.read('API_Schema_Reference/Manifest_Reference.json'))
                    if reference_manifest['srs']['sha256'] != manifest['requirements']['sha256']:
                        raise SystemExit('API/schema reference SRS hash mismatch')
                    if reference_manifest['srs']['path'] != '../' + PurePosixPath(delivery['requirements_baseline']).name:
                        raise SystemExit('API/schema reference SRS path mismatch')
                    expected_reference = {'API_Schema_Reference/Manifest_Reference.json'}
                    for item in reference_manifest['contract_files']:
                        name = 'API_Schema_Reference/' + item['path']
                        if sha256(reference.read(name)) != item['sha256']:
                            raise SystemExit(f'API/schema reference checksum mismatch: {name}')
                        expected_reference.add(name)
                    if set(reference.namelist()) != expected_reference:
                        raise SystemExit('API/schema reference file list mismatch')
                    for member in reference.namelist():
                        member_path = PurePosixPath(member)
                        if member_path.is_absolute() or '..' in member_path.parts:
                            raise SystemExit(f'Unsafe reference path: {member}')
                        for label, pattern in SECRET_PATTERNS.items():
                            if pattern.search(reference.read(member)):
                                raise SystemExit(f'Possible {label} found in reference: {member}')
        srs_path = manifest["requirements"]["path"]
        if sha256(archive.read(prefix + srs_path)) != manifest["requirements"]["sha256"]:
            raise SystemExit("SRS checksum mismatch")
        sbom = json.loads(archive.read(prefix + "docs/release/SBOM.cdx.json"))
        if sbom.get("bomFormat") != "CycloneDX" or not sbom.get("components"):
            raise SystemExit("CycloneDX SBOM is missing or empty")
        versions = [manifest['version'], sbom['metadata']['component']['version']]
        for item in ('starter.manifest.json', 'web/package.json', 'web/package-lock.json'):
            versions.append(json.loads(archive.read(prefix + item))['version'])
        if len(set(versions)) != 1:
            raise SystemExit('Archive version mismatch')
    checksum_file = archive_path.with_suffix(archive_path.suffix + ".sha256")
    if not checksum_file.is_file() or not checksum_file.read_text().startswith(sha256(archive_path.read_bytes())):
        raise SystemExit("Archive checksum file is missing or invalid")
    print(f"PASS: {archive_path}")


if __name__ == "__main__":
    main()
