"""Delivery regression checks use a clean local repository, without services."""
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed_dir = tempfile.TemporaryDirectory(prefix='insighthub-delivery-seed-')
        cls.seed = Path(cls.seed_dir.name)
        names = subprocess.check_output(
            ['git', 'ls-files', '--cached', '--others', '--exclude-standard'],
            cwd=ROOT, text=True).splitlines()
        for name in names:
            source = ROOT / name
            if source.is_file() and not name.startswith(('dist/', 'reports/')):
                target = cls.seed / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        for args in [('init', '-q'), ('add', '.'),
                     ('-c', 'user.name=Delivery Test', '-c', 'user.email=delivery@example.invalid',
                      'commit', '-qm', 'test delivery input')]:
            subprocess.run(['git', *args], cwd=cls.seed, check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.seed_dir.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='insighthub-delivery-test-')
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo'
        subprocess.run(['git', 'clone', '-q', '--shared', str(self.seed), str(self.repo)],
                       check=True, capture_output=True)
        self.delivery = json.loads((self.repo / 'starter.manifest.json').read_text())

    def run_script(self, name, *args, ok=True):
        result = subprocess.run([sys.executable, f'scripts/{name}.py', *args],
                                cwd=self.repo, capture_output=True, text=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def package(self):
        self.run_script('package_starter')
        return next((self.repo / 'dist').glob('*.zip'))

    def rewrite_package(self, archive, mutate):
        with zipfile.ZipFile(archive) as z:
            entries = {name: z.read(name) for name in z.namelist()}
        mutate(entries)
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
            for name, data in entries.items():
                z.writestr(name, data)
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        archive.with_suffix('.zip.sha256').write_text(f'{digest}  {archive.name}\n')

    def test_clean_delivery_contains_current_docs_and_excludes_archive(self):
        self.run_script('check_project')
        archive = self.package()
        self.run_script('verify_package', str(archive))
        with zipfile.ZipFile(archive) as z:
            names = z.namelist()
            self.assertFalse(any('/archive/' in name for name in names))
            self.assertFalse(any(name.endswith('/START_HERE.md') for name in names))
            receipt = next(name for name in names if name.endswith('/PACKAGE_MANIFEST.json'))
            prefix = receipt.removesuffix('PACKAGE_MANIFEST.json')
            self.assertTrue(all(prefix + self.delivery[key] in names for key in
                                ('requirements_baseline', 'learner_requirements', 'api_schema_reference')))
            extracted = Path(self.temp.name) / 'extracted'
            z.extractall(extracted)
        result = subprocess.run([sys.executable, 'scripts/check_project.py'],
                                cwd=extracted / prefix, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_scope_change_is_rejected(self):
        path = self.repo / self.delivery['learner_requirements']
        text = path.read_text()
        self.assertIn('| IH-AUTH-001-AC01 | A |', text)
        path.write_text(text.replace('| IH-AUTH-001-AC01 | A |', '| IH-AUTH-001-AC01 | N |', 1))
        result = self.run_script('check_project', ok=False)
        self.assertIn('Assignment scope drift', result.stderr)

    def test_reference_srs_hash_mismatch_is_rejected(self):
        path = self.repo / self.delivery['requirements_baseline']
        path.write_text(path.read_text() + '\n')
        result = self.run_script('check_project', ok=False)
        self.assertIn('Reference SRS hash drift', result.stderr)

    def test_dirty_source_cannot_be_packaged(self):
        with (self.repo / 'README.md').open('a') as file:
            file.write('\nUncommitted edit\n')
        result = self.run_script('package_starter', ok=False)
        self.assertIn('Commit the reviewed changes', result.stderr)

    def test_missing_learner_file_is_rejected_even_with_updated_file_list(self):
        archive = self.package()
        def mutate(entries):
            receipt = next(n for n in entries if n.endswith('/PACKAGE_MANIFEST.json'))
            prefix = receipt.removesuffix('PACKAGE_MANIFEST.json')
            relative = self.delivery['learner_requirements']
            del entries[prefix + relative]
            manifest = json.loads(entries[receipt])
            del manifest['files'][relative]
            entries[receipt] = json.dumps(manifest).encode()
        self.rewrite_package(archive, mutate)
        result = self.run_script('verify_package', str(archive), ok=False)
        self.assertIn('Required file is missing', result.stderr)

    def test_changed_nested_contract_is_rejected_even_with_valid_outer_hashes(self):
        archive = self.package()
        def mutate(entries):
            receipt = next(n for n in entries if n.endswith('/PACKAGE_MANIFEST.json'))
            prefix = receipt.removesuffix('PACKAGE_MANIFEST.json')
            relative = self.delivery['api_schema_reference']
            with zipfile.ZipFile(io.BytesIO(entries[prefix + relative])) as z:
                nested = {n: z.read(n) for n in z.namelist()}
            nested['API_Schema_Reference/schemas.json'] += b'\n'
            output = io.BytesIO()
            with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
                for n, data in nested.items():
                    z.writestr(n, data)
            entries[prefix + relative] = output.getvalue()
            manifest = json.loads(entries[receipt])
            manifest['files'][relative] = hashlib.sha256(output.getvalue()).hexdigest()
            entries[receipt] = json.dumps(manifest).encode()
        self.rewrite_package(archive, mutate)
        result = self.run_script('verify_package', str(archive), ok=False)
        self.assertIn('API/schema reference checksum mismatch', result.stderr)


if __name__ == '__main__':
    unittest.main()
