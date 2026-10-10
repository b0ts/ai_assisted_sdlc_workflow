# [Project name]: Release Readiness Review, Version [N.N]

<!-- Template d09-02. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Release Readiness Review is the go/no-go check before release. The
Release Manager checks every hard-stop rule, shows the evidence, discloses
any pressure on the decision, and recommends Go or No-Go. The stakeholders
decide, through the Tracking chat.
A hard stop can only be passed in one way: the stakeholders record a risk
acceptance in Section 5, naming who accepted which risk and the workaround.
A deadline, campaign, or instruction to "just ship it" never passes a hard
stop on its own. Never delete or soften a rule here; propose a change to
this template through the Tracking chat instead.
If anything changes after a Go (new code, a failed check), do a new review. -->

**Document:** d09-02 · **Step:** 9, Release · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting decision / Go / No-Go / Replaced by version N]
· **Owner:** Release Manager (Release chat)

## 1. Overview

| Item | Details |
|---|---|
| Product and software version | [Name, version] |
| Release Plan | [d09-01, version, date] |
| Review date | [YYYY-MM-DD] |
| Planned release date | [YYYY-MM-DD] |
| Recommendation in one sentence | [e.g., "No-Go: reminder emails are landing in spam, which breaks a Must-have use case."] |

## 2. Hard-Stop Rules

<!-- Every rule must be Pass, or Accepted (with a Section 5 row). Any Fail
means the recommendation is No-Go. Add project-specific rules at the end;
never remove the standard rules. -->

| # | Rule | Evidence | Result |
|---|---|---|---|
| HS-1 | Every earlier step has a recorded sign-off, the stakeholders approved the demo of this version, and the people who run the live servers approved the move | [Tracking Decision IDs; d09-01 Sections 1.1 and 6] | [Pass / Fail / Accepted] |
| HS-2 | Every automated test passes on the exact version being released, on the local environment and on the live servers | [d07-02, runs, dates] | [Pass / Fail / Accepted] |
| HS-3 | No test was changed, skipped, or weakened without the SDET's recorded reason | [d07-01 Change Log] | [Pass / Fail / Accepted] |
| HS-4 | A person has reviewed the code | [d08-01 Section 7] | [Pass / Fail / Accepted] |
| HS-5 | The stress test passes at the expected busiest load | [d09-01 Section 7, run] | [Pass / Fail / Accepted] |
| HS-6 | Every manual check passes | [d09-01 Section 8] | [Pass / Fail / Accepted] |
| HS-7 | Every Security & Compliance item is met on the live servers | [d04-01 Section 11; d06-01 Section 8] | [Pass / Fail / Accepted] |
| HS-8 | The rollback has been practiced, and its triggers are written down | [d09-01 Section 9] | [Pass / Fail / Accepted] |
| HS-9 | Backups, monitoring, and any budget alert are on for the live servers, and alerts reach a person | [d09-01 Section 6] | [Pass / Fail / Accepted] |
| HS-10 | No known issue affects a Must-have use case, security, or privacy | [d08-03 Section 4] | [Pass / Fail / Accepted] |
| HS-11 | Expected costs are within the approved spending limit | [d06-03] | [Pass / Fail / Accepted] |
| HS-12 | Every open question that blocks release is answered | [d01-01 Sections 5 and 6] | [Pass / Fail / Accepted] |
| [HS-13] | [Project-specific rule] | [Evidence] | [Result] |

## 3. Other Readiness Checks

<!-- Important, but not hard stops. A "No" here is listed in Section 6. -->

| Check | Ready? | Notes |
|---|---|---|
| Release Notes finalized, in plain language | [Yes / No] | [Notes] |
| Users and support told what is coming | [Yes / No] | [Notes] |
| Release-day roles filled, with backups | [Yes / No] | [Notes] |

## 4. Pressures on This Decision

<!-- Name every deadline, campaign, event, promise, or competitor that is
pushing toward Go. Recording them is not a criticism; it makes them
visible so they don't decide quietly. -->

| Pressure | What depends on the date | Cost of a delay | Raised by |
|---|---|---|---|
| [e.g., Newsletter already scheduled] | [e.g., Volunteer sign-up announcement] | [e.g., "Reschedule; no money lost"] | [Role] |

## 5. Risk Acceptances

<!-- Only the stakeholders fill this in. One row per hard stop they chose
to accept rather than fix. Write "None." if empty. -->

| Hard stop | Risk being accepted | Workaround | Fix by | Accepted by (name, role) | Date | Tracking Decision ID |
|---|---|---|---|---|---|---|
| [HS-N] | [Risk] | [Workaround] | [Date or version] | [Name, role] | [YYYY-MM-DD] | [D-N] |

## 6. Recommendation

| Item | Details |
|---|---|
| Recommendation | [Go / No-Go] |
| Why | [One or two sentences, citing rule numbers] |
| If No-Go: what must happen first | [Each failed rule, the fix, and who owns it] |
| Options for the stakeholders | [e.g., "A: delay one week and fix. B: release with a recorded risk acceptance for HS-10."] |

## 7. Decision

<!-- Filled in after the stakeholders decide, through the Tracking chat. -->

| Decision | Decided by | Date | Tracking Decision ID | Conditions |
|---|---|---|---|---|
| [Go / No-Go] | [Name, role] | [YYYY-MM-DD] | [D-N] | [Any conditions] |

## 8. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First review | — | [Name] |
