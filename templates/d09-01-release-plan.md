# [Project name]: Release Plan, Version [N.N]

<!-- Template d09-01. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Release Plan says what is being released, how, and how it will be
undone if something goes wrong. Step 9 has four stages: a stakeholder demo
on the local environment, the move to the live servers, a private pilot
with test accounts, and going live. Section 1.1 (the demo) is filled in
first; the rest of the plan is written after the demo is approved, with the
DevOps Engineer and the people who run the live servers, and approved
through the Tracking chat BEFORE anything is moved to the live servers. Scale it to the risk: a small
change on one website may need a few lines per section; a shared library
(SDK) used by many products needs much more. Write "Not needed" with a
reason rather than deleting a section. Never write passwords, keys, or
account numbers here. -->

**Document:** d09-01 · **Step:** 9, Release · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting sign-off / Approved / Released]
· **Owner:** Release Manager (Release chat)

## 1. Overview

| Item | Details |
|---|---|
| Product | [Name] |
| Software version being released | [e.g., 1.0] |
| Source Implementation Record | [d08-01, version, date] |
| Source Release Notes | [d08-03, version, date] |
| Implementation sign-off | [Tracking Decision ID, date] |
| Latest test result | [e.g., "38 of 38 pass (d07-02, Run 13)"] |
| Planned release date | [YYYY-MM-DD] |
| Hard deadline, if any | [YYYY-MM-DD, and why] |
| Release type | [e.g., "Small: one new website" / "Large: shared library used by N products"] |
| Live servers | [e.g., "The organization's existing servers, run by its IT team" (d06-01)] |
| Plan in one sentence | [e.g., "Demo locally, move to the IT team's servers, pilot with test accounts for a week, then open sign-ups on launch day."] |

### 1.1 Stakeholder Demo

<!-- The stakeholders try the working software on the local environment
(your computer), with made-up data, BEFORE anything is moved. Nothing goes
to the live servers until their approval is recorded in the Tracking chat.
If they ask for changes, list them and the chat each goes to. -->

| Item | Details |
|---|---|
| Date and place | [YYYY-MM-DD, e.g., "Park office, on the Volunteer Program Manager's laptop"] |
| Who tried it | [Stakeholders and roles] |
| Version shown | [e.g., 1.0, the version that passed d07-02 Run N] |
| Script | [The Must-have use cases walked through, e.g., "UC-1 to UC-7, one per person"] |
| What they said | [Approved / Changes asked for, with each change and the chat it went to] |
| Demo approval | [Tracking Decision ID and date, or "Not yet"] |

## 2. Inputs

| Input | Source | Notes |
|---|---|---|
| [e.g., PRD] | [d03-01 vN.N] | [What this plan takes from it] |

## 3. What Is Being Released

<!-- List everything that changes on the live system: code, settings,
database changes, new services, and anything removed. -->

| Item | Change | Affects | Can it be undone? |
|---|---|---|---|
| [e.g., The app] | [e.g., First version] | [Who] | [Yes / Yes, with data steps / No] |

**Who is affected:** [Users, other products, other teams]

## 4. Release Approach

<!-- Choose one and say why: All at once, Feature flag, Gradual (canary),
or Side by side (blue-green). See b09-release.md. -->

| Item | Details |
|---|---|
| Approach | [e.g., Gradual: 5%, then 25%, then everyone] |
| Why | [Reason, linked to risk] |
| Stages | [Each stage, its audience, and how long it lasts] |
| Move to the next stage when | [e.g., "No rollback trigger for 24 hours"] |

### 4.1 Private Pilot

<!-- After the move, and before real users are invited, a few trusted
people use TEST accounts on the live servers. The stress test, manual
checks, and rollback practice happen here. -->

| Item | Details |
|---|---|
| Who takes part | [e.g., "Two coordinators and three staff, with test accounts"] |
| Dates | [YYYY-MM-DD to YYYY-MM-DD] |
| What they do | [e.g., "Use every screen; post real-looking tasks; sign up and cancel"] |
| Test accounts removed by | [Role, date, and how it is checked] |

## 5. Feature Flags

<!-- One row per on/off switch. Write "None" and why if none are used.
A first release of a brand-new application usually has no flags, because
with the flag off there would be nothing to show. Flags are mainly for new
features added to an application people already use. -->

