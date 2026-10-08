# AI-Assisted SDLC Workflow

Documentation and templates for incorporating AI assistance into the software development lifecycle (SDLC).

## Start here

- [What Is a Software Development Lifecycle Workflow?](docs/a03-what-is-an-sdlc-workflow.md) — a plain-language introduction for non-programmers
- [Documentation index](docs/README.md) — all how-to guides and the ten step guides

## Numbering system

Every file starts with a letter that says what kind of file it is. Steps are numbered 01 to 10, and that number links a step's guide, prompts, templates, and sample documents.

| Prefix | What it is | Where it lives | Example |
|---|---|---|---|
| **a**NN | How-to and background guides | [`docs/`](docs/) | `a03-what-is-an-sdlc-workflow.md` |
| **b**NN | Step guides, one per step | [`docs/`](docs/) | `b01-tracking.md` |
| **c**NN | Predefined prompts: step number, plus a second number if a step needs more than one prompt | [`prompts/`](prompts/) | `c01-tracking-prompt.md` |
| **d**NN-NN | Templates: step number, then document number | [`templates/`](templates/) | `d01-01-checklist`, `d01-02-gantt` |
| **d**NN-NN | Sample documents: filled-in templates for the made-up sample project, named after the template they fill in | [`samples/`](samples/) | `samples/BeautifulBeachParkVolunteers/docs/d03-01-prd.md` |
| **e**NN | Case studies of real projects, each in its own repository | [`docs/case-studies.md`](docs/case-studies.md) | None yet |

### The ten steps

| Step | Name | Role |
|---|---|---|
| 01 | [Tracking](docs/b01-tracking.md) (starts first, runs throughout) | Scrum Master |
| 02 | [Feasibility](docs/b02-feasibility.md) | Product Manager |
| 03 | [Requirements](docs/b03-requirements.md) | Product Manager |
| 04 | [Design](docs/b04-design.md) | Software Architect |
| 05 | [User Experience](docs/b05-user-experience.md) | UI/UX Designer |
| 06 | [Initial Infrastructure](docs/b06-infrastructure.md) (DevOps support continues through step 10) | DevOps Engineer |
| 07 | [Test Creation](docs/b07-test-creation.md) | SDET |
| 08 | [Implementation](docs/b08-implementation.md) | Software Engineer |
| 09 | [Release](docs/b09-release.md) | Release Manager |
| 10 | [Maintenance](docs/b10-maintenance.md) | SRE / Maintenance Engineer |

## Sample

The [`samples/`](samples/) folder holds a finished sample project: [BeautifulBeachPark Volunteers](samples/BeautifulBeachParkVolunteers/), a volunteer sign-up app for a made-up park. It has the same layout as the [`skeleton/`](skeleton/), so you can compare your own project folder with it after any step, then build your own version by following the docs.

## Case studies

Additional [case studies](docs/case-studies.md) may be added to this repo at a future time.

## Status

This is a work in progress. Content is being added incrementally.
