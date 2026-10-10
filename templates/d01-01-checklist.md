# [Project name]: Tracking Checklist

<!-- Template d01-01. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order. -->

**Document:** d01-01 · **Step:** 1, Tracking · **Last updated:** [YYYY-MM-DD]
· **Overall status:** [Not started / On track / At risk / Blocked / Parked / Abandoned / Complete]

## 1. Project Summary

| Item | Details |
|---|---|
| Project | [Name] |
| Description | [One or two sentences: what it does and for whom] |
| Sample or own project | [e.g., "sample: samples/BeautifulBeachParkVolunteers," or "own project"] |
| Where files live | [Repo, folder, or link] |
| Stakeholders | [Names and roles] |
| Signs off each step | [Name, or "see Status Table"] |
| Tracking level | [Small: checklist / Medium: + status table / Large: + Gantt chart] |
| Status reports | [Audience and how often] |
| Deadlines | [YYYY-MM-DD, or TBD] |
| Constraints | [Budget, tools, rules, or "none known"] |

## 2. Step Checklist

- [x] Step 1: Tracking: initialized [YYYY-MM-DD] (ongoing)
- [ ] Step 2: Feasibility
- [ ] Step 3: Requirements
- [ ] Step 4: Design
- [ ] Step 5: User Experience
- [ ] Step 6: Initial Infrastructure (DevOps support continues through Step 10)
  - [ ] Cost sign-off: Cost Sign-Off Sheet approved, before anything is set up
  - [ ] Final sign-off: System Infrastructure Document approved, before Step 7
- [ ] Step 7: Test Creation
- [ ] Step 8: Implementation
- [ ] Step 9: Release
  - [ ] Demo approval: stakeholders tried the software on the local environment, before anything moves to the live servers
  - [ ] Go/no-go: Release Readiness Review, after the move and the private pilot, before real users are invited
- [ ] Step 10: Maintenance

## 3. Status Table

<!-- Medium and large projects. For small projects, replace the table with
"Not used for this project." Status values: Not started, In progress,
Awaiting sign-off, Approved, Sent back, Ongoing.
After each deliverable, add its template number in parentheses, e.g.,
"PRD (d03-01)", or "(no template yet)". List every template that applies. -->

| Step | Name | Role | Deliverable | Sign-off by | Target date | Status | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Tracking | Scrum Master | Tracking documents (d01-01, plus d01-02 and d01-03 if used) | [Name] | Ongoing | Ongoing | |
| 2 | Feasibility | Product Manager | One-pager (d02-01) or feasibility study (d02-02) | [Name] | [YYYY-MM-DD] | Not started | |
| 3 | Requirements | Product Manager | Product Requirements Document (d03-01) | [Name] | [YYYY-MM-DD] | Not started | |
| 4 | Design | Software Architect | Software Design Specification (Spec) | [Name] | [YYYY-MM-DD] | Not started | |
| 5 | User Experience | UI/UX Designer | UI/UX Document with mockups | [Name] | [YYYY-MM-DD] | Not started | |
| 6 | Initial Infrastructure | DevOps Engineer | Cost Sign-Off Sheet (approved before anything is set up); System Infrastructure Document, with the live servers chosen and a local environment set up; then ongoing DevOps support | [Name] | [YYYY-MM-DD] | Not started | [Approved monthly limit, once signed off] |
| 7 | Test Creation | SDET | Test Plan and automated tests | [Name] | [YYYY-MM-DD] | Not started | |
| 8 | Implementation | Software Engineer | Working software and Release Notes | [Name] | [YYYY-MM-DD] | Not started | |
| 9 | Release | Release Manager | Stakeholder demo, move to the live servers, private pilot, live release, and Release Efficacy Document | [Name] | [YYYY-MM-DD] | Not started | [Demo approval, once recorded] |
| 10 | Maintenance | SRE / Maintenance Engineer | Maintenance Log | [Name] | Ongoing | Not started | |

## 4. Decision Log

<!-- One row per decision: Go, Go back, Park, or Abandon. Newest at the
bottom. Never delete rows. Step 6 gets two rows: its cost sign-off (with
the approved spending limit in the Reason) and its final sign-off. Step 9
gets at least two: the demo approval and the go/no-go decision. -->

| # | Date | Step | Decision | Decided by | Reason |
|---|---|---|---|---|---|
| D1 | [YYYY-MM-DD] | 1 Tracking | Tracking initialized | [Name] | Project set up |

## 5. Issue Log

<!-- Status values: Open, Resolved. Never delete rows. -->

| ID | Date raised | Step | Description | Impact | Owner | Status |
|---|---|---|---|---|---|---|
| [I1] | [YYYY-MM-DD] | [Step] | [What's wrong] | [What it affects] | [Name] | [Open] |

## 6. Open Questions

<!-- Anything marked TBD above belongs here. Write "None" if empty. -->

- [Question, and who can answer it]

## 7. Next Action

- **Next chat:** Step [N]: [Name]
- **Prompt:** `c[NN]-...`
- **Templates to fill in:** [e.g., `templates/d03-01-prd.md`, or "no template yet"]
- **Give it:** [List of input files]
- **Waiting on:** [Anything that must happen first, or "nothing"]
