# Contributing

How to work on this project with others. It follows the
[AI-Assisted SDLC Workflow](https://github.com/b0ts/ai_assisted_sdlc_workflow):
ten steps, each carried out by its own AI chat, with a person deciding at
every step. The README's **Collaborators and ownership** section says who's
involved and who owns the work.

## Joining a Project Already Under Way

You can follow a public project without joining it: anyone with its link
can read it on GitHub, with no account needed. Its README's **Status**
says which step it's on. To help with the work:

1. **Get invited.** You need a free [GitHub](https://github.com) account.
   Send your username to the project's owner; they add you as a
   collaborator, and GitHub emails you an invitation. Click **Accept
   invitation**. (Until then you can read the project but not change it.)
2. **Get the project onto your computer.** Install
   [GitHub Desktop](https://desktop.github.com) and sign in. Choose
   **File**, then **Clone Repository...**, pick the project from the list,
   choose where to put it, and click **Clone**.
3. **Catch up, in this order:**
   1. `README.md`: what the project is, and who's involved.
   2. The tracking checklist, [`docs/d01-01-checklist.md`](docs/d01-01-checklist.md):
      its **Next Action** says what's happening now, and its Decision Log
      says how it got there.
   3. The documents already approved, in step order (the checklist's
      Status Table lists them): for example, the one-pager (`d02-01`), then
      the requirements (`d03-01`), then the design (`d04-01`).
4. **Know which rules are already in force.** Approved documents don't
   change without a "go-back" approved in the Tracking chat. After Step 7,
   the tests are locked (see Rules below).
5. **Agree on your part** with the project's owner: which step or document
   you'll work on, and whether you'll sign anything off. The Tracking chat
   records it.

To run a step's chat yourself, start your own chat with the step's prompt
from [`prompts/`](prompts/) and attach the documents it needs; see
`START-HERE.md`, Part 2.

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
