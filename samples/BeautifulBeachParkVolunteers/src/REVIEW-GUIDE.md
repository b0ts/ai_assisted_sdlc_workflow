# Reviewing the App

How the sample gets the three independent reviews the workflow requires
before Step 9 (b08, "Three Independent Reviews"), **without anyone having
to read code**. The reviews run **one after another**, in three rounds:

| Round | Reviewer | Report |
|---|---|---|
| 1 | Codex, a different company's AI, reviews the code | `docs/d08-04-code-review-codex.md` |
| 2 | A new Claude Code session reviews the improved code | `docs/d08-04-code-review-claude.md` |
| 3 | A person uses the app (the **hands-on review**) | `docs/d08-05-hands-on-review.md` |

In each round you decide on every finding, the fixes are made and tested,
and the same reviewer checks them (Section 4). The next round starts only
when this one is settled. No reviewer reads an earlier round's report, or
the review rows of d08-01 Section 7. This page also covers approving the
messages the code added in Step 8.

## 1. Round 1: Codex Code Review

Codex follows the prompt
[`c08-02-code-review-prompt.md`](../../../prompts/c08-02-code-review-prompt.md)
and writes a Code Review Report from the template
[`d08-04-code-review.md`](../../../templates/d08-04-code-review.md). It
reads but never changes the code. Either:

- In **Finder**, open the sample folder and double-click
  **`run-codex-review.command`**. Terminal opens, runs Codex in read-only
  mode, saves its answer word for word as
  `docs/d08-04-code-review-codex.md`, and opens it. It takes about 5 to 20
  minutes.
- Or ask Claude Code, in this sample folder: "Run Codex in read-only mode
  with the c08-02 prompt, and save its final answer, word for word, as
  `docs/d08-04-code-review-codex.md`." Claude Code only passes the prompt
  along and saves Codex's answer; it must never edit or summarize it.

Then decide and rework (Section 4). For the re-review, ask Claude Code:
"Run Codex in read-only mode with the c08-02 prompt's Mode E, comparing
with commit *[the commit before the fixes]*, and add its results to
`docs/d08-04-code-review-codex.md`."

## 2. Round 2: Claude Code Review

When every round 1 finding is settled and every test passes, open Claude
Code in this sample folder as a **new session**: not the one that built
the code, and not one used in round 1. Say: "Please follow
`prompts/c08-02-code-review-prompt.md` from the ai_assisted_sdlc_workflow
repo. This is round 2. Run `/security-review` first, and save your report
as `docs/d08-04-code-review-claude.md`." Then decide and rework (Section
4), and ask the same session for its Mode E re-review.

## 3. Round 3: Hands-On Review

When round 2 is settled, a person uses the app on a computer, the way
volunteers, coordinators, and the System Administrator will. Anyone can do
it, including you or another stakeholder; someone like a real volunteer
who didn't build it is best. They may look at the code, but don't have to.

**Prepare.** Start a chat with
[`c08-03-hands-on-review-prompt.md`](../../../prompts/c08-03-hands-on-review-prompt.md),
attaching `docs/d03-01-prd.md`, `docs/d05-01-ui-ux.md`, and
`docs/d08-02-developer-guide.md`. It writes the reviewer's **session
plan**. **For this sample, the plan is ready:** Section 2 of
[`docs/d08-05-hands-on-review.md`](../docs/d08-05-hands-on-review.md) has
the start steps, the made-up accounts, twelve tasks, and things to
explore. If round 1 or 2 changed a screen, check the plan still fits.

**Write up.** The reviewer notes what they did, what happened, and what
they expected, with screenshots. The same c08-03 chat turns the notes into
`docs/d08-05-hands-on-review.md`, and the reviewer checks it says what
they found. The helper never explains the screens during the session: if
the reviewer can't work something out, that's a finding.

Then decide and rework (Section 4); the reviewer re-checks each fixed
finding (c08-03, Mode E).

## 4. Deciding and Reworking, in Every Round

Each report starts with a **How to Read This Report** box. In short:

- Read the **verdict** first, then each **finding**. Each one says, in
  plain language, what's wrong, why it matters, and what to do next.
- Write your **Decision** in each finding's row: **Fix**, **Accept as is**
  (with a few words why), or **Ask**.
- **Rework.** Each "Fix" goes back to where the problem starts: a **bug**
  to the SDET chat (a test) and then the Software Engineer chat; a
  **usability** problem to the UI/UX chat first (d05-01), then the tests
  and code; a **missing requirement** to the Requirements chat (d03-01).
- **Re-review.** Every test runs again, then the same reviewer checks the
  changes and each fixed finding (Mode E of its prompt). Anything new goes
  around again. When every finding is settled, record the round in d08-01
  Section 7 and start the next round.
- **When a round ends.** A round ends when no Must-fix finding is left
  open. After that, a new Should-fix finding from a re-review goes on a
  Future Version list unless you choose Fix. (Decided for this sample on
  2026-10-26, during round 1.)

## 5. Questions Worth Deciding

Judgment calls the tests don't make. The reviewers may raise some of these
as "Question" findings; decide them either way. Any "change it" goes to the
right step's chat as a request.

