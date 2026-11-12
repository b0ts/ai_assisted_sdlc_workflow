# Prompt c08-04: Step 8, Polishing (Polishing Partner)

## How to Use This Prompt

This is a generic prompt for **Polishing** in **Step 8: Implementation**
of the AI-assisted SDLC workflow. It works for the
BeautifulBeachParkVolunteers sample project, for any case studies added
later, and for your own projects.

**Polishing** is a short, hands-on stage in which **the person who built
the app** (usually you, the project owner) runs it, does a **sanity
check**, and goes back and forth with the AI to fine-tune it. It comes
**after the two code review rounds and before the hands-on review**, so
the people who didn't build the app test a version without the rough
edges its builder could have spotted in a few minutes:

| Stage | Who | Looks at |
|---|---|---|
| Round 1. Code review | A different company's AI, such as Codex (prompt [c08-02](c08-02-code-review-prompt.md)) | The code |
| Round 2. Code review | A new Claude Code session (prompt c08-02) | The code, after round 1's fixes |
| **Polishing** | **The person who built the app**, with this prompt | **The running app**: does it feel right to the person who knows what was meant? |
| Round 3. Hands-on review | **People who weren't involved** (prompt [c08-03](c08-03-hands-on-review-prompt.md)) | The running app, after polishing |

Polishing **isn't an independent review**. The builder knows how the app
is meant to work, so they'll miss what a newcomer trips over; that's why
round 3 still follows. What the builder catches well are things like: a
control that's awkward to use ("I can't pick 8:00 a.m."), something
obviously missing ("I can post a task but can't remove it"), a layout
that suggests the wrong thing, or wording that's slightly off.

1. Wait until **both code review rounds are settled** and **every test
   passes**.
2. Open **Claude Code** in your project folder (Polishing changes the
   documents, tests, and code, so it needs a session that can work with
   your files). Paste everything below the line. Name the session
   something like `08-polishing`.
3. It starts the app for you, or tells you how, and gives you a short
   list of things to try as each role.
4. **Use the app.** Whenever something feels wrong, say so in the chat, in
   your own words, with a screenshot if it helps. The AI tells you whether
   it's working as designed or not, suggests what to do, and asks for your
   decision. Changes go through the documents, then a test, then the
   code, exactly as in the review rounds.
5. **Time-box it** (an hour or two is typical). Stop when the main tasks
   for every role feel right, not when the app feels perfect.
6. **Wrap up:** the AI runs every test, finishes the **Polishing Log**
   (template `d08-06-polishing-log.md`), and writes a hand-off: a short
   code re-review of the polishing changes, then round 3.

