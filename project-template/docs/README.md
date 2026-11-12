# Documents: The Deliverables

Every document the workflow produces, as a blank template. Each step's chat
fills its own in, in place, keeping the file name, so the files sort in step
order and match the workflow repo's
[`templates/`](https://github.com/b0ts/ai_assisted_sdlc_workflow/tree/main/templates)
folder. A file that still holds `[placeholders]` hasn't been written yet.
Compare each finished document with the same file in the
[sample project](https://github.com/b0ts/ai_assisted_sdlc_workflow/tree/main/samples/BeautifulBeachParkVolunteers/docs).

| File | Step | What it is | Needed? |
|---|---|---|---|
| `d01-01-checklist.md` | 1 Tracking | The steps, every decision, issues, and the next action | Always |
| `d01-02-gantt.md` | 1 Tracking | A timeline | Large or phased projects |
| `d01-03-status-report.md` | 1 Tracking | A one-page status report for stakeholders | When asked for |
| `d02-01-one-pager.md` | 2 Feasibility | The idea on one page, with a go or no-go recommendation | Always |
| `d02-02-feasibility-study.md` | 2 Feasibility | A full feasibility study | Larger projects |
| `d02-03-pitch-summary.md` | 2 Feasibility | Several ideas side by side, for the go or no-go | When choosing between ideas |
| `d02-04-proposal.md` | 2 Feasibility | A proposal for outside approval or funding | When someone outside must approve |
| `d03-01-prd.md` | 3 Requirements | The Product Requirements Document: users and use cases | Always |
| `d04-01-spec.md` | 4 Design | The Software Design Specification, with Security & Compliance | Always |
| `d04-02-design-options.md` | 4 Design | Design approaches compared | When there's a real choice |
| `d05-01-ui-ux.md` | 5 User Experience | Every screen, its wording, and the user flows | Always (if it has screens) |
| `d05-02-style-guide.md` | 5 User Experience | Colors, fonts, and components, matched to your organization | Always (if it has screens) |
| `d06-01-infrastructure.md` | 6 Initial Infrastructure | Where it runs, the live servers' rules, and the local environment | Always |
| `d06-02-infrastructure-options.md` | 6 Initial Infrastructure | Hosting options compared, with costs | When there's a real choice |
| `d06-03-cost-sign-off.md` | 6 Initial Infrastructure | The costs, approved before anything is set up | Always |
| `d07-01-test-plan.md` | 7 Test Creation | Every test, and what it proves | Always |
| `d07-02-test-results.md` | 7 Test Creation (continued in 8 to 10) | A row for every test run | Always |
| `d08-01-implementation-record.md` | 8 Implementation | The build plan, progress, and the reviews | Always |
| `d08-02-developer-guide.md` | 8 Implementation | How to set up, run, test, and change the code | Always |
| `d08-03-release-notes.md` | 8 Implementation (finalized in 9) | What this version does, in plain language | Always |
| `d08-04-code-review.md` | 8 Implementation | A code review report: copy it once per reviewer, as `d08-04-code-review-codex.md` and `d08-04-code-review-claude.md` | Always (two) |
| `d08-05-hands-on-review.md` | 8 Implementation | A person's hands-on review of the running app | Always |
| `d08-06-polishing-log.md` | 8 Implementation | Polishing by the person who built the app | Always |
| `d09-01-release-plan.md` | 9 Release | The stakeholder demo, the move to the live servers, the pilot, and rollback | Always |
| `d09-02-release-readiness-review.md` | 9 Release | The go or no-go check before release day | Always |
| `d09-03-release-efficacy.md` | 9 Release | How well the release went | Always |
| `d10-01-maintenance-log.md` | 10 Maintenance | Updates, incidents, and requests, kept while live | Always |
| `d10-02-maintenance-status-report.md` | 10 Maintenance | A regular status report | One per report |
| `d10-03-next-phase-or-sunset.md` | 10 Maintenance | A recommendation to start a new phase, or retire the product | Only when needed |

Templates a project doesn't need can stay blank or be deleted.
