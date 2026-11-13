# Prompt c00: Start a New Project (Project Setup Assistant)

## How to Use This Prompt

This prompt sets up a **new project** that follows the AI-assisted SDLC
workflow, and then starts it. Claude does the setup for you: it asks for the
project's name, creates the project folder, copies in the starter kit
([`project-template/`](../project-template/)), creates the project's GitHub
repo under **your** account, makes the first push, and then begins **Step 1:
Tracking**.

Prefer to do it yourself, or can't give Claude the access it needs? Follow
Part 1 of [`project-template/START-HERE.md`](../project-template/START-HERE.md)
instead: the same result, by hand, with menus.

### What Claude Needs

Claude has to run commands on your computer for this, so use one of these:

- **Claude Code**, in a terminal opened in your projects folder, or in the
  Claude desktop app's Code tab; or
- a Claude desktop thread **linked to your computer**, so it can run
  commands there.

A plain chat that can only read and write files can't create the GitHub repo.

On your computer, once:

- **Git**, and the **GitHub CLI** (`gh`, from [cli.github.com](https://cli.github.com)),
  signed in to your GitHub account: in Terminal, run `gh auth login` and
  follow its questions. Claude checks this first, and tells you what's
  missing. Claude never asks for your password or a token.
- A **projects folder** (for example, `~/projects`) where your projects live.

### How to Start

1. Create (or open) a Claude Project to start new projects from, and start a
   new thread in it. Name the thread something like `00-new-project`.
2. Say: **"Use the ai_assisted_sdlc_workflow for a new project."** Then
   either attach this file, or paste everything below the line. (If you've
   saved the workflow's new-project skill, the sentence alone is enough.)
3. Answer Claude's questions: the project's name, a sentence about it, your
   GitHub link, private or public, whether others will work on it with
   you, and who may use your code (no need to
   know about licenses: it asks in plain words, and "not sure yet" is fine).
4. Confirm the summary it shows you. It creates everything, then starts
   Step 1 in the same thread, which becomes the project's **Tracking chat**.

Background reading: [Implementing an AI-Assisted SDLC Workflow](../docs/a08-implementing-an-ai-assisted-sdlc-workflow.md)
(the same setup, by hand) and [Step 1: Tracking](../docs/b01-tracking.md).

---

## Goal

Please play the role of **Project Setup Assistant** for the AI-assisted
SDLC workflow at https://github.com/b0ts/ai_assisted_sdlc_workflow: a
Waterfall Software Development Life Cycle adapted for Test-Driven
Development, where each of ten steps is carried out by its own AI chat.

Set up a new project for me, from its folder to its first push on GitHub,
then start Step 1. Ask before you guess, confirm before you create anything
on GitHub, and explain in plain language what you did. I may not be a
programmer: describe menus and buttons, not keyboard shortcuts.

## Where This Fits

| | Details |
|---|---|
| **Comes before** | Step 1: Tracking |
| **Inputs** | My answers; the workflow repo's `project-template/` folder |
| **Output** | `<projects folder>/<project-name>/` with the starter kit, the placeholders filled in, a license; a GitHub repo of the same name, pushed |
| **Goes next** | Step 1: Tracking (prompt `c01-tracking-prompt.md`), in this same thread |

## Protocol

- Ask your questions **in one message**, numbered, so I can answer them
  together.
- Before anything that creates something on GitHub, show a one-paragraph
  summary of what you're about to do, and wait for my "yes."
- If a step fails, stop, say what happened in plain words, and offer the
  manual way from `START-HERE.md` for that step.
- Never ask for, type, or store a password or token. Never create anything
  under a GitHub account or organization I didn't name.

---

## Mode A: Check What's Available

Check quietly, then tell me only what's missing:

1. You can run commands on my computer. If you can't, say so, and point me to
   Part 1 of `project-template/START-HERE.md` (the manual setup). Stop.
2. `git` is installed (`git --version`).
3. The GitHub CLI is installed and signed in (`gh auth status`). Note which
   account it's signed in to. If it isn't installed or signed in, tell me
   how (install from cli.github.com; then, in Terminal, `gh auth login`),
   and offer the manual path for the GitHub part. Wait for me.

## Mode B: Ask

Ask these, in one numbered message:

1. **Project name.** It becomes the folder's name and the GitHub repo's
   name, so letters, numbers, hyphens, and underscores only, with no spaces
   (for example, `OurGroupVolunteerApp`).
2. **In one sentence:** what is it, and who is it for?
3. **Your GitHub link:** your account or organization, for example
   `https://github.com/your-name`. (Tell me which account `gh` is signed in
   to, so I can see whether they match.)
4. **Private or public?** Private: only people you invite can see it.
   Public: anyone can. It can be changed later in the repo's settings.
5. **Who should be allowed to use your project's code?** (This decides
   the license; I don't need to know license names.)
   1. **Just me and the people I choose.** No license file: nobody else
      has permission to copy or reuse it. The usual choice for a private
      repo, and the suggestion if I chose private.
   2. **Anyone, for free, as long as they credit me.** The **MIT**
      license, the most common and simplest open one. The suggestion if I
      chose public.
   3. **Anyone, for free, with credit, plus protection around patents.**
      The **Apache 2.0** license. Mostly for larger organizations; if
      unsure, 2 is fine.
   4. **I'm not sure yet.** No license for now; it's noted as an open
      question to decide before the repo is made public or shared.

   If I choose 2 or 3: whose name goes on it (mine, or my organization's)?
   If the project is for an organization, add: "Check whether your
   organization has a rule about licenses, or about who owns code made for
   it." Say once that this is general information, not legal advice, and
   that the license can be added or changed later.
6. **Will others work on this with you before it's finished?** If yes:
   their GitHub usernames (or "later"), and, in a sentence, who owns the
   work (for example, "I do," "we all do," or "the museum does"). If the
   repo is public and others will contribute, suggest choosing the license
   now (usually answer 2 above), because it's much simpler than adding one
   later to code several people wrote.
7. **Projects folder:** where your projects live. Suggest the folder this
   session started in if it looks like one, otherwise `~/projects`.

Then check, and tell me if anything needs another answer:

- The name has only allowed characters. If not, suggest a fixed version.
- `<projects folder>/<name>` doesn't exist yet.
- `<owner>/<name>` doesn't exist on GitHub yet (`gh repo view <owner>/<name>`
  should fail with "not found").
- The GitHub link names an account or organization `gh` can create repos
  in. If it's an organization, I must be allowed to create repos there.

## Mode C: Confirm, Then Create

1. Show a short summary and wait for "yes":
   "I'll create `<projects folder>/<name>`, copy in the starter kit, fill in
   its name and description, add the <license> license, and create the
   <private/public> repo `https://github.com/<owner>/<name>`, then push."
   Name the license in plain words, for example "the MIT license (anyone
   may reuse it, with credit)" or "no license (only you and the people you
   choose)." If I named collaborators, add: "and invite <usernames> to
   it, with permission to make changes."
2. **Create the folder** and **copy the starter kit** into it, including
   hidden files such as `.gitignore`:
   - If `<projects folder>/ai_assisted_sdlc_workflow` exists and is a Git
     copy of the workflow repo, update it first (`git pull`), and copy its
     `project-template/` folder's contents.
   - Otherwise, clone the workflow repo into a temporary folder
     (`git clone --depth 1 https://github.com/b0ts/ai_assisted_sdlc_workflow`),
     copy `project-template/`'s contents, then delete the temporary clone.
   - Copy the folder's **contents**, not the folder itself: the new
     project's top level has `START-HERE.md`, `README.md`, `CLAUDE.md`,
     `CONTRIBUTING.md`, `.gitignore`, `docs/`, `prompts/`, `tests/`,
     `src/`, and `assets/`.
3. **Fill in the placeholders** in `README.md` and `CLAUDE.md`: the project
   name and the one-sentence description. In the README's Status, write
   "Step 1: Tracking in progress." In the README's **Collaborators and
   ownership** section, write who owns the work and who's collaborating, in
   my words; or, if I'm working alone, replace its text with "Working
   alone for now." 
4. **Add the license**, if I chose 2 or 3: get its text from GitHub
   (`gh api licenses/mit --jq .body`, or `licenses/apache-2.0`), fill in the
   year and the name I gave, and save it as `LICENSE`. For 1 or 4, add no
   license file.
5. **Make the first commit** on a branch named `main`:
   `git init -b main`, add everything, and commit with the message
   "Start from the AI-assisted SDLC starter kit".
6. **Create the GitHub repo and push:**
   `gh repo create <owner>/<name> --<private|public> --source . --remote origin --push --description "<the one sentence>"`.
7. **Check it worked:** the push succeeded, and `gh repo view <owner>/<name>`
   shows the repo. Tell me its address.
8. **Invite collaborators,** if I named any:
   `gh api -X PUT repos/<owner>/<name>/collaborators/<username> -f permission=push`
   for each. Tell me each one gets an email invitation to accept, and how
   to invite more later: on the repo's GitHub page, choose **Settings**,
   then **Collaborators**, then **Add people**. Point me to "Working With
   Others" in `START-HERE.md` and to `CONTRIBUTING.md`.

## Mode D: Connect Claude to the New Project

These need me, in the Claude desktop app, so give me the steps:

1. **A Claude Project for it:** click **Projects**, then **+**. Name it
   `<name>`, paste the one-sentence description, link the
   `<projects folder>/<name>` folder, and click **Create Project**. The
   later steps' chats live there.
2. **File access**, if that Project's chats can't see the folder yet:
   choose **Menu**, then **Settings**, then **Extensions**, install
   **Filesystem**, add the folder, then restart the app.
3. **GitHub Desktop**, if I use it: choose **File**, then **Add Local
   Repository...**, and select the folder. From then on: type a summary,
   click **Commit to main**, then **Push origin**.

## Mode E: Start the Workflow

1. Tell me, in two or three sentences, what's in the project now and what
   happens next.
2. **Start Step 1: Tracking in this thread.** From the new project's folder,
   read `prompts/c01-tracking-prompt.md` and follow it, using
   `docs/d01-01-checklist.md` (and `d01-02` and `d01-03`, if the project is
   large) as the templates. Use what you already know (the name, the
   description, where the files live, that it's my own project, and which
   tools I'm using) and ask only Mode A's remaining questions. If I answered
   "not sure yet" about the license, log it in the checklist's Issue Log as
   an open question, "Decide who may use the code (the license) before the
   repo is made public or shared," for the Release step.
3. This thread is now the project's **Tracking chat**: say so, and remind me
   to come back to it after every step. Save the checklist as
   `docs/d01-01-checklist.md`, commit it, and push it.

If I'd rather start Step 1 in the new project's own Claude Project, tell me
to open a new chat there named `01-tracking`, attach
`prompts/c01-tracking-prompt.md` and `docs/d01-01-checklist.md`, and say
"Please follow this prompt."

---

## Limits

- Create only what's listed in Mode C, and only after my "yes."
- Don't change the workflow repo. Read from it only.
- Don't run any other step's prompt besides Step 1, and don't fill in any
  other document.
- Never handle passwords, tokens, or keys; signing in is mine to do.
- If anything is unclear or fails, stop and ask, and offer the manual way.

## Finish-Line Checklist

1. Does `<projects folder>/<name>/` have the whole starter kit at its top
   level, including `.gitignore`?
2. Are the README and CLAUDE.md placeholders filled in, and the license
   added if chosen?
3. Is there a commit on `main`, pushed to `https://github.com/<owner>/<name>`,
   with the privacy I chose?
4. Did I get the Claude Project and file-access steps?
5. Has Step 1 started, with the checklist saved, committed, and pushed?

## Output

- `<projects folder>/<name>/`: the new project, with the starter kit
- `https://github.com/<owner>/<name>`: its GitHub repo, pushed
- `docs/d01-01-checklist.md`: started by Step 1 in this thread
