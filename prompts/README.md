# Prompts

Predefined prompts for each step's chat. Names start with the step number. If a step ever needs more than one prompt, a second number is added (`c01-01-...`, `c01-02-...`).

- [c00-new-project-prompt.md](c00-new-project-prompt.md): Start a new project (Project Setup Assistant): asks the name and your GitHub link, creates the folder from `project-template/`, creates and pushes the GitHub repo, then starts Step 1. The manual alternative is Part 1 of [`project-template/START-HERE.md`](../project-template/START-HERE.md)
- [c01-tracking-prompt.md](c01-tracking-prompt.md): Step 1, Tracking (Scrum Master)
- [c02-feasibility-prompt.md](c02-feasibility-prompt.md): Step 2, Feasibility (Product Manager)
- [c03-requirements-prompt.md](c03-requirements-prompt.md): Step 3, Requirements (Product Manager)
- [c04-design-prompt.md](c04-design-prompt.md): Step 4, Design (Software Architect)
- [c05-user-experience-prompt.md](c05-user-experience-prompt.md): Step 5, User Experience (UI/UX Designer)
- [c06-initial-infrastructure-prompt.md](c06-initial-infrastructure-prompt.md): Step 6, Initial Infrastructure (DevOps Engineer)
- [c07-test-creation-prompt.md](c07-test-creation-prompt.md): Step 7, Test Creation (SDET)
- [c08-01-implementation-prompt.md](c08-01-implementation-prompt.md): Step 8, Implementation (Software Engineer)
- [c08-02-code-review-prompt.md](c08-02-code-review-prompt.md): Step 8, Independent Code Review (Code Reviewer), run in a new Claude Code session and in a second AI tool such as Codex
- [c08-03-hands-on-review-prompt.md](c08-03-hands-on-review-prompt.md): Step 8, Hands-On Review (helper for the person who uses the running app: ad-hoc testing and usability)
- [c08-04-polishing-prompt.md](c08-04-polishing-prompt.md): Step 8, Polishing (partner for the person who built the app: a sanity check and fine-tuning, between the code reviews and the hands-on review)
- [c09-release-prompt.md](c09-release-prompt.md): Step 9, Release (Release Manager)
- [c10-maintenance-prompt.md](c10-maintenance-prompt.md): Step 10, Maintenance (SRE / Maintenance Engineer)

See the [numbering system](../README.md#numbering-system) for the full scheme.

## Prompt-writing examples

These two files are not step prompts. They are the informal and formal prompts used to write [Steps, Roles, and Deliverables](../docs/a04-steps-roles-and-deliverables.md), kept as examples for [Prompt Engineering](../docs/a06-prompt-engineering.md). They are saved exactly as written, so they still use the old file names and the nine-step list.

- [example-01-roles-and-deliverables.md](example-01-roles-and-deliverables.md): informal prompt
- [example-02-roles-and-deliverables.md](example-02-roles-and-deliverables.md): formal prompt

A copy of every prompt is also in [`project-template/prompts/`](../project-template/prompts/), for new projects. After changing a prompt here, run `python3 scripts/build_project_template.py` to refresh the copies.
