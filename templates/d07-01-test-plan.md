# [Project name]: Test Plan

<!-- Template d07-01. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Test Plan says HOW we will prove the product works, BEFORE anything is
built. Every test must trace back to a use case or acceptance criterion in
the PRD (d03-01), a request or alternate flow in the Spec (d04-01), a
screen or message in the UI/UX Document (d05-01), or a security item in
Spec Section 11. Every in-scope use case must have tests. Results of each
test run go in the Test Results Log (d07-02), not here. Test data is always
made up. Never write real people's information, passwords, or keys in this
document. -->

**Document:** d07-01 · **Step:** 7, Test Creation · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting sign-off / Approved / Sent back]
· **Owner:** SDET (Test Creation chat)

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Source PRD | [d03-01, version, date] |
| Source Spec | [d04-01, version, date] |
| Source UI/UX Document | [d05-01, version, date] |
| Source System Infrastructure Document | [d06-01, version, date] |
| Infrastructure sign-off | [Decision ID and date from the Tracking Checklist, e.g., D10, YYYY-MM-DD] |
| Phase covered | [e.g., Phase 1: UC-1 to UC-5, or "all"] |
| Test environment | [From d06-01 Section 4, e.g., "Local (made-up data only); the full suite runs again on the live servers in Step 9"] |
| Where the tests live | [e.g., `tests/`] |
| Number of tests | [Total, e.g., "42: 9 happy path, 18 expected failure, 12 bounds, 3 monkey"] |
| Plan in one sentence | [e.g., "Every use case is tested for its normal path, its refusals, and its limits, plus random-input checks on every form."] |

## 2. Inputs

