# BeautifulBeachPark Volunteers: Release Plan, Version 1.1

**Document:** d09-01 · **Step:** 9, Release · **Version:** 1.1
· **Last updated:** 2027-01-21 · **Status:** Released
· **Owner:** Release Manager (Release chat)

> **Sample document.** BeautifulBeachPark, its city, its people, and Parks
> IT are made up, and every number is made up for illustration. Section 1.1
> shows the stakeholder demo on the local copy; Section 6 shows the move to
> Parks IT's servers; Section 7 shows a stress test that failed during the
> private pilot and how it was fixed; Section 8 shows a manual check that
> failed, which led to the No-Go in d09-02 v1.0.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Software version being released | 1.0 |
| Source Implementation Record | d08-01 v1.0, 2026-12-11 |
| Source Release Notes | d08-03 v1.0, 2026-12-11 |
| Implementation sign-off | D12, 2026-12-11 |
| Latest test result | 38 of 38 pass locally (d07-02, Run 4), and on Parks IT's servers (Run 6) |
| Planned release date | 2027-01-23 (Saturday), the spring volunteer newsletter |
| Hard deadline, if any | 2027-03-01, the start of spring planting season |
| Release type | Small: one new web app, used by one park, with no other products depending on it |
| Live servers | The city's existing servers, run by Parks IT (d06-01 v1.3) |
| Plan in one sentence | Demo on the laptop, move to Parks IT's servers, pilot with test accounts, then let coordinators post the spring tasks before opening the app to volunteers with the newsletter. |

### 1.1 Stakeholder Demo

| Item | Details |
|---|---|
| Date and place | 2026-12-18, park office, on the Volunteer Program Manager's laptop (the local environment) |
| Who tried it | Park Manager and Volunteer Program Manager (stakeholders); two coordinators (consulted) |
| Version shown | 1.0, the version that passed d07-02 Run 4 |
| Script | Each person took a role with a made-up account: a coordinator posted "Demo Beach Cleanup" (UC-1); the Park Manager created a volunteer account and signed up (UC-2, UC-3), then canceled (UC-4); the coordinator viewed the roster, sent a message, and blocked a volunteer (UC-5 to UC-7). Everyone checked the pretend inbox for the emails. |
| What they said | Approved, with no changes. One coordinator asked to edit a posted task; that isn't in the PRD, so it was logged for Phase 2 (I4). |
| Demo approval | D13, 2026-12-18. Parks IT's security review was booked the same day. |

## 2. Inputs

| Input | Source | Notes |
|---|---|---|
| Product Requirements Document | d03-01 v1.1 | Success measures (Section 2); UC-3 reminders are a Must-have; up to 500 volunteers |
| Software Design Specification | d04-01 v1.1 | Under 2 seconds on a phone; Security & Compliance (Section 11) |
| System Infrastructure Document | d06-01 v1.1 (v1.3 after the requests in Section 14) | Live server requirements (Section 5.1); production on Parks IT's servers planned for Step 9; second contact needed (I2) |
| Cost Sign-Off Sheet | d06-03 v1.0 | $0 new spending |
| Test Plan | d07-01 v1.0 | Section 3 leaves real email delivery and other browsers to Step 9 |
| Implementation Record, Developer Guide, Release Notes | d08-01, d08-02, d08-03 v1.0 | Known issues: none |

## 3. What Is Being Released

| Item | Change | Affects | Can it be undone? |
|---|---|---|---|
| The app | First version, on Parks IT's servers | Volunteers, coordinators, the System Administrator | Yes: take it offline (Section 9) |
| Park website | A new "Volunteer" link to the app | Park website visitors | Yes: remove the link |
| Email | The city email service starts sending to real inboxes | Volunteers | Yes: Parks IT turns sending off |

**Who is affected:** volunteers, coordinators, and the park office. No
other system or product depends on the app.

## 4. Release Approach

| Item | Details |
|---|---|
| Approach | Two stages, using the park website link as the switch |
| Why | A small, brand-new app with no earlier version to protect. The busiest moment is predictable (the newsletter), so coordinators can fill the app with real tasks first and spot problems before volunteers arrive. |
| Stages | **Stage 1** (2027-01-22): the app is live at its address, but not linked from the park website. Coordinators get the address directly and post the spring tasks. **Stage 2** (2027-01-23, 9:00): the newsletter goes out and the website link appears. |
| Move to the next stage when | Stage 1 has no rollback trigger, and at least 10 spring tasks are posted |

### 4.1 Private Pilot

| Item | Details |
|---|---|
| Who takes part | Two coordinators, three park office staff, and the DevOps chat, with `example.test` test accounts |
| Dates | 2027-01-13 to 2027-01-21, on Parks IT's servers, not linked from anywhere |
| What they do | Use every screen; post real-looking tasks; sign up, cancel, message, and block; the stress test (Section 7), manual checks (Section 8), and rollback practice (Section 9) |
| Test accounts removed by | DevOps chat with Parks IT, 2027-01-21; checked on S-10 and in the roster of every task (MC-4) |

## 5. Feature Flags

None in version 1.0. This is the app's first release, so with a flag off
there would be nothing left to show; the unpublished address in Stage 1
keeps it out of sight until launch instead. Flags become useful once the
app is live and new features are added to it. **Recommendation for Phase 2:**
release text-message reminders behind a feature flag, so they can be
turned on for a few volunteers first, and off at once if costs rise
(request to the Tracking chat, Section 14).

## 6. Move to the Live Servers

