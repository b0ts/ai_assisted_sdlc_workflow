# Start Here: A New Project With the AI-Assisted SDLC Workflow

This folder is a **starter kit** for a new software project that follows the
[AI-Assisted SDLC Workflow](https://github.com/b0ts/ai_assisted_sdlc_workflow).
Copy it into a new project folder, and you get, ready to use:

| What | Where | What it's for |
|---|---|---|
| These directions | `START-HERE.md` | How to set up the project, then run each step |
| The **AI team** | [`prompts/`](prompts/) | One prompt per role: the Scrum Master, Product Manager, Software Architect, UI/UX Designer, DevOps Engineer, SDET, Software Engineer, Code Reviewer, Release Manager, and SRE. Each step's chat follows its prompt. |
| Blank **deliverables** | [`docs/`](docs/) | Every document the workflow produces, as a blank template with `[placeholders]`, named by its d-number (for example, `d03-01-prd.md`). Each step's chat fills its own in. |
| Instructions for Claude | `CLAUDE.md` | How this project is organized, and the workflow's rules |
| Places for the work | [`tests/`](tests/), [`src/`](src/), [`assets/`](assets/) | Tests (Step 7), code (Step 8), images and data |
| Your project's front page | `README.md` | Fill in the name and description |

You don't need to know how to program. You do need to read what each chat
produces and decide whether it's right: that is your job in every step.

**New to the workflow?** Read the repo's
[Introduction](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/a01-introduction.md)
first, and look at the finished sample project,
[BeautifulBeachPark Volunteers](https://github.com/b0ts/ai_assisted_sdlc_workflow/tree/main/samples/BeautifulBeachParkVolunteers),
to see what every document looks like when it's done. The full setup guide,
with pictures of each choice, is
[a08](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/a08-implementing-an-ai-assisted-sdlc-workflow.md),
and the step-by-step walkthrough is
[a10](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/a10-building-your-own-app.md).

Throughout, `<your-project>` stands for your project's name, for example
`OurGroupVolunteerApp`: letters and numbers, no spaces.

### Two Ways to Set Up

- **Let Claude do it (about 5 minutes).** In Claude Code, or a Claude
  thread that can run commands on your computer, say **"Use the
  ai_assisted_sdlc_workflow for a new project"** and attach the workflow
  repo's
  [`prompts/c00-new-project-prompt.md`](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/prompts/c00-new-project-prompt.md).
  It asks for the name and your GitHub link, does Steps A to D below for
  you, gives you the clicks for Step E, and starts Step 1. You need Git and
  the GitHub CLI, signed in once with `gh auth login` in Terminal; the
  prompt checks and explains. If you're reading this inside a project it
  already set up, skip to Part 2.
- **Do it yourself (about 30 minutes),** with menus, following Part 1. Use
  this way if you'd rather, or if you can't give Claude access to run
  commands or to your GitHub account.

---

## Part 1: Set Up the Project by Hand (About 30 Minutes, Once)

### What You Need First

- A free [GitHub](https://github.com) account.
- [GitHub Desktop](https://desktop.github.com), a free app for working with
  GitHub through menus. (Prefer a terminal? Every step below also says what
  to ask Claude Code.)
- The **Claude desktop app**, and **Claude Code** (needed from Step 6).
- A copy of the workflow repo on your computer, in your projects folder. In
  GitHub Desktop: choose **File**, then **Clone Repository...**, click the
  **URL** tab, paste `https://github.com/b0ts/ai_assisted_sdlc_workflow`,
  choose your projects folder as the **Local Path**, and click **Clone**.
  If you already have it, get the latest version: select it in GitHub
  Desktop, then choose **Repository**, then **Pull**.

### Step A: Create the Project Folder and Its GitHub Repo

GitHub Desktop creates the folder, a README, and a license in one go:

1. In GitHub Desktop, choose **File**, then **New Repository...**
2. Fill in:
   - **Name:** `<your-project>`
   - **Description:** one sentence about what it's for
   - **Local Path:** your projects folder, the one that holds
     `ai_assisted_sdlc_workflow` (click **Choose...**)
   - Tick **Initialize this repository with a README**
   - **Git Ignore:** choose **Python** (a sensible start; the starter kit
     adds its own list too)
   - **License:** choose one, for example **MIT License** (anyone may reuse
     your work, with credit), or **None** if you want to keep all rights
3. Click **Create Repository**.

You now have `projects/<your-project>/` with a `README.md`, `LICENSE`, and
`.gitignore`, ready to put on GitHub.

> **With Claude Code instead:** open a terminal in your projects folder,
> start Claude Code, and say: "Create a folder named `<your-project>`, make
> it a Git repository with a README and an MIT license, and create a private
> GitHub repo for it."

### Step B: Copy the Starter Kit Into It

1. In **Finder**, open `ai_assisted_sdlc_workflow/project-template/`.
2. Choose **Edit**, then **Select All**, then **Edit**, then **Copy**.
3. Open your new `<your-project>` folder, and choose **Edit**, then
   **Paste Items**.
4. When Finder asks about `README.md`, choose **Replace**: the starter
   kit's README describes the project's layout. Keep your `LICENSE`.

Finder doesn't show or copy hidden files whose names start with a dot, such
as the starter kit's `.gitignore`. That's fine: GitHub Desktop already made
one in Step A. To use the starter kit's fuller list as well, ask Claude Code
(below).

> **With Claude Code instead:** in your projects folder, say: "Copy
> everything in `ai_assisted_sdlc_workflow/project-template`, including
> hidden files, into `<your-project>`. Keep its LICENSE, replace its
> README.md, and add the starter kit's .gitignore lines to its .gitignore."

### Step C: Fill In the Name and Description

Open `README.md` and `CLAUDE.md` in any text editor (TextEdit works: choose
**Format**, then **Make Plain Text**), and replace `<Project Name>` and the
one-sentence description. Or ask Claude Code, in your project folder: "Fill
in the README.md and CLAUDE.md placeholders. The project is
`<your-project>`: <one sentence about it>."

You can delete this `START-HERE.md` later, once you know the steps; it's
also in the workflow repo.

### Step D: Push the Project to GitHub

1. In GitHub Desktop, your project's changes appear on the left.
2. In the **Summary** box at the bottom left, type
   `Start from the AI-assisted SDLC starter kit`, and click
   **Commit to main**.
3. Click **Publish repository** at the top. Tick **Keep this code
   private** unless you want anyone to see it, then click
   **Publish Repository**.

Your empty project is now on GitHub. From now on, whenever a step saves a
document: type a summary, click **Commit to main**, then **Push origin**.

### Step E: Connect Claude to the Project

1. **A Claude Project:** in the Claude desktop app, click **Projects**, then
   **+**. Name it `<your-project>`, add the one-sentence description, link
   your `<your-project>` folder, and click **Create Project**. Every step's
   chat lives here.
2. **File access:** choose **Menu**, then **Settings**, then
   **Extensions**. Install **Filesystem**, add your `<your-project>` folder,
   then quit and restart the app. To check, ask a chat in the Project:
   "Please list the contents of the local folder." It should list `docs/`,
   `prompts/`, and the rest.

Setup is done.

---

## Part 2: Run the Workflow, One Step at a Time

### How Every Step Works

1. **Open a new chat** in your Claude Project, named after the step (for
   example, `02-feasibility`). Steps 6 to 10 work best in **Claude Code**
   in your project folder, because they run commands and change code.
2. **Give it the step's prompt** from `prompts/`: attach the file and say
   "Please follow this prompt," or paste everything below its line.
3. **Attach what it asks for:** your tracking checklist
   (`docs/d01-01-checklist.md`), the approved documents from earlier steps,
   and **the blank templates for this step**, which are already in `docs/`
   (the prompt says which; for example, Step 2 uses the `d02-...` files).
4. **Answer its questions.** "Don't know yet" is a fine answer.
5. **Review what it produces.** Compare it with the same document in the
   [sample project](https://github.com/b0ts/ai_assisted_sdlc_workflow/tree/main/samples/BeautifulBeachParkVolunteers/docs).
   Ask for changes until you're happy.
6. **Take its hand-off note to the Tracking chat** (Step 1's chat, which
   stays open the whole project). You decide: **Go**, **Go back** (an
   earlier document must change first), **Park**, or **Abandon**.
7. **Save and push:** the filled-in document replaces the blank one in
   `docs/`, with the same name. Commit and push it in GitHub Desktop.

A blank template that still holds `[placeholders]` simply means that step
hasn't happened yet. Templates a step doesn't need (for example, a full
feasibility study for a small project) can stay blank or be deleted.

### Step 1: Tracking (the Scrum Master), First

The **Scrum Master** chat keeps the project on track: the checklist of
steps, every decision, every open issue, and what to do next. It starts
first and stays open until the end.

1. Open a chat named `01-tracking`. Attach `prompts/c01-tracking-prompt.md`
   and `docs/d01-01-checklist.md` (and `d01-02-gantt.md` and
   `d01-03-status-report.md` if the project is large), and say "Please
   follow this prompt."
2. Tell it: your project's name, one sentence about what it's for, who the
   **stakeholders** are (the people who approve each step; it can be just
   you), and any deadline.
3. It fills in `docs/d01-01-checklist.md`: the ten steps, the stakeholders,
   and a **Next Action** pointing to Step 2. Save it, commit, and push.
4. **Keep this chat.** You come back to it after every step.

### Step 2: Feasibility (the Product Manager): Brainstorm, One-Pager, Go or No-Go

The **Product Manager** chat helps you decide whether the idea is worth
building before anything else is spent on it.

1. Open a chat named `02-feasibility`. Attach
   `prompts/c02-feasibility-prompt.md`, your checklist, and the blank
   `docs/d02-01-one-pager.md` (plus `d02-02` to `d02-04` for a bigger
   project, a pitch between ideas, or an outside funder).
2. **Brainstorm:** describe your group's real problem in your own words,
   for example "Our coordinators spend hours on email chains filling
   Saturday shifts." It asks questions, compares ideas, and researches
   users, costs, and anything legal.
3. It writes the **one-pager**, `docs/d02-01-one-pager.md`: the problem,
   the users, the idea, why now, a rough cost, how you'll measure success,
   the risks, and a **go or no-go recommendation**.
4. Take its hand-off note to the **Tracking chat**. You, and any other
   stakeholders, record the decision: **Go** to Step 3, **Park** it, or
   **Abandon** it. A No-Go is a good result: it saved the cost of building
   the wrong thing.

### Steps 3 to 10

| Step | Role and chat | Prompt | It produces (in `docs/`) | Done when |
|---|---|---|---|---|
| 3. Requirements | Product Manager, `03-requirements` | `c03-requirements-prompt.md` | `d03-01-prd.md`: who the users are, and what they must be able to do (use cases) | The stakeholders approve the PRD |
| 4. Design | Software Architect, `04-design` | `c04-design-prompt.md` | `d04-01-spec.md` (and `d04-02-design-options.md`): how it will work, including Security & Compliance | The stakeholders approve the Spec |
| 5. User Experience | UI/UX Designer, `05-user-experience` | `c05-user-experience-prompt.md` | `d05-01-ui-ux.md`, `d05-02-style-guide.md`: every screen, its wording, and your organization's look | The stakeholders approve the screens |
| 6. Initial Infrastructure | DevOps Engineer, in **Claude Code** | `c06-initial-infrastructure-prompt.md` | `d06-03-cost-sign-off.md` (approved **before** anything is set up), `d06-01-infrastructure.md`, `d06-02-infrastructure-options.md`; a free local environment | Costs signed off; the local environment works |
| 7. Test Creation | SDET, in Claude Code | `c07-test-creation-prompt.md` | `d07-01-test-plan.md`, `d07-02-test-results.md`, and the tests in `tests/`, all failing because nothing is built yet | The stakeholders approve the Test Plan |
| 8. Implementation | Software Engineer, in Claude Code | `c08-01-implementation-prompt.md` | The code in `src/` until every test passes; `d08-01` to `d08-03` | See the reviews below |
| 9. Release | Release Manager | `c09-release-prompt.md` | A stakeholder demo, then `d09-01` to `d09-03`: the move to the live servers, a pilot, and go-live | The stakeholders approve the demo, then the release |
| 10. Maintenance | SRE, in Claude Code | `c10-maintenance-prompt.md` | `d10-01-maintenance-log.md`, monthly `d10-02` reports, and `d10-03` if a new phase or a sunset is due | Ongoing |

**Step 8's reviews**, one after another, each with your decision on every
finding, the fixes, and a re-check before the next:

1. **Code review, round 1:** a different company's AI, such as Codex
   (`c08-02-code-review-prompt.md`), writes `d08-04-code-review-codex.md`.
2. **Code review, round 2:** a **new** Claude Code session (same prompt,
   plus `/security-review`) writes `d08-04-code-review-claude.md`.
3. **Polishing:** you, who built it, run the app and fine-tune it with the
   AI (`c08-04-polishing-prompt.md`), recorded in
   `d08-06-polishing-log.md`; then the round 2 reviewer checks those
   changes.
4. **Hands-on review, round 3:** someone who wasn't involved uses the app
   (`c08-03-hands-on-review-prompt.md`), recorded in
   `d08-05-hands-on-review.md`.

Copy `d08-04-code-review.md` once per code reviewer, named after the tool.

**If a step says an earlier document must change** (a "go-back"), take its
request to that earlier step's chat, get the revised document approved in
the Tracking chat, then return.

---

## Checklist

- [ ] A: Project folder and GitHub repo created (README, license, .gitignore)
- [ ] B: Starter kit copied in
- [ ] C: Name and description filled in
- [ ] D: Committed and published to GitHub
- [ ] E: Claude Project created and linked; file access working
- [ ] Step 1: Tracking chat started; checklist saved
- [ ] Step 2: One-pager written; Go or No-Go recorded
- [ ] Steps 3 to 10, each with a decision recorded in the Tracking chat

**Keeping the starter kit current:** if the workflow repo changes, the
newest prompts and templates are in its `prompts/` and `templates/`
folders. Copy any you want into your project's `prompts/` and `docs/`
(a document you've already filled in keeps your content; only use a newer
template for documents not yet written).
