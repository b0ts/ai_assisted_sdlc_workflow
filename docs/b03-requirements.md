# Step 3: Requirements (The Product Manager Chat, Continued)

**Role:** Product Manager · **Prompts:** c03-xx · **Templates:** d03-xx

## Executive Summary

Once the stakeholders say **go** at the end of
[Step 2: Feasibility](b02-feasibility.md), the question changes from *"Should
we build this?"* to *"What exactly are we building, and for whom?"* The
answer is written down in a **Product Requirements Document (PRD)**.

Requirements is **Step 3**, and it is played by the **same role as Step 2:
the Product Manager**. The person (or AI chat) who studied the idea and
pitched it is the best one to turn it into a clear description of what the
product must do.

- **Inputs:** the approved one-pager or feasibility study from Step 2, the
  go decision and any conditions recorded by the
  [Tracking chat](b01-tracking.md), and other inputs such as customer
  interview notes, competitor research, and rules the product must follow.
- **Output:** the **PRD**, filled in from the template
  [`d03-01-prd`](../templates/d03-01-prd.md): who the users are, what they
  need to do (the **use cases**), a **UML Use Case Diagram**, and how
  success is measured.
- **Hand-off:** once the PRD is signed off, it becomes the main input to
  [Step 4: Design](b04-design.md), where the Software Architect writes the
  Software Design Specification ("Spec").

---

## The Same Role, a New Job

In Feasibility, the Product Manager worked **wide**: many ideas, quick
research, and a pitch. In Requirements, the Product Manager works **deep**:
one approved idea, described carefully enough that a whole team could build
it without guessing. Keeping the same role gives **continuity** (the PM
already knows the problem, the customers, and the promises made in the
pitch) and **ownership** (when a later step asks what the product should
do, the answer comes back to the PM).

Requirements still runs in its **own new chat**, following the Multi Chat
Prompt Chaining (MCPC) approach in
[What Is an AI-Assisted SDLC Workflow?](a05-what-is-an-ai-assisted-sdlc-workflow.md).
Only the approved Step 2 documents carry forward. If something from
Feasibility isn't written down, the Requirements chat won't know about it,
which is a quick way to spot gaps.

---

## Users, Use Cases, and UML

The PRD is built around three connected ideas. The
[PRD template](../templates/d03-01-prd.md) has a section for each.

**Users (template Section 3).** Every requirement exists to serve someone,
so the PRD starts by naming everyone and everything that interacts with the
system. These are called **actors**: **primary users** the product is built
for, **secondary users** such as administrators and support staff, and
**external systems** such as a payment or map service. Each gets a short
profile: who they are, what they want to get done, and what could get in
their way. A common mistake is writing for one imaginary "user" who is
really just the author, which misses the needs of admins and people using
accessibility tools.

**Use cases (template Section 5).** A **use case** describes one goal a user
wants to reach, such as *"Book a tour,"* written from the user's point of
view with no mention of how the software works inside. Each one lists the
normal step-by-step path, what happens when things go differently, a
priority, and **acceptance criteria**: specific, checkable statements of
when it's done correctly. Because this workflow uses **Test-Driven
Development**, the SDET in [Step 7](b07-test-creation.md) turns those
criteria into automated tests before any code is written. A vague
requirement leads to a vague test.

