# Redesign Plan: The BeautifulBeachPark Sample

This plan records the decisions behind the repo's redesign and the work
still to do. It can be deleted once the checklist at the end is complete.

## The Redesign in One Paragraph

The repo teaches the workflow with **one story**. Readers first look at a
finished sample project, the BeautifulBeachPark volunteer app in
[`samples/BeautifulBeachParkVolunteers/`](samples/BeautifulBeachParkVolunteers/),
then build their own copy (for example, `OurGroupVolunteerApp`) by following
the docs: creating a folder, copying in the skeleton, connecting it to
GitHub, and running each step's prompt. Their version is styled to match
their own organization's website. Real-organization case studies may be
added later (see [docs/case-studies.md](docs/case-studies.md)); the RC Park
Tour example has been removed from this repo.

## The Sample Product

**BeautifulBeachPark** is an obviously made-up park. Its volunteer app lets
coordinators post tasks that need volunteers, and lets volunteers sign up
for one-hour slots.

**Example tasks:** Raking Leaves, Pulling Weeds, Beach Cleanup, Driftwood
Removal.

**Roles (actors):**

| Role | What they do | What they can see |
|---|---|---|
| **Volunteer** | Creates an account with a username and email only, browses slots, signs up, cancels | Usernames only; never other people's emails |
| **Coordinator** | Posts tasks with one-hour slots, views rosters, messages volunteers through the app, blocks volunteers by username | Usernames only; never emails. There can be several coordinators. |
| **System Administrator** | Runs the system; the only one who can undo a block | Can technically see emails. This is stated plainly in the Spec and in the privacy notice volunteers see at sign-up. |
| **Email service** (external system) | Sends reminders and relayed messages | — |

**Use cases (Phase 1):**

1. A coordinator posts a task with one-hour slots.
2. A volunteer creates an account with a username and email only.
3. A volunteer browses open slots and signs up.
4. A volunteer cancels.
5. A coordinator views a task's roster (usernames only).
6. A coordinator messages a volunteer through the app's relay.
7. A coordinator blocks a volunteer.

If the samples run long, UC-4 and UC-6 can move to Phase 2.

## Privacy Decisions (from the start, not a later change)

- **No real names.** The app never asks for one. Only a username and email
  are collected (data minimization).
- **No sharing of email.** Volunteers and coordinators never see anyone's
  email. Reminders are sent automatically by the app, and coordinators
  reach volunteers through a **message relay** that forwards messages
  without revealing the address.
- **Email is not hidden from system-level administration.** The Spec and
  the sign-up privacy notice say so honestly, rather than promising no one
  can ever see it.

## Blocking

- A coordinator blocks by **username**. The system looks up that account's
  hidden email and adds it to a **block list**, so the person can't simply
  create a new account with the same email. The coordinator never sees the
  address.
- Emails are **normalized** before checking (for example,
  `j.o.h.n+food@gmail.com` and `john@gmail.com` count as the same inbox).
- The Spec states honestly that a determined person can create a new email
  address. Stronger checks, like phone verification, would mean collecting
  more personal data, which conflicts with the privacy goal. That trade-off
  is written down.
- If a blocked account is deleted, the block list keeps a scrambled
  (**hashed**) copy of the email, not the address itself.
- Only the System Administrator can undo a block. A full appeal process is
  out of scope.
- Use the term **block list**, not "blacklist."

## Situational Diagrams

- **State Machine Diagram** for a slot: open → filled → completed, or back
  to open on cancel.
- **Sequence diagrams** of special teaching value: two volunteers taking the
  last open slot at the same moment, the message relay, and blocking.

## Out of Scope (listed in the sample PRD)

- Recurring weekly tasks
- Waitlists when a task is full
- Skills matching (for example, needing a forklift license)
- Volunteer hour reports
- Real identities for background checks, waivers, or emergency contacts
- A token economy (see the note below)

