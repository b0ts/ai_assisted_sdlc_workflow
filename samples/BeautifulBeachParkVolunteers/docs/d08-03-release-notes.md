# BeautifulBeachPark Volunteers: Release Notes, Version 1.0

**Document:** d08-03 · **Step:** 8, Implementation (finalized in Step 9) · **Software version:** 1.0
· **Last updated:** 2027-01-21 · **Status:** Released
· **Owner:** Software Engineer (Implementation chat); finalized by the Release Manager (Release chat)

> **Sample document.** BeautifulBeachPark and its people are made up.
> Version 1.0 was the draft handed to Step 9; version 1.1 is the final
> version, with the release date set by the Release Manager.

## 1. Summary

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Version | 1.0, the first release |
| Planned release date | 2027-01-23 (coordinators from 2027-01-22) |
| Who it is for | Volunteers, coordinators, and the System Administrator |
| In one sentence | The first version: coordinators post one-hour volunteer slots for park, garden, and beach tasks, and volunteers sign up using only a username. |

## 2. What's New

| Who | What you can do | Use case |
|---|---|---|
| Volunteers | Create an account with just a username and your email. Nobody else ever sees your email. | UC-2 |
| Volunteers | Sign in with a link sent to your email. There's no password to remember. | UC-2 |
| Volunteers | See every open one-hour slot and how many places are left, and sign up in three taps. | UC-3 |
| Volunteers | Get a reminder email the day before your slot. | UC-3 |
| Volunteers | See your sign-ups, and cancel one before it starts. | UC-4 |
| Coordinators | Post a task with one-hour slots, and choose how many volunteers each slot needs (1 to 20). | UC-1 |
| Coordinators | See all your tasks and slots on one screen, and who has signed up, by username. | UC-5 |
| Coordinators | Send a short message to a volunteer without seeing their email. | UC-6 |
| Coordinators | Block a volunteer, so they can't sign up again, even with a new account. | UC-7 |
| System Administrator | See the blocked volunteers, and undo a block. | UC-7 |

## 3. Changes Since the Last Version

- First release.

## 4. Known Issues

None known.

## 5. Not Included in This Version

- **Text-message reminders:** planned for Phase 2. Reminders are by email
  only for now.
- **Other languages:** English only in this version. The wording is kept
  in one place so other languages can be added later.
- **Replying to a coordinator's message:** messages come from a no-reply
  address. Volunteers contact the park office instead.

## 6. Quality Checks

| Check | Result |
|---|---|
| Automated tests | 38 of 38 pass |
| Person's review of the code | Done, 2026-12-10 |
| Privacy | Checked: no email address appears on any screen |
| Accessibility | Checked against WCAG 2.1 AA |
| Speed | Slot pages load in under 2 seconds on a phone |
| Busy-moment test | 500 pretend volunteers, 150 at the same moment, with no errors |
| Real email delivery | Sign-in links and reminders checked at the three most-used email providers |

## 7. Getting Help

| Need | Contact |
|---|---|
| Can't sign in, or didn't get a sign-in email | The park office, at the volunteer desk or the office phone number on the park website |
| Question about a task | The coordinator who posted it, through the park office |
| Think you were blocked by mistake | The park office, which can ask the System Administrator |

## 8. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-12-11 | First draft | — | Park Manager (D12, 2026-12-11) |
| 1.1 | 2027-01-21 | Release date set; release checks added to Quality Checks | Finalized in Step 9 | Park Manager (D15, 2027-01-21) |
