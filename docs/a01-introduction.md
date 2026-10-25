# Introduction

## Executive Summary

This repo teaches you how to build software with help from **artificial
intelligence (AI)**, even if you have never written a line of code or heard
the term **SDLC** before. It gives you a step-by-step plan, a set of
ready-made AI instructions, fill-in-the-blank documents, and a finished
sample project to copy from. You stay in charge and make the decisions. The
AI does most of the writing and building.

The repo is organized in four sections, **a** through **d**, so you can
always tell what kind of file you're looking at and where it fits.

---

## An Everyday Comparison: A Cooking Class

Think of this repo as a cooking class. Section **a** is the opening lecture:
what the kitchen tools are and why recipes matter. Section **b** walks
through each course of the meal, one at a time. Section **c** is the
recipe cards you take home and reuse. Section **d** is the blank shopping
lists and prep sheets. The sample project is the instructor's finished
dish, which you can taste and compare against your own.

---

## How the Repo Is Organized

Every file name starts with a letter that tells you what kind of file it is,
followed by a number. Steps are numbered 01 to 10, and that number links a
step's guide, prompt, templates, and sample documents together.

```
ai_assisted_sdlc_workflow/
├── docs/        a01–a09   Background and how-to guides (section a)
│                b01–b10   One guide per SDLC step (section b)
├── prompts/     c01–c10   Ready-made AI prompts, one per step (section c)
├── templates/   d01–d10   Fill-in documents for each step's deliverables
├── samples/               Finished examples
│   ├── BeautifulBeachParkVolunteers/   The complete sample project
│   └── FivePersonaCouncil/             A small multi-AI decision helper
└── skeleton/              Empty starter folder for your own project
```

See the [numbering system](../README.md#numbering-system) for full details.

---

## Section a: The Background

Read these in order. Each one builds on the last.

| Guide | What you'll learn |
|---|---|
| [a02 The Multi-AI-Agent Paradigm](a02-multi-ai-agent-paradigm.md) | Why several AI chats, each playing a different role and led by one coordinator, give better results than a single chatbot |
| [a03 What Is an SDLC Workflow?](a03-what-is-an-sdlc-workflow.md) | What a **Software Development Lifecycle** is: a step-by-step plan for turning an idea into working software, and the Test-Driven Development (TDD) version this repo uses |
| [a04 Steps, Roles, and Deliverables](a04-steps-roles-and-deliverables.md) | The ten steps, who owns each one, and the documents each one produces |
| [a05 Understanding AI](a05-understanding-ai.md) | What AI is good at, where it needs checking, and the six parts of a good instruction |
| [a06 Prompt Engineering](a06-prompt-engineering.md) | How to write a **prompt**, the message that tells the AI what you want, and which of four prompt types to use |
| [a07 What Is an AI-Assisted SDLC Workflow?](a07-what-is-an-ai-assisted-sdlc-workflow.md) | How AI roles and SDLC steps combine: ten chained AI chats, one per step, each passing its finished document to the next |
| [a08 Implementing an AI-Assisted SDLC Workflow](a08-implementing-an-ai-assisted-sdlc-workflow.md) | Setting up your computer, Claude, and GitHub so you can start your own project |
| [a09 UML Diagram Guide](a09-uml-diagram-guide.md) | Which standard software diagrams every project needs, and which only some do |

---

## Section b: The Ten Steps

Each step guide explains the AI's role, the prompt to use, what goes in,
what comes out, and the deliverables someone must approve before the next
step begins.

| Step | Name | AI role |
|---|---|---|
| 01 | [Tracking](b01-tracking.md) (runs throughout) | Scrum Master |
| 02 | [Feasibility](b02-feasibility.md) | Product Manager |
| 03 | [Requirements](b03-requirements.md) | Product Manager |
| 04 | [Design](b04-design.md) | Software Architect |
| 05 | [User Experience](b05-user-experience.md) | UI/UX Designer |
| 06 | [Initial Infrastructure](b06-infrastructure.md) (support continues) | DevOps Engineer |
| 07 | [Test Creation](b07-test-creation.md) | SDET |
| 08 | [Implementation](b08-implementation.md) | Software Engineer |
| 09 | [Release](b09-release.md) | Release Manager |
| 10 | [Maintenance](b10-maintenance.md) | SRE / Maintenance Engineer |

Notice that **tests are written before the software is built** (step 7
comes before step 8). That's the heart of Test-Driven Development: the AI
keeps building until every check passes.

---

## Section c: Reusable Prompts

The [`prompts/`](../prompts/) folder holds one ready-made prompt per step.
They're written to be **generic**, so they work for any project, not just
the sample. To run a step, you open a new AI chat, paste in that step's
prompt, and attach the previous step's finished document. You don't have to
write prompts from scratch.

---

## Samples, Skeleton, and Templates

- **[BeautifulBeachPark Volunteers](../samples/BeautifulBeachParkVolunteers/)**
  is a finished sample: a volunteer sign-up app for a made-up park. It has a
  filled-in document for every step plus working code and tests. Whenever a
  step feels abstract, open the matching sample file.
- **[`skeleton/`](../skeleton/)** is an empty project folder with the same
  layout as the sample. Copy it to start your own app.
- **[`templates/`](../templates/)** holds the fill-in documents (d-numbers)
  that each step produces, so every project's paperwork looks the same.

---

## Key Takeaways

- An **SDLC** breaks building software into small, ordered steps, each with
  a role and a written result.
- Giving each step to a **separate AI chat with one role** produces more
  reliable work than one chat doing everything.
- **You** review and approve every step's result before moving on.
- Start with [a02](a02-multi-ai-agent-paradigm.md), keep the sample project
  open beside you, and use the prompts and templates when you build your own.

**Next:** [a02 The Multi-AI-Agent Paradigm](a02-multi-ai-agent-paradigm.md)
