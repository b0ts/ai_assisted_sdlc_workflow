# [Project name]: Next Phase or Sunset Recommendation, Version [N.N]

<!-- Template d10-03. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The SRE writes this when a Maintenance Status Report (d10-02) gives a Product
Fit verdict of "New phase" or "Sunset." It sets out the evidence and the
options, and it is decided by the stakeholders through the Tracking chat.
Fill in Section 5 (New Phase) OR Section 6 (Sunset) to match the
recommendation; in the other one, write "Not recommended," with one
sentence why. Never write real users' personal information here; use
counts. -->

**Document:** d10-03 · **Step:** 10, Maintenance · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting sign-off / Approved]
· **Owner:** SRE (Maintenance chat)

## 1. Overview

| Item | Details |
|---|---|
| Product and live version | [Name, version] |
| Live since | [YYYY-MM-DD] |
| Source status report | [d10-02, date] |
| Recommendation | [New phase / Sunset] |
| In one sentence | [e.g., "Volunteer numbers have outgrown Phase 1; start Phase 2 with text reminders and task editing."] |

## 2. Why Now: The Evidence

<!-- Facts from the status reports and the Maintenance Log: success
measures missed or outgrown, tipping points close, rust that would need a
rebuild, rising costs, changed needs, or a better tool now available. -->

| Evidence | Source | What it shows |
|---|---|---|
| [Evidence] | [d10-02 date / d10-01 ID] | [Meaning] |

## 3. Options Considered

| Option | What it means | Cost | Risk | Pros | Cons |
|---|---|---|---|---|---|
| Keep running as is | [Meaning] | [$] | [Risk] | [Pros] | [Cons] |
| New phase | [Meaning] | [$] | [Risk] | [Pros] | [Cons] |
| Sunset | [Meaning] | [$] | [Risk] | [Pros] | [Cons] |

## 4. Recommendation

[Two to four sentences: which option, and why, linked to the evidence.]

## 5. New Phase

<!-- What the new phase must achieve, and what goes back to Step 2. The
current product keeps running, with Step 10 maintenance, until the new phase is
released. -->

| Item | Details |
|---|---|
| Problems the new phase must solve | [List, with IDs] |
| Known requests carried forward | [IDs from d10-01 and the Issue Log] |
| What keeps running meanwhile | [e.g., "Phase 1, with monthly maintenance"] |
| Starts at | Step 2: Feasibility, with a new one-pager (d02-01) |

## 6. Sunset

<!-- A sunset is a planned, safe retirement. Every row needs an owner and a
date. -->

| Item | Plan | Owner | Date |
|---|---|---|---|
| Tell users | [How and when, at least N weeks ahead] | [Role] | [YYYY-MM-DD] |
| Replacement, if any | [What users should use instead] | [Role] | [YYYY-MM-DD] |
| Users' data | [Returned, archived, or deleted, and how; legal rules on keeping records] | [Role] | [YYYY-MM-DD] |
| Turn off the software | [Steps] | DevOps Engineer | [YYYY-MM-DD] |
| Stop every paid service | [Each service and account] | DevOps Engineer | [YYYY-MM-DD] |
| Remove links and names | [Website links, domain names, app-store listings] | [Role] | [YYYY-MM-DD] |
| Keep the records | [Where the documents and code are archived] | Scrum Master | [YYYY-MM-DD] |

## 7. Decision

<!-- Filled in by the Scrum Master after the stakeholders decide in the
Tracking chat. The SRE never fills this in. -->

| Decision | Decided by | Date | Tracking Decision ID |
|---|---|---|---|
| [New phase / Sunset / Keep running] | [Name or role] | [YYYY-MM-DD] | [D-number] |

## 8. Change Log

<!-- Newest at the bottom. Never delete rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
