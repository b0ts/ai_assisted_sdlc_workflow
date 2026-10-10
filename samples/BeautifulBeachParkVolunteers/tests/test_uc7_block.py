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
