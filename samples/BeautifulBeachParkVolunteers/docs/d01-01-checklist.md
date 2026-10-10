# BeautifulBeachPark Volunteers: Tracking Checklist

**Document:** d01-01 · **Step:** 1, Tracking · **Last updated:** 2027-02-10
· **Overall status:** On track

> **Sample document.** BeautifulBeachPark and its people are made up. This
> checklist shows the project at the end of Step 9, including one go-back
> decision (Design back to Requirements, D4), the stakeholder demo on the
> local copy (D13), and one release No-Go (D15).

## 1. Project Summary

| Item | Details |
|---|---|
| Project | BeautifulBeachPark Volunteers |
| Description | A web app where park coordinators post one-hour volunteer slots and volunteers sign up using only a username. |
| Sample or own project | sample: samples/BeautifulBeachParkVolunteers |
| Where files live | `samples/BeautifulBeachParkVolunteers/` in the ai_assisted_sdlc_workflow repo |
| Stakeholders | Park Manager; Volunteer Program Manager; coordinators (consulted); Parks IT, the city parks department's IT team, which runs the servers the app goes live on (consulted) |
| Signs off each step | Park Manager, with the Volunteer Program Manager |
| Tracking level | Medium: checklist + status table |
| Status reports | Park Manager, every two weeks |
| Deadlines | Live before the spring planting season, 2027-03-01 |
| Constraints | Small budget; no IT staff of the park's own (Parks IT runs the city's servers); up to 500 volunteers |

## 2. Step Checklist

- [x] Step 1: Tracking: initialized 2026-09-01 (ongoing)
- [x] Step 2: Feasibility
- [x] Step 3: Requirements
- [x] Step 4: Design
- [x] Step 5: User Experience
- [x] Step 6: Initial Infrastructure (DevOps support continues through Step 10)
  - [x] Cost sign-off: Cost Sign-Off Sheet approved, before anything is set up
  - [x] Final sign-off: System Infrastructure Document approved, before Step 7
- [x] Step 7: Test Creation
- [x] Step 8: Implementation
- [x] Step 9: Release
  - [x] Demo approval: stakeholders tried the app on the local copy (D13)
  - [x] Go/no-go: Release Readiness Review, after the move and the private pilot (D16)
- [ ] Step 10: Maintenance

## 3. Status Table

| Step | Name | Role | Deliverable | Sign-off by | Target date | Status | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Tracking | Scrum Master | Tracking checklist (d01-01) | Park Manager | Ongoing | Ongoing | |
| 2 | Feasibility | Product Manager | One-pager (d02-01) | Park Manager | 2026-09-05 | Approved | |
| 3 | Requirements | Product Manager | Product Requirements Document (d03-01) | Park Manager | 2026-09-12 | Approved | v1.1, after D4 go-back |
| 4 | Design | Software Architect | Software Design Specification (d04-01) | Park Manager | 2026-09-26 | Approved | v1.1: two requests added for Step 5 (D7) |
| 5 | User Experience | UI/UX Designer | UI/UX Document (d05-01); Style Guide (d05-02) | Park Manager | 2026-10-03 | Approved | |
| 6 | Initial Infrastructure | DevOps Engineer | Cost Sign-Off Sheet (d06-03); System Infrastructure Document (d06-01); Options (d06-02) | Park Manager | 2026-10-09 | Approved | City's existing servers (Parks IT); $0 new spending (D9) |
| 7 | Test Creation | SDET | Test Plan (d07-01); Test Results Log (d07-02); tests in `tests/` | Park Manager | 2026-10-16 | Approved | 38 tests, all failing for the right reason; d05-01 and d06-01 updated to v1.1 for the tests |
| 8 | Implementation | Software Engineer | Working software in `src/`; Implementation Record (d08-01); Developer Guide (d08-02); Release Notes (d08-03); runs added to d07-02 | Park Manager | 2026-12-15 | Approved | 38 of 38 tests pass (Run 4); person's code review done |
| 9 | Release | Release Manager | Release Plan (d09-01); Release Readiness Review (d09-02); Release Notes finalized (d08-03 v1.1); Release Efficacy Document (d09-03); the live app | Park Manager | 2027-02-15 | Approved | Demo approved (D13); moved to Parks IT's servers; live 2027-01-23 after one No-Go (D15); no rollback |
| 10 | Maintenance | SRE / Maintenance Engineer | Maintenance Log (d10-01); Maintenance Status Reports (d10-02); Next Phase or Sunset Recommendation (d10-03), when needed | Volunteer Program Manager | Ongoing | Not started | |

## 4. Decision Log

