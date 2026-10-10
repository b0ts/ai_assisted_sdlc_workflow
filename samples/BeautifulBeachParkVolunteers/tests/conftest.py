"""Shared setup for the BeautifulBeachPark Volunteers tests.

Read tests/README.md first: it describes what these helpers expect the app
to provide (the contract between Step 07 and Step 08).
"""

import datetime as dt
import html
import os
import re
from html.parser import HTMLParser

import pytest

# ---------------------------------------------------------------------------
# Fixed test data (Test Plan Section 6)
# ---------------------------------------------------------------------------

TODAY = dt.date(2027, 4, 20)
TOMORROW = TODAY + dt.timedelta(days=1)
DAY_AFTER = TODAY + dt.timedelta(days=2)
NOON = dt.datetime.combine(TODAY, dt.time(12, 0))

TASK = "Test Beach Cleanup"
TWO_SLOTS = (("09:00", "10:00", 2), ("10:00", "11:00", 2))

# Any test email address. The domain is reserved, so it never reaches a real inbox.
TEST_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@example\.test", re.IGNORECASE)

# Exact wording from the UI/UX Document (d05-01 Section 9)
MSG = {
    "check_email": "Check your email. If you have an account, we've sent you a sign-in link.",
    "link_expired": "This link has expired. We've sent a new one.",
    "username_taken": "That username is taken. Please try another.",
    "username_rules": "Usernames are 3 to 20 letters, numbers, or underscores.",
    "couldnt_create": "We couldn't create this account. Please contact the park office.",
    "signed_up": "You're signed up! We'll email you a reminder the day before.",
    "just_taken": "Sorry, this slot was just taken. Here are other open times.",
    "already": "You're already signed up for this slot.",
    "started": "This slot has already started, so it can't be canceled.",
    "one_hour": "Each slot must be one hour.",
    "places_range": "Each slot needs 1 to 20 volunteers.",
    "title_long": "Titles can be up to 60 characters.",
    "empty_roster": "No one has signed up yet.",
    "blocked": "Blocked.",
    "sent": "Message sent.",
    "message_long": "Messages can be up to 500 characters.",
    "unblocked": "Block removed.",
    "not_allowed": "Not allowed. Please contact the park office if you think this is wrong.",
}

ALL_REFUSALS = [
    MSG[k]
    for k in (
        "username_taken", "username_rules", "couldnt_create", "just_taken", "already",
        "started", "one_hour", "places_range", "title_long", "message_long", "not_allowed",
    )
]


def block_confirm_wording(username):
    return (
        f"Block {username}? They won't be able to sign up for any slots. "
        "Only the System Administrator can undo this."
    )


# ---------------------------------------------------------------------------
# Reading pages
# ---------------------------------------------------------------------------


def body(resp):
    """The raw page or reply, with HTML codes like &#39; turned back into characters."""
    return html.unescape(resp.get_data(as_text=True))


def text(resp):
    """What a person reads on the page: tags removed, spaces collapsed."""
    raw = resp.get_data(as_text=True)
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


