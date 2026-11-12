I've checked R2-17's fix and run the quick tests (65 passed, 1 skipped). Here is the updated report.

# BeautifulBeachPark Volunteers: Code Review Report

**Document:** d08-04 · **Step:** 8, Implementation · **Version:** 1.3
· **Last updated:** 2026-11-11 · **Status:** Round 2 closed: every finding decided and done
· **Owner:** Code Reviewer (Claude Code, model Claude Opus 5.5)

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
> named in "Next step"), **Accept as is** (say why, in a few words),
> **Future Version** (worth doing, but not now), or **Ask** (you need to
> know more; ask the reviewer or the Software Engineer chat). A round ends
> when no Must-fix finding is left open; after that, a new Should-fix
> finding goes to Future Version unless you choose Fix. An AI reviewer can be wrong in both directions: it can
> miss a problem or report one that isn't there. That's why there are three
> independent reviews, and why the decision is yours.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Review round | 2 |
| Code reviewed | `src/` and `tests/` as they are in the folder on 2026-11-11 (commit a1185f6, with no uncommitted code changes) |
| Reviewer | Claude Code, model Claude Opus 5.5 (`claude-opus-5-5`) |
| Independent? | Yes. This is a new session that didn't write the code. I didn't read any other review report (`d08-04-code-review-codex.md`, `d08-04-code-review-claude-trial.md`, the untracked `d08-04-code-review-claude.md.new`, or `d08-05`), `src/REVIEW-GUIDE.md`, or d08-01 Section 7 and its Future Version list. |
| Documents checked against | d03-01 PRD v1.2; d04-01 Spec v1.2; d05-01 UI/UX v1.2; d06-01 Infrastructure v1.4; d07-01 Test Plan v1.4; d08-01 Implementation Record v1.1 (Sections 1 to 6); d08-02 Developer Guide (the header says v1.1, and the Change Log goes up to v1.2) |
| Review date | 2026-11-11 |
| Verdict | **Ready after the Must-fix items.** The privacy design is sound and every role check is in place. One promise in the PRD is broken: a message or description that has line breaks can be refused even though it is under the limit. |
| Findings | 1 Must fix · 7 Should fix · 2 Question · 3 Note |
| Re-review (v1.1) | 2026-11-11. I compared the uncommitted changes with commit a1185f6: `src/`, `tests/`, the new `src/bbpv/templates/sign_in_finish.html`, and PRD v1.3, Spec v1.3, UI/UX v1.3, Infrastructure v1.5, Test Plan v1.5, and Developer Guide v1.3. The same independence rules applied. |
| Re-review verdict | **Ready after the Must-fix items.** 7 of the 8 Fix findings are fixed, and both Question answers are carried out. R2-2 is only partly fixed: the reply is now the same, but a second try with the same username still shows whether an email has an account. That breaks the new PRD v1.3 UC-2 AC5 (new finding R2-14, Must fix). |
| New findings (v1.1) | 1 Must fix · 0 Should fix · 0 Question · 2 Note (R2-14 to R2-16) |
| Re-review 2 (v1.2) | 2026-11-11. I compared the uncommitted changes with commit a1185f6 again, and looked most closely at what changed after v1.1: the new account requests (Spec DD-13), the "Sign in" step that turns a request into an account, the email queue's new way of sending to someone with no account yet, the daily clean-up, T-02-02, T-02-07, and Test Plan v1.6. The same independence rules applied. |
| Re-review 2 verdict (v1.2) | **Ready.** R2-14 is fixed: no account is made, and no username is taken, until the email's owner presses "Sign in." So no number of tries shows who has an account, and R2-2 is now fixed too. No Must-fix finding is open. One new Should fix (R2-17) is for the person to decide, or to put on the Future Version list. |
| New findings (v1.2) | 0 Must fix · 1 Should fix · 0 Question · 0 Note (R2-17) |
| Re-review 3 (v1.3) | 2026-11-11. I compared the uncommitted changes with commit a1185f6 again, and looked most closely at the R2-17 fix: `request_account()`, `_finish_account_request()`, the `account_requests` table, Spec v1.3 Section 6 and DD-13, Test Plan v1.6 (T-02-08), and the test itself. The same independence rules applied. |
| Re-review 3 verdict (v1.3) | **Ready.** R2-17 is fixed: every request's link keeps working until one of them becomes the account, and then the others stop working. No Must-fix finding is open. One new Note (R2-18) about the Spec's Change Log. |
| New findings (v1.3) | 0 Must fix · 0 Should fix · 0 Question · 1 Note (R2-18) |

## 2. What Was Checked

