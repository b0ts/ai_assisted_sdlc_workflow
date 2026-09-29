# Prompt Engineering: Choosing the Right Kind of Prompt

## Executive Summary

A **prompt** is the message you type (or speak) to an AI to tell it what you
want. It can be one short sentence or several pages of instructions. The AI
has only your prompt to go on, so the quality of what you get back depends
heavily on the quality of what you put in.

In [Understanding AI](a03-understanding-ai.md), we compared AI to a very smart
teenager. A **vague prompt** is like asking *"Did you clean your room?"* You
get a quick, confident answer that probably isn't what you meant. A
**well-defined prompt** is like the parent who sets the roles, gives a clear
goal and directions, shows an example, and then inspects the result. The
second approach takes a little more effort up front and saves a lot of
effort later.

This document describes four kinds of prompts, from quickest to most
thorough, and explains how to decide which one to use.

---

## The Four Types of Prompts

| Type | What it looks like | Result | Effort |
|---|---|---|---|
| 1. Vague | One loose sentence | "AI slop": generic, padded, often off target | Very low |
| 2. Informal | A conversational paragraph covering role, inputs, outputs, and how you'll check the result | Good, useful results | Low |
| 3. Formal | A written document with labeled sections, saved as a prompt file | Repeatable results that are easy to share | Medium |
| 4. Test-Driven (TDD) | A formal prompt plus an **evaluator** that grades every result | The best and most consistent results | High |

### 1. The Vague Prompt

> *"Write something about software development."*

The AI will happily produce a page or two, but it has to guess who the reader
is, how long it should be, what to include, and what "done" looks like. The
result is what people call **AI slop**: text that sounds polished but is
generic, wordy, and not quite what you needed. Vague prompts are fine for
quick curiosity questions, but not for work you plan to use.

### 2. The Informal Prompt

An informal prompt is written the way you'd explain a task to a helpful
coworker. It covers the key parts from
[Understanding AI](a03-understanding-ai.md): the **role** the AI should play,
the **deliverable** you want, the **inputs** to work from, what the **output**
should contain, and how you'll **test** it. It doesn't need to be tidy or
perfectly worded.

See [example-01-roles-and-deliverables.md](../prompts/example-01-roles-and-deliverables.md)
for a real informal prompt. It produced a good first draft of
[Steps, Roles, and Deliverables](a02-steps-roles-and-deliverables.md) in one
try.

### 3. The Formal Prompt

A formal prompt is the same request, organized into clearly labeled sections
and saved in its own file (for example, `example-02-roles-and-deliverables.md`). Because it's written
down, anyone can reuse it, share it, or improve it, and the AI can read it
directly from the file instead of having it typed in each time. A formal
prompt usually includes these sections:

- **Goal:** the role, the deliverable, the audience, and why the document exists
- **Inputs:** the files or information to work from
- **Document Structure:** the sections to include, in order
- **Writing Style:** tone, length, and how to explain terms
- **Limits:** what the AI should *not* do
- **Finish-Line Checklist:** what to confirm before saving
- **Output:** where to save the result and what to report back

See [example-02-roles-and-deliverables.md](../prompts/example-02-roles-and-deliverables.md)
for the formal version of the example-01 prompt.

### 4. The Test-Driven (TDD) Prompt

This applies the same idea as the
[Test-Driven Development workflow](a01-what-is-an-sdlc-workflow.md) to prompts
themselves. Before relying on a prompt, you build an **evaluator**: a set of
checks, often run by a second AI, that grades each result against a clear
answer key. You then run the prompt, see which checks fail, improve the
prompt, and repeat until the results pass consistently.

This produces the best results, but it has a high cost: building a good
evaluator and working through the rounds of improvement takes real time. It
pays off for prompts that will be used many times, or where mistakes are
expensive.

**Note:** Building evaluators is an advanced subject that isn't covered in
this document. To learn more, see Anthropic's guide to
[defining success criteria and building evaluations](https://docs.claude.com/en/docs/test-and-evaluate/develop-tests)
and the free
[Prompt Evaluations course](https://github.com/anthropics/courses/tree/master/prompt_evaluations)
in Anthropic's training materials.

---

## Why the Human Still Matters

Part of the value of keeping a person involved is **judgment**. AI can write
any of these four kinds of prompts, but a person decides which kind the task
deserves. A quick question needs only a vague prompt. A one-time document
does well with an informal one. A prompt you'll reuse or hand to others
deserves a formal version. Only the most important, repeated work justifies
the cost of an evaluator.

When you do use an evaluator, a person also decides what is **good enough**.
No set of checks is ever perfect, and at some point more rounds of
improvement cost more than they're worth. Deciding where that point is
remains a human call.

---

## Add a Protocol Statement

A **protocol statement** is a short instruction about *how the conversation
should go*, rather than about the work itself. It helps a great deal with
long prompts, and especially when you **speak** your prompt using dictation.
When you talk, you naturally pause to think, and the AI may take a pause as
the end of your request and start working before you've finished.

A simple protocol statement fixes this:

> *"I'm going to give you a long prompt over several messages. Please wait
> until I say 'I am done' before creating the document."*

This lets you give instructions a piece at a time, correct yourself along the
way, and add points as you think of them. This document was created that way.

---

## How This Guide Was Written: An Informal Workflow in Practice

The informal approach is the one we use most often. For example, the first
draft of [Steps, Roles, and Deliverables](a02-steps-roles-and-deliverables.md)
started with a prompt like this:

1. Please play the role of an SDLC educator. *(role)*
2. Create a one-to-two-page markdown file called
   03-steps-roles-and-deliverables.md (since renamed
   a02-steps-roles-and-deliverables.md). *(deliverable and output)*
3. Target it to a person with no experience with SDLC or workflows.
   *(audience)*
4. Please use 02-what-is-an-sdlc-workflow.md (now
   a01-what-is-an-sdlc-workflow.md) as input. *(input)*
5. This was followed by a lot of informal chat describing what the document
   should contain.
6. No example was needed, because the AI picks up the style and format from
   the input file.

Next, the AI saved the first draft locally. We opened it in
**Visual Studio Code**, a free program for editing code and documents, and
went back and forth with the AI to fix misspellings, spell out
**TLAs** (three-letter acronyms), and improve the wording until the document
was ready.

Once the document was finished, we turned to the prompt itself. First, we
asked the AI how the original prompt could be improved, without creating a
prompt file yet. We reviewed its suggestions and kept the ones we liked.
Then we saved two prompt files: the original informal prompt
(example-01) and a more formal, repeatable version (example-02).

**Try it yourself:** ask Claude to read either prompt file, or paste one into
a chat, along with doc a01. (The prompts were written before the docs were
renumbered and before Tracking became step 1, so the result will list nine
steps rather than ten.) It should produce a document very similar to
[Steps, Roles, and Deliverables](a02-steps-roles-and-deliverables.md).

---

## Why We Keep This Short

This overview is meant to help you **understand** prompts, not to make you
an expert prompt writer. This case study provides a set of predefined prompts
for each step of the workflow, which you can use as-is or adapt when creating
your own projects with this methodology. Knowing how and why those prompts
work will help you use them well and adjust them when your project needs
something different.

---

**Learn more:**

- [Prompt engineering overview (Anthropic)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview):
  the AI maker's own guide to writing good prompts
- [Anthropic courses](https://github.com/anthropics/courses): free, hands-on
  tutorials on prompting and prompt evaluation
- [RC Park Tour case study](rc-park-tour-ai-sdlc-case-study.md): the actual
  prompts used for each role in a real project
