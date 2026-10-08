# BeautifulBeachPark Volunteers: Release Efficacy Document, Version 1.0

**Document:** d09-03 · **Step:** 9, Release · **Version:** 1.0
· **Last updated:** 2027-02-09 · **Status:** Approved
· **Owner:** Release Manager (Release chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up, and every number is made up for illustration.
> Counts are used instead of any volunteer's details.

## 1. Overview

| Item | Details |
|---|---|
| Product and software version | BeautifulBeachPark Volunteers 1.0 |
| Release Plan and Readiness Review | d09-01 v1.1; d09-02 v1.1 |
| Go decision | D15, 2027-01-21 (after the No-Go, D14, 2027-01-19) |
| Released on | Stage 1: 2027-01-22, 10:00; Stage 2: 2027-01-23, 9:00 |
| Watch period | 2027-01-23 to 2027-02-06 |
| In one sentence | Released on the planned day with no rollback; the two problems the release checks found would both have hit launch morning. |

## 2. Plan Compared With What Happened

| Item | Planned | Actual | Notes |
|---|---|---|---|
| Release date | 2027-01-22 and 2027-01-23 | Same | Kept only because the email fix was finished on 2027-01-20 |
| Stages | Coordinators first, then volunteers | Same | Coordinators posted 14 spring tasks in Stage 1 |
| Flags turned on | None | None | Website link added at 8:30 on 2027-01-23 |
| Rollbacks | None planned | 0 | No trigger was reached |

## 3. Load: Stress Test Compared With Real Use

| Measure | Stress test | Real busiest moment | Notes |
|---|---|---|---|
| Users at the same moment | 150 | 96 (2027-01-23, 9:04) | 340 volunteers visited in the first hour |
| Error rate | 0 | 3 error pages in about 9,000 requests | All during a SampleCloud update at 11:40; under the 2% trigger |
| Slowest page | 1.6 seconds | 1.4 seconds | Open Slots, on phones |

Without the connection-pool fix from stress test Run 1, the 9:04 peak
would have passed the 20-connection limit, and volunteers would have seen
error pages at the moment the newsletter arrived.

## 4. Problems Found

| ID | Date | Problem | Who it affected | Rollback trigger? | What was done | Status |
|---|---|---|---|---|---|---|
| R-1 | 2027-01-23 | Some volunteers didn't get a sign-in email because they mistyped their address. Not a fault in the app. | 27 volunteers, all helped by the park office | No | Park office help sheet used; a clearer "check your email address" message suggested | Handed to Step 10, as a request for the UI/UX Designer |
| R-2 | 2027-01-27 | Coordinators can't edit a task after posting it; one posted the wrong date and had to ask the park office. Not in the PRD. | 2 coordinators | No | Logged as a feature request | Handed to Step 10, for the Product Manager (Phase 2) |
| R-3 | 2027-01-23 | 3 error pages during a SampleCloud update | 3 visitors | No (under 2%) | No action needed; noted for Step 10 to watch | Closed |

## 5. Rollbacks

None.

## 6. Early Results

| Goal | Target | Result so far | On track? |
|---|---|---|---|
| Fill slots without email chains | 80% of slots filled through the app within 3 months | 71% of spring slots filled in two weeks; 312 volunteer accounts | Yes |
| Save coordinators' time | Half of today's scheduling hours | Not yet measured | Too early: coordinator survey in Step 10, 2027-04-23 |
| Protect volunteers' privacy | Zero emails shown to others | Zero | Yes |

## 7. Costs

| Item | Amount | Source |
|---|---|---|
| Approved monthly limit | $60 | d06-03 |
| Actual spend in the watch period | $19, plus $2 for the stress test | SampleCloud and SampleMail billing |
| Any alert reached? | No | Expected about $41 for a full month |

## 8. What People Said

- Volunteers at the desk said signing up "took less than a minute."
- Coordinators liked seeing "places left" without counting replies.
- Two coordinators asked to be able to edit a posted task (R-2).

## 9. Lessons Learned

| What went well | What to change next time | Owner |
|---|---|---|
| The stress test found the connection limit before real users did | Run a small stress test in Step 6, as soon as the database is chosen | DevOps Engineer |
| The real-inbox check caught reminders landing in spam | Check real email delivery when the email service is first set up, not a week before launch | DevOps Engineer |
| The Release Rules held under newsletter pressure, and the stakeholders chose the fix with the facts in front of them | Agree a backup newsletter date when the release date is first set | Release Manager |
| Coordinators-first staging filled the app before volunteers arrived | Keep staging for Phase 2, using a feature flag for text reminders | Release Manager |

## 10. Hand-Off to Step 10

| Item | Details |
|---|---|
| Open problems handed over | R-1, R-2 |
| Flags still to remove | None |
| Things to watch | Spam rate on reminder emails; database connections at busy times; monthly costs against $60 |
| Next success-measure check | 2027-04-23 (three months after launch) |

## 11. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2027-02-09 | First version | — | Park Manager (D16, 2027-02-10) |
