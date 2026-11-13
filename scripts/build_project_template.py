#!/usr/bin/env python3
"""Refresh project-template/ from this repo's prompts/ and templates/.

project-template/ is the starter folder people copy into a new project
(see project-template/START-HERE.md). Its prompts/ and docs/ folders hold
copies of this repo's step prompts (c01 to c10) and document templates
(d01-01 to d10-03). Run this script after changing any prompt or template,
so the copies never drift:

    python3 scripts/build_project_template.py

It overwrites the copied files only; START-HERE.md, README.md, CLAUDE.md,
.gitignore, and the README.md in each folder are written by hand and left
alone. Links that point elsewhere in this repo are rewritten so they still
work from inside a new project: to the GitHub copy of this repo, or, for a
template, to its copy in the project's own docs/ folder.
"""

import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
TARGET = REPO / "project-template"
GITHUB = "https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/"


def rewrite_links(text):
    """Make relative links that leave the copied folder point somewhere real."""
    # Guides, samples, and other prompts stay in this repo: link to its GitHub copy.
    text = re.sub(r"\]\(\.\./(docs|samples|prompts)/", rf"]({GITHUB}\1/", text)
    # A document template sits in the new project's own docs/ folder.
    text = re.sub(r"\]\(\.\./templates/(d\d\d-\d\d-[a-z0-9-]+\.md)\)", r"](../docs/\1)", text)
    text = text.replace("](../templates/)", "](../docs/)")
    # Anything else in templates/ (its README) stays on GitHub.
    text = re.sub(r"\]\(\.\./templates/", f"]({GITHUB}templates/", text)
    return text


def copy_all(source_dir, pattern, target_dir, kind):
    target_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    for source in sorted(source_dir.glob(pattern)):
        if source.name.startswith("c00-"):
            continue  # c00 sets up a new project; it lives in this repo, not in the kit
        text = rewrite_links(source.read_text(encoding="utf-8"))
        (target_dir / source.name).write_text(text, encoding="utf-8")
        copied.append(source.name)
    return copied


def main():
    prompts = copy_all(REPO / "prompts", "c[0-9][0-9]-*.md", TARGET / "prompts", "prompts")
    docs = copy_all(REPO / "templates", "d[0-9][0-9]-[0-9][0-9]-*.md", TARGET / "docs", "docs")
    # Remove copies whose source no longer exists (a prompt or template was renamed).
    for folder, names, pattern in ((TARGET / "prompts", prompts, "c[0-9][0-9]-*.md"),
                                   (TARGET / "docs", docs, "d[0-9][0-9]-[0-9][0-9]-*.md")):
        for stale in folder.glob(pattern):
            if stale.name not in names:
                stale.unlink()
                print(f"Removed {stale.relative_to(REPO)} (no longer in this repo)")
    print(f"Copied {len(prompts)} prompts and {len(docs)} document templates into project-template/.")


if __name__ == "__main__":
    main()
