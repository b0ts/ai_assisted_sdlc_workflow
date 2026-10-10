# Infrastructure

Setup scripts (Infrastructure as Code) from Step 6, Initial Infrastructure.

| File | What it sets up | When |
|---|---|---|
| `setup_local.py` | The local environment: `src/.env` with made-up keys, a local SQLite database, and the pretend inbox | Step 6; anyone working on the code |

The live servers are run by Parks IT. They install the app by following
`docs/d08-02-developer-guide.md` Section 5.1, so there is no script for
them here.
