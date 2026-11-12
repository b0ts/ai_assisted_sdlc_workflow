# BeautifulBeachPark Volunteers: Code Review Report

**Document:** d08-04 · **Step:** 8, Implementation · **Version:** 1.0
· **Last updated:** 2026-10-25 · **Status:** Awaiting decisions
· **Owner:** Code Reviewer (Claude Code, a new, separate session; model Claude Opus 5.5)

> **How to Read This Report**
>
> You don't need to read the code. Start with the **verdict** in the
> Overview, then read each row in **Findings**:
>
> - **Must fix** means the code breaks a promise in the approved documents
>   or puts people's information at risk. These normally get "Fix."
> - **Should fix** is a real risk the documents didn't ask about. Decide
>   whether it's worth the time now or in a later phase.
> - **Question** is something only the stakeholders can decide.
> - **Note** needs no action.
>
> For each finding, write your **Decision**: **Fix** (send it to the chat
> named in "Next step"), **Accept as is** (say why, in a few words), or
> **Ask** (you need to know more; ask the reviewer or the Software
> Engineer chat). An AI reviewer can be wrong in both directions: it can
> miss a problem or report one that isn't there. That's why there are two
> independent reviews, and why the decision is yours.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Code reviewed | `src/` as of 2026-10-25 (commit 4867cab plus later local changes), and `tests/` |
| Reviewer | Claude Code (a new, separate session), model Claude Opus 5.5 |
| Independent? | Yes: a new session that didn't write or change the code; no other review read first (none was in the project) |
| Documents checked against | d03-01 PRD v1.1, d04-01 Spec v1.1, d05-01 UI/UX v1.1, d06-01 Infrastructure v1.3, d07-01 Test Plan v1.1, d08-01 Implementation Record v1.0, d08-02 Developer Guide v1.0 |
| Review date | 2026-10-25 |
| Verdict | **Ready after the Must-fix items.** No email address reaches any volunteer's or coordinator's screen, and the core rules are sound, but the daily reminder job can silently skip people's reminders, and two promises in the Spec (retrying failed emails, deleting old tasks) aren't carried out. |
| Findings | 2 Must fix · 9 Should fix · 4 Question · 4 Note |

**The app in brief.** Park coordinators post volunteer tasks split into
one-hour slots, volunteers sign up with only a username and an email
address, and a System Administrator can undo blocks. Everyone signs in
with a one-time link sent by email; there are no passwords. Spec Section
11 promises that volunteers' email addresses are stored encrypted, are
never sent to anyone's web browser, and are used only to send email; the
block list keeps only a scrambled copy. The code is small: about 1,130
lines of Python and 14 page templates in `src/`, with about 1,340 lines
of tests.

## 2. What Was Checked

| Area | What was checked | Result |
|---|---|---|
| Privacy and security | Spec Section 11: where email addresses are stored, read, and shown, on every page, every reply, every email sent, and the sign-in cookie; secrets; sign-in links; injected code in form fields; forged form submissions; plain HTTP. **Your priority (no email shown to other volunteers or coordinators) was checked page by page and holds.** | No email reaches a volunteer's or coordinator's screen. 4 Should fix (R-3 to R-6), 2 Note (R-16, R-17) |
| Who may do what | Every page and request checks the person's role, as Spec 11.1 says | Every page checks the role correctly. 1 Question (R-15) |
| PRD and Spec rules | UC-1 to UC-7 acceptance criteria and limits; DD-1 to DD-5, including taking the last place in one step (DD-5) | 2 Must fix (R-1, R-2), 1 Should fix (R-9), 2 Question (R-12, R-13) |
| Ready to move | d06-01 Section 5.1, row by row; every setting from outside the code | 2 Should fix (R-7, R-8), 1 Question (R-14), 1 Note (R-18) |
| Tests | They match the Test Plan's 38 tests; gaps. Ran the 34 quick tests: all pass | 1 Should fix (R-10) |
| Nothing surprising | Data sent anywhere unexpected; libraries not in the Developer Guide; leftover debugging code | Nothing found: no data goes anywhere but the email service; every library is listed; no debugging code left. 1 Note (R-19) |
| Wording | Messages against d05-01 Section 9 and the empty-screen texts in Section 8; messages d05-01 didn't cover | Section 9 messages match word for word. 1 Should fix (R-11) |
| Built-in security scan | Claude Code's `/security-review` command | Not available in this session (it was started by another tool). A manual security review was done instead, and its findings are in R-3 to R-6 |

