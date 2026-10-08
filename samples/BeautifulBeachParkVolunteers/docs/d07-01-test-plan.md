# BeautifulBeachPark Volunteers: Test Plan

**Document:** d07-01 · **Step:** 7, Test Creation · **Version:** 1.0
· **Last updated:** 2026-10-16 · **Status:** Approved
· **Owner:** SDET (Test Creation chat)

> **Sample document.** BeautifulBeachPark, its people, and every username
> and email below are made up. Section 12 shows three requests sent back
> while the tests were being written.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Source PRD | d03-01 v1.1, 2026-09-18 |
| Source Spec | d04-01 v1.1, 2026-09-30 |
| Source UI/UX Document | d05-01 v1.1, 2026-10-13 (v1.0 plus two messages; Section 12) |
| Source System Infrastructure Document | d06-01 v1.1, 2026-10-13 (v1.0 plus a test inbox; Section 12) |
| Infrastructure sign-off | D10, 2026-10-09 |
| Phase covered | Phase 1: UC-1 to UC-7, email reminders |
| Test environment | Test (made-up data only), d06-01 Section 4 |
| Where the tests live | `tests/` |
| Number of tests | 38: 10 happy path, 17 expected failure, 7 bounds, 2 monkey, 2 quality |
| Plan in one sentence | Every use case is tested for its normal path, its refusals, and its limits, with extra checks that no email address ever reaches a volunteer's or coordinator's screen. |

## 2. Inputs

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | d03-01 v1.1 | UC-1 to UC-7 and their acceptance criteria; Section 6 quality requirements |
| Software Design Specification | d04-01 v1.1 | Limits (Section 6), requests and failure replies (Section 7), sequence diagrams (Section 9), Security & Compliance (Section 11) |
| UI/UX Document | d05-01 v1.1 | Screens S-1 to S-10; exact wording (Section 9); accessibility (Section 10); privacy on screen (Section 11) |
| System Infrastructure Document | d06-01 v1.1 | Test environment with `example.test` emails, test inbox, and a reminder job that can be run by hand |

## 3. Scope

**Use cases tested:** UC-1 to UC-7

**Quality requirements tested:** Speed, Accessibility, Privacy and data
(PRD Section 6)

**Not tested in this plan:**

- Reliability (99% available): measured by the uptime alert in d06-01
  Section 9 once the app is live (Step 10).
- Devices and browsers: every test runs in one desktop and one phone-sized
  browser; other browsers are checked by hand in Step 9.
- Delivery of real emails into real inboxes: the test environment never
  sends to real addresses (d06-01 v1.1). Checked by hand in Step 9.
- Text-message reminders: Phase 2 (PRD Section 8).

## 4. Test Approach

| Test type | What it checks | Used for |
|---|---|---|
| Happy path (HP) | The normal flow works | Every use case's main flow |
| Expected failure (EF) | The system refuses what it should, with the exact message from d05-01 | Every alternate flow; every "only" and "never" rule; every Spec Section 11 item |
| Bounds checking (BC) | Behavior at and just past every limit | Username length, title length, places per slot, message length, the last place, an empty roster |
| Monkey testing (MK) | The app survives random input without crashing or leaking an email | Every form and screen |

**Testing tools:** A common Python web-app test framework that drives a
real browser, chosen with the Software Engineer to match the Spec's Python
web service (d04-01 Section 5).

**How to run the tests:** Run the test command in the project folder. It
uses the test environment only. Tests that check email read the test inbox
(d06-01 v1.1).

**How sources are written:** "UC-3 AC2" means the second acceptance
criterion of UC-3 in the PRD. "UC-3 2a" means alternate flow 2a.

## 5. Traceability

