#!/usr/bin/env python3
"""Maintainer tool: rebuild trace/ac-trace.csv from the learner Requirements AC table.

Instructor columns come from Requirements section 15.4 (AC, scope, tier, LR, due,
UAT) and from the suggested risk already recorded in the current trace file.
Learner columns start empty. Run when Requirements changes, before publishing.

    python3 scripts/maintainer/build_trace_skeleton.py            # write trace/ac-trace.csv
    python3 scripts/maintainer/build_trace_skeleton.py --check    # only compare, exit 1 on drift
    python3 scripts/maintainer/build_trace_skeleton.py --risk IH-NB-001-AC03=R1   # risk for a new AC
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from trace_lib import COLUMNS, REQUIREMENTS, RISKS, ROOT, read_rows, write_rows  # noqa: E402
from trace_lib import TRACE as OUTPUT  # noqa: E402

ROW = re.compile(
    r"^\| (IH-[A-Z]+-\d{3}) \| (IH-[A-Z]+-\d{3}-AC\d{2}) \| (A|D\d|N) \| (Core|Extended|Ngoài phạm vi) \| "
    r"([^|]*)\| ([^|]*)\| ([^|]*)\|",
    re.M,
)
TIER = {"Core": "Core", "Extended": "Extended", "Ngoài phạm vi": "OutOfScope"}


def srs_path():
    found = sorted((ROOT / "docs" / "learner").glob("02_SRS_InsightHub_v*.md"))
    if len(found) != 1:
        sys.exit(f"Expected exactly one SRS in docs/learner, found {[p.name for p in found]}")
    return found[0].relative_to(ROOT).as_posix()


def parse_overrides(items):
    overrides = {}
    for item in items:
        ac, _, risk = item.partition("=")
        if risk not in RISKS:
            sys.exit(f"--risk {item}: risk must be one of {sorted(RISKS)}")
        overrides[ac] = risk
    return overrides


def build(overrides):
    _, current = read_rows(OUTPUT) if OUTPUT.exists() else ([], [])
    known_risk = {row["ac_id"]: row["risk_suggested"] for row in current}
    known_risk.update(overrides)
    srs = srs_path()
    rows, missing = [], []
    for req, ac, scope, tier_label, lr, due, uat in ROW.findall(REQUIREMENTS.read_text(encoding="utf-8")):
        tier = TIER[tier_label]
        if (scope == "N") != (tier == "OutOfScope"):
            sys.exit(f"{ac}: scope {scope} does not match tier {tier_label} in Requirements 15.4")
        risk = "" if scope == "N" else known_risk.get(ac, "")
        if scope != "N" and risk not in RISKS:
            missing.append(ac)
        row = dict.fromkeys(COLUMNS, "")
        row.update(
            ac_id=ac, req_id=req, group=req.rsplit("-", 1)[0].replace("IH-", ""), scope=scope, tier=tier,
            risk_suggested=risk, lr=lr.strip(), due=due.strip().replace("→", "->"), uat=uat.strip(),
            srs_ref=f"{srs}#req-{req.lower()}", risk=risk,
            verification="" if scope == "N" else "Unverified",
            verdict="OutOfScope" if scope == "N" else "NotRun",
        )
        rows.append(row)
    if missing:
        sys.exit(f"No suggested risk for {missing}; pass --risk <AC>=R1|R2|R3")
    ids = [r["ac_id"] for r in rows]
    if not rows or len(ids) != len(set(ids)):
        sys.exit(f"Requirements 15.4 has {len(ids)} rows, {len(set(ids))} unique AC")
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="compare with trace/ac-trace.csv without writing")
    parser.add_argument("--risk", action="append", default=[], metavar="AC=R1", help="suggested risk for a new AC")
    args = parser.parse_args()
    rows = build(parse_overrides(args.risk))
    count = lambda key, value: sum(r[key] == value for r in rows)  # noqa: E731
    summary = (f"{len(rows)} AC; R1={count('risk', 'R1')} R2={count('risk', 'R2')} R3={count('risk', 'R3')}; "
               f"Core={count('tier', 'Core')} Extended={count('tier', 'Extended')} "
               f"OutOfScope={count('tier', 'OutOfScope')}")
    if args.check:
        _, current = read_rows(OUTPUT)
        if current != rows:
            sys.exit(f"Drift: trace/ac-trace.csv differs from Requirements 15.4 ({summary})")
        print(f"OK: trace/ac-trace.csv matches Requirements 15.4 ({summary})")
        return
    write_rows(OUTPUT, COLUMNS, rows)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {summary}")


if __name__ == "__main__":
    main()