## 3. Findings

| ID | Seriousness | Where | What's wrong, in plain language | Why it matters | Breaks | Next step | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|
| R-1 | Must fix | `src/bbpv/cli.py`, `send_reminders()`; `src/bbpv/mail.py`, `send()`; `src/bbpv/views.py`, `send_sign_in_link()` and `message_volunteer()` | Failed emails are never retried. Worse, the daily reminder job sends all of the day's reminders as one batch: if any single email fails (for example, the email service rejects one address), the job stops, the rest get no reminder, and the record of who already got one is undone. The next day those slots are "today," so the job never goes back for them. The reviewer reproduced this: with three volunteers and the second email failing, one got a reminder, two got none, and no retry ever happened. A failed sign-in link or coordinator message just shows "Something went wrong," and a new account isn't saved. | Volunteers miss reminders without anyone knowing, so slots go unfilled, which is the problem the app exists to solve. One bad address can stop every reminder for a day. | Spec Section 7 ("Send email ... fails: Retried later"); Spec Section 14 ("Retry later"); PRD UC-3 AC5 (reminder the day before) | SDET chat: add a test where one email fails and the others must still go out and be retried; then Software Engineer chat: send each reminder separately, record each one as it's sent, and keep failed emails to retry | | |
| R-2 | Must fix | `src/bbpv/cli.py` (no clean-up command); `src/bbpv/db.py` | The Spec says tasks (with their slots and sign-ups) are kept for 12 months after their date. Nothing in the code ever deletes them, so they are kept forever. | Sign-ups record which username was at the park when. Keeping that for ever goes beyond what the park told people, and privacy laws (Spec 11.3) expect data to be kept only as long as stated. It isn't urgent: nothing is older than 12 months until a year after going live. | Spec Section 6 (Task: "12 months after its date") | SDET chat: add a test; then Software Engineer chat: add a clean-up to the daily job. Or, if the park prefers, the Design chat changes the Spec instead | | |
| R-3 | Should fix | `src/bbpv/views.py`, `pretend_inbox()`; `src/bbpv/__init__.py`, `create_app()` | The local "pretend inbox" page shows every email the app would have sent, including each person's email address and working sign-in links, to **anyone** who opens it, without signing in. The only thing that stops it on a live server is a check on the type of database; it doesn't check that the app is on a laptop. The reviewer confirmed that, with that database type and HTTPS turned on, a stranger could open the page, copy someone's sign-in link, and be signed in as them. | Today it holds only made-up data on a laptop, so the risk is small. But if the demo is ever run on a shared network, or the app is set up live with the simple database, everyone's email address is exposed and anyone can sign in as anyone. | Reviewer's opinion (supports Spec 11.1) | Software Engineer chat: allow the pretend inbox only when the app is running on the laptop itself, and refuse to start with it when HTTPS is forced; SDET chat: add a test | | |
| R-4 | Should fix | `src/bbpv/views.py`, `create_account()` | The sign-in page is careful to give the same reply whether or not an email has an account (Spec Section 7). But the Create Account page gives it away: try to create an account with someone's email, and it says "We couldn't create this account" if that email already has one, and "Check your email" if not. Anyone can also create an account using someone else's email address. | Someone could find out whether a neighbor or ex-partner volunteers at the park, which is the very thing the sign-in reply was designed to hide. | Reviewer's opinion; defeats the purpose stated in Spec Section 7 ("so no one can test which emails exist") | Software Engineer chat: give the same "Check your email" reply when the email is already in use, and email the owner instead; SDET chat: add a test | | |
| R-5 | Should fix | `src/bbpv/views.py`, `sign_in()` and `create_account()` | There's no limit on how often someone can ask for a sign-in link or create accounts. A person or a program could ask hundreds of times. | Someone could flood a volunteer's inbox, and use up Parks IT's limit of 3,000 emails a month (d06-01 Section 5), after which no one gets reminders or sign-in links. | Reviewer's opinion; risk to the d06-01 Section 5 email limit | Software Engineer chat: limit requests per email address and per visitor (for example, a few per hour); SDET chat: add a test | | |
| R-6 | Should fix | `src/bbpv/views.py`, `use_sign_in_link()` | The sign-in link signs the person in, and is used up, the moment it's opened. Some email services open every link in an email automatically to check it for viruses. | For volunteers whose email service does this, the link is used up before they tap it, and they see "This link isn't valid." They may give up on signing in. | Reviewer's opinion | Software Engineer chat: have the link open a page with a "Sign in" button, and sign in only when it's pressed; SDET chat: update the sign-in tests | | |
| R-7 | Should fix | `src/bbpv/__init__.py`, `create_app()` (`CLOCK` is the server's own clock) | The app takes "now" from the server's clock and treats it as park time. There is no setting for the park's time zone. Servers are often set to world time (UTC), which can be 7 or 8 hours different. | If Parks IT's server isn't set to park time: the 6 p.m. reminder job would remind people about the day after tomorrow; slots would disappear from Open Slots hours early or late; and cancelling could be allowed after a slot started, or refused before. | Reviewer's opinion; d06-01 Section 5.1 ("needs only settings") doesn't cover time zone | Initial Infrastructure (DevOps) chat: confirm the server's time zone with Parks IT; Software Engineer chat: add a park time zone setting; SDET chat: add a test | | |
| R-8 | Should fix | `src/requirements.txt`; d08-02 Section 5.1, step 3 | The Developer Guide tells Parks IT to "start the app as a service," but doesn't say with what. The only way to start it that the guide mentions is the built-in test server (`flask run`), which Flask itself says not to use on live servers. No production web server is listed. | Parks IT may run the app on the test server, which is slower and less reliable under load, or come back with questions during their 2-week security review. | Reviewer's opinion; d06-01 Section 5.1 ("following the Developer Guide; started as a service") | Software Engineer chat: name a production server (for example, Gunicorn), add it to the library list and requirements, and give the exact start command in d08-02 | | |
| R-9 | Should fix | `src/bbpv/templates/post_task.html` (script); `src/bbpv/views.py`, `_check_task()` | The slot end time is filled in by the browser, and the "Ends" box can't be typed in. If the browser's scripts are off or fail, every task is refused with "Please enter each slot's start and end time," which the coordinator can't do. Separately, a slot starting at 11 p.m. or later is always refused with "Each slot must be one hour," because the end falls on the next day. | A coordinator on a locked-down or older phone can't post a task at all. Late-evening tasks (such as a night beach walk) can't be posted. | d05-01 UX-3 (end set automatically); tests/README.md says everything works without JavaScript (a browser's scripting language) | Software Engineer chat: work out the end time on the server, from the start time; SDET chat: add a test for an 11 p.m. slot | | |
| R-10 | Should fix | `tests/conftest.py` and `src/bbpv/__init__.py`, `check_form_token()` | The protection against forged form submissions (another website quietly submitting a form as the signed-in person) is turned off in every test, as the tests' contract allows. So no test checks it. The reviewer checked by hand that it works today. Also untested: what happens when an email fails (R-1), and that the pretend inbox is off on live settings (R-3). | If a later change breaks this protection, the tests will still pass, and another website could make a signed-in coordinator block a volunteer. | Reviewer's opinion (Test Plan Section 8 covers Spec 11.1, but not this) | SDET chat: add tests that run with the protection on, and for R-1 and R-3 | | |
| R-11 | Should fix | `src/bbpv/templates/open_slots.html`, `my_tasks.html`, `message_volunteer.html`, `confirm.html`; `src/bbpv/views.py`, `page_not_found()` and the error pages | Some text differs from d05-01: the empty Open Slots screen says "There are no open slots right now. Please check again soon." (d05-01: "No open slots this week. Check back soon!"); empty My Tasks says "You haven't posted any upcoming tasks." (d05-01: "...any tasks yet."); S-9 has no "0 of 500 characters" counter; S-4 says "Signing up as" instead of "You'll appear as." After "Send" and "Yes, block," the app doesn't go back to the Roster as the user flows show. The "page not found" and "something went wrong" messages are written straight into the code, not in `wording.py`, and aren't in the list sent to the Designer (d08-01 Section 9). Also, a 500-character message with line breaks is refused, because browsers count each line break as one character but send it as two. | Small differences add up to confusion for volunteers, and messages outside `wording.py` would be missed when other languages are added (Spec Section 10). | d05-01 Sections 6, 7, 8, and 13; d08-02 Section 6, rule 5 | UI/UX Designer chat: confirm or update the wording; then Software Engineer chat: match it and move every message into `wording.py` | | |
| R-12 | Question | `src/bbpv/views.py`, `block_volunteer()` | When a volunteer is blocked, their existing sign-ups stay. The reviewer confirmed that they stay on the roster and will still get reminder emails. | Should a blocked volunteer still come to slots they already signed up for? The PRD says only that they "can't sign up again." | Documents don't say (PRD UC-7) | Stakeholders decide; if sign-ups should be removed, the Requirements chat updates UC-7, then SDET and Software Engineer chats | | |
| R-13 | Question | `src/bbpv/cli.py`, `send_reminders()`; `src/bbpv/wording.py`, `SIGNED_UP` | The reminder job runs once, at 6 p.m., for tomorrow's slots. Anyone who signs up after 6 p.m. for tomorrow, or for a slot later today, never gets a reminder, though the screen promises "We'll email you a reminder the day before." | Is that acceptable, or should late sign-ups get a reminder straight away, or the message change? | PRD UC-3 AC5 doesn't cover late sign-ups | Stakeholders decide; then UI/UX Designer chat (wording) or SDET and Software Engineer chats | | |
| R-14 | Question | `src/bbpv/cli.py` (`create-account`, `delete-account`); d06-01 Section 7.2 | Coordinator accounts can be created, and any account deleted, only by typing a command on the server. The System Administrator has no web page for this, and d06-01 gives them only read-only access to the live database. Also, the privacy notice says the System Administrator "can see your email," but emails are encrypted, so in practice they can't without the key. | Who adds a new coordinator, or deletes a volunteer's account when asked: Parks IT? Is that quick enough? And should the privacy notice be reworded so it's accurate? | Documents don't say | Stakeholders decide; then Initial Infrastructure (DevOps) chat with Parks IT, and UI/UX Designer chat for the notice | | |
| R-15 | Question | `src/bbpv/views.py`, `roster()`, `message_volunteer()`, `block_volunteer()` | Any coordinator can open any slot's roster (not just their own tasks), and can message or block any volunteer by username, even one who never signed up for their tasks. | Is that the intended trust level for every coordinator, including lead volunteers? | Documents don't say (Spec 11.1 says only "coordinators see usernames") | Stakeholders decide; if limited, the Design chat updates the Spec, then SDET and Software Engineer chats | | |
| R-16 | Note | `src/bbpv/__init__.py`, `load_user()`; `src/bbpv/views.py`, `message_volunteer()` and `block_volunteer()` | Pages are handed the whole account record, including the encrypted email and its scrambled copies. No page shows them, and they can't be read without the key. | Safe today, but a careless future change to a page could print the scrambled text. Handing pages only the username and role would remove the chance. | Reviewer's opinion | None needed; the Software Engineer chat may tidy this in a later change | | |
| R-17 | Note | `src/bbpv/privacy.py`, `EmailVault` | The scrambled copies used for sign-in and the block list are made from the same secret key that encrypts emails. | If that key is ever changed, no one can sign in and the block list stops working until every stored copy is remade. This should be written down before anyone tries it. | Reviewer's opinion | Software Engineer chat: add a short note to d08-02 Section 5 | | |
| R-18 | Note | `src/bbpv/__init__.py` (`DB_POOL_SIZE` defaults to 15); d06-01 Section 12 | Each copy of the app keeps up to 15 database connections unless the setting says otherwise. Parks IT runs 4 copies with a limit of 20 in all, so the setting must be 4, as d06-01 v1.2 says. Also, d06-01's table describes this in two ways that don't agree ("15 connections (60 in all)" and "set to 4"). | If the setting is ever left out, the app can run out of connections under load. | Reviewer's opinion | Initial Infrastructure (DevOps) chat: tidy the d06-01 wording; optionally, Software Engineer chat: a lower default | | |
| R-19 | Note | `src/bbpv/__init__.py`, `create_app()` (`create_all`) | The app creates its database tables the first time it starts, but has no way to change existing tables later. | Any future change to what's stored (for example, Phase 2 phone numbers) will need a careful, hand-written change to the live database. | Reviewer's opinion | None now; plan for it before Phase 2 | | |

