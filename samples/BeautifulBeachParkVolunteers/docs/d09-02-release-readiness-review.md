# BeautifulBeachPark Volunteers: Release Readiness Review, Version 1.1

**Document:** d09-02 · **Step:** 9, Release · **Version:** 1.1
· **Last updated:** 2027-01-21 · **Status:** Go
· **Owner:** Release Manager (Release chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up. This review shows the rules working under
> pressure. **Version 1.0 (2027-01-19) recommended No-Go:** reminder
> emails were landing in spam at one email provider, and the spring
> newsletter announcing sign-ups was already scheduled. The Park Manager
> asked whether the app could go live anyway. The Release chat recorded
> the pressure, kept the result at Fail, and gave the stakeholders two
> options. They chose to fix it first (D14). **Version 1.1** is the new
> review after the fix.

## 1. Overview

| Item | Details |
|---|---|
| Product and software version | BeautifulBeachPark Volunteers 1.0 |
| Release Plan | d09-01 v1.1, 2027-01-21 |
| Review date | 2027-01-21 (version 1.0: 2027-01-19) |
| Planned release date | 2027-01-22 (Stage 1) and 2027-01-23 (Stage 2) |
| Recommendation in one sentence | Go: every hard stop now passes, including the real-inbox email check that failed in version 1.0. |

## 2. Hard-Stop Rules

| # | Rule | Evidence | Result |
|---|---|---|---|
| HS-1 | Every earlier step has a recorded sign-off | D2 to D13 in d01-01 | Pass |
| HS-2 | Every automated test passes on the exact version being released | d07-02 Run 13; production version confirmed in d09-01 Section 6 | Pass |
| HS-3 | No test was changed, skipped, or weakened without the SDET's recorded reason | d07-01 v1.0 Change Log; TC-1 in d08-01 was turned down | Pass |
| HS-4 | A person has reviewed the code | d08-01 Section 7, 2026-12-10 | Pass |
| HS-5 | The stress test passes at the expected busiest load | d09-01 Section 7, Run 2 (Run 1 failed; fixed by d06-01 v1.2) | Pass |
| HS-6 | Every manual check passes | d09-01 Section 8: MC-1 to MC-4 | Pass (v1.0: **Fail**, MC-1) |
| HS-7 | Every Security & Compliance item is met on production | d06-01 Section 8, rechecked on production 2027-01-13 | Pass |
| HS-8 | The rollback has been practiced, and its triggers are written down | d09-01 Section 9: 6 minutes, 2027-01-16 | Pass |
| HS-9 | Backups, monitoring, and the budget alert are on in production, and alerts reach a person | d09-01 Section 6 | Pass |
| HS-10 | No known issue affects a Must-have use case, security, or privacy | Reminders (UC-3 AC5, Must-have) arrive in inboxes at all three providers | Pass (v1.0: **Fail**, same cause as MC-1) |
| HS-11 | Expected costs are within the approved spending limit | Expected $41 a month against the $60 limit (d06-03) | Pass |
| HS-12 | Every open question that blocks release is answered | Second account owner named (I2, D13) | Pass |
| HS-13 | No email address appears on any screen in production | T-SEC-01 run once against production with made-up accounts, 2027-01-15 | Pass |

## 3. Other Readiness Checks

| Check | Ready? | Notes |
|---|---|---|
| Release Notes finalized, in plain language | Yes | d08-03 v1.1: release date set |
| Users and support told what is coming | Yes | Newsletter scheduled; park office help sheet printed (d09-01 Section 11) |
| Release-day roles filled, with backups | Yes | d09-01 Section 9 |

## 4. Pressures on This Decision

| Pressure | What depends on the date | Cost of a delay | Raised by |
|---|---|---|---|
| Spring newsletter scheduled for 2027-01-23, 9:00, announcing "Sign-ups are open" | Volunteers' first look at the app | The newsletter could be moved one week; printing and mailing are not yet paid | Volunteer Program Manager |
| Park Manager asked on 2027-01-19 whether the app could go live anyway, since "most people will still get their reminders" | — | — | Park Manager |
| Spring planting season starts 2027-03-01 | Volunteers needed from the first week of March | None if the release is before mid-February | PRD; d01-01 |

## 5. Risk Acceptances

None. In version 1.0 the stakeholders were offered a risk acceptance for
HS-6 and HS-10 (Option B in Section 6) and chose not to use it.

## 6. Recommendation

| Item | Details |
|---|---|
| Recommendation | **Go** |
| Why | Every hard stop passes (HS-1 to HS-13). |
| If No-Go: what must happen first | Not applicable in version 1.1. In version 1.0: fix MC-1 (DevOps chat, request 2 in d09-01), then repeat MC-1 at all three providers and do a new review. |
| Options for the stakeholders | Version 1.0 offered: **A.** Fix first; the DevOps chat estimated one day, so the 2027-01-23 newsletter can stay if the fix is done by 2027-01-21. **B.** Go anyway with a recorded risk acceptance for HS-6 and HS-10, telling volunteers to check their spam folder. Reminders are a Must-have, and missed reminders mean empty slots, so the Release chat did not recommend B. |

## 7. Decision

| Decision | Decided by | Date | Tracking Decision ID | Conditions |
|---|---|---|---|---|
| No-Go (version 1.0); Option A chosen | Park Manager, with the Volunteer Program Manager | 2027-01-19 | D14 | Keep the newsletter date only if MC-1 passes by 2027-01-21 |
| **Go** (version 1.1) | Park Manager, with the Volunteer Program Manager | 2027-01-21 | D15 | Follow d09-01 v1.1, Stages 1 and 2 |

## 8. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2027-01-19 | First review: No-Go (HS-6, HS-10) | MC-1 failed | Park Manager (D14, 2027-01-19) |
| 1.1 | 2027-01-21 | New review after the email fix: Go | Release Rule 6: a change after a review needs a new review | Park Manager (D15, 2027-01-21) |
