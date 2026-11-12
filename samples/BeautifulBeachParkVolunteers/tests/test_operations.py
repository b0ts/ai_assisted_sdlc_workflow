"""Email queue, clean-up, park time, and wording (Test Plan Section 9, v1.2).

Added after the round 1 code review (d08-04-code-review-codex.md).
"""

import datetime as dt

import pytest

from conftest import (
    MSG, NOON, TASK, TODAY, TOMORROW, make_app, mails_to, new_client, run_command, sign_in_link, text,
    use_link,
)


def test_t_em_01_sign_in_email_waits_while_the_email_service_is_down(app, inbox, clock):
    """EF · Spec 7, 14, DD-6; round 1, R-2"""
    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    client = new_client(app)

    inbox.down = True
    known = client.post("/sign-in", data={"email": "test_vol_01@example.test"}, follow_redirects=True)
    unknown = client.post("/sign-in", data={"email": "nobody@example.test"}, follow_redirects=True)
    assert known.status_code == unknown.status_code == 200
    assert text(known) == text(unknown), "the replies differ while the email service is down"
    assert MSG["check_email"] in text(known)
    assert not mails_to(inbox, "test_vol_01@example.test")

    inbox.down = False
    clock.advance(minutes=5)
    run_command(app, "send-emails")
    sent = mails_to(inbox, "test_vol_01@example.test")
    assert len(sent) == 1, "the sign-in email wasn't sent once the service was back"
    resp = use_link(client, sign_in_link(sent[0]))
    assert resp.status_code in (302, 303), "the late sign-in link didn't work"

    run_command(app, "send-emails")
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 1, "the email was sent twice"


def test_t_em_02_reminders_survive_an_outage_without_duplicates(app, inbox, clock, beach_task, people):
    """EF · Spec 14, DD-6; UC-3 AC6; round 1, R-2"""
    vols = [people(f"test_vol_0{i}") for i in (1, 2, 3)]
    for vol, start, end in zip(vols, ("09:00", "09:00", "10:00"), ("10:00", "10:00", "11:00")):
        vol.sign_up(TASK, start, end)

    clock.advance(hours=6)  # 6 p.m.
    since = len(inbox)
    inbox.down = True
    run_command(app, "send-reminders")
    inbox.down = False
    assert not inbox[since:]

    run_command(app, "send-reminders")  # a rerun must not queue them again
    clock.advance(minutes=10)
    run_command(app, "send-emails")
    for vol in vols:
        reminders = [m for m in mails_to(inbox, vol.email, since) if m["subject"].startswith("Reminder")]
        assert len(reminders) == 1, f"{vol.username} got {len(reminders)} reminders"


def test_t_em_03_expired_sign_in_email_is_never_sent_late(app, inbox, clock):
    """BC · Spec 11.1 (links work for 15 minutes), DD-6; round 1, R-2"""
    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    inbox.down = True
    new_client(app).post("/sign-in", data={"email": "test_vol_01@example.test"})
    inbox.down = False

    clock.advance(minutes=20)
    run_command(app, "send-emails")
    assert not mails_to(inbox, "test_vol_01@example.test"), "an expired sign-in link was emailed"


def test_t_data_01_clean_up_removes_tasks_after_twelve_months(app, inbox, clock, coord, people, admin):
    """HP · Spec 6 (kept 12 months after its date); round 1, R-3"""
    vol = people("test_vol_01")
    old_day = TODAY.replace(year=TODAY.year - 1) - dt.timedelta(days=1)
    recent_day = TODAY.replace(year=TODAY.year - 1) + dt.timedelta(days=1)
    for title, day in (("Test Old Task", old_day), ("Test Recent Task", recent_day)):
        clock.set(dt.datetime.combine(day - dt.timedelta(days=1), dt.time(12)))
        coord.post_task(title=title, day=day)
        vol.sign_up(title)
    clock.set(NOON)
    coord.post_task()  # tomorrow's task stays
    coord.block("test_vol_01")

    run_command(app, "clean-up")

    engine = app.extensions["engine"]
    import sqlalchemy as sa
    with engine.connect() as conn:
        titles = set(conn.execute(sa.text("SELECT title FROM tasks")).scalars())
        orphans = conn.execute(sa.text(
            "SELECT COUNT(*) FROM slots WHERE task_id NOT IN (SELECT id FROM tasks)")).scalar()
        signups = conn.execute(sa.text("SELECT COUNT(*) FROM signups")).scalar()
    assert titles == {"Test Recent Task", TASK}
    assert orphans == 0, "slots of a removed task were left behind"
    assert signups == 1, "sign-ups of the removed task were left behind"
    assert "test_vol_01" in text(admin.get("/blocked")), "the clean-up removed a block"


