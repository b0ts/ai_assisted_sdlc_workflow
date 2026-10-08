# UML Diagram Guide

## Executive Summary

**UML (Unified Modeling Language)** is a standard set of diagram types used
across the software industry. Not every diagram type earns its place on
every project. Some add real clarity; others are extra work that nobody
reads. This guide splits them into **Required** diagrams, which every
project draws, and **Situational** diagrams, which are drawn only when a
stated condition applies.

---

## Required and Situational Diagrams

The role that owns a deliverable decides which situational diagrams to
include when it writes that deliverable. It records the decision (which
diagrams were included or skipped, and why) in a short **"Diagrams
included"** line at the top of the deliverable, so the choice is visible
rather than silent.

| Diagram | Owning role | Status | Include when… | Skip when… |
|---|---|---|---|---|
| Use Case Diagram | Product Manager (Step 3) | **Required** | Always. It defines the scope everything else traces back to. | — |
| Sequence Diagram | Software Architect (Step 4) | **Required** | Always, one per use case. It ties the Spec back to the PRD. | — |
| Deployment Diagram ("system diagram") | DevOps Engineer (Step 6) | **Required** | Always. The layout of computers and services is the core of the Infrastructure Document. | — |
| Class Diagram | Software Architect | Situational | The data has several kinds of information with real relationships between them. | There is only one kind of information, or simple lists with nothing interesting to connect. |
| Component Diagram | Software Architect | Situational | The system has several services or modules with connections that aren't obvious. | The system is a single module with no internal boundaries worth drawing. |
| Activity Diagram | Software Architect or Product Manager | Situational | A use case has real branching or decision logic: several paths and conditions. | The use case is a single straight path already covered by its sequence diagram. |
| State Machine Diagram | Software Architect | Situational | Something in the system has states that change how it behaves. | Nothing has states that matter. |

**An example from the sample.** In the
[BeautifulBeachPark volunteer app](../samples/BeautifulBeachParkVolunteers/),
a one-hour volunteer slot moves from **open**, to **filled** when someone
signs up, to **completed** after the shift, or back to **open** if the
volunteer cancels. Because the slot's state changes what people can do
with it, the Spec includes a State Machine Diagram for it.

---

## Drawing Diagrams With AI

AI can draw every diagram above as [Mermaid](https://mermaid.js.org/) text,
which displays as a picture on GitHub and in Visual Studio Code with a
Markdown preview. For official UML shapes, [PlantUML](https://plantuml.com/)
is an alternative.

---

**Learn more:**

- [Step 3: Requirements](b03-requirements.md): the Use Case Diagram
- [Step 4: Design](b04-design.md): sequence diagrams and the situational
  diagrams
- [Unified Modeling Language (Wikipedia)](https://en.wikipedia.org/wiki/Unified_Modeling_Language):
  a plain introduction to UML
