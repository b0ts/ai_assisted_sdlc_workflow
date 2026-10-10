"""UC-2: Create an account (Test Plan Section 7)."""

from conftest import MSG, elements, form_fields, mails_to, new_client, run_command, sign_in_link, text


def create(app, username, email, accept=True):
    client = new_client(app)
    data = {"username": username, "email": email}
    if accept:
        data["privacy_accepted"] = "yes"
    return client, client.post("/create-account", data=data, follow_redirects=True)


def test_t_02_01_create_account_with_username_and_email_only(app, inbox):
    """HP · UC-2 main flow, AC1"""
    client = new_client(app)
    form = client.get("/create-account")
    assert form.status_code == 200
    assert sorted(form_fields(form)) == ["email", "privacy_accepted", "username"]

    _, resp = create(app, "test_vol_01", "test_vol_01@example.test")
    assert MSG["check_email"] in text(resp)

    sent = mails_to(inbox, "test_vol_01@example.test")
    assert len(sent) == 1
    client = new_client(app)
    assert client.get(sign_in_link(sent[0]), follow_redirects=True).status_code == 200
    assert client.get("/my-sign-ups").status_code == 200, "the new account could not sign in"


def test_t_02_02_username_taken(app, inbox):
    """EF · UC-2 3a"""
    create(app, "test_vol_01", "test_vol_01@example.test")
    _, resp = create(app, "test_vol_01", "someone_else@example.test")
    assert MSG["username_taken"] in text(resp)
    assert not mails_to(inbox, "someone_else@example.test")


def test_t_02_03_username_bounds(app, inbox):
    """BC · UC-2 AC2; d05-01 v1.1"""
    cases = [
        ("ab", False),
        ("abc", True),
        ("u" * 20, True),
        ("v" * 21, False),
        ("sandy helps", False),
    ]
    for i, (username, accepted) in enumerate(cases):
        email = f"bounds_{i}@example.test"
        _, resp = create(app, username, email)
        if accepted:
            assert MSG["check_email"] in text(resp), f"{username!r} was refused"
            assert mails_to(inbox, email)
        else:
            assert MSG["username_rules"] in text(resp), f"{username!r} was not refused"
            assert not mails_to(inbox, email)


def test_t_02_04_blocked_email_refused_even_written_differently(app, inbox, coord):
    """EF · UC-2 AC4, 3b; UC-7 AC2"""
    run_command(app, "create-account", "john_test", "john@example.test", "--role", "volunteer")
    assert MSG["blocked"] in text(coord.block("john_test"))

    _, resp = create(app, "johnny_beach", "j.o.h.n+beach@example.test")
    shown = text(resp)
    assert MSG["couldnt_create"] in shown
    assert "block" not in shown.lower()
    assert not mails_to(inbox, "j.o.h.n+beach@example.test")


def test_t_02_05_privacy_notice_must_be_ticked(app, inbox):
    """EF · UC-2 AC3"""
    page = new_client(app).get("/create-account")
    tick_required = any(
        el["tag"] == "input" and el["attrs"].get("name") == "privacy_accepted" and "required" in el["attrs"]
        for el in elements(page).elements
    )
    button_disabled = any(
        el["tag"] in ("button", "input")
        and el["attrs"].get("type", "submit") == "submit"
        and "disabled" in el["attrs"]
        for el in elements(page).elements
    )
    assert tick_required or button_disabled, "'Create account' can be used without ticking the box"

    create(app, "test_vol_01", "test_vol_01@example.test", accept=False)
    assert not mails_to(inbox, "test_vol_01@example.test"), "an account was saved without the tick"
