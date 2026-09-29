# Step 1: Tracking (The Scrum Master Chat)

## Executive Summary

Every project needs someone who keeps the big picture in view. In our
AI-assisted SDLC workflow, that job belongs to the **Tracking chat**, which
plays the role of **Scrum Master**. It oversees the other nine chats, keeps
the stakeholders informed, and, together with those stakeholders, makes a
**go/no-go decision** at the end of every step.

Tracking is **Step 1** because it is the first chat started: it
**initializes tracking** for the project. But unlike every other step, it
doesn't end when the next one begins. It keeps running alongside steps 2
through 10 and is the chat you return to most often.

---

## What Is a Scrum Master?

The term comes from **Scrum**, a popular Agile way of running software
teams. In Scrum, the Scrum Master is not the boss and does not do the
technical work. Instead, they:

- **Keep the process running.** They make sure the team follows the agreed
  steps and that meetings and reviews actually happen.
- **Remove roadblocks.** When someone is stuck waiting on a decision, a
  person, or a missing piece, the Scrum Master chases it down.
- **Connect the team to the people it serves.** They make sure customers,
  managers, and other stakeholders know where things stand, and that the
  team hears what the stakeholders want.

Our workflow is a Waterfall adapted for Test-Driven Development (TDD), not
Scrum, so we borrow the title and stretch it a little. Our Scrum Master also
tracks progress across all ten steps and brokers **sign-off** for each
deliverable, as described in
[Steps, Roles, and Deliverables](a02-steps-roles-and-deliverables.md).

> **Why "Scrum Master"?** In classic Waterfall, this role is called the
> **Project Manager**. We use Scrum Master instead, as many companies do even
> when they aren't fully Agile, to avoid confusion with the **Product
> Manager** (steps 2 and 3), since both are often shortened to "PM."

### An Everyday Comparison: The General Contractor

Go back to the house example from
[What Is a Software Development Lifecycle Workflow?](a01-what-is-an-sdlc-workflow.md).
The architect, electrician, and plumber each do their own job. The
**general contractor** doesn't wire the house or lay the pipes. They keep
the schedule, make sure each inspection passes before the next crew shows
up, and sit down with the homeowner whenever a decision is needed: *"The
plans came back over budget. Do we drop the third bedroom, build it later,
or stop here?"* That is the Scrum Master's job.

---

## The Scrum Master Agent in Our Workflow

In the AI-assisted workflow described in
[What Is an AI-Assisted SDLC Workflow?](a05-what-is-an-ai-assisted-sdlc-workflow.md),
each step is carried out by its own AI chat, or **agent**. The Scrum Master
agent is the **overseer of that group of agents**. It has three jobs:

| Job | What it means |
|---|---|
| **Monitor** | Track which step is in progress, which deliverables are done, and which are waiting for review. |
| **Coordinate** | Make sure each chat receives the right input files from the step before, and signal when the next chat can start. |
| **Interface** | Act as the go-between for the AI agents and the human stakeholders: summarize results for people, and turn people's decisions into instructions for the agents. |

The Scrum Master agent does **not** make decisions on its own. As
[Understanding AI](a03-understanding-ai.md) reminds us, AI is a smart
assistant, not a boss. The agent lays out the facts and a recommendation;
the stakeholders decide.

### Go/No-Go Decisions at Every Step

When a step finishes, the Scrum Master and the stakeholders review its
deliverable and choose one of four paths:

| Decision | When to use it | Example |
|---|---|---|
| **Go** | The deliverable is approved. | The PRD is signed off, so the Design chat can start. |
| **Go back** | A later step exposed a problem in an earlier one. | The Design step shows the project is too complex, so it returns to **Requirements** to be split into phases of delivery. |
| **Park** | The idea is sound, but now isn't the time. | Feasibility shows the budget isn't there this year. The project is saved and set aside. |
| **Abandon** | The project shouldn't continue. | Feasibility shows the stakeholders don't want to proceed. The project is closed, and the reasons are recorded. |

