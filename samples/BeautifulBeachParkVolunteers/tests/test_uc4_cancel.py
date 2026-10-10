"""UC-4: Cancel a sign-up (Test Plan Section 7)."""

import datetime as dt

from conftest import MSG, TASK, TODAY, TOMORROW, text


def test_t_04_01_cancel_reopens_a_place(beach_task, people):
    """HP · UC-4 main flow, AC1"""
    vol = people("test_vol_01")
    vol.sign_up()
    path = vol.cancel_path(TASK, TOMORROW, "09:00", "10:00")
    assert path, "no 'Cancel' link on S-5"
    assert "Yes, cancel" in text(vol.get(path))

    vol.post(path, data={"confirm": "yes"})
    assert TASK not in text(vol.get("/my-sign-ups"))
    assert "9:00 – 10:00 2 places left" in text(vol.open_slots())


def test_t_04_02_only_your_own_sign_ups(beach_task, people):
    """EF · UC-4 AC2"""
    vol1, vol2 = people("test_vol_01"), people("test_vol_02")
    vol1.sign_up()
    path = vol1.cancel_path(TASK, TOMORROW, "09:00", "10:00")

    resp = vol2.client.post(path, data={"confirm": "yes"}, follow_redirects=True)
    assert resp.status_code == 403
    assert MSG["not_allowed"] in text(resp)
    assert TASK in text(vol1.get("/my-sign-ups"))


def test_t_04_03_not_after_the_slot_starts(clock, coord, people):
    """EF · UC-4 AC3, 2a"""
    clock.set(dt.datetime.combine(TODAY, dt.time(11, 0)))
    coord.post_task(title="Test Pulling Weeds", day=TODAY, slots=(("11:50", "12:50", 2),))
    vol = people("test_vol_01")
    vol.sign_up("Test Pulling Weeds", "11:50", "12:50")
    path = vol.cancel_path("Test Pulling Weeds", TODAY, "11:50", "12:50")

    clock.set(dt.datetime.combine(TODAY, dt.time(12, 0)))  # started 10 minutes ago
    resp = vol.post(path, data={"confirm": "yes"})
    assert MSG["started"] in text(resp)
    assert "Test Pulling Weeds" in text(vol.get("/my-sign-ups"))
