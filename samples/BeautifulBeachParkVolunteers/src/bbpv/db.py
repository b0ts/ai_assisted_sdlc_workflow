"""The database tables (Spec Section 6) and how the app connects to them.

Works with SQLite (the local environment and the tests) and PostgreSQL
(Parks IT's servers). Email addresses are never stored as plain text: each
account keeps an encrypted copy and two scrambled (hashed) copies used for
looking it up and for the block list.
"""

import sqlalchemy as sa

metadata = sa.MetaData()

accounts = sa.Table(
    "accounts", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String(20), nullable=False),
    sa.Column("username_key", sa.String(20), nullable=False, unique=True),  # lowercase, for "taken"
    sa.Column("role", sa.String(12), nullable=False),  # volunteer, coordinator, admin
    sa.Column("email_encrypted", sa.Text, nullable=False),
    sa.Column("email_lookup", sa.String(64), nullable=False, index=True),  # hash of the lowercase email
    sa.Column("email_block_key", sa.String(64), nullable=False),  # hash of the standardized email
    sa.Column("created", sa.DateTime, nullable=False),
)

tasks = sa.Table(
    "tasks", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(60), nullable=False),
    sa.Column("description", sa.Text, nullable=False, default=""),
    sa.Column("date", sa.Date, nullable=False, index=True),
    sa.Column("posted_by", sa.Integer, sa.ForeignKey("accounts.id", ondelete="SET NULL"), nullable=True),
)

slots = sa.Table(
    "slots", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("task_id", sa.Integer, sa.ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True),
    sa.Column("starts", sa.DateTime, nullable=False, index=True),
    sa.Column("ends", sa.DateTime, nullable=False),
    sa.Column("places", sa.Integer, nullable=False),
    sa.Column("places_left", sa.Integer, nullable=False),
    sa.CheckConstraint("places_left >= 0 AND places_left <= places", name="places_left_in_range"),
)

signups = sa.Table(
    "signups", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("slot_id", sa.Integer, sa.ForeignKey("slots.id", ondelete="CASCADE"), nullable=False),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
    sa.Column("signed_up", sa.DateTime, nullable=False),
    sa.Column("reminder_sent", sa.Boolean, nullable=False, default=False),
    sa.UniqueConstraint("slot_id", "account_id", name="one_signup_per_slot"),
)

block_list = sa.Table(
    "block_list", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email_block_key", sa.String(64), nullable=False, unique=True),
    sa.Column("username", sa.String(20), nullable=True),  # cleared when the account is deleted
    sa.Column("blocked_by", sa.String(20), nullable=False),
    sa.Column("blocked_on", sa.Date, nullable=False),
)

sign_in_links = sa.Table(
    "sign_in_links", metadata,
    sa.Column("token_hash", sa.String(64), primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False),
    sa.Column("expires", sa.DateTime, nullable=False),
)


def make_engine(url, pool_size=15):
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url[len("postgresql://"):]
    if url.startswith("sqlite"):
        engine = sa.create_engine(url, connect_args={"check_same_thread": False, "timeout": 30})

        @sa.event.listens_for(engine, "connect")
        def _sqlite_settings(dbapi_conn, _record):
            cur = dbapi_conn.cursor()
            cur.execute("PRAGMA foreign_keys=ON")
            cur.execute("PRAGMA journal_mode=WAL")
            cur.close()

        return engine
    # Parks IT allows each app 20 connections at once (d06-01 Section 5.1). Each running
    # copy of the app (process) keeps its own pool, so DB_POOL_SIZE times the number of
    # processes must stay under that limit.
    return sa.create_engine(url, pool_size=pool_size, max_overflow=0, pool_pre_ping=True)
