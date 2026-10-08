# BeautifulBeachPark Volunteers: Maintenance Log

**Document:** d10-01 · **Step:** 10, Maintenance · **Last updated:** 2027-04-23
· **Owner:** SRE (Maintenance chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up, and every version, date, and number is made up
> for illustration. This log shows the first three months of maintenance,
> including one phone update that broke a screen, a provider database
> upgrade, an email service retiring its old connection, and a busy
> Earth Day that came close to a tipping point.

## 1. Overview

| Item | Details |
|---|---|
| Product and live version | BeautifulBeachPark Volunteers 1.1 |
| Live since | 2027-01-23 |
| Maintenance sign-off | D16, 2027-02-10 |
| Source Release Efficacy Document | d09-03 v1.0, 2027-02-09 |
| Source System Infrastructure Document | d06-01 v1.3, 2027-01-20 |
| Reliability targets | 99% available; pages under 2 seconds on a phone (d03-01, d04-01) |
| Approved monthly spending limit | $60, alert at $50 (d06-03) |
| Update rhythm | Check every part on the first Monday of each month; security fixes within 7 days |
| Status reports | Monthly, to the Park Manager and Volunteer Program Manager |

## 2. Parts List

| Part | Type | Version in use | Latest version | End of support | Who updates it | Last checked |
|---|---|---|---|---|---|---|
| SampleCloud app hosting | Hosting platform | Current | Current | — | SampleCloud, automatically | 2027-04-05 |
| Python | Language | 3.11 | 3.13 | 2027-10-31 (SampleCloud stops running 3.11 on 2027-12-01) | Us | 2027-04-05 |
| Flask | Framework | 3.1.4 | 3.1.4 | — | Us | 2027-04-05 |
| Other code libraries (12) | Libraries | See `src/requirements.txt` | 11 current, 1 waiting | — | Us | 2027-04-05 |
| PostgreSQL (SampleCloud managed) | Database | 16 | 16 | — | SampleCloud, with notice | 2027-04-05 |
| SampleMail connection | Outside service | Version 2 | Version 3 | 2027-06-30 | Us | 2027-04-05 |
| Phone and desktop browsers | Browsers | Last two versions of each | — | — | Users' devices | 2027-04-05 |
| pytest and Playwright | Test tools | Current | Current | — | Us | 2027-04-05 |
| Claude Code | AI coding tool | Newer model since 2027-03-01 | — | Older model retired 2027-03-31 | Anthropic | 2027-04-05 |
| AI in the app itself | AI model | None used | — | — | — | — |

## 3. Updates

| ID | Date | Part | From → To | Why | Tests run | Result | Released |
|---|---|---|---|---|---|---|---|
| U-1 | 2027-02-15 | Flask | 3.1.2 → 3.1.4 | Security fix | 38 of 38 pass (Run 14) | Done | 2027-02-16 |
| U-2 | 2027-03-02 | Claude Code | Older model → newer model | Old model being retired | 38 of 38 pass (Run 15); the c08 and c10 prompts reran unchanged | Done | Not needed (tool only) |
| U-3 | 2027-03-08 | PostgreSQL | 15 → 16 | SampleCloud's planned upgrade on 2027-03-14; tried on the test copy first | 38 of 38 pass (Run 16) | Done | 2027-03-14, by SampleCloud |
| U-4 | 2027-04-12 | SampleMail connection | Version 2 → 3 | Version 2 retired 2027-06-30; the code must change | New test T-03-08 written; fix in progress | Waiting | Target 2027-05-15 |
| U-5 | — | Python | 3.11 → 3.13 | End of support 2027-10-31 | Not yet | Planned for 2027-07 | Not yet |

## 4. Incidents

| ID | Date | What happened | Who it affected | How it was found | Cause | Fix | Stops it happening again | Status |
|---|---|---|---|---|---|---|---|---|
| M-1 | 2027-02-20 | App unreachable for 4 minutes | About 10 visitors | Log (under the 5-minute alert) | SampleCloud maintenance | None needed | Noted SampleCloud's maintenance calendar | Closed |
| M-2 | 2027-03-09 | Date box on Post a Task (S-7) showed blank on some phones | 3 coordinators | Coordinator email | A phone operating-system update changed how date boxes work | Test T-01-06 added (SDET); date box fixed (Software Engineer) | Test now runs on the newest phone browsers every month | Fixed 2027-03-12 |
| M-3 | 2027-04-10 | Earth Day Beach Cleanup: pages took up to 3.1 seconds | 210 volunteers at once, for about 20 minutes | Dashboard | Database connections reached 14 of 15 | None during the event | See status report 2027-04-23, Recommendation 1 | Open |

## 5. Problems Handed Over From Step 9

| ID | Problem | Sent to | Status |
|---|---|---|---|
| R-1 | Volunteers mistyping their email address | UI/UX, SDET, Software Engineer chats | Fixed 2027-03-12: "check your email address" message added to S-2 (d05-01 v1.2) |
| R-2 | Coordinators can't edit a posted task (Issue I4) | Product Manager, through Tracking | Proposed for Phase 2 (d10-03) |

## 6. Requests Sent to Other Chats

| Date | To chat | Request | Reason (ID) | Outcome |
|---|---|---|---|---|
| 2027-02-17 | UI/UX | Clearer wording on S-2 for mistyped email addresses | R-1 | d05-01 v1.2 approved |
| 2027-02-24 | SDET, then Software Engineer | Test and build the new S-2 message | R-1 | Released 2027-03-12 |
| 2027-03-09 | SDET, then Software Engineer | Test and fix the S-7 date box on the new phone update | M-2 | Released 2027-03-12 |
| 2027-04-12 | SDET, then Software Engineer | Move to SampleMail version 3 | U-4 | In progress |
| 2027-04-23 | DevOps | Options for more database connections before summer | M-3 | Waiting on d10-02 decision |

## 7. Change Log

| Date | Change | By |
|---|---|---|
| 2027-02-10 | Log started | SRE |
| 2027-03-12 | Version 1.1 released (R-1, M-2) | SRE |
| 2027-04-23 | Earth Day incident; Python and SampleMail dates added | SRE |
