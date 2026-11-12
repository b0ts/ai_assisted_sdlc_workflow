#!/bin/bash
# Round 2: an independent code review by a NEW Claude Code session (prompt c08-02),
# in read-only mode. Its final answer, word for word, is saved as
# docs/d08-04-code-review-claude.md.new for a person to check.
# Double-click this file in Finder to run it.
cd "$(dirname "$0")" || exit 1
if ! command -v claude >/dev/null 2>&1; then
  [ -s "$HOME/.nvm/nvm.sh" ] && . "$HOME/.nvm/nvm.sh"
  export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code (the 'claude' command) wasn't found on this Mac."
  echo "Instead, open the Claude desktop app, start a NEW Code session in this folder,"
  echo "and say: Please follow prompts/c08-02-code-review-prompt.md from the"
  echo "ai_assisted_sdlc_workflow repo. This is round 2. Run /security-review first,"
  echo "and save your report as docs/d08-04-code-review-claude.md."
  read -r -p "Press Return to close." _; exit 1
fi
OUT=docs/d08-04-code-review-claude.md.new
echo "Starting round 2: an independent Claude Code review. This takes about 10 to 30 minutes."
echo
{ cat <<'EOF'
This is round 2 of the independent code reviews, in read-only mode. Follow the prompt below,
Modes A to D. Don't change or create any files. You did not write this code.

Independence: don't open any other review report or anything about earlier reviews:
docs/d08-04-code-review-codex.md, docs/d08-04-code-review-claude-trial.md,
docs/d08-05-hands-on-review.md, src/REVIEW-GUIDE.md, the review rows of
docs/d08-01-implementation-record.md Section 7, or its Future Version list.

Review the code as it is in the folder now (src/ and tests/), against the documents in docs/:
d03-01 PRD, d04-01 Spec, d05-01 UI/UX, d06-01 Infrastructure, d07-01 Test Plan, d08-02 Developer
Guide. The report template is ../../templates/d08-04-code-review.md. The review round is 2.
Start with the security review that Claude Code's /security-review command does (look for
real, exploitable security and privacy problems, and check each one against the code), and
include what you find in "Built-in security scan". You may run the tests with
"pytest -m 'not monkey and not browser'" if your tools allow it; never change them.

Give the complete report, in Markdown, as your final answer, with nothing before or after it,
followed by the hand-off note (Mode D). Leave the Decision column empty.

EOF
  sed -n '/^---$/,$p' ../../prompts/c08-02-code-review-prompt.md
} | claude -p --allowedTools "Read" "Grep" "Glob" "Bash(git diff:*)" "Bash(git log:*)" "Bash(git status:*)" "Bash(ls:*)" "Bash(pytest:*)" "Bash(python -m pytest:*)" "Bash(.venv/bin/python -m pytest:*)" > "$OUT"
STATUS=$?
echo
if [ $STATUS -eq 0 ] && [ -s "$OUT" ]; then
  echo "Done. The report is saved as $OUT"
  open -t "$OUT"
else
  echo "Claude Code didn't finish (status $STATUS). Scroll up to see why."
fi
read -r -p "Press Return to close this window." _
