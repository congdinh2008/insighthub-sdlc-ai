"""Build a traceable student starter archive from the current working tree."""

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DELIVERY = json.loads((ROOT / "starter.manifest.json").read_text())
VERSION = DELIVERY["version"]
PREFIX = f"insighthub-starter-v{VERSION}-docs{DELIVERY['documentation_revision']}"
ARCHIVE = DIST / f"{PREFIX}.zip"
SRS_SOURCE = ROOT / DELIVERY["requirements_baseline"]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def source_files() -> list[Path]:
    names = git_output("ls-files", "--cached", "--others", "--exclude-standard").splitlines()
    excluded = ("dist/", "docs/archive/", "reports/")
    return [ROOT / name for name in sorted(names) if name and name != "PACKAGE_MANIFEST.json" and not name.startswith(excluded)]


def main():
    if not SRS_SOURCE.is_file():
        raise SystemExit(f"Missing SRS baseline: {SRS_SOURCE}")
    if git_output("status", "--porcelain"):
        raise SystemExit("Commit the reviewed changes before creating a release archive.")
    DIST.mkdir(exist_ok=True)
    entries: dict[str, bytes] = {}
    for path in source_files():
        if path.is_file():
            entries[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    manifest = {
        "schema_version": 1,
        "package": "InsightHub Starter",
        "version": VERSION,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_commit": git_output("rev-parse", "HEAD"),
        "working_tree_dirty": bool(git_output("status", "--porcelain")),
        "requirements": {
            "path": DELIVERY["requirements_baseline"],
            "source_repository_path": DELIVERY["requirements_source"],
            "sha256": sha256(entries[DELIVERY["requirements_baseline"]]),
        },
        "documentation_revision": DELIVERY["documentation_revision"],
        "files": {name: sha256(data) for name, data in sorted(entries.items())},
    }
    entries["PACKAGE_MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(f"{PREFIX}/{name}", date_time=(2026, 9, 19, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    digest = sha256(ARCHIVE.read_bytes())
    ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256").write_text(f"{digest}  {ARCHIVE.name}\n")
    print(ARCHIVE)
    print(f"sha256={digest}")


if __name__ == "__main__":
    main()
