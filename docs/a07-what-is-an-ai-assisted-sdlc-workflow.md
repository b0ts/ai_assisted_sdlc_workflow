# What Is an AI-Assisted SDLC Workflow?

## Executive Summary

An AI-assisted software development workflow lets a small team, or even one
person, build software the way a large professional team would. It uses a series of AI
chats, each playing one role and passing its finished document to the next.
Because AI works so quickly, every step can be done in order without
shortcuts, giving faster results with fewer problems.

---

## Introduction

An **AI-assisted Software Development Lifecycle (SDLC) workflow** combines
three ideas covered earlier in this guide:

- the **Waterfall SDLC adapted for Test-Driven Development (TDD)** from
  [What Is a Software Development Lifecycle Workflow?](a03-what-is-an-sdlc-workflow.md),
- the **steps, roles, and deliverables** from
  [Steps, Roles, and Deliverables](a04-steps-roles-and-deliverables.md), and
- **prompt engineering** from [Understanding AI](a05-understanding-ai.md) and
  [Prompt Engineering](a06-prompt-engineering.md).

Together, they create a workflow that can match, and in some cases exceed,
the results of a large team of dedicated professionals. The difference is
that the work is done by a much smaller team, sometimes a single person,
using a **series of AI chats**. Each chat plays one role, is given specific
inputs, and produces specific outputs, so that together the chats carry out
a complete TDD SDLC with AI assistance.

The chats are arranged in what is called an **AI chaining workflow**: they
run one after another, and the output of one chat becomes part of the input
for the next.

Running every step in order might sound slow, but AI changes that. Human
teams often try to save time by skipping steps or running them side by side.
They then spend extra time later reconciling work that doesn't fit together.
AI can produce each deliverable in minutes or hours rather than weeks, so the
whole process can be done one step at a time, very quickly.

This greatly reduces the need to skip steps or run them in parallel, giving
**faster time to market with fewer integration issues**.

---

## Multi Chat Prompt Chaining (MCPC)

There are two common ways to chain prompts, and people use the term
"prompt chaining" for both:

| Approach | How it works | Good for |
|---|---|---|
| Chaining in one chat | You ask for one result, then build on it with the next request, all in the same conversation. | Quick, small tasks |
| **Multi Chat Prompt Chaining (MCPC)** | Each step gets its own **separate chat**, with its own role. The only thing carried forward is the output file from the step before. | Larger, repeatable work like an SDLC |

This workflow uses **MCPC**, because starting each role in a fresh chat has
two big benefits:

- **A clean slate.** Each chat sees only what it needs, like a new team
  member reading a handoff document rather than sitting through every
  earlier meeting. Anything the next step needs must be written into that
  document, so gaps show up quickly.
- **Easy to fix and reuse.** If one step goes wrong, you can redo just that
  step. And the same prompts can be reused on the next project.

MCPC is a specific form of what Anthropic, the company that makes Claude,
calls **prompt chaining**:
[Chain complex prompts for stronger performance (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts).

---

## Putting It All Together: Ten Chats

For an AI-assisted SDLC, this boils down to **ten specific chats**, one for
each of the ten steps. Each chat has a role, an audience, inputs, outputs, and additional steering information.

**The first chat plays the Scrum Master.** Step 1 initializes tracking: this
chat is started before any other and sets up the project's tracking
document. Unlike the other steps, it doesn't end there. It stays open while
steps 2 through 10 run one after another, and you return to it after each
step and whenever you need a status update. As each of the other
chats completes its deliverable, the Scrum Master records it, makes sure it
has been reviewed and approved, and then signals that the next chat in the
chain can start.

**The other nine chats** play the roles and produce the deliverables
outlined in
[What Is a Software Development Lifecycle Workflow?](a03-what-is-an-sdlc-workflow.md)
and [Steps, Roles, and Deliverables](a04-steps-roles-and-deliverables.md).
One of them, the **Initial Infrastructure** chat (Step 6), is also
revisited later: after it sets up the initial infrastructure, later steps
bring DevOps questions back to it, such as a test environment for Step 7
or help putting the software live in Step 9.

| Step | Chat | Role | Main deliverable |
|---|---|---|---|
| 01 | Tracking | Scrum Master | Project checklist and progress reports |
| 02 | Feasibility | Product Manager | One-page project summary with a go/no-go decision |
| 03 | Requirements | Product Manager | Product Requirements Document (PRD) |
| 04 | Design | Software Architect | Software Design Specification ("Spec") |
| 05 | User experience | UI/UX Designer | UI/UX Document with screen sketches |
| 06 | Initial infrastructure | DevOps Engineer | Cost Sign-Off Sheet (approved before building) and System Infrastructure Document, then ongoing DevOps support |
| 07 | Test creation | SDET (Software Development Engineer in Test) | Test Plan and automated tests |
| 08 | Implementation | Software Engineer | Working software and Release Notes |
| 09 | Release | Release Manager | Live software and Release Efficacy Document |
| 10 | Maintenance | SRE (Site Reliability Engineer) / Maintenance Engineer | Maintenance Log |

### When the Chain Runs Backward

The chain doesn't always move straight forward. Sometimes a later step runs
into a stumbling block that sends the work back a step, and an earlier
document has to be rewritten.

When a downstream role discovers that an upstream deliverable is wrong or
incomplete, a **feedback loop** sends a revision request back to the
upstream role's chat (or a fresh chat continuing that role). The affected
deliverables are updated before work moves forward again.

For example, during the design step, the Software Architect may find that
the project described in the PRD is too complex to deliver all at once. The
PRD is then rewritten to deliver the product in **phases**, each with a
smaller chunk of functionality, and the design picks up from the revised
PRD.

---

## What Comes Next

Each step has its own guide, and the files that go with it all share the
step's number:

| Prefix | What it is | Where it lives | Example |
|---|---|---|---|
| **a** | How-to and background guides | `docs/` | `a07-what-is-an-ai-assisted-sdlc-workflow.md` |
| **b** | Step guides, one per step | `docs/` | `b01-tracking.md` |
| **c** | Predefined prompts for each step's chat | `prompts/` | `c01-tracking-prompt.md` |
| **d** | Templates for each step's documents | `templates/` | `d01-01-checklist`, `d01-02-gantt` |
| **d** | Sample documents: the templates filled in for the sample project | `samples/` | `d03-01-prd.md` in the sample's `docs/` |
| **e** | Case studies of real projects, each in its own repository | separate repos | None yet |

Templates have two numbers because one step can produce several documents.
Prompts get a second number only if a step needs more than one. For example, the Tracking step (01) can produce a checklist
(`d01-01`), a Gantt chart (`d01-02`), and a status report (`d01-03`).

The [sample project](../samples/README.md),
**BeautifulBeachPark Volunteers**, is a volunteer sign-up app for a made-up
park. Its documents use the same d numbers as the templates they came from,
so `d03-01` is always its requirements document. Additional
[case studies](case-studies.md) may be added to this repo at a future time,
each numbered the same way.

---

**Learn more:**

- [Chain complex prompts for stronger performance (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts):
  Anthropic's guide to prompt chaining
- [BeautifulBeachPark Volunteers sample](../samples/README.md): every
  step's deliverable for one made-up project
- [Prompt Engineering](a06-prompt-engineering.md): how to choose and write
  the kind of prompt each chat needs
