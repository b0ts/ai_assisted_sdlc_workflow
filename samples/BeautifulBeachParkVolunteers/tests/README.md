# Tests

The automated tests for BeautifulBeachPark Volunteers, written in Step 07
(Test Creation) **before any code exists**. Each test is named after its ID
in the Test Plan ([`docs/d07-01-test-plan.md`](../docs/d07-01-test-plan.md)),
so `test_t_03_04_...` is test T-03-04.

Step 08 (Implementation) is finished when every test passes. After sign-off
the tests are locked: the code changes to pass the tests, never the other way
round (Test Plan Section 11).

## How to Run the Tests

Everything runs on your own computer, at no cost. No real emails are sent.

1. Install Python 3.10 or newer from [python.org](https://www.python.org).
2. Open Terminal in the project folder and set up the project's Python:

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r src/requirements.txt -r tests/requirements.txt
   python -m playwright install chromium
   ```

   The first line makes a **virtual environment**: a private copy of
   Python just for this project, in a `.venv` folder that Git ignores. It
   avoids the "externally-managed-environment" error that Python from
   Homebrew (and some Linux systems) gives for a plain `pip install`. The
   last line downloads the browser the two browser tests use (about
   150 MB). On Windows, the second line is `.venv\Scripts\activate`.
   Each time you open a new Terminal window for this project, run
   `source .venv/bin/activate` again; your prompt then starts with
   `(.venv)`.
3. Run `pytest -m "not monkey and not browser"` while building. This skips
   the two long monkey tests and the two browser tests, and takes under a
   minute.
4. Before sign-off, run plain `pytest` to run all 74.

Or ask Claude Code: "Run the tests in this project and summarize which pass
and which fail."

| Option | What it does |
|---|---|
| `TEST_DATABASE_URL=postgresql://...` | Runs against a PostgreSQL test database instead of the default throwaway SQLite file. Its tables are dropped after each test, so never point it at real data. |
| `MONKEY_INPUTS=1000` | Random inputs per field in T-MK-01 (the plan's 1,000 is the default) |
| `MONKEY_SECONDS=300` | How long T-MK-02 runs (the plan's 5 minutes is the default) |
| `MONKEY_SEED=1` | Makes the random tests repeat exactly, to reproduce a failure |

The two browser tests (T-QR-01, T-QR-02) need Playwright and its Chromium
browser (step 2 installs both). Without them they are reported as
**skipped**, not passed.

## What the Tests Expect from the Code (the Contract)

The tests can only be written before the code if they agree on a few names.
This section is that agreement. The Software Engineer builds to it in
Step 08. If something here turns out to be wrong, send a request back to the
SDET chat (Test Plan Section 11); don't change the tests.

### The app

- `src/bbpv/` is a Python package with `create_app(config)`, which returns a
  Flask app. `config` is a dictionary that overrides the defaults.
- The tests pass these settings:

| Setting | What the tests give | What the app must do with it |
|---|---|---|
| `TESTING` | `True` | Turn off request forgery tokens (CSRF) if the app uses them |
| `CHECK_FORM_TOKENS` | Left out; `True` in T-SEC-12 only | When `True`, check the tokens even though `TESTING` is on (v1.5) |
| `DATABASE_URL` | A SQLite file, or `TEST_DATABASE_URL` | Store everything there, creating the tables if they're missing |
| `CLOCK` | A function returning the current park time (a `datetime` with no time zone) | Use it for **every** "now": slot started, tomorrow's reminders, link expiry |
| `TEST_INBOX` | An empty list | Instead of sending email, append one dictionary per email: `{"to", "from", "subject", "text"}`. When a test sets `inbox.down = True`, `append` raises an error, like an email service that is down: the app must keep the email and send it later (T-EM tests). When it sets `inbox.reject = True`, `append` raises the mail library's "recipient refused" error, which names the address (T-EM-04). `inbox.slow = 3` makes each email take 3 seconds (T-EM-07) |
| `PARK_TIMEZONE` | Left out (T-QR-03 passes a zone, with no `CLOCK`) | Without `CLOCK`, use the time in this zone for every "now" |
| `SECRET_KEY` | A test-only value | Sign sessions and sign-in links |
| `BASE_URL` | `https://volunteers.example.test` | Start the links in emails with it |
| `FORCE_HTTPS` | Left out (browser tests pass `False`) | By default, send any `http://` request to `https://` (T-SEC-02) |

- The app keeps its own encryption key for stored emails. In testing it may
  make one up.
- The sign-in and create-account pages send their email in the background
  (Spec DD-10). The app keeps each background sender (a `threading.Thread`)
  in the set `app.extensions["email_senders"]` until it ends, so the test
  client can wait for it (`wait_for_emails()` in `conftest.py`, v1.5).

### Commands (for the System Administrator and the daily job)

Run with `flask --app bbpv <command>`. The tests call them through Flask's
command runner.

| Command | What it does |
|---|---|
| `create-account USERNAME EMAIL --role volunteer\|coordinator\|admin` | Creates an account (how coordinator and admin accounts are made) |
| `delete-account USERNAME` | Deletes an account; its block list entry stays (T-SEC-03) |
| `send-reminders` | The reminder job: emails everyone signed up for a slot tomorrow, once each, even if it runs twice |
| `send-emails` | Sends queued emails and retries ones that failed (T-EM tests) |
| `clean-up` | Removes tasks dated more than 12 months ago, with their slots and sign-ups (T-DATA-01) |

### Screens and addresses

Pages are ordinary HTML. Confirm boxes (cancel, block) also work as their own
page, so everything works without JavaScript.

| Screen | Address | Notes for the tests |
|---|---|---|
| S-1 Sign In | `GET/POST /sign-in` (field `email`); the emailed link is `/sign-in/<token>` | Opening the link (`GET`) shows "Finish signing in" with a "Sign in" button in a form that posts to the same address; only the `POST` signs in and uses the link up (v1.5; `use_link()` in `conftest.py`) |
| S-2 Create Account | `GET/POST /create-account` (fields `username`, `email`, checkbox `privacy_accepted`) | The account is made only when "Sign in" is pressed on the emailed link (v1.6, Spec DD-13) |
| S-3 Open Slots | `GET /slots` | Each slot shows its time, then its places: `9:00 – 10:00 a.m.` (en dash), then `2 places left`, `1 place left`, or `Full`. Each open slot has a link to S-4 with `aria-label="Sign up for <title>, 9:00 to 10:00 a.m."` |
| S-4 Confirm Sign-Up | `GET /slots/<id>/confirm`; confirming is `POST /slots/<id>/sign-up` | |
| S-5 My Sign-Ups | `GET /my-sign-ups` | Each sign-up has a link to its cancel page with `aria-label="Cancel <title>, April 21, 9:00 to 10:00 a.m."` |
| Cancel confirm | `GET/POST /sign-ups/<id>/cancel` | The page has a "Yes, cancel" button |
| S-6 My Tasks | `GET /my-tasks` | A table row per slot: title, time, `2 of 2` (plus `(Full)` when full), and a link with `aria-label="Roster for <title>, 9:00 to 10:00 a.m."` |
| Delete a task | `GET/POST /tasks/<id>/delete` | From S-6: each task is a `<section class="task">` with its title as an `<h3>`, a "Delete task" link with `aria-label="Delete <title>, April 21"`, and a table of its slots (time, places filled, Roster). The page shows the d05-01 confirm wording and a "Yes, delete" button (v1.7) |
| S-7 Post a Task | `GET/POST /tasks/new` | Fields `title`, `description`, `date` (`2027-04-21`), and for each slot `slot_start`, `slot_end` (`09:00`), `places`, repeated in order. `slot_start` is a drop-down list (`<select>`) of `06:00` to `22:00` every 30 minutes; `slot_end` is hidden and may be empty (v1.7). Three rows to start; the "Add another slot" button is `<button name="add_slot">`, and posting with it shows the form again with one more row, up to 10, saving nothing |
| S-8 Roster | `GET /slots/<id>/roster` | Links with `aria-label="Message <username>"` and `aria-label="Block <username>"` |
| S-9 Message | `GET/POST /volunteers/<username>/message` (field `message`) | Shows `0 of 500 characters`. Sending returns to the roster the link came from, with "Message sent." |
| Block confirm | `GET/POST /volunteers/<username>/block` | Shows the d05-01 confirm wording. "Yes, block" returns to the roster the link came from, with "Blocked." |
| S-10 Blocked Volunteers | `GET /blocked`; undo is `POST /blocked/<username>/undo` from a form whose button has `aria-label="Undo block for <username>"` | |

Times use the 12-hour clock with "a.m." or "p.m." (d05-01 v1.2, UX-6): a
1:00 p.m. slot is `1:00 – 2:00 p.m.` and `1:00 to 2:00 p.m.`; an 11:30
slot is `11:30 a.m. – 12:30 p.m.`.

### Messages

Every message is matched word for word against the UI/UX Document
(d05-01 Section 9). A request that a role isn't allowed to make returns
status 403 with "Not allowed. Please contact the park office if you think
this is wrong."

## Files

| File | Tests |
|---|---|
| `conftest.py` | Shared setup: the app, the test inbox, the clock, test accounts, and helpers |
| `test_uc1_post_task.py` | T-01-01 to T-01-09 |
| `test_uc2_create_account.py` | T-02-01 to T-02-08 |
| `test_uc3_sign_up.py` | T-03-01 to T-03-08 |
| `test_uc4_cancel.py` | T-04-01 to T-04-03 |
| `test_uc5_roster.py` | T-05-01 to T-05-04 |
| `test_uc6_message.py` | T-06-01 to T-06-04 |
| `test_uc7_block.py` | T-07-01 to T-07-05 |
| `test_uc8_delete_task.py` | T-08-01 to T-08-03 (v1.7) |
| `test_security.py` | T-SEC-01 to T-SEC-12 |
| `test_quality.py` | T-QR-01, T-QR-02 (browser) |
| `test_operations.py` | T-EM-01 to T-EM-08, T-DATA-01, T-QR-03, T-QR-04, T-WD-01 to T-WD-03 (added in v1.2 to v1.5) |
| `test_monkey.py` | T-MK-01, T-MK-02 (monkey) |

All test data is made up: usernames like `test_vol_01` and emails ending in
`@example.test`, a domain reserved so it can never reach a real inbox.
