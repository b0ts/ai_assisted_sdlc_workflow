"""Security and privacy tests (Test Plan Section 8)."""

import re
from collections import deque

from conftest import (
    MSG, TASK, TEST_EMAIL_RE, body, dump_database, elements, form_fields, mails_to, new_client,
    run_command, sign_in_link, target_of, text,
)

SKIP_WHILE_CRAWLING = ("/sign-out", "/static/")


def crawl(person, start_pages, limit=200):
    """Opens every page reachable by links from the start pages. Returns {path: response}."""
    seen, queue = {}, deque(start_pages)
    while queue and len(seen) < limit:
        path = queue.popleft()
        if path in seen or any(path.startswith(s) for s in SKIP_WHILE_CRAWLING):
            continue
        resp = person.client.get(path)
        seen[path] = resp
        if resp.status_code in (301, 302, 303, 307, 308):
            location = resp.headers.get("Location", "")
            queue.append(re.sub(r"^https?://[^/]+", "", location))
            continue
        for el in elements(resp).elements:
            href = el["attrs"].get("href", "") if el["tag"] == "a" else ""
            if href.startswith("/") and not href.startswith("//"):
                queue.append(href.split("#")[0])
    return seen


def assert_no_emails(replies, who):
    for path, resp in replies.items():
        found = TEST_EMAIL_RE.findall(body(resp))
        headers = " ".join(f"{k}: {v}" for k, v in resp.headers.items())
        found += TEST_EMAIL_RE.findall(headers)
        assert not found, f"{who} was sent {found} on {path}"


def test_t_sec_01_emails_never_sent_to_the_browser(beach_task, people):
    """EF · Spec 11.1; PRD 2, 6; d05-01 Section 11"""
    vol1, vol2 = people("test_vol_01"), people("test_vol_02")
    vol1.sign_up()
    vol2.sign_up(TASK, "10:00", "11:00")

    vol_pages = crawl(vol1, ["/slots", "/my-sign-ups"])
    assert len(vol_pages) >= 3, "the volunteer crawl reached too few screens"
    assert_no_emails(vol_pages, "test_vol_01")

    coord_pages = crawl(beach_task, ["/my-tasks", "/tasks/new"])
    assert len(coord_pages) >= 4, "the coordinator crawl reached too few screens"
    assert_no_emails(coord_pages, "test_coord_01")

    # Replies to actions, not just pages
    message_path = target_of(beach_task.roster(), "Message test_vol_01")
    actions = {
        "message sent": beach_task.post(message_path, data={"message": "Test message"}),
        "blocked": beach_task.block("test_vol_02"),
        "signed up": vol1.sign_up(TASK, "10:00", "11:00"),
    }
    assert_no_emails(actions, "a volunteer or coordinator")


def test_t_sec_02_https_only(app):
    """EF · Spec 11.1"""
    plain = new_client(app, scheme="http")
    resp = plain.get("/slots")
    assert resp.status_code in (301, 302, 307, 308), "S-3 was served over plain HTTP"
    assert resp.headers["Location"].startswith("https://")

    secure = new_client(app)
    assert secure.get("/slots", follow_redirects=True).status_code == 200


def test_t_sec_03_block_list_holds_scrambled_copy_only(app, inbox, db_url, beach_task, admin, people):
    """EF · Spec 11.1, DD-4; UC-7 AC2"""
    vol5 = people("test_vol_05")
    beach_task.block("test_vol_05")
    run_command(app, "delete-account", "test_vol_05")

    stored = [v for v in dump_database(db_url) if "@example.test" in v.lower()]
    assert not stored, f"email addresses are stored unscrambled: {stored[:3]}"

    assert "(account deleted)" in text(admin.get("/blocked"))

    client = new_client(app)
    resp = client.post(
        "/create-account",
        data={"username": "test_vol_05b", "email": vol5.email, "privacy_accepted": "yes"},
        follow_redirects=True,
    )
    assert MSG["couldnt_create"] in text(resp)


NAME_FIELD = re.compile(r"(first|last|full|real|given|family|sur)[\s_\-]*name|^name$", re.IGNORECASE)


def test_t_sec_04_no_real_names_asked(app, beach_task, people):
    """EF · PRD 6, Privacy; UC-2 AC1"""
    vol = people("test_vol_01")
    vol.sign_up()
    anon = new_client(app)
    message_path = target_of(beach_task.roster(), "Message test_vol_01")
    pages = {
        "S-1": anon.get("/sign-in"),
        "S-2": anon.get("/create-account"),
        "S-3": vol.open_slots(),
        "S-4": vol.get(vol.signup_path(TASK, "10:00", "11:00").replace("/sign-up", "/confirm")),
        "S-5": vol.get("/my-sign-ups"),
        "S-6": beach_task.get("/my-tasks"),
        "S-7": beach_task.get("/tasks/new"),
        "S-8": beach_task.roster(),
        "S-9": beach_task.get(message_path),
        "S-10": people("test_admin_01", role="admin").get("/blocked"),
    }
    for screen, resp in pages.items():
        assert resp.status_code == 200, f"{screen} didn't open"
        labels = elements(resp).labels.values()
        for name in form_fields(resp):
            assert not NAME_FIELD.search(name), f"{screen} has a field named {name!r}"
        for label in labels:
            assert not NAME_FIELD.search(label) and label.strip().lower() != "name", (
                f"{screen} has a field labeled {label!r}"
            )


