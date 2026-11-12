# <Project Name>

<One or two sentences describing what this project is and who it's for.>

This project follows the
[AI-Assisted SDLC Workflow](https://github.com/b0ts/ai_assisted_sdlc_workflow):
ten steps, each carried out by its own AI chat, with a person deciding at
every step. [`START-HERE.md`](START-HERE.md) explains how to run them.

## Folder layout

| Folder | What goes in it |
|---|---|
| [`docs/`](docs/) | The documents each step produces, named by their d-number (for example, `d03-01-prd.md`). Each starts as a blank template. |
| [`prompts/`](prompts/) | The prompt for each step's chat, named by their c-number (for example, `c01-tracking-prompt.md`) |
| [`tests/`](tests/) | Automated tests, written before the code (Step 7: Test Creation) |
| [`src/`](src/) | The project's source code (Step 8: Implementation) |
| [`assets/`](assets/) | Images, media, and data files the project uses |

## Status

<Where the project stands, for example: "Step 2: Feasibility in progress.">
The tracking checklist, [`docs/d01-01-checklist.md`](docs/d01-01-checklist.md),
has the details.