| Area | What was checked | Result |
|---|---|---|
| Privacy and security | Spec Section 11: where emails are stored, decrypted, and shown; the scrambled (hashed) copies; sign-in links; secrets; protection against code typed into form fields, forged form submissions, and plain HTTP | No email reaches any page. Three Should fix: R2-2 and R2-3 (someone can find out whether an email address has an account) and R2-6 (the connection to the email service isn't checked) |
| Who may do what | Every page and request in `views.py`, against Spec 11.1 | No findings. Every page checks the role, and volunteers can cancel only their own sign-ups. One Question: R2-9 |
| PRD and Spec rules | UC-1 to UC-7 acceptance criteria; DD-5 to DD-9 | 1 Must fix (R2-1). DD-5 (last place), DD-7 (one-time link), and DD-9 (10 emails a day) are built as designed. One Question: R2-10 |
| Ready to move | d06-01 Section 5.1, row by row; settings from outside the code | Two Should fix: R2-5 (database connections) and R2-7 (no production web server named). Every setting comes from environment variables, and the app refuses to start without its secrets |
| Tests | Test Plan d07-01 v1.4 against `tests/` | Each test in the plan exists. One Should fix: R2-8 (the protection against forged forms is never tested). R2-1 to R2-5 also have no test. I couldn't run the tests (Section 6) |
| Nothing surprising | Data sent anywhere unexpected; libraries not listed in the Developer Guide; leftover debugging code | No findings. Libraries match d08-02 Section 7. Nothing is sent anywhere except the email service. No debugging code |
| Wording | `wording.py` against d05-01 Section 9 | Every message matches word for word. One Note: R2-13 |
| Built-in security scan | The same method as Claude Code's `/security-review`, applied by hand to all of `src/`, because `/security-review` only looks at changes and there were no code changes to look at. Each candidate was checked against the code | Nothing critical. Included: R2-2, R2-3, R2-6 (and R2-4, which is about reliability). Left out because they can't do real harm: forced sign-out with a link (`/sign-out` works by a simple visit), signing someone in to an account the attacker owns, no Content-Security-Policy header, and sign-in tokens appearing in web server logs (they work once and expire in 15 minutes) |
| Re-review, privacy and security (v1.1) | The new background sending, the "Finish signing in" page and its form token, the create-account path for an email in use, and the certificate check | One Must fix: R2-14 (the username shows whether an email has an account). Everything else is sound: the new page carries the form token, and no email reaches any page |
| Re-review, who may do what (v1.1) | `block_volunteer()` and `use_sign_in_link()` | No findings. Only coordinators can block; the "Sign in" button needs the form token |
| Re-review, PRD and Spec rules (v1.1) | PRD v1.3 UC-1, UC-2 3c and AC5, UC-6, UC-7; Spec v1.3 DD-10 to DD-12 | R2-14 (UC-2 AC5). One Note: R2-16 (blocking cancels sign-ups on every coordinator's tasks, and no one is told) |
| Re-review, ready to move (v1.1) | d06-01 v1.5 Section 5.1; Waitress; `SMTP_CA_FILE`; connection pool | No findings. The pool still can't grow past `DB_POOL_SIZE`, and emails no longer hold a connection |
| Re-review, tests (v1.1) | Test Plan v1.5 against `tests/`; I ran `pytest -m 'not monkey and not browser'` | 63 passed, 1 skipped (T-QR-04), 4 left out by design. One Note: R2-15 (T-QR-04 skips itself when Waitress is missing) |
| Re-review, nothing surprising (v1.1) | New library (Waitress) and the background threads | Waitress is listed in d08-02 Section 7 and `requirements.txt`. No debugging code |
| Re-review, wording (v1.1) | New and changed messages against d05-01 v1.3 Section 9 | Every new message matches word for word |
| Re-review 2, privacy and security (v1.2) | `create_account()`, `request_account()`, `_finish_account_request()`, the "Open sign-in link" check, and `deliver()` for an email with no account yet. I tried the two-try check from R2-14 and other ways to tell the two cases apart: the reply, the username, the daily limit of 10 emails, and the time taken | No findings. Every path gives the same reply, and nothing an outsider can see changes until the email's owner presses "Sign in." The new request's email is stored encrypted, sent only by `deliver()`, and removed when used or by the daily clean-up. One Should fix about reliability: R2-17 |
| Re-review 2, who may do what (v1.2) | The "Sign in" button for an account request; the block list at that moment | No findings. A request can't become an account if the email was blocked in the meantime, and only the holder of the emailed link can finish it |
| Re-review 2, PRD and Spec rules (v1.2) | PRD v1.3 UC-2 steps 3 and 4, 3c, 4a, and AC5; Spec v1.3 Sections 6 and 7, DD-7, DD-9, and DD-13; d05-01 v1.3 S-1 and S-2 | Built as written: the account and username are made only at "Sign in," the request is used up in one step (DD-7), the daily limit counts requests too (DD-9), and an expired request sends a new link. R2-17: a second request for the same email makes the first link stop working |
| Re-review 2, ready to move (v1.2) | The email queue table changed (a new column and a rule), and there is a new table | No findings. The app can't change an existing table (R2-12). d08-02 v1.3 tells developers to delete the local database once. The live database doesn't exist yet, so nothing is lost before Step 9 |
| Re-review 2, tests (v1.2) | Test Plan v1.6 against `tests/`; I ran `pytest -m 'not monkey and not browser'` again | 64 passed, 1 skipped (T-QR-04, R2-15), 4 left out by design. T-02-07 runs the two-try check from R2-14 and the "username taken first" case (UC-2 4a). T-02-06 now matches the new design. No test covers R2-17 |
| Re-review 2, nothing surprising (v1.2) | New code since v1.1 | No new libraries, no data sent anywhere new, no debugging code |
| Re-review 2, wording (v1.2) | Messages on the new paths | All come from d05-01 Section 9. "This link isn't valid. Please ask for a new one below." can't be followed by someone with no account yet (R2-17) |
| Re-review 3, privacy and security (v1.3) | Several live requests for one email: whether they show who has an account, whether someone else's request can take over a person's account, and the daily limit | No findings. More than one request for an email changes nothing an outsider can see. Each link still goes only to the email's owner, and the limit of 10 emails a day still caps how many requests one email can have |
| Re-review 3, who may do what (v1.3) | `_finish_account_request()` when another request for the same email has already become the account; the block list check | No findings. If the account already exists, the link signs its owner in to it and doesn't make a second one. The block list is still checked first |
| Re-review 3, PRD and Spec rules (v1.3) | Spec v1.3 Section 6 ("An email may have several at once") and DD-13; DD-7 (each link used once); DD-9 (limit) | Built as written. One Note: R2-18 (the Spec was changed for R2-17 without a Change Log row) |
| Re-review 3, ready to move (v1.3) | The `account_requests` table; two "Sign in" presses at the same moment for one email on PostgreSQL | No findings. The table is unchanged except for its comment. In my reading of the code, two presses at the same moment can't make two accounts. At worst, one of the two people sees "Something went wrong" (Section 6) |
| Re-review 3, tests (v1.3) | Test Plan v1.6 T-02-08 against `tests/test_uc2_create_account.py`; I ran `pytest -m 'not monkey and not browser'` again | 65 passed, 1 skipped (T-QR-04, R2-15), 4 left out by design. T-02-08 checks that the first of two emails still works, that the second then stops working, and that only one account is made |
| Re-review 3, nothing surprising (v1.3) | Code changed since v1.2 | No new libraries, no data sent anywhere new, no debugging code |
| Re-review 3, wording (v1.3) | "This link isn't valid. Please ask for a new one below." on a request's link | It now appears only after the account exists, so asking for a new link on the sign-in page works. The v1.2 concern is gone |

## 3. Findings

IDs start at R2- so that they don't get mixed up with round 1's R-numbers.

| ID | Seriousness | Where | What's wrong, in plain language | Why it matters | Breaks | Next step | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|
| R2-1 | Must fix | `src/bbpv/views.py`, `message_volunteer()` and `_check_task()` | When a browser sends a form, it counts each line break as 2 characters, but the on-screen counter counts it as 1. The server counts what it receives, so a 495-character message with 6 line breaks is refused with "Messages can be up to 500 characters," while the counter shows "495 of 500." Task descriptions have the same problem with their 1,000-character limit. | Coordinators get a refusal that contradicts the counter in front of them, and have to guess what to cut. | PRD UC-6 AC2; UC-1 AC3; d05-01 S-9 counter | SDET chat: add tests that send a 500-character message and a 1,000-character description, both with line breaks in the browser's form; then Software Engineer chat: count each line break as one character before checking the length | Fix | Park Manager, 2026-11-11 |
| R2-2 | Should fix | `views.py`, `create_account()` | If someone enters an email that already has an account, the page says "We couldn't create this account." For a new email, it creates the account. So anyone can type someone else's email address and find out whether that person volunteers at the park. | This undoes the Spec's stated reason for always giving the same sign-in reply ("so no one can test which emails exist"). The documents don't say what should happen when an email is already in use. | Spec 7 ("Send sign-in link" row, its stated purpose); reviewer's opinion for this page | UI/UX Designer: decide the reply (for example, the same "Check your email" reply, with a sign-in link emailed to the existing owner); then SDET chat: add a test; Software Engineer chat: fix | Fix | Park Manager, 2026-11-11 |
| R2-3 | Should fix | `views.py`, `sign_in()` and `send_now()` | For an email that has an account, the sign-in page waits while the email is sent, up to 5 seconds. For an unknown email, it answers at once. The words are the same, but the timing shows whether the email has an account. | Same harm as R2-2: someone with a stopwatch or a simple script can test email addresses. | Spec 7 ("always, so no one can test which emails exist"), DD-3 | SDET chat: add a test that the two replies take about the same time; then Software Engineer chat: send the email entirely in the background, or wait the same time either way | Fix | Park Manager, 2026-11-11 |
| R2-4 | Should fix | `views.py`, `use_sign_in_link()` | The sign-in link signs you in and is used up as soon as the web address is opened. Many work and school email systems open every link in an email to check it for danger before the person sees it. That check uses up the link, and the volunteer then sees "This link isn't valid." | Volunteers who use such email systems may never be able to sign in, with no clue why. | Reviewer's opinion (DD-7 is kept either way) | SDET chat: add a test that opening the link doesn't sign in until a button is pressed; then Software Engineer chat: have the link open a page with a "Sign in" button, and use the link up only when the button is pressed | Fix | Park Manager, 2026-11-11 |
| R2-5 | Should fix | `views.py`, `send_due_emails()` (the part that calls `deliver()`) | While an email is being sent, the app keeps one of its few database connections open for the whole send, which can take up to 20 seconds when the email service is slow. On the live servers each copy of the app has only 4 connections (d06-01 v1.2). | If the city email service is slow, a few sign-ins at once can use up every connection. Everyone else's pages then wait or fail, which is the opposite of DD-6's promise that pages never wait for other people's emails. | Spec DD-6; d06-01 5.1 (database connections) | SDET chat: add a test with a slow email service and a pool of 1 connection; then Software Engineer chat: read the address and close the connection before sending | Fix (also closes round 1's R-18, moved off the Future Version list) | Park Manager, 2026-11-11 |
| R2-6 | Should fix | `src/bbpv/mail.py`, `send()` | The connection to the city email service is encrypted, but the app doesn't check that it is really talking to the city's server (no certificate check). | Someone who could get onto Parks IT's network could pose as the email service and read sign-in links, the email service password, and volunteers' addresses. The risk is low because that network is private. | d06-01 7.1 ("Encrypted"); Spec 11.1 | Software Engineer chat: turn on the certificate check (one line); DevOps chat: confirm the city email service's certificate with Parks IT | Fix | Park Manager, 2026-11-11 |
| R2-7 | Should fix | `src/requirements.txt`; d08-02 Section 5.1, step 3 | The guide tells Parks IT to "start the app as a service" but doesn't name a production web server, and none is in the library list. The only start command it gives is `flask run`, which Flask itself says is for development only. | Parks IT may run the live app on the development server, which is slower and less safe under real traffic. It's also why the move might need more than settings. | d06-01 5.1 ("How software is installed and started") | Software Engineer chat: choose a production server, add it to `requirements.txt` and d08-02 Sections 5.1 and 7; DevOps chat: confirm it with Parks IT | Fix | Park Manager, 2026-11-11 |
| R2-8 | Should fix | `src/bbpv/__init__.py`, `check_form_token()`; `tests/conftest.py` | The protection against forged form submissions works, but it's switched off whenever the tests run. No test checks it. | If a later change breaks this protection, every test would still pass. Another website could then make a signed-in coordinator block a volunteer, or make a volunteer cancel. | Reviewer's opinion (a gap in d07-01) | SDET chat: add a test that runs with the protection on and checks that a form without the token is refused | Fix | Park Manager, 2026-11-11 |
| R2-9 | Question | `views.py`, `block_volunteer()` | Blocking someone stops new sign-ups, but their existing upcoming sign-ups stay, and they still get reminders for them. | A coordinator may expect "Block" to also remove the person from slots they already have. The PRD and Spec don't say either way. | — (the documents don't say) | Stakeholders: decide. If they say "remove," it goes to the Product Manager (PRD), then the SDET and Software Engineer chats | Yes: blocking also cancels the person's upcoming sign-ups and gives the places back | Park Manager, 2026-11-11 |
| R2-10 | Question | `src/bbpv/cli.py`, `clean_up()` | The Spec keeps each scrambled sign-in email count for 24 hours. The clean-up that deletes them runs once a day, so a record can stay for up to about 48 hours. | It's harmless, because the copy is scrambled, but the code doesn't do exactly what the Spec says. | Spec 6 ("Sign-in email count … 24 hours") | Stakeholders: accept, and ask the Architect to say "deleted daily, after 24 hours," or send to the Software Engineer chat to delete old records at each sign-in | Yes: accept "deleted daily, after 24 hours"; the Spec's wording changes | Park Manager, 2026-11-11 |
| R2-11 | Note | `src/bbpv/privacy.py`, `EmailVault.__init__()` | The key used for the scrambled copies is made from the email encryption key. Changing that key later, or losing it, makes every account lookup and the whole block list stop working. | It's fine as built, but the people running the app need to know. | — | Software Engineer chat: one line in d08-02 Section 5: "never change or lose `EMAIL_ENCRYPTION_KEY`" | Do it: one line in d08-02 Section 5 | Park Manager, 2026-11-11 |
| R2-12 | Note | `src/bbpv/__init__.py`, `create_app()` (`create_all`) | The app creates its database tables when it first starts, but it can't change existing tables later. | Any change to the tables in Step 10 will need manual steps on the live database. | — | None now; keep in mind for Step 10 | Noted for Step 10 | Park Manager, 2026-11-11 |
| R2-13 | Note | `views.py`, `undo_block()`; `_500()` | "Block removed." appears even when nothing was removed, for example after a double-click. The mockups' "We couldn't load slots…" and "We couldn't undo this block…" messages aren't used; a general "Something went wrong on our side…" message appears instead. | Minor. The wording still comes from d05-01 Section 9. | d05-01 Section 8 (mockup error states) | None, unless the Designer wants the specific messages | Noted; no change | Park Manager, 2026-11-11 |
| R2-14 | Must fix | `views.py`, `create_account()` (the "email already has an account" path); `tests/test_uc2_create_account.py`, T-02-06 | The reply is now the same either way, but the username isn't. For a new email, the account is made and the username is taken. For an email that already has an account, nothing is made and the username stays free. So someone can test an email in two tries. First, they create an account with a made-up username (say "probe_4821") and the email they want to test. Then they try "probe_4821" again with their own email. If they're told "That username is taken," the email had no account before. If not, it already had one. Test T-02-06 checks that the username stays free, so the tests make sure this leak stays. | Anyone can still find out whether a neighbor, coworker, or ex volunteers at the park. This is exactly what R2-2 was meant to stop. Each test of a new email also creates an account for that person and sends them an unexpected email. | PRD v1.3 UC-2 AC5 ("Creating an account never shows whether an email already has one"); Spec v1.3 Section 7 ("Create account" row) | Product Manager and Software Architect: choose a fix. One option is to make no account, and take no username, until the person presses "Sign in" on the emailed link. Then a try changes nothing either way. Then SDET chat: change T-02-06 and add a test of the two-try check; Software Engineer chat: fix. Or the stakeholders accept the risk, and the Product Manager rewords AC5 to promise only that the reply is the same | Fix: make the account, and take the username, only when the emailed "Sign in" button is pressed | Park Manager, 2026-11-11 |
| R2-15 | Note | `tests/test_operations.py`, T-QR-04 | The test for the production web server skips itself when Waitress isn't installed, so a run can still look fine. In my run it was skipped, because the project's local environment doesn't have Waitress yet. | Nothing is wrong with the code, but R2-7's test hasn't really run until Waitress is installed (`pip install -r src/requirements.txt`). In d07-02, a skipped T-QR-04 should count as not run. | — (reviewer's opinion) | SDET chat: make sure T-QR-04 shows as passed, not skipped, in the next full run on d07-02 | Do it: Waitress installed for the next full run | Park Manager, 2026-11-11 |
| R2-16 | Note | `views.py`, `block_volunteer()` | Blocking cancels the volunteer's upcoming sign-ups on every task, including other coordinators' tasks. Neither the volunteer nor those other coordinators are told. Their places just open again. | This is what PRD v1.3 UC-7 asks for. Still, another coordinator may find a slot short of people they had counted on, and won't know why. | — (works as the PRD says) | None, unless the stakeholders want a notice, which would go to the Product Manager | No notice: works as PRD v1.3 says | Park Manager, 2026-11-11 |
| R2-17 | Should fix | `views.py`, `request_account()` (its first step removes any earlier request for the same email); `_finish_account_request()` | The app keeps only one account request per email. If the Create Account form is sent twice for the same email, the newer request replaces the older one, and the link in the first email stops working. This can happen with a double tap on "Create account," a second try because the first email is slow to arrive, or someone else typing that email. Opening the first link shows "This link isn't valid. Please ask for a new one below." But asking on the sign-in page sends nothing, because there is no account yet. The page still says "Check your email," and no email comes. Also, if someone else sends the form with your email, the newest email greets you with the username they chose, and pressing "Sign in" makes your account with that username. | A new volunteer who opens the older email can get stuck and give up, with no clue that they need to use the newer email or start over. This is a reliability problem, not a privacy one: it doesn't show who has an account. The Spec's "one per email" is built as designed. | Reviewer's opinion. Spec v1.3 Section 6 says "One per email," so the code matches the Spec. d05-01 Section 9's "Please ask for a new one below" can't help someone who has no account yet | Stakeholders: decide (Fix, or Future Version). If Fix: Software Architect: choose a fix, for example keep every request's link working until one is used, then remove the others (the daily limit of 10 still applies); then SDET chat: add a test that the first of two emails still works; Software Engineer chat: fix | Fix | Park Manager, 2026-11-11 |
| R2-18 | Note | `docs/d04-01-spec.md`, Section 6 ("Account request" row), DD-13, and the Change Log (Section 15) | For R2-17, the Spec's Section 6 and DD-13 were changed from "one per email" to "an email may have several at once." The Spec still says v1.3, and its v1.3 Change Log row names R2-10 and R2-14 but not R2-17. | Someone comparing Spec versions later won't see that this rule changed, or why. The code matches the Spec as it reads now. | d04-01 Change Log practice (reviewer's opinion; no rule is broken in the code) | Software Architect: add R2-17 to the Spec's Change Log (or raise it to v1.4) when the Spec is next approved | Done: R2-17 added to the Spec's v1.3 Change Log row | Park Manager, 2026-11-12 |

### Re-Review, 2026-11-11

I checked each Fix finding and each Question answered Yes against the uncommitted changes since commit a1185f6. I also ran `pytest -m 'not monkey and not browser'`: 63 passed, 1 skipped (T-QR-04, see R2-15), and 4 left out by design (the monkey and browser tests).

| ID | Result | What I found |
|---|---|---|
| R2-1 | **Fixed** | `one_line_break()` turns each two-character line break into one before the message and description are checked. PRD v1.3, Spec v1.3, and d05-01 v1.3 say so. T-01-08 and T-06-04 send line breaks the way a browser does, and both pass. |
| R2-2 | **Partly fixed** | The reply is now the same "Check your email." The owner gets a sign-in link and no second account is made (PRD v1.3 UC-2 3c; T-02-06 passes). But the username is taken only when the email is new, so a second try still shows whether an email has an account. That's new finding R2-14. |
| R2-3 | **Fixed** | `sign_in()` and `create_account()` now call `send_in_background()` and answer without waiting (Spec DD-10). T-SEC-10 checks all four replies come back in under half a second with a slow email service, and passes. The two paths still do slightly different database work, a difference of milliseconds that I didn't measure (Section 6). |
| R2-4 | **Fixed** | Opening the link now only shows "Finish signing in" with a "Sign in" button (`sign_in_finish.html`). Only pressing the button uses the link up, still in one step (DD-7, DD-11). The button's form carries the token against forged forms. T-SEC-09 passes. |
| R2-5 | **Fixed** | `deliver()` now reads the address with its own short database step and closes it before sending (DD-12). T-EM-08 counts the connections in use during each send, finds none, and passes. The pool still can't grow past `DB_POOL_SIZE`. |
| R2-6 | **Fixed** | `mail.send()` now checks the email service's certificate and its name, with an optional `SMTP_CA_FILE` (d06-01 v1.5, d08-02 Section 5). T-SEC-11 passes. Parks IT still has to confirm the certificate (DevOps chat). |
| R2-7 | **Fixed** | Waitress is in `requirements.txt`, d08-02 Sections 5.1 and 7, and d06-01 v1.5, with a start command and "never `flask run`." T-QR-04 exists, but it was skipped in my run (R2-15). Parks IT still has to confirm Waitress. |
| R2-8 | **Fixed** | A new setting, `CHECK_FORM_TOKENS`, turns the protection on in a test. It can't be set from the live server's environment, so it can't switch the protection off there. T-SEC-12 checks the sign-in form, the create-account form, and the "Sign in" button with and without their token, and passes. |
| R2-9 (Yes) | **Fixed** | `block_volunteer()` now cancels the person's sign-ups for slots that haven't started and gives the places back, in the same database step as the block. The confirm box wording matches d05-01 v1.3. T-07-05 checks the rosters, the places, and that no reminder goes out, and passes. See Note R2-16. |
| R2-10 (Yes) | **Fixed** | Spec v1.3 Section 6 now says "kept up to about 48 hours." The code is unchanged, as decided. |

The Notes stay as they are. Even so, the Developer Guide v1.3 now carries R2-11's warning about `EMAIL_ENCRYPTION_KEY` and R2-12's warning about table changes.

### Re-Review 2, 2026-11-11

I checked the Fix findings whose latest result wasn't "Fixed" (R2-2 and R2-14) against the uncommitted changes since commit a1185f6, and looked over the rest of the changed code again. I ran `pytest -m 'not monkey and not browser'`: 64 passed, 1 skipped (T-QR-04, see R2-15), and 4 left out by design.

| ID | Result | What I found |
|---|---|---|
| R2-14 | **Fixed** | `create_account()` no longer makes an account. For a new email, it saves only an account request (`request_account()`, Spec DD-13). A request doesn't hold the username, so the username check sees only real accounts. The account is made, and the username taken, only when the email's owner presses "Sign in" (`_finish_account_request()`). The request is used up in one step (DD-7). If someone took the username first, the owner sees "That username is taken" (UC-2 4a). I walked through the two-try check: whether or not the first email has an account, the second try gives "Check your email," and nothing changes. The daily limit of 10 emails counts both paths the same way, and both answer straight away (DD-10). T-02-07 runs this check and passes. T-02-06 now expects the new design and passes. PRD v1.3, Spec v1.3, d05-01 v1.3, and Test Plan v1.6 match the code. |
| R2-2 | **Fixed** | What was left of R2-2 was R2-14, which is now fixed. Creating an account with an email that already has one gives the same reply, sends the owner a sign-in link, makes no second account, and leaves no trace an outsider can see. |

New in this look: R2-17 (Should fix). Only one request is kept per email, so a second try makes the first email's link stop working. Since no Must-fix finding is open, the round can end. R2-17 goes on the Future Version list unless the person chooses Fix.

### Re-Review 3, 2026-11-11

I checked the one Fix finding whose latest result wasn't "Fixed" (R2-17) against the uncommitted changes since commit a1185f6, and looked over the rest of the changed code and documents again. I ran `pytest -m 'not monkey and not browser'`: 65 passed, 1 skipped (T-QR-04, see R2-15), and 4 left out by design.

| ID | Result | What I found |
|---|---|---|
| R2-17 | **Fixed** | `request_account()` no longer removes earlier requests for the same email. Each request has its own link, and each link works until it is used or expires. When one link's "Sign in" makes the account, `_finish_account_request()` removes the email's other requests in the same step, so their links then show "This link isn't valid." The person can then ask for a new link on the sign-in page, because the account now exists. If an account for that email already exists when a link is used, the link signs its owner in to it and makes no second account. The daily limit of 10 emails still applies, so one email can't have more than 10 requests a day, and the daily clean-up removes expired ones. Spec v1.3 Section 6 and DD-13 now describe this (see Note R2-18). T-02-08 sends the form twice, uses the first link, checks that the second then stops working, and checks that only one account exists. It passes. If someone else sends the form with your email, you now get your own email's link too, and can use whichever one has the username you chose. |

New in this look: R2-18 (Note). The Spec's Change Log doesn't mention the R2-17 change. No Must-fix finding is open, so round 2 stays closed.

## 4. Things Done Well

- Email addresses are decrypted in exactly one place (`deliver()`), and only to send an email. No page template ever receives one. Lookups and the block list use keyed, scrambled copies.
- Sign-in links are stored only in scrambled form. A link is used up in a single database step (DD-7), and the last place in a slot is taken in a single step, backed by database rules (DD-5).
- Every page checks the role. Volunteers can cancel only their own sign-ups, and only the System Administrator can undo a block.
- Every form carries a token against forged submissions, checked in a way that doesn't leak timing. Session cookies are HTTPS-only and can't be read by scripts. Plain HTTP is redirected, and HSTS (an instruction to browsers to always use HTTPS) is set.
- Everything typed into a form is shown safely: no page turns off the template's automatic escaping.
- The app refuses to start without its secrets. The pretend inbox can't run against the live database. Reasons for failed emails never include an address.
- Re-review: each fix came with its documents (PRD, Spec, UI/UX, Infrastructure, Test Plan, Developer Guide) and a test that was written for it. The background email senders are tracked so the tests can wait for them, and each send still claims its email first, so no email goes out twice.
- Re-review 2: the R2-14 fix closes the leak at its root: nothing an outsider can see changes until the email's owner acts. The new request keeps the same protections as an account: the email is encrypted, the link is stored scrambled and works once, the block list is checked again at "Sign in," and the daily clean-up removes old requests. The test T-02-07 follows the attack step by step.
- Re-review 3: the R2-17 fix is small and keeps every earlier protection. The other requests are removed in the same database step that makes the account, so a later link can't make a second account, and the existing daily limit already caps how many requests can pile up.

## 5. Questions for the Stakeholders

- **R2-9:** Should blocking a volunteer also remove their upcoming sign-ups? Right now they stay on rosters and still get reminders.
- **R2-10:** Is "kept for about 24 to 48 hours, deleted daily" acceptable for the scrambled sign-in counts, or must it be exactly 24 hours?
- **R2-14 (re-review):** To keep the PRD's promise that creating an account never shows who has one, should the app wait until the emailed "Sign in" button is pressed before it makes the account and takes the username? Or do you accept the risk and soften the promise?

## 6. Limits of This Review

- **The tests weren't run.** My tools weren't allowed to run `pytest` in this session, so I couldn't confirm that every test passes. Test results come from d08-01 Section 1 (58 of 58, Run 11).
- R2-1 is based on how browsers send line breaks under the HTML standard. I didn't confirm it in a real browser. R2-3 and R2-5 are based on reading the code, not on measuring.
- I didn't run the app or check the live servers, Parks IT's web server, or the city email service. I didn't review the mockups, the style sheet, or accessibility.
- The code reviewed is what was in the folder on 2026-11-11 (commit a1185f6). I didn't open the untracked file `docs/d08-04-code-review-claude.md.new`, because it may be another review.
- I was started with written instructions and couldn't ask questions, so I assumed:
  - The version to review is what's in the folder now.
  - This is round 2.
  - The report is given as my final answer rather than saved.
- An AI reviewer can miss problems or misjudge them. This report is one of three independent review rounds, and a person decides on every finding.
- **Re-review (v1.1):**
  - This time I ran the quick tests with the project's own Python environment: 63 passed and 1 was skipped (T-QR-04, because Waitress isn't installed locally). I didn't run the 2 monkey tests or the 2 browser tests (T-QR-01 and T-QR-02), which now press the new "Sign in" button. So I can't confirm those pass, or that the app starts under Waitress.
  - I reviewed only what changed since commit a1185f6, as asked. I didn't read d07-02 or d08-01, which also changed.
  - I didn't measure the small time difference between an email with an account and one without (R2-3). I judged it too small to matter over the internet, but I didn't prove it.
  - R2-14 comes from reading the code and T-02-06. I didn't try it against a running app.
  - I was started with written instructions and couldn't ask questions. I assumed that the version to compare with is commit a1185f6, and that I should give the report as my final answer rather than save it.
