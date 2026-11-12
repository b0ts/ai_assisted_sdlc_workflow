"""UC-2: Create an account (Test Plan Section 7)."""

from conftest import MSG, elements, form_fields, mails_to, new_client, run_command, sign_in_link, text, use_link


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
    assert use_link(client, sign_in_link(sent[0]), follow_redirects=True).status_code == 200
    assert client.get("/my-sign-ups").status_code == 200, "the new account could not sign in"


def test_t_02_02_username_taken(app, inbox):
    """EF · UC-2 3a (v1.6: the account exists once its owner signs in, PRD v1.3 UC-2 step 4)"""
    client, _ = create(app, "test_vol_01", "test_vol_01@example.test")
    use_link(client, sign_in_link(mails_to(inbox, "test_vol_01@example.test")[-1]))
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


def test_t_02_06_an_email_in_use_gets_the_same_reply(app, inbox):
    """EF · UC-2 3c, AC5 (PRD v1.3); Spec 7, DD-10; round 2, R2-2

    Creating an account with an email that already has one must look exactly
    like creating a new account, so no one can find out who volunteers. The
    owner gets a sign-in link instead.
    """
    import sqlalchemy as sa

    _, new = create(app, "test_vol_01", "test_vol_01@example.test")
    since = len(inbox)
    _, again = create(app, "test_vol_02", "Test_Vol_01@example.test")
    assert again.status_code == new.status_code
    assert text(again) == text(new), "the reply shows that the email already has an account"

    sent = mails_to(inbox, "test_vol_01@example.test", since)
    assert len(sent) == 1, "the account's owner didn't get a sign-in link"
    sign_in_link(sent[0])
    with app.extensions["engine"].connect() as conn:
        names = conn.execute(sa.text("SELECT username FROM accounts")).scalars().all()
    assert "test_vol_02" not in names, "a second account was made with the same email"

    _, later = create(app, "test_vol_02", "test_vol_02@example.test")
    assert MSG["check_email"] in text(later), "the username was used up by the refused attempt"


def test_t_02_07_no_number_of_tries_shows_who_has_an_account(app, inbox):
    """EF · UC-2 4a, AC5 (PRD v1.3); Spec DD-13; round 2 re-review, R2-14

    Try a username with someone's email, then the same username with your own.
    Before v1.3, the second try showed whether the first email had an account.
    Now nothing is saved until the email's owner signs in.
    """
    import sqlalchemy as sa

    def accounts():
        with app.extensions["engine"].connect() as conn:
            return sorted(conn.execute(sa.text("SELECT username FROM accounts")).scalars().all())

    run_command(app, "create-account", "test_vol_01", "test_vol_01@example.test", "--role", "volunteer")
    _, first_a = create(app, "probe_one", "test_vol_01@example.test")      # has an account
    _, second_a = create(app, "probe_one", "prober_a@example.test")
    _, first_b = create(app, "probe_two", "new_person@example.test")      # has none
    _, second_b = create(app, "probe_two", "prober_b@example.test")
    assert text(first_a) == text(first_b) and MSG["check_email"] in text(first_a)
    assert text(second_a) == text(second_b), "the second try shows whether the first email had an account"
    assert MSG["username_taken"] not in text(second_b)
    assert accounts() == ["test_vol_01"], "an account was made before anyone signed in"

    owner = new_client(app)
    resp = use_link(owner, sign_in_link(mails_to(inbox, "new_person@example.test")[-1]))
    assert resp.status_code in (302, 303), "the new account's owner couldn't sign in"
    assert owner.get("/slots").status_code == 200
    assert accounts() == ["probe_two", "test_vol_01"]

    late = use_link(new_client(app), sign_in_link(mails_to(inbox, "prober_b@example.test")[-1]),
                    follow_redirects=True)
    assert MSG["username_taken"] in text(late), "two accounts got the same username"
    assert accounts() == ["probe_two", "test_vol_01"]


def test_t_02_08_the_first_of_two_emails_still_works(app, inbox):
    """EF · Spec DD-13, Section 6; round 2 re-review 2, R2-17

    A double tap on "Create account" sends two emails. The first one's link
    must still work; once it's used, the other stops working.
    """
    import sqlalchemy as sa

    create(app, "test_vol_01", "test_vol_01@example.test")
    create(app, "test_vol_01", "test_vol_01@example.test")
    first, second = mails_to(inbox, "test_vol_01@example.test")

    person = new_client(app)
    resp = use_link(person, sign_in_link(first))
    assert resp.status_code in (302, 303), "the first email's link stopped working"
    assert person.get("/slots").status_code == 200

    late = new_client(app)
    assert MSG["link_invalid"] in text(late.get(sign_in_link(second)))
    assert MSG["link_invalid"] in text(late.post(sign_in_link(second), follow_redirects=True))
    with app.extensions["engine"].connect() as conn:
        assert conn.execute(sa.text("SELECT COUNT(*) FROM accounts")).scalar() == 1
