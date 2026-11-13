# Contributing

How to work on this project with others. It follows the
[AI-Assisted SDLC Workflow](https://github.com/b0ts/ai_assisted_sdlc_workflow):
ten steps, each carried out by its own AI chat, with a person deciding at
every step. The README's **Collaborators and ownership** section says who's
involved and who owns the work.

## The Shared Record

- **The tracking checklist,** [`docs/d01-01-checklist.md`](docs/d01-01-checklist.md),
  is everyone's source of truth: which step the project is on, every
  decision, every open issue, and who approves each step. Check it before
  you start.
- **The documents in `docs/` carry the work between people,** not the AI
  chats. Each person runs their own step chats, with the same prompts from
  [`prompts/`](prompts/), and attaches the documents they need.
- **Steps go in order,** and the Tracking chat records each decision. A
  change to an earlier step's document is a "go-back": it goes to that
  step's chat and is approved in the Tracking chat.

## Making a Change

With [GitHub Desktop](https://desktop.github.com):

1. **Get the latest first:** choose **Repository**, then **Pull**.
2. **For anything bigger than a small fix, use a branch:** choose
   **Branch**, then **New Branch...**, name it after the change (for
   example, `prd-volunteer-roles`), and click **Create Branch**.
3. **Make the change,** following the workflow's order: documents first,
   then a test that fails, then the code, then every test.
4. **Commit:** type a short summary at the bottom left, and click
   **Commit to** your branch.
5. **Share it:** click **Publish branch** (or **Push origin**), then
   **Create Pull Request**. Others read it on GitHub, and a person merges
   it into `main` when it's approved.

Small fixes on your own can go straight to `main`: pull, commit, push.

## Rules

- After Step 7, the tests are locked: change the code to pass them, never
  the other way round. Only the SDET chat changes a test, with a recorded
  reason.
- Never commit passwords, keys, or real people's information.
- Someone who didn't build a part makes a good reviewer for it, including
  the hands-on review in Step 8.
