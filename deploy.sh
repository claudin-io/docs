#!/usr/bin/env bash
# Manual docs deploy.
#
# Builds the site (to catch errors), commits + pushes the docs submodule, then
# bumps the submodule pointer in the parent repo. Run it from anywhere:
#
#   ./docs/deploy.sh "docs: update client setup"
#
# The parent repo is committed but NOT pushed — review and push it yourself.
set -euo pipefail

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DOCS_DIR"

MSG="${1:-docs: manual deploy}"

# Prefer the local venv's mkdocs if present.
MKDOCS="$DOCS_DIR/.venv/bin/mkdocs"
[ -x "$MKDOCS" ] || MKDOCS="mkdocs"

# 1. Build first so a broken site never gets published.
echo "[..] Building site"
"$MKDOCS" build --clean

# 2. Commit + push the docs repo (this submodule). site/ and .venv/ are
#    gitignored, so they won't be committed.
if [ -n "$(git status --porcelain)" ]; then
  echo "[..] Committing docs changes"
  git add -A
  git commit -m "$MSG"
else
  echo "[ok] No docs changes to commit"
fi
echo "[..] Pushing docs submodule"
git push origin HEAD

# 3. Bump the submodule pointer in the parent repo (if we're a submodule).
PARENT="$(git -C "$DOCS_DIR/.." rev-parse --show-toplevel 2>/dev/null || true)"
if [ -n "$PARENT" ] && [ "$PARENT" != "$DOCS_DIR" ]; then
  git -C "$PARENT" add docs
  if ! git -C "$PARENT" diff --cached --quiet -- docs; then
    git -C "$PARENT" commit -m "chore(docs): bump docs submodule"
    echo "[ok] Parent pointer bumped."
    echo "[->] Push the parent when ready:  git -C \"$PARENT\" push"
  else
    echo "[ok] Parent pointer already current"
  fi
fi

echo "[ok] Docs deployed."
