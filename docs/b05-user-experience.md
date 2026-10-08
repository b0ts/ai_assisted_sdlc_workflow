# Step 5: User Experience (The UI/UX Designer Chat)

**Role:** UI/UX Designer · **Prompt:** [c05](../prompts/c05-user-experience-prompt.md) · **Templates:** d05-01 to d05-02

## Executive Summary

At the end of [Step 4: Design](b04-design.md), we know **what** the product
must do (the PRD) and **how** it will be built (the Spec). But nobody has
yet decided what the product will **look like** or how it will **feel** to
use. That is the job of Step 5.

The person who does it is the **UI/UX Designer**, and the main thing they
produce is the **UI/UX Document**: pictures of every screen people will
see, called **mockups**, plus the design files that go with them.

- **Inputs:** the signed-off PRD from Step 3 and the signed-off Spec from
  Step 4, plus other inputs such as brand colors and logos, accessibility
  rules, and examples of apps the users already like.
- **Output:** the **UI/UX Document** (mockups, user flows, and a style
  guide), plus attached **design files**, such as Figma files, that coding
  tools can import.
- **Hand-off:** once the UI/UX Document is signed off, it goes to
  [Step 6: Initial Infrastructure](b06-infrastructure.md), and later to the
  Software Engineer in [Step 8: Implementation](b08-implementation.md),
  who builds the screens from it.

---

## What Is UI/UX?

UI/UX is two related ideas that usually go together:

- **User Interface (UI)** is everything a person *sees and touches*: the
  buttons, menus, text boxes, colors, pictures, and the layout of each
  screen.
- **User Experience (UX)** is how using the product *feels*: whether it is
  easy to understand, how many steps a task takes, whether it is confusing
  or frustrating, and whether people want to come back.

A restaurant is a good comparison again. In [Step 4](b04-design.md), the
Architect designed the kitchen: how orders travel and where the
ingredients are stored. The UI/UX Designer designs the **dining room**:
the menu, the tables, the lighting, and how easy it is to order. A
restaurant can have a great kitchen and still lose customers if the menu
is impossible to read.

## How UI/UX Relates to Architecture and Implementation

| | Architect (Step 4) | UI/UX Designer (Step 5) | Software Engineer (Step 8) |
|---|---|---|---|
| **Answers** | *How* is the system built inside? | *What* will people see, and how will it feel? | Building it for real |
| **House comparison** | Blueprints: walls, beams, pipes | Interior design: rooms, colors, where the light switches go | The construction crew |
| **Main output** | The Spec | The UI/UX Document and design files | Working software |

The three roles depend on each other. The Designer must work **inside**
the Architect's plan: if the Spec says the product is a phone app, the
screens are designed for a phone, and a screen can only show information
the Spec says the system actually has. In return, the Designer may
**discover** that a use case needs something the Spec left out, such as a
"forgot password" screen or a way to undo a mistake. Just as in Step 4,
the Designer doesn't quietly change the plan; the question goes back to
the Architect or Product Manager through the
[Tracking chat](b01-tracking.md).

---

## Why Architects and Programmers Need a Designer

Here is an honest truth about our industry: **Software Architects and
Programmers are usually not very good at user experience.** Their training
is in making systems that work correctly, not in making them pleasant.

Ask a programmer to draw a picture of a user, and you will probably get a
stick figure. Ask them to design how a user enters information, and you
will probably get a blinking cursor that the user types into:

```text
  The programmer's user:        The programmer's sign-up screen:

         O                      > Enter task ID, date (MM/DD/YYYY),
        /|\                       and start hour (0-23): _
        / \
```

It works, technically. But a real volunteer who wants to help clean the
beach doesn't know what a "task ID" is, won't remember the date format, and
will give up. Compare that with what a designer would sketch for
BeautifulBeachPark, the made-up park in our
[sample project](../samples/README.md):

```text
  ┌─────────────────────────────────┐
  │  Beach Cleanup                  │
  │  [ photo of the beach ]         │
  │                                 │
  │  Saturday, October 12           │
  │   9:00 – 10:00   2 spots left   │
  │                   [ Sign up ]   │
  │  10:00 – 11:00   Full           │
  │  11:00 – 12:00   4 spots left   │
  │                   [ Sign up ]   │
  │                                 │
  │  You'll appear as: BigHeartedGuy│
  └─────────────────────────────────┘
```

Both screens do the same job. Only one of them will be used. This is why
it is important to have someone, in our case an **AI assistant playing
the role of a UI/UX artist**, create a well-thought-out and compelling
interface for the people who will actually use the product. A clumsy
interface can sink a product with a perfect design underneath it, and a
good one is often what makes users choose you over a competitor.

This matters even more with AI. If the Software Engineer chat in Step 8 is
given no UI/UX Document, it will invent screens on its own, and they will
usually look like every other generic AI-built app: another form of the
"AI slop" described in [Prompt Engineering](a06-prompt-engineering.md).

---

## Inputs, Role, and Outputs

**Inputs.** The Designer starts from the two documents already signed off:

- **From the PRD:** who the **users** are (their skills, devices, and what
  might get in their way) and the **use cases**, since every use case
  needs at least one screen.
