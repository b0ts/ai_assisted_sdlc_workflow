# BeautifulBeachPark Volunteers: Implementation Record

**Document:** d08-01 · **Step:** 8, Implementation · **Version:** 1.3
· **Last updated:** 2026-11-12 · **Status:** In review: rounds 1 and 2 closed; polished and re-reviewed; round 3 (hands-on) next
· **Owner:** Software Engineer (Implementation chat)

> **Sample document.** BeautifulBeachPark, its city, its people, and Parks
> IT are made up, but the code and the runs are real: `src/` holds the
> working app, and every run in Section 5 really happened. Section 8 shows
> two requests to change a test that the SDET accepted, because the tests,
> not the code, were wrong. Every run is recorded in full in the Test
> Results Log (d07-02 v1.1).

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Source PRD | d03-01 v1.1, 2026-09-18 |
| Source Spec | d04-01 v1.1, 2026-09-30 |
| Source UI/UX Document and Style Guide | d05-01 v1.1, 2026-10-13; d05-02 v1.0 |
| Source System Infrastructure Document | d06-01 v1.1, 2026-10-13 |
| Source Test Plan | d07-01 v1.0, 2026-10-16 (v1.1 after TC-1 and TC-2); runs recorded in d07-02 v1.1 |
| Test sign-off | D11, 2026-10-16 |
| Phase covered | Phase 1: UC-1 to UC-7, email reminders |
| Where the code lives | `src/` |
| Built with | Claude Code, working in the project folder, using the local environment only |
| Latest test result | 74 of 74 pass at full length (Run 24, 2026-11-12, after polishing and its code re-review) |
| Build in one sentence | Claude Code wrote the whole app in one session, in the order of the Build Plan, then ran the tests; the runs found two problems in the tests, which the SDET fixed, and all 38 passed. |

## 2. Inputs

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | d03-01 v1.1 | UC-1 to UC-7 |
| Software Design Specification | d04-01 v1.1 | Python web service, PostgreSQL, email service (Section 5); requests (Section 7); DD-5 single-step sign-up (Section 13); Security & Compliance (Section 11) |
| UI/UX Document | d05-01 v1.1 | Screens S-1 to S-10; exact wording (Section 9) |
| Style Guide and design files | d05-02 v1.0; `assets/design-tokens.json`; `assets/mockups/` | Colors, fonts, spacing, and the HTML mockups |
| System Infrastructure Document | d06-01 v1.1 | Local environment with a pretend inbox; the live server requirements in Section 5.1 (Python 3.12, PostgreSQL 16, settings from environment variables) |
| Test Plan and tests | d07-01 v1.0; `tests/`, including the contract in `tests/README.md` | 38 tests, all failing at the start |
| Other | Volunteer Program Manager, 2026-10-19 | Agreed the app would get three independent reviews, one after another (a Codex code review, then a new Claude Code session's code review, both prompt c08-02, then a volunteer's hands-on review, prompt c08-03), and that the Park Manager would decide on every finding |

## 3. Build Plan

| Piece | What is built | Use cases | Screens | Tests it must pass | Status |
|---|---|---|---|---|---|
| B-1 | Project setup, database tables, wording file | — | — | None; the tests can now reach the app | Done |
| B-2 | Sign-in links and account creation, including the block-list check | UC-2 | S-1, S-2 | T-02-01 to T-02-05, T-SEC-05 | Done |
| B-3 | Posting a task with one-hour slots | UC-1 | S-7 | T-01-01 to T-01-05 | Done |
| B-4 | Open slots and signing up, in a single database step (DD-5) | UC-3 | S-3, S-4 | T-03-01 to T-03-06, T-SEC-02 | Done |
| B-5 | Daily reminder job | UC-3 | — | T-03-07 | Done |
| B-6 | My sign-ups and canceling | UC-4 | S-5 | T-04-01 to T-04-03 | Done |
| B-7 | My tasks and rosters | UC-5 | S-6, S-8 | T-05-01 to T-05-04 | Done |
| B-8 | Messaging a volunteer through the server | UC-6 | S-9 | T-06-01, T-06-02 | Done |
| B-9 | Blocking and undoing a block | UC-7 | S-10 | T-07-01 to T-07-03 | Done |
| B-10 | Whole-app checks: privacy on every screen, forms, speed, accessibility, random input | All | All | T-SEC-01, T-SEC-03, T-SEC-04, T-QR-01, T-QR-02, T-MK-01, T-MK-02 | Done |

