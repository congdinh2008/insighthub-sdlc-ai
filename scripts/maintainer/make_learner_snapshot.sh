#!/usr/bin/env bash
# Maintainer only: create a clean learner repository from a reviewed commit.
# History is NOT carried over, so removed material (docs/archive, old solution
# hints) cannot be recovered by learners with `git log`.
#
# Usage: scripts/maintainer/make_learner_snapshot.sh <commit-or-tag> <output-dir> [tag]
# Then: cd <output-dir> && git remote add origin <new learner repo URL> && git push -u origin main --tags
set -euo pipefail
REF="${1:?commit or tag}"
OUT="${2:?output directory (must not exist)}"
TAG="${3:-learner-r1.0}"
ROOT="$(git rev-parse --show-toplevel)"
[ ! -e "$OUT" ] || { echo "Output exists: $OUT" >&2; exit 1; }
git -C "$ROOT" diff --quiet "$REF" -- || echo "Note: working tree differs from $REF; snapshot uses $REF only." >&2
SHA="$(git -C "$ROOT" rev-parse "$REF^{commit}")"
mkdir -p "$OUT"
git -C "$ROOT" archive --format=tar "$SHA" | tar -x -C "$OUT"
# Maintainer-only material stays out of the learner repository.
rm -rf "$OUT/scripts/maintainer" "$OUT/dist" "$OUT/docs/archive"
for path in .env reports; do [ ! -e "$OUT/$path" ] || { echo "Unexpected $path in snapshot" >&2; exit 1; }; done
if grep -rIl --exclude-dir=node_modules -E '(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,})' "$OUT" >/dev/null; then
  echo "Possible API key in snapshot; aborting" >&2; exit 1
fi
cd "$OUT"
export GIT_AUTHOR_NAME="InsightHub Starter" GIT_AUTHOR_EMAIL="noreply@insighthub.local"
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME" GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
git init -q -b main
git add -A
git commit -q -m "chore: InsightHub Starter learner snapshot" -m "Source commit: $SHA"
git tag -a "$TAG" -m "InsightHub learner snapshot from $SHA"
echo "Snapshot ready: $OUT ($(git rev-list --count HEAD) commit, tag $TAG, source $SHA)"
