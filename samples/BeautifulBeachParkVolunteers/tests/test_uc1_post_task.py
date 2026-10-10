"""UC-1: Post a task (Test Plan Section 7)."""

from conftest import MSG, TASK, TOMORROW, slot_label, target_of, text


def test_t_01_01_posted_slots_appear_straight_away(coord, people):
    """HP · UC-1 AC4, AC1"""
    resp = coord.post_task()
    assert resp.status_code == 200

    page = people("test_vol_01").open_slots()
    shown = text(page)
    assert TASK in shown
    assert "9:00 – 10:00 2 places left" in shown
    assert "10:00 – 11:00 2 places left" in shown
    assert target_of(page, f"Sign up for {TASK}, {slot_label('09:00', '10:00')}")
    assert target_of(page, f"Sign up for {TASK}, {slot_label('10:00', '11:00')}")


def test_t_01_02_slot_not_one_hour_is_refused_by_server(coord, people):
    """EF · UC-1 AC1, 2a. S-7 can't make this (UX-3), so the server is checked directly."""
    resp = coord.post_task(slots=(("09:00", "10:30", 2),))
    assert MSG["one_hour"] in text(resp)
    assert TASK not in text(people("test_vol_01").open_slots())
    assert TASK not in text(coord.get("/my-tasks"))


def test_t_01_03_places_per_slot_bounds(coord):
    """BC · UC-1 AC2, 2b"""
    for places, saved in ((1, True), (20, True), (0, False), (21, False)):
        title = f"Test Places {places}"
        resp = coord.post_task(title=title, slots=(("09:00", "10:00", places),))
        listed = title in text(coord.get("/my-tasks"))
        if saved:
            assert MSG["places_range"] not in text(resp), f"{places} places was refused"
            assert listed, f"{places} places was not saved"
        else:
            assert MSG["places_range"] in text(resp), f"{places} places was not refused"
            assert not listed, f"{places} places was saved"


def test_t_01_04_title_length_bounds(coord):
    """BC · Spec 6; d05-01 v1.1"""
    title_60 = "T" * 59 + "A"
    title_61 = "T" * 60 + "B"

    resp = coord.post_task(title=title_60)
    assert MSG["title_long"] not in text(resp)
    assert title_60 in text(coord.get("/my-tasks"))

    resp = coord.post_task(title=title_61)
    assert MSG["title_long"] in text(resp)
    assert title_61 not in text(coord.get("/my-tasks"))


def test_t_01_05_only_coordinators_can_post(people, coord):
    """EF · UC-1 AC3"""
    vol = people("test_vol_01")
    resp = vol.post_task(title="Test Not Allowed Task", day=TOMORROW)
    assert resp.status_code == 403
    assert MSG["not_allowed"] in text(resp)
    assert "Post a task" not in text(vol.open_slots())
    assert "Test Not Allowed Task" not in text(coord.get("/my-tasks"))
