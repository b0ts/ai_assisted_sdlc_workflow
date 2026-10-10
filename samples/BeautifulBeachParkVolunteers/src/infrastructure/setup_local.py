"""Set up the local environment (d06-01 Section 11): free, on your own computer.

Run from the src/ folder:   python infrastructure/setup_local.py

It writes src/.env with fresh, made-up keys, a local SQLite database, and
the pretend inbox, so nothing is ever emailed. It never overwrites an
existing src/.env.
"""

import pathlib
import secrets
import sys

from cryptography.fernet import Fernet

env = pathlib.Path(__file__).resolve().parent.parent / ".env"
if env.exists():
    print(f"{env} already exists; leaving it as it is.")
    sys.exit(0)

env.write_text(
    "# Local environment only: made-up keys, a local database, and the pretend inbox.\n"
    "DATABASE_URL=sqlite:///bbpv-local.db\n"
    f"SECRET_KEY={secrets.token_hex(32)}\n"
    f"EMAIL_ENCRYPTION_KEY={Fernet.generate_key().decode()}\n"
    "BASE_URL=http://localhost:5000\n"
    "EMAIL_SERVICE=pretend\n"
    "FORCE_HTTPS=false\n"
)
print(f"Wrote {env}. Next, from the src/ folder:")
print("  flask --app bbpv seed-demo     # made-up accounts and tasks for the demo")
print("  flask --app bbpv run           # then open http://localhost:5000")