| Use case or requirement | Acceptance criterion or rule | Test IDs |
|---|---|---|
| UC-1: Post a task | AC1: every slot exactly one hour | T-01-02 |
| | AC2: 1 to 20 volunteers per slot | T-01-03 |
| | AC3: only coordinators can post | T-01-05 |
| | AC4: appears in the open-slot list straight away | T-01-01 |
| | Spec 6: title up to 60 characters | T-01-04 |
| UC-2: Create an account | AC1: username and email only | T-02-01, T-SEC-04 |
| | AC2: 3 to 20 letters, numbers, or underscores | T-02-03 |
| | AC3: privacy notice before creating | T-02-05 |
| | AC4: blocked email refused, even written differently | T-02-04 |
| | 3a: username taken | T-02-02 |
| UC-3: Sign up for a slot | AC1: places left shown | T-03-01 |
| | AC2: places left drops by one; "Full" at zero | T-03-01, T-03-02 |
| | AC3: never over-filled, even at the same moment | T-03-04, T-MK-02 |
| | AC4: blocked volunteers can't sign up | T-03-06 |
| | AC5: reminder email the day before | T-03-07 |
| | 2a, 2b: slot just taken; already signed up | T-03-03, T-03-05 |
| UC-4: Cancel a sign-up | AC1: reopens one place | T-04-01 |
| | AC2: only your own sign-ups | T-04-02 |
| | AC3: not after the slot starts | T-04-03 |
| UC-5: View a roster | AC1: usernames only, never emails | T-05-01, T-SEC-01 |
| | AC2: empty roster says so | T-05-02 |
| | Spec 11.1: coordinators only | T-05-03 |
| | d05-01 Section 16, request 1: full slots reachable | T-05-04 |
| UC-6: Message a volunteer | AC1: arrives by email; neither sees the other's address | T-06-01 |
| | AC2: up to 500 characters | T-06-02 |
| UC-7: Block a volunteer | AC1: blocked volunteer can't sign up | T-07-01 |
| | AC2: new account with the blocked email refused | T-02-04, T-SEC-03 |
| | AC3: coordinator never sees the email | T-07-01, T-SEC-01 |
| | AC4: only the System Administrator can undo | T-07-02, T-07-03 |
| Spec 11.1 | Emails never sent to the client | T-SEC-01 |
| Spec 11.1 | HTTPS only | T-SEC-02 |
| Spec 11.1 | Block list holds a scrambled copy only | T-SEC-03 |
| PRD 6, Privacy | No real names collected | T-SEC-04 |
| Spec 7, DD-3 | Sign-in link reply never reveals who has an account | T-SEC-05 |

**Coverage check:** Every use case has at least one happy path and at
least one expected failure or bounds test. Every Spec Section 11.1 row
has a security test. No test lacks a source.

## 6. Test Data

| Data | Example values | Used by tests |
|---|---|---|
| Volunteer accounts | test_vol_01 to test_vol_05, at `@example.test` addresses | UC-2 to UC-7 tests |
| Blocked email | `john@example.test`, blocked before T-02-04 runs | T-02-04, T-SEC-03 |
| Coordinator account | test_coord_01 | UC-1, UC-5 to UC-7 tests |
| System Administrator account | test_admin_01 | T-07-03, T-SEC-03 |
| Task | "Test Beach Cleanup," tomorrow, two slots of 2 places each | UC-3 to UC-6 tests |
| Started slot | "Test Pulling Weeds," a slot that started 10 minutes ago | T-04-03 |

## 7. Test Definitions

