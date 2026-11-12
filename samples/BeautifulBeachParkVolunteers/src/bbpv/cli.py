"""Commands for the System Administrator and the daily job.

Run with `flask --app bbpv <command>` (d08-02 Section 5.1).
"""

import datetime as dt
import re

import click
import sqlalchemy as sa
from flask import current_app

from . import db
from .privacy import EmailVault, looks_like_email


def register(app):
    @app.cli.command("create-account")
    @click.argument("username")
    @click.argument("email")
    @click.option("--role", type=click.Choice(["volunteer", "coordinator", "admin"]), default="volunteer")
    def create_account(username, email, role):
        """Create an account (how coordinator and admin accounts are made)."""
        if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
            raise click.ClickException("Usernames are 3 to 20 letters, numbers, or underscores.")
        if not looks_like_email(email):
            raise click.ClickException("That doesn't look like an email address.")
        vault = current_app.extensions["vault"]
        with current_app.extensions["engine"].begin() as conn:
            if conn.execute(sa.select(db.accounts.c.id).where(db.accounts.c.username_key == username.lower())).first():
                raise click.ClickException("That username is taken.")
            if conn.execute(sa.select(db.accounts.c.id).where(
                    db.accounts.c.email_lookup == vault.lookup_key(email))).first():
                raise click.ClickException("An account already uses that email.")
            conn.execute(db.accounts.insert().values(
                username=username, username_key=username.lower(), role=role,
                email_encrypted=vault.encrypt(email), email_lookup=vault.lookup_key(email),
                email_block_key=vault.block_key(email), created=current_app.config["CLOCK"]()))
        click.echo(f"Created {role} account {username}.")

    @app.cli.command("delete-account")
    @click.argument("username")
    def delete_account(username):
        """Delete an account. Its block list entry stays, as a scrambled copy only."""
        with current_app.extensions["engine"].begin() as conn:
            account = conn.execute(db.accounts.select().where(
                db.accounts.c.username_key == username.lower())).mappings().first()
            if account is None:
                raise click.ClickException("No account has that username.")
            slot_ids = conn.execute(sa.select(db.signups.c.slot_id).where(
                db.signups.c.account_id == account["id"])).scalars().all()
            for slot_id in slot_ids:  # give the places back
                conn.execute(db.slots.update().where(db.slots.c.id == slot_id)
                             .values(places_left=db.slots.c.places_left + 1))
            conn.execute(db.signups.delete().where(db.signups.c.account_id == account["id"]))
            conn.execute(db.sign_in_links.delete().where(db.sign_in_links.c.account_id == account["id"]))
            conn.execute(db.outbox.delete().where(db.outbox.c.account_id == account["id"]))
            conn.execute(db.sign_in_emails.delete().where(db.sign_in_emails.c.email_lookup == account["email_lookup"]))
            conn.execute(db.tasks.update().where(db.tasks.c.posted_by == account["id"]).values(posted_by=None))
            conn.execute(db.block_list.update().where(db.block_list.c.username == account["username"])
                         .values(username=None))
            conn.execute(db.accounts.delete().where(db.accounts.c.id == account["id"]))
        click.echo(f"Deleted {username}.")

    @app.cli.command("send-reminders")
    def send_reminders():
        """The daily reminder job (6 p.m.): email everyone signed up for a slot tomorrow.

        Each reminder is queued and marked as sent in one step, so running the job
        again never sends a second one, even after the email service was down.
        """
        from . import wording as w
        from .views import day_heading, queue_email, send_due_emails, slot_time

        tomorrow = current_app.config["CLOCK"]().date() + dt.timedelta(days=1)
        start = dt.datetime.combine(tomorrow, dt.time())
        end = start + dt.timedelta(days=1)
        eng = current_app.extensions["engine"]
        with eng.connect() as conn:
            rows = conn.execute(
                sa.select(db.signups.c.id, db.signups.c.account_id, db.accounts.c.username,
                          db.slots.c.starts, db.slots.c.ends, db.tasks.c.title, db.tasks.c.description)
                .join(db.accounts, db.accounts.c.id == db.signups.c.account_id)
                .join(db.slots, db.slots.c.id == db.signups.c.slot_id)
                .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
                .where(db.slots.c.starts >= start, db.slots.c.starts < end,
                       db.signups.c.reminder_sent.is_(False))
            ).mappings().all()
        queued = 0
        for row in rows:
            with eng.begin() as conn:
                # Claim this reminder first: if another run already did, skip it (R-2)
                claimed = conn.execute(db.signups.update().where(
                    db.signups.c.id == row["id"], db.signups.c.reminder_sent.is_(False)
                ).values(reminder_sent=True)).rowcount
                if claimed != 1:
                    continue
                queue_email(conn, row["account_id"], w.reminder_email(
                    row["username"], row["title"], day_heading(tomorrow),
                    slot_time(row["starts"], row["ends"]), row["description"]), expires=row["starts"])
                queued += 1
        sent, waiting = send_due_emails()
        click.echo(f"Queued {queued} reminder(s) for {tomorrow.isoformat()}; "
                   f"sent {sent} email(s); {waiting} waiting.")

    @app.cli.command("send-emails")
    def send_emails():
        """Send queued emails and retry ones that failed (every 5 minutes; Spec DD-6)."""
        from .views import send_due_emails

        sent, waiting = send_due_emails()
        click.echo(f"Sent {sent} email(s); {waiting} waiting.")
        hour_ago = current_app.config["CLOCK"]() - dt.timedelta(hours=1)
        with current_app.extensions["engine"].connect() as conn:
            stuck = conn.execute(sa.select(sa.func.count()).select_from(db.outbox).where(
                db.outbox.c.created < hour_ago)).scalar()
        if stuck:
            click.echo(f"Warning: {stuck} email(s) have waited more than an hour. "
                       "The email service may be down (d06-01 Section 9).")

    @app.cli.command("clean-up")
    def clean_up():
        """The daily clean-up: remove tasks 12 months after their date, with their slots
        and sign-ups (Spec Section 6). The block list is never touched."""
        today = current_app.config["CLOCK"]().date()
        try:
            cutoff = today.replace(year=today.year - 1)
        except ValueError:  # February 29
            cutoff = today.replace(year=today.year - 1, day=28)
        now = current_app.config["CLOCK"]()
        with current_app.extensions["engine"].begin() as conn:
            old_tasks = sa.select(db.tasks.c.id).where(db.tasks.c.date < cutoff)
            old_slots = sa.select(db.slots.c.id).where(db.slots.c.task_id.in_(old_tasks))
            signups = conn.execute(db.signups.delete().where(db.signups.c.slot_id.in_(old_slots))).rowcount
            conn.execute(db.slots.delete().where(db.slots.c.task_id.in_(old_tasks)))
            tasks = conn.execute(db.tasks.delete().where(db.tasks.c.date < cutoff)).rowcount
            conn.execute(db.sign_in_links.delete().where(db.sign_in_links.c.expires < now))
            conn.execute(db.sign_in_emails.delete().where(db.sign_in_emails.c.sent < now - dt.timedelta(hours=24)))
        click.echo(f"Removed {tasks} task(s) dated before {cutoff.isoformat()}, with {signups} sign-up(s).")

    @app.cli.command("new-key")
    def new_key():
        """Print a new EMAIL_ENCRYPTION_KEY, to keep in the secret store."""
        click.echo(EmailVault.new_key())

    @app.cli.command("seed-demo")
    def seed_demo():
        """Fill the local environment with made-up accounts and tasks for the stakeholder demo."""
        if not current_app.config["DATABASE_URL"].startswith("sqlite"):
            raise click.ClickException("seed-demo is for the local environment only.")
        runner = current_app.test_cli_runner()
        people = [("DemoCoordinator", "coordinator"), ("DemoAdmin", "admin"),
                  ("SandyHelps", "volunteer"), ("ShellSeeker", "volunteer"), ("TidePoolTim", "volunteer")]
        for name, role in people:
            runner.invoke(args=["create-account", name, f"{name.lower()}@example.test", "--role", role])
        vault = current_app.extensions["vault"]
        today = current_app.config["CLOCK"]().date()
        with current_app.extensions["engine"].begin() as conn:
            coord = conn.execute(sa.select(db.accounts.c.id).where(
                db.accounts.c.email_lookup == vault.lookup_key("democoordinator@example.test"))).scalar()
            for offset, title, desc, hours in [
                (2, "Beach Cleanup", "Bring a hat and water. Gloves and bags provided.", (9, 10, 11)),
                (2, "Pulling Weeds", "In the dune garden by the north entrance.", (9,)),
                (3, "Driftwood Removal", "Meet at the south parking lot.", (13, 14)),
            ]:
                day = today + dt.timedelta(days=offset)
                task_id = conn.execute(db.tasks.insert().values(
                    title=title, description=desc, date=day, posted_by=coord)).inserted_primary_key[0]
                for h in hours:
                    starts = dt.datetime.combine(day, dt.time(h))
                    conn.execute(db.slots.insert().values(task_id=task_id, starts=starts,
                                                          ends=starts + dt.timedelta(hours=1), places=4, places_left=4))
        click.echo("Demo data added. Sign in as democoordinator@example.test, sandyhelps@example.test, "
                   "or demoadmin@example.test, then open the pretend inbox.")
