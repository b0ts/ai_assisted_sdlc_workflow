# Five Persona Council

This folder holds a sample **skill** called `five-persona-council`. A skill is a short set of written instructions that teaches Claude how to do one kind of task the same way every time. Once you install this one, Claude can turn any decision you're stuck on into a short debate between five advisors, followed by a final verdict.

## Why use a council instead of just asking?

If you ask an AI "Is my plan good?", it often tells you the plan is great. That feels nice, but it can give you a false sense of security. This habit of telling people what they want to hear is called **sycophancy**.

A council fixes this by making Claude look at your decision from five different angles. The advisors are told to stay in character and are allowed to disagree with each other and with you. Then a sixth voice, the Chairman, weighs everything and gives you a clear answer.

| Advisor | What they look for | How they sound |
|---|---|---|
| The Contrarian | Everything that could go wrong and what breaks first | Blunt and grim |
| The First Principles Thinker | Hidden assumptions, rebuilding the problem from the basics | Probing and slow |
| The Expansionist | The upside you're missing and bigger opportunities | Energetic |
| The Outsider | The obvious questions experts stopped asking | Casual and naive |
| The Executor | What to actually do this week | Terse and practical |

**The Chairman's verdict** always ends with exactly three things: the single decision to make, the biggest risk to watch, and the very first step to take.

## What's in this folder

- `README.md` is this explanation.
- `SKILL.md` is the skill itself. The section between the `---` lines at the top gives the skill's name and tells Claude when to use it. The rest is the instructions Claude follows.
- `create-council-skill-prompt.md` is a prompt you can give Claude so it builds the skill for you, instead of installing the ready-made `SKILL.md`.

## Two ways to get the skill

- **Use the ready-made file.** Skip ahead to **How to install it** and use the `SKILL.md` in this folder. This is the quickest way.
- **Have Claude build it for you.** This is how the skill was originally made, and it teaches you how skills are created. See the next section.

## Have Claude build the skill for you

1. Open `create-council-skill-prompt.md` in this folder.
2. Pick a version. The **full version** is meant to be copied and pasted, and gives a result very close to the sample. The **short version** is short enough to type in yourself, and Claude fills in the rest.
3. Start a new chat in Claude. Paste or type the prompt and send it.
4. Read what Claude wrote. If you want changes, ask for them in plain words, such as "make the Executor focus on today instead of this week."
5. Download the `SKILL.md` file Claude gives you. If Claude offers to add the skill for you directly, you can accept that instead and skip the install steps below.
6. Follow **How to install it** below, using your new file.

## How to install it

1. Make a new folder on your computer called `five-persona-council`.
2. Copy `SKILL.md` into that folder.
3. Compress the folder into a zip file. On a Mac, right-click (or Control-click) the folder in Finder and choose **Compress**. On Windows, right-click the folder and choose **Send to**, then **Compressed (zipped) folder**.
4. In Claude, open **Settings** and find the **Skills** section. Upload the zip file there and make sure the skill is turned on. Menu names can change over time, so if you can't find it, search for "skills" at support.claude.com.

> **Already have a skill called `council`?** This sample is deliberately named `five-persona-council` so it won't clash with a built-in council skill. If both are turned on, Claude may pick either one when you say "run the council." Turn one of them off if you want predictable results.

## How to use it

Start a chat and type `/five-persona-council`, or just say "run the council," followed by a real decision you're facing. The council works best on a concrete choice with at least two options. For example:

> /five-persona-council Should our volunteer group build its own sign-up app, or use a free sign-up website?

If you don't give it a clear choice, Claude will ask you for one before the advisors start. It won't run on vague topics like "help me think about my career," because the advisors need something specific to argue about.

After the verdict, you can ask follow-up questions. By default the Chairman answers directly. If you want all five advisors to weigh in again, ask Claude to re-run the council.

## How this connects to the rest of the repo

The council is a small example of a big idea used throughout this repo: you get better results from AI when you give it **separate roles** instead of asking one general question. The full workflow applies the same idea to building software. Each step of the process gets its own chat playing a real job role, such as Product Manager, Tester or DevOps Engineer. You can see that in action in the `BeautifulBeachParkVolunteers` sample.

## Credits

This sample was written from scratch by giving Claude a prompt, but the idea behind it comes from others:

- **Andrej Karpathy** created the original [LLM Council](https://github.com/karpathy/llm-council). His version sends one question to several different AI models, has them review each other's answers, and has a "Chairman" model write the final response.
- **Ole Lehmann** ([@itsolelehmann](https://x.com/itsolelehmann) on X) turned that idea into a Claude skill. He used five "thinking styles" inside a single Claude chat instead of separate AI models, which is where the Contrarian, First Principles Thinker, Expansionist, Outsider and Executor come from.
- **aiwithremy** hosts Ole Lehmann's skill on GitHub at [aiwithremy/claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council).

This sample is a simplified version. Ole Lehmann's skill also has the advisors anonymously review each other's answers before the Chairman decides. This sample skips that step and has the Chairman end with exactly three things: the decision, the risk and the first step.
