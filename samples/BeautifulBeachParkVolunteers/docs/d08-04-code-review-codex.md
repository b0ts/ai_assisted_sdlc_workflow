# BeautifulBeachPark Volunteers: Code Review Report

**Document:** d08-04 · **Step:** 8, Implementation · **Version:** 1.3  
· **Last updated:** 2026-11-11 · **Status:** Decided; round 1 closed  
· **Owner:** Code Reviewer (Codex, GPT-6)

> **How to Read This Report**
>
> You don't need to read the code. Start with the **verdict** in the Overview, then read each row in **Findings**:
>
> - **Must fix** means the code breaks a promise in the approved documents or puts people's information at risk. These normally get "Fix."
> - **Should fix** is a real risk the documents didn't ask about. Decide whether it's worth the time now or in a later phase.
> - **Question** is something only the stakeholders can decide.
> - **Note** needs no action.
>
> For each finding, write your **Decision**: **Fix** (send it to the chat named in "Next step"), **Accept as is** (say why, in a few words), or **Ask** (you need to know more; ask the reviewer or the Software Engineer chat). An AI reviewer can be wrong in both directions: it can miss a problem or report one that isn't there. That's why there are two independent reviews, and why the decision is yours.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Code reviewed | Current contents of `src/` and `tests/`, against the documents currently in the folder. Repository base commit: `a77451540e9cc8cf3c53ab0df159a69f087cafb2`. The working folder contains uncommitted document changes; this is not a review of the commit alone. |
| Reviewer | Codex, GPT-6 |
| Independent? | I did not write or change this code in this conversation. No other code review report or hands-on report was opened. However, the required Implementation Record, Section 7, exposed another review's summary, including two findings. This limits strict independence; see Section 6. |
| Documents checked against | Product Requirements Document (PRD), d03-01 v1.1; Spec, d04-01 v1.1; User Interface/User Experience (UI/UX) Document, d05-01 v1.1; Infrastructure, d06-01 v1.3; Test Plan, d07-01 v1.1; Implementation Record, d08-01 v1.0; Developer Guide, d08-02 v1.0; supplied d08-04 template. |
| Review date | 2026-10-25 |
| Verdict | **Ready after the Must-fix items:** the main workflows have useful safeguards, but one-time sign-in, email handling, retention, reminders, and centralized wording do not fully meet the approved promises. |
| Findings | **5 Must fix · 6 Should fix · 2 Question · 0 Note** |
| Report delivery | Complete report supplied in this response. Suggested filename: `docs/d08-04-code-review-codex.md`. No file was created. |

The app lets coordinators publish volunteer tasks, view rosters, send messages, and block volunteers. Volunteers create accounts, sign in through emailed links, and reserve or cancel places; an administrator can remove blocks. Spec Section 11 promises encrypted email storage, restricted access, username-only rosters, one-time sign-in links, and HTTPS—the secure version of a web address. The application contains approximately 1,600 lines across seven Python modules, fourteen page templates, and one stylesheet, plus a small setup script. Ten test modules contain 38 named tests.

**Version 1.1 update:** The original report and the person's decisions are preserved above and below. Its original counts, verdict explanation, and hand-off describe round 1 before rework. The Re-Review section gives the current results.

| Re-review item | Details |
|---|---|
| Round and scope | Mode E, round 1 re-review. Changes since `a77451540e9cc8cf3c53ab0df159a69f087cafb2` in `src/`, `tests/`, and the six documents specified by the user, including new files within those source and test folders. |
| Updated documents | PRD v1.2; Spec v1.2; UI/UX Document v1.2; Infrastructure v1.4; Test Plan v1.2; Developer Guide v1.1. |
| Independence | I did not write or change the code. I read this report first. No other review report or Implementation Record review rows were opened during this re-review. The original independence qualification remains part of the history. |
| Current verdict | **Ready after the Must-fix items:** seven requested items are fixed by source inspection; email reliability, wording, and the sign-in email limit remain partly fixed. New error handling can store email addresses without encryption. |
| Re-review results | **7 Fixed · 3 Partly fixed · 0 Not fixed.** R-7, R-8, and R-11 retain their accepted decisions and were not reopened. |
| New findings | **R-14: Must fix. R-15: Should fix.** Both await the person's decision. |
| Cumulative findings | **6 Must fix · 7 Should fix · 2 Question · 0 Note**, retaining the original seriousness labels. These are historical totals, not counts of unresolved work. |
| Verification | Source and test inspection only. The updated suite contains 51 named tests; no tests or application services were run. No files were created or changed. |

**Version 1.2 update:** Earlier text and decisions remain unchanged. The following summary and the Re-Review dated 2026-10-26 give the latest results. The retained “Decided” status describes the existing decisions; new findings R-16 and R-17 await decisions.

| Re-review item | Details |
|---|---|
| Round and scope | Mode E, further round 1 re-review. Only changes since `a77451540e9cc8cf3c53ab0df159a69f087cafb2` in `src/`, `tests/`, and the six specified documents were reviewed, with surrounding code read where needed. |
| Documents | PRD v1.2; Spec v1.2; UI/UX Document v1.2; Infrastructure v1.4; Test Plan v1.3; Developer Guide headed v1.1, with a v1.2 Change Log entry. The workflow's d08-04 template was also read. |
| Independence | I did not write or change this code. I read this report first, including the decisions and previous Re-Review. No other review report or Implementation Record review rows were opened. |
| Current verdict | **Ready after the Must-fix items:** email-error privacy, reminder claims, and the sign-in limit are corrected by source inspection. Wording centralization and the promised maximum wait for email remain incomplete. |
| Findings checked again | R-2, R-5, R-6, R-14, and R-15: **3 Fixed · 2 Partly fixed · 0 Not fixed.** Previously Fixed findings were not reopened. R-7, R-8, and R-11 remain accepted. |
| New findings | **R-16: Should fix**, queued reminders survive cancellation. **R-17: Should fix**, the new simultaneous-request test can block itself on PostgreSQL. Decisions are empty. |
| Cumulative findings | **6 Must fix · 9 Should fix · 2 Question · 0 Note**, preserving historical seriousness labels. |
| Verification | Read-only source and test inspection. The suite contains 56 named tests. No tests, browser, database, or email service were run. No files were created or changed. |

**Version 1.3 update:** Earlier text and the person's decisions remain unchanged. The Re-Review dated 2026-11-11 gives the current results. The retained “Decided” status describes the recorded decisions; new finding R-18 has no decision.

| Re-review item | Details |
|---|---|
| Round and scope | Mode E, further round 1 re-review. Changes since `a77451540e9cc8cf3c53ab0df159a69f087cafb2` in `src/`, `tests/`, and the six specified documents, including untracked files in the permitted source and test folders. Surrounding code was read where needed. |
| Documents | PRD v1.2; Spec v1.2; UI/UX Document v1.2; Infrastructure v1.4; Test Plan v1.4; Developer Guide headed v1.1, with a v1.2 Change Log entry. The workflow's d08-04 template was read. |
| Independence | I did not write or change this code. I read this report first, including all previous Re-Review sections and decisions. No other review report or Implementation Record review rows were opened. The historical independence qualification remains unchanged. |
| Current verdict | **Ready for the next review round:** all remaining requested fixes are supported by source inspection, and no Must-fix finding remains open. This is not release approval or verification of a passing test run. |
| Findings checked again | R-5, R-15, and R-17: **3 Fixed · 0 Partly fixed · 0 Not fixed.** Previously Fixed findings and both answered questions retain their results. R-7, R-8, R-11, and R-16 remain accepted. |
| New findings | **R-18: Should fix**, background email delivery can occupy the database connections needed by pages. It belongs on the Future Version list under the recorded stop rule unless the person chooses Fix. Its Decision column is empty. |
| Cumulative findings | **6 Must fix · 10 Should fix · 2 Question · 0 Note.** These are historical totals. All existing Fix decisions are now assessed as Fixed. |
| Verification | Read-only source and test inspection. The suite contains 58 named tests. No tests, browser, database, or email service were run. No files were created or changed. |

