# CLAUDE.md

Instructions for Claude when working in this project.

## Project

<Project Name>: <one-sentence description>.

This project follows the AI-assisted SDLC workflow at
https://github.com/b0ts/ai_assisted_sdlc_workflow: a Waterfall Software
Development Life Cycle adapted for Test-Driven Development, where each of ten
steps is carried out by its own AI chat playing one role. `START-HERE.md`
explains how to run the steps; the workflow repo's `docs/` folder has a guide
for each step (b01 to b10).

## Where things go

- `prompts/`: one prompt per step's role, named by c-number
  (`cNN-<name>-prompt.md`). When a chat is asked to "follow this prompt,"
  play that role and stay within it.
- `docs/`: step deliverables, named by d-number (`dNN-NN-<name>.md`), for
  example `d01-01-checklist.md` or `d03-01-prd.md`. Every deliverable starts
  as a blank template with `[placeholders]` and hint comments; a step fills
  its own in place. When a prompt says to use a template "from the workflow
  repository's `templates/` folder," use the file of the same name here in
  `docs/`. A file that still holds `[placeholders]` hasn't been written yet.
- `tests/`: automated tests, written in Step 7 before any code
- `src/`: source code, written in Step 8 to pass the tests
- `assets/`: images, media, and data files

## Rules

- Keep files in the folders above; ask before adding a new top-level folder.
- Follow the steps in order. Step 1 (Tracking) starts first and records every
  decision; a step starts only when the Tracking chat's Next Action points to
  it.
- Don't change an approved deliverable in `docs/` without being asked;
  suggest changes instead. A change to an earlier step's document is a
  "go-back": it goes to that step's chat and is approved in the Tracking chat.
- After Step 7, the tests are locked: change the code to pass them, never the
  other way round. Only the SDET chat changes a test, with a recorded reason.
- Never write passwords, keys, or real people's information into the code,
  the documents, or a chat.
- A person decides at every step. Ask, in one numbered list, rather than
  guess.