| # | Date | Step | Decision | Decided by | Reason |
|---|---|---|---|---|---|
| D1 | 2026-09-01 | 1 Tracking | Tracking initialized | Park Manager | Project set up |
| D2 | 2026-09-04 | 2 Feasibility | Go to Requirements | Park Manager | One-pager d02-01 v1.0: clear problem, low cost |
| D3 | 2026-09-11 | 3 Requirements | Go to Design | Park Manager | PRD d03-01 v1.0 approved |
| D4 | 2026-09-16 | 4 Design | Go back to Requirements | Park Manager | Text-message reminders cost money for every message; Architect recommends email only in Phase 1 (I1) |
| D5 | 2026-09-18 | 3 Requirements | Go to Design | Park Manager | PRD d03-01 v1.1: text reminders moved to Phase 2 |
| D6 | 2026-09-25 | 4 Design | Go to User Experience | Park Manager | Spec d04-01 v1.0 approved |
| D7 | 2026-09-30 | 5 User Experience | Style Guide approved; Spec v1.1 approved | Park Manager | d05-02 v1.0 matches the park's pretend website, so mockups may begin; Spec v1.1 adds two requests the UI/UX Designer needed for screens S-6 and S-10 |
| D8 | 2026-10-02 | 5 User Experience | Go to Initial Infrastructure | Park Manager | UI/UX Document d05-01 v1.0 approved |
| D9 | 2026-10-07 | 6 Initial Infrastructure | Cost sign-off | Park Manager, Volunteer Program Manager | Option A, the city's existing servers run by Parks IT; $0 new spending (d06-03 v1.0) |
| D10 | 2026-10-09 | 6 Initial Infrastructure | Go to Test Creation | Park Manager | d06-01 v1.0 approved; local environment set up; Parks IT confirmed the live server requirements |
| D11 | 2026-10-16 | 7 Test Creation | Go to Implementation | Park Manager | Test Plan d07-01 v1.0 approved; 38 of 38 tests failing for the right reason (d07-02) |
| D12 | 2026-12-11 | 8 Implementation | Go to Release | Park Manager | d08-01, d08-02, and d08-03 v1.0 approved; 38 of 38 tests pass (d07-02 v1.1, Run 4); every screen matches its mockup; person's code review passed |
| D13 | 2026-12-18 | 9 Release | Demo approved | Park Manager, Volunteer Program Manager | Both tried the app on the local copy with two coordinators (d09-01 Section 1.1); no changes asked for; the move to Parks IT's servers may begin |
| D14 | 2027-01-08 | 9 Release | Release Plan approved | Park Manager | d09-01 v1.0; Parks IT approved the move; Board treasurer named second contact for Parks IT (I2) |
| D15 | 2027-01-19 | 9 Release | No-Go; fix first (Option A) | Park Manager, Volunteer Program Manager | d09-02 v1.0: reminders landing in spam at one provider (HS-6, HS-10); newsletter date kept only if fixed by 2027-01-21 |
| D16 | 2027-01-21 | 9 Release | Go | Park Manager, Volunteer Program Manager | d09-02 v1.1: every hard stop passes; d09-01 v1.1 and d08-03 v1.1 approved |
| D17 | 2027-02-10 | 9 Release | Go to Maintenance | Park Manager | d09-03 v1.0: two weeks live, no rollback; R-1 and R-2 handed to Step 10 |

## 5. Issue Log

| ID | Date raised | Step | Description | Impact | Owner | Status |
|---|---|---|---|---|---|---|
| I1 | 2026-09-15 | 4 Design | Text-message reminders need a paid texting service | Monthly cost the budget doesn't cover | Product Manager | Resolved (D5) |
| I2 | 2026-10-08 | 6 Initial Infrastructure | Only one person is Parks IT's contact for the app | No one to approve changes if they leave | Volunteer Program Manager | Resolved (D14) |
| I3 | 2027-01-18 | 9 Release | Reminder emails land in spam at one email provider | Volunteers miss reminders; empty slots | DevOps Engineer | Resolved (d06-01 v1.3; D16) |
| I4 | 2027-01-27 | 9 Release | Coordinators can't edit a posted task (not in the PRD) | Wrong dates need the park office to fix | Product Manager | Open: Phase 2 request, for Step 10 |

## 6. Open Questions

- None.

## 7. Next Action

- **Next chat:** Step 10: Maintenance
- **Prompt:** `c10-maintenance-prompt.md`
- **Templates to fill in:** d10-01 now; d10-02 monthly; d10-03 only if a report recommends a new phase or sunset
- **Give it:** d03-01, d04-01, d06-01, d06-03, d08-02, d08-03, d09-03, and the `src/` and `tests/` folders
- **Waiting on:** nothing