- **Re-review 2 (v1.2):**
  - I ran the quick tests again: 64 passed and 1 was skipped. T-QR-04 is still skipped, because Waitress still isn't installed locally (R2-15). I didn't run the monkey or browser tests, so I can't confirm that the browser tests pass with the new account flow, or that the app starts under Waitress.
  - I checked R2-14 by reading the code and running T-02-07, not by trying it against a running app. I looked at the four signals I could think of (reply, username, daily limit, time taken). There may be others I didn't think of.
  - Two requests sent at the same moment for the same email rely on the database refusing the second one. The tests use SQLite. I didn't test this on PostgreSQL, the live database.
  - R2-17 comes from reading the code. I didn't try it with a real email inbox.
  - I was started with written instructions and couldn't ask questions. I assumed the same as in v1.1: compare with commit a1185f6, and give the report as my final answer.
- **Re-review 3 (v1.3):**
  - I ran the quick tests again: 65 passed and 1 was skipped. T-QR-04 is still skipped, because Waitress still isn't installed locally (R2-15). I didn't run the monkey or browser tests.
  - Without a saved copy of the v1.2 code, I couldn't separate exactly what changed after v1.2. So I compared everything with commit a1185f6 again and looked most closely at the R2-17 code, its test, and its documents.
  - I reasoned through what happens if two different links for the same email have "Sign in" pressed at the same moment on PostgreSQL. The accounts table doesn't stop two accounts with the same email by itself. In my reading, the database's row locks still let only one account be made, and the other press either signs in to that account, shows "This link isn't valid," or shows "Something went wrong." The person can then sign in normally. The tests use SQLite, which handles one change at a time, so this wasn't tested on PostgreSQL. A person would rarely press two links within a split second.
  - I was started with written instructions and couldn't ask questions. I assumed the same as before: compare with commit a1185f6, and give the report as my final answer.