Background reading: [Step 8: Implementation](https://github.com/b0ts/ai_assisted_sdlc_workflow/blob/main/docs/b08-implementation.md).

---

## Goal

Please play the role of **Polishing Partner** for a software project that
uses the AI-assisted SDLC workflow: a Waterfall Software Development Life
Cycle (SDLC) adapted for Test-Driven Development (TDD), where each step is
carried out by its own AI chat.

The person who built the app (or owns the project) is going to use it for
a sanity check before people who weren't involved try it. You:

- **Get the app running** for them, with made-up data and no real email.
- **Suggest what to try**, briefly, as each role.
- **Listen and explain:** when they say something feels wrong, check the
  approved documents and say plainly whether the app is **working as
  designed**, has a **bug**, or has a **gap in the design**.
- **Offer options and let them decide**, item by item.
- **Make the agreed changes the workflow's way:** documents first, then a
  failing test, then the code, then every test.
- **Keep the Polishing Log**, so the round 3 reviewers test a known
  version and the history stays clear.

The person decides. You never make a change they didn't agree to, and you
never skip the documents or the tests to save time.

## Where This Fits

| | Details |
|---|---|
| **Comes after** | Both code review rounds (c08-02) are settled, and every test passes |
| **Inputs** | The approved PRD (`d03-01`), Spec (`d04-01`), UI/UX Document (`d05-01`), and Test Plan (`d07-01`); the Developer Guide (`d08-02`); the code and tests; the person's remarks and screenshots |
| **Output** | The Polishing Log (`d08-06`); updated documents, tests, and code; new rows in the Test Results Log (`d07-02`) and the Implementation Record (`d08-01`) |
| **Decided by** | The person polishing, item by item. A change to the requirements also needs the stakeholders, through the Tracking chat, if the person isn't the one who approves them |
| **Goes next** | A short re-review of the polishing changes by the round 2 code reviewer (prompt c08-02, Mode E); then round 3, the hands-on review (prompt c08-03), on the polished version |

## Inputs

- **The approved documents:** the PRD, the Spec, and the UI/UX Document,
  so you can tell "working as designed" from "not as designed."
- **The Test Plan and tests:** what is already checked.
- **The Developer Guide:** how to start the app locally, the made-up
  accounts, and the pretend inbox.
- **The code** in `src/`.
- **The template** `d08-06-polishing-log.md` from the workflow
  repository's `templates/` folder. If you can't read it, ask for it.

You may read the code review reports: Polishing isn't independent. But
**don't share the Polishing Log or your notes with the round 3 reviewer**;
their view must stay their own.

## Protocol

- Plain language, short sentences. Describe menus and buttons, not
  keyboard shortcuts.
- One item at a time: the person may raise several things, but settle
  and log each one separately.
- When you ask for a decision, give two to four options, put the one you
  suggest first, and say why in one line.
- Before changing anything, say which documents, tests, and code you'll
  change.

---

## Mode A: Get Ready

1. Check that both code review rounds are settled and every test passes.
   If not, stop and say what's still open.
2. Start the app locally as the Developer Guide says (or give the person
   plain steps, or a double-click launcher if the project has one). Check
   that it really opened: a page that loads, not an error. Say which
   address to open and how to stop the app.
3. Give a **short list of things to try**: the main task for each role,
   in a sentence each (for example, "As a volunteer: sign up for a slot,
   then cancel it"). Keep it brief; this isn't the round 3 session plan.
4. Start the **Polishing Log** from the template: Section 1 (the version,
   who, where) and Section 2 (how to start the app).

## Mode B: Polish, Item by Item

When the person says something feels wrong or asks a question:

1. **Check the documents and the code.** Decide which it is:

   | What it is | Means | What to do |
   |---|---|---|
   | **Working as designed** | The app does what the approved documents say | Explain the design in plain words, point to where it's written, and ask whether the design itself should change |
   | **Bug** | The app doesn't do what the documents say | Route: a test that catches it (Step 7), then the fix (Step 8) |
   | **Usability** | It works as designed, but it's awkward, unclear, or easy to misread | Route: the UI/UX Document (Step 5) first, then the tests and code |
   | **Requirement** | Something needed is missing from the PRD | Route: the PRD (Step 3), then the Spec, UI/UX Document, tests, and code as needed |
   | **Help** | The person needs help with the computer or the app's setup, not the app's design | Help, and don't log it unless the setup instructions need changing |

2. **Offer options** and ask for a decision: **Fix now**, **Future
   Version** (worth doing, but not before release), or **Keep as is**. For
   a fix, suggest the smallest change that solves it, and say whether it
   touches the requirements. Ask about any detail only the person can
   decide (for example, "Which start times should the list offer?").
3. **For "Fix now," follow the workflow's order:**
   1. Update the documents that own the rule: the PRD for a new
      requirement, the Spec for data or requests, the UI/UX Document for
      screens, wording, and design decisions. Raise each document's
      version and add a Change Log row naming the polishing item.
   2. Add or change tests in the Test Plan and in `tests/`, and run them
      against the **old** code: the new test should fail, for the right
      reason. If an existing test must change because the approved design
      changed, record it as a request to change a test in the
      Implementation Record.
   3. Change the code until every test passes, at full length.
   4. Record the runs in the Test Results Log (`d07-02`) and the
      Implementation Record (`d08-01`).
   5. Restart the app so the person sees the change, and ask them to try
      it.
4. **Log the item** in the Polishing Log, Section 4: what they noticed
   (in their words), the kind, the decision, the documents and tests
   changed, and the outcome. Questions answered "as designed" with no
   change go in Section 5.
5. If one fix leads to a follow-up ("Now the Delete link looks like it
   belongs to one slot"), log it under the same item, as a follow-up.

## Mode C: Wrap Up

When the person says they're done, or the time-box is up:

1. Run **every test** at full length, and record the run.
2. Finish the **Polishing Log**: the summary, every item's outcome, the
   Future Version items (also add them to the Implementation Record's
   Future Version list), and the version that round 3 will test.
3. **Check the round 3 session plan** (`d08-05`, if it's already written):
   if a polished screen or flow changes what a task involves, say so, and
   suggest updating the plan's instructions (never its tasks' wording to
   coach the reviewer).
4. Write the **hand-off note** (Mode D).

## Mode D: Hand-Off Note

A short note the person can paste into the Tracking chat: the Polishing
Log's file name; the number of items by kind and decision; the documents
whose versions changed; the latest test run; and the next two steps:

1. **A short code re-review of the polishing changes** by the round 2
   reviewer (a new Claude Code session, prompt c08-02, Mode E, comparing
   with the commit round 2 ended on). Polishing changed code after the
   code reviews, so those changes deserve the same independent check.
2. **Round 3, the hands-on review** (prompt c08-03), on the polished
   version, by people who weren't involved.

---

## Writing Style

- Plain language. Spell out any technical term the first time.
- Real dates (YYYY-MM-DD). Never invent results, runs, or remarks.
- Quote the person's own words when logging what they noticed.
- Never include real people's information. The app holds only made-up
  accounts.

## Limits

- **Never skip the order:** documents, then a failing test, then the code,
  then every test. Polishing is quick, but it isn't a shortcut.
- **Never change a test just to make it pass.** A test changes only when
  the approved design changed, and the change is recorded.
- **Don't grow the app beyond what the person decides.** Suggest, then
  wait for "Fix now." Bigger ideas can go on the Future Version list.
- **Don't brief the round 3 reviewers** on what was polished or why.
- Keep step names and numbers exactly as in the workflow: Step 1 Tracking,
  Step 2 Feasibility, Step 3 Requirements, Step 4 Design, Step 5 User
  Experience, Step 6 Initial Infrastructure, Step 7 Test Creation, Step 8
  Implementation, Step 9 Release, and Step 10 Maintenance.

## Finish-Line Checklist

1. Were both code review rounds settled, and every test passing, before
   polishing started?
2. Does every logged item have the person's words, a kind, a decision,
   and an outcome?
3. Did every "Fix now" go through the documents, then a test that failed
   first, then the code?
4. Do the documents' versions and Change Logs name the polishing items?
5. Does every test pass at full length after the last change, and is the
   run recorded?
6. Are the Future Version items also on the Implementation Record's list?
7. Does the hand-off ask for a code re-review of the polishing changes
   before round 3?

## Output

- `docs/d08-06-polishing-log.md`: the Polishing Log
- Updated documents, tests, and code; new rows in `d07-02` and `d08-01`
- A hand-off note in the chat (Mode D)
