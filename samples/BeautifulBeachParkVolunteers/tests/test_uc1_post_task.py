"""UC-1: Post a task (Test Plan Section 7)."""

from conftest import MSG, TASK, TOMORROW, slot_label, slot_time, target_of, text


def test_t_01_01_posted_slots_appear_straight_away(coord, people):
    """HP · UC-1 AC4, AC1"""
    resp = coord.post_task()
    assert resp.status_code == 200

    page = people("test_vol_01").open_slots()
    shown = text(page)
    assert TASK in shown
    assert f"{slot_time('09:00', '10:00')} 2 places left" in shown
    assert f"{slot_time('10:00', '11:00')} 2 places left" in shown
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


def test_t_01_06_description_and_slot_count_bounds(coord):
    """BC · UC-1 AC3 (PRD v1.2); round 1, R-12"""
    resp = coord.post_task(title="Test Description 1000", description="d" * 1000)
    assert MSG["description_long"] not in text(resp)
    assert "Test Description 1000" in text(coord.get("/my-tasks"))

    resp = coord.post_task(title="Test Description 1001", description="d" * 1001)
    assert MSG["description_long"] in text(resp)
    assert "Test Description 1001" not in text(coord.get("/my-tasks"))

    ten = tuple((f"{h:02d}:00", f"{h + 1:02d}:00", 1) for h in range(8, 18))
    resp = coord.post_task(title="Test Ten Slots", slots=ten)
    assert MSG["too_many_slots"] not in text(resp)
    assert text(coord.get("/my-tasks")).count("Test Ten Slots") == 10

    eleven = tuple((f"{h:02d}:00", f"{h + 1:02d}:00", 1) for h in range(7, 18))
    resp = coord.post_task(title="Test Eleven Slots", slots=eleven)
    assert MSG["too_many_slots"] in text(resp)
    assert "Test Eleven Slots" not in text(coord.get("/my-tasks"))


def test_t_01_07_add_another_slot_up_to_ten(coord):
    """HP · d05-01 v1.2, S-7; round 1, R-9"""
    from conftest import elements

    def slot_rows(resp):
        return [el for el in elements(resp).elements if el["tag"] == "input" and el["attrs"].get("name") == "slot_start"]

    def add_button(resp):
        return [el for el in elements(resp).elements
                if el["tag"] == "button" and el["attrs"].get("name") == "add_slot"]

    page = coord.get("/tasks/new")
    assert len(slot_rows(page)) == 3
    assert add_button(page), "S-7 has no 'Add another slot' button"

    data = {"title": "Test Add Slot", "description": "", "date": TOMORROW.isoformat(),
            "slot_start": ["09:00", "", ""], "slot_end": ["10:00", "", ""], "places": ["2", "", ""]}
    for expected in range(4, 11):
        resp = coord.post("/tasks/new", data=dict(data, add_slot="yes"))
        assert resp.status_code == 200
        assert len(slot_rows(resp)) == expected, f"expected {expected} slot rows"
        assert "Test Add Slot" in resp.get_data(as_text=True), "the typed title was lost"
        assert "Test Add Slot" not in text(coord.get("/my-tasks")), "adding a row saved the task"
        data["slot_start"] = data["slot_start"] + [""]
    assert not add_button(resp), "'Add another slot' is still offered at 10 rows"


def test_t_01_08_a_line_break_counts_as_one_character(coord):
    """BC · UC-1 AC3 (PRD v1.3); round 2, R2-1

    Browsers send each line break in a form as two characters (CR LF). The
    counter counts one, so the server must too.
    """
    lines = "\r\n".join(["d" * 99] * 10) + "d"  # 991 letters + 9 line breaks = 1,000 counted
    assert len(lines.replace("\r\n", "\n")) == 1000 and len(lines) == 1009
    resp = coord.post_task(title="Test Description Lines", description=lines)
    assert MSG["description_long"] not in text(resp)
    assert "Test Description Lines" in text(coord.get("/my-tasks"))

    resp = coord.post_task(title="Test Description Lines 2", description=lines + "d")
    assert MSG["description_long"] in text(resp)