- **From the Spec:** what **type of application** is being built (web app
  or app-store app), what information the system stores, and the
  **sequence diagrams**, whose top "User ↔ Client" arrows show exactly
  where the user interacts with the product.
- **Other inputs:** brand colors, fonts, and logos; **accessibility**
  rules (for example, large enough text and support for screen readers);
  and apps the target users already know and like.

**The role.** The Designer's work usually moves from rough to polished:

1. **User flows:** simple diagrams of the path through each use case,
   screen by screen.
2. **Wireframes:** plain black-and-white sketches showing *where* things
   go, with no colors or pictures yet. Cheap to draw and cheap to change.
3. **Mockups:** full-color pictures of each screen, looking the way the
   finished product will look.
4. **Prototypes:** clickable mockups that let people try the flow before
   any code exists, so problems are found while they are still cheap to fix.

**Outputs.** Unlike some steps, UI/UX usually produces **several
documents**, not just one:

| Document | What it contains | Used to create code? |
|---|---|---|
| **UI/UX Document** | The main write-up: user flows, wireframes, mockups for every use case, and the reasons behind the choices | Guides the engineer |
| **Style Guide** (or design system) | Colors, fonts, spacing, and reusable pieces such as buttons and menus | **Yes:** often turned directly into code |
| **Design files** (such as Figma) | The actual editable screen designs | **Yes:** can be imported into coding tools |
| **Accessibility notes** (a section of the UI/UX Document) | How the design works for people with disabilities | Becomes test cases in [Step 7](b07-test-creation.md) |

Some of these are written for people to **read**, and some are made for
tools to **use**. The second kind is where UI/UX saves the most time.

---

## Design Files That Become Code

Professional UI/UX Designers rarely draw screens in a word processor. They
use design programs, and the best known is
[Figma](https://www.figma.com/). In Figma, a designer lays out every
screen, button, and color, and the file stores precise details: sizes,
spacing, fonts, and exact color codes.

Those design files can be **imported by the programmers during coding**.
Figma and similar tools can connect to coding tools such as Visual Studio
and Claude Code, and a Software Engineer (or Software Engineer AI chat)
can turn a design into the code for that screen, instead of writing the
layout by hand from a picture. The engineer still connects each button to
what it *does*, but the look of the screen comes straight from the
Designer's file, so the finished product matches the mockup instead of
being someone's best guess. This shortens the gap between design and code
and removes a whole category of mistakes.

---

## The UI/UX Designer Agent in Our Workflow

Like every step, User Experience runs in its **own new chat** (see
[What Is an AI-Assisted SDLC Workflow?](a07-what-is-an-ai-assisted-sdlc-workflow.md)).
The signed-off PRD and Spec are attached as its inputs.

| Stage | What the UI/UX chat does | What you do |
|---|---|---|
| **Review inputs** | Summarizes the PRD and Spec and lists gaps or open questions. | Answer questions or return to the PM or Architect. |
| **Map user flows** | Draws the screen-by-screen path for each use case. | Check that the steps make sense to a real user. |
| **Sketch wireframes** | Lays out each screen in simple form. | Pick a direction before details are added. |
| **Create mockups** | Produces polished screens and a style guide. | Review the look; test it on someone who fits the user profile. |
| **Prepare design files** | Organizes files (such as Figma) for import into coding tools. | Confirm they open and import correctly. |
| **Assemble the UI/UX Document** | Fills in the template. | Review it, then take it to the Tracking chat for sign-off. |

As always, the AI drafts and recommends, and **people decide**.

---

## Prompts, Templates, and Samples

> **To be updated:** This section will link to sample documents for the
> User Experience chat as they become available.

**Prompts** (in `prompts/`):

- [`c05-user-experience-prompt`](../prompts/c05-user-experience-prompt.md):
  plays the UI/UX Designer; reviews the PRD and Spec, maps a user flow per
  use case, sketches wireframes, matches the style to your organization's
  website, creates mockups of every screen, checks accessibility and
  privacy, and assembles the documents

**Templates** (in `templates/`):

- [`d05-01-ui-ux`](../templates/d05-01-ui-ux.md): UI/UX Document
- [`d05-02-style-guide`](../templates/d05-02-style-guide.md): Style Guide

**Samples** (in [`samples/BeautifulBeachParkVolunteers/docs/`](../samples/BeautifulBeachParkVolunteers/docs/)):

- **d05-01:** the sample project's
  [UI/UX Document](../samples/BeautifulBeachParkVolunteers/docs/d05-01-ui-ux.md),
  with a user flow for each use case in the sample PRD, a wireframe and
  [mockup](../samples/BeautifulBeachParkVolunteers/assets/mockups/) for
  each screen, and two requests sent back to the Architect
- **d05-02:** the sample project's
  [Style Guide](../samples/BeautifulBeachParkVolunteers/docs/d05-02-style-guide.md),
  matched to the park's pretend website, including a brand color darkened
  to pass the contrast check

Additional [case studies](case-studies.md) may be added to this repo at a
future time.

---

**Learn more:**

- [Step 4: Design](b04-design.md): where the Spec comes from
- [Step 6: Initial Infrastructure](b06-infrastructure.md): the next step
- [User experience design (Wikipedia)](https://en.wikipedia.org/wiki/User_experience_design):
  a plain introduction to UX design
