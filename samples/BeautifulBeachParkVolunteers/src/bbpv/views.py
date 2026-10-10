"""The screens S-1 to S-10 and the requests behind them (Spec Section 7).

Every request checks who is asking (Spec Section 11.1). No page is ever
given an email address: they are decrypted only in send_email().
"""

import datetime as dt
import functools
import re
import secrets

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


def vault():
    return current_app.extensions["vault"]


def now():
    return current_app.config["CLOCK"]()


def clock_time(t):
    """9:00, 1:00 (12-hour clock, as in the mockups)."""
    return f"{t.hour % 12 or 12}:{t.minute:02d}"


def slot_time(starts, ends):
    return f"{clock_time(starts)} – {clock_time(ends)}"


def hours_label(starts, ends):
    """'9 to 10': used in accessible button names (d05-01 Section 10)."""
    return f"{starts.hour % 12 or 12} to {ends.hour % 12 or 12}"


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
    if left <= 0:
        return "Full"
    return "1 place left" if left == 1 else f"{left} places left"


def not_allowed():
    return render_template("message.html", title="Not allowed", banner=("error", w.NOT_ALLOWED)), 403


def page_not_found():
    return render_template("message.html", title="Not found",
                           banner=("error", "We couldn't find that page.")), 404


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


def send_email(conn, account_id, subject, text):
    """The only place an email address is decrypted, and only to send to it."""
    row = conn.execute(sa.select(db.accounts.c.email_encrypted).where(db.accounts.c.id == account_id)).first()
    if row is not None:
        mail.send(vault().decrypt(row.email_encrypted), subject, text)


def send_sign_in_link(conn, account):
    token = secrets.token_urlsafe(24)
    minutes = current_app.config["SIGN_IN_LINK_MINUTES"]
    conn.execute(db.sign_in_links.delete().where(db.sign_in_links.c.expires < now()))
    conn.execute(db.sign_in_links.insert().values(
        token_hash=token_hash(token), account_id=account["id"], expires=now() + dt.timedelta(minutes=minutes)))
    link = f"{current_app.config['BASE_URL'].rstrip('/')}/sign-in/{token}"
    send_email(conn, account["id"], "Your BeautifulBeachPark sign-in link", (
        f"Hello {account['username']},\n\n"
        f"Use this link to sign in to BeautifulBeachPark Volunteers. It works for {minutes} minutes:\n\n"
        f"{link}\n\n"
        "If you didn't ask for it, you can ignore this email.\n"
    ))


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
            with engine().begin() as conn:
                account = conn.execute(db.accounts.select().where(
                    db.accounts.c.email_lookup == vault().lookup_key(email))).mappings().first()
                if account is not None:
                    send_sign_in_link(conn, account)
        # The same reply whether or not the account exists (Spec DD-3, T-SEC-05)
        return render_template("sign_in.html", banner=("info", w.CHECK_EMAIL))
    return render_template("sign_in.html")


