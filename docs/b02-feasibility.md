# Step 2: Feasibility (The Product Manager Chat)

**Role:** Product Manager · **Prompt:** [c02](../prompts/c02-feasibility-prompt.md) · **Templates:** d02-01 to d02-04

## Executive Summary

Before anyone writes requirements, designs screens, or writes code, someone
has to answer a simpler question: **is this product worth building at all?**
In our AI-assisted SDLC workflow, that question belongs to the **Feasibility
chat**, which plays the role of **Product Manager**.

Feasibility is **Step 2**. It starts once [Tracking](b01-tracking.md) has
been initialized, and it ends with a **go/no-go decision** that is backed up
by enough evidence and documentation for the stakeholders to decide with
confidence.

- **Inputs:** one or more product ideas, the problem each is meant to solve,
  and the tracking document from Step 1 (project name, goal, and
  stakeholders).
- **Outputs:** a **one-pager** for each idea
  ([d02-01](../templates/d02-01-one-pager.md)) and, for larger projects, a
  **feasibility study** ([d02-02](../templates/d02-02-feasibility-study.md)),
  plus a **pitch summary** for the stakeholders
  ([d02-03](../templates/d02-03-pitch-summary.md)). When approval or funding
  comes from outside the company, a formal **proposal** is added
  ([d02-04](../templates/d02-04-proposal.md)).
- **Hand-off:** if the decision is **go**, these outputs become the input to
  [Step 3: Requirements](b03-requirements.md). If not, the Tracking chat
  records the product as parked or abandoned, and why.

---

## What Is a Product Manager?

A **product manager** decides *what* a product should be and *why* it should
exist. In a corporation, they:

- **Represent the customer** inside the company.
- **Set the product's direction** and decide which features matter most.
- **Connect the people involved**, from engineers and designers to finance
  and executives.
- **Write the requirements** the team builds from (our Step 3).

> **Not the project manager.** The project manager handles *how* and *when*
> work gets delivered. In our workflow, that job belongs to the Scrum Master
> in the [Tracking chat](b01-tracking.md).

## From Idea to Pitch

Feasibility narrows a wide field of ideas down to the few worth building:

- **Spitballing:** informal, unfiltered ideas tossed out in conversation.
- **Brainstorming:** a focused session to generate and sort ideas around one
  problem.
- **Initial research:** a quick look at users, competitors, and legal
  issues. Many ideas stop here.
- **One-pager:** a single page covering the problem, who has it, the
  proposed solution, rough cost, and how success is measured.
- **Feasibility study:** a deeper look at whether the idea is technically
  possible, whether customers want it, what it costs against what it returns
  (ROI), and whether the company can support it. Sometimes this includes a
  small **proof of concept**.
- **Pitch:** a short presentation to stakeholders that ends with a clear
  request, such as approval to write the requirements.
- **Proposal:** a formal document submitted to an outside party, such as a
  grant application, an investor pitch, or a response to a client's request
  for proposal (RFP). It is built from the one-pager and feasibility study,
  and often adds scope, budget, and a timeline.

**Pitching side by side.** Several ideas often finish feasibility at the
same time and are pitched together. This lets stakeholders compare them on
the same measures, such as cost, risk, value, and ROI, and choose the ones
with the highest return.

> **Outside stakeholders count too.** Funders, investors, and clients who
> must approve a proposal are stakeholders just like the people inside the
> company. The go/no-go decision may depend on their answer.

## Why Feasibility Matters

- **Focus:** a company that says yes to too many products spreads its people
  and money too thin, and nothing gets finished well. Feasibility filters
  ideas so the company can commit fully to the best ones.
- **Lower risk:** finding a deal-breaker in a two-week study is far cheaper
  than finding it six months into development.
- **Alignment:** stakeholders agree on what the product is before work
  begins.
- **A head start:** the problem, users, and success measures gathered here
  become the backbone of the PRD.

Saying no is part of the job. Turning down ten mediocre ideas to do one
great idea well creates more value than launching all eleven.

---

## The Product Manager Agent in Our Workflow

In the AI-assisted workflow described in [What Is an AI-Assisted SDLC
Workflow?](a07-what-is-an-ai-assisted-sdlc-workflow.md), the Feasibility
chat is its own agent with one role: Product Manager. It takes the place of
the research and writing that a product team would do by hand.

| Stage | What the Feasibility chat does | What you do |
|---|---|---|
| **Spitballing and brainstorming** | Suggests ideas, asks clarifying questions, and plays devil's advocate. | Supply the problem and pick the ideas worth pursuing. |
| **Initial research** | Searches for competitors, similar products, and possible legal issues. | Check the findings and add what you know. |
| **One-pager** | Drafts a one-pager for each idea using template d02-01. | Review and correct it. |
| **Feasibility study** | For larger projects, expands the one-pager into a full study using template d02-02, including interview questions for future customers. | Run the interviews and bring back the answers. |
| **Pitch** | Compares one or more ideas side by side for the stakeholders using template d02-03. | Present them, or share the summary. |
| **Proposal** | When an outside party must approve or fund the work, drafts the proposal in the format they require, or with template d02-04 if they have none. | Check it against their guidelines, then submit it. |

When the pitch, and any proposal, is done, take the outputs to the
**Tracking chat**. It summarizes the result, and the stakeholders make the
call described in [Step 1: Tracking](b01-tracking.md):

- **Go:** the one-pager, feasibility study, and any approved proposal are
  attached to the **Requirements chat**, which turns them into the Product
  Requirements Document (PRD). Anything the proposal promised becomes a
  constraint the PRD must honor. The Product Manager role continues into
  Step 3.
- **Park:** the idea is sound but the timing isn't, or the project is
  waiting on an outside funding decision. The outputs are saved until it can
  be reopened.
- **Abandon:** the idea is closed, and the reasons are recorded so no one
  repeats the study.

The agent does **not** make the decision. As [Understanding
AI](a05-understanding-ai.md) reminds us, AI is a smart assistant, not a
boss. It gathers the evidence and lays out a recommendation; the
stakeholders decide.

---

## Prompts, Templates, and Samples

> **To be updated:** This section will link to sample documents for the
> Feasibility chat as they become available.

**Prompts** (in `prompts/`):

- [`c02-feasibility-prompt`](../prompts/c02-feasibility-prompt.md): the
  Product Manager prompt for this step, covering intake questions,
  research, each template, and the hand-off to Tracking

**Templates** (in `templates/`):

- [`d02-01-one-pager`](../templates/d02-01-one-pager.md): one-page summary
  of a product idea
- [`d02-02-feasibility-study`](../templates/d02-02-feasibility-study.md):
  full feasibility study for larger projects
- [`d02-03-pitch-summary`](../templates/d02-03-pitch-summary.md):
  side-by-side comparison of ideas for the go/no-go decision
- [`d02-04-proposal`](../templates/d02-04-proposal.md): proposal for outside
  approval or funding

**Samples** (in [`samples/BeautifulBeachParkVolunteers/docs/`](../samples/BeautifulBeachParkVolunteers/docs/)):

- **d02-01:** the sample project's one-pager: *coming soon*

Additional [case studies](case-studies.md) may be added to this repo at a
future time.

---

**Learn more:**

- [Step 1: Tracking](b01-tracking.md): where the go/no-go decision is
  recorded
- [Step 3: Requirements](b03-requirements.md): the next step, which takes
  this step's outputs as input