## 2. What Was Checked

| Area | What was checked | Result |
|---|---|---|
| Privacy and security | Email encryption and lookup, page output, sign-in links, secrets configuration, database queries, page escaping, forged-form protection, HTTPS handling, and demo inbox access. | Must fix R-1 and R-2; Should fix R-6 and R-11. Normal production page templates do not expose stored email addresses. |
| Who may do what | Route restrictions, ownership checks for cancellation, coordinator actions, administrator-only block removal, and command-line administration. | Role restrictions are present. No confirmed role bypass found in the reviewed page handlers. Sign-in race remains R-1. |
| PRD and Spec rules | All seven use cases, field limits, block matching, capacity updates, reminders, deletion, retention, and design decisions DD-1 through DD-5. | Must fix R-1 through R-4; Should fix R-7; Questions R-12 and R-13. |
| Ready to move | Every d06-01 Section 5.1 row: Python version, PostgreSQL support, connection limits, installation/service instructions, environment settings, city email, scheduler, HTTPS, and release approval. | Interfaces generally fit. Four web processes with pools of four allow 16 web connections; scheduler and administrative processes must also fit within 20. R-2 and R-10 need attention. Actual servers, service startup, certificates, and approvals were not verified. |
| Tests | All test modules and their mapping to d07-01, shared fixtures, browser checks, concurrent capacity test, and random-input tests. | All 38 planned test names are represented. Important production behavior is bypassed or missing: R-8 and the tests requested in other findings. Tests were read, not run. |
| Nothing surprising | External calls, dependencies, setup script, commands, demo behavior, and maintainability. | No unexplained external destination or analytics found. Direct third-party dependencies align with the guide. R-5, R-7, and R-11 identify maintenance or operational risks. |
| Wording | Section 9 messages, empty states, error handlers, email text, and messages added during implementation. | Section 9 constants match the approved text. Other wording is scattered or differs from the documented screen states: R-5. Screen-flow differences appear in R-9. |
| Built-in security scan | Availability of a dedicated built-in code security review. | No dedicated scan was available in this session. Manual source review performed; no scanner result is claimed. |

**Version 1.1 checks of the changed material:**

| Area | Re-review result |
|---|---|
| Privacy and security | Single-use link consumption is corrected. Queued subjects and bodies are encrypted, but raw delivery errors can expose recipient addresses in the database and logs: R-14. The email limit remains vulnerable to simultaneous requests: R-6. |
| Who may do what | Changed posting, messaging, blocking, and roster handlers retain their role checks. Return links lead to internal roster routes. No new role bypass found. |
| PRD and Spec rules | Immediate confirmations, task cleanup, approved task limits, and clearer time labels are implemented. Reminder duplication and the email limit still have competing-request gaps. |
| Ready to move | The park time zone and additional scheduled commands are documented. Infrastructure Section 5.1 explicitly leaves Parks IT confirmation of the five-minute scheduler pending. Retry delays also differ from the documented five-minute promise. Live setup was not verified. |
| Tests | Thirteen tests were added, including the new `tests/test_operations.py`. They cover ordinary outages, sequential retries, cleanup, time-zone selection, wording, limits, and changed flows. They do not cover overlapping reminder jobs, simultaneous email-limit requests, recipient-bearing delivery errors, or a slow delivery backlog. |
| Nothing surprising | The added `tzdata` dependency is listed in the Developer Guide. No new unexplained external service was found. Page requests now process the entire due email queue: R-15. |
| Wording | Approved empty states, error messages, email text, and counters have moved into `wording.py`. Other visible wording remains in changed templates: R-5 is partly fixed. |
| Built-in security scan | No dedicated scan was available. Manual source review only. |

**Version 1.2 checks of the changed material:**

| Area | Re-review result |
|---|---|
| Privacy and security | Delivery exceptions now become safe categories or numeric service codes before storage and logging. The per-account database lock closes the identified simultaneous sign-in-request path. Accepted findings remain unchanged. |
| Who may do what | Changed handlers retain their role restrictions. Shared wording and banner templates retain escaped output. No new permission bypass found. |
| PRD and Spec rules | Reminder creation now uses a conditional claim in the same transaction as queue insertion. Retry delays are fixed at five minutes. The documented crash-related duplicate limitation is explicit. Queued reminders can outlive cancellation: R-16. |
| Ready to move | The email timeout is configurable and documented, but it does not enforce the promised total five-second wait: R-15. Infrastructure Section 5.1 still leaves the five-minute scheduler confirmation pending. The PostgreSQL test path needs attention: R-17. Live requirements were assessed only as affected by the changes. |
| Tests | Five more tests cover recipient rejection, page-specific email delivery, overlapping reminders, the sign-in limit, and template wording. They do not test the total time of a multi-stage email exchange or cancellation of queued reminders. T-SEC-08's synchronous nested request conflicts with the new PostgreSQL lock. |
| Nothing surprising | Pages select only their own queued email, leaving backlog delivery to scheduled commands. No new unexplained external destination or dependency was found. |
| Wording | Headings, buttons, hints, accessible labels, counters, and banner prefixes now use the shared wording file. Time helpers still supply English wording outside it: R-5. |
| Built-in security scan | No dedicated scan was available. Manual source review only. |

**Version 1.3 checks of the changed material:**

| Area | Re-review result |
|---|---|
| Privacy and security | Background delivery uses the existing encrypted queue and safe error categories. No new address exposure or secret was found in the reviewed changes. Accepted privacy findings were not reopened. |
| Who may do what | Changed routes retain their role checks. The delivery thread receives queued email identifiers from server code and runs within an application context. No new permission bypass found. |
| PRD and Spec rules | The page's email wait is now bounded independently of individual mail-service operations, matching the revised DD-6. Existing accepted behavior and previously Fixed findings retain their recorded outcomes. |
| Ready to move | The new delivery work shares each app process's database pool with page requests; slow sends can occupy that pool, recorded as R-18. The configured connection cap remains in place. Parks IT scheduler confirmation and live deployment remain unverified. |
| Tests | T-EM-07 covers a page returning while a slow send continues; T-WD-03 checks that displayed and spoken time words come from `wording.py`. T-SEC-08 now runs the second request separately and limits its waits, removing the identified circular wait. The suite does not cover several slow background sends competing with pages for database connections. |
| Nothing surprising | The new background thread is documented in Spec DD-6 and the Developer Guide. No new external destination or third-party dependency was found. Thread and connection use need future hardening under R-18. |
| Wording | `_period()`, `slot_time()`, and `hours_label()` now take the previously identified language-dependent strings from `wording.py`. R-5 is Fixed. |
| Built-in security scan | No dedicated scan was available. Manual source review only. |

## 3. Findings

The findings below are based on source inspection. Concurrency and failure scenarios have not been reproduced against a running PostgreSQL server.