def test_t_sec_05_sign_in_reply_never_reveals_who_has_an_account(app, inbox, clock):
    """EF · Spec 7, DD-3; d05-01 Section 9"""
    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    client = new_client(app)

    known = client.post("/sign-in", data={"email": "test_vol_01@example.test"}, follow_redirects=True)
    unknown = client.post("/sign-in", data={"email": "nobody@example.test"}, follow_redirects=True)
    assert MSG["check_email"] in text(known)
    assert known.status_code == unknown.status_code
    assert text(known) == text(unknown), "the two replies are different"
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 1
    assert not mails_to(inbox, "nobody@example.test")

    link = sign_in_link(mails_to(inbox, "test_vol_01@example.test")[0])
    clock.advance(days=1)
    since = len(inbox)
    resp = new_client(app).get(link, follow_redirects=True)
    assert MSG["link_expired"] in text(resp)
    assert len(mails_to(inbox, "test_vol_01@example.test", since)) == 1, "no new link was sent"


def test_t_sec_06_a_sign_in_link_never_works_twice_at_once(app, inbox):
    """EF · Spec 11.1, DD-3, DD-7; round 1, R-1

    The second use of the link is made at the worst moment: after the first
    request has read the link, just before it removes it.
    """
    import sqlalchemy as sa

    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    first, second = new_client(app), new_client(app)
    first.post("/sign-in", data={"email": "test_vol_01@example.test"})
    link = sign_in_link(mails_to(inbox, "test_vol_01@example.test")[-1])

    engine = app.extensions["engine"]
    replies, armed = {}, [True]

    def just_before_delete(conn, cursor, statement, params, context, executemany):
        if armed[0] and statement.lstrip().upper().startswith("DELETE FROM SIGN_IN_LINKS"):
            armed[0] = False
            replies["second"] = second.get(link)

    sa.event.listen(engine, "before_cursor_execute", just_before_delete)
    try:
        replies["first"] = first.get(link)
    finally:
        sa.event.remove(engine, "before_cursor_execute", just_before_delete)

    assert "second" in replies, "the test couldn't reach the moment it checks"
    signed_in = [name for name, resp in replies.items() if resp.status_code in (302, 303)]
    assert len(signed_in) == 1, f"the same link signed in {len(signed_in)} times"


def test_t_sec_07_at_most_ten_sign_in_emails_a_day(app, inbox, clock):
    """BC · PRD 6, Email limits (v1.2); Spec DD-9; round 1, R-6"""
    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    client = new_client(app)
    replies = []
    for _ in range(12):
        resp = client.post("/sign-in", data={"email": "test_vol_01@example.test"}, follow_redirects=True)
        replies.append(text(resp))
        clock.advance(minutes=5)
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 10
    assert all(r == replies[0] for r in replies), "the reply changed once the limit was reached"
    assert MSG["check_email"] in replies[-1]

    clock.advance(hours=24)
    client.post("/sign-in", data={"email": "test_vol_01@example.test"})
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 11, "the limit didn't reset after 24 hours"


def test_t_sec_08_the_limit_holds_for_requests_at_the_same_moment(app, inbox, clock):
    """BC · PRD 6, Email limits; Spec DD-9; round 1 re-review, R-6 and R-17

    With 9 emails sent, two requests arrive at once: the second starts at the
    worst moment, after the first has begun, just before it records its email.
    The two run side by side, each with a bounded wait, so the test can never
    hang, even on PostgreSQL, where the second waits for the first's lock.
    """
    import threading

    import sqlalchemy as sa

    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    first, second = new_client(app), new_client(app)
    for _ in range(9):
        first.post("/sign-in", data={"email": "test_vol_01@example.test"})
        clock.advance(minutes=1)
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 9

    engine = app.extensions["engine"]
    armed, errors, started = [True], [], []

    def second_request():
        try:
            second.post("/sign-in", data={"email": "test_vol_01@example.test"})
        except Exception as e:  # reported below, never left hanging
            errors.append(e)

    def second_request_now(conn, cursor, statement, params, context, executemany):
        if armed[0] and statement.lstrip().upper().startswith("INSERT INTO SIGN_IN_EMAILS"):
            armed[0] = False
            t = threading.Thread(target=second_request, daemon=True)
            started.append(t)
            t.start()
            t.join(timeout=1)  # give it a head start; it may be waiting for this request's lock

    sa.event.listen(engine, "before_cursor_execute", second_request_now)
    try:
        first.post("/sign-in", data={"email": "test_vol_01@example.test"})
    finally:
        sa.event.remove(engine, "before_cursor_execute", second_request_now)

    assert started, "the test couldn't reach the moment it checks"
    started[0].join(timeout=30)
    assert not started[0].is_alive(), "the second request never finished"
    assert not errors, f"the second request failed: {errors[0]!r}"
    assert len(mails_to(inbox, "test_vol_01@example.test")) == 10, "not exactly 10 sign-in emails in a day"
