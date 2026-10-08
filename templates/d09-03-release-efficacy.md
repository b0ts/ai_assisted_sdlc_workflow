# [Project name]: Release Efficacy Document, Version [N.N]

<!-- Template d09-03. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Release Efficacy Document records how well the release actually went:
what happened compared with the plan, any problems and rollbacks, early
results against the PRD's success measures, and what to do differently
next time. The Release Manager writes it at the end of the watch period
(d09-01 Section 12), and it is signed off through the Tracking chat before
Step 10 begins. Be honest: a release that needed a rollback, written up
clearly, is more useful than one that "went fine" on paper. Never write
real users' personal information here; use counts. -->

**Document:** d09-03 · **Step:** 9, Release · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting sign-off / Approved]
· **Owner:** Release Manager (Release chat)

## 1. Overview

| Item | Details |
|---|---|
| Product and software version | [Name, version] |
| Release Plan and Readiness Review | [d09-01 vN.N; d09-02 vN.N] |
| Go decision | [Tracking Decision ID, date] |
| Released on | [YYYY-MM-DD, time] |
| Watch period | [YYYY-MM-DD to YYYY-MM-DD] |
| In one sentence | [e.g., "Released on time with no rollback; one email problem fixed on day 2."] |

## 2. Plan Compared With What Happened

| Item | Planned | Actual | Notes |
|---|---|---|---|
| Release date | [Date] | [Date] | [Why it moved, if it did] |
| Stages | [Plan] | [Actual] | [Notes] |
| Flags turned on | [Plan] | [Actual] | [Notes] |
| Rollbacks | None planned | [Number] | [Notes] |

## 3. Load: Stress Test Compared With Real Use

| Measure | Stress test | Real busiest moment | Notes |
|---|---|---|---|
| Users at the same moment | [Number] | [Number] | [Notes] |
| Error rate | [Rate] | [Rate] | [Notes] |
| Slowest page | [Seconds] | [Seconds] | [Notes] |

## 4. Problems Found

<!-- Every problem during the watch period, however small. Write "None."
if empty. -->

| ID | Date | Problem | Who it affected | Rollback trigger? | What was done | Status |
|---|---|---|---|---|---|---|
| [R-1] | [YYYY-MM-DD] | [Problem] | [Who, how many] | [Yes / No] | [Action] | [Fixed / Handed to Step 10] |

## 5. Rollbacks

<!-- For each rollback: trigger, decision, time taken, data impact. Write
"None." if there were none. -->

| Date | Trigger | Decided by | Time to roll back | Data impact |
|---|---|---|---|---|
| [YYYY-MM-DD] | [Trigger] | [Role] | [Minutes] | [Impact] |

## 6. Early Results

<!-- Compare against the PRD's success measures (d03-01 Section 2). Many
targets take months; record the early trend and say when Step 10 checks
again. -->

| Goal | Target | Result so far | On track? |
|---|---|---|---|
| [Goal] | [Target] | [Result] | [Yes / Too early / No] |

## 7. Costs

| Item | Amount | Source |
|---|---|---|
| Approved monthly limit | [$] | d06-03 |
| Actual spend in the watch period | [$] | [Provider billing] |
| Any alert reached? | [Yes / No] | [Notes] |

## 8. What People Said

<!-- Feedback from users and staff, summarized, with no personal details. -->

- [Feedback]

## 9. Lessons Learned

| What went well | What to change next time | Owner |
|---|---|---|
| [Item] | [Item] | [Role] |

## 10. Hand-Off to Step 10

| Item | Details |
|---|---|
| Open problems handed over | [Problem IDs from Section 4] |
| Flags still to remove | [Flags] |
| Things to watch | [e.g., "Spam rate on reminders"] |
| Next success-measure check | [YYYY-MM-DD] |

## 11. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
