# Samples

Two samples that show the ideas in this repo in action:

- **BeautifulBeachPark Volunteers** is a finished sample project, so you can
  see what your own project folder and documents should look like at every
  step, not just the templates' headings.
- **Five Persona Council** is a small decision-making skill that shows the
  multi-AI-agent idea on its own, outside of software development.

## The sample project: BeautifulBeachPark Volunteers

[`BeautifulBeachParkVolunteers/`](BeautifulBeachParkVolunteers/) is a
volunteer sign-up app for **BeautifulBeachPark**, a made-up park.
Coordinators post tasks such as Raking Leaves, Pulling Weeds, Beach
Cleanup, and Driftwood Removal, and volunteers sign up for one-hour slots
using a username only.

The sample folder has the same layout as the [skeleton](../skeleton/), so
you can compare your folder with it after any step. For example, after
Step 3 your `docs/` folder should have a PRD like
`BeautifulBeachParkVolunteers/docs/d03-01-prd.md`.

## The Five Persona Council

[`FivePersonaCouncil/`](FivePersonaCouncil/) holds a **skill**, a short set
of instructions that teaches Claude a repeatable task. When you face a
decision, five AI advisors with very different viewpoints weigh in, and a
Chairman pulls their views together into one verdict: the decision to make,
the biggest risk, and the first step.

It's the example used in
[The Multi-AI-Agent Paradigm](../docs/a02-multi-ai-agent-paradigm.md). The
folder includes the ready-made `SKILL.md`, a prompt for having Claude build
the skill yourself, install steps, and credits to the open-source work it's
adapted from.

## Samples and case studies: what's the difference?

| | Sample (this folder) | Case studies (`eNN`) |
|---|---|---|
| **What it is** | A made-up project, written to teach | Real projects for real organizations |
| **Where it lives** | Here, in `samples/` | Each in its own repository |
| **Size** | Short: about one page per document | Complete, and as messy as real work |

Additional [case studies](../docs/case-studies.md) may be added to this repo
at a future time.

## How the sample is kept

- **One story from start to finish.** The use cases in the sample PRD
  appear in the sample Spec's sequence diagrams, which become the screens in
  the sample UI/UX Document, the same way the workflow's chats hand off to
  each other.
- **Named after the templates.** Each document uses the file name of the
  template it fills in, so `docs/d03-01-prd.md` is a filled-in copy of
  `templates/d03-01-prd.md`.
- **Made by the prompts.** Each sample document is created by running that
  step's chat with its prompt, which also tests the prompts.
- **Kept in step with the templates.** When a template changes, its sample
  document is updated to match.

*Sample documents coming soon.*