## 7. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | 2026-11-11 | First version | Claude Code (Claude Opus 5.5) |
| 1.0 | 2026-11-11 | Decisions filled in: 8 Fix (R2-1 to R2-8), 2 Questions answered Yes (R2-9, R2-10), Notes acknowledged. Report text unchanged | Park Manager (recorded by Claude) |
| 1.1 | 2026-11-11 | Re-review (Mode E) of the changes since commit a1185f6: R2-1, R2-3 to R2-10 fixed; R2-2 partly fixed. New findings R2-14 (Must fix), R2-15 and R2-16 (Notes). Overview, What Was Checked, Questions, and Limits extended; quick tests run (63 passed, 1 skipped) | Claude Code (Claude Opus 5.5) |
| 1.1 | 2026-11-11 | Decisions filled in: R2-14 Fix (account made only at sign-in); R2-15 do it; R2-16 no notice. Report text unchanged | Park Manager (recorded by Claude) |
| 1.2 | 2026-11-11 | Re-review 2 (Mode E): R2-14 fixed, so R2-2 is now fixed too. New finding R2-17 (Should fix). Overview, What Was Checked, Things Done Well, and Limits extended; quick tests run (64 passed, 1 skipped) | Claude Code (Claude Opus 5.5) |
| 1.2 | 2026-11-11 | Decision filled in: R2-17 Fix. Report text unchanged | Park Manager (recorded by Claude) |
| 1.3 | 2026-11-11 | Re-review 3 (Mode E): R2-17 fixed. New finding R2-18 (Note). Overview, What Was Checked, Things Done Well, and Limits extended; quick tests run (65 passed, 1 skipped) | Claude Code (Claude Opus 5.5) |
| 1.3 | 2026-11-12 | R2-18 done (Spec Change Log). Round 2 closed. Report text unchanged | Park Manager (recorded by Claude) |

