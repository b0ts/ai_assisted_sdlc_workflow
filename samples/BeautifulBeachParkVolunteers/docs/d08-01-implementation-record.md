# BeautifulBeachPark Volunteers: Implementation Record

**Document:** d08-01 · **Step:** 8, Implementation · **Version:** 1.0
· **Last updated:** 2026-12-11 · **Status:** Approved
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
| Latest test result | 38 of 38 pass at full length (Run 4, 2026-12-08) |
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
| Other | Volunteer Program Manager, 2026-10-19 | Confirmed that a volunteer software developer would do the person's code review |

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
| Person's code review | A volunteer software developer read all of `src/` | Pass, with two small wording fixes in code comments | Volunteer developer, 2026-12-10 |

## 8. Requests to Change a Test

| Request | Test ID | Reason | SDET's answer | Outcome |
|---|---|---|---|---|
| TC-1 | All | Run 2: every test failed because the tests opened the app over plain HTTP and the app redirected them to HTTPS, as Spec 11.1 requires | **Test wrong, code right.** The shared setup should open the app at its `https://` address; T-SEC-02 keeps checking plain HTTP on purpose. | `tests/conftest.py` fixed; no expected result changed (d07-01 v1.1). Run 3: 37 of 38. |
| TC-2 | T-MK-01 | Run 3: flagged a coordinator's own earlier title, which happened to be an email address, as an email "shown"; counted `&lt;` as four characters; and, with another random seed, flagged " 1YY1" although the app saved it as `1YY1` | **Test wrong, code right.** Text the coordinator typed may reappear; titles are measured as people read them; usernames are checked as saved. No one else's email may appear, and nothing saved may break a rule, as before. | `tests/test_monkey.py` fixed (d07-01 v1.1). Run 4: 38 of 38. |

## 9. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| Confirm the wording of messages d05-01 Section 9 didn't cover: an invalid sign-in link, the privacy box not ticked, an invalid email, a missing title, a long description, a missing date or time, no slots, too many slots, "Task posted," an empty message, a canceled sign-up, and a slot that has already started | Designer: UI/UX Document | The code needed a message for each case; they are marked "Added in Step 8" in `src/bbpv/wording.py` | Logged for d05-01 v1.2; the code works with the current wording meanwhile |

## 10. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| Only one volunteer developer can review code | Medium | Medium | The Volunteer Program Manager will recruit a second reviewer before Phase 2 |
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
