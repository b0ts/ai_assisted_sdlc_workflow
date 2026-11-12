# BeautifulBeachPark Volunteers: Polishing Log

**Document:** d08-06 · **Step:** 8, Implementation · **Version:** 1.1
· **Last updated:** 2026-11-12 · **Status:** Done
· **Owner:** Park Manager (project owner), with the Polishing Partner (Claude, prompt c08-04)

> **Sample document.** The park and its people are made up; the app is
> real, and so is this polishing session. It happened on 2026-11-12, after
> both code review rounds were closed and before round 3's hands-on
> review. It's also where this stage came from: the project owner's quick
> look turned up two real gaps in a few minutes, and the workflow gained a
> Polishing stage (prompt c08-04, template d08-06) as a result.

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
| Product | BeautifulBeachPark Volunteers |
| Version polished | After both code review rounds, at commit f7878b1 (round 2 merged) |
| Polished by | The Park Manager, the project owner, who built the app with Claude |
| Where it ran | MacBook, Chrome, local demo with made-up accounts and the pretend inbox |
| Date and time spent | 2026-11-12, about 90 minutes, including the changes |
| Items | 1 Bug · 1 Requirement (with a Usability follow-up); 2 Fix now · 0 Future Version · 0 Keep as is |
| Documents changed | PRD 1.4, Spec 1.4, UI/UX Document 1.4, Test Plan 1.7, Test Results Log 1.7 |
| Latest test run | Run 24: 74 of 74 at full length (after the code re-review) |
| Version for round 3 | The commit that adds this log (to be named once committed) |

## 2. How the App Was Started

1. In Finder, open `samples/BeautifulBeachParkVolunteers` and double-click
   **start-demo.command** (if macOS asks, choose **Open**). The first time,
   it makes the local settings and the made-up demo data.
2. The browser opens <http://127.0.0.1:5050>. (Not port 5000: on a Mac,
   AirPlay Receiver answers there. The first try at starting the app hit
   this, and the launcher was changed to use 5050.)
3. Sign in with a made-up email (`sandyhelps@example.test`,
   `democoordinator@example.test`, or `demoadmin@example.test`), then
   **Open the pretend inbox** and use the newest link.
4. To stop the app, close its Terminal window.

## 3. What Was Tried

| Role | What was tried | Felt right? |
|---|---|---|
| Volunteer (SandyHelps) | Signed in, looked at the open slots | Yes, after a mistyped email (the "Check your email" reply is the same for unknown emails, by design) |
| Coordinator (DemoCoordinator) | Posted a task | Not at first: see P-1 |
| Coordinator | Looked for a way to remove a task | No: see P-2 |
| System Administrator (DemoAdmin) | Looked at what the role can do | Yes, once explained: see Section 5 |

## 4. Polishing Items

| ID | What I noticed (in my words) | Kind | Decision | What changed | Outcome |
|---|---|---|---|---|---|
| P-1 | "For the coordinator, the time picker is wrong; for example, there is no way to create a task at 8:00 AM." (The browser's time box showed 11 a.m. to 5 a.m. and the current minute; 8:00 a.m. needed scrolling or typing.) | Bug: the UI/UX Document's sketch shows a list ("9:00 ▾"), but the code used the browser's time box | Fix now: a drop-down list, 6:00 a.m. to 10:00 p.m. every 30 minutes. Park Manager, 2026-11-12 | PRD 1.4 (UC-1 AC6), Spec 1.4 (slot start times), UI/UX 1.4 (UX-8, two messages); T-01-09 added; TC-6 (T-01-07, T-04-03) | T-01-09 failed first (Run 19); fixed in Run 20, 71 of 71 |
| P-2 | "When signed in as the coordinator, I can Post a Task, but I don't seem to be able to remove one." | Requirement: no use case covered removing a task | Fix now: "Cancel and Delete a task is enough without an edit, as the Coordinator can always delete and recreate." Park Manager, 2026-11-12 | PRD 1.4 (new UC-8, Delete a task), Spec 1.4 (Delete task request, UC-8 diagram, who may delete), UI/UX 1.4 (confirm page, wording, "Canceled" email); T-08-01 to T-08-03 added | All three failed first (Run 21); built in Run 22, 74 of 74 |
| P-2, follow-up | "Why do I only see delete for some tasks? The Beach Cleanup from 9 to 10 has Delete and the 10 to 11 does not." (One Delete on a task's first slot row looked like it deleted only that slot.) | Usability | Fix now: each task gets its own heading with a "Delete task" button, and its slots listed under it (option 1 of 2). No single-slot delete. Park Manager, 2026-11-12 | UI/UX 1.4 (UX-9, S-6 sketch); T-08-01 checks the layout; TC-7 (T-01-06, T-03-04, T-MK-01 read S-6 task by task) | Run 23, 74 of 74 |

## 5. Answered as Designed

| Question | Answer |
|---|---|
| "What things should the admin be able to do? I only see Blocked." | As designed: the System Administrator's jobs are keeping the app running and undoing blocks (PRD Section 3), and their only screen is Blocked Volunteers (d05-01 S-10). Making coordinator accounts, deleting accounts, and the email and clean-up jobs are commands (d08-02 Section 4). The Park Manager chose no change. |
| "I started with sqndyehlps@example.test and now see a note telling me to check your email." | As designed: a mistyped email gets the same "Check your email" reply as a real one, so no one can use the sign-in page to find out who volunteers (Spec DD-3, DD-10). No email was sent. |

## 6. Hand-Off

- **Future Version items:** R2-19, from the code re-review. (One limit was noted with P-2 and left
  as it is: an email already waiting to send when a task is deleted, such
  as a reminder held up while the email service was down, can still go
  out; the "Canceled" email follows it.)
- **Code re-review of the polishing changes:** Done, 2026-11-12: the round
  2 reviewer (a new Claude Code session, prompt c08-02, Mode E) reviewed
  the changes since commit f7878b1 (d08-04-code-review-claude.md v1.4). No
  Must fix. R2-19 (a rare timing gap when a task is deleted as someone
  signs up) went on the Future Version list; Notes R2-20 to R2-22 (the
  Spec's wording for the "Canceled" email, the S-7 missing-time message,
  and small document slips) were done.
- **Round 3 session plan:** Checked. The tasks still fit; task T5 (post a
  task with two morning slots) now uses the start-time list. The
  instructions for starting the app were updated for
  `start-demo.command` and port 5050.

## 7. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | 2026-11-12 | First version: P-1, P-2 and its follow-up; two questions answered as designed | Park Manager, with the Polishing Partner (Claude) |
| 1.1 | 2026-11-12 | Code re-review of the polishing changes recorded; R2-19 to Future Version | Park Manager, with Claude |