---

**Hand-off note for the Tracking chat**

- **Report:** `docs/d08-04-code-review-claude.md` (round 2), by Claude Code, model Claude Opus 5.5.
- **Verdict:** Ready after the Must-fix items.
- **Findings:** 1 Must fix, 7 Should fix, 2 Question, 3 Note.
- **Must fix:**
  - R2-1: line breaks count as two characters on the server, so messages and descriptions under the limit can be refused (PRD UC-6 AC2, UC-1 AC3).
- **Recommendation: Fix first.**
  - R2-1: SDET chat (test), then Software Engineer chat (fix).
  - After that, decide on the Should-fix items:
    - R2-2: UI/UX Designer, then SDET and Software Engineer chats.
    - R2-3 to R2-5: SDET, then Software Engineer chat.
    - R2-6: Software Engineer and DevOps chats.
    - R2-7: Software Engineer and DevOps chats.
    - R2-8: SDET chat.
  - The stakeholders should answer R2-9 and R2-10.
  - Then re-review (Mode E), and go on to round 3, the hands-on review.
- **Limit:** the tests weren't run in this review.

---

**Hand-off note for the Tracking chat (re-review, v1.1, 2026-11-11)**

- **Report:** `docs/d08-04-code-review-claude.md` v1.1 (round 2 re-review), by Claude Code, model Claude Opus 5.5.
- **Verdict:** Ready after the Must-fix items.
- **Re-review results:** 9 fixed (R2-1, R2-3 to R2-8, and the answers to R2-9 and R2-10); 1 partly fixed (R2-2); none not fixed.
- **New findings:** 1 Must fix, 0 Should fix, 0 Question, 2 Note (R2-14 to R2-16).
- **Must fix:**
  - R2-14: after a failed try, the username is still free only if the email already had an account, so two tries show who has an account (PRD v1.3 UC-2 AC5).