| ID | Seriousness | Where | What's wrong, in plain language | Why it matters | Breaks | Next step | Decision | Decided by and date |
|---|---|---|---|---|---|---|---|---|
| R-1 | **Must fix** | `src/bbpv/views.py`, `use_sign_in_link()` | A sign-in link can potentially succeed twice when two requests arrive together. The code reads the link, then deletes it, but does not check whether that request actually deleted anything. On PostgreSQL, both requests can read the link before either deletion finishes, and both can create signed-in sessions. | Anyone holding the same link could obtain a second session while its owner signs in. The promised one-time protection is not enforced at the database boundary. | Spec 11.1 and DD-3: one-time email links. | **SDET chat:** add simultaneous redemption tests against PostgreSQL, requiring exactly one success. **Software Engineer chat:** consume and validate the link as one atomic operation, allowing sign-in only for the request that consumed it. | Fix | Park Manager, 2026-10-25 |
| R-2 | **Must fix** | `src/bbpv/mail.py`, `send()`; `src/bbpv/views.py`, `sign_in()`, `send_sign_in_link()`, `message_volunteer()`; `src/bbpv/cli.py`, `send_reminders()` | Failed email is not saved for later delivery. An email-service error escapes to an error page or stops the reminder command. For sign-in, a known account can receive an error while an unknown account still receives “Check your email,” revealing whether the account exists during an outage. Reminder delivery also happens inside one database transaction: a later failure can erase the “sent” records for earlier emails that already went out. | Volunteers may miss links, messages, or reminders. Retrying a partially completed reminder run can send duplicates. Account membership can become visible through different replies. | Spec 7: failed email is retried and sign-in replies are always the same; Spec 14: retry after an email-service outage. | **SDET chat:** test unavailable email service and partial reminder delivery. **Software Engineer chat:** persist pending delivery work, retry safely, track each delivery, and keep sign-in replies uniform. **DevOps Engineer chat:** schedule retries and monitor failures. | Fix | Park Manager, 2026-10-25 |
| R-3 | **Must fix** | `src/bbpv/db.py`, task/slot/sign-up table definitions; `src/bbpv/cli.py`, `register()` | There is no cleanup command or other code that removes tasks twelve months after their date. Their slots and sign-ups also remain. Account deletion does not perform this task cleanup. | Attendance history is kept longer than promised, and the database grows indefinitely. | Spec 6: tasks retained for twelve months after their date; slots and sign-ups retained with their parent records. | **SDET chat:** test the retention boundary and preservation of newer records and blocks. **Software Engineer chat:** implement retention cleanup. **DevOps Engineer chat:** schedule and monitor it. | Fix | Park Manager, 2026-10-25 |
| R-4 | **Must fix** | `src/bbpv/cli.py`, `send_reminders()`; `src/bbpv/views.py`, `sign_up()` | A volunteer who signs up for tomorrow after the daily 6 p.m. reminder run receives no reminder. The next day's run searches for the following day, so that sign-up is skipped permanently. The confirmation still promises a reminder the day before. | A valid late sign-up silently misses a promised service and may result in a missed shift. | PRD UC-3 acceptance criterion 5; Spec 9, UC-3; d05-01 Section 9 sign-up confirmation; d06-01 Section 5 daily schedule. | **SDET chat:** add a sign-up-after-6-p.m. case. **Software Engineer chat:** send or queue the reminder when a next-day sign-up occurs after the daily run, without duplicating reminders already sent. | Fix: always send a confirmation email straight after signing up, so the person knows they're signed up and the timing gap is closed | Park Manager, 2026-10-25 |
| R-5 | **Must fix** | `src/bbpv/views.py`, `_places_text()`, `page_not_found()`, `_400()`, `_500()`, `send_sign_in_link()`; `src/bbpv/cli.py`, `send_reminders()`; page templates including `open_slots.html` and `my_tasks.html` | Many messages remain embedded in page templates and functions despite the promise to keep all wording in one place. The Open Slots and My Tasks empty-state messages also differ from d05-01 Section 8. The Implementation Record lists several new messages for approval, but does not cover all embedded error and empty-state text. | Future wording changes or translation can miss messages. Stakeholders cannot rely on the approved wording document as a complete record of what users see. | Spec 10: all wording kept in one place. Also d05-01 Sections 8–9 and Developer Guide Section 6. | **Software Engineer chat:** centralize user-facing wording. **UI/UX Designer chat:** reconcile changed and additional messages with the document. **SDET chat:** cover the approved empty and error states. | Fix | Park Manager, 2026-10-25 |
| R-6 | **Should fix** | `src/bbpv/views.py`, `sign_in()`, `create_account()`, `send_sign_in_link()` | Public forms can send repeated emails without an application-level limit. Each successful request can create another sign-in link. No cooldown or shared sending limit is present. | An automated visitor could flood inboxes and consume the city's monthly email allowance, preventing legitimate mail delivery. A form token does not prevent someone repeatedly submitting their own valid form. | **Reviewer's opinion:** abuse controls are not specified. Relevant operating constraint: d06-01 Section 5, 3,000 emails per month. | **Software Engineer chat:** add configurable limits and duplicate-request suppression shared across running app copies. **SDET chat:** test repeated requests. **DevOps Engineer chat:** confirm any gateway limits and delivery alerts. | Fix: set the limit low, about 10 (10 sign-in emails per address in 24 hours) | Park Manager, 2026-10-25 |
| R-7 | **Should fix** | `src/bbpv/views.py`, `create_account()` and `sign_in()`; `src/bbpv/db.py`, `accounts.email_lookup` | Two simultaneous account creations using the same email and different usernames can both pass the “already used” check. The database does not require the email lookup value to be unique. Later sign-in selects just the first matching account. | One account may become unreachable, and attendance can become split between accounts. The code intends to reject reused emails but does not reliably enforce that intention. | **Reviewer's opinion:** one account per email is an implementation rule, not an explicit PRD requirement. | **SDET chat:** add concurrent registration cases. **Software Engineer chat:** enforce the intended uniqueness rule in the database and return a controlled response when two requests compete. Check existing data before adding the constraint. | Accept as is (Skip) | Park Manager, 2026-10-25 |
| R-8 | **Should fix** | `tests/conftest.py`, `make_app()`; `src/bbpv/__init__.py`, `check_form_token()`; `tests/test_security.py`; `tests/test_quality.py`, `test_t_qr_02_accessibility_checks_on_every_screen()` | Every test app disables cross-site request forgery protection—the check that stops another website submitting actions through a user's browser—and substitutes a list for real email delivery. The suite does not test simultaneous link use or email failure. Accessibility checks cover contrast, labels, button size, and page language, but not the complete keyboard and text-resizing behavior promised by the design. | Passing tests do not establish that production form protection, failure handling, or the full accessibility experience works. This is a coverage limitation, not evidence that all those features are broken. | **Reviewer's opinion:** expand coverage supporting d07-01 Sections 4, 8–9 and d05-01 Section 10. | **SDET chat:** add tests with production form protection enabled, a failing email-service substitute, concurrent authentication, and keyboard/200% text checks. Keep the existing fast tests. **Software Engineer chat:** fix any failures found. | Accept as is (Skip) | Park Manager, 2026-10-25 |
| R-9 | **Should fix** | `src/bbpv/views.py`, `post_task()`, `message_volunteer()`, `block_volunteer()`; `src/bbpv/templates/post_task.html`, `message_volunteer.html` | The posting screen always starts with three slot rows and has no “Add another slot” control. The message screen has no live character counter. Sending a message stays on that screen, and blocking opens a generic result page instead of returning to the roster. | Coordinators cannot enter a fourth slot through the normal form and must take extra steps to resume roster work. The Implementation Record's statement that there are no mockup differences is inaccurate. | d05-01 Sections 6–7 and 13. **Should fix:** these are documented interface differences, not a demonstrated security failure. | **UI/UX Designer chat:** reconcile the intended flow and controls. **Software Engineer chat:** implement the agreed behavior and correct the Implementation Record. **SDET chat:** exercise these actions through the browser rather than direct requests alone. | Fix | Park Manager, 2026-10-25 |
| R-10 | **Should fix** | `src/bbpv/__init__.py`, `create_app()` default `CLOCK`; `src/bbpv/cli.py`, `send_reminders()` | Production uses the server's local clock without an explicit park time zone. The Developer Guide does not state that the server time zone must match the park. | Moving to a server with a different time zone can change when cancellations close and which date counts as “tomorrow.” | **Reviewer's opinion:** deployment ambiguity affecting PRD UC-3/UC-4 and d06-01 Section 5's park-time schedule. | **Software Engineer chat:** make the park time zone explicit. **DevOps Engineer chat:** document consistent scheduler and application settings. **SDET chat:** test different host time zones and date boundaries. | Fix | Park Manager, 2026-10-25 |
| R-11 | **Should fix** | `src/bbpv/__init__.py`, `create_app()`; `src/bbpv/views.py`, `pretend_inbox()` | The demo inbox exposes every captured recipient and sign-in link without authentication. Its “local only” check relies on the database being SQLite; it does not establish that access comes from the local computer or that entered addresses are made up. | If someone exposes the demo server to a network or enters real details, visitors can read mail and use other people's sign-in links. The documented PostgreSQL production setup disables this page, so this is a demo-deployment risk. | **Reviewer's opinion:** strengthen the boundary supporting d06-01 Section 4's local-only, made-up-data condition. | **Software Engineer chat:** require an explicit restricted demo mode and reject real-address input there. **DevOps Engineer chat:** document local-only binding. **SDET chat:** verify that ordinary deployments cannot expose the inbox. | Accept as is (Skip): local demo only, made-up accounts, turned off on the live servers | Park Manager, 2026-10-25 |
| R-12 | **Question** | `src/bbpv/views.py`, `_check_task()`, `MAX_SLOTS`, `FORM_ROWS`; `src/bbpv/templates/post_task.html` | The code imposes a 1,000-character description limit and ten-slot maximum, while the normal form supplies only three rows. The approved PRD and Spec do not define these limits. | Coordinators may be refused valid work based on limits stakeholders did not approve. Tests cannot settle what the intended limits should be. | **Stakeholder decision:** PRD UC-1 and Spec 6 leave these limits unspecified. | **Requirements chat:** obtain a decision on description length and slots per task. **Design and UI/UX Designer chats:** update the documents. **SDET and Software Engineer chats:** align tests and implementation. | Yes: approve 1,000 characters and 10 slots, with "Add another slot" up to 10 | Park Manager, 2026-10-25 |
| R-13 | **Question** | `src/bbpv/views.py`, `clock_time()`, `slot_time()`, `hours_label()`; templates using these functions; `tests/conftest.py`, `slot_time()` and `slot_label()` | Displayed times omit morning/evening markers. A morning and evening slot can have identical visible times. Accessible button names also omit minutes, so different quarter-hour starts can receive the same label. | Volunteers, especially those using a screen reader, may choose the wrong time. The tests deliberately reproduce the ambiguous format. | **Stakeholder decision:** follows the mockup convention, but d05-01 Section 10 also calls for clear labels. | **UI/UX Designer chat:** agree an unambiguous time format including minutes where needed and morning/evening information. **SDET chat:** update the test contract after approval. **Software Engineer chat:** apply the agreed format to pages and reminders. | Yes: show a.m. or p.m. and the minutes on every time | Park Manager, 2026-10-25 |
| R-14 | **Must fix** | `src/bbpv/views.py`, `send_due_emails()` exception handler, lines 193–199; `src/bbpv/db.py`, `outbox.last_error`; delivery through `src/bbpv/mail.py`, `send()` | When the email service rejects a recipient, its error can contain that person's email address. The new handler saves the error text without encryption in `last_error` and writes it to the application log. Python's recipient-refusal exception includes the rejected recipient address. Truncating the error to 200 characters does not remove it. | A failed delivery can leave a readable copy of a volunteer's address outside the protected account field. Logs can retain that copy after the queued email is deleted. | Spec 11.1: volunteer email stored encrypted; Spec DD-4. | **SDET chat:** simulate a recipient rejection containing a made-up address and check both saved errors and captured logs. **Software Engineer chat:** record only safe error categories and codes, without recipient addresses or raw service replies. **DevOps Engineer chat:** check whether any affected logs or queue records need cleanup. | Fix (the person said to continue with the suggested fixes) | Park Manager, 2026-10-26 |
| R-15 | **Should fix** | `src/bbpv/views.py`, `send_now()`, `send_due_emails()`, and their calls from `sign_in()`, `create_account()`, `sign_up()`, and `message_volunteer()` | A person's page request tries to deliver every due email in the app before returning. During a slow email-service outage, each queued message can wait for the email connection timeout. Even a sign-in request for an unknown address starts this work. | One visitor may wait through other people's entire email backlog. Several such requests can occupy all web workers, making the app appear unavailable even though sign-ups have already been saved. The new tests fail delivery immediately, so they do not expose this delay. | **Reviewer's opinion:** keep background delivery work from tying up interactive pages; relevant reliability requirement is Spec 10. | **SDET chat:** simulate a slow service and a backlog, checking that page responses do not wait for the whole queue. **Software Engineer chat:** move backlog processing to the delivery worker and keep any immediate delivery attempt bounded. **DevOps Engineer chat:** monitor queue age and worker health. | Fix (the person said to continue with the suggested fixes) | Park Manager, 2026-10-26 |
| R-16 | **Should fix** | `src/bbpv/views.py`, `queue_email()`, `deliver()`, `cancel_sign_up()`; `src/bbpv/cli.py`, `send_reminders()`; `src/bbpv/db.py`, `outbox` | A reminder queued during an email outage can arrive after the volunteer cancels. Cancellation removes the sign-up, but the queued email stores only the account and message, with no link to that sign-up. Delivery checks that the account exists, not that the booking still exists. A queued confirmation has the same problem. | A volunteer can receive “you're signed up” after successfully canceling and may attend a place that has been given to someone else. | **Reviewer's opinion:** cancellation should invalidate undelivered booking notices. PRD UC-4 removes the booking, but the documents do not explicitly define this queue interaction. | **SDET chat:** queue a confirmation or reminder during an outage, cancel, restore delivery, and check that no stale booking notice is sent. **Software Engineer chat:** associate queued booking notices with their sign-up and remove or invalidate them on cancellation. | Accept as is (Skip) | Park Manager, 2026-10-26 |
| R-17 | **Should fix** | `tests/test_security.py`, `test_t_sec_08_the_limit_holds_for_requests_at_the_same_moment()` and `second_request_now()`; `src/bbpv/views.py`, `send_sign_in_link()` | The new test can stop making progress on PostgreSQL. The first request locks the account, then its test callback starts a second request and waits for it to finish. The second request needs the first request's lock. The first cannot release it until the callback returns. SQLite does not enforce this row lock, so a local passing run misses the problem. | The required PostgreSQL test run can hang or fail on a lock timeout, preventing the release check from completing. This is a test problem, not evidence that ordinary parallel requests bypass the corrected limit. | **Reviewer's opinion:** repair the test so it can support d07-01 T-SEC-08 and Developer Guide Section 5.1's full suite on the live-server test database. | **SDET chat:** use independently running requests with controlled synchronization and bounded waits, then verify completion and exactly ten emails on PostgreSQL. **Software Engineer chat:** investigate only if that corrected test exposes an application failure. | Fix | Park Manager, 2026-10-26 |
| R-18 | **Should fix** | `src/bbpv/views.py`, `send_now()`, `send_due_emails()`, `deliver()`; `src/bbpv/db.py`, `make_engine()` | Several slow email sends can delay unrelated pages. Each immediate send starts a background thread, and `send_due_emails()` holds a database connection while `deliver()` waits for the email service. With the documented pool of four connections per app process, four slow sends can occupy every connection that process's pages need. Returning the original page after five seconds does not release those connections or stop the sends. | Volunteers trying to browse, sign up, or cancel may wait or receive an error during a slow email-service incident. Further send requests can also leave more background threads waiting for connections. T-EM-07 checks one slow send, so it does not expose this shared-resource problem. | **Reviewer's opinion:** limit background work and avoid holding database connections during network delivery. Relevant constraints are Spec 10 reliability and d06-01 Section 5.1's connection limit. No new worker-isolation requirement is stated in the documents. | **Future Version unless the person chooses Fix. SDET chat:** test several slow sends with a small connection pool while another person loads a page. **Software Engineer chat:** release the database connection before contacting the email service and bound immediate background work, leaving excess work in the saved queue. **DevOps Engineer chat:** monitor connection use and delivery backlog. | Future Version (the stop rule's default; the person may still choose Fix) | Park Manager's stop rule, 2026-10-26; recorded 2026-11-11 |