**UML Use Case Diagram (template Section 4).** **UML (Unified Modeling
Language)** is a standard set of diagram types used across the software
industry. Its Use Case Diagram gives a one-glance picture of the product's
scope: **stick figures** are actors, **ovals** are use cases, **lines**
connect them, and a **box** marks the edge of the system. It is
**required** in every PRD (see the UML Diagram Guide in the
[RC Park Tour case study](rc-park-tour-ai-sdlc-case-study.md)), because the
Architect draws one sequence diagram per use case and the SDET writes tests
per use case. A use case missing from this diagram will likely be missing
from everything that follows. AI can draw it as
[Mermaid](https://mermaid.js.org/) text, as the template shows, or in
[PlantUML](https://plantuml.com/use-case-diagram) for official UML shapes.

---

## What a Good PRD Is, and Isn't

| A good PRD **is** | A good PRD **is not** |
|---|---|
| Focused on **what** the product does and **why** | A design of **how** it will be built |
| Written from the users' point of view | A list of features someone thought would be cool |
| Specific and testable ("loads in under 2 seconds on a phone") | Vague ("fast and easy to use") |
| Clear about scope, including what is **out of scope** | Open-ended, letting every new idea slip in |
| Prioritized, so phases can be planned | A wish list where everything is equally urgent |
| Short enough to read, and kept up to date | A giant document nobody opens after sign-off |

Beyond users and use cases, the template prompts the Product Manager to
consider goals and success measures carried over from Feasibility,
**quality requirements** (speed, reliability, accessibility, devices),
**constraints** (laws, privacy, copyright, budget), **scope and phases**,
and **assumptions and open questions**, written down so they can be
checked instead of silently guessed.

---

## The PRD and the Spec: "What" Versus "How"

The most important boundary in this step is between the **PRD** and the
**Software Design Specification ("Spec")** written in
[Step 4: Design](b04-design.md).

| | PRD (Step 3) | Spec (Step 4) |
|---|---|---|
| **Answers** | *What* will the product do, and *for whom*? | *How* will we build it? |
| **Owner** | Product Manager | Software Architect |
| **Contains** | Users, use cases, acceptance criteria, priorities, constraints | System structure, data, technology choices, security design |
| **Key diagram** | UML Use Case Diagram | UML Sequence Diagram for each use case |
| **Example** | "A visitor can book a tour and get a confirmation." | "Bookings are saved in a database and confirmations sent through an email service." |

Think back to the house example from
[What Is a Software Development Lifecycle Workflow?](a01-what-is-an-sdlc-workflow.md).
The PRD is the homeowner's list: *three bedrooms, a kitchen big enough for
family dinners, a ramp for Grandma's wheelchair.* The Spec is the
architect's blueprint: *where the walls go, which beams hold the roof, how
steep the ramp can be.* The homeowner shouldn't pick the beams, and the
architect shouldn't decide how many bedrooms the family needs.

Keeping them apart gives the Architect **freedom** to choose the best *how*,
and **traceability**: every part of the Spec should map back to a use case
in the PRD, and design with no matching use case is often something nobody
asked for. When the Architect finds a use case too costly or complex, the
fix goes back to the PRD, for example by splitting delivery into phases, as
described in [Step 1: Tracking](b01-tracking.md). The change is recorded in
the PRD's change log, and the Spec picks up from the revised version.

---

## The Product Manager Agent in Our Workflow

| Stage | What the Requirements chat does | What you do |
|---|---|---|
| **Review inputs** | Summarizes the Step 2 documents and lists gaps and open questions. | Answer the questions or bring in missing notes. |
| **Identify users** | Proposes actors and user profiles. | Confirm who the real users are, and add any missing. |
| **Write use cases** | Drafts use cases with flows, acceptance criteria, and priorities. | Correct them, and decide priorities. |
| **Draw the diagram** | Produces the UML Use Case Diagram. | Check that nothing is missing or out of place. |
| **Assemble the PRD** | Fills in the `d03-01` template. | Review it, then take it to the Tracking chat for sign-off. |

As with every step, the agent drafts and recommends, and **people decide**.
The stakeholders sign off the PRD through the Tracking chat before the
Design chat begins.

---

## Examples, Templates, and Prompts

> **To be updated:** This section will link to real-world material for the
> Requirements chat as it becomes available.

**Prompts** (in `prompts/`):

- `c03-01`: identify users and draft use cases from the feasibility outputs:
  *coming soon*
- `c03-02`: assemble the PRD with a UML Use Case Diagram: *coming soon*

**Templates** (in `templates/`):

- [`d03-01-prd`](../templates/d03-01-prd.md): Product Requirements Document

**Examples** (each in its own repository):

- **e01 · d03-01:** the PRD from the [RC Park
  Tour](https://github.com/b0ts/rc_park_tour) project: *coming soon*

---

**Learn more:**

- [Step 2: Feasibility](b02-feasibility.md): where this step's inputs come
  from
- [Step 4: Design](b04-design.md): the next step, which turns the PRD into
  the Spec
- [Use case diagram (Wikipedia)](https://en.wikipedia.org/wiki/Use_case_diagram):
  a plain introduction to UML use case diagrams
