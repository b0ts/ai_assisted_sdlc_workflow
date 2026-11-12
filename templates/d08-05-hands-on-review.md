# [Project name]: Hands-On Review Report

<!-- Template d08-05. Replace every [placeholder]. Delete all hint comments
like this one, EXCEPT keep the "How to Read This Report" box. Keep every
heading, in this order.
A Hands-On Review Report records what a PERSON found by using the running
app: working through tasks, exploring freely to try to break it (ad-hoc
testing), and judging how easy it is to use. Prompt c08-03 helps prepare
the session and write this report from the person's notes; the findings
are the person's own. It is round 3, the last of the three reviews: it
starts only when both code review rounds (d08-04) are settled and the
app has been polished by the person who built it (d08-06), and it tests
that latest version. The reviewer doesn't read the code reviews or the
Polishing Log first.
The reviewer may look at the code, but doesn't have to.
Never write real people's information here: the app holds only made-up
accounts. -->

**Document:** d08-05 · **Step:** 8, Implementation · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Session planned / Awaiting decisions / Decided / Re-checked]
· **Owner:** Hands-on reviewer ([name and role]), helped by the Hands-On Review Helper (prompt c08-03)

> **How to Read This Report**
>
> This report is about **using** the app, not its code. Each finding is
> something the reviewer noticed while using it. For each one:
>
> - **Kind** says what sort of problem it is: a **Bug** (the app did
>   something wrong), **Usability** (it works, but people struggle), a
>   **Requirement** (something people need is missing from the plan), a
>   **Question** for the stakeholders, or **Praise**.
> - **Route** says where a fix would go back to. A Bug goes to Step 7
>   (a test) and Step 8 (the fix). A Usability finding goes to Step 5
>   (screens and wording) first. A Requirement goes to Step 3 (the PRD).
>   Every fix is followed by all the tests, and a re-check.
>
> Write your **Decision** for each: **Fix**, **Accept as is** (say why),
> **Future Version** (worth doing, but not now), or **Ask**. The round
> ends when no Must-fix finding is left open; after that, a new
> Should-fix finding goes to Future Version unless you choose Fix. Step 8
> is signed off only when every finding is settled.

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Version tested | [e.g., "1.0 at commit 4867cab, after both code review rounds' fixes and polishing"] |
| Reviewer | [Name and role, e.g., "Sam, a volunteer"] |
| Connection to the project | [e.g., "Didn't build it; not an approver" / "Stakeholder" / "Built the app"] |
| Read the code reviews first? | [No / Yes] |
| Looked at the code? | [No / Yes: what] |
| Where it ran | [e.g., "MacBook, Safari, local demo with made-up accounts; also a phone-sized window"] |
| Session date and length | [YYYY-MM-DD, about N minutes] |
| Overall impression | ["In the reviewer's own words"] |
| Findings | [N Bug · N Usability · N Requirement · N Question · N Praise; N Must fix] |

## 2. Session Plan

<!-- Written before the session (prompt c08-03, Mode A). -->

### 2.1 How to Start the App

1. [Plain step, from the Developer Guide]
2. [How to sign in with each made-up account, and open the pretend inbox]
3. [How to stop the app at the end]

### 2.2 Tasks

<!-- One or two per use case, per role. Say WHAT to do, never how.
Results are filled in after the session. -->

| Task | Role | What to do | Use case | Result | About how long | Notes |
|---|---|---|---|---|---|---|
| T1 | [e.g., Volunteer] | [e.g., "Create an account and sign up for the Saturday beach cleanup"] | [UC-2, UC-3] | [Done / Done with difficulty / Not done] | [Minutes] | [Notes] |

### 2.3 Things to Explore

- [e.g., Go back in the middle of signing up; tap buttons twice; leave
  fields empty; type very long or odd text; use a phone-sized window; try
  something your role shouldn't be able to do]

## 3. What Was Explored

<!-- What the reviewer actually tried beyond the tasks. -->

- [What was tried, and what happened in general]

## 4. Findings

<!-- One row per thing noticed, most serious first. Quote the reviewer.
Leave Decision and Decided by empty for the person deciding. -->

| ID | Kind | Seriousness | Screen | What I did | What happened | What I expected | Screenshot | Route | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|---|---|
| H-1 | [Bug / Usability / Requirement / Question / Praise] | [Must fix / Should fix / Question / Note] | [e.g., S-3 Open Slots] | [Steps] | [What the app did] | [What the reviewer expected] | [File name, or "None"] | [e.g., "Step 5 → Step 7 → Step 8"] | | |

## 5. Usability Summary

| Question | Reviewer's answer |
|---|---|
| Which tasks were easy? | [Answer] |
| Which were hard, and why? | [Answer] |
| Any words or labels that confused you? | [Answer] |
| Could a typical user manage without help? | [Yes / Mostly / No, and why] |
| Did anything feel unsafe or too revealing? | [Answer] |

## 6. Notes on the Code (Optional)

<!-- Only if the reviewer chose to look. Otherwise write "Not reviewed." -->

- [Notes, or "Not reviewed"]

## 7. Re-Check After Rework

<!-- Filled in after the fixes (prompt c08-03, Mode E). Write "Not yet"
until then. -->

| Finding | Fixed in (step, version) | Re-checked on | Result | Notes |
|---|---|---|---|---|
| [H-1] | [e.g., "Step 5 d05-01 v1.2; Step 8 version 1.0.1"] | [YYYY-MM-DD] | [Fixed / Partly fixed / Not fixed] | [Anything new becomes a new finding] |

## 8. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | [Reviewer, with the helper] |