## The Go-Back Moment

The sample PRD includes **text-message reminders**. The Architect sends
them back to a later phase, because a texting service costs money for every
message, while email reminders cost nothing to start. The revised PRD
shows a Change Log row, demonstrating the loop in
[Step 4: Design](docs/b04-design.md).

## Note for Readers Building Their Own App

Include this in the sample PRD's out-of-scope section and in the tutorial
where readers write their own PRD:

> **Idea for your own app: a token economy.** Some groups reward volunteers
> with tickets, for example one ticket for every hour of volunteer work,
> which volunteers can collect and exchange for small items such as
> stickers, T-shirts, or water bottles. This can be added to your own app,
> provided it complies with the local laws and regulations that apply to
> volunteer work. Some places limit what volunteers can receive before they
> count as paid workers. Keep rewards small, give tickets no cash value, and
> check with your organization's legal advisor before launching.

## Look and Feel

The sample's UI/UX Document takes a pretend BeautifulBeachPark website as
an input (sand-and-ocean colors, a simple logo) and matches it. In the
tutorial, readers give the UI/UX chat their own website's address or
screenshots instead.

## Remaining Work

**Done in this redesign:**

- [x] Removed RC Park Tour references, including
  `docs/rc-park-tour-ai-sdlc-case-study.md` (its history stays in Git);
  added [docs/case-studies.md](docs/case-studies.md) for future case studies
- [x] Moved the UML Diagram Guide to
  [docs/a09-uml-diagram-guide.md](docs/a09-uml-diagram-guide.md)
- [x] Created the sample project folder from the skeleton
- [x] Pointed prompts, templates, and step guides at the sample
- [x] Replaced the "Book a tour" illustrations in b03, b04, and b05
- [x] Wrote prompts `c01` to `c10`, templates `d01` to `d10`, and step
  guides b01 to b10
- [x] Created all the sample documents, `d01-01` to `d10-03`, plus the
  UI mockups and design tokens in `assets/`
- [x] Replaced the tour-booking hints in the templates (`d02-01`, `d02-02`,
  `d02-04`, `d03-01`, `d04-01`, `d04-02`) with volunteer examples
- [x] Offered a menu-based path in a08 (GitHub Desktop) alongside asking
  Claude Code in a terminal
- [x] Adopted "local first, live later" across the guides, prompts, and
  templates (a04, a07, b06 to b09, c01, c06 to c10, d01-01, d06, d09):
  Step 6 chooses the live servers (the organization's existing servers
  first) and records their rules, but sets up only a free local
  environment; Step 8 writes portable code; Step 9 runs a stakeholder demo
  on the local copy, then moves the software to the live servers, runs a
  private pilot with test accounts, and goes live
- [x] Replaced the made-up "SampleCloud" and "SampleMail" in the sample with
  the city's existing servers, run by a made-up IT team, Parks IT
  (d01-01, d06 to d10)
- [x] Wrote the sample's tests in `samples/BeautifulBeachParkVolunteers/tests/`
  (38, one per Test Plan ID), with the contract the code must follow in
  `tests/README.md`

- [x] Wrote the sample's real code in `samples/BeautifulBeachParkVolunteers/src/`
  (Flask, SQLAlchemy, encrypted emails, a pretend inbox for the local demo);
  all 38 tests pass, and `d07-01`, `d07-02`, `d08-01`, `d08-02`, and the
  sample README now match the real code and runs

**Still to do:**

- [ ] A person reviews the sample's code in `src/` (the workflow requires
  it before Step 9; the sample documents describe a made-up reviewer)
- [ ] Confirm the wording the code added in Step 8 (marked in
  `src/bbpv/wording.py`) and record it in `d05-01` v1.2
- [ ] Write the tutorial: building your own app (for example,
  `OurGroupVolunteerApp`) from the skeleton, styled to match your website,
  following the same local, demo, live path, including the private pilot
