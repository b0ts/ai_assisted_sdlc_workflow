# Steps, Roles, and Deliverables

## Introduction

This guide uses a **Waterfall Software Development Life Cycle (SDLC)
adapted for Test-Driven Development (TDD)**, which goes through a series of
ten steps. Each step produces a **deliverable**: a written document, a set
of checks, or the working software itself. Before the next step can begin,
the deliverable must be reviewed and approved. This approval is called
**sign-off**.

In a standard Waterfall, the software is built first and tested afterward.
Our TDD version keeps the same step-by-step order but writes the tests
*before* the software is built. Other styles, such as Agile, can be used by
modifying this case study: combining steps, reordering them, or repeating
them in shorter cycles. Regardless of the style used, each step still has
specific deliverables and a sign-off before the work moves on.

At most corporations, each step is owned by people with a specific job title
and skill set. The following chart shows the association of Steps, Roles, and
Deliverables. The steps are the same ten described in
[What Is a Software Development Lifecycle Workflow?](a03-what-is-an-sdlc-workflow.md).

## Steps, Roles, and Deliverables

| Step | Role | Deliverables |
|---|---|---|
| 1. Tracking | Scrum Master | A tracking document (checklist, status report, or timeline) that is started first and kept up to date through every other step |
| 2. Feasibility | Product Manager | A one-page project summary with a go/no-go decision, or, for larger projects, a full feasibility study that includes interviews with future customers |
| 3. Requirements | Product Manager | Product Requirements Document (PRD): who the users are and what they need to do |
| 4. Design | Software Architect | Software Design Specification ("Spec"): how the software will work, including a Security & Compliance section |
| 5. User experience | UI/UX Designer | UI/UX Document: sketches ("mockups") of the screens people will see |
| 6. Initial infrastructure | DevOps Engineer | A Cost Sign-Off Sheet, approved before anything is built; System Infrastructure Document: the computers and online services the software runs on, plus a security review; the setup itself; then ongoing DevOps support through steps 7 to 10 |
| 7. Test creation | SDET (Software Development Engineer in Test) | Test Plan Document and the automated checks ("tests") that prove the software works |
| 8. Implementation | Software Engineer | Working software that passes every check, its documentation, and Release Notes |
| 9. Release | Release Manager | The software, live for real users, and a Release Efficacy Document describing how well the release went |
| 10. Maintenance | SRE (Site Reliability Engineer) / Maintenance Engineer | Ongoing fixes and updates, recorded in a Maintenance Log; regular Maintenance Status Reports; and, when the product no longer serves its purpose, a recommendation to start a new phase or sunset (retire) it |

**Note:** Step 1 is ongoing. The Scrum Master starts tracking before any other
step begins and keeps going while steps 2 through 10 run one after another.
The Scrum Master is responsible for tracking all the steps and brokering
sign-off for each step with the stakeholders, the people who have a say in
whether the project succeeds, such as customers, managers, and the team
members who own each step. See [Step 1: Tracking](b01-tracking.md).

**Note:** Step 6 is also partly ongoing, and it has **two sign-offs**
instead of one. The stakeholders first approve a **Cost Sign-Off Sheet**,
because this is the first step that spends money, and only then is the
infrastructure built. The finished System Infrastructure Document is
signed off before Step 7 begins. The DevOps Engineer then keeps supporting
the later steps:
a test environment for Step 7, the automatic build-and-test pipeline for
Step 8, putting the software live in Step 9, and monitoring and costs in
Step 10. See [Step 6: Initial Infrastructure](b06-infrastructure.md).

## Where AI Fits In

With an AI-assisted SDLC, we can reduce the team size dramatically by having
AI role-play the different jobs and produce the deliverables, all the way
through to the finished, runnable software. A small number of people still
guide the work and give sign-off at each step, but they no longer need a full
department of specialists to fill every role.

---

**Learn more:** the [BeautifulBeachPark Volunteers sample](../samples/README.md)
shows each step's deliverables filled in for a made-up project, a volunteer
sign-up app for a park.
