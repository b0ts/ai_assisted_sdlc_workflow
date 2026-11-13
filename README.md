# AI-Assisted SDLC Workflow

Documentation and templates for incorporating AI assistance into the software development lifecycle (SDLC).

## Start here

- [Introduction](docs/a01-introduction.md) — start here: what this repo teaches, how it's organized, and the order to read it in
- [What Is a Software Development Lifecycle Workflow?](docs/a03-what-is-an-sdlc-workflow.md) — a plain-language introduction for non-programmers
- [Building Your Own App](docs/a10-building-your-own-app.md) — the step-by-step walkthrough for your own project
- [Project template](project-template/START-HERE.md) — the starter kit to copy into a new project: directions, every prompt, and blank deliverables
- [Documentation index](docs/README.md) — all how-to guides and the ten step guides

## Numbering system

Every file starts with a letter that says what kind of file it is. Steps are numbered 01 to 10, and that number links a step's guide, prompts, templates, and sample documents.

| Prefix | What it is | Where it lives | Example |
|---|---|---|---|
| **a**NN | How-to and background guides | [`docs/`](docs/) | `a01-introduction.md` |
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

The [`samples/`](samples/) folder holds a finished sample project: [BeautifulBeachPark Volunteers](samples/BeautifulBeachParkVolunteers/), a volunteer sign-up app for a made-up park. It has the same layout as the [`project-template/`](project-template/), so you can compare your own project folder with it after any step, then build your own version by following the docs.

## Starting your own project

**Fastest start: let Claude set it up.** Claude creates the project folder,
copies in the starter kit, creates the project's GitHub repo, makes the
first push, and starts Step 1.

1. **Once, on your computer:** install Git and the
   [GitHub CLI](https://cli.github.com). In Terminal, run `gh auth status`
   to check it's signed in; if it isn't, run `gh auth login` and follow its
   questions. (Claude never asks for your password.)
2. **Use a Claude chat that can run commands on your computer:** Claude
   Code, or a Claude desktop thread linked to your computer. A plain chat
   can't create the repo.
3. **Start a new thread** (for example, `00-new-project`) and say:
   > Use the ai_assisted_sdlc_workflow for a new project:
   > https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/prompts/c00-new-project-prompt.md

   If the chat can't open the link, attach
   [`prompts/c00-new-project-prompt.md`](prompts/c00-new-project-prompt.md)
   instead.
4. **Answer its questions:** the project's name, a sentence about it, your
   GitHub link, private or public, who may use the code, and whether others
   will work on it. For the **projects folder**, give the folder your
   projects live in; if it holds your copy of this repo, Claude copies the
   starter kit from there, after updating it.
5. **Confirm the summary.** Claude creates everything, then starts Step 1
   in the same thread, which becomes the project's Tracking chat.

**Or do it yourself:** copy the [`project-template/`](project-template/)
folder into a new project folder, and follow Part 1 of its
[`START-HERE.md`](project-template/START-HERE.md), with menus in Finder and
GitHub Desktop: create the project's GitHub repo, then run the steps,
starting with the Scrum Master (Step 1). Its `prompts/` and `docs/` folders are copies of this repo's
prompts and templates; after changing either, run
`python3 scripts/build_project_template.py` to refresh the copies.

## Case studies

Additional [case studies](docs/case-studies.md) may be added to this repo at a future time.

## Status

This is a work in progress. Content is being added incrementally.