### Re-Review — 2026-10-25

“Fixed” below means the requested behavior is supported by the changed source and test inspection. It does not claim a fresh passing test run or live-server verification.

| Finding | Result | Evidence and remaining work |
|---|---|---|
| R-1 | **Fixed** | `use_sign_in_link()` now checks the deletion's affected-row count and signs in only when that request removed exactly one link. This closes the identified competing-request path. T-SEC-06 introduces a second redemption after the first request reads the link but before it deletes it. PostgreSQL execution remains unverified. |
| R-2 | **Partly fixed** | `queue_email()` saves encrypted delivery work in the same transaction as the related change. Delivery failures leave it queued; ordinary sign-in replies remain uniform. Each successful delivery is removed separately, so a later email failure no longer rolls back earlier delivery records. However, two overlapping `send-reminders` runs can both read `reminder_sent=False`, both enqueue the reminder, and then both mark it true. The update does not claim the reminder conditionally, and the queue has no unique reminder identifier. Also, if the process stops after the email service accepts a message but before its queue row is deleted, a retry can send it again. T-EM-02 covers sequential reruns, not these cases. Finally, retry delays grow from 5 to 10 minutes and onward to 60, despite Spec Sections 7 and 14 promising retries every 5 minutes. **SDET chat:** add overlapping-job and partial-delivery tests. **Software Engineer chat:** claim each reminder atomically and address delivery acknowledgement failures. **Design chat:** state any unavoidable duplicate-delivery limitation accurately and reconcile retry timing. **DevOps Engineer chat:** complete the scheduler confirmation identified in d06-01 Section 5.1. |
| R-3 | **Fixed** | The new `clean-up` command removes tasks older than the calendar-year cutoff, their slots, and their sign-ups in one transaction. It leaves the block list alone. T-DATA-01 checks older and newer tasks, related records, and block preservation. Infrastructure and the Developer Guide document daily cleanup at 3 a.m. park time. Installation of that job was not verified. |
| R-4 | **Fixed** | Assessed against the person's decision to send a confirmation after every sign-up. `sign_up()` queues that confirmation with the sign-up and immediately attempts delivery. T-03-08 includes a 7 p.m. sign-up after the reminder run. PRD UC-3 and UI/UX Section 9 now describe the confirmation; the confirmation screen avoids promising a later reminder for today or tomorrow. The shared delivery limitations remain under R-2 and R-15. |
| R-5 | **Partly fixed** | Email subjects and bodies, error-page messages, place counts, confirmation notes, and the affected empty states now use `wording.py`. UI/UX Sections 8–9 reconcile those empty states and added messages. However, changed templates still embed visible wording: the slot instructions and “Add another slot” button in `post_task.html`; the email privacy explanation and “Back to the roster” link in `message_volunteer.html`; and button text in `block_confirm.html`. Several templates also retain their own “Problem:” prefix despite the shared prefix constant. Spec 10 now explicitly requires one wording file. **Software Engineer chat:** finish centralizing visible text, including labels and hints. **UI/UX Designer chat:** reconcile remaining wording. **SDET chat:** verify representative labels, hints, and error states as well as the already-covered empty states. |
| R-6 | **Partly fixed** | `send_sign_in_link()` now counts requests by the hashed address in a shared database table and suppresses requests after ten; T-SEC-07 checks sequential requests and reset after 24 hours. The count and insertion are separate database steps without a per-address lock or atomic limit check. On PostgreSQL, two requests can both see nine previous emails and both queue another, allowing eleven. **SDET chat:** test simultaneous requests at the limit against PostgreSQL. **Software Engineer chat:** enforce the limit atomically for each address. The original “Should fix” label is preserved, but the ten-email limit is now an explicit promise in PRD Section 6 and Spec DD-9, so completing this approved fix is required. |
| R-9 | **Fixed** | `post_task()` and its template add rows up to ten while retaining entered values. The message template updates its counter as the coordinator types. Roster links carry the originating slot, and successful message and block actions redirect back with a banner. UI/UX Sections 7 and 13 now describe these controls and flows. T-01-07, T-06-03, and T-07-04 inspect the form and return paths. Browser interaction was not run; the tests do not exercise the live counter while typing. The Implementation Record correction was outside this re-review's permitted scope and was not checked. |
| R-10 | **Fixed** | `park_clock()` uses the configured `PARK_TIMEZONE` instead of the host's local time zone. Infrastructure documents park-time scheduling, and the Developer Guide lists the setting and scheduled jobs. T-QR-03 checks two explicit zones without the test clock. Actual scheduler configuration and date-boundary execution were not verified. |
| R-12 | **Fixed** | PRD UC-1 and Spec Section 6 now approve descriptions up to 1,000 characters and one to ten slots. `_check_task()` enforces these limits, and the form offers “Add another slot” up to ten. T-01-06 and T-01-07 cover the limits and row addition. |
| R-13 | **Fixed** | `slot_time()` and `hours_label()` now include minutes and morning/evening markers, including both markers when a range crosses noon. Pages and confirmation/reminder emails use these helpers. UI/UX UX-6 explicitly approves a shared marker when both ends have the same period, such as “9:00 – 10:00 a.m.” Test expectations were updated accordingly. |

