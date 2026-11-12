# BeautifulBeachPark Volunteers: Hands-On Review Report

**Document:** d08-05 · **Step:** 8, Implementation · **Version:** 1.1
· **Last updated:** 2026-11-12 · **Status:** Decided; round 3 closed
· **Owner:** Hands-on reviewer ("the reviewer"), helped by the Hands-On Review Helper (prompt c08-03)

> **Sample document.** The park and its people are made up; the app is
> real, and so is this session: a real person used the app on
> 2026-11-12, and the findings are hers, as relayed by the project owner,
> who sat with her.
> This is **round 3**, the last of the three reviews: the session waits
> until both code review rounds (Codex, then Claude Code) are settled, so
> the person tests the version closest to final. If those rounds change a
> screen, check this plan still fits before the session.
> The plan was written from the PRD (d03-01), the UI/UX Document (d05-01),
> and the Developer Guide (d08-02), without reading the code reviews.
> Checked again on 2026-11-12 after round 2 (v0.2): the tasks still fit.
> Round 2 changed how signing in and creating an account work, and what
> blocking does; the tasks say what to do, not how, so they stay as they
> are. Starting the app is now one double-click.
> Checked again after polishing (v0.3, d08-06): the tasks still fit. The
> reviewer shouldn't read the Polishing Log first.

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
| Product | BeautifulBeachPark Volunteers |
| Version tested | `src/` at commit 93b3fe4 (2026-11-12): after both code review rounds and polishing (d08-06) |
| Reviewer | "The reviewer" (she asked to be called that) |
| Connection to the project | Didn't build it; not an approver. The project owner sat with her and relayed her answers |
| Read the code reviews first? | No. She had never seen the app |
| Looked at the code? | No |
| Where it ran | The project owner's MacBook, Chrome, local demo with fresh made-up data and the pretend inbox; a second, private (incognito) window for T12 |
| Session date and length | 2026-11-12, about 55 minutes (13:34 to 14:28), including free exploring |
| Overall impression | "Cool basic app, love that stalking is restricted ;)"; "Looking good" |
| Findings | 0 Bug · 0 Usability · 0 Requirement · 0 Question · 4 Praise · 1 Note (about the session plan, not the app); 0 Must fix |

## 2. Session Plan

### 2.1 How to Start the App

**The quick way (v0.2):** in **Finder**, open the sample folder
(`samples/BeautifulBeachParkVolunteers`) and double-click
**start-demo.command**. If macOS asks, choose **Open**. It does steps 2 to
4 for you: it makes the local settings and demo data the first time, starts
the app, and opens it in your browser. Then go on to step 5. To stop the
app, close its Terminal window.

The steps by hand: you (or whoever set up the project) only need to do
steps 1 and 2 once.

1. **Set up the project's Python,** if it isn't already: in **Terminal**
   (in **Finder**, choose **Applications**, then **Utilities**, then
   **Terminal**), go to the sample folder and follow the five setup lines
   in the sample's [README](../README.md), starting with
   `python3 -m venv .venv`.
2. **Make the local settings and demo data:** in Terminal, still in the
   sample folder with `(.venv)` at the start of the prompt, type
   `cd src`, then `python infrastructure/setup_local.py`, then
   `flask --app bbpv seed-demo`. (If you see "already exists" or "That
   username is taken," it was done before; that's fine.)
3. **Start the app:** `flask --app bbpv run --port 5050`. Leave this Terminal window
   open while you test.
4. **Open the app:** in your browser, go to <http://127.0.0.1:5050>. (Not
   port 5000: on a Mac, AirPlay Receiver answers there instead of the app.)

   > **The app's address is <http://127.0.0.1:5050>.** If you open a new
   > browser window or tab (including a private or incognito window) and
   > it's blank, the app is still running: click in the address bar at the
   > top, type `http://127.0.0.1:5050`, and press Return to see the app.
