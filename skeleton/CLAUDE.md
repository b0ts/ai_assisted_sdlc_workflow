# CLAUDE.md

Instructions for Claude when working in this project.

## Project

<Project Name>: <one-sentence description>.

This project follows the AI-assisted SDLC workflow at
https://github.com/b0ts/ai_assisted_sdlc_workflow. Each step's chat has its own
role, inputs, and outputs; see that repo's `docs/` folder for the step guides.

## Where things go

- `docs/`: step deliverables, named by d-number (`dNN-NN-<name>.md`), for
  example `d01-01-checklist.md` or `d03-01-prd.md`
- `prompts/`: prompts used for this project, named by c-number
  (`cNN-<name>-prompt.md`)
- `tests/`: automated tests; write tests before the code they check
- `src/`: source code
- `assets/`: images, media, and data files

## Rules

- Keep files in the folders above; ask before adding a new top-level folder.
- Don't change an approved deliverable in `docs/` without being asked; suggest
  changes instead.
