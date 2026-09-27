#!/usr/bin/env python3
"""CI guard for test-as-spec (LR-13).

Every commit in BASE..HEAD that changes an approved test (glob patterns in
.claude/approved-tests.txt, union of base and head so a PR cannot drop a pattern
to bypass the rule) or the pattern file itself must carry the trailer
`Test-Change-Approved: <reason>` written by the learner.

Usage: python3 scripts/check_approved_tests.py --base origin/main
"""
import argparse
import fnmatch
import subprocess
import sys

PATTERN_FILE = ".claude/approved-tests.txt"
TRAILER = "Test-Change-Approved:"


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def parse_patterns(text):
    return {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")}


def patterns_at(ref):
    try:
        return parse_patterns(git("show", f"{ref}:{PATTERN_FILE}"))
    except subprocess.CalledProcessError:
        return set()


def violations(base, head="HEAD"):
    patterns = patterns_at(base) | patterns_at(head)
    found = []
    for sha in git("rev-list", f"{base}..{head}").split():
        files = git("diff-tree", "--no-commit-id", "--name-only", "-r", sha).split()
        guarded = [f for f in files if f == PATTERN_FILE or any(fnmatch.fnmatch(f, p) for p in patterns)]
        if not guarded:
            continue
        message = git("log", "-1", "--format=%B", sha)
        reason = next((line.split(":", 1)[1].strip() for line in message.splitlines() if line.startswith(TRAILER)), "")
        if not reason:
            found.append((sha[:10], guarded))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Base ref, for example origin/main")
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()
    problems = violations(args.base, args.head)
    if problems:
        for sha, files in problems:
            print(f"FAIL {sha}: sửa test đã duyệt mà thiếu trailer '{TRAILER} <lý do>': {', '.join(files)}")
        print("Test-as-spec: học viên tự sửa test đã duyệt trong commit riêng và ghi lý do; agent không sửa test để đạt.")
        return 1
    print("PASS: không có thay đổi test đã duyệt thiếu trailer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
