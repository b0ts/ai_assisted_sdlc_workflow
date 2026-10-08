# [Project name]: Implementation Record

<!-- Template d08-01. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Implementation Record says HOW the software was built: the build plan,
the order the pieces were built in, the progress run by run, the tools and
libraries chosen, the reviews done, and every request sent back to an
earlier step. It does NOT repeat what the product does (the PRD), how it
is designed (the Spec), or how the code is organized (the Developer Guide,
d08-02). Every test result is recorded in the Test Results Log (d07-02);
this record only summarizes it. Never write passwords, keys, tokens, or
real people's information in this document. -->

**Document:** d08-01 · **Step:** 8, Implementation · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / In progress / Awaiting sign-off / Approved / Sent back]
· **Owner:** Software Engineer (Implementation chat)

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Source PRD | [d03-01, version, date] |
| Source Spec | [d04-01, version, date] |
| Source UI/UX Document and Style Guide | [d05-01, version; d05-02, version] |
| Source System Infrastructure Document | [d06-01, version, date] |
| Source Test Plan | [d07-01, version, date] |
| Test sign-off | [Decision ID and date from the Tracking Checklist, e.g., D11, YYYY-MM-DD] |
| Phase covered | [e.g., Phase 1: UC-1 to UC-7] |
| Where the code lives | [e.g., `src/`] |
| Built with | [e.g., "Claude Code, working in the project folder"] |
| Latest test result | [e.g., "38 of 38 pass (Run 12, YYYY-MM-DD)"] |
| Build in one sentence | [e.g., "Built one use case at a time, screens last, until every test passed."] |

## 2. Inputs

<!-- Everything this build was based on. Anything not listed here was not
used. -->

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | [d03-01, version] | [Use cases] |
| Software Design Specification | [d04-01, version] | [Components, data, requests, technology, Security & Compliance] |
| UI/UX Document | [d05-01, version] | [Screens and exact wording] |
| Style Guide and design files | [d05-02, version; design file location] | [Colors, fonts, components] |
| System Infrastructure Document | [d06-01, version] | [Test environment; build-and-test pipeline] |
| Test Plan and tests | [d07-01, version; `tests/`] | [The finish line] |
| Other | [Source] | [e.g., the stakeholders' answers to questions] |

## 3. Build Plan

<!-- Required. The small pieces of work, in the order they will be built.
Each piece names the use cases, screens, and tests it covers. Build the
pieces other pieces depend on first (for example, sign-in before sign-up).
Every test in d07-01 must appear in at least one row. -->

| Piece | What is built | Use cases | Screens | Tests it must pass | Status |
|---|---|---|---|---|---|
| B-1 | [e.g., Project setup and database tables] | [—] | [—] | [e.g., none; the tests can now reach the app] | [Not started / In progress / Done] |
| B-2 | [e.g., Sign-in and account creation] | [UC-2] | [S-1, S-2] | [T-02-01 to T-02-05] | [Status] |

**Coverage check:** [e.g., "All 38 tests in d07-01 appear in at least one
piece."]

## 4. Tools, Languages, and Libraries

<!-- The technology actually used, matched to the Spec. Explain any choice
the Spec left open. The full list of libraries and their licenses goes in
the Developer Guide (d08-02 Section 7). -->

| Item | Chosen | Spec section | Why |
|---|---|---|---|
| Programming language | [e.g., Python] | [e.g., d04-01 Section 5] | [e.g., Named in the Spec] |
| Framework | [e.g., A Python web framework] | [Section] | [Reason] |
| Database | [e.g., A relational database] | [Section] | [Reason] |
| Test framework | [From d07-01 Section 4] | [—] | [Chosen with the SDET] |
| Coding tool | [e.g., Claude Code] | [—] | [Reason] |

## 5. Progress

<!-- A short summary of the run-by-run progress. Every run is recorded in
full in the Test Results Log (d07-02 Section 3); copy only the milestones
here. -->

| Run | Date | Piece finished | Tests passing |
|---|---|---|---|
| [1] | [YYYY-MM-DD] | [Step 7 first run: nothing built] | [0 of N] |
| [N] | [YYYY-MM-DD] | [e.g., B-2: Sign-in and accounts] | [e.g., 9 of 38] |

```mermaid
xychart-beta
    title "Tests passing, by milestone"
    x-axis [Run 1]
    y-axis "Tests passing" 0 --> [N]
    line [0]
```

<!-- Add one x-axis label and one value per row of the table above. -->

## 6. Screens Built

<!-- Required. One row per screen in d05-01. Each screen must be checked
against its mockup and the Style Guide by a person, not only by the
tests. -->

| Screen | Name | Built from | Matches the mockup? | Checked by and date |
|---|---|---|---|---|
| [S-1] | [Sign In] | [d05-01 Section N; design file] | [Yes / Differences listed below] | [Name, YYYY-MM-DD] |

**Differences from the mockups:** [Write "None," or list each with the
request that approved it.]

## 7. Reviews

<!-- Required before hand-off. AI-written code must be reviewed by a
person before it goes live (Spec Section 11). -->

| Review | What was checked | Result | By and date |
|---|---|---|---|
| Security and privacy | [Every item in Spec Section 11; no secrets in the code] | [Pass / Issues listed] | [Name, YYYY-MM-DD] |
| Speed and cost | [e.g., Database indexes; pages send only what they need] | [Result] | [Name, YYYY-MM-DD] |
| Licenses | [Every library in d08-02 Section 7 may be used] | [Result] | [Name, YYYY-MM-DD] |
| Person's code review | [A person read the code and its changes] | [Result] | [Name, YYYY-MM-DD] |

## 8. Requests to Change a Test

<!-- Requests sent to the SDET chat because a test looked wrong. The code
changes to pass the tests, never the other way round. Write "None" if
there were none. -->

| Request | Test ID | Reason | SDET's answer | Outcome |
|---|---|---|---|---|
| [TC-1] | [T-NN-NN] | [Why the test seemed wrong] | [Test wrong, or code wrong] | [e.g., "Code fixed; test unchanged" or "Test changed in d07-01 v1.1"] |

## 9. Requests Sent Back

<!-- Changes the Software Engineer asked an earlier step to make, for
example a request missing from the Spec, or a message missing from the
UI/UX Document. Write "None" if there were none. -->

| Request | Sent to | Reason | Version that answered it |
|---|---|---|---|
| [e.g., Say what happens when ...] | [e.g., Software Architect: Spec] | [Reason] | [e.g., d04-01 v1.2] |

## 10. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| [e.g., A library stops being updated] | [Low / Medium / High] | [Low / Medium / High] | [Action] |

**Assumptions:**

- [Something believed true but not yet confirmed, and how to confirm it]

**Open questions:** <!-- Write "None" if empty. An open question that
affects a Must-have use case blocks the hand-off. -->

- [Question, and who can answer it]

## 11. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