5. **Sign in:** type one of the made-up email addresses below and click
   **Send me a sign-in link**. No real email is sent: click **Open the
   pretend inbox** on the sign-in page and click the newest link
   addressed to that email, then finish signing in on the page it opens.

   | Role | Made-up email |
   |---|---|
   | Volunteer | `sandyhelps@example.test` |
   | Volunteer | `shellseeker@example.test` |
   | Volunteer | `tidepooltim@example.test` |
   | Coordinator | `democoordinator@example.test` |
   | System Administrator | `demoadmin@example.test` |

   To switch roles, click **Sign out** at the top of the page and sign in
   as someone else. To be two people at once, use a second browser, or a
   private window (in Safari: **File**, then **New Private Window**; in
   Chrome: **File**, then **New Incognito Window**). A new window opens
   blank: type the app's address, `http://127.0.0.1:5050`, into it.
6. **Stop the app at the end:** close the Terminal window.

**Taking notes:** keep a document open and write as you go: what you
did, what happened, and what you expected. For screenshots on a Mac, open
the **Screenshot** app (in **Applications**, then **Utilities**) and
choose what to capture.

### 2.2 Tasks

Do them in this order. Each says **what** to do, not how: working out how
is part of the test. If you get stuck for more than a couple of minutes,
write down where, and move on.

| Task | Role | What to do | Use case | Result | About how long | Notes |
|---|---|---|---|---|---|---|
| T1 | New volunteer (signed out) | Create your own account, with a username you make up and an email ending in `@example.test`, and sign in with it. | UC-2 | Done | 3 to 5 min | Typed a username with spaces and symbols first: "The app gave me an adequate error message and I was able to fix it easily" (F-1). No confusion |
| T2 | Volunteer (your new account) | Sign up for a Beach Cleanup slot. | UC-3 | Done | Under 30 s | At first she hadn't been asked to sign up (the helper's slip in relaying the task, not the app); once asked: "no confusion" |
| T3 | Volunteer | Find the list of everything you've signed up for. | UC-3, UC-4 | Done | Under 1 min | Found My Sign-Ups straight away |
| T4 | Volunteer | Change your mind: cancel the Beach Cleanup sign-up. Then sign up for a Pulling Weeds slot instead. | UC-4, UC-3 | Done | Under 1 min |  |
| T5 | Coordinator (`democoordinator`) | Post a new task for next Saturday, "Picnic Area Tidy," with two one-hour slots in the morning, 3 volunteers each. | UC-1 | Done | 2 to 3 min | A slip of her own ("user driver error"); nothing wrong in the app |
| T6 | Volunteer (`sandyhelps`) | Sign up for one of the Picnic Area Tidy slots. | UC-3 | Done | Under 2 min |  |
| T7 | Coordinator | Find out who signed up for that Picnic Area Tidy slot. | UC-5 | Done | Under 1 min |  |
| T8 | Coordinator | Send that volunteer a short message: "Please bring gloves." Then, as the volunteer, find out whether it arrived (pretend inbox). | UC-6 | Done | Under 3 min | Sent, and confirmed in the pretend inbox; another small slip of her own |
| T9 | Coordinator | Block that volunteer. | UC-7 | Done | — | "The app asked if I was sure I wanted to block with a button choice" (F-2) |
| T10 | Volunteer (the blocked one) | Try to sign up for another slot. | UC-7, UC-3 | Done | — | Refused: "Not allowed. Please contact the park office if you think this is wrong." in red, with a link to the home page. Afterwards My Sign-Ups showed no sign-ups: blocking had canceled them, as designed (F-3) |
| T11 | System Administrator (`demoadmin`) | Find the blocked volunteer and undo the block. Then, as the volunteer, check you can sign up again. | UC-7 | Done | — | The administrator removed the block; Sandy then signed up for the second Picnic Area Tidy slot |
| T12 | Two volunteers at once | Find a slot with only one place left (or make one: post a task with 1 place). With two browsers, have two volunteers try to take the last place at about the same time. | UC-3 | Done | — | ShellSeeker got the place; Tide Pool Tim saw, in red, "Sorry, this slot was just taken," with the open slots (F-4). The private window opened blank, so she copied the app's address into it (F-5) |

### 2.3 Things to Explore

After the tasks, spend 15 to 30 minutes trying to break it, or just
poking around:

