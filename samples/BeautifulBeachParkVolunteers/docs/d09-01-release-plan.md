# BeautifulBeachPark Volunteers: Release Plan, Version 1.1

**Document:** d09-01 · **Step:** 9, Release · **Version:** 1.1
· **Last updated:** 2027-01-21 · **Status:** Released
· **Owner:** Release Manager (Release chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up, and every number is made up for illustration.
> Section 7 shows a stress test that failed and how it was fixed; Section 8
> shows a manual check that failed, which led to the No-Go in d09-02 v1.0.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Software version being released | 1.0 |
| Source Implementation Record | d08-01 v1.0, 2026-12-11 |
| Source Release Notes | d08-03 v1.0, 2026-12-11 |
| Implementation sign-off | D12, 2026-12-11 |
| Latest test result | 38 of 38 pass (d07-02, Run 13) |
| Planned release date | 2027-01-23 (Saturday), the spring volunteer newsletter |
| Hard deadline, if any | 2027-03-01, the start of spring planting season |
| Release type | Small: one new web app, used by one park, with no other products depending on it |
| Plan in one sentence | Put the app live quietly for coordinators to post the spring tasks, then open it to volunteers with the newsletter. |

## 2. Inputs

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | d03-01 v1.1 | Success measures (Section 2); UC-3 reminders are a Must-have; up to 500 volunteers |
| Software Design Specification | d04-01 v1.1 | Under 2 seconds on a phone; Security & Compliance (Section 11) |
| System Infrastructure Document | d06-01 v1.1 (v1.3 after the requests in Section 14) | Production planned for Step 9; second account owner needed (I2) |
| Cost Sign-Off Sheet | d06-03 v1.0 | $60 monthly limit, alert at $50 |
| Test Plan | d07-01 v1.0 | Section 3 leaves real email delivery and other browsers to Step 9 |
| Implementation Record, Developer Guide, Release Notes | d08-01, d08-02, d08-03 v1.0 | Known issues: none |

## 3. What Is Being Released

| Item | Change | Affects | Can it be undone? |
|---|---|---|---|
| The app | First version, in the new production environment | Volunteers, coordinators, the System Administrator | Yes: take it offline (Section 9) |
| Park website | A new "Volunteer" link to the app | Park website visitors | Yes: remove the link |
| Email | SampleMail starts sending to real inboxes | Volunteers | Yes: turn sending off |

**Who is affected:** volunteers, coordinators, and the park office. No
other system or product depends on the app.

## 4. Release Approach

| Item | Details |
|---|---|
| Approach | Two stages, using the park website link as the switch |
| Why | A small, brand-new app with no earlier version to protect. The busiest moment is predictable (the newsletter), so coordinators can fill the app with real tasks first and spot problems before volunteers arrive. |
| Stages | **Stage 1** (2027-01-22): the app is live at its address, but not linked from the park website. Coordinators get the address directly and post the spring tasks. **Stage 2** (2027-01-23, 9:00): the newsletter goes out and the website link appears. |
| Move to the next stage when | Stage 1 has no rollback trigger, and at least 10 spring tasks are posted |

## 5. Feature Flags

None in version 1.0. This is the app's first release, so with a flag off
there would be nothing left to show; the unpublished address in Stage 1
keeps it out of sight until launch instead. Flags become useful once the
app is live and new features are added to it. **Recommendation for Phase 2:**
release text-message reminders behind a feature flag, so they can be
turned on for a few volunteers first, and off at once if costs rise
(request to the Tracking chat, Section 14).

## 6. Production Environment

| Item | Ready? | Checked by and date |
|---|---|---|
| Production environment built | Yes | DevOps chat, 2027-01-12; Volunteer Program Manager reviewed the preview |
| Secrets in the secret store (never in files) | Yes | DevOps chat, 2027-01-12 |
| Backups running, and a restore tested | Yes | DevOps chat, 2027-01-13: restored a backup to the test environment |
| Monitoring and alerts on, going to a person | Yes | Volunteer Program Manager received a test alert, 2027-01-13 |
| Budget alert set below the approved limit | Yes | $50 alert confirmed in SampleCloud billing, 2027-01-13 |
| Second account owner (Issue I2) | Yes | Board treasurer added, 2027-01-07 (D13) |
| Version in production matches Run 13 | Yes | Release chat, 2027-01-15 |

## 7. Stress Test

| Item | Details |
|---|---|
| Busiest moment expected | Newsletter at 9:00 on a Saturday: up to 300 volunteers in the first 10 minutes, most on phones |
| Test load | 500 pretend volunteers over 10 minutes, including 150 tapping "Confirm" at the same moment |
| Where it runs | Production, before any real users, with made-up `example.test` accounts only, deleted afterward |
| Tool | An open-source load-testing tool, run by the DevOps chat |
| Passes if | Error pages for under 1 in 1,000 requests; Open Slots under 2 seconds; no slot over-filled; spend for the test under $5 |

**Results:**

| Run | Date | Load | Errors | Slowest page | Pass? | Notes |
|---|---|---|---|---|---|---|
| 1 | 2027-01-14 | 500 over 10 min; 150 at once | 6 in 100 during the 150 | 9 seconds | No | The smallest database plan accepts 20 connections at once, and the app opened a new one for every request. Volunteer 21 onward got an error page. No slot was over-filled. Request 1 sent to the DevOps chat. |
| 2 | 2027-01-15 | Same | 0 | 1.6 seconds | Yes | After d06-01 v1.2: the app shares a pool of 15 connections. No extra monthly cost. The test cost $2. |

## 8. Manual Checks

| Check | Source | Result | By and date |
|---|---|---|---|
| MC-1: Sign-in links and reminders arrive in real inboxes, not spam, at the three email providers park volunteers use most | d07-01 Section 3 | **Fail** 2027-01-18: one provider put reminders in spam. **Pass** 2027-01-21 after request 2. | Volunteer Program Manager, using staff test inboxes |
| MC-2: The app works in the four most common phone and desktop browsers | d07-01 Section 3 | Pass | Two coordinators, 2027-01-18 |
| MC-3: The privacy notice and park office contact details are correct | d08-03 Section 7 | Pass | Park Manager, 2027-01-18 |
| MC-4: Stress-test accounts deleted from production | Section 7 | Pass | DevOps chat, 2027-01-15 |

## 9. Rollback Plan

| Item | Details |
|---|---|
| Rollback triggers | (1) Any email address shown to a volunteer or coordinator: **immediately**. (2) Any slot over-filled. (3) Error pages for more than 2% of visitors for 10 minutes. (4) The app unreachable for 15 minutes. |
| Who decides | Park Manager; backup: Volunteer Program Manager |
| Who does it | Volunteer Program Manager, with the DevOps chat; backup: Board treasurer (second account owner) |
| Steps | 1. Replace the website link with a "Sign-ups open soon" notice. 2. In SampleCloud, choose the app, then **Settings**, then turn on **Maintenance page**. 3. Tell coordinators by phone. 4. Record what happened in d09-03. |
| Time to roll back | Under 10 minutes |
| What happens to data | Accounts and sign-ups stay in the database and return when the app comes back |
| Roll forward instead when | The cause is a wording or setting change that has been tested in the test environment, and no privacy trigger was reached |
| Practiced on | 2027-01-16, in the test environment: 6 minutes |

## 10. Release-Day Schedule

| Time | Action | Who | Done when |
|---|---|---|---|
| 2027-01-22, 10:00 | Stage 1: send coordinators the app's address | Volunteer Program Manager | Coordinators can sign in |
| 2027-01-22, all day | Coordinators post spring tasks; Release chat watches alerts | Coordinators; Release chat | At least 10 tasks posted |
| 2027-01-22, 17:00 | Stage 1 check | Release chat | No trigger reached |
| 2027-01-23, 8:30 | Add the website link; final check | Volunteer Program Manager | Link opens the app |
| 2027-01-23, 9:00 | Newsletter goes out (Stage 2) | Park office | Sent |
| 2027-01-23, 9:00 to 12:00 | Watch errors, speed, emails, and spending | Release chat; Volunteer Program Manager | No trigger reached |

## 11. Communication

| Who is told | What | When | How | By |
|---|---|---|---|---|
| Coordinators | The app's address, and how to post tasks | 2027-01-22 | Email and a short meeting | Volunteer Program Manager |
| Volunteers | "Spring sign-ups are open" | 2027-01-23, 9:00 | Newsletter and park website | Park office |
| Park office | How to answer "I didn't get my sign-in email" | 2027-01-21 | Printed sheet at the volunteer desk | Volunteer Program Manager |

## 12. Watch Period

| Item | Details |
|---|---|
| How long the release is watched | Two weeks: 2027-01-23 to 2027-02-06 |
| What is watched | The alerts in d06-01 Section 9, and the PRD success measures |
| Who watches | Release chat, with the Volunteer Program Manager |
| Ends with | The Release Efficacy Document (d09-03) |

## 13. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| More volunteers than expected arrive at 9:00 | Low | High | Stress-tested at 500; a larger database plan stays within the $60 limit if needed |
| Volunteers mistype their email and get no sign-in link | Medium | Low | Park office help sheet (Section 11) |

**Assumptions:**

- No more than 300 volunteers arrive in the first 10 minutes.

**Open questions:**

- None.

## 14. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| 1. Share database connections instead of opening one per request | DevOps chat | Stress test Run 1 failed (Section 7) | d06-01 v1.2, 2027-01-15; Run 2 passed |
| 2. Add the email sender records the provider asked for to the park's web address | DevOps chat | MC-1 failed: reminders landed in spam at one provider | d06-01 v1.3, 2027-01-20; MC-1 passed 2027-01-21 |
| 3. Use a feature flag for Phase 2 text reminders | Tracking chat, for the Product Manager | Lets a costly feature be turned on gradually and off at once | Logged for Phase 2 |

## 15. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2027-01-08 | First version | — | Park Manager (D13, 2027-01-08) |
| 1.1 | 2027-01-21 | Stress test, manual check, and rollback practice results added; requests 1 to 3 | Results from Mode D | Park Manager (D15, 2027-01-21) |