def test_t_qr_03_park_time_zone_setting(tmp_path, inbox):
    """BC · Spec DD-8; d06-01 v1.4; round 1, R-10"""
    from zoneinfo import ZoneInfo

    for zone in ("America/Los_Angeles", "Pacific/Auckland"):
        app = make_app(None, inbox, f"sqlite:///{tmp_path / (zone.replace('/', '_') + '.db')}", PARK_TIMEZONE=zone)
        app_now = app.config["CLOCK"]()
        park_now = dt.datetime.now(ZoneInfo(zone)).replace(tzinfo=None)
        assert app_now.tzinfo is None
        assert abs(app_now - park_now) < dt.timedelta(minutes=1), f"'now' isn't {zone} time"


def test_t_wd_01_empty_screens_use_the_approved_wording(app, coord, people):
    """EF · Spec 10; d05-01 v1.2 Sections 8 and 9; round 1, R-5"""
    vol = people("test_vol_01")
    assert MSG["no_open_slots"] in text(vol.open_slots())
    assert MSG["no_sign_ups"] in text(vol.get("/my-sign-ups"))
    assert MSG["no_tasks"] in text(coord.get("/my-tasks"))
    resp = new_client(app).get("/sign-in/not-a-real-link")
    assert MSG["link_invalid"] in text(resp)


def test_t_em_04_a_failed_email_never_stores_the_address(app, inbox, db_url, caplog):
    """EF · Spec 11.1 (emails stored encrypted), DD-6; round 1 re-review, R-14"""
    import logging

    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    inbox.reject = True
    with caplog.at_level(logging.DEBUG):
        new_client(app).post("/sign-in", data={"email": "test_vol_01@example.test"})
        run_command(app, "send-emails")
    inbox.reject = False

    from conftest import dump_database
    stored = [v for v in dump_database(db_url) if "@example.test" in v.lower()]
    assert not stored, f"a failed email left an address in the database: {stored[:2]}"
    assert "@example.test" not in caplog.text, "a failed email wrote an address to the log"


def test_t_em_05_a_page_sends_only_its_own_email(app, inbox, clock, people):
    """EF · Spec DD-6, Spec 10 (reliability); round 1 re-review, R-15"""
    for i in (1, 2, 3):
        run_command(app, "create-account", f"test_vol_0{i}", f"test_vol_0{i}@example.test", "--role", "volunteer")
    client = new_client(app)
    inbox.down = True
    for i in (1, 2):
        client.post("/sign-in", data={"email": f"test_vol_0{i}@example.test"})
    inbox.down = False
    clock.advance(minutes=6)  # the two waiting emails are due again

    client.post("/sign-in", data={"email": "test_vol_03@example.test"})
    assert len(mails_to(inbox, "test_vol_03@example.test")) == 1
    assert not mails_to(inbox, "test_vol_01@example.test"), "a page sent someone else's queued email"
    assert not mails_to(inbox, "test_vol_02@example.test"), "a page sent someone else's queued email"

    run_command(app, "send-emails")  # the 5-minute job sends the rest
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 1
    assert len(mails_to(inbox, "test_vol_02@example.test")) == 1


def test_t_em_06_two_reminder_runs_at_once_send_one_reminder(app, inbox, clock, beach_task, people):
    """EF · Spec DD-6; UC-3 AC6; round 1 re-review, R-2

    The second run starts at the worst moment: after the first has found who
    needs a reminder, just before it marks the first one sent.
    """
    import sqlalchemy as sa

    vols = [people(f"test_vol_0{i}") for i in (1, 2)]
    for vol in vols:
        vol.sign_up(TASK)
    clock.advance(hours=6)  # 6 p.m.
    since = len(inbox)

    engine = app.extensions["engine"]
    armed = [True]

    def second_run_now(conn, cursor, statement, params, context, executemany):
        if armed[0] and statement.lstrip().upper().startswith("UPDATE SIGNUPS"):
            armed[0] = False
            run_command(app, "send-reminders")

    sa.event.listen(engine, "before_cursor_execute", second_run_now)
    try:
        run_command(app, "send-reminders")
    finally:
        sa.event.remove(engine, "before_cursor_execute", second_run_now)
    run_command(app, "send-emails")

    assert not armed[0], "the test couldn't reach the moment it checks"
    for vol in vols:
        reminders = [m for m in mails_to(inbox, vol.email, since) if m["subject"].startswith("Reminder")]
        assert len(reminders) == 1, f"{vol.username} got {len(reminders)} reminders"


