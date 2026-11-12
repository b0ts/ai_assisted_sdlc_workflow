"""UC-7: Block a volunteer (Test Plan Section 7)."""

from conftest import MSG, TASK, TEST_EMAIL_RE, block_confirm_wording, body, target_of, text


def test_t_07_01_block_a_volunteer(beach_task, people):
    """HP · UC-7 main flow, AC1, AC3"""
    vol4 = people("test_vol_04")
    vol4.sign_up()
    other_slot = vol4.signup_path(TASK, "10:00", "11:00")
    path = target_of(beach_task.roster(), "Block test_vol_04")
    assert path, "no 'Block' link on S-8"

    confirm = beach_task.get(path)
    assert block_confirm_wording("test_vol_04") in text(confirm)
    assert not TEST_EMAIL_RE.search(body(confirm))

    resp = beach_task.post(path, data={"confirm": "yes"})
    assert MSG["blocked"] in text(resp)
    assert not TEST_EMAIL_RE.search(body(resp))

    refused = vol4.client.post(other_slot, follow_redirects=True)
    assert MSG["not_allowed"] in text(refused)


def test_t_07_02_coordinator_cannot_undo_a_block(beach_task, people):
    """EF · UC-7 AC4"""
    vol4 = people("test_vol_04")
    path = vol4.signup_path(TASK, "09:00", "10:00")
    beach_task.block("test_vol_04")

    resp = beach_task.client.post("/blocked/test_vol_04/undo", follow_redirects=True)
    assert resp.status_code == 403
    assert MSG["not_allowed"] in text(resp)
    assert MSG["not_allowed"] in text(vol4.client.post(path, follow_redirects=True))


def test_t_07_03_admin_undoes_a_block(beach_task, people, admin):
    """HP · UC-7 1a, AC4"""
    vol4 = people("test_vol_04")
    beach_task.block("test_vol_04")

    page = admin.get("/blocked")
    assert "test_vol_04" in text(page)
    assert not TEST_EMAIL_RE.search(body(page)), "S-10 shows an email address"
    path = target_of(page, "Undo block for test_vol_04")
    assert path, "no 'Undo block' button on S-10"

    assert MSG["unblocked"] in text(admin.post(path))
    assert MSG["signed_up"] in text(vol4.sign_up())


def test_t_07_04_block_returns_to_the_roster(beach_task, people):
    """HP · d05-01 v1.2, UC-7 flow; round 1, R-9"""
    vol4 = people("test_vol_04")
    vol4.sign_up()
    roster_path = beach_task.roster_path()
    path = target_of(beach_task.roster(), "Block test_vol_04")

    resp = beach_task.post(path, data={"confirm": "yes"})
    assert MSG["blocked"] in text(resp)
    assert resp.request.path == roster_path, "'Yes, block' didn't return to the roster"


def test_t_07_05_blocking_cancels_upcoming_sign_ups(app, inbox, clock, beach_task, people):
    """HP · UC-7 main flow 3, AC2 (PRD v1.3); round 2, R2-9"""
    from conftest import NOON, mails_to, run_command

    vol4 = people("test_vol_04")
    vol4.sign_up(TASK, "09:00", "10:00")
    vol4.sign_up(TASK, "10:00", "11:00")
    vol1 = people("test_vol_01")
    vol1.sign_up(TASK, "09:00", "10:00")

    beach_task.block("test_vol_04")

    assert "test_vol_04" not in text(beach_task.roster(TASK, "09:00", "10:00"))
    assert "test_vol_04" not in text(beach_task.roster(TASK, "10:00", "11:00"))
    assert "test_vol_01" in text(beach_task.roster(TASK, "09:00", "10:00")), "someone else's sign-up was canceled"
    assert "1 place left" in text(vol1.open_slots()), "the 9:00 place wasn't given back"
    assert "2 places left" in text(vol1.open_slots()), "the 10:00 places weren't given back"

    since = len(inbox)
    clock.set(NOON.replace(hour=18))
    run_command(app, "send-reminders")
    run_command(app, "send-emails")
    assert not [m for m in mails_to(inbox, vol4.email, since) if m["subject"].startswith("Reminder")], (
        "a blocked volunteer got a reminder"
    )
    assert [m for m in mails_to(inbox, vol1.email, since) if m["subject"].startswith("Reminder")]
