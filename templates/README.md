# Templates

Templates for the documents each step produces. Names use two numbers: the step number, then the document number within that step, because one step can produce several documents.

**Step 1: Tracking**

- [d01-01-checklist.md](d01-01-checklist.md): project summary, step checklist, status table, decision log, issue log, and next action
- [d01-02-gantt.md](d01-02-gantt.md): Gantt chart timeline for large or phased projects
- [d01-03-status-report.md](d01-03-status-report.md): one-page status report for stakeholders

**Step 2: Feasibility**

- [d02-01-one-pager.md](d02-01-one-pager.md): one-page summary of a product idea: problem, users, solution, why now, rough cost, success measures, risks, and recommendation
- [d02-02-feasibility-study.md](d02-02-feasibility-study.md): full feasibility study for larger projects: users and market, customer interviews, technical, economic (ROI), operational, and legal feasibility, options, risks, and recommendation
- [d02-03-pitch-summary.md](d02-03-pitch-summary.md): one-page, side-by-side comparison of one or more ideas for the stakeholders' go/no-go decision
- [d02-04-proposal.md](d02-04-proposal.md): proposal for outside approval or funding (grant, investor, or client RFP), including commitments made and a submission checklist

**Step 3: Requirements**

- [d03-01-prd.md](d03-01-prd.md): Product Requirements Document: overview, success measures, users, UML use case diagram, use cases, quality requirements, constraints, scope, and change log

**Step 4: Design**

- [d04-01-spec.md](d04-01-spec.md): Software Design Specification (Spec): design approach, system overview, components, data, client–server interface, use case coverage, a UML sequence diagram per use case, quality requirements, Security & Compliance, design decisions, and change log
- [d04-02-design-options.md](d04-02-design-options.md): side-by-side comparison of design approaches (such as web app vs. app-store app), with trade-offs and a recommendation

**Step 5: User Experience**

- [d05-01-ui-ux.md](d05-01-ui-ux.md): UI/UX Document: design goals, screen inventory, a user flow per use case, a wireframe and mockup per screen, wording, accessibility, privacy on screen, design files, and change log
- [d05-02-style-guide.md](d05-02-style-guide.md): Style Guide: colors with contrast checks, fonts, spacing, components, icons and images, voice and tone, and optional design tokens, matched to the organization's existing look

**Step 6: Initial Infrastructure**

- [d06-01-infrastructure.md](d06-01-infrastructure.md): System Infrastructure Document: infrastructure needs, environments, chosen setup, deployment diagram, network and access, security review, monitoring and alerts, costs, setup record, ongoing DevOps support, and change log
- [d06-02-infrastructure-options.md](d06-02-infrastructure-options.md): Infrastructure Options and Cost Analysis: side-by-side comparison of ways to provide the infrastructure (such as cloud vs. on-premises), with up-front, monthly, and three-year costs and a recommendation
- [d06-03-cost-sign-off.md](d06-03-cost-sign-off.md): Cost Sign-Off Sheet: one-page approval of the chosen option's costs, spending limit, budget alert, and who pays, signed off before anything is built

**Step 7: Test Creation**

- [d07-01-test-plan.md](d07-01-test-plan.md): Test Plan: scope, test approach (happy path, expected failure, bounds checking, monkey testing), traceability from use cases to tests, test data, test definitions, security and quality tests, rules for changing tests, and change log
- [d07-02-test-results.md](d07-02-test-results.md): Test Results Log: run history (starting with the all-fail first run), results by test and by use case, and problems found; continued by the Software Engineer in Step 8

**Step 8: Implementation**

- [d08-01-implementation-record.md](d08-01-implementation-record.md): Implementation Record: build plan linked to use cases, screens, and tests; tools and libraries; progress run by run; screens built; security, speed, cost, license, and code reviews; requests to change a test; requests sent back; and change log
- [d08-02-developer-guide.md](d08-02-developer-guide.md): Developer Guide: how the code is organized, setting up, running the app and the tests, settings and secrets (where kept, never the values), making a change, libraries and licenses, and troubleshooting
- [d08-03-release-notes.md](d08-03-release-notes.md): Release Notes: what's new in plain language, changes since the last version, known issues, what's not included, quality checks, and getting help; drafted in Step 8 and finalized in Step 9

**Step 9: Release**

- [d09-01-release-plan.md](d09-01-release-plan.md): Release Plan: what is released, release approach, feature flags, production readiness, stress test, manual checks, rollback plan, release-day schedule, communication, and watch period
- [d09-02-release-readiness-review.md](d09-02-release-readiness-review.md): Release Readiness Review: hard-stop rules with evidence, pressures on the decision, stakeholder risk acceptances, and the go/no-go recommendation and decision
- [d09-03-release-efficacy.md](d09-03-release-efficacy.md): Release Efficacy Document: plan compared with what happened, stress test compared with real use, problems, rollbacks, early results, costs, lessons learned, and hand-off to Step 10

**Step 10: Maintenance**

- [d10-01-maintenance-log.md](d10-01-maintenance-log.md): Maintenance Log: parts list with versions and end-of-support dates, updates, incidents, problems handed over from Step 9, and requests sent to other chats; kept up to date for as long as the product is live
- [d10-02-maintenance-status-report.md](d10-02-maintenance-status-report.md): Maintenance Status Report: overall health, reliability, incidents, rust report, scale and tipping points, costs, success measures, recommendations, and a Product Fit verdict; written on a regular rhythm
- [d10-03-next-phase-or-sunset.md](d10-03-next-phase-or-sunset.md): Next Phase or Sunset Recommendation: the evidence, the options, and the plan for a new phase (back to Step 2) or a safe retirement

To use a template, fill it in: keep every heading in the same order, replace every `[placeholder]`, and delete the hint comments (`<!-- ... -->`).

To see a template filled in, open the file with the same name in the sample project's [`docs/`](../samples/BeautifulBeachParkVolunteers/docs/) folder. When you change a template, update its sample document to match.

See the [numbering system](../README.md#numbering-system) for the full scheme.
