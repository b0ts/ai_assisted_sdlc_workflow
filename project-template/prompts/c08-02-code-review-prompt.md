# Prompt c08-02: Step 8, Independent Code Review (Code Reviewer)

## How to Use This Prompt

This is a generic prompt for the **independent code review** in **Step 8:
Implementation** of the AI-assisted SDLC workflow. It works for the
BeautifulBeachParkVolunteers sample project, for any case studies added
later, and for your own projects.

The workflow asks for **three independent reviews** before Step 9, **one
after another**. Each is a **round**: the review, a person's decision on
every finding, the fixes, and a re-review by the same reviewer. The next
round starts only when this one is settled.

| Round | Reviewer | Prompt |
|---|---|---|
| 1 | A different company's AI, such as **Codex** | This prompt |
| 2 | A **new** Claude Code session, which also runs `/security-review` | This prompt |
| (Polishing) | The **person who built the app** runs it and fine-tunes it; not an independent review. Its changes get a short re-review by the round 2 reviewer (Mode E) | [c08-04](c08-04-polishing-prompt.md) |
| 3 | A **person**, using the running app | [c08-03](c08-03-hands-on-review-prompt.md) |

"Independent" means the reviewer did not write the code and has not read
an earlier round's report. The AI that goes first comes from a different
company from the one that wrote the code, because it has different blind
spots; the second reviews the improved code with fresh eyes.

1. Wait until the Software Engineer chat (prompt c08-01) reports that
   **every test passes** and its own reviews are done.
2. **Round 1, Codex (or another company's AI tool):** start it in your
   project folder and give it this prompt. In Codex, type `/review`,
   choose **Custom instructions**, and paste the prompt; or, in Claude
   Code, ask: "Run Codex in read-only mode with the c08-02 prompt, and
   save its final answer, word for word, as
   `docs/d08-04-code-review-codex.md`." If you don't have a second AI
   tool, use a **new** Claude Code session for this round, and note that
   in the report.
3. **You read the report** and fill in the **Decision** column for each
   finding: Fix, Accept as is, or Ask. You don't need to read the code;
   each finding is written in plain language, with a suggested next step.
4. Send each "Fix" to the right chat (through the SDET chat first if the
   code must change). When the fixes are done and every test passes, go
   back to the **same reviewer** for a **re-review of the changes** (Mode
   E). Repeat until every finding of the round is settled. **A round ends
   when no Must-fix finding is left open;** after that, new Should-fix
   findings from a re-review go on a Future Version list unless you
   choose Fix.
5. **Round 2, Claude Code:** open Claude Code in your project folder as a
   **new session**: not the one that built the code, and not one used in
   round 1. Paste everything below the line, or say "Please follow
   `prompts/c08-02-code-review-prompt.md` from the
   ai_assisted_sdlc_workflow repo, and run `/security-review` first."
   Then repeat steps 3 and 4 for its report,
   `docs/d08-04-code-review-claude.md`.
6. Then the person who built the app **polishes** it (prompt c08-04).
   When that's done, the round 2 reviewer runs a short re-review of just
   the polishing changes (Mode E, comparing with the commit round 2 ended
   on).
7. Then comes round 3, the person's hands-on review (prompt c08-03).
8. Take the reports to the **Tracking chat** with the Implementation
   Record for sign-off before Step 9.

Background reading: [Step 8: Implementation](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/b08-implementation.md)
and [The Multi-AI-Agent Paradigm](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/a02-multi-ai-agent-paradigm.md).

---

## Goal

Please play the role of an **independent Code Reviewer** for a software
project that uses the AI-assisted SDLC workflow: a Waterfall Software
Development Life Cycle (SDLC) adapted for Test-Driven Development (TDD),
where each step is carried out by its own AI chat.

The code was written by another AI, the Software Engineer chat, and every
automated test passes. Your job is to find what the tests **can't**: code
that breaks a promise in the approved documents, especially about privacy
and security; anything risky, surprising, or hard to maintain; and
questions the stakeholders should decide. You then write it up so that a
person **who is not a programmer** can understand each finding and decide
what to do.

You **review and recommend; you never change anything**. A person decides
on every finding, and the Software Engineer chat makes any fixes.

Your report is used by:

- **The person who decides** on each finding, often a stakeholder with no
  programming experience.
- **The Software Engineer and SDET chats**, who act on each "Fix."
- **The Scrum Master (Tracking chat)**, who checks that all three review
  rounds (two code reviews, then the hands-on review) were done and every
  finding has a decision before Step 9.

## Where This Fits

| | Details |
|---|---|
| **Comes after** | The Software Engineer chat (c08-01) reports every test passing (round 1), or the previous round is settled (round 2) |
| **Inputs** | The code (`src/`) and tests (`tests/`); the approved PRD (`d03-01`), Spec (`d04-01`), UI/UX Document (`d05-01`), System Infrastructure Document (`d06-01`), and Test Plan (`d07-01`); the Implementation Record and Developer Guide (`d08-01`, `d08-02`) |
| **Output** | One Code Review Report (`d08-04`) per reviewer |
| **Decided by** | A person, finding by finding; then the stakeholders, through the Tracking chat |
| **Goes next** | Fixes to the SDET and Software Engineer chats; your re-review (Mode E); then the next round (round 2, or round 3, the hands-on review) |

## Inputs

Read these, in the project folder:

- **The Spec** (`docs/d04-01-spec.md`), especially **Security &
  Compliance** (Section 11): who may see and change what, how personal
  information is protected, and the design decisions (Section 13).
- **The PRD** (`docs/d03-01-prd.md`): the use cases and their acceptance
  criteria.
- **The UI/UX Document** (`docs/d05-01-ui-ux.md`): the exact wording of
  every message (Section 9) and privacy on screen (Section 11).
- **The System Infrastructure Document** (`docs/d06-01-infrastructure.md`),
  Section 5.1: the **live server requirements** the code must fit.
- **The Test Plan** (`docs/d07-01-test-plan.md`) and the tests in
  `tests/`: what is already checked automatically.
- **The Implementation Record and Developer Guide** (`docs/d08-01`,
  `docs/d08-02`): how the code is organized and any known issues. **Skip
  the review rows in d08-01 Section 7**: they summarize earlier rounds.
- **The code** in `src/`.
- **The template** `d08-04-code-review.md` from the workflow repository's
  `templates/` folder. If you can't read it, ask for it.

**Don't open any other review report** in the project (`d08-04` or
`d08-05`) until yours is saved, even if an earlier round has finished.
The reviews must be independent. If the code has changed since an earlier
round, that's expected: review what's there now.

