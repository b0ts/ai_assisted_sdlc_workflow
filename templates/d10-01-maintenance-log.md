# [Project name]: Maintenance Log

<!-- Template d10-01. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Maintenance Log is the SRE's running record of the live product. It is
started at the beginning of Step 10 and kept up to date for as long as the
product is live: one file, with rows added, never deleted. It holds the
parts list (every piece the product depends on, with its version and
end-of-support date), every update, every incident, and every request sent
to another chat. The Maintenance Status Report (d10-02) summarizes it. Never
write real users' personal information, passwords, keys, or tokens here;
use counts. -->

**Document:** d10-01 · **Step:** 10, Maintenance · **Last updated:** [YYYY-MM-DD]
· **Owner:** SRE (Maintenance chat)

## 1. Overview

| Item | Details |
|---|---|
| Product and live version | [Name, version] |
| Live since | [YYYY-MM-DD] |
| Maintenance sign-off | [Tracking Decision ID, date] |
| Source Release Efficacy Document | [d09-03, version, date] |
| Source System Infrastructure Document | [d06-01, version, date] |
| Reliability targets | [e.g., "99% available; pages under 2 seconds" (d03-01, d04-01)] |
| Approved monthly spending limit | [$] (d06-03) |
| Update rhythm | [e.g., "Check for updates monthly; security fixes within 7 days"] |
| Status reports | [e.g., "Monthly, to the Park Manager"] |

## 2. Parts List

<!-- Every piece the product depends on, so nothing rusts unnoticed:
operating system or hosting platform, programming language, framework and
libraries, database, outside services (email, maps, payments), AI models,
browsers and devices supported, and the tools used to build and test.
Check each one on every update cycle. -->

| Part | Type | Version in use | Latest version | End of support | Who updates it | Last checked |
|---|---|---|---|---|---|---|
| [e.g., Python] | [Language] | [3.x] | [3.y] | [YYYY-MM-DD / Unknown] | [Us / Provider, automatically] | [YYYY-MM-DD] |

## 3. Updates

<!-- One row per update, applied or planned. Every update that changes the
product goes through the test environment and the full test suite first.
Write "None yet." if empty. -->

| ID | Date | Part | From → To | Why (security, end of support, new feature, fix) | Tests run | Result | Released |
|---|---|---|---|---|---|---|---|
| [U-1] | [YYYY-MM-DD] | [Part] | [Old → New] | [Reason] | [e.g., "38 of 38 pass, Run 14"] | [Done / Waiting / Rolled back] | [YYYY-MM-DD / Not yet] |

## 4. Incidents

<!-- An incident is anything that hurt or nearly hurt users: an outage, an
error spike, a slow page, missing emails, a cost alert. Record the cause,
not just the symptom, and what stops it happening again. Write "None." if
empty. -->

| ID | Date | What happened | Who it affected | How it was found (alert, log, user) | Cause | Fix | Stops it happening again | Status |
|---|---|---|---|---|---|---|---|---|
| [M-1] | [YYYY-MM-DD] | [Problem] | [Who, how many] | [Source] | [Cause] | [Fix] | [Prevention] | [Open / Fixed] |

## 5. Problems Handed Over From Step 9

<!-- Copy every open problem from d09-03 Section 10, and track it here until
it is closed. -->

| ID | Problem | Sent to | Status |
|---|---|---|---|
| [R-1] | [Problem] | [Chat] | [Open / Fixed / Moved to new phase] |

## 6. Requests Sent to Other Chats

<!-- Code fixes go to the SDET chat first (a test that catches the
problem), then the Software Engineer chat. Settings and services go to the
DevOps chat. Screens go to the UI/UX chat. New features go to the Product
Manager through the Tracking chat. -->

| Date | To chat | Request | Reason (ID) | Outcome |
|---|---|---|---|---|
| [YYYY-MM-DD] | [Chat] | [Request] | [U-/M-/R- ID] | [Outcome] |

## 7. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Date | Change | By |
|---|---|---|
| [YYYY-MM-DD] | Log started | SRE |
