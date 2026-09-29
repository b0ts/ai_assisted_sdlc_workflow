# AI-Assisted SDLC Workflow

Documentation and templates for incorporating AI assistance into the software development lifecycle (SDLC).

## Start here

- [What Is a Software Development Lifecycle Workflow?](docs/a01-what-is-an-sdlc-workflow.md) — a plain-language introduction for non-programmers
- [Documentation index](docs/README.md) — all how-to guides and the ten step guides

## Numbering system

Every file starts with a letter that says what kind of file it is. Steps are numbered 01 to 10, and that number links a step's guide, prompts, templates, and examples.

| Prefix | What it is | Where it lives | Example |
|---|---|---|---|
| **a**NN | How-to and background guides | [`docs/`](docs/) | `a01-what-is-an-sdlc-workflow.md` |
| **b**NN | Step guides, one per step | [`docs/`](docs/) | `b01-tracking.md` |
| **c**NN | Predefined prompts: step number, plus a second number if a step needs more than one prompt | [`prompts/`](prompts/) | `c01-tracking-prompt.md` |
| **d**NN-NN | Templates: step number, then document number | [`templates/`](templates/) | `d01-01-checklist`, `d01-02-gantt` |
| **e**NN | Worked examples, each in its own repository | see below | `e01` RC Park Tour |

### The ten steps

| Step | Name | Role |
|---|---|---|
| 01 | [Tracking](docs/b01-tracking.md) (starts first, runs throughout) | Scrum Master |
| 02 | [Feasibility](docs/b02-feasibility.md) | Product Manager |
| 03 | [Requirements](docs/b03-requirements.md) | Product Manager |
| 04 | [Design](docs/b04-design.md) | Software Architect |
| 05 | [User Experience](docs/b05-user-experience.md) | UI/UX Designer |
| 06 | [Infrastructure](docs/b06-infrastructure.md) | DevOps Engineer |
| 07 | [Test Creation](docs/b07-test-creation.md) | SDET |
| 08 | [Implementation](docs/b08-implementation.md) | Software Engineer |
| 09 | [Release](docs/b09-release.md) | Release Manager |
| 10 | [Upkeep](docs/b10-upkeep.md) | SRE / Maintenance Engineer |

## Examples

Each example lives in its own repository. Inside an example repo, files use the same c and d numbers as the prompts and templates they came from (for example, `d01-01-checklist.md` is that project's tracking checklist). E-numbers are never reused; retired examples are marked archived.

| # | Example | Repository |
|---|---|---|
| e01 | RC Park Tour: an interactive and printable tour of Rosicrucian Park in San Jose | [b0ts/rc_park_tour](https://github.com/b0ts/rc_park_tour) |

## Status

This is a work in progress. Content is being added incrementally.
