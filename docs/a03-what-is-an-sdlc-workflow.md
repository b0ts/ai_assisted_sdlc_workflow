# What Is a Software Development Lifecycle Workflow?

## Executive Summary

A **Software Development Lifecycle (SDLC)** is a step-by-step plan for
turning an idea into working software and keeping it working afterward. It
answers questions in a sensible order: *Should we build this? What should it
do? How will it work? Does it work? How do we keep it running?*

Today, AI tools can write software very quickly. But an AI that is simply told
"build me an app" has nothing to check its work against, and the results are
often messy, unreliable, and hard to fix. Following an SDLC gives the AI clear
written instructions at every step and a way to check whether each step was
done right.

This project uses a **Waterfall** SDLC adapted for **Test-Driven Development
(TDD)**. Waterfall means the steps happen in order, like water flowing
downhill: each step is finished before the next one begins. A standard
Waterfall builds the software first and checks it afterward. Our TDD version
flips that: **before anything is built, we write down exactly how we'll check
that it works. Then the AI builds until every check passes.** In our
experience, this has given more reliable results with AI than the
alternatives we tried.

---

## An Everyday Comparison: Building a House

You wouldn't hire a builder and say "make me a nice house" with no plans. You
would:

1. Decide whether you can afford it and where it will go.
2. List what you need: three bedrooms, a big kitchen, a ramp at the front door.
3. Have an architect draw the plans.
4. Agree on an **inspection checklist**: the doors are the right width, the
   wiring meets code, the roof doesn't leak.
5. Build the house.
6. Pass inspection and move in.
7. Keep up with repairs over the years.

Software works the same way. Each step produces something written down: a
list, a plan, a checklist. That written result is handed to the next step so
nobody has to guess.

---

## The Steps in Our Workflow

| Step | What happens | House comparison |
|---|---|---|
| 1. Tracking | Start a tracker for the project, then keep it updated through every other step. | The general contractor's schedule |
| 2. Feasibility | Decide whether the project is worth doing. | Can we afford it? |
| 3. Requirements | Describe who will use it and what they need to do. | "Three bedrooms, a ramp" |
| 4. Design | Plan how the software will work, including how it keeps information safe. | The architect's plans |
| 5. User experience | Sketch the screens people will see. | Choosing layouts and finishes |
| 6. Initial infrastructure | Arrange the computers or online services it will run on, then keep supporting them through the later steps. | Preparing the lot and utilities |
| 7. **Test creation** | Write down every check that proves the software works. | The inspection checklist |
| 8. Implementation | The AI builds the software until every check passes. | Construction |
| 9. Release | Make it available to real users and watch closely. | Move-in day |
| 10. Maintenance | Fix problems and keep it up to date. | Ongoing repairs |

Step 1 is different from the others. Tracking starts first, but it doesn't
finish when Feasibility begins. It keeps running alongside steps 2 through
10, recording progress and decisions as the other steps flow one after
another. Step 6 is partly like this too: it sets up the *initial*
infrastructure, and the DevOps Engineer then keeps helping through steps 7
to 10, for example by setting up a safe place to run tests and helping put
the software live.

Between every step, someone **reviews and approves** the result before the next
step begins. If a later step discovers a problem with an earlier one, such as
the plans revealing that the wish list is too big, we go back and fix the
earlier document first.

---

## What Makes Test-Driven Development Different

In a standard Waterfall approach, the software is built first and checked
afterward. In Test-Driven Development, **the checks come first.**

Think of a teacher who writes the answer key *before* the exam, rather than
grading answers by whatever "seems about right." Because the answer key already
exists, there's no arguing about what counts as correct.

The pattern repeats in small pieces:

1. **Write a check** for one small thing the software should do. It fails at
   first, because that part hasn't been built yet.
2. **Build** just enough to make the check pass.
3. **Tidy up** the work, making sure every check still passes.

Then move on to the next small piece.

## Why This Works Well With AI

- **A clear finish line.** The AI knows it's done when every check passes, not
  when it *thinks* it's done.
- **It catches convincing mistakes.** AI can produce work that looks right but
  isn't. The checks reveal the difference.
- **No surprise extras.** If there's no check asking for a feature, there's no
  reason to build it, so the project stays on track.
- **Safe changes later.** When something is fixed or added months from now,
  the existing checks immediately show if anything else broke.
- **Problems don't come back.** When a problem is reported after release, we
  first write a check that catches it, then fix it. That check stays forever.

We found TDD gave more consistent results than building first and checking
later, or letting the AI work with no checks at all. Results can vary, so we
encourage readers to compare approaches on their own projects.

---

## Learn More

**In this repo**

- [BeautifulBeachPark Volunteers sample](../samples/README.md): this
  workflow applied to a made-up project, with a document for every step
- Step guides: [1 Tracking](b01-tracking.md) ·
  [2 Feasibility](b02-feasibility.md) · [3 Requirements](b03-requirements.md) ·
  [4 Design](b04-design.md) · [5 User experience](b05-user-experience.md) ·
  [6 Initial infrastructure](b06-infrastructure.md) · [7 Test creation](b07-test-creation.md) ·
  [8 Implementation](b08-implementation.md) · [9 Release](b09-release.md) · [10 Maintenance](b10-maintenance.md)

**Beginner-friendly outside reading**

- [What is SDLC? (Amazon Web Services)](https://aws.amazon.com/what-is/sdlc/):
  a plain overview of the lifecycle and its phases
- [Systems development life cycle (Wikipedia)](https://en.wikipedia.org/wiki/Systems_development_life_cycle):
  history and the different styles of SDLC
- [Test-driven development (Wikipedia)](https://en.wikipedia.org/wiki/Test-driven_development):
  a general introduction to TDD
- [Test Driven Development (Martin Fowler)](https://martinfowler.com/bliki/TestDrivenDevelopment.html):
  a short explanation of TDD by a well-known software author

**Next:** [Steps, Roles, and Deliverables](a04-steps-roles-and-deliverables.md)
shows who is involved in each step, and
[What Is an AI-Assisted SDLC Workflow?](a07-what-is-an-ai-assisted-sdlc-workflow.md)
shows how AI chats play those roles.
