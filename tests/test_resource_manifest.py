"""Offline regression tests for malformed resource metadata and CLI behavior."""
import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "validate_resource_manifest.py"


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.data = yaml.safe_load((ROOT / "data/manifests/public-resources.yaml").read_text())

    def run_manifest(self, text):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "manifest.yaml"
            path.write_text(text, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                  capture_output=True, text=True, cwd=folder)

    def test_repository_manifest(self):
        result = self.run_manifest(yaml.safe_dump(self.data))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("10 resources validated", result.stdout)

    def test_invalid_metadata(self):
        cases = [
            ("schema_version", True),
            ("snapshot_date", "2026-02-30"),
            ("snapshot_date", "20260921"),
            ("snapshot_date", "yesterday"),
            ("resources", []),
            ("resources", self.data["resources"] * 2),
        ]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(self.data)
                data[key] = value
                self.assert_invalid(data)

    def test_invalid_resource_fields(self):
        cases = [
            ("id", " "), ("platform", []), ("platform", "unknown"),
            ("type", "unknown"), ("owner", ""), ("license", None),
            ("url", "http://huggingface.co/fosters/test"),
            ("url", "https://[broken/fosters/test"),
            ("url", "https://example.org/fosters/test"),
            ("url", "https://user@huggingface.co/fosters/test"),
            ("metrics", {"rows": -1}), ("metrics", {"rows": True}),
            ("metrics", {"rows": float("nan")}),
            ("metrics", {"rows": float("inf")}),
        ]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                data = copy.deepcopy(self.data)
                data["resources"][0][key] = value
                self.assert_invalid(data)

    def assert_invalid(self, data):
        result = self.run_manifest(yaml.safe_dump(data))
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("ERROR:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_malformed_yaml(self):
        result = self.run_manifest("resources: [")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            result = subprocess.run([sys.executable, str(SCRIPT), str(Path(folder) / "missing")],
                                    capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
