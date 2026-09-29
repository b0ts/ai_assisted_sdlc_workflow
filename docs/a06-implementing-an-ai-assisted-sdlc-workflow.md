# Implementing an AI-Assisted SDLC Workflow

## Executive Summary

This guide walks you through setting up your computer and accounts so you can
build your own product with the AI-assisted SDLC workflow. In six short steps
you'll get a copy of this repo, create a folder for your project with a
standard layout, connect it to Claude and GitHub, and confirm that Claude can
work with your files. When you're done, you're ready to start Step 01,
Tracking.

---

## Introduction

The earlier guides explained what an AI-assisted SDLC workflow is and why it
works. This one is hands-on: it sets up everything the ten chats described in
[What Is an AI-Assisted SDLC Workflow?](a05-what-is-an-ai-assisted-sdlc-workflow.md)
will need.

Throughout this guide, `<your-project>` stands for the product you're building.
Each step also shows how it was done for **rc_park_tour**, a real project built
with this workflow. You can browse it at
[github.com/b0ts/rc_park_tour](https://github.com/b0ts/rc_park_tour) to see the
results of each step. Don't copy its name; use your own.

You'll use two Claude tools along the way:

| Tool | What it is | Used for |
|---|---|---|
| **Claude desktop app** | Claude in a window on your computer, with chats organized into Projects | Research, planning, and the step chats |
| **Claude Code** | Claude in a terminal, working directly in a folder on your computer | Creating folders and files, and working with GitHub |

A checklist of all the steps is at the [end of this guide](#checklist).

---

## Step 1: Get a local copy of this repo

If you don't already have this repo locally, open a terminal in the folder
where you keep your projects, start Claude Code, and ask it to clone the repo.

**In projects:** "Clone https://github.com/b0ts/ai_assisted_sdlc_workflow into this folder."

---

## Step 2: Create a new folder for your project

Create a folder for your product in your projects folder, next to
`ai_assisted_sdlc_workflow`.

    projects/
    ├── ai_assisted_sdlc_workflow/
    └── <your-project>/

**In rc_park_tour:** the folder is `projects/rc_park_tour`.

---

## Step 3: Copy the skeleton into your project folder

A **skeleton** is a starter set of folders and placeholder files that gives
every project the same layout before any real work begins. Think of it as the
frame of a house: nothing is finished yet, but everyone can see where the
kitchen and bedrooms will go. With a skeleton, you, Claude, and anyone reading
your project always know where to find the documents, prompts, tests, and code,
and every project built with this workflow looks the same.

This repo's `skeleton/` folder contains:

    skeleton/
    ├── README.md     describes your project (fill in the placeholders)
    ├── CLAUDE.md     tells Claude how your project is organized
    ├── .gitignore    lists files Git should ignore
    ├── docs/         documents each step produces (d-numbers)
    ├── prompts/      prompts used for each step's chat (c-numbers)
    ├── tests/        automated tests (Step 07)
    ├── src/          source code (Step 08)
    └── assets/       images, media, and data

Each folder has its own `README.md` explaining what belongs there.

To copy it, open a terminal in your projects folder, start Claude Code, and
ask it to copy the skeleton into your project folder. Asking Claude Code is
easier than copying by hand, because `.gitignore` is a hidden file that Finder
doesn't show by default.

**In projects:** "Copy everything in ai_assisted_sdlc_workflow/skeleton,
including hidden files, into `<your-project>`."

**In rc_park_tour:** rc_park_tour was set up before the skeleton existed, so its
layout is different. It will be brought in line as the example develops.

---

## Step 4: Create a Claude Project linked to your folder

In the Claude desktop app, create a new Project for your product and link it to
the `<your-project>` folder you created in Step 2. This associates the folder
with the Project (Step 6 gives Claude access to its files), and keeps your
research and planning conversations together where you can pick them up later.

1. Click **Projects** in the left menu, then click the **+** button to add a new Project.
2. Enter your project's name and a short description of it in the details field.
3. Click the folder button and select your `<your-project>` folder.
4. Click **Create Project**.

**In rc_park_tour:**

- Name: `rc_park_tour`
- Details: "A printed and interactive tour of RC Park in San Jose, CA"
- Folder: `projects/rc_park_tour`

---

## Step 5: Create a GitHub repo for your project

Open a terminal, navigate to your `<your-project>` folder, start Claude Code,
and ask it to create a new repo for the folder in your GitHub account.

> **Note:** If you don't already have a GitHub account, create one at
> [github.com](https://github.com). Claude Code uses the GitHub CLI (`gh`) to
> work with your account, so install it from
> [cli.github.com](https://cli.github.com), then sign in by running
> `gh auth login` in your terminal and following the prompts. You only need to
> do this once; you can also ask Claude Code to walk you through it.

**Public or private:** Make the repo **private** if you don't want to share
your project, or **public** if it's fine for anyone to see your work. You can
change this later in the repo's settings on GitHub.

**Fill in the skeleton:** In the same request, give Claude Code a one-sentence
description of your project and ask it to fill in the placeholders in
`README.md` and `CLAUDE.md`, add a `LICENSE` if you want one, and then commit
and push everything. Your new repo then starts with a clear description
instead of blank placeholders.

**In rc_park_tour:** "Create a new public GitHub repo named rc_park_tour for
this folder. Add a README.md describing the project as a printed and
interactive tour of RC Park in San Jose, CA, then commit and push it." Claude
Code also added a `LICENSE` file. The result is
[github.com/b0ts/rc_park_tour](https://github.com/b0ts/rc_park_tour).

---

## Step 6: Give Claude desktop access to your folder

Turn on file access so Claude in the desktop app can read and write the files
in your `<your-project>` folder. This uses the Filesystem extension.

1. Open **Menu | Settings | Extensions**.
2. Browse for **Filesystem** and install it.
3. Add a directory to give it access to your `<your-project>` folder.
4. Quit the Claude desktop app completely and restart it.
5. To check that it worked, start a chat in your Project and ask:
   "Please list the contents of the local folder." Claude should reply with
   the files and folders in `<your-project>`, including the skeleton folders
   from Step 3.

**In rc_park_tour:** the directory added was `~/projects/rc_park_tour`.

---

## What Comes Next

Your system is set up. The next move is to start the first of the ten chats:
[Step 1: Tracking](b01-tracking.md), which initializes tracking for your
project and stays open while the other steps run.

---

## Checklist

Use this to track your progress through the setup steps.

- [ ] Step 1: Get a local copy of this repo
- [ ] Step 2: Create a folder for your project
- [ ] Step 3: Copy the skeleton into your project folder
- [ ] Step 4: Create a Claude Project linked to your folder
- [ ] Step 5: Create a GitHub repo for your project
- [ ] Step 6: Give Claude desktop access to your folder

---

**Learn more:**

- [What Is an AI-Assisted SDLC Workflow?](a05-what-is-an-ai-assisted-sdlc-workflow.md):
  the ten chats this setup prepares for
- [Step 1: Tracking](b01-tracking.md): the first chat you'll start
- [GitHub CLI manual](https://cli.github.com/manual/): more on the `gh`
  command used in Step 5