### UC-1: Post a task

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-01-01 | HP | test_coord_01 opens S-7 and posts "Test Beach Cleanup" with slots starting 9:00 and 10:00, 2 places each. test_vol_01 opens S-3. | Both slots appear on S-3 as 9–10 and 10–11, each with "2 places left." | UC-1 AC4, AC1 |
| T-01-02 | EF | Send a Post task request with a slot from 9:00 to 10:30. (S-7 can't make this, UX-3, so the test checks the server.) | "Each slot must be one hour." Nothing is saved. | UC-1 AC1, 2a |
| T-01-03 | BC | Post slots with 1, 20, 0, and 21 places. | 1 and 20 saved; 0 and 21 refused with "Each slot needs 1 to 20 volunteers." | UC-1 AC2, 2b |
| T-01-04 | BC | Post tasks with titles of 60 and 61 characters. | 60 saved; 61 refused with "Titles can be up to 60 characters." | Spec 6; d05-01 v1.1 |
| T-01-05 | EF | test_vol_01 sends a Post task request. | "Not allowed. Please contact the park office if you think this is wrong." No "Post a task" button appears for volunteers. | UC-1 AC3 |

### UC-2: Create an account

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-02-01 | HP | On S-2, enter test_vol_01 and an `example.test` email, tick "I've read this," tap "Create account." | Account created; S-1 shows "Check your email…"; the sign-in link arrives in the test inbox. S-2 has only the username and email fields. | UC-2 main flow, AC1 |
| T-02-02 | EF | Create test_vol_01 again with a different email. | "That username is taken. Please try another." | UC-2 3a |
| T-02-03 | BC | Try usernames of 2, 3, 20, and 21 characters, and "sandy helps" (a space). | 3 and 20 accepted; the others refused with "Usernames are 3 to 20 letters, numbers, or underscores." | UC-2 AC2; d05-01 v1.1 |
| T-02-04 | EF | `john@example.test` is blocked. Create an account with `j.o.h.n+beach@example.test`. | "We couldn't create this account. Please contact the park office." The message doesn't mention blocking. | UC-2 AC4, 3b; UC-7 AC2 |
| T-02-05 | EF | Fill in S-2 without ticking "I've read this." | "Create account" can't be used; no account is saved. | UC-2 AC3 |

### UC-3: Sign up for a slot

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-03-01 | HP | test_vol_01 opens S-3, taps "Sign up" on 9–10, then "Confirm" on S-4. | S-5 shows "You're signed up! We'll email you a reminder the day before." S-3 now shows "1 place left." | UC-3 main flow, AC1, AC2 |
| T-03-02 | BC | With 1 place left, test_vol_02 signs up. | The slot shows "Full" on S-3 and has no "Sign up" button. | UC-3 AC2 |
| T-03-03 | EF | test_vol_03 is on S-4 for a slot that fills before they tap "Confirm." | S-3 shows "Sorry, this slot was just taken. Here are other open times." | UC-3 2a |
| T-03-04 | BC | With 1 place left, test_vol_02 and test_vol_03 tap "Confirm" at the same moment. Repeat 50 times. | Every time, exactly one succeeds and places left is never below zero. | UC-3 AC3; Spec DD-5 |
| T-03-05 | EF | test_vol_01 signs up for the same slot twice. | "You're already signed up for this slot." | UC-3 2b |
| T-03-06 | EF | A blocked volunteer, test_vol_04, tries to sign up. | "Not allowed. Please contact the park office if you think this is wrong." | UC-3 AC4, 2c |
| T-03-07 | HP | test_vol_01 is signed up for tomorrow and test_vol_02 for the day after. Run the reminder job by hand. | One reminder for tomorrow's slot arrives in the test inbox for test_vol_01; none for test_vol_02. | UC-3 AC5; Spec UC-3 diagram |

### UC-4: Cancel a sign-up

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-04-01 | HP | test_vol_01 taps "Cancel" on S-5, then "Yes, cancel." | The sign-up leaves S-5; the slot shows one more place left on S-3. | UC-4 main flow, AC1 |
| T-04-02 | EF | test_vol_02 sends a Cancel sign-up request for test_vol_01's sign-up. | "Not allowed. Please contact the park office if you think this is wrong." The sign-up stays. | UC-4 AC2 |
| T-04-03 | EF | test_vol_01 tries to cancel the "Test Pulling Weeds" slot that started 10 minutes ago. | "This slot has already started, so it can't be canceled." | UC-4 AC3, 2a |

### UC-5: View a roster

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-05-01 | HP | test_coord_01 opens S-6 and taps "Roster" on a slot with two sign-ups. | S-8 lists both usernames and "2 of 2 places filled," with "Message" and "Block" next to each. | UC-5 main flow, AC1 |
| T-05-02 | BC | test_coord_01 opens the roster of a slot with no sign-ups. | "No one has signed up yet." | UC-5 AC2, 2a |
| T-05-03 | EF | test_vol_01 sends a Get roster request. | "Not allowed. Please contact the park office if you think this is wrong." | Spec 11.1 |
| T-05-04 | HP | A slot is full. test_coord_01 opens S-6. | The full slot is listed with a "Roster" button, and its roster opens. | d05-01 Section 16, request 1 |

### UC-6: Message a volunteer

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-06-01 | HP | On S-8, test_coord_01 taps "Message" next to test_vol_01, writes a message on S-9, and taps "Send." | "Message sent." The message arrives in the test inbox for test_vol_01, from the park's no-reply address; it contains no coordinator email. S-9 never shows test_vol_01's email. | UC-6 AC1 |
| T-06-02 | BC | Send messages of 500 and 501 characters. | 500 sent; 501 refused with "Messages can be up to 500 characters." | UC-6 AC2, 1a |

### UC-7: Block a volunteer

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-07-01 | HP | On S-8, test_coord_01 taps "Block" next to test_vol_04, then "Yes, block" in the confirm box. Then test_vol_04 tries to sign up. | Confirm box and "Blocked." appear with no email shown; test_vol_04's sign-up is refused. | UC-7 main flow, AC1, AC3 |
| T-07-02 | EF | test_coord_01 sends an Undo block request for test_vol_04. | "Not allowed. Please contact the park office if you think this is wrong." test_vol_04 stays blocked. | UC-7 AC4 |
| T-07-03 | HP | test_admin_01 opens S-10 and taps "Undo block" next to test_vol_04. | S-10 lists usernames only; "Block removed."; test_vol_04 can sign up again. | UC-7 1a, AC4 |

## 8. Security and Privacy Tests

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-SEC-01 | EF | As test_vol_01 and as test_coord_01, open every screen they can reach and record every reply the server sends to the browser. | No email address appears anywhere: not on screen, in the page source, or in any reply. | Spec 11.1; PRD 2, 6; d05-01 Section 11 |
| T-SEC-02 | EF | Open S-3 using `http://` instead of `https://`. | The browser is sent to `https://`, and S-3 opens there. Nothing is ever served over plain HTTP. | Spec 11.1 |
| T-SEC-03 | EF | Block test_vol_05, then have test_admin_01 delete the account. Look in the block list and on S-10, then try a new account with test_vol_05's email. | The block list holds only a scrambled copy, never the email. S-10 shows "(account deleted)." The new account is refused. | Spec 11.1, DD-4; UC-7 AC2 |
| T-SEC-04 | EF | Check every form on S-1 to S-10. | No field asks for a real name. | PRD 6, Privacy; UC-2 AC1 |
| T-SEC-05 | EF | On S-1, ask for a sign-in link for an existing email and for an unknown one. Then use a link after it expires. | Both replies are identical: "Check your email. If you have an account, we've sent you a sign-in link." The expired link shows "This link has expired. We've sent a new one." | Spec 7, DD-3; d05-01 Section 9 |

## 9. Quality Requirement Tests

| ID | Area | Steps | Expected result | Source |
|---|---|---|---|---|
| T-QR-01 | Speed | Load S-3 with 50 open slots in a phone-sized browser on a slowed, phone-like connection. | Fully loaded in under 2 seconds. | PRD 6, Speed |
| T-QR-02 | Accessibility | Run an automatic WCAG 2.1 AA check on S-1 to S-10, and measure every button. | No serious problems; every text color at least 4.5 to 1; every button and field has a text label; every button at least 44 by 44 pixels. | PRD 6; d05-01 Section 10 |

## 10. Monkey Testing

| ID | Screens or forms | How | Fails if |
|---|---|---|---|
| T-MK-01 | Every form (S-1, S-2, S-7, S-9) | 1,000 random inputs per field, including very long text, symbols, emoji, and text that looks like code | Crash, error page, anything saved that breaks a rule, or any email address shown |
| T-MK-02 | Every screen, as each role | Random taps, back-button presses, and repeated "Sign up" and "Cancel" taps for 5 minutes | Crash, a slot over-filled or below zero, or any email address shown |

## 11. Rules for Changing Tests

- After sign-off, the tests are **locked**. The Software Engineer (Step 8)
  makes the code pass the tests; never the other way round.
- If a test seems wrong, the Software Engineer writes a request to the SDET
  chat. Only the SDET chat changes a test, and every change is recorded in
  the Change Log with its reason.
- A change that alters what a use case means goes back to the PRD first.

## 12. Requests Sent Back

| Request | Sent to | Reason | Version that answered it |
|---|---|---|---|
| 1. Wording for a username that breaks the rules | Designer: UI/UX Document | T-02-03 needs an exact message; d05-01 Section 9 had none | d05-01 v1.1: "Usernames are 3 to 20 letters, numbers, or underscores." |
| 2. Wording for a title over 60 characters | Designer: UI/UX Document | T-01-04 needs an exact message; d05-01 Section 9 had none | d05-01 v1.1: "Titles can be up to 60 characters." |
| 3. A way for tests to read emails sent to `example.test` addresses | DevOps Engineer: infrastructure | T-02-01, T-03-07, T-06-01, and T-SEC-05 must check emails without sending to real inboxes | d06-01 v1.1: test inbox in the test environment |

## 13. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| T-03-04 (same-moment sign-up) is hard to repeat exactly | Medium | High | Run it 50 times per test run; one failure counts as Fail |
| Tests run on a slow day give a false Fail for T-QR-01 | Low | Low | Rerun once before reporting; note it in d07-02 Section 6 |

**Assumptions:**

- The test inbox behaves like SampleMail for the content of each email;
  confirm by hand in Step 9.

**Open questions:**

- None

## 14. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-10-16 | First version | — | Park Manager (D11, 2026-10-16) |