**Re-review outcome:** R-2, R-5, and R-6 need further work. R-14 and R-15 are new findings awaiting decisions. The accepted decisions on R-7, R-8, and R-11 remain unchanged.

### Re-Review — 2026-10-26

This re-review checks every finding marked Fix whose latest result was not Fixed: R-2, R-5, R-6, R-14, and R-15. Both questions answered Yes were already Fixed. Accepted findings and previously Fixed results remain unchanged.

“Fixed” means supported by source inspection within the permitted scope. It does not certify a passing test run, live configuration, or cleanup of historical operational data.

| Finding | Result | Evidence and remaining work |
|---|---|---|
| R-2 | **Fixed** | `src/bbpv/cli.py`, `send_reminders()`, now changes `reminder_sent` only when it is still false and queues the email in that same transaction. A competing run that changes no row skips the reminder. T-EM-06 exercises an overlapping run at this boundary. `send_due_emails()` retains separate delivery records and now uses a fixed five-minute retry interval. Spec DD-6 explicitly records the remaining possibility of a duplicate if the app stops after the service accepts an email but before the queue is updated. This resolves the previously requested code and design changes. Parks IT's five-minute scheduler confirmation remains pending in d06-01 Section 5.1 and must be completed before release; it was not verified here. Cancellation of already queued notices is a separate new finding, R-16. |
| R-5 | **Partly fixed** | All previously identified template headings, buttons, hints, and banner prefixes now use `wording.py`, including the new `_banner.html`. T-WD-02 checks for words embedded in templates. However, `src/bbpv/views.py`, `_period()` and `hours_label()`, still supply “a.m.”, “p.m.”, and “ to ” directly. These appear in page text, accessible button names, and emails. Changing only the promised wording file still cannot change all displayed or spoken wording. The template-only test does not inspect these helpers. **Software Engineer chat:** move these language-dependent time strings or their formatting helpers into the shared wording file. **SDET chat:** cover wording supplied by Python helpers as well as templates. This is a smaller remainder of the existing Spec Section 10 finding, not a new time-format defect. |
| R-6 | **Fixed** | `send_sign_in_link()` now locks the account row before recording and counting requests. On the normal PostgreSQL path, a second request for that account must wait until the first transaction finishes, then sees its committed count. Requests above ten remove their provisional count record and queue no email. T-SEC-07 covers the sequential limit and reset. The application correction closes the previously identified same-account race by source inspection. The new T-SEC-08 test has its own PostgreSQL blocking problem, recorded separately as R-17; passing PostgreSQL verification is not claimed. The accepted R-7 account-creation finding is not reopened. |
| R-14 | **Fixed** | `safe_error()` replaces recipient-refusal exceptions with a fixed description, other email-service responses with their numeric code, and connection failures with a fixed category. Neither the exception's raw text nor the recipient dictionary is saved or logged by `send_due_emails()` or `send_now()`. T-EM-04 supplies a recipient-bearing rejection and checks both the database and captured logs. This closes the identified new-error storage path. Whether earlier deployments left addresses in historical logs or queue records remains an operational check for the **DevOps Engineer chat**; no such data was accessed. |
| R-15 | **Partly fixed** | `queue_email()` returns the new email's identifier, and every immediate-delivery caller passes only its own identifier to `send_now()`. An unknown account passes no identifier and causes no delivery attempt. T-EM-05 checks that the backlog is left to `send-emails`. However, the five-second `EMAIL_SEND_TIMEOUT` is passed to Python's Simple Mail Transfer Protocol (SMTP) socket operations in `mail.send()`. It is not a deadline for the whole exchange: connection, greeting, encryption negotiation, authentication, and message replies can each consume time. For example, several replies arriving four seconds apart can keep a page waiting much longer than five seconds without any socket timeout. This does not meet Spec DD-6 or the Developer Guide's stated maximum wait. **SDET chat:** simulate a multi-stage slow service and check total elapsed time. **Software Engineer chat:** enforce a total delivery deadline, or move delivery fully off the page path through an agreed design change. The historical Should-fix label is preserved, but the maximum wait is now an explicit Spec promise. |