@bp.route("/sign-in/<token>")
def use_sign_in_link(token):
    with engine().begin() as conn:
        link = conn.execute(db.sign_in_links.select().where(
            db.sign_in_links.c.token_hash == token_hash(token))).mappings().first()
        if link is None:
            return render_template("sign_in.html", banner=("error", w.LINK_INVALID)), 400
        conn.execute(db.sign_in_links.delete().where(db.sign_in_links.c.token_hash == link["token_hash"]))
        account = conn.execute(db.accounts.select().where(
            db.accounts.c.id == link["account_id"])).mappings().first()
        if link["expires"] < now():
            send_sign_in_link(conn, account)
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
        in_use = conn.execute(sa.select(db.accounts.c.id).where(db.accounts.c.email_lookup == lookup)).first()
        if blocked or in_use:
            return again(w.COULDNT_CREATE, None)  # never says why (UC-2 3b)
        account_id = conn.execute(db.accounts.insert().values(
            username=form["username"], username_key=form["username"].lower(), role="volunteer",
            email_encrypted=v.encrypt(form["email"]), email_lookup=lookup, email_block_key=block_key,
            created=now())).inserted_primary_key[0]
        send_sign_in_link(conn, {"id": account_id, "username": form["username"]})
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
    return render_template("confirm.html", slot=slot)


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
    except _SlotFull:
        return open_slots_page(banner=("error", w.JUST_TAKEN), status=409)
    except sa.exc.IntegrityError:  # a fast second tap on "Confirm"
        return open_slots_page(banner=("error", w.ALREADY), status=409)
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
        "description": request.form.get("description", ""),
        "date": request.form.get("date", ""),
    }
    starts = request.form.getlist("slot_start")
    ends = request.form.getlist("slot_end")
    places = request.form.getlist("places")
    count = max(len(starts), len(ends), len(places))
    rows = []
    for i in range(count):
        row = {
            "start": starts[i] if i < len(starts) else "",
            "end": ends[i] if i < len(ends) else "",
            "places": places[i] if i < len(places) else "",
        }
        if any(v.strip() for v in row.values()):
            rows.append(row)
    form["rows"] = rows
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
        return render_template("post_task.html", form={"rows": []}, rows=FORM_ROWS)
    form = _read_task_form()
    error, task, slot_values = _check_task(form)
    if error:
        return render_template("post_task.html", form=form, rows=max(FORM_ROWS, len(form["rows"])),
                               error=error), 400
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
    return render_template("roster.html", slot=slot, names=names)


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
    if request.method == "GET":
        return render_template("message_volunteer.html", volunteer=volunteer, text="")
    text = request.form.get("message", "")
    if len(text) > 500:
        return render_template("message_volunteer.html", volunteer=volunteer, text=text,
                               error=w.MESSAGE_LONG), 400
    if not text.strip():
        return render_template("message_volunteer.html", volunteer=volunteer, text=text,
                               error=w.MESSAGE_MISSING), 400
    with engine().connect() as conn:
        send_email(conn, volunteer["id"], "A message from a BeautifulBeachPark coordinator", (
            f"Hello {volunteer['username']},\n\n"
            f"{g.user['username']}, a BeautifulBeachPark coordinator, sent you this message:\n\n"
            f"{text}\n\n"
            "Please don't reply to this email; replies aren't read. "
            "To reach the coordinators, contact the park office.\n"
        ))
    return render_template("message_volunteer.html", volunteer=volunteer, text="", banner=("success", w.SENT))


@bp.route("/volunteers/<username>/block", methods=["GET", "POST"])
@signed_in("coordinator")
def block_volunteer(username):
    with engine().connect() as conn:
        volunteer = volunteer_named(conn, username)
    if volunteer is None:
        return page_not_found()
    if request.method == "GET":
        return render_template("block_confirm.html", volunteer=volunteer)
    with engine().begin() as conn:
        exists = conn.execute(sa.select(db.block_list.c.id).where(
            db.block_list.c.email_block_key == volunteer["email_block_key"])).first()
        if not exists:
            conn.execute(db.block_list.insert().values(
                email_block_key=volunteer["email_block_key"], username=volunteer["username"],
                blocked_by=g.user["username"], blocked_on=now().date()))
    return render_template("message.html", title=f"Blocked {volunteer['username']}",
                           banner=("success", w.BLOCKED), back=url_for("main.my_tasks"), back_text="Back to my tasks")


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
    return render_template("message.html", title="Not allowed", banner=("error", w.NOT_ALLOWED)), 405


@bp.app_errorhandler(400)
def _400(_e):
    return render_template("message.html", title="Please try again",
                           banner=("error", "Something was wrong with that request. Please go back and try again.")), 400


@bp.app_errorhandler(500)
def _500(_e):
    return render_template("message.html", title="Sorry",
                           banner=("error", "Something went wrong on our side. Please try again in a few minutes.")), 500
