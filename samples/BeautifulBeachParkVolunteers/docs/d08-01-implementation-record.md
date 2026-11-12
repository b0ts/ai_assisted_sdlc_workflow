# BeautifulBeachPark Volunteers: Implementation Record

**Document:** d08-01 · **Step:** 8, Implementation · **Version:** 1.1
· **Last updated:** 2026-10-25 · **Status:** In review: round 1 closed; round 2 (Claude Code) next
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
| Latest test result | 58 of 58 pass at full length (Run 11, 2026-10-26, after the third pass of round 1 fixes) |
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
| Round 2: independent code review | A new Claude Code session, prompt c08-02 and `/security-review`: report `d08-04-code-review-claude.md` | Next: round 1 closed on 2026-11-11. (An early Claude Code review was run on 2026-10-25, before the reviews were put in order; it's kept for the record as [`d08-04-code-review-claude-trial.md`](d08-04-code-review-claude-trial.md). Its two Must-fix items match Codex's R-2 and R-3. The round 2 reviewer mustn't read it.) | — |
| Round 3: hands-on review | A person uses the running app (prompt c08-03): report [`d08-05-hands-on-review.md`](d08-05-hands-on-review.md) | Not yet: starts when round 2 is settled. The session plan is ready | — |

> The three review rounds run one after another: each round's findings
> are decided, fixed, and re-reviewed before the next starts. Reviewers
> skip these rows, so each review stays independent.

## 8. Requests to Change a Test

| Request | Test ID | Reason | SDET's answer | Outcome |
|---|---|---|---|---|
| TC-1 | All | Run 2: every test failed because the tests opened the app over plain HTTP and the app redirected them to HTTPS, as Spec 11.1 requires | **Test wrong, code right.** The shared setup should open the app at its `https://` address; T-SEC-02 keeps checking plain HTTP on purpose. | `tests/conftest.py` fixed; no expected result changed (d07-01 v1.1). Run 3: 37 of 38. |
| TC-2 | T-MK-01 | Run 3: flagged a coordinator's own earlier title, which happened to be an email address, as an email "shown"; counted `&lt;` as four characters; and, with another random seed, flagged " 1YY1" although the app saved it as `1YY1` | **Test wrong, code right.** Text the coordinator typed may reappear; titles are measured as people read them; usernames are checked as saved. No one else's email may appear, and nothing saved may break a rule, as before. | `tests/test_monkey.py` fixed (d07-01 v1.1). Run 4: 38 of 38. |
| TC-3 | T-MK-01 | Run 8: flagged a volunteer's email "shown" after sending a message. "Send" now returns to My Tasks (d05-01 v1.2), where a random S-7 title, `test_vol_01@example.test`, appeared again | **Test wrong, code right.** As in TC-2, text the coordinator typed may reappear; the S-9 check now allows the S-7 titles too. | `tests/test_monkey.py` fixed (d07-01 v1.2). Run 9: 51 of 51. |

## 9. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| Confirm the wording of messages d05-01 Section 9 didn't cover: an invalid sign-in link, the privacy box not ticked, an invalid email, a missing title, a long description, a missing date or time, no slots, too many slots, "Task posted," an empty message, a canceled sign-up, and a slot that has already started | Designer: UI/UX Document | The code needed a message for each case; they are marked "Added in Step 8" in `src/bbpv/wording.py` | Answered by d05-01 v1.2, Section 9, "Added in v1.2" (round 1, R-5) |

### Future Version List

Findings decided "Future Version": worth doing, but not in version 1.0.
They are considered in Step 10 (Maintenance).

| Finding | From | What it is |
|---|---|---|
| R-18 | Round 1, re-review 3 (Codex) | When the email service is slow, background sends hold database connections, so several at once could slow other pages |

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