**Re-review outcome:** **3 Fixed · 2 Partly fixed · 0 Not fixed.** R-5 and R-15 need further work. New Should-fix findings R-16 and R-17 await decisions. R-7, R-8, and R-11 remain accepted as recorded.

### Re-Review — 2026-11-11

This re-review checks every finding marked Fix whose latest result was not Fixed: R-5, R-15, and R-17. Both questions answered Yes were already Fixed. Previously Fixed findings and accepted findings R-7, R-8, R-11, and R-16 remain unchanged.

“Fixed” means the requested correction is supported by source inspection. Tests were read but not run because this review must not create or change files.

| Finding | Result | Evidence and remaining work |
|---|---|---|
| R-5 | **Fixed** | `src/bbpv/views.py`, `_period()`, now reads `w.MORNING` and `w.EVENING`; `slot_time()` and `hours_label()` use `w.RANGE_DASH` and `w.RANGE_TO`. These strings are defined in `src/bbpv/wording.py`. T-WD-03 in `tests/test_operations.py` changes all four values and checks both the displayed time and the accessible sign-up label across noon. Together with the previously corrected templates and messages, this closes the identified remainder of R-5. |
| R-15 | **Fixed** | `src/bbpv/views.py`, `send_now()`, starts delivery in a separate thread and waits with `worker.join(timeout=app.config["EMAIL_SEND_TIMEOUT"])`. The page no longer waits for every stage of the mail exchange to finish. Only that page's queued identifiers are passed to delivery. Spec DD-6 and the Developer Guide now explicitly say that slow delivery continues in the background. T-EM-07 sets a half-second page wait and a three-second simulated send, checks that the page returns in under two seconds, and checks that the email subsequently arrives. This supports the requested page-wait correction; production timing was not measured. Shared database-connection use by these background sends is a separate new Should-fix finding, R-18. |
| R-17 | **Fixed** | `tests/test_security.py`, T-SEC-08, now starts the second request in a separate thread. The callback waits at most one second, then lets the first request continue and release its account lock. Afterward, the test waits at most thirty seconds for the second request, checks that it finished without a captured exception, and requires exactly ten emails in total. This removes the identified circular wait in which the first request waited indefinitely for a second request that needed its lock. A passing PostgreSQL run remains unverified and is still required by the deployment test procedure. |

**Re-review outcome:** **3 Fixed · 0 Partly fixed · 0 Not fixed.** No Must-fix finding remains open. All existing Fix decisions now have a latest result of Fixed. The recorded stop rule allows round 1 to end, subject to the workflow's passing-test evidence. No new Must-fix finding was identified.

**Future Version list:** R-18, background email sends competing with pages for database connections. This follows the person's recorded stop rule; it is not a new decision entered on their behalf. Its Decision cell remains empty, and the person may choose Fix.

## 4. Things Done Well

- Email addresses are encrypted in account records. Lookup and block matching use keyed hashes, and normal delivery decrypts addresses in one helper.
- Roster queries select usernames rather than email addresses. The administrator's block-list screen also avoids displaying addresses.
- Capacity is reduced through a conditional database update inside the same transaction as the sign-up. A database constraint prevents negative remaining capacity, and another prevents duplicate sign-ups for one account and slot.
- Cancellation checks ownership. Posting, roster access, messaging, blocking, and block removal have server-side role checks.
- Page templates escape submitted text, and database queries use structured parameters rather than joining form text into database commands.
- Production forms include forgery tokens. Session cookies have protective settings, and HTTPS enforcement is enabled by default.
- Known Section 9 messages match the approved wording. The tests provide useful coverage of ordinary workflows, boundary values, privacy output, and competing requests for the last place.

**Additional strengths in the rework:**

