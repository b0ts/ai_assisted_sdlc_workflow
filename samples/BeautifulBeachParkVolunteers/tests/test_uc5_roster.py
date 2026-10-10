"""UC-5: View a roster (Test Plan Section 7)."""

from conftest import MSG, TASK, slot_label, target_of, text


def test_t_05_01_roster_lists_usernames(beach_task, people):
    """HP · UC-5 main flow, AC1"""
    people("test_vol_01").sign_up()
    people("test_vol_02").sign_up()

    page = beach_task.roster()
    shown = text(page)
    assert "test_vol_01" in shown and "test_vol_02" in shown
    assert "2 of 2 places filled" in shown
    for username in ("test_vol_01", "test_vol_02"):
        assert target_of(page, f"Message {username}"), f"no 'Message' for {username}"
        assert target_of(page, f"Block {username}"), f"no 'Block' for {username}"


def test_t_05_02_empty_roster_says_so(beach_task):
    """BC · UC-5 AC2, 2a"""
    assert MSG["empty_roster"] in text(beach_task.roster(TASK, "10:00", "11:00"))


def test_t_05_03_coordinators_only(beach_task, people):
    """EF · Spec 11.1"""
    path = beach_task.roster_path()
    resp = people("test_vol_01").client.get(path, follow_redirects=True)
    assert resp.status_code == 403
    assert MSG["not_allowed"] in text(resp)


def test_t_05_04_full_slots_still_reachable(beach_task, people):
    """HP · d05-01 Section 16, request 1"""
    people("test_vol_01").sign_up()
    people("test_vol_02").sign_up()

    tasks = beach_task.get("/my-tasks")
    assert "9:00 – 10:00 2 of 2 (Full)" in text(tasks)
    path = target_of(tasks, f"Roster for {TASK}, {slot_label('09:00', '10:00')}")
    assert path, "the full slot has no 'Roster' link"
    assert beach_task.get(path).status_code == 200
