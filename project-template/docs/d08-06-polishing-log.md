# [Project name]: Polishing Log

<!-- Template d08-06. Replace every [placeholder]. Delete all hint comments
like this one, EXCEPT keep the "How to Read This Log" box. Keep every
heading, in this order.
A Polishing Log records the person who BUILT the app running it for a
sanity check and fine-tuning it with the AI (prompt c08-04). It comes
after both code review rounds (d08-04) and before round 3, the hands-on
review (d08-05), so the people who weren't involved test a polished
version. It is NOT an independent review, and the round 3 reviewers
don't read it.
Never write real people's information here: the app holds only made-up
accounts. -->

**Document:** d08-06 · **Step:** 8, Implementation · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [In progress / Done; code re-review pending / Done]
· **Owner:** [Name and role of the person polishing], with the Polishing Partner (prompt c08-04)

> **How to Read This Log**
>
> Each **item** is something the person who built the app noticed while
> using it, in their own words. For each one:
>
> - **Kind** says what it turned out to be: a **Bug** (the app didn't do
>   what the documents say), **Usability** (it works as designed, but it's
>   awkward or unclear), or a **Requirement** (something needed was
>   missing from the plan). Questions that were answered "working as
>   designed," with no change, are listed in Section 5.
> - **Decision** is the person's: **Fix now**, **Future Version** (worth
>   doing, but not before release), or **Keep as is**.
> - **Outcome** names the documents, tests, and test run that carried the
>   change, so every fix can be traced. Polishing follows the same order
>   as every other change: documents, then a failing test, then the code,
>   then every test.

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Version polished | [e.g., "After both code review rounds, at commit f7878b1"] |
| Polished by | [Name and role, e.g., "Pat, the project owner, who built the app with Claude Code"] |
| Where it ran | [e.g., "MacBook, Chrome, local demo with made-up accounts"] |
| Date and time spent | [YYYY-MM-DD, about N minutes] |
| Items | [N Bug · N Usability · N Requirement; N Fix now · N Future Version · N Keep as is] |
| Documents changed | [e.g., "PRD 1.4, Spec 1.4, UI/UX 1.4, Test Plan 1.7"] |
| Latest test run | [e.g., "Run 23: 74 of 74 at full length"] |
| Version for round 3 | [e.g., "The commit after polishing" or the commit] |

## 2. How the App Was Started

<!-- Plain steps, from the Developer Guide (or a double-click launcher if
the project has one): how to start the app, the address to open, the
made-up accounts, the pretend inbox, and how to stop it. -->

[Steps]

## 3. What Was Tried

<!-- The short list from prompt c08-04, Mode A: the main task for each
role, and whether it felt right. -->

| Role | What was tried | Felt right? |
|---|---|---|
| [e.g., Volunteer] | [e.g., "Signed up for a slot, then canceled it"] | [Yes / Not at first: see P-1] |

## 4. Polishing Items

<!-- One row per item, in the order raised. A follow-up that one fix led
to stays under the same ID ("P-2, follow-up"). -->

| ID | What I noticed (in my words) | Kind | Decision | What changed | Outcome |
|---|---|---|---|---|---|
| P-1 | ["..."] | [Bug / Usability / Requirement] | [Fix now / Future Version / Keep as is], [name], [YYYY-MM-DD] | [Documents and versions; tests added or changed] | [e.g., "Run 20: 71 of 71"] |

## 5. Answered as Designed

<!-- Questions the person asked that turned out to be working as designed,
with no change: what they asked, and the short answer with where it's
written. If the answer led to a change, it's an item in Section 4 instead. -->

| Question | Answer |
|---|---|
| ["..."] | [e.g., "As designed: the System Administrator's only screen is Blocked Volunteers (d05-01 S-10); accounts are made with commands (d08-02 Section 4)"] |

## 6. Hand-Off

<!-- Prompt c08-04, Modes C and D. -->

- **Future Version items:** [IDs, also on the Implementation Record's
  Future Version list, or "None"]
- **Code re-review of the polishing changes:** [Not yet / Done: result]
  (round 2 reviewer, prompt c08-02, Mode E)
- **Round 3 session plan:** [e.g., "Checked: the tasks still fit; the
  instructions for starting the app were updated"]

## 7. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| [1.0] | [YYYY-MM-DD] | [First version] | [Name, with the Polishing Partner] |
