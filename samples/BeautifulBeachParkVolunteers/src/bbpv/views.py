"""The screens S-1 to S-10 and the requests behind them (Spec Section 7).

Every request checks who is asking (Spec Section 11.1). No page is ever
given an email address: they are decrypted only in deliver(), and only to
send an email. Every email goes through the outbox (Spec DD-6).
"""

import datetime as dt
import functools
import re
import secrets
import threading

import sqlalchemy as sa
from flask import Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for

from . import db, mail, wording as w
from .privacy import looks_like_email, token_hash

bp = Blueprint("main", __name__)

USERNAME_RE = re.compile(r"[A-Za-z0-9_]{3,20}")
TIME_RE = re.compile(r"([01]\d|2[0-3]):([0-5]\d)")
MAX_SLOTS = 10
FORM_ROWS = 3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def engine():
    return current_app.extensions["engine"]


def one_line_break(value):
    """Browsers send each line break as two characters; count it as one, as the
    on-screen counter does (PRD v1.3, UC-1 and UC-6; round 2, R2-1)."""
    return value.replace("\r\n", "\n").replace("\r", "\n")


def vault():
    return current_app.extensions["vault"]


def now():
    return current_app.config["CLOCK"]()


def clock_time(t):
    """9:00, 1:30 (12-hour clock)."""
    return f"{t.hour % 12 or 12}:{t.minute:02d}"


def _period(t):
    return w.MORNING if t.hour < 12 else w.EVENING


def _span(starts, ends, joiner):
    """a.m. or p.m. once when both ends share it, on both ends when they don't (d05-01 v1.2, UX-6)."""
    if _period(starts) == _period(ends):
        return f"{clock_time(starts)}{joiner}{clock_time(ends)} {_period(ends)}"
    return f"{clock_time(starts)} {_period(starts)}{joiner}{clock_time(ends)} {_period(ends)}"


def slot_time(starts, ends):
    """'9:00 – 10:00 a.m.', '11:30 a.m. – 12:30 p.m.'"""
    return _span(starts, ends, w.RANGE_DASH)


def hours_label(starts, ends):
    """'9:00 to 10:00 a.m.': used in accessible button names (d05-01 Section 10)."""
    return _span(starts, ends, w.RANGE_TO)


def day_heading(day):
    return f"{day.strftime('%A')}, {day.strftime('%B')} {day.day}"


def day_label(day):
    return f"{day.strftime('%B')} {day.day}"


def short_day(day):
    return f"{day.strftime('%a')}, {day.strftime('%b')} {day.day}"


@bp.app_template_filter("slot_time")
def _slot_time_filter(row):
    return slot_time(row["starts"], row["ends"])


@bp.app_template_filter("hours")
def _hours_filter(row):
    return hours_label(row["starts"], row["ends"])


@bp.app_template_filter("day_heading")
def _day_heading_filter(day):
    return day_heading(day)


@bp.app_template_filter("day_label")
def _day_label_filter(day):
    return day_label(day)


@bp.app_template_filter("short_day")
def _short_day_filter(day):
    return short_day(day)


@bp.app_template_filter("places_text")
def _places_text(left):
    return w.places_text(left)


def not_allowed():
    return render_template("message.html", title=w.TITLE_NOT_ALLOWED, banner=("error", w.NOT_ALLOWED)), 403


def page_not_found():
    return render_template("message.html", title=w.TITLE_NOT_FOUND, banner=("error", w.NOT_FOUND)), 404