| Question | How the code behaves now |
|---|---|
| Should sign-in links and new accounts be **rate-limited**? | Decided in round 1 (R-6): at most 10 sign-in emails per address in 24 hours (PRD v1.2). |
| Is a 30-day sign-in session right? | Volunteers stay signed in for 30 days on a device. |
| Should coordinators see only their own tasks on My Tasks? | Yes, only their own; but any coordinator can open any slot's roster. |
| Should blocking also cancel the blocked volunteer's existing sign-ups? | No: existing sign-ups stay; the volunteer just can't sign up again. |
| Is "Sign out" as a plain link acceptable? | Yes, a link; a stranger's page could sign someone out, but nothing else. |
| What if the encryption key is ever changed? | Existing emails, sign-ins, and blocks stop matching. The key must be kept, and backed up, in the secret store. Worth a line in d06-01. |

## 6. Messages to Approve

The messages the code added in Step 8, where the UI/UX Document had no
wording, were reconciled into d05-01 version 1.2, Section 9 ("Added in
v1.2"), in round 1 (finding R-5), with the empty screens, error pages, and
email subjects. All of them now live in
[`bbpv/wording.py`](bbpv/wording.py). To change any wording, ask the
Step 5 chat for a d05-01 change; the tests and the wording file follow.

## 7. When You're Done

1. **Record each round** in d08-01 Section 7 when it's settled: the
   "Round 1", "Round 2", and "Round 3" rows, each with the reviewer, the
   verdict or overall impression, your decisions, and the re-review
   result.
2. **Send any changes as requests**, never as quiet edits: wording to the
   Step 5 chat (d05-01 v1.2), new rules to the Step 3 chat, and code fixes
   to the Step 8 chat, with a test first through the Step 7 chat.
3. **Run the tests again** after any change, and add the run to d07-02.

## Appendix: If a Developer Also Reviews

A professional developer's review is still worth having if one is available,
especially for an app that stores personal information. This is the order
and checklist to give them.

### Before You Start

1. Set up and run the tests once, as the sample's [README](../README.md)
   shows. Seeing `58 passed` (or 56 plus the two browser tests) tells you
   the behavior is checked; your review is about what the tests can't see.
2. Start the local demo (`flask --app bbpv seed-demo`, then
   `flask --app bbpv run`) and click through it as a volunteer, a
   coordinator, and the admin. It's easier to read code for screens
   you've used.
3. Keep the Spec's Section 11, Security & Compliance
   ([`docs/d04-01-spec.md`](../docs/d04-01-spec.md)), open beside the code.

### Read in This Order

| # | File | What to check | Time |
|---|---|---|---|
| 1 | [`README.md`](README.md) | What each file is for | 5 min |
| 2 | [`bbpv/privacy.py`](bbpv/privacy.py) | Emails are encrypted (`EmailVault.encrypt`); the sign-in and block-list copies are one-way scrambles (`lookup_key`, `block_key`); `standardize` turns `j.o.h.n+beach@...` into `john@...` as the Spec says | 15 min |
| 3 | [`bbpv/db.py`](bbpv/db.py) | No table has a plain email column, only `email_encrypted` and the two scrambled copies. The block list keeps only `email_block_key`, so a block survives when an account is deleted | 10 min |
| 4 | [`bbpv/views.py`](bbpv/views.py) | The rules for every screen (see the checklist below) | 45 min |
| 5 | [`bbpv/__init__.py`](bbpv/__init__.py) | Settings come from the environment; the app refuses to start without its keys, or with the pretend inbox on a live database; plain HTTP is redirected to HTTPS; forms need a token (`check_form_token`) | 15 min |
| 6 | [`bbpv/cli.py`](bbpv/cli.py) | `delete-account` gives places back and keeps the block; `send-reminders` emails only tomorrow's sign-ups, once each | 10 min |
| 7 | [`bbpv/templates/`](bbpv/templates/) | No page is handed an email address. Pages show usernames only (the pretend inbox is the deliberate exception: local demo only) | 15 min |

### Checklist

Tick each one, or note what you found.

**Privacy (Spec 11.1)**

- [ ] Emails are decrypted in exactly one place, `deliver()` in
      `views.py`, and only to send an email. Quick check, in the `src/`
      folder: search the code for `decrypt` (in Visual Studio Code:
      **Edit**, then **Find in Files**). Only `privacy.py` (where it's
      defined) and `deliver()` should use it.
- [ ] The roster (`roster()`) reads usernames only, never emails.
- [ ] The sign-in page gives the **same reply** whether or not an account
      exists (`sign_in()`), so no one can test which emails are signed up.
- [ ] A blocked email can't make a new account, even written differently
      (`create_account()`), and the refusal never says why.

**Who may do what (Spec 11.1)**

- [ ] Every screen has a `@signed_in(...)` line naming who may use it, and
      it matches the Spec: volunteers sign up and cancel; coordinators post,
      see rosters, message, and block; only the admin undoes a block.
- [ ] A volunteer can cancel only their **own** sign-up (`cancel_sign_up()`
      checks `account_id`).

**The rules from the PRD and Spec**

- [ ] The last place is taken in a single database step (`sign_up()`: the
      `UPDATE ... WHERE places_left > 0`), so a slot can't be over-filled
      (Spec DD-5).
- [ ] Posting a task (`_check_task()`) enforces one-hour slots, 1 to 20
      places, and titles up to 60 characters.
- [ ] Sign-in links work once, for 15 minutes, and are stored scrambled
      (`send_sign_in_link()`, `use_sign_in_link()`).

**Nothing surprising**

- [ ] No passwords, keys, or real email addresses are written in the code.
- [ ] No code sends data anywhere except the email service in `mail.py`.
- [ ] Every outside library is in `requirements.txt` and in the Developer
      Guide's license table (d08-02 Section 7).
