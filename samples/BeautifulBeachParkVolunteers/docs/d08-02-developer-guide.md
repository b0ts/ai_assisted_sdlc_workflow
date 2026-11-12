# BeautifulBeachPark Volunteers: Developer Guide

**Document:** d08-02 · **Step:** 8, Implementation · **Version:** 1.4
· **Last updated:** 2026-11-12 · **Status:** Approved
· **Owner:** Software Engineer (Implementation chat)

> **Sample document.** BeautifulBeachPark, its city, and Parks IT are made
> up. The code is real: this guide describes the working app in `src/`.

## 1. Overview

| Item | Details |
|---|---|
| Product | BeautifulBeachPark Volunteers |
| Software version | 1.0 |
| What the code does, in one sentence | A Python web service and web pages that let coordinators post one-hour volunteer slots and volunteers sign up with only a username, without ever showing anyone's email. |
| Where the code lives | `src/` |
| Where the tests live | `tests/` |
| Related documents | d04-01 Spec, d06-01 System Infrastructure Document, d07-01 Test Plan, d08-01 Implementation Record |

## 2. How the Code Is Organized

| Folder or file | What it holds | Spec component |
|---|---|---|
| `src/bbpv/__init__.py` | Builds the app and reads every setting from the environment; turns plain HTTP away | Application server |
| `src/bbpv/views.py` | Screens S-1 to S-10 and every request behind them, each checking who is asking | Application server, Client |
| `src/bbpv/templates/` | The page layouts for S-1 to S-10, built from `assets/mockups/` | Client |
| `src/bbpv/static/style.css` | Colors, fonts, and spacing, taken from `assets/design-tokens.json` | Client |
| `src/bbpv/wording.py` | Every message people see, in one place, so other languages can be added later (Spec Section 10) | Client and Application server |
| `src/bbpv/cli.py` | Commands: create and delete accounts, the scheduled jobs (reminders, sending queued emails, the 12-month clean-up), demo data | Scheduled jobs; System Administrator |
| `src/bbpv/db.py` | The database tables, including the email queue (`outbox`) | Database |
| `src/bbpv/privacy.py` | Email encryption, the scrambled copies, and the standardized email (Spec Section 6) | Application server |
| `src/bbpv/mail.py` | Sending email: the test inbox, the pretend inbox, or the city email service | Email service |
| `src/infrastructure/setup_local.py` | Sets up the local environment | — |
| `src/requirements.txt` | The outside libraries (see Section 7) | — |

```mermaid
flowchart LR
    P["templates/ and static/<br/>(screens S-1 to S-10)"] --> S["views.py<br/>(requests and rules)"]
    S --> D[("db.py<br/>SQLite locally;<br/>PostgreSQL live")]
    J["cli.py<br/>send-reminders, send-emails,<br/>clean-up"] --> D
    S --> V["privacy.py<br/>(encrypt, scramble)"]
    S --> M["mail.py<br/>(pretend inbox locally;<br/>city email service live)"]
    J --> M
    W["wording.py"] --> P
    W --> S
```

**The one rule to remember:** email addresses are decrypted in exactly one
place, `deliver()` in `views.py`, and only to send an email. No page in
`templates/` ever receives one (Spec Section 11). T-SEC-01 and T-SEC-03
check this.

**How email works (Spec DD-6):** nothing is emailed directly. Each email is
saved to the queue (`queue_email()`), encrypted, in the same step as the
change it's about. The page that queued it tries to send it once, waiting
at most `EMAIL_SEND_TIMEOUT` seconds in all (a slow send finishes in the
background), and never sends anyone else's. If the
email service doesn't answer, the email stays queued and `send-emails`
retries it every 5 minutes until it expires: a sign-in email with its link,
a confirmation or reminder when the slot starts, a message after 3 days. A
failure is recorded as a short reason, never with the address or the
service's own reply.

**All wording lives in `wording.py`:** messages, emails, every heading,
label, and button, and the words in times (a.m., p.m.). The page templates hold no words of their own; T-WD-02
checks this.

## 3. Setting Up

1. Install **Python** (version 3.10 or newer) from python.org.
2. Install **Visual Studio Code**, and from its **Extensions** panel (the
   icon of four squares in the left sidebar), add the **Python**
   extension.
3. Copy the project to your computer from the park's GitHub repository:
   on GitHub, choose the green **Code** button, then **Download ZIP**, and
   unzip it. (Or use GitHub Desktop's **File | Clone Repository...**, or
   ask Claude Code to copy it for you.)
4. In Visual Studio Code, choose **File**, then **Open Folder**, and open
   the project folder.
5. Set up a **virtual environment** (a private copy of Python for this
   project, in a `.venv` folder that Git ignores). Ask Claude Code to
   "create a .venv virtual environment, install `src/requirements.txt`
   and `tests/requirements.txt`, and install Playwright's Chromium," or
   in Visual Studio Code choose **View**, then **Command Palette...**, type
   **Python: Create Environment**, choose **Venv**, and tick both
   requirements files. A plain `pip install` without one fails on Python
   from Homebrew with an "externally-managed-environment" error.
   Visual Studio Code then uses `.venv` automatically; if not, click the
   Python version in the status bar at the bottom of the window and pick
   the one marked `.venv`.
