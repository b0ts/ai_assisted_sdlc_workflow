# Prompt: Have Claude Build the Five Persona Council Skill

Use this prompt to have Claude write the `five-persona-council` skill for you, instead of installing the ready-made `SKILL.md` in this folder. Building it yourself is a good way to see how skills are made. You can also change the advisors to fit your own needs.

There are two versions. Pick one.

- **Full version:** Copy and paste it as-is. It gives Claude every detail, so the result will closely match the `SKILL.md` in this folder.
- **Short version:** Short enough to type yourself. Claude will fill in the details on its own, so your result may differ a little from the sample. That's fine.

---

## Full version (copy and paste)

```text
Please create a Claude skill for me and give me the finished SKILL.md file.

Skill name: five-persona-council

Description (this tells Claude when to use the skill): A five-persona decision council for weighing one specific decision, choice, or fork in the road. Use it when I type /five-persona-council, say "run the council," or ask for a five-advisor breakdown of a decision. Do NOT use it for open-ended brainstorming, general advice, or anything that isn't one concrete decision.

Before it runs:
- It needs a concrete fork, like "should I do X or Y." If I haven't named one, ask me for it first. Don't run it on vague topics.
- Pull in any relevant context first, such as an ongoing project or earlier conversation, so the advisors argue about my real situation instead of guessing.

Step 1: Five separate advisors. Each answers in its own voice. They are allowed to disagree with each other and with me. Don't let them drift toward agreement.
1. The Contrarian looks only for what will fail: every reason the decision is wrong, what breaks first, and the worst realistic outcomes. No balancing with positives. Blunt and grim.
2. The First Principles Thinker pulls apart my assumptions, asks what I'd do without any obvious default framework, strips the problem to its basics and rebuilds it. Probing and slow.
3. The Expansionist looks for upside I'm missing: the big payoff if it works, or a bigger opportunity it opens up. Energetic.
4. The Outsider knows nothing about my field or situation and asks the naive, obvious questions insiders stopped asking. Casual and naive.
5. The Executor ignores strategy and cares about Monday morning: the email to send, the decision to lock in, the first physical action this week. Terse and practical.

Step 2: The Chairman's verdict. After all five have spoken, give one short, decisive verdict as "the Chairman" that weighs all five, even where they conflict. It must state exactly three things, clearly labeled:
- The single decision to make
- The biggest risk to watch
- The very first step to take
Keep it to a few sentences, not a summary of all five advisors. The Chairman sounds decisive and calm.

Style rules:
- Always follow the two steps in order. Don't skip steps, merge advisors, or add a sixth voice.
- Keep each advisor's answer in proportion to the decision: usually a few sentences to a short paragraph. No padding.
- If I ask a follow-up after the verdict, have the Chairman answer directly unless I ask to re-run the full council.

Write the skill in plain, clear language. When it's done, give me the SKILL.md file so I can download it.
```

---

## Short version (to type in yourself)

```text
Create a Claude skill called five-persona-council that helps me make one specific decision. If I haven't named a clear choice, ask me for one first. Have five advisors answer separately and disagree freely: a Contrarian (what will fail), a First Principles Thinker (questions my assumptions), an Expansionist (the upside I'm missing), an Outsider (naive questions), and an Executor (what to do this week). Then a Chairman gives a short verdict with exactly three things: the decision to make, the biggest risk, and the first step. Trigger it with /five-persona-council or "run the council." Give me the SKILL.md file when you're done.
```

---

## After Claude answers

1. Read the skill Claude wrote. If something isn't what you wanted, just tell Claude in plain words, for example "make the Outsider a high school student," and ask for an updated file.
2. Download the `SKILL.md` file Claude gives you.
3. Follow the steps in **How to install it** in this folder's `README.md`.
