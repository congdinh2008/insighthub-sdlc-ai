#!/usr/bin/env bash
# Maintainer only: so cây file của repository nguồn với một revision Starter.
# Chỉ cho phép khác ở các đường dẫn trong publish-exclude.txt (file người bảo trì).
#
#   bash scripts/maintainer/compare_starter.sh <starter-repo-hoặc-URL> [starter-ref=main] [source-ref=HEAD]
#   ví dụ: bash scripts/maintainer/compare_starter.sh ../insighthub-starter learner-r1.3.1
#
# Mã thoát 0: khớp. Mã 1: có file lệch (in danh sách). Không đổi working tree.
set -euo pipefail

STARTER="${1:?đường dẫn hoặc URL repository Starter}"
STARTER_REF="${2:-main}"
SOURCE_REF="${3:-HEAD}"
SOURCE="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
EXCLUDE="$SOURCE/scripts/maintainer/publish-exclude.txt"

[ -d "$STARTER" ] && STARTER="$(cd "$STARTER" && pwd)"
git -C "$SOURCE" fetch -q --no-tags "$STARTER" "$STARTER_REF"
STARTER_SHA="$(git -C "$SOURCE" rev-parse FETCH_HEAD)"
SOURCE_SHA="$(git -C "$SOURCE" rev-parse --verify "$SOURCE_REF^{commit}")"

is_excluded() {
  local f="$1" p
  while IFS= read -r p; do
    case "$p" in ''|'#'*) continue ;; esac
    case "$p" in
      */) [ "${f#"$p"}" != "$f" ] && return 0 ;;
      *) [ "$f" = "$p" ] && return 0 ;;
    esac
  done < "$EXCLUDE"
  return 1
}

ok=0; extra=0
while IFS=$'\t' read -r status file; do
  if [ "$status" = "A" ] && is_excluded "$file"; then
    extra=$((extra + 1))
  else
    echo "LỆCH  $status  $file"; ok=1
  fi
done < <(git -C "$SOURCE" diff --no-renames --name-status "$STARTER_SHA" "$SOURCE_SHA")

echo "Source $(git -C "$SOURCE" rev-parse --short "$SOURCE_SHA") so với Starter $STARTER_REF ($(git -C "$SOURCE" rev-parse --short "$STARTER_SHA")): $extra file người bảo trì"
if [ "$ok" -ne 0 ]; then echo "FAIL: có file lệch ngoài danh sách người bảo trì"; exit 1; fi
echo "OK: file học viên giống hệt Starter"
