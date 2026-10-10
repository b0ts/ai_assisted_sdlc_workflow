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
4. Before sign-off, run plain `pytest` to run all 38.

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
| `DATABASE_URL` | A SQLite file, or `TEST_DATABASE_URL` | Store everything there, creating the tables if they're missing |
| `CLOCK` | A function returning the current park time (a `datetime` with no time zone) | Use it for **every** "now": slot started, tomorrow's reminders, link expiry |
| `TEST_INBOX` | An empty Python list | Instead of sending email, append one dictionary per email: `{"to", "from", "subject", "text"}` |
| `SECRET_KEY` | A test-only value | Sign sessions and sign-in links |
| `BASE_URL` | `https://volunteers.example.test` | Start the links in emails with it |
| `FORCE_HTTPS` | Left out (browser tests pass `False`) | By default, send any `http://` request to `https://` (T-SEC-02) |

- The app keeps its own encryption key for stored emails. In testing it may
  make one up.

### Commands (for the System Administrator and the daily job)

Run with `flask --app bbpv <command>`. The tests call them through Flask's
command runner.

| Command | What it does |
|---|---|
| `create-account USERNAME EMAIL --role volunteer\|coordinator\|admin` | Creates an account (how coordinator and admin accounts are made) |
| `delete-account USERNAME` | Deletes an account; its block list entry stays (T-SEC-03) |
| `send-reminders` | The reminder job: emails everyone signed up for a slot tomorrow |

### Screens and addresses

Pages are ordinary HTML. Confirm boxes (cancel, block) also work as their own
page, so everything works without JavaScript.

| Screen | Address | Notes for the tests |
|---|---|---|
| S-1 Sign In | `GET/POST /sign-in` (field `email`); the emailed link is `/sign-in/<token>` | |
| S-2 Create Account | `GET/POST /create-account` (fields `username`, `email`, checkbox `privacy_accepted`) | |
| S-3 Open Slots | `GET /slots` | Each slot shows its time, then its places: `9:00 – 10:00` (en dash), then `2 places left`, `1 place left`, or `Full`. Each open slot has a link to S-4 with `aria-label="Sign up for <title>, 9 to 10"` |
| S-4 Confirm Sign-Up | `GET /slots/<id>/confirm`; confirming is `POST /slots/<id>/sign-up` | |
| S-5 My Sign-Ups | `GET /my-sign-ups` | Each sign-up has a link to its cancel page with `aria-label="Cancel <title>, April 21, 9 to 10"` |
| Cancel confirm | `GET/POST /sign-ups/<id>/cancel` | The page has a "Yes, cancel" button |
| S-6 My Tasks | `GET /my-tasks` | A table row per slot: title, time, `2 of 2` (plus `(Full)` when full), and a link with `aria-label="Roster for <title>, 9 to 10"` |
| S-7 Post a Task | `GET/POST /tasks/new` | Fields `title`, `description`, `date` (`2027-04-21`), and for each slot `slot_start`, `slot_end` (`09:00`), `places`, repeated in order |
| S-8 Roster | `GET /slots/<id>/roster` | Links with `aria-label="Message <username>"` and `aria-label="Block <username>"` |
| S-9 Message | `GET/POST /volunteers/<username>/message` (field `message`) | |
| Block confirm | `GET/POST /volunteers/<username>/block` | Shows the d05-01 confirm wording |
| S-10 Blocked Volunteers | `GET /blocked`; undo is `POST /blocked/<username>/undo` from a form whose button has `aria-label="Undo block for <username>"` | |

Times in labels use the 12-hour clock without "a.m." or "p.m.", as in the
mockups: a 1:00 p.m. slot is `1:00 – 2:00` and `1 to 2`.

### Messages

Every message is matched word for word against the UI/UX Document
(d05-01 Section 9). A request that a role isn't allowed to make returns
status 403 with "Not allowed. Please contact the park office if you think
this is wrong."

## Files

| File | Tests |
|---|---|
| `conftest.py` | Shared setup: the app, the test inbox, the clock, test accounts, and helpers |
| `test_uc1_post_task.py` | T-01-01 to T-01-05 |
| `test_uc2_create_account.py` | T-02-01 to T-02-05 |
| `test_uc3_sign_up.py` | T-03-01 to T-03-07 |
| `test_uc4_cancel.py` | T-04-01 to T-04-03 |
| `test_uc5_roster.py` | T-05-01 to T-05-04 |
| `test_uc6_message.py` | T-06-01, T-06-02 |
| `test_uc7_block.py` | T-07-01 to T-07-03 |
| `test_security.py` | T-SEC-01 to T-SEC-05 |
| `test_quality.py` | T-QR-01, T-QR-02 (browser) |
| `test_monkey.py` | T-MK-01, T-MK-02 (monkey) |

All test data is made up: usernames like `test_vol_01` and emails ending in
`@example.test`, a domain reserved so it can never reach a real inbox.