def signed_in(*roles):
    """Only signed-in people with one of these roles may use the page."""
    def decorate(view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            if g.user is None:
                return redirect(url_for("main.sign_in"))
            if roles and g.user["role"] not in roles:
                return not_allowed()
            return view(*args, **kwargs)
        return wrapper
    return decorate


def home_for(user):
    return {
        "coordinator": url_for("main.my_tasks"),
        "admin": url_for("main.blocked_volunteers"),
    }.get(user["role"], url_for("main.open_slots"))


# ---------------------------------------------------------------------------
# Email: queue first, then send (Spec DD-6)
# ---------------------------------------------------------------------------

RETRY_MINUTES = 5            # a failed email is tried again every 5 minutes (Spec 7, 14)
MESSAGE_KEEP_DAYS = 3        # a coordinator's message is dropped if it can't be sent in 3 days
SIGN_IN_EMAILS_PER_DAY = 10  # PRD 6, Email limits; Spec DD-9


def queue_email(conn, account_id, subject_and_text, expires=None, to_encrypted=None):
    """Save an email to send, in the same step as the change it's about. Returns its id.
    An account request's email has no account yet: it goes to `to_encrypted` (Spec DD-13)."""
    subject, text = subject_and_text
    v = vault()
    return conn.execute(db.outbox.insert().values(
        account_id=account_id, to_encrypted=to_encrypted,
        subject_encrypted=v.encrypt_text(subject), text_encrypted=v.encrypt_text(text),
        created=now(), send_after=now(), attempts=0, expires=expires)).inserted_primary_key[0]


def deliver(row, timeout):
    """The only place an email address is decrypted, and only to send to it.

    The address is read with a short database step that ends before sending
    starts, so no connection is held while the email service works (Spec DD-12;
    round 1, R-18; round 2, R2-5).
    """
    if row["account_id"] is None:
        to_encrypted = row["to_encrypted"]
    else:
        with engine().connect() as conn:
            to_encrypted = conn.execute(sa.select(db.accounts.c.email_encrypted).where(
                db.accounts.c.id == row["account_id"])).scalar()
    if to_encrypted is None:
        return
    v = vault()
    mail.send(v.decrypt(to_encrypted), v.decrypt_text(row["subject_encrypted"]),
              v.decrypt_text(row["text_encrypted"]), timeout=timeout)


def safe_error(e):
    """What went wrong, in words that never include an address or the service's own reply (R-14)."""
    import smtplib
    if isinstance(e, smtplib.SMTPRecipientsRefused):
        return "The email service refused the recipient"
    if isinstance(e, smtplib.SMTPResponseException):
        return f"The email service answered with code {e.smtp_code}"
    if isinstance(e, (smtplib.SMTPServerDisconnected, ConnectionError, TimeoutError, OSError)):
        return "Couldn't reach the email service"
    return f"Sending failed ({type(e).__name__})"


def send_due_emails(ids=None, timeout=20):
    """Send queued emails that are due: all of them (the 5-minute job), or only `ids`
    (a page sending its own). Returns (sent, still waiting). Never raises.

    Each email is claimed before it is sent, so two copies of the app running at
    once never both send it. A failure is tried again in 5 minutes; an email past
    its expiry (a sign-in link that has run out, a slot that has started) is dropped.
    If the app stops just after the email service accepts an email but before the
    queue is updated, that one email can be sent twice (Spec DD-6).
    """
    sent = 0
    eng = engine()
    query = sa.select(db.outbox).where(db.outbox.c.send_after <= now()).order_by(db.outbox.c.id)
    if ids is not None:
        ids = [i for i in ids if i is not None]
        if not ids:
            return 0, None
        query = query.where(db.outbox.c.id.in_(ids))
    with eng.connect() as conn:
        due = conn.execute(query).mappings().all()
    for row in due:
        try:
            with eng.begin() as conn:
                if row["expires"] is not None and row["expires"] < now():
                    conn.execute(db.outbox.delete().where(db.outbox.c.id == row["id"]))
                    continue
                claimed = conn.execute(db.outbox.update().where(
                    db.outbox.c.id == row["id"], db.outbox.c.send_after == row["send_after"]
                ).values(send_after=now() + dt.timedelta(minutes=RETRY_MINUTES))).rowcount
            if claimed != 1:
                continue  # another copy of the app has it
            deliver(row, timeout)
        except Exception as e:  # the email service is down, or refused it: try again in 5 minutes
            reason = safe_error(e)
            with eng.begin() as conn:
                conn.execute(db.outbox.update().where(db.outbox.c.id == row["id"]).values(
                    attempts=row["attempts"] + 1, last_error=reason,
                    send_after=now() + dt.timedelta(minutes=RETRY_MINUTES)))
            current_app.logger.warning("Email %s not sent (attempt %s): %s", row["id"], row["attempts"] + 1, reason)
            continue
        with eng.begin() as conn:
            conn.execute(db.outbox.delete().where(db.outbox.c.id == row["id"]))
        sent += 1
    with eng.connect() as conn:
        waiting = conn.execute(sa.select(sa.func.count()).select_from(db.outbox)).scalar()
    return sent, waiting


_senders_lock = threading.Lock()


def _start_sending(ids):
    """Send these queued emails on a background thread, and return the thread.

    The thread is kept in app.extensions["email_senders"] until it ends, so the
    tests can wait for it (tests/README.md).
    """
    app = current_app._get_current_object()
    senders = app.extensions["email_senders"]
    listed = threading.Event()

    def send():
        try:
            with app.app_context():
                try:
                    send_due_emails(ids)
                except Exception as e:
                    app.logger.warning("Couldn't send queued email: %s", safe_error(e))
        finally:
            listed.wait()  # only ever listed once started, and always removed
            with _senders_lock:
                senders.discard(worker)

    worker = threading.Thread(target=send, daemon=True)
    worker.start()
    with _senders_lock:
        senders.add(worker)
    listed.set()
    return worker


def send_now(*ids):
    """Send the email(s) this page just queued, waiting at most EMAIL_SEND_TIMEOUT
    seconds in all (Spec DD-6; R-15). The sending carries on in the background if
    the email service is slow; anything that fails stays queued for the 5-minute job.
    """
    ids = [i for i in ids if i is not None]
    if ids:
        _start_sending(ids).join(timeout=current_app.config["EMAIL_SEND_TIMEOUT"])


def send_in_background(*ids):
    """Send the email(s) without waiting at all: the sign-in and create-account
    pages answer straight away, so the time taken can't show whether an email
    has an account (Spec DD-10; round 2, R2-2, R2-3)."""
    ids = [i for i in ids if i is not None]
    if ids:
        _start_sending(ids)


def send_sign_in_link(conn, account):
    """Queue a sign-in link, unless this address has had 10 in the last 24 hours (Spec DD-9).
    Returns the queued email's id, or None when the limit is reached.

    The email is recorded first and counted after, with the account row locked, so two
    requests at the same moment can never both slip past the limit (R-6).
    """
    conn.execute(sa.select(db.accounts.c.id).where(db.accounts.c.id == account["id"]).with_for_update())
    if not _one_more_sign_in_email(conn, account["email_lookup"]):
        return None
    token = secrets.token_urlsafe(24)
    minutes = current_app.config["SIGN_IN_LINK_MINUTES"]
    expires = now() + dt.timedelta(minutes=minutes)
    conn.execute(db.sign_in_links.insert().values(
        token_hash=token_hash(token), account_id=account["id"], expires=expires))
    link = f"{current_app.config['BASE_URL'].rstrip('/')}/sign-in/{token}"
    return queue_email(conn, account["id"], w.sign_in_email(account["username"], minutes, link), expires=expires)


def _one_more_sign_in_email(conn, lookup):
    """Record one more sign-in email for this address, unless it has had 10 in the last
    24 hours (Spec DD-9). The caller holds a lock on the address first: its account row,
    or its account request row."""
    conn.execute(db.sign_in_emails.insert().values(email_lookup=lookup, sent=now()))
    in_last_day = conn.execute(sa.select(sa.func.count()).select_from(db.sign_in_emails).where(
        db.sign_in_emails.c.email_lookup == lookup,
        db.sign_in_emails.c.sent > now() - dt.timedelta(hours=24))).scalar()
    if in_last_day > SIGN_IN_EMAILS_PER_DAY:
        conn.execute(db.sign_in_emails.delete().where(
            db.sign_in_emails.c.email_lookup == lookup,
            db.sign_in_emails.c.id == sa.select(sa.func.max(db.sign_in_emails.c.id)).where(
                db.sign_in_emails.c.email_lookup == lookup).scalar_subquery()))
        return False
    return True


def request_account(conn, username, email_encrypted, lookup, block_key):
    """Save an account request and queue its sign-in link (Spec DD-13). The account is made
    only when "Sign in" is pressed. Earlier requests for the same email keep working until
    one of them is used (R2-17). Returns the queued email's id, or None when the daily limit
    is reached."""
    if conn.dialect.name == "postgresql":
        # No account row to lock yet: lock this email's lookup key instead, so two requests
        # at the same moment can't both slip past the limit (DD-9). SQLite already lets
        # only one change happen at a time.
        conn.execute(sa.text("SELECT pg_advisory_xact_lock(hashtext(:key))"), {"key": lookup})
    token = secrets.token_urlsafe(24)
    minutes = current_app.config["SIGN_IN_LINK_MINUTES"]
    expires = now() + dt.timedelta(minutes=minutes)
    if not _one_more_sign_in_email(conn, lookup):
        return None
    conn.execute(db.account_requests.insert().values(
        token_hash=token_hash(token), username=username, email_encrypted=email_encrypted,
        email_lookup=lookup, email_block_key=block_key, expires=expires))
    link = f"{current_app.config['BASE_URL'].rstrip('/')}/sign-in/{token}"
    return queue_email(conn, None, w.sign_in_email(username, minutes, link), expires=expires,
                       to_encrypted=email_encrypted)


def is_blocked(conn, account):
    return conn.execute(sa.select(db.block_list.c.id).where(
        db.block_list.c.email_block_key == account["email_block_key"])).first() is not None


def slot_with_task(conn, slot_id):
    return conn.execute(
        sa.select(db.slots, db.tasks.c.title, db.tasks.c.description, db.tasks.c.date)
        .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
        .where(db.slots.c.id == slot_id)
    ).mappings().first()


# ---------------------------------------------------------------------------
# S-1 Sign In and S-2 Create Account
# ---------------------------------------------------------------------------

@bp.route("/")
def home():
    return redirect(home_for(g.user) if g.user else url_for("main.sign_in"))


@bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("email", "")
        if looks_like_email(email):
            queued = None
            with engine().begin() as conn:
                account = conn.execute(db.accounts.select().where(
                    db.accounts.c.email_lookup == vault().lookup_key(email))).mappings().first()
                if account is not None:
                    queued = send_sign_in_link(conn, account)
            send_in_background(queued)
        # The same reply, straight away, whether or not the account exists, the limit is
        # reached, or the email service is down (Spec DD-3, DD-6, DD-9, DD-10; T-SEC-05,
        # T-SEC-07, T-SEC-10, T-EM-01)
        return render_template("sign_in.html", banner=("info", w.CHECK_EMAIL))
    return render_template("sign_in.html")


@bp.route("/sign-in/<token>", methods=["GET", "POST"])
def use_sign_in_link(token):
    if request.method == "GET":
        # Opening the link only shows the "Sign in" button: email systems that open
        # links to check them can't use it up (Spec DD-11; d05-01 UX-7; round 2, R2-4)
        with engine().connect() as conn:
            exists = conn.execute(sa.select(db.sign_in_links.c.token_hash).where(
                db.sign_in_links.c.token_hash == token_hash(token))).first() or conn.execute(
                sa.select(db.account_requests.c.token_hash).where(
                    db.account_requests.c.token_hash == token_hash(token))).first()
        if exists is None:
            return render_template("sign_in.html", banner=("error", w.LINK_INVALID)), 400
        return render_template("sign_in_finish.html", action=request.path)
    with engine().begin() as conn:
        link = conn.execute(db.sign_in_links.select().where(
            db.sign_in_links.c.token_hash == token_hash(token))).mappings().first()
        if link is None:
            return _finish_account_request(token)
        # Use the link up in a single step: only the request that removes it may sign in (Spec DD-7)
        used = conn.execute(db.sign_in_links.delete().where(
            db.sign_in_links.c.token_hash == link["token_hash"])).rowcount
        if used != 1:
            return render_template("sign_in.html", banner=("error", w.LINK_INVALID)), 400
        account = conn.execute(db.accounts.select().where(
            db.accounts.c.id == link["account_id"])).mappings().first()
        expired = link["expires"] < now()
        if expired:
            queued = send_sign_in_link(conn, account)
    if expired:
        send_now(queued)
        return render_template("sign_in.html", banner=("error", w.LINK_EXPIRED))
    session.clear()
    session.permanent = True
    session["account_id"] = account["id"]
    return redirect(home_for(account))


def _finish_account_request(token):
    """"Sign in" on a new account's link: make the account now (Spec DD-13; R2-14)."""
    try:
        with engine().begin() as conn:
            request_row = conn.execute(db.account_requests.select().where(
                db.account_requests.c.token_hash == token_hash(token))).mappings().first()
            if request_row is None:
                return render_template("sign_in.html", banner=("error", w.LINK_INVALID)), 400
            # Use the request up in a single step: only the request that removes it goes on (DD-7)
            used = conn.execute(db.account_requests.delete().where(
                db.account_requests.c.token_hash == request_row["token_hash"])).rowcount
            if used != 1:
                return render_template("sign_in.html", banner=("error", w.LINK_INVALID)), 400
            r = request_row
            if r["expires"] < now():
                queued = request_account(conn, r["username"], r["email_encrypted"], r["email_lookup"],
                                         r["email_block_key"])
                expired = True
            else:
                expired = False
                if conn.execute(sa.select(db.block_list.c.id).where(
                        db.block_list.c.email_block_key == r["email_block_key"])).first():
                    return render_template("create_account.html", form={}, error=w.COULDNT_CREATE,
                                           error_field=None), 403
                account = conn.execute(db.accounts.select().where(
                    db.accounts.c.email_lookup == r["email_lookup"])).mappings().first()
                if account is None:
                    if conn.execute(sa.select(db.accounts.c.id).where(
                            db.accounts.c.username_key == r["username"].lower())).first():
                        return render_template("create_account.html", form={}, error=w.USERNAME_TAKEN,
                                               error_field="username"), 409  # UC-2 4a
                    account_id = conn.execute(db.accounts.insert().values(
                        username=r["username"], username_key=r["username"].lower(), role="volunteer",
                        email_encrypted=r["email_encrypted"], email_lookup=r["email_lookup"],
                        email_block_key=r["email_block_key"], created=now())).inserted_primary_key[0]
                    account = {"id": account_id, "role": "volunteer"}
                # The account exists now: the email's other requests stop working (R2-17)
                conn.execute(db.account_requests.delete().where(
                    db.account_requests.c.email_lookup == r["email_lookup"]))
    except sa.exc.IntegrityError:  # the username was taken at the same moment (UC-2 4a)
        return render_template("create_account.html", form={}, error=w.USERNAME_TAKEN,
                               error_field="username"), 409
    if expired:
        send_now(queued)
        return render_template("sign_in.html", banner=("error", w.LINK_EXPIRED))
    session.clear()
    session.permanent = True
    session["account_id"] = account["id"]
    return redirect(home_for(account))


@bp.route("/sign-out")
def sign_out():
    session.clear()
    return redirect(url_for("main.sign_in"))


@bp.route("/create-account", methods=["GET", "POST"])
def create_account():
    if request.method == "GET":
        return render_template("create_account.html", form={})
    form = {"username": request.form.get("username", "").strip(), "email": request.form.get("email", "").strip()}

    def again(message, field):
        return render_template("create_account.html", form=form, error=message, error_field=field), 400

    if not USERNAME_RE.fullmatch(form["username"]):
        return again(w.USERNAME_RULES, "username")
    if not looks_like_email(form["email"]):
        return again(w.EMAIL_INVALID, "email")
    if request.form.get("privacy_accepted") is None:
        return again(w.TICK_PRIVACY, "privacy")
    v = vault()
    with engine().begin() as conn:
        if conn.execute(sa.select(db.accounts.c.id).where(
                db.accounts.c.username_key == form["username"].lower())).first():
            return again(w.USERNAME_TAKEN, "username")
        block_key = v.block_key(form["email"])
        lookup = v.lookup_key(form["email"])
        blocked = conn.execute(sa.select(db.block_list.c.id).where(
            db.block_list.c.email_block_key == block_key)).first()
        if blocked:
            return again(w.COULDNT_CREATE, None)  # never says why (UC-2 3b)
        owner = conn.execute(db.accounts.select().where(db.accounts.c.email_lookup == lookup)).mappings().first()
        if owner is not None:
            # The same reply as a new account; the owner gets a sign-in link instead,
            # so no one can find out who has an account (PRD v1.3, UC-2 3c; round 2, R2-2)
            queued = send_sign_in_link(conn, owner)
        else:
            # No account yet: only a request, made into an account at "Sign in", so no
            # number of tries can show who has an account (Spec DD-13; R2-14)
            queued = request_account(conn, form["username"], v.encrypt(form["email"]), lookup, block_key)
    # Straight away, and the same either way (Spec DD-10)
    send_in_background(queued)
    return render_template("sign_in.html", banner=("info", w.CHECK_EMAIL))


@bp.route("/pretend-inbox")
def pretend_inbox():
    """The local environment's pretend inbox, for building and the stakeholder demo only."""
    if current_app.config["EMAIL_SERVICE"] != "pretend" or current_app.config.get("TEST_INBOX") is not None:
        return page_not_found()
    mails = list(reversed(current_app.extensions["pretend_inbox"]))
    return render_template("pretend_inbox.html", mails=mails)


# ---------------------------------------------------------------------------
# S-3 Open Slots, S-4 Confirm, S-5 My Sign-Ups (volunteers)
# ---------------------------------------------------------------------------

def open_slots_page(banner=None, status=200):
    with engine().connect() as conn:
        rows = conn.execute(
            sa.select(db.slots, db.tasks.c.title, db.tasks.c.description, db.tasks.c.date)
            .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
            .where(db.slots.c.starts > now())
            .order_by(db.tasks.c.date, db.tasks.c.id, db.slots.c.starts)
        ).mappings().all()
    days = []
    for row in rows:
        if not days or days[-1]["date"] != row["date"]:
            days.append({"date": row["date"], "tasks": []})
        tasks = days[-1]["tasks"]
        if not tasks or tasks[-1]["id"] != row["task_id"]:
            tasks.append({"id": row["task_id"], "title": row["title"],
                          "description": row["description"], "slots": []})
        tasks[-1]["slots"].append(row)
    return render_template("open_slots.html", days=days, banner=banner), status


@bp.route("/slots")
@signed_in()
def open_slots():
    return open_slots_page(banner=_flashed())


@bp.route("/slots/<int:slot_id>/confirm")
@signed_in("volunteer")
def confirm_sign_up(slot_id):
    with engine().connect() as conn:
        slot = slot_with_task(conn, slot_id)
    if slot is None:
        return page_not_found()
    reminder_later = slot["date"] > now().date() + dt.timedelta(days=1)
    return render_template("confirm.html", slot=slot, note=w.confirm_note(g.user["username"], reminder_later))


@bp.route("/slots/<int:slot_id>/sign-up", methods=["POST"])
@signed_in("volunteer")
def sign_up(slot_id):
    with engine().connect() as conn:
        slot = slot_with_task(conn, slot_id)
        if slot is None:
            return page_not_found()
        if is_blocked(conn, g.user):
            return not_allowed()
        already = conn.execute(sa.select(db.signups.c.id).where(
            db.signups.c.slot_id == slot_id, db.signups.c.account_id == g.user["id"])).first()
    if already:
        return open_slots_page(banner=("error", w.ALREADY), status=409)
    if slot["starts"] <= now():
        return open_slots_page(banner=("error", w.SLOT_GONE), status=409)
    try:
        with engine().begin() as conn:
            # Take one place, only if one is left, in a single step (Spec DD-5)
            taken = conn.execute(
                db.slots.update()
                .where(db.slots.c.id == slot_id, db.slots.c.places_left > 0)
                .values(places_left=db.slots.c.places_left - 1)
            ).rowcount
            if taken != 1:
                raise _SlotFull()
            conn.execute(db.signups.insert().values(
                slot_id=slot_id, account_id=g.user["id"], signed_up=now(), reminder_sent=False))
            # A confirmation straight away, saved in the same step (PRD v1.2, UC-3)
            queued = queue_email(conn, g.user["id"], w.confirmation_email(
                g.user["username"], slot["title"], day_heading(slot["date"]),
                slot_time(slot["starts"], slot["ends"]), slot["description"]), expires=slot["starts"])
    except _SlotFull:
        return open_slots_page(banner=("error", w.JUST_TAKEN), status=409)
    except sa.exc.IntegrityError:  # a fast second tap on "Confirm"
        return open_slots_page(banner=("error", w.ALREADY), status=409)
    send_now(queued)
    flash(w.SIGNED_UP, "success")
    return redirect(url_for("main.my_sign_ups"))


class _SlotFull(Exception):
    pass


def _flashed():
    from flask import get_flashed_messages
    messages = get_flashed_messages(with_categories=True)
    return messages[-1] if messages else None


def my_sign_ups_page(banner=None, status=200):
    with engine().connect() as conn:
        rows = conn.execute(
            sa.select(db.signups.c.id.label("signup_id"), db.slots.c.starts, db.slots.c.ends,
                      db.tasks.c.title, db.tasks.c.date)
            .join(db.slots, db.slots.c.id == db.signups.c.slot_id)
            .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
            .where(db.signups.c.account_id == g.user["id"], db.slots.c.ends > now())
            .order_by(db.slots.c.starts)
        ).mappings().all()
    return render_template("my_sign_ups.html", rows=rows, banner=banner), status


@bp.route("/my-sign-ups")
@signed_in("volunteer")
def my_sign_ups():
    return my_sign_ups_page(banner=_flashed())


@bp.route("/sign-ups/<int:signup_id>/cancel", methods=["GET", "POST"])
@signed_in("volunteer")
def cancel_sign_up(signup_id):
    with engine().connect() as conn:
        row = conn.execute(
            sa.select(db.signups, db.slots.c.starts, db.slots.c.ends, db.tasks.c.title, db.tasks.c.date)
            .join(db.slots, db.slots.c.id == db.signups.c.slot_id)
            .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
            .where(db.signups.c.id == signup_id)
        ).mappings().first()
    if row is None or row["account_id"] != g.user["id"]:
        return not_allowed()  # only your own sign-ups (UC-4 AC2)
    if row["starts"] <= now():
        return my_sign_ups_page(banner=("error", w.STARTED), status=409)
    if request.method == "GET":
        return render_template("cancel_confirm.html", row=row)
    with engine().begin() as conn:
        gone = conn.execute(db.signups.delete().where(
            db.signups.c.id == signup_id, db.signups.c.account_id == g.user["id"])).rowcount
        if gone:
            conn.execute(db.slots.update().where(db.slots.c.id == row["slot_id"])
                         .values(places_left=db.slots.c.places_left + 1))
    flash(w.CANCELED, "success")
    return redirect(url_for("main.my_sign_ups"))


# ---------------------------------------------------------------------------
# S-6 My Tasks, S-7 Post a Task, S-8 Roster, S-9 Message (coordinators)
# ---------------------------------------------------------------------------

@bp.route("/my-tasks")
@signed_in("coordinator")
def my_tasks():
    with engine().connect() as conn:
        rows = conn.execute(
            sa.select(db.slots, db.tasks.c.title, db.tasks.c.date)
            .join(db.tasks, db.tasks.c.id == db.slots.c.task_id)
            .where(db.tasks.c.posted_by == g.user["id"], db.tasks.c.date >= now().date())
            .order_by(db.tasks.c.date, db.tasks.c.id, db.slots.c.starts)
        ).mappings().all()
    days = []
    for row in rows:
        if not days or days[-1]["date"] != row["date"]:
            days.append({"date": row["date"], "rows": []})
        days[-1]["rows"].append(row)
    return render_template("my_tasks.html", days=days, banner=_flashed())


def _read_task_form():
    form = {
        "title": request.form.get("title", ""),
        "description": one_line_break(request.form.get("description", "")),
        "date": request.form.get("date", ""),
    }
    starts = request.form.getlist("slot_start")
    ends = request.form.getlist("slot_end")
    places = request.form.getlist("places")
    count = max(len(starts), len(ends), len(places))
    every_row = []
    for i in range(count):
        every_row.append({
            "start": starts[i] if i < len(starts) else "",
            "end": ends[i] if i < len(ends) else "",
            "places": places[i] if i < len(places) else "",
        })
    form["every_row"] = every_row  # as typed, empty rows included, to show the form again
    form["rows"] = [row for row in every_row if any(v.strip() for v in row.values())]
    return form


def _check_task(form):
    """Returns (error, task values, slot values). Every rule from UC-1 and Spec Section 6."""
    title = form["title"].strip()
    if not title:
        return w.TITLE_MISSING, None, None
    if len(title) > 60:
        return w.TITLE_LONG, None, None
    description = form["description"].strip()
    if len(description) > 1000:
        return w.DESCRIPTION_LONG, None, None
    try:
        day = dt.date.fromisoformat(form["date"].strip())
    except ValueError:
        return w.DATE_INVALID, None, None
    if not form["rows"]:
        return w.NO_SLOTS, None, None
    if len(form["rows"]) > MAX_SLOTS:
        return w.TOO_MANY_SLOTS, None, None
    slot_values = []
    for row in form["rows"]:
        start_m, end_m = TIME_RE.fullmatch(row["start"].strip()), TIME_RE.fullmatch(row["end"].strip())
        if not start_m or not end_m:
            return w.TIME_INVALID, None, None
        starts = dt.datetime.combine(day, dt.time(int(start_m[1]), int(start_m[2])))
        ends = dt.datetime.combine(day, dt.time(int(end_m[1]), int(end_m[2])))
        if ends - starts != dt.timedelta(hours=1):
            return w.ONE_HOUR, None, None
        places = row["places"].strip()
        if not places.isascii() or not places.isdigit() or not 1 <= int(places) <= 20:
            return w.PLACES_RANGE, None, None
        slot_values.append({"starts": starts, "ends": ends, "places": int(places), "places_left": int(places)})
    return None, {"title": title, "description": description, "date": day}, slot_values


@bp.route("/tasks/new", methods=["GET", "POST"])
@signed_in("coordinator")
def post_task():
    if request.method == "GET":
        return render_template("post_task.html", form={"rows": []}, rows=FORM_ROWS, max_rows=MAX_SLOTS)
    form = _read_task_form()
    shown = max(FORM_ROWS, len(form["every_row"]))
    if request.form.get("add_slot"):
        # "Add another slot": show the form again with one more row, up to 10 (d05-01 v1.2, S-7)
        return render_template("post_task.html", form=dict(form, rows=form["every_row"]),
                               rows=min(MAX_SLOTS, shown + 1), max_rows=MAX_SLOTS)
    error, task, slot_values = _check_task(form)
    if error:
        return render_template("post_task.html", form=dict(form, rows=form["every_row"]),
                               rows=shown, max_rows=MAX_SLOTS, error=error), 400
    with engine().begin() as conn:
        task_id = conn.execute(db.tasks.insert().values(posted_by=g.user["id"], **task)).inserted_primary_key[0]
        conn.execute(db.slots.insert(), [dict(s, task_id=task_id) for s in slot_values])
    flash(w.TASK_POSTED, "success")
    return redirect(url_for("main.my_tasks"))


@bp.route("/slots/<int:slot_id>/roster")
@signed_in("coordinator")
def roster(slot_id):
    with engine().connect() as conn:
        slot = slot_with_task(conn, slot_id)
        if slot is None:
            return page_not_found()
        # Usernames only: no email is ever read here (Spec UC-5)
        names = conn.execute(
            sa.select(db.accounts.c.username)
            .join(db.signups, db.signups.c.account_id == db.accounts.c.id)
            .where(db.signups.c.slot_id == slot_id)
            .order_by(db.signups.c.signed_up, db.signups.c.id)
        ).scalars().all()
    return render_template("roster.html", slot=slot, names=names, banner=_flashed())


def back_to_roster():
    """Where Send and "Yes, block" return to: the roster they came from (d05-01 v1.2, Section 6)."""
    slot = request.values.get("slot", "")
    if slot.isascii() and slot.isdigit():
        with engine().connect() as conn:
            if conn.execute(sa.select(db.slots.c.id).where(db.slots.c.id == int(slot))).first():
                return url_for("main.roster", slot_id=int(slot))
    return url_for("main.my_tasks")


def volunteer_named(conn, username):
    return conn.execute(db.accounts.select().where(
        db.accounts.c.username_key == username.lower(), db.accounts.c.role == "volunteer")).mappings().first()


@bp.route("/volunteers/<username>/message", methods=["GET", "POST"])
@signed_in("coordinator")
def message_volunteer(username):
    with engine().connect() as conn:
        volunteer = volunteer_named(conn, username)
    if volunteer is None:
        return page_not_found()
    back = back_to_roster()
    slot = request.values.get("slot", "")
    if request.method == "GET":
        return render_template("message_volunteer.html", volunteer=volunteer, text="", back=back, slot=slot)
    text = one_line_break(request.form.get("message", ""))
    if len(text) > 500:
        return render_template("message_volunteer.html", volunteer=volunteer, text=text, back=back, slot=slot,
                               error=w.MESSAGE_LONG), 400
    if not text.strip():
        return render_template("message_volunteer.html", volunteer=volunteer, text=text, back=back, slot=slot,
                               error=w.MESSAGE_MISSING), 400
    with engine().begin() as conn:
        queued = queue_email(conn, volunteer["id"], w.message_email(volunteer["username"], g.user["username"], text),
                             expires=now() + dt.timedelta(days=MESSAGE_KEEP_DAYS))
    send_now(queued)
    flash(w.SENT, "success")
    return redirect(back)


@bp.route("/volunteers/<username>/block", methods=["GET", "POST"])
@signed_in("coordinator")
def block_volunteer(username):
    with engine().connect() as conn:
        volunteer = volunteer_named(conn, username)
    if volunteer is None:
        return page_not_found()
    back = back_to_roster()
    if request.method == "GET":
        return render_template("block_confirm.html", volunteer=volunteer, back=back,
                               slot=request.values.get("slot", ""))
    with engine().begin() as conn:
        exists = conn.execute(sa.select(db.block_list.c.id).where(
            db.block_list.c.email_block_key == volunteer["email_block_key"])).first()
        if not exists:
            conn.execute(db.block_list.insert().values(
                email_block_key=volunteer["email_block_key"], username=volunteer["username"],
                blocked_by=g.user["username"], blocked_on=now().date()))
        # Cancel their upcoming sign-ups and give the places back, in the same step;
        # with no sign-up, no reminder is sent (PRD v1.3, UC-7; round 2, R2-9)
        upcoming = conn.execute(
            sa.select(db.signups.c.id, db.signups.c.slot_id)
            .join(db.slots, db.slots.c.id == db.signups.c.slot_id)
            .where(db.signups.c.account_id == volunteer["id"], db.slots.c.starts > now())
        ).all()
        for signup in upcoming:
            gone = conn.execute(db.signups.delete().where(db.signups.c.id == signup.id)).rowcount
            if gone:
                conn.execute(db.slots.update().where(db.slots.c.id == signup.slot_id)
                             .values(places_left=db.slots.c.places_left + 1))
    flash(w.BLOCKED, "success")
    return redirect(back)


# ---------------------------------------------------------------------------
# S-10 Blocked Volunteers (System Administrator)
# ---------------------------------------------------------------------------

def blocked_page(banner=None):
    with engine().connect() as conn:
        rows = conn.execute(db.block_list.select().order_by(db.block_list.c.blocked_on.desc(),
                                                            db.block_list.c.id.desc())).mappings().all()
    return render_template("blocked.html", rows=rows, banner=banner)


@bp.route("/blocked")
@signed_in("admin")
def blocked_volunteers():
    return blocked_page()


@bp.route("/blocked/<username>/undo", methods=["POST"])
@signed_in("admin")
def undo_block(username):
    with engine().begin() as conn:
        conn.execute(db.block_list.delete().where(db.block_list.c.username == username))
    return blocked_page(banner=("success", w.UNBLOCKED))


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------

@bp.app_errorhandler(404)
def _404(_e):
    return page_not_found()


@bp.app_errorhandler(405)
def _405(_e):
    return render_template("message.html", title=w.TITLE_NOT_ALLOWED, banner=("error", w.NOT_ALLOWED)), 405


@bp.app_errorhandler(400)
def _400(_e):
    return render_template("message.html", title=w.TITLE_TRY_AGAIN, banner=("error", w.BAD_REQUEST)), 400


@bp.app_errorhandler(500)
def _500(_e):
    return render_template("message.html", title=w.TITLE_SORRY, banner=("error", w.SERVER_ERROR)), 500