**Coverage check:** All 38 tests in d07-01 appear in exactly one piece.
The pieces were written in this order in one session, rather than one run
per piece: with the tests and the contract already written, Claude Code
could build the whole app before the first run.

## 4. Tools, Languages, and Libraries

| Item | Chosen | Spec section | Why |
|---|---|---|---|
| Programming language | Python (3.10 or newer; 3.12 on Parks IT's servers) | d04-01 Section 5; d06-01 Section 5.1 | Named in the Spec for the application server |
| Framework | Flask | d04-01 Section 5 | The Spec's example; small and well known |
| Database | SQLite in the local environment; PostgreSQL 16 on Parks IT's servers, through SQLAlchemy | d04-01 Section 5; d06-01 Section 5.1 | The same code works with both, so the local environment needs no database server |
| Email encryption | The `cryptography` library (Fernet) | d04-01 Section 11.1, DD-4 | Emails stored encrypted; scrambled copies for sign-in and the block list |
| Web pages | HTML, CSS, and a little JavaScript (the end time follows the start time on S-7) | d04-01 Section 5 | Built from the HTML mockups and design tokens |
| Test framework | pytest, with Playwright driving a real browser for T-QR-01 and T-QR-02 | d07-01 Section 4 | Chosen with the SDET in Step 7 |
| Coding tool | Claude Code | — | Can run the tests itself after every change |

## 5. Progress

| Run | Date | What changed | Tests passing |
|---|---|---|---|
| 1 | 2026-10-15 | Step 7 first run: nothing built | 0 of 38 (2 blocked) |
| 2 | 2026-12-07 | B-1 to B-10: the whole app, written in one session | 0 of 38: every test failed for the wrong reason (TC-1) |
| 3 | 2026-12-07 | TC-1 fixed by the SDET; monkey tests shortened for a quick check | 37 of 38: T-MK-01 false alarm (TC-2) |
| 4 | 2026-12-08 | TC-2 fixed by the SDET; full length | 38 of 38 |
| 7 | 2026-10-25 | Round 1: documents updated (PRD 1.2, Spec 1.2, d05-01 1.2, d06-01 1.4), then 13 new tests and the a.m./p.m. format (d07-01 1.2), run against the old code | 14 of 47 quick tests: the new ones failed for the right reasons |
| 8 | 2026-10-25 | Round 1 fixes: email queue with retries (R-2), one-step sign-in links (R-1), 12-month `clean-up` (R-3), confirmation email (R-4), all wording in `wording.py` (R-5), 10 sign-in emails a day (R-6), "Add another slot," counter, back to the roster (R-9), `PARK_TIMEZONE` (R-10), task limits (R-12), a.m./p.m. (R-13) | 50 of 51: T-MK-01 false alarm (TC-3) |
| 9 | 2026-10-25 | TC-3 fixed by the SDET; full length | 51 of 51 |
| 10 | 2026-10-26 | Second pass after Codex's re-review: 5 new tests first (d07-01 1.3), then: reminders claimed one at a time and fixed 5-minute retries with expiry (R-2); every word on the pages moved into `wording.py` (R-5); the email limit counted after recording, with the account locked (R-6); failure reasons with no address (R-14); a page sends only its own email, waiting at most 5 seconds (R-15) | 56 of 56 |
| 11 | 2026-10-26 | Third pass after Codex's second re-review: the time words moved into `wording.py` (R-5); a page waits at most 5 seconds in all, the send finishing in the background (R-15); T-SEC-08 runs its two requests side by side (R-17) | 58 of 58 |
| 12 | 2026-11-11 | Round 2: documents updated (PRD 1.3, Spec 1.3, d05-01 1.3, d06-01 1.5, d08-02 1.3), then 10 new tests and TC-4 (d07-01 1.5), run against the old code | 12 of 64 quick tests: every test that signs in failed, because opening a link still signed in (R2-4); each other new test failed for its own reason |
| 13 | 2026-11-11 | Round 2 fixes: a line break counts as one character (R2-1); an email already in use gets the same reply, and its owner a sign-in link (R2-2); the sign-in and create-account pages answer straight away and send in the background (R2-3); a "Finish signing in" page with a "Sign in" button (R2-4); no database connection held while sending (R2-5, and round 1's R-18); the email service's certificate checked, with `SMTP_CA_FILE` (R2-6); Waitress named and installed (R2-7); `CHECK_FORM_TOKENS` so T-SEC-12 can test the form tokens (R2-8); blocking cancels upcoming sign-ups (R2-9) | 68 of 68, with one warning in the test helper |
| 14 | 2026-11-11 | A background sender is listed only once it has started; full length | 68 of 68 |
| 15 | 2026-11-11 | Re-review R2-14 decided Fix: PRD UC-2 step 4 and 4a, Spec DD-13, d05-01 flow; T-02-07 added and TC-5 (d07-01 1.6), run against the old code | 64 of 65 quick tests: T-02-07 failed for the right reason |
| 16 | 2026-11-11 | R2-14 fix: Create Account saves only an account request (new `account_requests` table); the account is made at "Sign in"; a queued email can go to a request's encrypted address (`outbox.to_encrypted`); `clean-up` removes expired requests. Full length | 69 of 69 |
| 17 | 2026-11-11 | Re-review 2 R2-17 decided Fix: Spec Section 6 and DD-13; T-02-08 added (d07-01 1.6), run against the old code | 65 of 66 quick tests: T-02-08 failed for the right reason |
| 18 | 2026-11-11 | R2-17 fix: an email may have several account requests, each link working until one becomes the account, then the rest are removed; on PostgreSQL the email's lookup key is locked so the daily limit holds. Full length | 70 of 70 |
| 19 | 2026-11-12 | Polishing item P-1 (the Park Manager, before round 3): S-7's time box made 8:00 a.m. hard to find. PRD 1.4, Spec 1.4, d05-01 1.4 (UX-8); T-01-09 and TC-6 (d07-01 1.7), run against the old code | 66 of 67 quick tests: T-01-09 failed for the right reason |
| 20 | 2026-11-12 | P-1 fix: S-7's start time is a drop-down list, 6:00 a.m. to 10:00 p.m. every 30 minutes, with the end shown as text; the server refuses other start times and works out the end. Full length | 71 of 71 |
| 21 | 2026-11-12 | Polishing item P-2 (the Park Manager): a coordinator couldn't remove a task. PRD 1.4 adds UC-8, Delete a task (no editing: delete and post again); Spec 1.4 and d05-01 1.4 updated; T-08-01 to T-08-03 (d07-01 1.7), run against the old code | 0 of 3 new tests: no "Delete" on S-6 |
| 22 | 2026-11-12 | UC-8 built: "Delete" on S-6 for the coordinator who posted the task, a confirm page saying how many volunteers will be told, one "Canceled" email per volunteer (queued in the same step as the delete), "Task deleted." Full length | 74 of 74 |
| 23 | 2026-11-12 | P-2 follow-up: "Delete" on a task's first slot row looked like it deleted that slot only. d05-01 UX-9: each task has its own heading and "Delete task" button, with its slots listed under it. TC-7 (d07-01 1.7). Full length | 74 of 74 |
| 24 | 2026-11-12 | Code re-review of the polishing changes (round 2 reviewer, report v1.4): R2-21 done, the S-7 missing-time message reworded; R2-20 and R2-22 were document fixes. Full length | 74 of 74 |

(Runs 5 and 6, on Parks IT's servers in Step 9, are in d07-02. Runs 7 to
9 happened for real on 2026-10-25; the sample's story is set around
December 2026.)

**What the runs found:** both problems were in the tests, not the code.

- **Run 2 (TC-1):** the tests opened the app over plain HTTP, so the app,
  correctly, sent every request to HTTPS, and no test reached a screen.
  This is "failing for the wrong reason": the failures said nothing about
  the code. The SDET fixed the shared test setup; no expected result
  changed.
- **Run 3 (TC-2):** T-MK-01 types 1,000 random values into each field.
  One random title was a volunteer's email address, and the test then
  flagged it when the coordinator's own title reappeared on My Tasks. The
  SDET narrowed the check to what the rule means: no one *else's* email
  may appear. A run with a different random seed then flagged a username
  typed with a space in front, which the app trims before saving; the
  test now checks the saved username. Random tests find different things
  each run, which is why the plan runs them often.

**What didn't need fixing:** the hard parts were right the first time
because the Spec spelled them out: taking the last place in a single
database step (DD-5) passed T-03-04 fifty times out of fifty, and a fast
second tap on "Confirm" shows "You're already signed up for this slot"
instead of an error page.

## 6. Screens Built

| Screen | Name | Built from | Matches the mockup? | Checked by and date |
|---|---|---|---|---|
| S-1 | Sign In | d05-01; `s-1-sign-in.html` | Yes | Volunteer Program Manager, 2026-12-10 |
| S-2 | Create Account | d05-01; `s-2-create-account.html` | Yes | Volunteer Program Manager, 2026-12-10 |
| S-3 | Open Slots | d05-01; `s-3-open-slots.html` | Yes | Volunteer Program Manager, 2026-12-10 |
| S-4 | Confirm Sign-Up | d05-01; `s-4-confirm-sign-up.html` | Yes | Volunteer Program Manager, 2026-12-10 |
| S-5 | My Sign-Ups | d05-01; `s-5-my-sign-ups.html` | Yes | Volunteer Program Manager, 2026-12-10 |
| S-6 | My Tasks | d05-01; `s-6-my-tasks.html` | Yes | Two coordinators, 2026-12-10 |
| S-7 | Post a Task | d05-01; `s-7-post-a-task.html` | Yes | Two coordinators, 2026-12-10 |
| S-8 | Roster | d05-01; `s-8-roster.html` | Yes | Two coordinators, 2026-12-10 |
| S-9 | Message | d05-01; `s-9-message.html` | Yes | Two coordinators, 2026-12-10 |
| S-10 | Blocked Volunteers | d05-01; `s-10-blocked-volunteers.html` | Yes | Volunteer Program Manager, 2026-12-10 |

**Differences from the mockups:** None.

## 7. Reviews

| Review | What was checked | Result | By and date |
|---|---|---|---|
| Security and privacy | Every Spec Section 11 item; emails encrypted and never sent to a browser; no secrets in the code (all read from environment variables) | Pass | Software Engineer chat, 2026-12-09; confirmed in the person's review |
| Speed and cost | Only needed data sent to each page; reminder job runs once a day, not every minute | Pass: Open Slots asks only for slots that haven't started, with indexes on slot times; the number of database connections is a setting (`DB_POOL_SIZE`), so it can be fitted to Parks IT's limit of 20 | Software Engineer chat, 2026-12-08 |
| Ready to move | Every row of d06-01 Section 5.1: Python 3.12, PostgreSQL 16, every setting from an environment variable, the reminder job as a command Parks IT's scheduler can run | Pass | Software Engineer chat, 2026-12-09 |
| Licenses | Every library in d08-02 Section 7 | Pass: all open-source licenses that allow this use | Volunteer Program Manager, 2026-12-10 |
| Round 1: independent code review | Codex (OpenAI), prompt c08-02, read-only: report [`d08-04-code-review-codex.md`](d08-04-code-review-codex.md) | Ready after the Must-fix items: 5 Must fix, 6 Should fix, 2 Question. Codex noted it saw an earlier review's summary in this table. **Decided:** 8 Fix (R-1 to R-6, R-9, R-10), 3 Accept as is (R-7, R-8, R-11), 2 Questions answered Yes (R-12, R-13). **Fixed and tested** (Runs 7 to 9, 51 of 51). **Re-review 1** (Mode E, report v1.1): 7 Fixed; 3 Partly fixed (R-2: overlapping reminder runs, retry timing; R-5: some template text; R-6: the limit under simultaneous requests); new R-14 (Must fix: an email error can hold the address) and R-15 (Should fix: pages send the whole queue), both decided Fix. **Second pass fixed and tested** (Run 10, 56 of 56). **Re-review 2** (report v1.2): R-2, R-6, R-14 Fixed; R-5 (a.m., p.m., and "to" still written in the code) and R-15 (the 5-second wait is per step, not in total) partly fixed; new R-16 (Should fix: a queued notice can arrive after a cancel; **Accept as is**) and R-17 (Should fix: T-SEC-08 could hang on PostgreSQL; **Fix**). Stop rule set by the Park Manager: a round ends when no Must-fix finding is left open. **Third pass fixed and tested** (Run 11, 58 of 58). **Re-review 3** (report v1.3, 2026-11-11): R-5, R-15, R-17 Fixed; every Fix confirmed. New R-18 (Should fix: slow background sends can tie up database connections) goes to the Future Version list under the stop rule. **Round 1 closed, 2026-11-11** | Codex, 2026-10-25; decisions by the Park Manager, 2026-10-25 |
| Round 2: independent code review | A new Claude Code session (Claude Opus 5.5), prompt c08-02, read-only: report [`d08-04-code-review-claude.md`](d08-04-code-review-claude.md) | Ready after the Must-fix items: 1 Must fix (a line break counts as 2 characters on the server, so a message or description under the limit can be refused), 7 Should fix, 2 Question, 3 Note. Tests weren't run by the reviewer. Decided 2026-11-11: all 8 Fix; R2-9 and R2-10 Yes. Fixed in Runs 12 to 14 (68 of 68). Re-review 1 (2026-11-11): 9 of 10 fixed; R2-2 partly fixed. New: R2-14 **Must fix** (a second try with the same username still shows whether an email has an account), Notes R2-15 and R2-16. Decided: R2-14 Fix (account made only at "Sign in"), R2-15 do it, R2-16 no notice. Fixed in Runs 15 and 16 (69 of 69). Re-review 2 (2026-11-11): R2-14 and R2-2 fixed; **no Must fix open, so round 2 is closed** (stop rule). New Should fix R2-17 (the first of two Create Account emails stopped working): decided Fix, fixed in Runs 17 and 18 (70 of 70). Re-review 3 (2026-11-11): R2-17 fixed; one Note (R2-18, Spec Change Log), done. **Round 2 closed, 2026-11-12** | Claude Code (new session), 2026-11-11; decisions by the Park Manager, 2026-11-11 |
| Polishing | The Park Manager, who built the app, ran it and fine-tuned it with Claude (prompt c08-04): log [`d08-06-polishing-log.md`](d08-06-polishing-log.md) | 2 items, both Fix now: P-1 (the start-time picker; Bug) and P-2 (no way to remove a task; Requirement, new UC-8), with a Usability follow-up (UX-9). Runs 19 to 23 (74 of 74). Two questions answered as designed. **Code re-review of the polishing changes** (round 2 reviewer, report v1.4, 2026-11-12): no Must fix; R2-19 (Should fix, a rare timing gap) to the Future Version list; Notes R2-20 to R2-22 done. **Polishing done** | Park Manager, with Claude, 2026-11-12 |
| Round 3: hands-on review | People who weren't involved use the running app (prompt c08-03): report [`d08-05-hands-on-review.md`](d08-05-hands-on-review.md) | Ready to start: the session plan is ready (v0.3) | — |

> The three review rounds run one after another: each round's findings
> are decided, fixed, and re-reviewed before the next starts. Reviewers
> skip these rows, so each review stays independent.

## 8. Requests to Change a Test

| Request | Test ID | Reason | SDET's answer | Outcome |
|---|---|---|---|---|
| TC-1 | All | Run 2: every test failed because the tests opened the app over plain HTTP and the app redirected them to HTTPS, as Spec 11.1 requires | **Test wrong, code right.** The shared setup should open the app at its `https://` address; T-SEC-02 keeps checking plain HTTP on purpose. | `tests/conftest.py` fixed; no expected result changed (d07-01 v1.1). Run 3: 37 of 38. |
| TC-2 | T-MK-01 | Run 3: flagged a coordinator's own earlier title, which happened to be an email address, as an email "shown"; counted `&lt;` as four characters; and, with another random seed, flagged " 1YY1" although the app saved it as `1YY1` | **Test wrong, code right.** Text the coordinator typed may reappear; titles are measured as people read them; usernames are checked as saved. No one else's email may appear, and nothing saved may break a rule, as before. | `tests/test_monkey.py` fixed (d07-01 v1.1). Run 4: 38 of 38. |
| TC-3 | T-MK-01 | Run 8: flagged a volunteer's email "shown" after sending a message. "Send" now returns to My Tasks (d05-01 v1.2), where a random S-7 title, `test_vol_01@example.test`, appeared again | **Test wrong, code right.** As in TC-2, text the coordinator typed may reappear; the S-9 check now allows the S-7 titles too. | `tests/test_monkey.py` fixed (d07-01 v1.2). Run 9: 51 of 51. |
| TC-4 | Shared setup, T-02-01, T-SEC-05, T-SEC-06, T-EM-01, T-EM-07, T-07-01, browser tests | Round 2 decisions changed what the tests must do: opening a sign-in link no longer signs in (R2-4); the sign-in page no longer waits for its email (R2-3); the block confirm box has new wording (R2-9) | **Tests changed to follow approved documents** (PRD 1.3, Spec 1.3, d05-01 1.3). They press "Sign in" on the page the link opens; the test client waits for emails sent in the background; T-EM-07 uses S-9 | d07-01 v1.5. Run 14: 68 of 68 |
| TC-5 | T-02-02 | Re-review finding R2-14: an account now exists only once its owner presses "Sign in" (PRD v1.3, UC-2 step 4), so T-02-02's second try no longer met a taken username | **Test changed to follow the approved PRD.** It signs in from the first link before trying the username again | d07-01 v1.6. Run 16: 69 of 69 |
| TC-6 | T-01-07, T-04-03 | Polishing P-1: S-7's start time became a list (UX-8). T-01-07 looked only for text boxes, and T-04-03 used 11:50, a time no longer allowed | **Tests changed to follow the approved design** (PRD 1.4, d05-01 1.4): T-01-07 also counts lists; T-04-03 uses 11:30 | d07-01 v1.7. Run 20: 71 of 71 |
| TC-7 | T-01-06, T-03-04, T-MK-01 | Polishing P-2 follow-up: S-6 lists each task under its own heading (UX-9), so the task's title appears once, not on every slot row | **Tests changed to follow the approved design** (d05-01 1.4): they read S-6 task by task, with a shared helper | d07-01 v1.7. Run 23: 74 of 74 |

## 9. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| Confirm the wording of messages d05-01 Section 9 didn't cover: an invalid sign-in link, the privacy box not ticked, an invalid email, a missing title, a long description, a missing date or time, no slots, too many slots, "Task posted," an empty message, a canceled sign-up, and a slot that has already started | Designer: UI/UX Document | The code needed a message for each case; they are marked "Added in Step 8" in `src/bbpv/wording.py` | Answered by d05-01 v1.2, Section 9, "Added in v1.2" (round 1, R-5) |

### Future Version List

Findings decided "Future Version": worth doing, but not in version 1.0.
They are considered in Step 10 (Maintenance).

| Finding | From | What it is |
|---|---|---|
| ~~R-18~~ | Round 1, re-review 3 (Codex) | When the email service is slow, background sends hold database connections, so several at once could slow other pages. **Taken off the list 2026-11-11:** round 2 found it too (R2-5), and the Park Manager chose Fix; fixed in Run 13 (Spec DD-12) |
| R2-19 | Round 2 reviewer, re-review of the polishing changes | If a volunteer signs up in the same split second the coordinator deletes the task, they can be told "You're signed up" and never get the "Canceled" email. Suggested fix: the delete first closes the task's slots, then lists whom to tell |

## 10. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| An AI reviewer misses a real problem | Medium | Medium | Two reviewers from different companies; the tests; a professional developer's review if one becomes available |
| A library stops being updated | Low | Medium | Libraries are checked for updates in Step 10 |

**Assumptions:**

- Real email delivery into real inboxes works the same as the test inbox.
  To be checked by hand in Step 9 (d07-01 Section 3).
- The code was tested on SQLite. PostgreSQL is used only on Parks IT's
  servers; the full suite runs there in Step 9 before any real user.

**Open questions:**

- None. (A second contact for Parks IT, I2 in the Tracking Checklist, is
  still open, but it is needed before the move in Step 9, not for this
  hand-off.)

## 11. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-12-11 | First version | — | Park Manager (D12, 2026-12-11) |
| 1.1 | 2026-10-25 | Round 1: decisions, fixes, Runs 7 to 9, TC-3 | Round 1 code review (Codex) | Waiting for Codex's re-review, then the Park Manager |
| 1.2 | 2026-11-11 | Round 2: decisions, fixes, Runs 12 to 18, TC-4, TC-5; R2-14, R2-17; R-18 fixed and taken off the Future Version list | Round 2 code review (Claude Code) | Waiting for Claude Code's re-review, then the Park Manager |
| 1.3 | 2026-11-12 | Polishing (d08-06): P-1, P-2 and its follow-up, Runs 19 to 23, TC-6 and TC-7 | Polishing before round 3 | Park Manager, 2026-11-12 |