def test_t_wd_02_no_wording_written_in_the_pages(app):
    """EF · Spec 10 (all wording in one place); round 1 re-review, R-5

    Every word a person sees or hears on a page comes from src/bbpv/wording.py:
    the page templates hold no words of their own, in text or in labels.
    """
    import pathlib
    import re as _re

    folder = pathlib.Path(app.root_path) / "templates"
    found = {}
    for page in sorted(folder.glob("*.html")):
        source = page.read_text()
        source = _re.sub(r"(?s)\{#.*?#\}|\{%.*?%\}|\{\{.*?\}\}", " ", source)
        source = _re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", source)
        source = _re.sub(r"(?is)<title>.*?</title>", lambda m: m.group(0), source)
        words = []
        for attr in ("aria-label", "placeholder", "alt", "title"):
            words += _re.findall(rf'{attr}="([^"]*)"', source)
        words += _re.sub(r"<[^>]+>", "\n", source).split("\n")
        words = [w.strip() for w in words if _re.search(r"[A-Za-z]", w)]
        if words:
            found[page.name] = words[:5]
    assert not found, f"words written in page templates instead of wording.py: {found}"


def test_t_em_07_a_page_never_waits_long_for_a_slow_email_service(app, inbox, beach_task, people):
    """BC · Spec DD-6 (a page waits at most EMAIL_SEND_TIMEOUT); round 1 re-review 2, R-15

    v1.5 (round 2): uses S-9, because the sign-in page no longer waits at all (DD-10).
    """
    import time

    from conftest import target_of

    vol = people("test_vol_01")
    vol.sign_up()
    path = target_of(beach_task.roster(), "Message test_vol_01")
    app.config["EMAIL_SEND_TIMEOUT"] = 0.5
    inbox.slow = 3
    beach_task.client.wait_for_emails = False
    since = len(inbox)
    started = time.monotonic()
    resp = beach_task.post(path, data={"message": "See you tomorrow."})
    waited = time.monotonic() - started
    assert MSG["sent"] in text(resp)
    assert waited < 2, f"the page waited {waited:.1f} seconds for the email service"

    for _ in range(100):  # the email still goes out once the service answers
        if mails_to(inbox, vol.email, since):
            break
        time.sleep(0.1)
    assert len(mails_to(inbox, vol.email, since)) == 1


def test_t_wd_03_times_take_their_words_from_the_wording_file(app, coord, people, monkeypatch):
    """EF · Spec 10 (all wording in one place); round 1 re-review 2, R-5"""
    from bbpv import wording

    monkeypatch.setattr(wording, "MORNING", "AM")
    monkeypatch.setattr(wording, "EVENING", "PM")
    monkeypatch.setattr(wording, "RANGE_DASH", " to ")
    monkeypatch.setattr(wording, "RANGE_TO", " until ")
    coord.post_task(slots=(("11:00", "12:00", 2),))
    page = people("test_vol_01").open_slots()
    assert "11:00 AM to 12:00 PM" in text(page)
    from conftest import target_of
    assert target_of(page, f"Sign up for {TASK}, 11:00 AM until 12:00 PM")


def test_t_em_08_no_database_connection_is_held_while_sending(app, inbox, beach_task, people):
    """EF · Spec DD-12; round 1, R-18; round 2, R2-5

    While the email service is working on an email, the app holds no database
    connection, so a slow service can't use them all up.
    """
    engine = app.extensions["engine"]
    held = []
    plain_append = inbox.append

    def append(mail):
        held.append(engine.pool.checkedout())
        plain_append(mail)

    inbox.append = append
    vol = people("test_vol_01")           # a sign-in email (sent in the background)
    vol.sign_up()                         # a confirmation (sent by the page)
    inbox.down = True
    from conftest import target_of
    path = target_of(beach_task.roster(), "Message test_vol_01")
    beach_task.post(path, data={"message": "Bring a hat."})
    inbox.down = False
    run_command(app, "send-emails")       # the 5-minute job
    assert len(held) >= 3, "the test didn't see every way an email is sent"
    assert held == [0] * len(held), f"database connections held while sending: {held}"


def test_t_qr_04_the_production_web_server_runs_the_app(clock, inbox, db_url):
    """HP · d06-01 v1.5, 5.1; d08-02 Section 5.1; round 2, R2-7"""
    import threading
    import urllib.request

    waitress = pytest.importorskip("waitress", reason="Waitress isn't installed: pip install -r src/requirements.txt")
    app = make_app(clock, inbox, db_url, FORCE_HTTPS=False)
    server = waitress.create_server(app, host="127.0.0.1", port=0, threads=4)
    worker = threading.Thread(target=server.run, daemon=True)
    worker.start()
    try:
        port = server.effective_port
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/sign-in", timeout=10) as resp:
            assert resp.status == 200
            assert "Send me a sign-in link" in resp.read().decode()
    finally:
        server.close()
