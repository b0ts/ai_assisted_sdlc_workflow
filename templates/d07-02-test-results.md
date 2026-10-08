# [Project name]: Test Results Log

<!-- Template d07-02. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Test Results Log records what happened EACH TIME the tests in the Test
Plan (d07-01) were run. The SDET starts it in Step 7 with Run 1, in which
every test should FAIL, because nothing has been built yet. The Software
Engineer adds a row to the Run History for every run in Step 8, until every
test passes. Never delete runs; the history shows the progress. -->

**Document:** d07-02 · **Step:** 7, Test Creation (continued in Step 8) · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Red: tests failing / Green: all tests pass / Blocked]
· **Owner:** SDET (Test Creation chat); runs added by the Software Engineer (Implementation chat)

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Test Plan | [d07-01, version, date] |
| Test environment | [From d06-01 Section 4] |
| Total tests | [Number, matching d07-01 Section 1] |
| Latest run | [Run number, date] |
| Latest result | [e.g., "0 pass, 42 fail, 0 blocked"] |

## 2. What the Results Mean

| Result | Meaning |
|---|---|
| **Pass** | The test ran and the expected result happened. |
| **Fail** | The test ran and the expected result did not happen. In Run 1, this is correct: the feature isn't built yet. |
| **Blocked** | The test could not run at all, e.g., the test environment was down. Not the same as Fail. |
| **Fail (wrong reason)** | The test failed, but not because the feature is missing, e.g., a typo in the test. The test must be fixed by the SDET. |

## 3. Run History

<!-- One row per run, newest at the bottom. "Changed since last run" is what
was built or fixed, in one short phrase. -->

| Run | Date | Run by | Changed since last run | Pass | Fail | Blocked |
|---|---|---|---|---|---|---|
| 1 | [YYYY-MM-DD] | [SDET chat] | [Tests written; nothing built] | 0 | [N] | 0 |

```mermaid
xychart-beta
    title "Tests passing, run by run"
    x-axis [Run 1]
    y-axis "Tests passing" 0 --> [N]
    bar [0]
```

<!-- Add one x-axis label and one bar value per run. -->

## 4. Results by Test (Latest Run)

<!-- One row per test ID in d07-01, in the same order. "Step 7 check" is
filled in by the SDET only, after the last run in Step 7: "Failed for the
right reason" means it failed because the feature isn't built, not because
the test is broken. -->

| Test ID | Use case | Type | Latest result | First passed in run | Step 7 check | Notes |
|---|---|---|---|---|---|---|
| [T-01-01] | [UC-1] | [HP] | [Fail] | [—] | [Failed for the right reason] | [e.g., "Post task" page not built] |

## 5. Summary by Use Case (Latest Run)

| Use case | Tests | Pass | Fail | Blocked |
|---|---|---|---|---|
| [UC-1: Verb phrase] | [N] | [N] | [N] | [N] |
| Security (T-SEC) | [N] | [N] | [N] | [N] |
| Quality (T-QR) | [N] | [N] | [N] | [N] |
| Monkey (T-MK) | [N] | [N] | [N] | [N] |

## 6. Problems Found

<!-- Anything a run revealed that needs action other than writing more
code: a test that looks wrong, a Blocked test, or a requirement that turns
out to be unclear. Write "None" if empty. -->

| Date | Test ID | Problem | Sent to | Outcome |
|---|---|---|---|---|
| [YYYY-MM-DD] | [T-03-04] | [e.g., Test expects old message wording] | [SDET chat] | [e.g., Test fixed in d07-01 v1.1] |

## 7. Change Log

<!-- Newest at the bottom. Runs go in Section 3; record here only changes
to this document's layout or to the Test Plan version it follows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version, with Run 1 | — | [Name] |