- Sign-up confirmations are saved with the sign-up, so an ordinary email-service outage does not lose the delivery work.
- Queued subjects and bodies are encrypted, including sign-in links.
- The single-use link correction checks the database operation that actually decides the winner.
- The new tests cover ordinary outages, late sign-ups, retention cleanup, approved task limits, and revised wording.
- Requirements, design, interface, infrastructure, and test documents were updated together for the approved changes.

**Additional strengths in version 1.2:**

- Error handling keeps useful failure categories without copying recipient addresses or raw service replies.
- Reminder creation claims the sign-up conditionally and saves the queued message in the same transaction.
- Interactive pages no longer process other people's queued emails.
- Shared screen wording now includes accessible labels and a single banner-prefix template.

**Additional strengths in version 1.3:**

- The page's email wait is separated from the duration of the mail exchange.
- The new wording test checks actual page output after changing the shared time words.
- The revised simultaneous-request test lets the first request release its lock before requiring the second to finish.

## 5. Questions for the Stakeholders

1. **R-12:** What maximum description length and number of slots should one task allow? Should coordinators be able to add rows up to that agreed limit?
2. **R-13:** Should all displayed and spoken times distinguish morning from evening and include the actual minutes?

**Version 1.1 update:** Both questions were answered Yes in the person's decisions, and their implementation is assessed as Fixed above. No additional stakeholder question is needed to explain the re-review results. R-14 and R-15 await finding decisions.

**Version 1.2 update:** The existing Yes answers and Fix decisions remain unchanged. R-14 is now Fixed; R-15 is Partly fixed. No additional requirements question was needed to conduct this re-review. The person should decide new findings R-16 and R-17.

**Version 1.3 update:** No additional requirements question was needed. R-5, R-15, and R-17 are now Fixed. The accepted decision on R-16 remains unchanged. R-18 is listed for a Future Version under the recorded stop rule unless the person chooses Fix; its Decision column remains empty.

## 6. Limits of This Review

- **Read-only:** no code, tests, documents, or report files were created or changed. No software was installed, no messages were sent, and no repository changes were pushed.
- **Independence qualification:** no other `d08-04` report or `d08-05` hands-on report was opened. However, the required d08-01 Implementation Record contained another review's summary. It named missing email retries and retention cleanup, corresponding to R-2 and R-3 here. Both were checked directly against source, but this report cannot honestly claim complete blindness to the earlier review. The Tracking chat should record this limitation when assessing the independent-review requirement.
- **Version assumption:** “what is in the folder now” was used. The user's instruction to return the complete report in chat replaced the default request to save a report.
- **Dates:** this report uses the actual review date, 2026-10-25. Some supplied sample documents describe events in December 2026 and January 2027. Their content was treated as supplied requirements and narrative, not independently verified operational history.
- **No execution:** tests were not run because their fixtures create temporary databases and may create other files. The reported 38 passing tests comes from the supplied account of prior runs, not a new verification.
- **No live verification:** PostgreSQL 16 behavior, Python 3.12 deployment, city email delivery, connection totals, production logging, secrets, network restrictions, backups, uptime, and Parks IT approval were not inspected.
- **Source-based concurrency findings:** R-1 and R-7 describe concrete competing-request paths visible in the code. A controlled PostgreSQL test is needed to reproduce and verify their fixes.
- **Accessibility and performance:** no browser walkthrough, screen-reader session, phone performance run, or full Web Content Accessibility Guidelines (WCAG) 2.1 AA assessment was performed.
- **Dependencies:** direct dependencies were compared with the Developer Guide. This was not a current vulnerability-database audit or a complete transitive-license review.
- **Scope of privacy claims:** normal account data flows were inspected. Free-text task descriptions and coordinator messages can still contain information that their authors choose to type.
- An AI reviewer can miss problems or misjudge them. This report is one of two intended independent reviews, and a person decides on every finding.

**Additional limits for version 1.1:**

- Only the requested changes were reviewed, with surrounding code read where needed to understand them. Unrelated uncommitted documents were excluded. No other review report or Implementation Record review rows were opened.
- New files within the permitted folders were included: `tests/test_operations.py` and `src/REVIEW-GUIDE.md`. References from the guide to excluded reports were not followed.
- The updated tests were read, not run. Their passing status was not independently established. No database, mail service, or browser session was started.
- R-14 was checked against the application's delivery path and the locally installed Python mail library's exception implementation. No real recipient data was inspected or recorded.
- The remaining competing-request paths and backlog delays were established by source inspection, not reproduced against production services.
- “Fixed” for R-9 covers the permitted code and UI/UX documents; it does not verify the excluded Implementation Record.
- The original text is retained as requested. Current results and the current hand-off are additions, rather than silent replacements of the original findings or the person's decisions.

**Additional limits for version 1.2:**

- The review date is 2026-10-26. The comparison remains the user-specified commit to the current permitted working-folder changes, including untracked files within `src/` and `tests/`.
- This report was read first. No excluded report, Implementation Record review rows, or unrelated uncommitted document contents were opened.
- The 56 named tests were inspected as relevant to the changes, not executed. No passing-test claim is independently certified.
- R-15's timeout assessment was checked against the delivery code and the locally installed Python mail library. The city's mail server and production Python runtime were not exercised.
- R-16 and R-17 describe concrete source paths, not reproduced incidents. PostgreSQL lock behavior and total email-send time still require controlled tests.
- The existing Spec's documented crash-related duplicate-delivery limit was treated as the current design. This re-review does not approve that design on the stakeholders' behalf.
- Parks IT scheduler confirmation, historical-log cleanup, browser behavior, and production deployment remain outside this source review.
- Historical report text, counts, decisions, and hand-off notes are preserved. The version number and last-updated date are advanced; additions state the latest result.

**Additional limits for version 1.3:**

- The review date is 2026-11-11. The comparison remains the specified commit to the permitted current working-folder changes. Other uncommitted documents were excluded.
- This report was read first. No other review report or Implementation Record review rows were opened. References to excluded reports in `src/REVIEW-GUIDE.md` were not followed.
- The suite contains 58 named tests. Relevant tests were inspected but not executed; their passing status, including PostgreSQL execution, was not independently verified.
- R-18 is a source-based failure scenario, not a reproduced production incident. No load test, database-pool exhaustion test, or live email timing measurement was performed.
- The revised DD-6 explicitly permits slow delivery to continue in the background. The R-15 result assesses the bounded page wait against that supplied design.
- Parks IT's five-minute scheduler confirmation remains pending in the permitted Infrastructure document. Historical-log cleanup and operational approvals remain unverified.
- The current “Ready” verdict applies to progressing from this code-review round. It does not replace the second independent code review, the hands-on review, passing-test evidence, or release approval.
- Existing report text and decisions are preserved. Only the header version and last-updated date are advanced; additions give the current assessment.

## 7. Change Log