<!-- Everything this plan was built from. Anything not listed here was not
used. -->

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | [d03-01, version] | [Use cases and acceptance criteria] |
| Software Design Specification | [d04-01, version] | [Requests, sequence diagrams, Security & Compliance] |
| UI/UX Document | [d05-01, version] | [Screens, message wording, accessibility] |
| System Infrastructure Document | [d06-01, version] | [Test environment] |
| Other | [Source] | [e.g., the organization's accessibility rules] |

## 3. Scope

**Use cases tested:** [e.g., UC-1 to UC-7]

**Quality requirements tested:** [e.g., Speed, Accessibility, Privacy, from
PRD Section 6]

**Not tested in this plan:** <!-- Write "None" if empty. Give a reason for
each, e.g., "UC-6: moved to Phase 2." -->

- [Item, and why]

## 4. Test Approach

<!-- Plain language. Explain which types of test are used and how the tests
are run. Use all four types unless there is a reason not to. -->

| Test type | What it checks | Used for |
|---|---|---|
| Happy path (HP) | The normal flow works | [e.g., Every use case's main flow] |
| Expected failure (EF) | The system refuses what it should, with a clear message | [e.g., Every alternate flow; every security rule] |
| Bounds checking (BC) | Behavior at and just past every limit | [e.g., Text lengths, slot counts, times] |
| Monkey testing (MK) | The system survives random input without crashing or leaking data | [e.g., Every form and screen] |

**Testing tools:** [e.g., "The test framework named in Spec Section 5," or
"TBD, chosen with the Software Engineer"]

**How to run the tests:** [One or two sentences, e.g., "Run the test
command in the project folder; it uses the test environment only."]

## 5. Traceability

<!-- Required. One row per acceptance criterion in the PRD, plus one per
Spec Section 11 item. Every row needs at least one test. Flag any row with
no tests, and any test with no row. -->

| Use case or requirement | Acceptance criterion or rule | Test IDs |
|---|---|---|
| [UC-1: Verb phrase] | [Criterion, copied from the PRD] | [T-01-01, T-01-02] |
| [Spec 11.1] | [e.g., Emails never shown to coordinators] | [T-SEC-01] |

**Coverage check:** [e.g., "Every in-scope use case has at least one happy
path and one expected failure test. No test lacks a source."]

## 6. Test Data

<!-- Made-up data the tests create or expect. Never copy real people.
Name the data clearly so no one mistakes it for real, e.g., "test_vol_01". -->

| Data | Example values | Used by tests |
|---|---|---|
| [e.g., Volunteer accounts] | [e.g., test_vol_01, test_vol_02] | [e.g., T-03-01 to T-03-06] |
| [e.g., Tasks and slots] | [e.g., "Test Beach Cleanup," 2 slots] | [e.g., T-01-01, T-03-01] |

## 7. Test Definitions

<!-- Copy this block once per use case, in PRD order. IDs are
T-[use case number]-[test number], e.g., T-03-02. Write steps a person
could follow by hand. "Expected result" must be specific and checkable:
quote exact messages from the UI/UX Document. -->

### UC-[N]: [Verb phrase]

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-[NN]-01 | HP | [Setup and actions] | [Exact result] | [e.g., PRD UC-1 criterion 1] |
| T-[NN]-02 | EF | [Setup and actions] | [e.g., Message "..." appears; nothing is saved] | [e.g., PRD UC-1 alternate flow 2a] |
| T-[NN]-03 | BC | [Setup and actions at the limit] | [Result at the limit] | [e.g., Spec Section 6] |

## 8. Security and Privacy Tests

<!-- Required. One or more tests for every item in Spec Section 11. These
use IDs T-SEC-NN. -->

| ID | Type | Steps | Expected result | Source |
|---|---|---|---|---|
| T-SEC-01 | [EF] | [e.g., Coordinator opens a roster] | [e.g., No email address appears anywhere on the page] | [Spec 11.1] |

## 9. Quality Requirement Tests

<!-- One row per PRD Section 6 area that can be tested. Write "Not tested"
with a reason rather than deleting a row. IDs T-QR-NN. -->

| ID | Area | Steps | Expected result | Source |
|---|---|---|---|---|
| T-QR-01 | [e.g., Speed] | [e.g., Load the slot list on a phone-sized screen] | [e.g., Under 2 seconds] | [PRD Section 6] |

## 10. Monkey Testing

<!-- How random input is generated, for how long, and what counts as a
failure. IDs T-MK-NN. -->

| ID | Screens or forms | How | Fails if |
|---|---|---|---|
| T-MK-01 | [e.g., Every form] | [e.g., 1,000 random inputs per field, random taps for 5 minutes] | [e.g., Crash, error page, or any email address shown] |

## 11. Rules for Changing Tests

<!-- Keep this section as written unless the stakeholders agree otherwise. -->

- After sign-off, the tests are **locked**. The Software Engineer (Step 8)
  makes the code pass the tests; never the other way round.
- If a test seems wrong, the Software Engineer writes a request to the SDET
  chat. Only the SDET chat changes a test, and every change is recorded in
  the Change Log with its reason.
- A change that alters what a use case means goes back to the PRD first.

## 12. Requests Sent Back

<!-- Changes the SDET asked the Product Manager (PRD), Architect (Spec),
Designer (UI/UX Document), or DevOps Engineer (infrastructure) to make,
for example an acceptance criterion too vague to test. Write "None" if
there were none. -->

| Request | Sent to | Reason | Version that answered it |
|---|---|---|---|
| [e.g., Say how many characters a username may have] | [Product Manager: PRD] | [Can't write a bounds test without it] | [e.g., d03-01 v1.1] |

## 13. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| [e.g., Test environment is down] | [Low / Medium / High] | [Low / Medium / High] | [e.g., Mark tests Blocked; ask DevOps] |

**Assumptions:**

- [Something believed true but not yet confirmed, and how to confirm it]

**Open questions:** <!-- Write "None" if empty. An open question that
affects a Must-have use case blocks the hand-off. -->

- [Question, and who can answer it]

## 14. Change Log

<!-- Newest at the bottom. Add a row for every revision, including any test
changed at the Software Engineer's request. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