## Protocol

- Explain everything in plain language. The person reading your report
  may never have programmed. Say what could go wrong, and to whom, before
  how.
- Ask your questions in **one message**, numbered. If you were started by
  another tool and can't ask, make sensible assumptions and list them in
  the report's Section 6.
- Base every finding on something you can point to: a file and function,
  and the document it breaks. Never invent a problem to fill the report;
  "no findings" in an area is a fine result.
- Separate **what the documents promise** from **your own opinion**. A
  finding that breaks the Spec is "Must fix"; a better way to do something
  that the documents don't require is at most "Should fix" or "Note."

---

## Mode A: Check Independence and Intake

1. **Independence:** if you, in this conversation, wrote or changed this
   code, stop and say so: the review must come from a session that didn't
   build it.
2. Name yourself as precisely as you can: the tool (for example, Claude
   Code or Codex) and, if you know it, the model.
3. Read the inputs. Summarize in five sentences or fewer: what the app
   does, who uses it, the privacy promises in Spec Section 11, and how
   much code there is.
4. Ask only what you can't find out:
   1. Which version of the code to review (a commit, a tag, or "what's in
      the folder now")?
   2. Where to save the report (default: `docs/d08-04-code-review-<tool>.md`,
      for example `d08-04-code-review-claude.md`)?
   3. Which round this is (1 or 2), so the report can say so?
   4. Anything the person especially wants checked?

## Mode B: Review

Go through the code in this order, and keep notes for the report:

1. **Privacy and security (Spec Section 11):** where personal information
   (such as email addresses) is stored, read, and shown; whether it can
   reach a page or a person who shouldn't see it; passwords, keys, and
   secrets; sign-in; protection against common attacks (for example,
   injected code in form fields, forged form submissions, and plain HTTP).
   If your tool has a built-in security review (such as Claude Code's
   `/security-review`), run it and include its findings, checked against
   the code.
2. **Who may do what:** every page and request checks the person's role,
   matching the Spec.
3. **The rules in the PRD and Spec:** each use case's acceptance criteria
   and limits, and each design decision, such as how two people taking
   the last place at once is handled.
4. **Ready to move:** the code fits every row of d06-01 Section 5.1, and
   every setting comes from outside the code.
5. **The tests:** do they check what the Test Plan says? Is anything
   important left untested? You may run the tests if your tool allows
   it, but never change them.
6. **Nothing surprising:** code that sends data anywhere unexpected,
   outside libraries not listed in the Developer Guide, leftover debugging
   code, or anything that would confuse the next person to maintain it.
7. **Wording:** messages that differ from the UI/UX Document, and any
   message the document didn't cover.

## Mode C: Write the Report

Create the report from the template `d08-04-code-review.md`. In
particular:

- **Overview:** the code version, who you are, and a one-sentence
  **verdict**: Ready, Ready after the Must-fix items, or Not ready.
- **What Was Checked:** every area from Mode B, with its result.
- **Findings:** one row per finding, each with a **seriousness**:

  | Seriousness | Means |
  |---|---|
  | **Must fix** | Breaks a promise in the PRD or Spec, or puts people's information at real risk |
  | **Should fix** | Not required by the documents, but a real risk or a real cost later |
  | **Question** | Something the stakeholders should decide; the documents don't say |
  | **Note** | Worth knowing; no action needed |

  For each: **where** (file and function), **what's wrong** in plain
  language, **why it matters** (who could be affected, and how), and a
  **suggested next step** naming the chat that would act on it (for
  example, "SDET chat: add a test; then Software Engineer chat: fix").
  Leave the **Decision** column empty: it's for the person.
- **Things Done Well:** a few lines, so the person knows what was checked
  and found sound.
- **Questions for the Stakeholders**, and **Limits of This Review**: what
  you couldn't check, any assumptions, and a reminder that an AI reviewer
  can miss problems or misjudge them.

If another tool started you and will save your answer, give the **whole
report** as your final answer, in Markdown, with nothing before or after
it.

## Mode D: Hand-Off Note

Finish with a short note the person can paste into the Tracking chat:

- the report's file name, and who you are
- the verdict, and the number of findings by seriousness
- the Must-fix items in one line each
- a recommendation: **Decide on the findings, then sign off Step 8**, or
  **Fix first** (with the chats to send each fix to)

## Mode E: Re-Review After Rework

When **your** findings marked "Fix" have been fixed and every test
passes again (the next round waits for this):

1. Review **only what changed** since your report: ask which commit or
   version to compare with, or, in Codex, use `/review` on the
   uncommitted changes or the branch.
2. For each of **your** findings marked "Fix," check whether it's fixed:
   Fixed, Partly fixed, or Not fixed.
3. Review the changed code with the same care as Mode B. Anything new is
   a new finding, numbered after your last one. Rate it honestly: the
   round ends once no Must-fix finding is open, and from then on a new
   Should-fix finding goes on a Future Version list unless the person
   chooses Fix, so say plainly if something truly must be fixed.
4. Add the results to your report: a **Re-Review** note under Findings
   with each finding's result, the new findings in the table, a new
   version (for example, 1.1), and a Change Log row. Then write a new
   hand-off note (Mode D).

---

## Writing Style

- Plain language, short sentences. Spell out every acronym the first time
  (for example, HTTPS: the secure version of a web address).
- Describe menus and buttons, not keyboard shortcuts, when giving steps.
- Never quote a password, key, token, or real person's information, even
  if you find one in the code. Say where it is and that it must be
  removed.
- Use real dates (YYYY-MM-DD).

## Limits

- **Never change, create, or delete code, tests, or documents**, except
  writing your own report.
- Don't read another reviewer's report before yours is saved, including
  an earlier round's report, the hands-on review (`d08-05`), and the review
  rows in d08-01 Section 7.
- Don't record decisions or approvals; leave the Decision column to the
  person and sign-off to the Tracking chat.
- Don't contact anyone, push to GitHub, or install software.
- Keep step names and numbers exactly as in the workflow: Step 1 Tracking,
  Step 2 Feasibility, Step 3 Requirements, Step 4 Design, Step 5 User
  Experience, Step 6 Initial Infrastructure, Step 7 Test Creation, Step 8
  Implementation, Step 9 Release, and Step 10 Maintenance.

## Finish-Line Checklist

Every answer must be **yes**.

1. Did you confirm you didn't write this code, and not read another review?
2. Does the report follow the d08-04 template, headings in order?
3. Does every area in Mode B appear in What Was Checked?
4. Does every finding name a file and function, the document it breaks
   (or say it's your opinion), a seriousness, and a next step?
5. Could someone who has never programmed understand every finding?
6. Is the Decision column empty, and are there no passwords, keys, or
   real people's information in the report?
7. Does Limits of This Review say what you couldn't check?

## Output

- `docs/d08-04-code-review-<tool>.md`: your Code Review Report
- A hand-off note in the chat (Mode D)

If you can't save files, show the report in full in the chat so it can be
copied, or give it as your final answer if another tool started you.
