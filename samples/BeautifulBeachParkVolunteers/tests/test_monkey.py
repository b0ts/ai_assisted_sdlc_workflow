"""Monkey tests (Test Plan Section 10): random input and random tapping.

Long-running, so they're marked 'monkey'. Skip them while building with
pytest -m "not monkey". Set MONKEY_SEED to repeat a failing run exactly.
"""

import html
import os
import random
import re
import time

import pytest

from conftest import ALL_REFUSALS, MSG, TASK, TOMORROW, TEST_EMAIL_RE, body, elements, new_client, text

pytestmark = pytest.mark.monkey

INPUTS = int(os.environ.get("MONKEY_INPUTS", "1000"))
SECONDS = float(os.environ.get("MONKEY_SECONDS", "300"))
SEED = int(os.environ.get("MONKEY_SEED", str(int(time.time()))))

NASTY = [
    "", " ", "\t\n", "0", "-1", "21", "99999999999999999999", "1e9", "NaN", "null", "None", "true",
    "<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>", "'; DROP TABLE accounts; --",
    "' OR '1'='1", "{{7*7}}", "${7*7}", "../../etc/passwd", "%00", "\x00", "🌊🏖️🐚", "Ω≈ç√∫", "مرحبا",
    "𝓗𝓮𝓵𝓵𝓸", "a" * 61, "a" * 501, "a" * 5000, "2027-02-30", "2027-13-01", "9999-12-31", "25:00",
    "09:60", "09:00:00", "test_vol_01@example.test", "@", "a@b", "x" * 300 + "@example.test",
]


def random_value(rng):
    roll = rng.random()
    if roll < 0.4:
        return rng.choice(NASTY)
    if roll < 0.7:
        alphabet = "abcXYZ019_ -.@+<>'\"&;%/\\🌊é​"
        return "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 80)))
    if roll < 0.85:
        return str(rng.randint(-1000, 1000))
    return "".join(chr(rng.randint(32, 0x2FFF)) for _ in range(rng.randint(1, 40)))


def check_reply(resp, where, typed=()):
    """No crash, and no email shown except one the person just typed into the form."""
    assert resp.status_code < 500, f"crash ({resp.status_code}) at {where}"
    allowed = {e.lower() for v in typed for e in TEST_EMAIL_RE.findall(str(v))}
    leaked = [e for e in TEST_EMAIL_RE.findall(body(resp)) if e.lower() not in allowed]
    assert not leaked, f"email shown at {where}: {leaked}"


def task_rows(coord):
    """(title, time, filled, places) for every row on S-6."""
    rows = []
    page = coord.get("/my-tasks").get_data(as_text=True)
    for row in re.findall(r"(?is)<tr\b.*?</tr>", page):
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
                 for c in re.findall(r"(?is)<td\b.*?</td>", row)]
        match = len(cells) >= 3 and re.match(r"(\d+) of (\d+)", cells[2])
        if match:
            rows.append((cells[0], cells[1], int(match.group(1)), int(match.group(2))))
    return rows


def assert_rows_follow_rules(coord):
    for title, slot_time, filled, places in task_rows(coord):
        assert len(title) <= 60, f"saved a title of {len(title)} characters"
        assert 1 <= places <= 20, f"saved a slot with {places} places"
        assert 0 <= filled <= places, f"slot {title} {slot_time} has {filled} of {places}"
        hours = re.findall(r"(\d+):(\d\d)", slot_time)
        assert len(hours) == 2, f"odd slot time {slot_time!r}"
        (h1, m1), (h2, m2) = [(int(h) % 12, int(m)) for h, m in hours]
        assert m1 == m2 and (h2 - h1) % 12 == 1, f"slot {slot_time} is not one hour"


