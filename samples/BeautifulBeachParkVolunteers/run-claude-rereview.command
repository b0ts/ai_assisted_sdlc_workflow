#!/bin/bash
# Round 2 re-review: Claude Code checks the round 2 fixes (prompt c08-02, Mode E) in
# read-only mode, in a NEW session. Its final answer, word for word, is saved as
# docs/d08-04-code-review-claude.md.new, so the report it updates is never
# overwritten by accident. Double-click this file in Finder to run it.
cd "$(dirname "$0")" || exit 1
if ! command -v claude >/dev/null 2>&1; then
  [ -s "$HOME/.nvm/nvm.sh" ] && . "$HOME/.nvm/nvm.sh"
  export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code (the 'claude' command) wasn't found on this Mac."
  read -r -p "Press Return to close." _; exit 1
fi
BASE=a1185f6   # the commit Claude Code reviewed in round 2
OUT=docs/d08-04-code-review-claude.md.new
echo "Starting Claude Code's re-review of the round 2 fixes. This takes about 10 to 30 minutes."
echo
{ cat <<EOF
This is a read-only re-review, Mode E of the prompt below. Don't change or create any files.

You are the round 2 reviewer: you wrote docs/d08-04-code-review-claude.md. Read it first: a person
has filled in the Decision column. Check every finding marked Fix (and every question answered
Yes) whose latest re-review result isn't "Fixed", plus any new finding marked Fix, and look over
everything changed since your last re-review with the same care. Notes stay as they are.

Review only what changed since commit $BASE, in src/, tests/, and these documents:
docs/d03-01-prd.md, docs/d04-01-spec.md, docs/d05-01-ui-ux.md, docs/d06-01-infrastructure.md,
docs/d07-01-test-plan.md, and docs/d08-02-developer-guide.md. For example:
  git diff $BASE -- src tests docs/d03-01-prd.md docs/d04-01-spec.md docs/d05-01-ui-ux.md docs/d06-01-infrastructure.md docs/d07-01-test-plan.md docs/d08-02-developer-guide.md
The changes aren't committed yet. One new file isn't in git diff: src/bbpv/templates/sign_in_finish.html
(use git status to check for others).
Independence: don't open any other review report (docs/d08-04-code-review-codex.md,
docs/d08-04-code-review-claude-trial.md, docs/d08-05-hands-on-review.md), src/REVIEW-GUIDE.md,
or the review rows of docs/d08-01-implementation-record.md Section 7 and its Future Version list.
You may run the tests with "pytest -m 'not monkey and not browser'" if your tools allow it;
never change them.

Give your complete updated report, in Markdown, as your final answer, with nothing before or
after it: keep everything already in it, including the person's decisions, word for word; add a
new, dated "Re-Review" section under Findings, with Fixed, Partly fixed, or Not fixed for each
finding you checked; add any new findings to the table, numbered after the last one,
with the Decision column empty; raise the version by 0.1; and add a Change Log row and a new
hand-off note. Number new findings after the last one in the table.

EOF
  sed -n '/^---$/,$p' ../../prompts/c08-02-code-review-prompt.md
} | claude -p --allowedTools "Read" "Grep" "Glob" "Bash(git diff:*)" "Bash(git log:*)" "Bash(git status:*)" "Bash(git show:*)" "Bash(ls:*)" "Bash(pytest:*)" "Bash(python -m pytest:*)" "Bash(.venv/bin/python -m pytest:*)" > "$OUT"
STATUS=$?
echo
if [ $STATUS -eq 0 ] && [ -s "$OUT" ]; then
  echo "Done. The updated report is saved as $OUT"
  open -t "$OUT"
else
  echo "Claude Code didn't finish (status $STATUS). Scroll up to see why."
fi
read -r -p "Press Return to close this window." _