- Go **back** (the browser's back arrow) in the middle of signing up or
  cancelling, then carry on.
- Click buttons **twice** quickly.
- Leave fields **empty**, or type very long text, odd symbols, or emoji,
  into every box you can find.
- Make the browser window **narrow**, like a phone, and repeat a task.
- As a volunteer, try to **reach coordinator pages** (for example, by
  going back to an address you visited as the coordinator).
- Try to post a slot that **isn't one hour**, or a task with **0** or
  **25** volunteers.
- Look for any place where you can see **someone else's email address**.
  You shouldn't find one (apart from the pretend inbox, which is only for
  this demo).
- Read every message the app shows you: is the wording clear? Friendly?
  Would a volunteer who doesn't use computers much understand it?

**For every task, note:** did you finish it (yes, with difficulty, or
no)? About how long did it take? Was anything confusing? Did anything
seem wrong?

## 3. What Was Explored

After the tasks, about 10 minutes of free exploring. In her words: she
"explored back button, double clicks, not filling out fields, restoring
the page, etc." Nothing broke, and nothing showed an error she didn't
expect. She looked for other people's email addresses: "did not see other
folks emails on the app." Earlier, in T1, she had also tried a username
with spaces and symbols on purpose.

## 4. Findings

| ID | Kind | Seriousness | Screen | What I did | What happened | What I expected | Screenshot | Route | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|---|---|
| F-1 | Praise | Note | S-2 Create Account | Typed a username with spaces and symbols | "The app gave me an adequate error message and I was able to fix it easily" | A clear message | — | None: keep it | | |
| F-2 | Praise | Note | Block confirm | Blocked a volunteer as the coordinator | "The app asked if I was sure I wanted to block with a button choice" | — | — | None: keep it | | |
| F-3 | Praise | Note | Every screen | Looked for other people's email addresses, as each role | "Love that stalking is restricted"; "did not see other folks emails on the app" | No one else's email | — | None: keep it | | |
| F-4 | Praise | Note | S-3, S-4 | Two volunteers took the last place at about the same time (T12) | One got it; the other saw "Sorry, this slot was just taken," with the other open slots | Only one gets it | — | None: keep it | | |
| F-5 | Note | Note | (The session plan, not the app) | Opened a private (incognito) window for the second volunteer (T12) | "The google incognito page is blank"; she copied the app's address into it | — | — | Session plan (d08-05 Section 2): say to type <http://127.0.0.1:5050> in the new window. No change to the app | Fix: the plan gives the app's address, with a note on what to do if a new window or tab is blank (Section 2.1, steps 4 and 5) | Project owner, 2026-11-12 |

## 5. Usability Summary

| Question | Reviewer's answer |
|---|---|
| Which tasks were easy? | "Easy tasks." Every task was done, most in under 3 minutes |
| Which were hard, and why? | None in the app: "hard for me to follow simple directions (user error)" |
| Any words or labels that confused you? | "Nothing confused me, except my own brain" |
| Could a typical user manage without help? | "Yes, I think a person could follow the app and volunteer or coordinate" |
| Did anything feel unsafe or too revealing? | No: "did not see other folks emails on the app" |

## 6. Notes on the Code (Optional)

Not reviewed: she didn't look at the code.

## 7. Re-Check After Rework

Not needed unless a finding is marked Fix: no finding is about the app
itself.

## 8. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 2026-10-25 | Session plan written (prompt c08-03, Mode A) | Hands-On Review Helper |
| 0.2 | 2026-11-12 | Plan checked after round 2; version to test named; `start-demo.command` added | Hands-On Review Helper (Claude) |
| 0.3 | 2026-11-12 | Plan checked after polishing; the owner's notes moved to the Polishing Log (d08-06); the app's address is now port 5050 | Hands-On Review Helper (Claude) |
| 1.0 | 2026-11-12 | Session held; results, findings, and usability summary written from the reviewer's answers (prompt c08-03, Mode C) | Hands-On Review Helper (Claude), from the reviewer's answers |
| 1.1 | 2026-11-12 | Report confirmed by the project owner ("She was happy with the app"); round 3 closed. F-5 decided and done: the session plan gives the app's address, and what to do if a new window or tab is blank | Hands-On Review Helper (Claude), decided by the project owner |
