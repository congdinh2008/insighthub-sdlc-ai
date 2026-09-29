#!/usr/bin/env python3
"""Maintainer tool: build trace/ac-trace.csv from the learner Requirements AC table.

Instructor-owned columns (from Requirements section 15.4 plus the suggested risk
and tier maps below) are regenerated; learner columns start empty. Run again
only when Requirements changes, before a learner snapshot is published.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from trace_lib import COLUMNS, REQUIREMENTS, ROOT, write_rows  # noqa: E402
from trace_lib import TRACE as OUTPUT

SRS = "docs/learner/02_SRS_InsightHub_v1.0.md"

R1 = set("""
IH-AUTH-001-AC01 IH-AUTH-001-AC02 IH-AUTH-002-AC01 IH-AUTH-002-AC02 IH-AUTH-003-AC01 IH-AUTH-003-AC02
IH-AUTH-004-AC01 IH-AUTH-004-AC02 IH-AUTH-005-AC01 IH-AUTH-005-AC02 IH-AUTH-005-AC03 IH-AUTH-006-AC01
IH-AUTH-007-AC01 IH-AUTH-007-AC02 IH-AUTH-007-AC03 IH-AUTH-008-AC01 IH-AUTH-008-AC02 IH-AUTH-010-AC01
IH-AUTH-010-AC02 IH-NB-001-AC01 IH-NB-003-AC02 IH-NB-004-AC01 IH-NB-004-AC02 IH-DOC-004-AC02
IH-DOC-006-AC01 IH-CHAT-001-AC02 IH-CHAT-002-AC01 IH-CHAT-002-AC02 IH-CHAT-003-AC01 IH-CHAT-005-AC02
IH-AI-004-AC02 IH-SUM-001-AC02 IH-QUIZ-001-AC02 IH-QUIZ-002-AC01 IH-OUT-001-AC02 IH-OUT-003-AC01
IH-DATA-001-AC04 IH-DATA-002-AC01 IH-DATA-002-AC02 IH-DATA-002-AC03 IH-DATA-002-AC04 IH-UX-004-AC02
IH-MSG-003-AC02 IH-MSG-004-AC02 IH-INT-002-AC02 IH-INT-002-AC03 IH-INT-004-AC02 IH-NFR-001-AC01
IH-NFR-001-AC02 IH-NFR-001-AC03 IH-NFR-001-AC04 IH-NFR-001-AC05 IH-NFR-002-AC01 IH-NFR-002-AC02
IH-NFR-003-AC01 IH-NFR-003-AC02 IH-NFR-004-AC01 IH-NFR-008-AC02 IH-NFR-009-AC01 IH-NFR-009-AC02
IH-NFR-011-AC01 IH-NFR-011-AC02 IH-REL-001-AC02
""".split())
R3 = set("""
IH-AUTH-009-AC01 IH-AUTH-009-AC02 IH-UX-001-AC01 IH-UX-001-AC02 IH-MSG-001-AC01 IH-MSG-001-AC02
IH-MSG-002-AC01 IH-MSG-002-AC02 IH-INT-001-AC01 IH-INT-003-AC02 IH-NFR-008-AC01 IH-REL-002-AC01
IH-REL-002-AC02
""".split())
# D7 công bố 29/09/2026: Core = Auth, Notebook (gồm Document, Chat/Conversation), Summary, Quiz,
# nền AI Job/Output và các mục kiểm M4/M5; Extended = danh sách dưới (45 AC). Auth giữ quyết định QĐ3 28/09.
EXTENDED = set("""
IH-AUTH-002-AC02 IH-AUTH-003-AC02 IH-AUTH-005-AC01 IH-AUTH-005-AC03 IH-AUTH-005-AC04 IH-AUTH-006-AC02 IH-AUTH-007-AC03 IH-AUTH-009-AC02 IH-MSG-003-AC03
IH-NB-002-AC02 IH-NB-003-AC01 IH-DOC-003-AC02 IH-DOC-005-AC01 IH-DOC-006-AC02 IH-CHAT-004-AC03 IH-CHAT-004-AC04 IH-CHAT-004-AC05
IH-NOTE-001-AC01 IH-NOTE-001-AC02 IH-NOTE-001-AC03 IH-NOTE-001-AC04 IH-NOTE-002-AC01 IH-NOTE-002-AC02 IH-SUM-002-AC01 IH-SUM-002-AC02
IH-OUT-002-AC01 IH-OUT-002-AC02 IH-OUT-003-AC02 IH-AI-003-AC02 IH-DATA-001-AC01 IH-DATA-001-AC03 IH-DATA-001-AC05 IH-DATA-001-AC06
IH-UX-001-AC02 IH-UX-002-AC02 IH-UX-003-AC01 IH-UX-003-AC02 IH-UX-004-AC01 IH-MSG-001-AC01 IH-MSG-001-AC02 IH-MSG-002-AC01 IH-MSG-002-AC02 IH-INT-001-AC01 IH-INT-001-AC02 IH-INT-004-AC01
""".split())

ROW = re.compile(r"^\| (IH-[A-Z]+-\d{3}) \| (IH-[A-Z]+-\d{3}-AC\d{2}) \| (A|D\d|N) \| (Core|Extended|Ngoài phạm vi) \| ([^|]*)\| ([^|]*)\| ([^|]*)\|", re.M)


def main():
    rows = []
    for req, ac, scope, listed_tier, lr, due, uat in ROW.findall(REQUIREMENTS.read_text(encoding="utf-8")):
        group = req.rsplit("-", 1)[0].replace("IH-", "")
        if scope == "N":
            tier = "OutOfScope"
        else:
            tier = "Extended" if ac in EXTENDED else "Core"
        expected_label = {"OutOfScope": "Ngoài phạm vi"}.get(tier, tier)
        assert listed_tier == expected_label, f"{ac}: Requirements 15.4 ghi {listed_tier}, bản đồ ghi {tier}"
        risk = "" if scope == "N" else ("R1" if ac in R1 else "R3" if ac in R3 else "R2")
        row = dict.fromkeys(COLUMNS, "")
        row.update(
            ac_id=ac, req_id=req, group=group, scope=scope, tier=tier, risk_suggested=risk,
            lr=lr.strip(), due=due.strip().replace("→", "->"), uat=uat.strip(),
            srs_ref=f"{SRS}#req-{req.lower()}", risk=risk,
            verification="" if scope == "N" else "Unverified",
            verdict="OutOfScope" if scope == "N" else "NotRun",
        )
        rows.append(row)
    assert len(rows) == 163 and len({r["ac_id"] for r in rows}) == 163, f"Expected 163 AC rows, got {len(rows)}"
    unknown = (R1 | R3 | EXTENDED) - {r["ac_id"] for r in rows}
    assert not unknown, f"Unknown AC in maps: {sorted(unknown)}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    write_rows(OUTPUT, COLUMNS, rows)
    count = lambda key, value: sum(r[key] == value for r in rows)  # noqa: E731
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: 163 AC; R1={count('risk', 'R1')} R2={count('risk', 'R2')} "
          f"R3={count('risk', 'R3')}; Core={count('tier', 'Core')} Extended={count('tier', 'Extended')} "
          f"Pending={count('tier', 'Pending')} OutOfScope={count('tier', 'OutOfScope')}")


if __name__ == "__main__":
    main()
