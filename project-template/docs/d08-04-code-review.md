# [Project name]: Code Review Report

<!-- Template d08-04. Replace every [placeholder]. Delete all hint comments
like this one, EXCEPT keep the "How to Read This Report" box for the person.
Keep every heading, in this order.
A Code Review Report is written by an INDEPENDENT AI reviewer, using prompt
c08-02: one that did not write the code and has not seen any other
reviewer's report. Each project gets two, one after another: round 1 from
a different company's AI (such as Codex), then round 2 from a new Claude
Code session, each saved as docs/d08-04-code-review-<tool>.md. Each round
is decided, fixed, and re-reviewed before the next starts. After round 2,
the person who built the app polishes it (prompt c08-04, d08-06), and the
round 2 reviewer re-reviews just the polishing changes (Mode E), added to
this same report. The reviewer never
changes code and leaves the Decision column empty; a person fills it in.
Never write passwords, keys, tokens, or real people's information here. -->

**Document:** d08-04 · **Step:** 8, Implementation · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting decisions / Decided]
· **Owner:** Code Reviewer ([tool and model, e.g., "Codex" or "Claude Code"])

> **How to Read This Report**
>
> You don't need to read the code. Start with the **verdict** in the
> Overview, then read each row in **Findings**:
>
> - **Must fix** means the code breaks a promise in the approved documents
>   or puts people's information at risk. These normally get "Fix."
> - **Should fix** is a real risk the documents didn't ask about. Decide
>   whether it's worth the time now or in a later phase.
> - **Question** is something only the stakeholders can decide.
> - **Note** needs no action.
>
> For each finding, write your **Decision**: **Fix** (send it to the chat
> named in "Next step"), **Accept as is** (say why, in a few words),
> **Future Version** (worth doing, but not now), or **Ask** (you need to
> know more; ask the reviewer or the Software Engineer chat). A round ends
> when no Must-fix finding is left open; after that, a new Should-fix
> finding goes to Future Version unless you choose Fix. An AI reviewer can be wrong in both directions: it can
> miss a problem or report one that isn't there. That's why there are three
> independent reviews, and why the decision is yours.

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Review round | [1 or 2] |
| Code reviewed | [Folder and version, e.g., "`src/` at commit 4867cab" or "tag v1.0"] |
| Reviewer | [Tool and model] |
| Independent? | [e.g., "Yes: a new session that didn't write the code; no other review report, and not the review rows of d08-01 Section 7, read first"] |
| Documents checked against | [d03-01, d04-01, d05-01, d06-01, d07-01, d08-01, d08-02, with versions] |
| Review date | [YYYY-MM-DD] |
| Verdict | [Ready / Ready after the Must-fix items / Not ready], [one sentence why] |
| Findings | [N Must fix · N Should fix · N Question · N Note] |

## 2. What Was Checked

<!-- Every area, with a short result. "No findings" is a fine result. -->

| Area | What was checked | Result |
|---|---|---|
| Privacy and security | [Spec Section 11: personal information stored, read, and shown; secrets; sign-in; common attacks] | [e.g., "1 Must fix (R-1)"] |
| Who may do what | [Every page and request checks the role, as the Spec says] | [Result] |
| PRD and Spec rules | [Each use case's acceptance criteria and limits; design decisions] | [Result] |
| Ready to move | [d06-01 Section 5.1; settings from outside the code] | [Result] |
| Tests | [They check what the Test Plan says; important gaps] | [Result] |
| Nothing surprising | [Unexpected data sent anywhere; unlisted libraries; leftover debugging code] | [Result] |
| Wording | [Messages match d05-01 Section 9; messages it didn't cover] | [Result] |
| Built-in security scan | [e.g., "Claude Code /security-review run; findings checked and included" or "Not available"] | [Result] |

## 3. Findings

<!-- One row per finding, most serious first. "Where" is a file and
function. "Breaks" names the document and section, or says "Reviewer's
opinion." Leave Decision and Decided by empty for the person. -->

| ID | Seriousness | Where | What's wrong, in plain language | Why it matters | Breaks | Next step | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|
| R-1 | [Must fix / Should fix / Question / Note] | [e.g., `src/app/views.py`, `sign_in()`] | [Plain description] | [Who could be affected, and how] | [e.g., "Spec 11.1" / "Reviewer's opinion"] | [e.g., "SDET chat: add a test; then Software Engineer chat: fix"] | | |

## 4. Things Done Well

- [A few lines on what was checked and found sound, e.g., "Email
  addresses are decrypted in one place only, and only to send email."]

## 5. Questions for the Stakeholders

<!-- Write "None" if empty. Each also appears as a "Question" finding. -->

- [Question, and why it matters]

## 6. Limits of This Review

- [What couldn't be checked, e.g., "Not run against the live servers'
  database"]
- [Assumptions made, e.g., "Reviewed the code as it was in the folder on
  YYYY-MM-DD"]
- An AI reviewer can miss problems or misjudge them. This report is one of
  three independent review rounds (two code reviews, then a hands-on
  review, with polishing by the builder in between), and a person decides
  on every finding.

## 7. Change Log

<!-- Newest at the bottom. Never delete rows. Add a row when the person's
decisions are filled in, and when a fixed finding is checked again. -->

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | [Reviewer] |
