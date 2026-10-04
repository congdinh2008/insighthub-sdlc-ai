import csv
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import trace_check  # noqa: E402
import trace_sample  # noqa: E402
from trace_lib import TRACE, read_rows, requirement_scopes, write_rows  # noqa: E402


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.fields, self.rows = read_rows(TRACE)
        self.scopes = requirement_scopes()

    def row(self, ac):
        return next(r for r in self.rows if r["ac_id"] == ac)

    def errors(self, gate=None):
        return trace_check.check(self.rows, self.fields, self.scopes, gate)[0]

    def test_skeleton_is_consistent(self):
        self.assertEqual(len(self.rows), 165)
        self.assertEqual(self.errors(), [])
        applied = [r for r in self.rows if r["scope"] != "N"]
        self.assertEqual(len(applied), 153)
        self.assertEqual({k: sum(r["risk"] == k for r in applied) for k in ("R1", "R2", "R3")}, {"R1": 63, "R2": 77, "R3": 13})

    def test_auth_tiers_follow_decision(self):
        auth = [r for r in self.rows if r["group"] == "AUTH"]
        # Requirements 1.2: đăng nhập Google và liên kết danh tính là Extended (quyết định 04/10/2026).
        self.assertEqual(sum(r["tier"] == "Core" for r in auth), 12)
        self.assertEqual(self.row("IH-AUTH-003-AC02")["tier"], "Extended")
        for ac in ("IH-AUTH-004-AC01", "IH-AUTH-004-AC02", "IH-AUTH-005-AC02"):
            self.assertEqual(self.row(ac)["tier"], "Extended")

    def test_core_list_is_published(self):
        applied = [r for r in self.rows if r["scope"] != "N"]
        self.assertEqual(sum(r["tier"] == "Core" for r in applied), 106)
        self.assertEqual(sum(r["tier"] == "Extended" for r in applied), 47)
        self.assertFalse(any(r["tier"] == "Pending" for r in applied))
        self.assertTrue(all(r["tier"] == "Extended" for r in applied if r["group"] == "NOTE"))
        self.assertEqual(self.row("IH-QUIZ-002-AC01")["tier"], "Core")
        # SRS v1.1: IH-AI-005 (fallback, usage) Core R2; IH-UX-003-AC01 Core với phạm vi D6.
        for ac in ("IH-AI-005-AC01", "IH-AI-005-AC02"):
            self.assertEqual((self.row(ac)["tier"], self.row(ac)["risk_suggested"]), ("Core", "R2"))
        self.assertEqual((self.row("IH-UX-003-AC01")["tier"], self.row("IH-UX-003-AC01")["scope"]), ("Core", "D6"))

    def test_passed_requires_commit_evidence_and_verification(self):
        self.row("IH-NB-004-AC01")["verdict"] = "Passed"
        messages = " ".join(self.errors())
        self.assertIn("commit", messages)
        self.assertIn("Human-verified", messages)
        self.assertIn("test_ids", messages)

    def test_lowering_risk_requires_reason(self):
        self.row("IH-NB-004-AC01")["risk"] = "R3"
        self.assertTrue(any("risk_reason" in e for e in self.errors()))
        self.row("IH-NB-004-AC01")["risk_reason"] = "demo"
        self.assertFalse(any("risk_reason" in e for e in self.errors()))

    def test_ai_draft_cannot_have_verdict_before_verification(self):
        r = self.row("IH-NOTE-001-AC01")
        r.update(draft_by="AI", verdict="Failed", commit="abcdef1", actual="x", evidence="y")
        self.assertTrue(any("bản nháp AI" in e for e in self.errors()))

    def test_gate_flags_unfinished_core(self):
        self.assertTrue(any("gate M4" in e for e in self.errors("M4")))

    def test_sampling_is_seeded_and_stratified(self):
        pop1, a = trace_sample.sample(self.rows, "seed-1", 10)
        pop2, b = trace_sample.sample(self.rows, "seed-1", 10)
        self.assertEqual([r["ac_id"] for r in a], [r["ac_id"] for r in b])
        self.assertEqual(len(a), 10)
        self.assertEqual(len({r["group"] for r in a}), 10)
        self.assertTrue(all(r["tier"] != "Extended" and r["scope"] != "N" for r in a))

    def test_evaluate_threshold(self):
        log = [{"round": "1", "result": "Error" if i < 2 else "OK"} for i in range(10)]
        self.assertTrue(trace_sample.evaluate(log, 0.2)[0][4].startswith("EXPAND"))
        log[1]["result"] = "OK"
        self.assertTrue(trace_sample.evaluate(log, 0.2)[0][4].startswith("ACCEPT"))

    def test_cli_appends_round(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "log.csv"
            with redirect_stdout(io.StringIO()):
                trace_sample.main(["--seed", "7", "--log", str(log)])
                trace_sample.main(["--seed", "8", "--log", str(log)])
            rounds = {r["round"] for r in csv.DictReader(log.open(encoding="utf-8"))}
            self.assertEqual(rounds, {"1", "2"})

    def test_missing_column_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.csv"
            fields = [f for f in self.fields if f != "evidence"]
            write_rows(path, fields, [{k: r[k] for k in fields} for r in self.rows])
            with redirect_stdout(io.StringIO()):
                self.assertEqual(trace_check.main(["--file", str(path)]), 1)


if __name__ == "__main__":
    unittest.main()
