# BeautifulBeachPark Volunteers

A volunteer sign-up app for BeautifulBeachPark, a made-up park. Coordinators
post tasks such as Raking Leaves, Pulling Weeds, Beach Cleanup, and
Driftwood Removal, and volunteers sign up for one-hour slots using a
username only.

This is the **sample project** for the
[AI-Assisted SDLC Workflow](https://github.com/b0ts/ai_assisted_sdlc_workflow).
It shows what your own project folder should look like at each step. The
park, its website, and its people are all made up.

## Folder layout

| Folder | What goes in it |
|---|---|
| [`docs/`](docs/) | The documents each step produces, named by their d-number (for example, `d03-01-prd.md`) |
| [`prompts/`](prompts/) | The prompts used for each step's chat, named by their c-number (for example, `c01-tracking-prompt.md`) |
| [`tests/`](tests/) | Automated tests, written before the code (Step 07: Test Creation) |
| [`src/`](src/) | The project's source code (Step 08: Implementation) |
| [`assets/`](assets/) | Images, media, and data files the project uses |

## Status

Every step's documents are filled in (`docs/d01-01` to `d10-03`), and the
app is real: `src/` holds working code that passes all 38 automated tests
in `tests/`. The story told by the documents (the park, its people, Parks
IT, and the dates) is made up; the code and the test runs are not.

## Try It on Your Own Computer

It runs locally, at no cost, and never sends a real email.

1. Install Python 3.10 or newer from [python.org](https://www.python.org).
2. Open Terminal in this folder and set up the project's Python:

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
3. Run the tests: `pytest -m "not monkey and not browser"` (34 tests, a few
   seconds), or plain `pytest` for all 38 (about 7 minutes).
4. Try the app: in the `src/` folder, run
   `python infrastructure/setup_local.py`, then
   `flask --app bbpv seed-demo`, then `flask --app bbpv run`, and open
   <http://localhost:5000>. Sign in as `sandyhelps@example.test` and find
   the sign-in link in the **pretend inbox**.

Or ask Claude Code: "Set up this sample, run its tests, and start the app."
See [`src/README.md`](src/README.md) and the Developer Guide
([`docs/d08-02-developer-guide.md`](docs/d08-02-developer-guide.md)).