## 4. Things Done Well

- **Email privacy holds where it matters.** Email addresses are stored
  only encrypted, decrypted in exactly one place (`send_email()`) and only
  to hand to the email service. No page, reply, error page, or sign-in
  cookie carries one; rosters, the block page, and S-10 show usernames
  only; coordinator messages go from the no-reply address with no
  reply-to address. The reviewer traced every page and email to confirm
  this.
- **The block list** stores only a scrambled copy of the standardized
  email, so `j.o.h.n+beach@...` and `john@...` match, and the block
  survives when the account is deleted.
- **Taking the last place** happens in a single database step (DD-5),
  with a database rule that places left can never go below zero, and a
  fast second tap shows a friendly message, not an error.
- **Sign-in links** are long and random, stored only in scrambled form,
  work once, and expire after 15 minutes; the sign-in reply never reveals
  who has an account.
- **Common attacks are handled:** text typed into forms can't run as code
  on a page; database requests can't be tricked by typed text; forms
  carry a protection token against forged submissions; plain HTTP is
  turned away, and the browser is told to use HTTPS (the secure version
  of a web address) from then on.
- **Every role is checked on every page,** and only the System
  Administrator can undo a block.
- **No secrets in the code:** every setting comes from the environment,
  and the app refuses to start without its keys.
