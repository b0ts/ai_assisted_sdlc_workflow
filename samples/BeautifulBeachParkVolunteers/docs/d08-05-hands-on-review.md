# BeautifulBeachPark Volunteers: Hands-On Review Report

**Document:** d08-05 · **Step:** 8, Implementation · **Version:** 0.3
· **Last updated:** 2026-11-12 · **Status:** Session planned; ready to run
· **Owner:** Hands-on reviewer (to be named), helped by the Hands-On Review Helper (prompt c08-03)

> **Sample document.** The park and its people are made up; the app is
> real. This report is at the **Session planned** stage: Section 2 is
> ready, and the rest is filled in after a real person has used the app.
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
| Version tested | `src/` after both code review rounds and polishing (d08-06) (commit to be named once committed) |
| Reviewer | To be filled in |
| Connection to the project | To be filled in (for example, "didn't build it," "stakeholder," or "built the app") |
| Read the code reviews first? | Should be **No**: don't read `d08-04` or d08-01 Section 7 before this session |
| Looked at the code? | To be filled in (optional) |
| Where it ran | To be filled in (for example, "MacBook, Safari, local demo; also a narrow, phone-sized window") |
| Session date and length | To be filled in (allow 60 to 90 minutes) |
| Overall impression | To be filled in, in the reviewer's own words |
| Findings | To be filled in |

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
   private window (in Safari: **File**, then **New Private Window**).
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
| T1 | New volunteer (signed out) | Create your own account, with a username you make up and an email ending in `@example.test`, and sign in with it. | UC-2 | | | |
| T2 | Volunteer (your new account) | Sign up for a Beach Cleanup slot. | UC-3 | | | |
| T3 | Volunteer | Find the list of everything you've signed up for. | UC-3, UC-4 | | | |
| T4 | Volunteer | Change your mind: cancel the Beach Cleanup sign-up. Then sign up for a Pulling Weeds slot instead. | UC-4, UC-3 | | | |
| T5 | Coordinator (`democoordinator`) | Post a new task for next Saturday, "Picnic Area Tidy," with two one-hour slots in the morning, 3 volunteers each. | UC-1 | | | |
| T6 | Volunteer (`sandyhelps`) | Sign up for one of the Picnic Area Tidy slots. | UC-3 | | | |
| T7 | Coordinator | Find out who signed up for that Picnic Area Tidy slot. | UC-5 | | | |
| T8 | Coordinator | Send that volunteer a short message: "Please bring gloves." Then, as the volunteer, find out whether it arrived (pretend inbox). | UC-6 | | | |
| T9 | Coordinator | Block that volunteer. | UC-7 | | | |
| T10 | Volunteer (the blocked one) | Try to sign up for another slot. | UC-7, UC-3 | | | |
| T11 | System Administrator (`demoadmin`) | Find the blocked volunteer and undo the block. Then, as the volunteer, check you can sign up again. | UC-7 | | | |
| T12 | Two volunteers at once | Find a slot with only one place left (or make one: post a task with 1 place). With two browsers, have two volunteers try to take the last place at about the same time. | UC-3 | | | |

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

To be filled in after the session.

## 4. Findings

To be filled in after the session (prompt c08-03, Mode C), from the
reviewer's notes.

| ID | Kind | Seriousness | Screen | What I did | What happened | What I expected | Screenshot | Route | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|---|---|

## 5. Usability Summary

To be filled in after the session.

| Question | Reviewer's answer |
|---|---|
| Which tasks were easy? | |
| Which were hard, and why? | |
| Any words or labels that confused you? | |
| Could a typical user manage without help? | |
| Did anything feel unsafe or too revealing? | |

## 6. Notes on the Code (Optional)

Not reviewed yet.

## 7. Re-Check After Rework

Not yet.

## 8. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 0.1 | 2026-10-25 | Session plan written (prompt c08-03, Mode A) | Hands-On Review Helper |
| 0.2 | 2026-11-12 | Plan checked after round 2; version to test named; `start-demo.command` added | Hands-On Review Helper (Claude) |
| 0.3 | 2026-11-12 | Plan checked after polishing; the owner's notes moved to the Polishing Log (d08-06); the app's address is now port 5050 | Hands-On Review Helper (Claude) |
