# The Multi-AI-Agent Paradigm

## Executive Summary

Most AI chatbots answer as a single, friendly voice, and that voice tends to
tell you what you want to hear. You get better results by having several AI
chats each play a **different role** with a different point of view, and
then having one more chat act as the **leader** who weighs them all and
decides. This idea of many specialized AI "agents" guided by one
coordinator, with a human in charge, is the foundation of everything else
in this repo.

---

## One Person, Many Facets

One way to picture a well-developed human mind is as a small crystal with
many facets. Each facet holds a different **persona**, a version of
ourselves suited to a particular situation. Like changing channels on a TV
or shaking a Magic 8 Ball, a different facet comes to the surface depending
on what the moment calls for. The same person might be any of these:

| Kind of role | Examples |
|---|---|
| Home and family | parent, child, homemaker, handyman |
| Learning | student, teacher, seeker |
| Work | accountant, programmer, electrician, auto mechanic |
| Creative | artist, musician, actor or actress |
| Style and interests | hiker, Goth, preppy, spiritual person |
| In a group | leader, follower |

At a certain stage of growth, many of these facets come together under a
central persona, a kind of **director** sitting at the center of the
crystal. The facets don't disappear. Each one still has its say, but the
director listens to all of them and decides, so they work together for the
common good instead of pulling in different directions.

### The Captain's Ready Room

A good picture of this is the ready room in *Star Trek: The Next
Generation*. Before a hard decision, Captain Jean-Luc Picard often gathers
his senior officers. Each has a very different personality and sees the
problem differently: the security chief urges caution, the engineer talks
about what's technically possible, the counselor reads people's feelings.
They argue. Then the captain makes a decision, and the crew puts aside their
differences and works as one team toward a shared goal.

That is exactly the pattern we want to copy with AI.

---

## The Problem With a Single AI Persona

Most chatbots, out of the box, use one helpful persona that tries to keep
you happy. That can cause two problems:

- **Sycophancy** means the AI tells you what you want to hear instead of
  what is accurate or deserved. Ask "Is my plan good?" and you may get
  praise, plus a false sense of security about something that has real
  flaws.
- **Hallucination** means the AI states things that aren't true as if they
  were facts. While trying to support your point, it may even invent
  sources or references that don't exist.

A single persona trying to be agreeable has nobody to push back on it.

## The Fix: Many Personas and One Captain

Instead of one yes-man, we create **several AI personas with very different
viewpoints**, plus one **integrator**: the captain of the ship, the leader of
the personas. The integrator weighs all the input and makes a
recommendation. This doesn't remove every mistake, and a human should still
check the results, but it greatly reduces the "tell me I'm right" problem.

### Example: The Five Persona Council

The [Five Persona Council](../samples/FivePersonaCouncil/README.md) in this
repo's `samples` folder puts this idea into a ready-to-use tool, called a
**skill**. It's adapted from similar tools shared openly on the web; see
that folder's README for the credits.

The council has five AI advisors, each playing a different role:

| Advisor | Focus |
|---|---|
| The Contrarian | What will fail |
| The First Principles Thinker | Which of your assumptions are wrong |
| The Expansionist | The upside you're missing |
| The Outsider | The naive questions experts stopped asking |
| The Executor | What to actually do this week |

A sixth persona, the **Chairman**, weighs all five viewpoints and gives you
three things: the decision to make, the biggest risk to watch, and the first
step to take.

Once the skill is added to your AI, whenever you face a decision you can say
something like *"I wonder what the council has to say about this?"* Your AI
will run the council and show you five very different views, pulled
together into one verdict. That gives far better results than asking the
same question in a regular chat.

---

## From a Council to a Whole Organization

The same idea works for any organization with clearly defined **job titles,
roles, responsibilities, inputs, outputs, tasks, and deliverables**. Each
job title becomes an AI persona, and each persona does its own part of the
work.

### Task Chaining

The personas can also work in sequence, which is called **task chaining**.
The document produced by one AI chat with one persona becomes the input for
the next chat, which has a different persona and skill set. Each step uses a
different persona and creates a different document.

A **controller chat** guides and coordinates every step and every document
along the way, and that controller is itself steered by **you**, the human.

```text
            You (the human)
                  │ steer
                  ▼
           Controller chat ── tracks and approves every step
                  │
  Chat A ──doc──▶ Chat B ──doc──▶ Chat C ──doc──▶ ...
 (persona 1)     (persona 2)     (persona 3)
```

---

## How This Repo Uses the Paradigm

This multi-agent paradigm is the foundation for everything else in this
repo. Here we apply it to the **Software Development Lifecycle (SDLC)**, the
step-by-step process for turning an idea into working software:

- **The personas are real job titles**, such as Product Manager, Software
  Architect, and Software Engineer.
- **The documents are the ones traditionally used** in a *Waterfall* SDLC, where
  each step is finished and handed down the chain before the next begins.
- **The controller chat is the Scrum Master**, who tracks every step and
  makes sure each document is approved before the next chat starts.

There is one important difference from traditional Waterfall: we use
**Test-Driven Development (TDD)**. That means the tests that prove the
software works are **written before** the software is built, not after.
The next guides explain what all of this means, one piece at a time.

---

**Learn more:**

- [Five Persona Council sample](../samples/FivePersonaCouncil/README.md):
  the council skill, a prompt to build it yourself, and credits
- [What Is an AI-Assisted SDLC Workflow?](a07-what-is-an-ai-assisted-sdlc-workflow.md):
  how the ten chats in this repo are chained together
- [LLM Council (Andrej Karpathy, GitHub)](https://github.com/karpathy/llm-council):
  the original idea of having several AIs review each other
- [Towards understanding sycophancy in language models (Anthropic)](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models):
  research on why AI tends to tell people what they want to hear
- [Hallucination (artificial intelligence) (Wikipedia)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)):
  a general introduction to AI hallucinations

**Next:** [What Is a Software Development Lifecycle Workflow?](a03-what-is-an-sdlc-workflow.md)
explains the SDLC and the TDD workflow this repo uses.
