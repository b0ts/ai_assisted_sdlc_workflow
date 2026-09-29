# Understanding AI: How to Get Good Work From It

## Executive Summary

AI can write documents, plans, and even working software in minutes. But it
does its best work only when **you** tell it clearly who it should be, what
you want, what to work from, and how you'll check the result. Giving AI those
instructions is called **prompt engineering**, and it's the skill that makes
the workflow in
[What Is a Software Development Lifecycle Workflow?](a01-what-is-an-sdlc-workflow.md)
possible.

---

## An Everyday Comparison: The Very Smart Teenager

One helpful way to think about AI is as an **extremely smart teenager**.
Unless you give it very specific guidance, it will often take the easy way
out and do as little as possible, all while talking a mile a minute, so it's
hard to get a word in edgewise.

Ask a teenager something vague, like *"Did you clean your room?"* and they
may honestly believe that walking through it in their socks counts as
cleaning. Press them on it, and you'll get a rapid stream of stories about
everything *except* the room, until you're worn out and leave them alone with
their phone.

So parents learn to steer:

1. **Set the roles.** "I'm the adult here. You live under my roof, so you
   help keep our home clean and orderly."
2. **Give a clear goal.** "Your room should look like mine does."
3. **Give detailed directions.** "Make your bed, put away your clothes, and
   vacuum the floor."
4. **Show an example.** "Come look at my room. That's what 'done' means."
5. **Trust, but verify.** When they say it's done, go inspect.
6. **Steer and redo.** If something is missed, have them redo that part, not
   the whole job.

AI works the same way. The more clearly you set the role, goal, directions,
and finish line, the better the result, and the less time you spend sorting
through confident-sounding chatter.

---

## Two Things Worth Knowing About AI

**1. AI is excellent at creating documents.** AI learned by reading an
enormous library of written material: books, articles, manuals, reports, and
code. It has seen countless requirements documents, test plans, and design
specs, so when you ask it to *produce a document* in a familiar shape, it
does very well. Open-ended questions ("What should my app do?") tend to get
long, wandering answers. A request for a specific document ("Write a
one-page project summary with a go/no-go recommendation") gets something you
can review and use.

**2. AI is a smart assistant, not a boss or an oracle.** Think of it as a
capable assistant you hand tasks to. It works fast, never gets tired, and
knows a little about almost everything. But it can also be **confidently
wrong**, and it won't always tell you when it's guessing. You stay in charge:
you assign the work, and you decide whether it's good enough.

---

## The Six Parts of a Good Prompt

A **prompt** is the instruction you give the AI. A good prompt has up to six
parts:

| Part | What it means | Teenager version |
|---|---|---|
| 1. Role | Tell the AI who to be. | "You're my helper today." |
| 2. Goal | Say what finished looks like, ideally a document. | "A clean room." |
| 3. Inputs | Give it what to work from: documents, web pages, or text you type or dictate. | "Here's the list on the fridge." |
| 4. Directions | Explain the steps, one by one if needed. | "Bed, clothes, vacuum." |
| 5. Examples | Show what good work looks like. | "Like my room." |
| 6. Test and verify | Check the result, then ask for fixes. | Inspect the room. |

---

## Key Takeaways

- Treat AI like a very smart teenager: capable, fast, and in need of clear
  direction.
- Ask for **documents**, not just answers.
- Every prompt should cover **role, goal, inputs, directions, examples,** and
  **how you'll check the result.**
- Always **verify**, and ask for fixes to the specific parts that fall short.

---

**Learn more:**

- [Prompt engineering overview (Anthropic)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview):
  the AI maker's own guide to writing good prompts
- [RC Park Tour case study](rc-park-tour-ai-sdlc-case-study.md): the actual
  prompts used for each role in a real project