class _Elements(HTMLParser):
    """Collects every element's tag and attributes, noting the form it sits in."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.form = None
        self.labels = {}
        self._label_for = None
        self._label_text = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v if v is not None else "") for k, v in attrs}
        if tag == "form":
            self.form = a
        if tag == "label":
            self._label_for = a.get("for", "")
            self._label_text = []
        self.elements.append({"tag": tag, "attrs": a, "form": self.form})

    def handle_endtag(self, tag):
        if tag == "form":
            self.form = None
        if tag == "label" and self._label_for is not None:
            self.labels[self._label_for] = " ".join("".join(self._label_text).split())
            self._label_for = None

    def handle_data(self, data):
        if self._label_for is not None:
            self._label_text.append(data)


def elements(resp):
    p = _Elements()
    p.feed(resp.get_data(as_text=True))
    return p


def target_of(resp, aria_label):
    """The address a link or form button with this accessible label goes to, or None."""
    for el in elements(resp).elements:
        if el["attrs"].get("aria-label") == aria_label:
            if el["tag"] == "a":
                return el["attrs"].get("href")
            if el["form"] is not None:
                return el["form"].get("action")
    return None


def form_fields(resp):
    """Names of the fields a person can fill in (not hidden fields or buttons)."""
    names = []
    for el in elements(resp).elements:
        a = el["attrs"]
        if el["tag"] == "input" and a.get("type", "text") not in ("hidden", "submit", "button"):
            names.append(a.get("name", ""))
        elif el["tag"] in ("textarea", "select"):
            names.append(a.get("name", ""))
    return names


def slot_label(start, end):
    """'09:00', '10:00' -> '9 to 10' (12-hour clock, as in the mockups)."""
    def h(t):
        hour = int(t.split(":")[0]) % 12
        return str(hour or 12)
    return f"{h(start)} to {h(end)}"


def slot_time(start, end):
    """'09:00', '10:00' -> '9:00 – 10:00' (en dash, 12-hour clock)."""
    def h(t):
        hour, minute = t.split(":")
        return f"{int(hour) % 12 or 12}:{minute}"
    return f"{h(start)} – {h(end)}"


# ---------------------------------------------------------------------------
# The app, the clock, and the test inbox
# ---------------------------------------------------------------------------


class Clock:
    """Park time that tests can move forward. The app must use it for every 'now'."""

    def __init__(self, now):
        self.now = now

    def __call__(self):
        return self.now

    def set(self, now):
        self.now = now

    def advance(self, **kwargs):
        self.now += dt.timedelta(**kwargs)


@pytest.fixture
def clock():
    return Clock(NOON)


@pytest.fixture
def inbox():
    """The test inbox: the app appends {'to', 'from', 'subject', 'text'} for every email."""
    return []


@pytest.fixture
def db_url(tmp_path):
    return os.environ.get("TEST_DATABASE_URL") or f"sqlite:///{tmp_path / 'test.db'}"


def make_app(clock, inbox, db_url, **extra):
    from bbpv import create_app  # fails until Step 08 builds src/bbpv

    config = {
        "TESTING": True,
        "DATABASE_URL": db_url,
        "CLOCK": clock,
        "TEST_INBOX": inbox,
        "SECRET_KEY": "test-only-secret",
        "BASE_URL": "https://volunteers.example.test",
    }
    config.update(extra)
    return create_app(config)


def drop_all_tables(db_url):
    import sqlalchemy as sa

    engine = sa.create_engine(db_url)
    meta = sa.MetaData()
    meta.reflect(engine)
    meta.drop_all(engine)
    engine.dispose()


@pytest.fixture
def app(clock, inbox, db_url):
    application = make_app(clock, inbox, db_url)
    yield application
    if os.environ.get("TEST_DATABASE_URL"):
        drop_all_tables(db_url)


def dump_database(db_url):
    """Every value in every table, as text. Used to look for stored email addresses."""
    import sqlalchemy as sa

    engine = sa.create_engine(db_url)
    values = []
    with engine.connect() as conn:
        for table in sa.inspect(engine).get_table_names():
            for row in conn.execute(sa.text(f'SELECT * FROM "{table}"')):
                for v in row:
                    if isinstance(v, (bytes, bytearray, memoryview)):
                        v = bytes(v).decode("latin-1")
                    values.append(f"{table}: {v}")
    engine.dispose()
    return values


def run_command(app, *args):
    result = app.test_cli_runner().invoke(args=list(args))
    assert result.exit_code == 0, f"flask {' '.join(args)} failed:\n{result.output}"
    return result.output


def new_client(app, scheme="https"):
    """A browser session that visits https://volunteers.example.test (or http:// for T-SEC-02)."""
    client = app.test_client()
    base_url = f"{scheme}://volunteers.example.test"
    plain_open = client.open

    def open_with_base_url(*args, **kwargs):
        if args and isinstance(args[0], str):
            kwargs.setdefault("base_url", base_url)
        return plain_open(*args, **kwargs)

    client.open = open_with_base_url
    return client