- All 34 quick tests pass, and every message in d05-01 Section 9 is used
  word for word.

## 5. Questions for the Stakeholders

- **R-12:** Should a blocked volunteer's existing sign-ups be removed?
  Today they stay, and the volunteer still gets reminders.
- **R-13:** Should people who sign up after 6 p.m. the day before (or on
  the day) get a reminder, or should the "We'll email you a reminder"
  message change?
- **R-14:** Who creates coordinator accounts and deletes accounts on the
  live servers, given that it needs a server command? Should the privacy
  notice's line about the System Administrator seeing emails be reworded?
- **R-15:** Should every coordinator be able to see every roster and
  message or block any volunteer, or only for their own tasks?

## 6. Limits of This Review

- Reviewed the code as it was in the folder on 2026-10-25 (commit 4867cab
  plus later local changes). The folder had no Git history, so the
  reviewer could not see which parts were the later changes.
- The tests and the reviewer's own checks ran on Python 3.13 with the
  simple local database (SQLite), not on Python 3.12 or PostgreSQL 16 as
  on Parks IT's servers, and not against the real city email service.
- The 2 monkey tests and 2 browser tests (speed and accessibility) were
  not run; Playwright wasn't installed. Accessibility and the screens'
  look were not checked by eye, and the HTML mockups in `assets/` were
  not in the folder, so screens were compared with the d05-01 wireframes
  and text only.
