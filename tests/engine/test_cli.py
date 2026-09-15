"""Tests for the Reference Engine CLI and the engine version record."""

import io
import json
import re
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine import cli  # noqa: E402
from engine.scope_gate import ENGINE_VERSION  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def run_cli(*args):
    out = io.StringIO()
    with redirect_stdout(out), redirect_stderr(io.StringIO()):
        code = cli.main(list(args))
    return code, out.getvalue()


class CliTest(unittest.TestCase):
    def test_cli_valid_record(self):
        code, out = run_cli("check", str(FIXTURES / "openai-held.json"))
        result = json.loads(out)
        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "VALID")
        self.assertEqual(result["engine_version"], ENGINE_VERSION)
        self.assertEqual(result["separate_considerations"], ["e2"])

    def test_cli_rejects_mixed_citations(self):
        code, out = run_cli("check", str(FIXTURES / "openai-mixed-break.json"))
        self.assertEqual(code, 1)
        self.assertIn("R2_VERDICT_EVIDENCE_MUST_BE_IN_SCOPE", json.loads(out)["violations"])

    def test_cli_output_is_deterministic(self):
        path = str(FIXTURES / "openai-mixed-break.json")
        self.assertEqual(run_cli("check", path), run_cli("check", path))

    def test_cli_unreadable_record(self):
        code, out = run_cli("check", str(FIXTURES / "missing.json"))
        self.assertEqual(code, 2)
        self.assertEqual(out, "")

    def test_package_version_matches_engine(self):
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        match = re.search(r'^version = "([^"]+)"', pyproject, flags=re.MULTILINE)
        self.assertEqual(match.group(1), ENGINE_VERSION)


if __name__ == "__main__":
    unittest.main()