- **Recommendation: Fix first.**
  - R2-14: Product Manager and Software Architect choose the fix (for example, make the account only when the emailed "Sign in" button is pressed), or the stakeholders accept the risk and the Product Manager rewords AC5. Then SDET chat (change T-02-06 and add a two-try test), then Software Engineer chat (fix).
  - R2-15: SDET chat should make sure T-QR-04 actually runs (Waitress installed) in the next full run.
  - R2-16: no action, unless the stakeholders want blocked volunteers or other coordinators told.
  - Still open with the DevOps chat: Parks IT to confirm Waitress (R2-7) and the email service's certificate (R2-6).
  - Then a short re-review of R2-14 (Mode E), and go on to round 3, the hands-on review.
- **Tests:** quick tests run, 63 passed and 1 skipped (T-QR-04). The monkey and browser tests weren't run.

---

**Hand-off note for the Tracking chat (re-review 2, v1.2, 2026-11-11)**

- **Report:** `docs/d08-04-code-review-claude.md` v1.2 (round 2, second re-review), by Claude Code, model Claude Opus 5.5.
- **Verdict:** Ready. No Must-fix finding is open, so round 2 can end.
- **Re-review results:** 2 fixed (R2-14, and with it R2-2); none partly fixed; none not fixed. All 8 Fix findings and both Question answers from round 2 are now fixed.
- **New findings:** 0 Must fix, 1 Should fix, 0 Question, 0 Note (R2-17).
- **Must fix:** none.
- **Recommendation: Decide on the findings, then sign off Step 8** once round 3 is done.
  - R2-17 (only one account request per email, so a second try makes the first email's link stop working): the person decides. It goes on the Future Version list unless they choose Fix. If Fix: Software Architect, then SDET chat (test), then Software Engineer chat (fix).
  - R2-15: SDET chat should still make sure T-QR-04 actually runs (Waitress installed) in the next full run. It was skipped again here.
  - Still open with the DevOps chat: Parks IT to confirm Waitress (R2-7) and the email service's certificate (R2-6).
  - Then go on to round 3, the hands-on review.
- **Tests:** quick tests run, 64 passed and 1 skipped (T-QR-04). The monkey and browser tests weren't run.

---

**Hand-off note for the Tracking chat (re-review 3, v1.3, 2026-11-11)**

- **Report:** `docs/d08-04-code-review-claude.md` v1.3 (round 2, third re-review), by Claude Code, model Claude Opus 5.5.
- **Verdict:** Ready. No Must-fix finding is open, and round 2 stays closed.
- **Re-review results:** 1 fixed (R2-17); none partly fixed; none not fixed. Every round 2 finding marked Fix, and both Question answers, are now fixed.
- **New findings:** 0 Must fix, 0 Should fix, 0 Question, 1 Note (R2-18: the Spec's Change Log doesn't mention the R2-17 change).
- **Must fix:** none.
- **Recommendation: Decide on the findings, then sign off Step 8** once round 3 is done.
  - R2-18: the person notes it. If they want, the Software Architect can add R2-17 to the Spec's Change Log when the Spec is next approved.
  - R2-15: SDET chat should still make sure T-QR-04 actually runs (Waitress installed) in the next full run. It was skipped again here.
  - Still open with the DevOps chat: Parks IT to confirm Waitress (R2-7) and the email service's certificate (R2-6).
  - Then go on to round 3, the hands-on review.
- **Tests:** quick tests run, 65 passed and 1 skipped (T-QR-04). The monkey and browser tests weren't run.