| Version | Date | Change | By |
|---|---|---|---|
| 1.0 | 2026-10-25 | First review supplied in chat; no file saved. All decisions left open. Independence limitation disclosed. | Codex, GPT-6 |
| 1.0 | 2026-10-25 | Decisions filled in: 8 Fix (R-1 to R-6, R-9, R-10), 3 Accept as is (R-7, R-8, R-11), 2 Questions answered Yes (R-12, R-13). Report text unchanged | Park Manager (recorded by Claude) |
| 1.1 | 2026-10-25 | Read-only Mode E re-review of the specified changes since a77451540e9cc8cf3c53ab0df159a69f087cafb2. Preserved original report and decisions. Added seven Fixed and three Partly fixed results, new findings R-14 and R-15 with decisions empty, updated scope and limits, and a current hand-off. No files changed; tests not run. | Codex, GPT-6 |
| 1.1 | 2026-10-26 | Decisions filled in for R-14 and R-15: Fix. Report text unchanged | Park Manager (recorded by Claude) |
| 1.2 | 2026-10-26 | Further read-only Mode E re-review against the same specified commit and scope. Preserved prior text and decisions. R-2, R-6, and R-14 Fixed; R-5 and R-15 Partly fixed. Added Should-fix findings R-16 and R-17 with decisions empty, current checks and limits, and a new hand-off. No files changed; tests not run. | Codex, GPT-6 |
| 1.2 | 2026-10-26 | Decisions filled in for R-16 (Accept as is) and R-17 (Fix). The person also set a stop rule: a round ends when no Must-fix finding is left open; after that, new Should-fix findings go to a Future Version list unless the person chooses Fix. Report text unchanged | Park Manager (recorded by Claude) |
| 1.3 | 2026-11-11 | Read-only Mode E re-review against the same specified commit and scope. Preserved prior text and decisions. R-5, R-15, and R-17 Fixed by source inspection; no Must-fix finding remains open. Added Should-fix R-18 with its decision empty and listed it for a Future Version under the recorded stop rule. Added current checks, limits, and hand-off. No files changed; tests not run. | Codex, GPT-6 |
| 1.3 | 2026-11-11 | R-18 recorded as Future Version, the stop rule's default. Round 1 closed: no Must-fix finding open, every Fix confirmed Fixed. Report text unchanged | Park Manager (recorded by Claude) |

**Hand-off note for the Tracking chat**

Report: `docs/d08-04-code-review-codex.md` — proposed filename; complete report delivered in chat, not saved. Reviewer: **Codex, GPT-6**.

Verdict: **Ready after the Must-fix items.** Findings: **5 Must fix, 6 Should fix, 2 Question, 0 Note.**

Must-fix items:

- **R-1:** Enforce single-use sign-in links under simultaneous requests.
- **R-2:** Persist and retry failed emails safely; preserve uniform sign-in replies.
- **R-3:** Remove expired tasks and related records after twelve months.
- **R-4:** Deliver reminders for next-day sign-ups made after the daily reminder run.
- **R-5:** Centralize user-facing wording and reconcile it with the approved document.

Recommendation: **Fix first.** A person should decide each finding, then send approved fixes to the **SDET chat** and **Software Engineer chat**; involve the **DevOps Engineer chat** for delivery retries and retention scheduling, and the **UI/UX Designer chat** for wording. Obtain re-review after rework before Step 8 sign-off and Step 9 Release. Record that the required Implementation Record exposed another review's summary, limiting strict review independence.

**Updated hand-off note for the Tracking chat — version 1.1**

Report: `docs/d08-04-code-review-codex.md`, version **1.1**, delivered in full in chat; no file changed. Reviewer: **Codex, GPT-6**. Mode E comparison: `a77451540e9cc8cf3c53ab0df159a69f087cafb2` to the specified current working-folder changes.

Verdict: **Ready after the Must-fix items.** Re-review: **7 Fixed, 3 Partly fixed, 0 Not fixed.** New findings: **1 Must fix, 1 Should fix.** Cumulative historical totals: **6 Must fix, 7 Should fix, 2 Question, 0 Note.**

Remaining required work:

- **R-2:** Prevent overlapping reminder jobs from queuing duplicates; address delivery acknowledgement failures and reconcile retry timing.
- **R-5:** Finish moving visible wording into the shared wording file.
- **R-6:** Enforce the approved ten-email limit under simultaneous requests; this is now an explicit PRD and Spec requirement.
- **R-14, new Must fix:** Keep recipient addresses out of saved error text and application logs.

**R-15, new Should fix:** Prevent interactive page requests from processing the entire email backlog.

Recommendation: **Fix first.** Send remaining approved work to the **SDET chat** and **Software Engineer chat**. Involve the **Design chat** for delivery guarantees and retry timing, the **UI/UX Designer chat** for wording, and the **DevOps Engineer chat** for scheduler confirmation and safe operational logging. A person must decide R-14 and R-15. Obtain passing tests and another Mode E re-review before treating round 1 as settled. R-7, R-8, and R-11 remain accepted as recorded.

**Updated hand-off note for the Tracking chat — version 1.2**

Report: `docs/d08-04-code-review-codex.md`, version **1.2**, delivered in full in chat; no file changed. Reviewer: **Codex, GPT-6**. Read-only Mode E comparison: `a77451540e9cc8cf3c53ab0df159a69f087cafb2` to the specified current working-folder changes.

Verdict: **Ready after the Must-fix items.** This re-review: **3 Fixed, 2 Partly fixed, 0 Not fixed.** R-2, R-6, and R-14 are Fixed by source inspection. New findings: **0 Must fix, 2 Should fix, 0 Question, 0 Note.** Cumulative historical totals: **6 Must fix, 9 Should fix, 2 Question, 0 Note.**

Remaining approved work:

- **R-5, Must fix:** Move the remaining displayed and spoken time wording into the shared wording file.
- **R-15, historically Should fix:** Enforce the total email-send wait promised by Spec DD-6; the backlog issue is corrected, but the five-second maximum is not.

New findings awaiting decisions:

- **R-16, Should fix:** Invalidate queued booking notices when their sign-up is canceled.
- **R-17, Should fix:** Repair the simultaneous email-limit test so it can complete on PostgreSQL.

Recommendation: **Fix first.** Send R-5 and R-15 to the **SDET chat** and **Software Engineer chat**. Have the person decide R-16 and R-17; send any approved work to the same chats. The **DevOps Engineer chat** must complete scheduler confirmation before release and check whether historical delivery-error records need cleanup. Obtain passing tests, including the corrected PostgreSQL concurrency test, and another Mode E re-review before treating round 1 as settled. Previously Fixed findings and the accepted decisions on R-7, R-8, and R-11 remain unchanged.

**Updated hand-off note for the Tracking chat — version 1.3, 2026-11-11**

Report: `docs/d08-04-code-review-codex.md`, version **1.3**, delivered in full in chat; no file changed. Reviewer: **Codex, GPT-6**. Read-only Mode E comparison: `a77451540e9cc8cf3c53ab0df159a69f087cafb2` to the specified current working-folder changes.

Verdict: **Ready for the next review round.** This re-review: **3 Fixed, 0 Partly fixed, 0 Not fixed.** R-5, R-15, and R-17 are Fixed by source inspection. **No Must-fix finding remains open.** All existing Fix decisions now have a latest result of Fixed. Accepted decisions on R-7, R-8, R-11, and R-16 remain unchanged.

New findings: **0 Must fix, 1 Should fix, 0 Question, 0 Note.** Cumulative historical totals: **6 Must fix, 10 Should fix, 2 Question, 0 Note.**

**Future Version:** R-18, slow background email sends can occupy the database connections needed by pages. Its Decision cell is empty. Under the recorded stop rule, it does not keep this round open unless the person chooses Fix. If chosen, send it to the **SDET chat** and **Software Engineer chat**, with monitoring support from the **DevOps Engineer chat**.

Recommendation: Record the resolved fixes and the Future Version item, confirm the passing-test evidence, and proceed to round 2. Tests were not run during this read-only review. Complete the second independent code review and the hands-on review before Step 8 sign-off. Parks IT scheduler confirmation, required PostgreSQL testing, and operational checks remain prerequisites for Step 9 Release.