def mails_to(inbox, email, since=0):
    return [m for m in inbox[since:] if m["to"].lower() == email.lower()]


def sign_in_link(mail):
    match = re.search(r"/sign-in/[A-Za-z0-9_\-.~]+", mail["text"])
    assert match, f"no sign-in link in the email: {mail['text']!r}"
    return match.group(0)


def sign_in(client, inbox, email):
    since = len(inbox)
    client.post("/sign-in", data={"email": email})
    sent = mails_to(inbox, email, since)
    assert sent, f"no sign-in email arrived for {email}"
    resp = client.get(sign_in_link(sent[-1]), follow_redirects=True)
    assert resp.status_code == 200, f"sign-in link failed for {email}: {resp.status_code}"
    return resp


# ---------------------------------------------------------------------------
# People
# ---------------------------------------------------------------------------


class Person:
    """A signed-in test account with its own browser session."""

    def __init__(self, app, inbox, username, email, role):
        self.app, self.inbox = app, inbox
        self.username, self.email, self.role = username, email, role
        self.client = new_client(app)

    def get(self, path, **kw):
        return self.client.get(path, follow_redirects=True, **kw)

    def post(self, path, data=None, **kw):
        return self.client.post(path, data=data or {}, follow_redirects=True, **kw)

    # --- Volunteers -------------------------------------------------------

    def open_slots(self):
        return self.get("/slots")

    def signup_path(self, title, start, end):
        target = target_of(self.open_slots(), f"Sign up for {title}, {slot_label(start, end)}")
        if target is None:
            return None
        return target.replace("/confirm", "/sign-up")

    def sign_up(self, title=TASK, start="09:00", end="10:00"):
        path = self.signup_path(title, start, end)
        assert path, f"{self.username} found no 'Sign up' for {title} {start}-{end} on S-3"
        assert self.get(path.replace("/sign-up", "/confirm")).status_code == 200
        return self.post(path)

    def cancel_path(self, title, day, start, end):
        day_label = f"{day.strftime('%B')} {day.day}"
        return target_of(self.get("/my-sign-ups"), f"Cancel {title}, {day_label}, {slot_label(start, end)}")

    # --- Coordinators -----------------------------------------------------

    def post_task(self, title=TASK, day=TOMORROW, slots=TWO_SLOTS, description="Made-up test task"):
        data = {
            "title": title,
            "description": description,
            "date": day.isoformat(),
            "slot_start": [s[0] for s in slots],
            "slot_end": [s[1] for s in slots],
            "places": [str(s[2]) for s in slots],
        }
        return self.post("/tasks/new", data=data)

    def roster_path(self, title=TASK, start="09:00", end="10:00"):
        return target_of(self.get("/my-tasks"), f"Roster for {title}, {slot_label(start, end)}")

    def roster(self, title=TASK, start="09:00", end="10:00"):
        path = self.roster_path(title, start, end)
        assert path, f"no 'Roster' link for {title} {start}-{end} on S-6"
        return self.get(path)

    def block(self, username):
        return self.post(f"/volunteers/{username}/block", data={"confirm": "yes"})


@pytest.fixture
def people(app, inbox):
    """make('test_vol_01') creates an account through the admin command and signs it in."""
    made = {}

    def make(username, role="volunteer", email=None):
        if username in made:
            return made[username]
        email = email or f"{username}@example.test"
        run_command(app, "create-account", username, email, "--role", role)
        person = Person(app, inbox, username, email, role)
        sign_in(person.client, inbox, email)
        made[username] = person
        return person

    return make


@pytest.fixture
def coord(people):
    return people("test_coord_01", role="coordinator")


@pytest.fixture
def admin(people):
    return people("test_admin_01", role="admin")


@pytest.fixture
def beach_task(coord):
    """'Test Beach Cleanup' tomorrow: 9:00 and 10:00 slots, 2 places each."""
    resp = coord.post_task()
    assert resp.status_code == 200
    return coord