Recording *why* a project was parked or abandoned matters. It saves the
next team from repeating the same study, and it tells you what would have
to change to reopen it.

### A Chat You Keep Coming Back To

The other nine chats each do their job and hand off a document. The
Tracking chat is different: because it oversees all the others, it is
**revisited after each step is completed**, and any time someone asks,
*"Where are we?"* A typical visit looks like this:

1. Tell the Tracking chat which step just finished and attach its
   deliverable.
2. It updates the tracking document and summarizes the result for the
   stakeholders.
3. The stakeholders make the go/no-go call.
4. It records the decision and tells you which chat runs next and which
   files to give it.

---

## Initialize, Then Keep Going

Steps 2 through 10 flow one after another, like a waterfall. Tracking runs
alongside all of them:

```text
Step  1  Tracking                 [=========================================]
Step  2  Feasibility              [===]
Step  3  Requirements                 [===]
Step  4  Design                           [===]
Step  5  User experience                      [===]
Step  6  Infrastructure                           [===]
Step  7  Test creation                                [===]
Step  8  Implementation                                   [===]
Step  9  Release                                              [===]
Step 10  Upkeep                                                   [===...
```

**Initializing tracking** means starting the Tracking chat and creating the
first tracking document: the project's name and goal, who the stakeholders
are, and the list of steps still to come. From then on, the chat is
**ongoing**: each time another step finishes, you come back to it.

---

## Tracking Documents: Simple to Complex

The Scrum Master's deliverables are **tracking documents**. Their templates
are numbered **d01-01**, **d01-02**, and so on, because one step can produce
several kinds of document. Their size should match the project.

**Simple projects** only need a checklist:

```markdown
- [x] Tracking: initialized (ongoing)
- [x] Feasibility: approved (Go)
- [x] Requirements: PRD signed off
- [ ] Design: in progress
- [ ] User experience
- [ ] Infrastructure
- [ ] Test creation
- [ ] Implementation
- [ ] Release
- [ ] Upkeep
```

**Medium projects** add a status table with owners, dates, decisions, and
open issues for each step.

**Complex projects**, especially ones delivered in phases, benefit from a
**Gantt chart**: a timeline showing each step as a bar, how steps overlap
across phases, and which ones depend on others. AI can draw simple Gantt
charts directly in Markdown using
[Mermaid](https://mermaid.js.org/syntax/gantt.html).

Start simple. If the checklist stops answering "Where are we?", move up a
level.

---

## Examples, Templates, and Prompts

> **To be updated:** This section will link to real-world material for the
> Tracking chat as it becomes available.

**Prompts** (in `prompts/`):

- [`c01-tracking-prompt.md`](../prompts/c01-tracking-prompt.md): one prompt
  that initializes tracking, then handles step updates, issues, status
  reports, and go/no-go reviews each time you return to the chat

**Templates** (in `templates/`):

- [`d01-01-checklist.md`](../templates/d01-01-checklist.md): simple step
  checklist, plus status table, decision log, and issue log
- [`d01-02-gantt.md`](../templates/d01-02-gantt.md): Gantt chart timeline for
  complex or phased projects
- [`d01-03-status-report.md`](../templates/d01-03-status-report.md): status
  report for stakeholders

**Examples** (each in its own repository):

- **e01 · d01-01:** the tracking checklist from the
  [RC Park Tour](https://github.com/b0ts/rc_park_tour) project: *coming soon*
- **e01:** a go-back decision (Design back to Requirements): *coming soon*

---

**Learn more:**

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html): the official
  definition of Scrum and the Scrum Master role
- [What Is an AI-Assisted SDLC Workflow?](a05-what-is-an-ai-assisted-sdlc-workflow.md):
  the ten chats and how they chain together
- [Step 2: Feasibility](b02-feasibility.md): the first step Tracking
  watches over
- [Gantt chart (Wikipedia)](https://en.wikipedia.org/wiki/Gantt_chart): a
  plain introduction to Gantt charts
