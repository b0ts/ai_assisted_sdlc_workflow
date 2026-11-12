#!/bin/bash
# Runs Codex's re-review of the round 1 fixes (prompt c08-02, Mode E; run it after each pass of fixes) in
# read-only mode. Codex's final answer, word for word, is saved as
# docs/d08-04-code-review-codex.md.new, so the report it updates is never
# overwritten by accident. Double-click this file in Finder to run it.
cd "$(dirname "$0")" || exit 1
if ! command -v codex >/dev/null 2>&1; then
  [ -s "$HOME/.nvm/nvm.sh" ] && . "$HOME/.nvm/nvm.sh"
  export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
fi
if ! command -v codex >/dev/null 2>&1; then
  echo "Codex wasn't found. Install it, then double-click this file again."
  read -r -p "Press Return to close." _; exit 1
fi
BASE=a77451540e9cc8cf3c53ab0df159a69f087cafb2   # the commit Codex reviewed in round 1
OUT=docs/d08-04-code-review-codex.md.new
echo "Starting Codex's re-review of the round 1 fixes. This takes about 5 to 20 minutes."
echo
{ cat <<EOF
This is a read-only re-review, Mode E of the prompt below. Don't change or create any files.

You are the same reviewer who wrote docs/d08-04-code-review-codex.md (round 1). Read it first,
including any earlier "Re-Review" sections: a person has filled in the Decision column. Check
every finding marked Fix (and every question answered Yes) whose latest re-review result isn't
"Fixed", plus any new finding marked Fix. Findings accepted as they are stay as they are.

Review only what changed since commit $BASE, in src/, tests/, and these documents:
docs/d03-01-prd.md, docs/d04-01-spec.md, docs/d05-01-ui-ux.md, docs/d06-01-infrastructure.md,
docs/d07-01-test-plan.md, and docs/d08-02-developer-guide.md. For example:
  git diff $BASE -- src tests docs/d03-01-prd.md docs/d04-01-spec.md docs/d05-01-ui-ux.md docs/d06-01-infrastructure.md docs/d07-01-test-plan.md docs/d08-02-developer-guide.md
The working folder also holds other uncommitted documents; they are outside this re-review.
Don't open any other review report (docs/d08-04-code-review-claude-trial.md, docs/d08-05-hands-on-review.md)
or the review rows of docs/d08-01-implementation-record.md Section 7.

Give your complete updated report, in Markdown, as your final answer, with nothing before or
after it: keep everything already in it, including the person's decisions, word for word; add a
new, dated "Re-Review" section after the last one, with Fixed, Partly fixed, or Not fixed for each
finding you checked; add any new findings to the table, numbered after the last one, with the
Decision column empty; raise the version by 0.1; and add a Change Log row and a new hand-off note.

EOF
  sed -n '/^---$/,$p' ../../prompts/c08-02-code-review-prompt.md
} | codex exec --sandbox read-only --output-last-message "$OUT" -
STATUS=$?
echo
if [ $STATUS -eq 0 ] && [ -s "$OUT" ]; then
  echo "Done. The updated report is saved as $OUT"
  open -t "$OUT"   # a .new file: open it in the default text editor
else
  echo "Codex didn't finish (status $STATUS). Scroll up to see why."
fi
read -r -p "Press Return to close this window." _
