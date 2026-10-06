#!/usr/bin/env bash
# Maintainer only: xuất bản một ref của repository nguồn sang nhánh release của insighthub-starter.
#
#   bash scripts/maintainer/publish_starter.sh <source-ref> <starter-repo> <revision>
#   ví dụ: bash scripts/maintainer/publish_starter.sh src-r1.3 ../insighthub-starter learner-r1.3
#
# Kết quả: nhánh release/<revision> trong <starter-repo> có đúng một commit mới trên BASE
# (mặc định main của Starter). Cây file = <source-ref> trừ publish-exclude.txt.
# Script dùng git worktree tạm, không đổi working tree hiện tại của Starter, không push, không tag.
# Biến tùy chọn: BASE=<ref trong Starter>, BRANCH=<tên nhánh>, SKIP_CHECKS=1 (bỏ kiểm sau khi tạo commit).
set -euo pipefail

REF="${1:?source ref, ví dụ src-r1.3}"
STARTER="$(cd "${2:?đường dẫn repository insighthub-starter}" && pwd)"
REVISION="${3:?revision, ví dụ learner-r1.3}"
SOURCE="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
EXCLUDE="$SOURCE/scripts/maintainer/publish-exclude.txt"
BASE="${BASE:-main}"
BRANCH="${BRANCH:-release/$REVISION}"

fail() { echo "FAIL: $*" >&2; exit 1; }

SHA="$(git -C "$SOURCE" rev-parse --verify "$REF^{commit}")" || fail "không tìm thấy $REF trong repository nguồn"
git -C "$STARTER" rev-parse --verify -q "$BASE^{commit}" >/dev/null || fail "Starter không có $BASE"
if git -C "$STARTER" rev-parse --verify -q "refs/heads/$BRANCH" >/dev/null; then
  fail "Starter đã có nhánh $BRANCH. Đặt BRANCH khác hoặc xóa nhánh cũ"
fi

PATHS=()
while IFS= read -r line; do PATHS+=("$line"); done < <(grep -v -E '^[[:space:]]*(#|$)' "$EXCLUDE")
[ "${#PATHS[@]}" -gt 0 ] || fail "publish-exclude.txt rỗng"
WT="$(mktemp -d "${TMPDIR:-/tmp}/starter-publish.XXXXXX")"
cleanup() { git -C "$STARTER" worktree remove --force "$WT" >/dev/null 2>&1 || true; rm -rf "$WT"; }
trap cleanup EXIT

git -C "$STARTER" worktree add -q -b "$BRANCH" "$WT" "$BASE"
cd "$WT"
git rm -r -q --ignore-unmatch . >/dev/null
find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
git -C "$SOURCE" archive --format=tar "$SHA" | tar -x -C "$WT"
for p in "${PATHS[@]}"; do rm -rf "./${p%/}"; done

echo "==== Kiểm nội dung xuất bản"
for p in .env reports; do [ ! -e "$p" ] || fail "có $p trong bản xuất bản"; done
for p in "${PATHS[@]}"; do [ ! -e "${p%/}" ] || fail "còn ${p%/}"; done
if grep -rIl --exclude-dir=node_modules -E '(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|gh[pousr]_[0-9A-Za-z]{30,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' . ; then
  fail "có chuỗi giống secret (danh sách file ở trên)"
fi
LEAK="$(grep -rIn --exclude-dir=node_modules --exclude=.gitignore -E 'docs/maintainer|scripts/maintainer|maintainer\.mk|package_starter|verify_package|starter-release\.yml|test-release' . || true)"
[ -z "$LEAK" ] || { echo "$LEAK"; fail "còn tham chiếu tới công cụ người bảo trì"; }

git add -A
git diff --cached --quiet && fail "không có thay đổi so với $BASE, không tạo commit rỗng"
git diff --cached --stat | tail -1
git commit -q -m "Starter $REVISION" -m "Source: $SHA ($REF)"

if [ "${SKIP_CHECKS:-0}" != "1" ]; then
  echo "==== Kiểm tài liệu, trace, công cụ"
  python3 scripts/check_project.py
  python3 scripts/trace_check.py
  python3 -m unittest discover -s scripts/tests >/dev/null 2>&1 || { python3 -m unittest discover -s scripts/tests; fail "test công cụ"; }
  echo "unittest scripts/tests: OK"
fi

echo
echo "DONE: $BRANCH = $(git rev-parse --short HEAD) trong $STARTER (source $(git -C "$SOURCE" rev-parse --short "$SHA"))"
echo "Tiếp theo: chạy make test, smoke, E2E trên nhánh này, merge --ff-only vào main, tag $REVISION rồi push."