6. Ask Claude Code to "set up the local environment" (it runs
   `python infrastructure/setup_local.py` in the `src/` folder). This
   writes `src/.env` with made-up keys, a local database, and a pretend
   inbox that catches every email. You never need the live servers'
   settings to work on the code.

## 4. Running the App and the Tests

| Task | How |
|---|---|
| Add made-up accounts and tasks | In the `src/` folder: `flask --app bbpv seed-demo` |
| Run the app on your own computer | In the `src/` folder: `flask --app bbpv run --port 5050`, then open <http://127.0.0.1:5050> (on a Mac, port 5000 belongs to AirPlay Receiver), or double-click `start-demo.command` in the sample folder. (After updating to v1.3, delete `src/bbpv-local.db` once and run `seed-demo` again: the email queue table changed in round 2, R2-14, and the app can't change existing tables.) Sign in as `sandyhelps@example.test` (volunteer), `democoordinator@example.test`, or `demoadmin@example.test`, and find the sign-in link in the **pretend inbox** (linked from the sign-in page). This is also how the stakeholder demo is run in Step 9. |
| Send tomorrow's reminders by hand | `flask --app bbpv send-reminders` (they appear in the pretend inbox) |
| Send queued emails by hand | `flask --app bbpv send-emails` |
| Remove tasks older than 12 months | `flask --app bbpv clean-up` |
| Run every test | In Visual Studio Code, choose the **Testing** icon (a beaker) in the left sidebar, then **Run Tests**. Or, in the project folder, run `pytest`. Or ask Claude Code to "run all the tests." The tests use a throwaway database and never send email. |
| Run the quick tests while working | `pytest -m "not monkey and not browser"`: 70 tests in a few seconds |
| Run one test | In the **Testing** panel, find the test by its ID (for example, `test_t_03_02`) and choose its run button. |
| Where results go | Add a Run History row to `docs/d07-02-test-results.md` after every full run. |

## 5. Settings and Secrets

Every setting comes from an **environment variable**, so the same code
runs on your computer and on Parks IT's servers; only the values change.

| Setting | What it controls | Locally | On Parks IT's servers |
|---|---|---|---|
| `DATABASE_URL` | Which database the app uses | The local test database | Parks IT's secret store (d06-01 Section 7.2) |
| `EMAIL_ENCRYPTION_KEY` | Encrypts volunteer emails | A made-up key in the local settings file | Parks IT's secret store |
| `EMAIL_SERVICE` | Where emails go | `pretend`: the pretend inbox | `smtp`: the city email service |
| `BASE_URL` | The web address used in emailed links | `http://127.0.0.1:5050` | The app's `volunteers.` address |
| `SECRET_KEY` | Signs sessions | A made-up value | Parks IT's secret store |
| `FORCE_HTTPS` | Sends plain HTTP to HTTPS (Spec 11.1) | `false` (the laptop has no certificate) | `true` (the default) |
| `TRUST_PROXY` | Trusts Parks IT's web server to say the visitor used HTTPS | Not set | `true` |
| `DB_POOL_SIZE` | Database connections each copy of the app may keep | Not needed | `4`: Parks IT runs 4 copies, and allows 20 connections in all (d06-01 v1.2) |
| `PARK_TIMEZONE` | The park's time zone, used for every "now" (Spec DD-8) | `America/Los_Angeles` (the default) | `America/Los_Angeles` (d06-01 v1.4) |
| `EMAIL_SEND_TIMEOUT` | Seconds a page waits for the email service before leaving its email to the 5-minute job. The sign-in and create-account pages never wait (Spec DD-10) | `5` (the default) | `5` |
| `EMAIL_FROM`, `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD` | The sending address and the city email service | Not needed | From Parks IT; the password in their secret store |
| `SMTP_CA_FILE` | The certificate authority used to check the email service's certificate, if Parks IT uses its own (otherwise the computer's standard ones are used) | Not needed | Only if Parks IT says so (d06-01 v1.5) |

**Never change or lose `EMAIL_ENCRYPTION_KEY`.** The app finds accounts
and checks the block list with scrambled copies made from this key. With a
new key, or none, no one can sign in and every block stops working. Keep a
copy in Parks IT's secret store and its backup (round 2, R2-11).

The local settings file is listed in `.gitignore`, so it never goes to
GitHub. Never copy any real value into the code, a document, or a chat.

### 5.1 Installing on the Live Servers

Parks IT follows these steps in Step 9, after the stakeholders approve the
demo, on a Tuesday evening (d06-01 Section 5.1):

1. Install the tagged version (for example, `v1.0`) from the park's GitHub
   repository, with Python 3.12, and install `src/requirements.txt` plus
   `psycopg[binary]` (for PostgreSQL).
2. Create the app's database on the PostgreSQL 16 server, and set the
   environment variables above from Parks IT's secret store.
