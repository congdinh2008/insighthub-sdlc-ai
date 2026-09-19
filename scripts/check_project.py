"""Check standalone release consistency without Docker or external credentials."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / 'starter.manifest.json').read_text())
    version = manifest['version']
    package = json.loads((ROOT / 'web/package.json').read_text())
    lock = json.loads((ROOT / 'web/package-lock.json').read_text())
    sbom = json.loads((ROOT / 'docs/release/SBOM.cdx.json').read_text())
    assert package['version'] == lock['version'] == lock['packages']['']['version'] == sbom['metadata']['component']['version'] == version, 'Version drift'
    assert (ROOT / 'api/app/main.py').read_text().count('"' + version + '"') == 2, 'API version drift'
    assert version in (ROOT / 'README.md').read_text(), 'README version drift'
    assert version in (ROOT / 'docs/release/Starter_Readiness_v1.0.0.md').read_text(), 'Readiness version drift'
    srs = ROOT / 'requirements/SRS_InsightHub_v2.4.md'
    parent = ROOT.parent / '04_Requirements/SRS_InsightHub_v2.4.md'
    if parent.exists():
        assert srs.read_bytes() == parent.read_bytes(), 'SRS snapshot differs from authoring source'
    mapping = (ROOT / 'docs/learner/02_SRS_Assignment_Map.md').read_text()
    requirements = set(re.findall(r'\| `?(IH-[A-Z]+-\d{3})`? \|', srs.read_text()))
    acceptance = set(re.findall(r'IH-[A-Z]+-\d{3}-AC\d{2}', srs.read_text()))
    mapped = set(re.findall(r'\| `?(IH-[A-Z]+-\d{3})`? \|', mapping))
    assert requirements == mapped and len(requirements) == 72, 'Incomplete requirement mapping'
    assert acceptance <= set(re.findall(r'IH-[A-Z]+-\d{3}-AC\d{2}', mapping)) and len(acceptance) == 163, 'Incomplete AC mapping'
    broken = []
    markdown = list(ROOT.glob('*.md')) + list((ROOT / 'docs').rglob('*.md')) + list((ROOT / 'evaluation').glob('*.md'))
    for path in markdown:
        if 'archive' in path.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            target = target.strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            relative = unquote(target.split('#')[0])
            if relative and (Path(relative).is_absolute() or not (path.parent / relative).exists()):
                broken.append(f'{path.relative_to(ROOT)}: {target}')
    assert not broken, 'Nonportable/broken links: ' + '; '.join(broken)
    print(f'PASS: {version}; 72 requirements / 163 AC; portable links; SRS sha256={hashlib.sha256(srs.read_bytes()).hexdigest()}')


if __name__ == '__main__':
    main()