def test_t_mk_01_random_input_in_every_form(app, inbox, coord, people):
    """MK · every form: S-1, S-2, S-7, S-9"""
    rng = random.Random(SEED)
    print(f"MONKEY_SEED={SEED}")
    vol = people("test_vol_01")
    coord.post_task()
    vol.sign_up()
    anon = new_client(app)

    # S-1: email
    for _ in range(INPUTS):
        value = random_value(rng)
        check_reply(anon.post("/sign-in", data={"email": value}, follow_redirects=True), "S-1", [value])

    # S-2: username, email (the other field stays valid)
    for field in ("username", "email"):
        for i in range(INPUTS):
            value = random_value(rng)
            data = {"username": f"mk{i}_{field[:1]}", "email": f"mk{i}_{field[:1]}@example.test",
                    "privacy_accepted": "yes", field: value}
            resp = anon.post("/create-account", data=data, follow_redirects=True)
            check_reply(resp, f"S-2 {field}", data.values())
            if MSG["check_email"] in text(resp):
                # The app may trim spaces typed around a username; what it saves must follow the rule.
                assert re.fullmatch(r"[A-Za-z0-9_]{3,20}", data["username"].strip()), (
                    f"saved an account with username {data['username']!r}"
                )

    # S-7: every field (the others stay valid). A saved title is shown again
    # on later pages, so anything the coordinator typed earlier may appear.
    good = {"title": "Test Monkey", "description": "Made-up", "date": TOMORROW.isoformat(),
            "slot_start": "13:00", "slot_end": "14:00", "places": "3"}
    typed_so_far = set()
    for field in good:
        for _ in range(INPUTS):
            data = dict(good, **{field: random_value(rng)})
            typed_so_far.update(TEST_EMAIL_RE.findall(data[field]))
            check_reply(coord.post("/tasks/new", data=data), f"S-7 {field}", typed_so_far)
        assert_rows_follow_rules(coord)

    # S-9: message
    message_path = "/volunteers/test_vol_01/message"
    for _ in range(INPUTS):
        value = random_value(rng)
        resp = coord.post(message_path, data={"message": value})
        check_reply(resp, "S-9", [value])
        if len(value) > 500:
            assert MSG["sent"] not in text(resp), "sent a message over 500 characters"


def test_t_mk_02_random_tapping_as_every_role(app, coord, admin, people):
    """MK · every screen, as each role"""
    rng = random.Random(SEED)
    print(f"MONKEY_SEED={SEED}")
    for title in (TASK, "Test Pulling Weeds", "Test Raking Leaves"):
        coord.post_task(title=title, slots=(("09:00", "10:00", 2), ("10:00", "11:00", 1)))
    vols = [people(f"test_vol_0{i}") for i in range(1, 6)]
    everyone = vols + [coord, admin]
    history = {p.username: ["/slots"] for p in everyone}
    last_form = {}

    deadline = time.monotonic() + SECONDS
    steps = 0
    while time.monotonic() < deadline:
        person = rng.choice(everyone)
        roll = rng.random()
        if roll < 0.15 and len(history[person.username]) > 1:  # back button
            history[person.username].pop()
            path = history[person.username][-1]
            resp = person.client.get(path, follow_redirects=True)
        elif roll < 0.3 and person.username in last_form:  # tap the same button again
            path, data = last_form[person.username]
            resp = person.client.post(path, data=data, follow_redirects=True)
        else:
            page = person.client.get(history[person.username][-1], follow_redirects=True)
            check_reply(page, history[person.username][-1])
            links, forms = [], []
            for el in elements(page).elements:
                href = el["attrs"].get("href", "")
                if el["tag"] == "a" and href.startswith("/") and "sign-out" not in href:
                    links.append(href)
                if el["tag"] == "form" and el["attrs"].get("method", "get").lower() == "post":
                    forms.append(el["attrs"].get("action", ""))
            if forms and rng.random() < 0.5:
                path = rng.choice(forms)
                data = {"confirm": "yes"}
                last_form[person.username] = (path, data)
                resp = person.client.post(path, data=data, follow_redirects=True)
            elif links:
                path = rng.choice(links)
                history[person.username].append(path)
                resp = person.client.get(path, follow_redirects=True)
            else:
                path = rng.choice(["/slots", "/my-sign-ups", "/my-tasks", "/blocked"])
                history[person.username].append(path)
                resp = person.client.get(path, follow_redirects=True)
        check_reply(resp, f"{person.username} at {path}")
        steps += 1
        if steps % 25 == 0:
            assert_rows_follow_rules(coord)
    assert_rows_follow_rules(coord)
    print(f"{steps} random steps")