3. Start the app as a service behind Parks IT's web server, with HTTPS,
   using the Waitress production web server (installed by
   `src/requirements.txt`), from the `src/` folder:
   `waitress-serve --listen=127.0.0.1:8000 --threads=4 --call bbpv:create_app`.
   Four threads match `DB_POOL_SIZE` 4. Never use `flask run` on the live
   servers: it's Flask's development server (d06-01 v1.5). The app creates
   its database tables the first time it starts; later changes to the
   tables need manual steps (round 2, R2-12).
4. Add three jobs to Parks IT's scheduler (d06-01 v1.4): a daily 6 p.m.
   job that runs `flask --app bbpv send-reminders`; one every 5 minutes
   that runs `flask --app bbpv send-emails`, with its output emailed to the
   Volunteer Program Manager when it warns; and a daily 3 a.m. job that
   runs `flask --app bbpv clean-up`.
5. Run the full test suite against the live servers, using a test
   database, and record the run in `docs/d07-02-test-results.md`.
6. Create the System Administrator's account with
   `flask --app bbpv create-account <username> <email> --role admin`.

## 6. Making a Change

1. **Write or ask for a test first.** A new feature or a bug fix starts
   with a failing test, written or approved through the SDET chat.
2. **Change the code** until the new test, and every old test, passes.
3. **Record the run** in d07-02.
4. **Have a person review** the change before it goes live.
5. **Put new wording in `src/bbpv/wording.py`**, never directly in a page,
   and use the exact words from the UI/UX Document.
6. **Never send an email address to a page.** T-SEC-01 will catch it, but
   don't rely on the test alone.

## 7. Libraries and Licenses

| Library | What it is used for | Version | License | May we use it? |
|---|---|---|---|---|
| Flask | The web framework for the application server | See `src/requirements.txt` | BSD-3-Clause | Yes |
| SQLAlchemy | Talks to the database (SQLite or PostgreSQL) | See `src/requirements.txt` | MIT | Yes |
| cryptography | Encrypts volunteer emails | See `src/requirements.txt` | Apache-2.0 or BSD-3-Clause | Yes |
| python-dotenv | Reads `src/.env` in the local environment | See `src/requirements.txt` | BSD-3-Clause | Yes |
| tzdata | Time zone data, for `PARK_TIMEZONE` on computers that lack it | See `src/requirements.txt` | Apache-2.0 | Yes |
| Waitress | The production web server on Parks IT's servers (Section 5.1) | See `src/requirements.txt` | ZPL-2.1 | Yes |
| psycopg | Talks to PostgreSQL on Parks IT's servers | 3.1 or newer | LGPL-3.0 | Yes, used unchanged as a library |
| pytest | Runs the tests | See `tests/requirements.txt` | MIT | Yes |
| Playwright for Python | Drives a real browser in T-QR-01 and T-QR-02 | Latest | Apache-2.0 | Yes |

## 8. Known Limits and Troubleshooting

| Problem | Likely cause | What to do |
|---|---|---|
| Tests show **Blocked** | The local database isn't running | Ask Claude Code to "start the local environment" (d06-01, ongoing DevOps support) |
| Email tests fail, other tests pass | `EMAIL_SERVICE` isn't set to the pretend inbox | Check the local settings file |
| Slot pages are slow | A missing database index after a database change | Check `src/bbpv/db.py`; T-QR-01 measures this |
| Emails aren't arriving | The email service is down, or rejecting the app | Run `flask --app bbpv send-emails`: it says how many are waiting, and warns after an hour. They're sent once the service answers |
| A new screen looks "off" | Styles written by hand instead of from the design tokens | Use `src/bbpv/static/style.css`, built from `assets/design-tokens.json` |

## 9. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-12-11 | First version | — | Park Manager (D12, 2026-12-11) |
| 1.1 | 2026-10-25 | Email queue and `send-emails`; `clean-up`; `PARK_TIMEZONE`; tzdata; decryption now in `deliver()` | Round 1 code review fixes (d08-04-code-review-codex.md) | Park Manager, 2026-10-25 |
| 1.2 | 2026-10-26 | Pages send only their own email (`EMAIL_SEND_TIMEOUT`); fixed 5-minute retries and expiry; safe failure reasons; all screen text in `wording.py` | Round 1 re-review (Codex), R-2, R-5, R-14, R-15 | Park Manager, 2026-10-26 |
| 1.3 | 2026-11-11 | Waitress production server and start command; recreate the local database after updating (R2-14); `SMTP_CA_FILE`; never change `EMAIL_ENCRYPTION_KEY`; sign-in pages don't wait for email | Round 2 code review (Claude Code), R2-3, R2-6, R2-7, R2-11, R2-12 | Park Manager, 2026-11-11 |
| 1.4 | 2026-11-12 | The app runs on port 5050 (`start-demo.command`, `BASE_URL`); 70 quick tests | Polishing (d08-06); round 2 re-review of polishing, R2-22 | Park Manager, 2026-11-12 |
