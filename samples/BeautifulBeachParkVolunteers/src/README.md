# Source Code

The BeautifulBeachPark Volunteers app, written in Step 08 (Implementation)
to pass the tests in `../tests/`. How it is organized, set up, run, and
installed on the live servers is in
[`docs/d08-02-developer-guide.md`](../docs/d08-02-developer-guide.md).

## Try It on Your Own Computer

1. Install Python 3.10 or newer, then set up the project's Python in a
   virtual environment, as the sample's [README](../README.md) shows
   (`python3 -m venv .venv`, `source .venv/bin/activate`, then
   `pip install -r src/requirements.txt -r tests/requirements.txt`).
   Then go into this `src/` folder.
2. `python infrastructure/setup_local.py` (makes `src/.env`)
3. `flask --app bbpv seed-demo` (made-up accounts and tasks)
4. `flask --app bbpv run`, then open <http://localhost:5000>
5. Sign in as `sandyhelps@example.test` (a volunteer),
   `democoordinator@example.test`, or `demoadmin@example.test`. No email is
   sent: open the **pretend inbox** link on the sign-in page to find the
   sign-in link.

Or ask Claude Code: "Set up the local environment and start the app."

| Folder or file | What it holds |
|---|---|
| `bbpv/__init__.py` | Builds the app; reads every setting from the environment |
| `bbpv/views.py` | Screens S-1 to S-10 and the rules behind each request |
| `bbpv/db.py` | The database tables |
| `bbpv/privacy.py` | Email encryption, scrambled copies, and the standardized email |
| `bbpv/mail.py` | Sending email: test inbox, pretend inbox, or the city email service |
| `bbpv/cli.py` | Commands: create and delete accounts, the reminder job, demo data |
| `bbpv/wording.py` | Every message people see |
| `bbpv/templates/`, `bbpv/static/` | Page layouts and styles |
| `infrastructure/` | Local environment setup |
