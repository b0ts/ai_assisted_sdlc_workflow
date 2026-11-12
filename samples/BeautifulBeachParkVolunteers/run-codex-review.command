#!/bin/bash
# Runs the independent Codex code review (prompt c08-02) in read-only mode
# and saves Codex's final answer, word for word, as
# docs/d08-04-code-review-codex.md. Double-click this file in Finder to run it.
cd "$(dirname "$0")" || exit 1
if ! command -v codex >/dev/null 2>&1; then
  [ -s "$HOME/.nvm/nvm.sh" ] && . "$HOME/.nvm/nvm.sh"
  export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
fi
if ! command -v codex >/dev/null 2>&1; then
  echo "Codex wasn't found. Install it, then double-click this file again."
  read -r -p "Press Return to close." _; exit 1
fi
OUT=docs/d08-04-code-review-codex.md
echo "Starting the Codex review. This takes about 5 to 20 minutes."
echo
{ echo "This is a read-only review. Don't change or create any files. Don't open docs/d08-04-code-review-claude.md. The report template is ../../templates/d08-04-code-review.md. Give the complete report, in Markdown, as your final answer."
  echo
  sed -n '/^---$/,$p' ../../prompts/c08-02-code-review-prompt.md
} | codex exec --sandbox read-only --output-last-message "$OUT" -
STATUS=$?
echo
if [ $STATUS -eq 0 ] && [ -s "$OUT" ]; then
  echo "Done. The report is saved as $OUT"
  open "$OUT"
else
  echo "Codex didn't finish (status $STATUS). Scroll up to see why."
fi
read -r -p "Press Return to close this window." _