| Flag | Hides or shows | Starts | Turned on by and when | Removed by |
|---|---|---|---|---|
| [Name] | [Feature] | [Off] | [Role, date or condition] | [Version or date] |

## 6. Move to the Live Servers

<!-- Done only after the demo approval (Section 1.1) is recorded. Confirm
with the DevOps Engineer and the people who run the live servers, from
d06-01 (especially Section 5.1, the live server requirements). -->

| Item | Ready? | Checked by and date |
|---|---|---|
| The people who run the live servers approved the move | [Yes / No] | [Who, date] |
| Software installed on the live servers, following the Developer Guide (d08-02) | [Yes / No] | [Who, date] |
| Every automated test passes on the live servers | [Yes / No] | [d07-02 run, date] |
| Real email service connected | [Yes / No] | [Who, date] |
| Secrets in the secret store (never in files) | [Yes / No] | [Who, date] |
| Backups running, and a restore tested | [Yes / No] | [Who, date] |
| Monitoring and alerts on, going to a person | [Yes / No] | [Who, date] |
| Budget alert set below the approved limit | [Yes / No] | [Who, date] |
| [Other, e.g., second account owner] | [Yes / No] | [Who, date] |

## 7. Stress Test

<!-- Pretend to be many users at once, on the live servers during the
private pilot (before real users arrive), at a time the people who run
them agree to. Base the numbers on the busiest moment you
expect, plus a safety margin. -->

| Item | Details |
|---|---|
| Busiest moment expected | [e.g., "Newsletter at 9:00: up to 300 people in 10 minutes"] |
| Test load | [e.g., "500 pretend users over 10 minutes, then 150 at the same moment"] |
| Where it runs | [Live servers, during the pilot / copy of the live servers] |
| Tool | [e.g., an open-source load-testing tool] |
| Passes if | [e.g., "Error pages for under 1 in 1,000 requests; pages under 2 seconds; costs stay under the limit"] |

**Results:**

| Run | Date | Load | Errors | Slowest page | Pass? | Notes |
|---|---|---|---|---|---|---|
| [1] | [YYYY-MM-DD] | [Load] | [Rate] | [Seconds] | [Yes / No] | [What was found and fixed] |

## 8. Manual Checks

<!-- Everything d07-01 left to "check by hand in Step 9", plus anything
only possible on the live system. -->

| Check | Source | Result | By and date |
|---|---|---|---|
| [e.g., Real emails arrive in real inboxes, not spam] | [d07-01 Section 3] | [Pass / Fail] | [Who, date] |

## 9. Rollback Plan

| Item | Details |
|---|---|
| Rollback triggers | [Exact, measurable conditions, e.g., "error pages for over 2% of users for 10 minutes"] |
| Who decides | [Role, and a backup person] |
| Who does it | [Role] |
| Steps | [Numbered steps, or link to the Developer Guide section] |
| Time to roll back | [e.g., "Under 10 minutes"] |
| What happens to data | [e.g., "Sign-ups made after launch are kept"] |
| Roll forward instead when | [e.g., "A one-line fix is ready and tested"] |
| Practiced on | [YYYY-MM-DD, on the live servers during the pilot, how long it took] |

## 10. Release-Day Schedule

| Time | Action | Who | Done when |
|---|---|---|---|
| [HH:MM] | [Action] | [Role] | [Check] |

## 11. Communication

| Who is told | What | When | How | By |
|---|---|---|---|---|
| [Users] | [e.g., "Sign-ups are open"] | [When] | [e.g., Newsletter] | [Role] |

## 12. Watch Period

| Item | Details |
|---|---|
| How long the release is watched | [e.g., "Two weeks"] |
| What is watched | [Alerts from d06-01, success measures from the PRD] |
| Who watches | [Role] |
| Ends with | The Release Efficacy Document (d09-03) |

## 13. Risks, Assumptions, and Open Questions

**Risks:**

| Risk | Likelihood | Impact | What we will do |
|---|---|---|---|
| [Risk] | [Low / Medium / High] | [Low / Medium / High] | [Action] |

**Assumptions:**

- [Assumption]

**Open questions:**

- [Question, who answers it, and by when]

## 14. Requests Sent Back

| Request | Sent to | Reason | Outcome |
|---|---|---|---|
| [Request] | [Chat] | [Reason] | [Outcome and version] |

## 15. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