| Item | Ready? | Checked by and date |
|---|---|---|
| Parks IT approved the move (security review) | Yes | Parks IT, 2027-01-07, two weeks after booking |
| Software installed on Parks IT's servers, following the Developer Guide (d08-02 Section 5.1) | Yes | Parks IT, Tuesday 2027-01-12, with the DevOps chat; Volunteer Program Manager watched |
| Every automated test passes on Parks IT's servers | Yes | d07-02 Run 5, 2027-01-12, against a test database; Run 6 after the connection change, 2027-01-15 |
| Real email service connected | Yes | Parks IT, 2027-01-12 |
| Secrets in Parks IT's secret store (never in files) | Yes | Parks IT, 2027-01-12 |
| Backups running, and a restore tested | Yes | Parks IT, 2027-01-13: restored a backup to a spare database |
| Monitoring and alerts on, going to a person | Yes | Volunteer Program Manager received a test alert from Parks IT, 2027-01-13 |
| Budget alert | Not needed | $0 new spending (d06-03) |
| Second contact for Parks IT (Issue I2) | Yes | Board treasurer added, 2027-01-07 (D14) |
| Version on Parks IT's servers matches the demo and Run 4 | Yes | Release chat, 2027-01-15 |

## 7. Stress Test

| Item | Details |
|---|---|
| Busiest moment expected | Newsletter at 9:00 on a Saturday: up to 300 volunteers in the first 10 minutes, most on phones |
| Test load | 500 pretend volunteers over 10 minutes, including 150 tapping "Confirm" at the same moment |
| Where it runs | Parks IT's servers during the private pilot, before any real users, with made-up `example.test` accounts only, deleted afterward; on a weekday evening Parks IT chose |
| Tool | An open-source load-testing tool, run by the DevOps chat |
| Passes if | Error pages for under 1 in 1,000 requests; Open Slots under 2 seconds; no slot over-filled; no effect on Parks IT's other websites |

**Results:**

| Run | Date | Load | Errors | Slowest page | Pass? | Notes |
|---|---|---|---|---|---|---|
| 1 | 2027-01-14 | 500 over 10 min; 150 at once | 6 in 100 during the 150 | 9 seconds | No | Parks IT allows each app 20 database connections at once (d06-01 Section 5.1). Parks IT runs 4 copies of the app to share the load, and each copy kept its own pool of 15, so up to 60 were asked for. Volunteer 21 onward got an error page. No slot was over-filled. The local environment runs one copy, which is why the tests didn't catch it. Request 1 sent to the DevOps chat. |
| 2 | 2027-01-15 | Same | 0 | 1.6 seconds | Yes | After d06-01 v1.2: `DB_POOL_SIZE` set to 4, so the 4 copies use at most 16 connections. No code change; no cost. |

## 8. Manual Checks

| Check | Source | Result | By and date |
|---|---|---|---|
| MC-1: Sign-in links and reminders arrive in real inboxes, not spam, at the three email providers park volunteers use most | d07-01 Section 3 | **Fail** 2027-01-18: one provider put reminders in spam. **Pass** 2027-01-21 after request 2. | Volunteer Program Manager, using staff test inboxes |
| MC-2: The app works in the four most common phone and desktop browsers | d07-01 Section 3 | Pass | Two coordinators, 2027-01-18 |
| MC-3: The privacy notice and park office contact details are correct | d08-03 Section 7 | Pass | Park Manager, 2027-01-18 |
| MC-4: Stress-test and pilot accounts deleted from Parks IT's servers | Sections 4.1 and 7 | Pass | DevOps chat with Parks IT, 2027-01-21 |

## 9. Rollback Plan

| Item | Details |
|---|---|
| Rollback triggers | (1) Any email address shown to a volunteer or coordinator: **immediately**. (2) Any slot over-filled. (3) Error pages for more than 2% of visitors for 10 minutes. (4) The app unreachable for 15 minutes. |
| Who decides | Park Manager; backup: Volunteer Program Manager |
| Who does it | Volunteer Program Manager and Parks IT on-call, with the DevOps chat; backup: Board treasurer (second contact) |
| Steps | 1. Replace the website link with a "Sign-ups open soon" notice. 2. Call Parks IT on-call, who turn on the maintenance page for the app's address. 3. Tell coordinators by phone. 4. Record what happened in d09-03. |
| Time to roll back | Under 10 minutes |
| What happens to data | Accounts and sign-ups stay in the database and return when the app comes back |
| Roll forward instead when | The cause is a wording or setting change that has passed every test locally, and no privacy trigger was reached |
| Practiced on | 2027-01-16, on Parks IT's servers during the pilot, with Parks IT on-call: 6 minutes |

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
| More volunteers than expected arrive at 9:00 | Low | High | Stress-tested at 500; Parks IT can raise the connection limit for the day if asked in advance |
| Volunteers mistype their email and get no sign-in link | Medium | Low | Park office help sheet (Section 11) |

**Assumptions:**

- No more than 300 volunteers arrive in the first 10 minutes.

**Open questions:**

- None.

## 14. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| 1. Keep the app's database connections under Parks IT's limit of 20 | DevOps chat, carried out by Parks IT | Stress test Run 1 failed (Section 7) | d06-01 v1.2, 2027-01-15; Run 2 passed |
| 2. Add the email sender records the provider asked for to the app's web address | DevOps chat, carried out by Parks IT | MC-1 failed: reminders landed in spam at one provider | d06-01 v1.3, 2027-01-20; MC-1 passed 2027-01-21 |
| 3. Use a feature flag for Phase 2 text reminders | Tracking chat, for the Product Manager | Lets a costly feature be turned on gradually and off at once | Logged for Phase 2 |

## 15. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2027-01-08 | First version: demo results (Section 1.1, D13), then the move, pilot, and release plan | — | Park Manager (D14, 2027-01-08) |
| 1.1 | 2027-01-21 | Stress test, manual check, and rollback practice results added; requests 1 to 3 | Results from Mode D | Park Manager (D16, 2027-01-21) |