- Claude Code's `/security-review` command wasn't available in this
  session; the security review was done by hand.
- Findings R-1, R-3, R-4, and R-12 were confirmed by running the app in a
  throwaway copy outside the project folder. R-6 and R-7 depend on how
  volunteers' email services and Parks IT's servers behave, which the
  reviewer couldn't check.
- Several approved documents carry dates later than this review (for
  example, d08-01 on 2026-12-11 and d06-01 v1.3 on 2027-01-20). The
  reviewer took them as the approved versions, as given.
- No one was available to ask the Mode A questions. The answers given
  were: review the folder as it is now; save as
  `docs/d08-04-code-review-claude.md`; check privacy of email addresses
  especially.
- An AI reviewer can miss problems or misjudge them. This report is one of
  two independent reviews, and a person decides on every finding.

## 7. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | 2026-10-25 | First version | Claude Code (a new, separate session), Claude Opus 5.5 |

---

**Hand-off note for the Tracking chat (Mode D):**

- Report: `docs/d08-04-code-review-claude.md`, by Claude Code (a new,
  separate session; Claude Opus 5.5).
- Verdict: **Ready after the Must-fix items.** 2 Must fix, 9 Should fix,
  4 Question, 4 Note.
- R-1: failed emails are never retried, and one failed reminder stops
  the rest of that day's reminders.
- R-2: tasks, slots, and sign-ups are never deleted after 12 months, as
  Spec Section 6 says.
- Recommendation: **Fix first.** Send R-1 and R-2 to the SDET chat (tests)
  and then the Software Engineer chat (R-2 could instead go to the Design
  chat to change the Spec). Decide on the Should-fix items and the four
  Questions, then sign off Step 8.
