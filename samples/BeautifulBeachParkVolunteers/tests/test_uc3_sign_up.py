"""UC-3: Sign up for a slot (Test Plan Section 7)."""

import threading

from conftest import (
    DAY_AFTER, MSG, TASK, mails_to, new_client, run_command, sign_in, slot_label, target_of, text,
)


def test_t_03_01_sign_up(beach_task, people):
    """HP · UC-3 main flow, AC1, AC2"""
    vol = people("test_vol_01")
    resp = vol.sign_up()
    assert MSG["signed_up"] in text(resp)
    assert "9:00 – 10:00 1 place left" in text(vol.open_slots())


def test_t_03_02_last_place_shows_full(beach_task, people):
    """BC · UC-3 AC2"""
    people("test_vol_01").sign_up()
    vol2 = people("test_vol_02")
    assert MSG["signed_up"] in text(vol2.sign_up())

    page = vol2.open_slots()
    assert "9:00 – 10:00 Full" in text(page)
    assert target_of(page, f"Sign up for {TASK}, {slot_label('09:00', '10:00')}") is None


def test_t_03_03_slot_taken_while_confirming(beach_task, people):
    """EF · UC-3 2a"""
    vol3 = people("test_vol_03")
    path = vol3.signup_path(TASK, "09:00", "10:00")
    assert vol3.get(path.replace("/sign-up", "/confirm")).status_code == 200  # on S-4

    people("test_vol_01").sign_up()
    people("test_vol_02").sign_up()

    resp = vol3.post(path)
    assert MSG["just_taken"] in text(resp)
    roster = text(beach_task.roster())
    assert "test_vol_03" not in roster


def test_t_03_04_never_over_filled_at_the_same_moment(app, inbox, coord, people):
    """BC · UC-3 AC3; Spec DD-5. Run 50 times; one failure counts as Fail."""
    vol2, vol3 = people("test_vol_02"), people("test_vol_03")
    for round_no in range(50):
        title = f"Test Race {round_no:02d}"
        coord.post_task(title=title, slots=(("09:00", "10:00", 1),))
        path = vol2.signup_path(title, "09:00", "10:00")
        assert path, f"round {round_no}: slot not listed"

        barrier = threading.Barrier(2)
        replies = {}

        def tap(person):
            barrier.wait()
            replies[person.username] = text(person.client.post(path, follow_redirects=True))

        threads = [threading.Thread(target=tap, args=(p,)) for p in (vol2, vol3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        winners = [u for u, r in replies.items() if MSG["signed_up"] in r]
        assert len(winners) == 1, f"round {round_no}: {len(winners)} volunteers got the last place"
        tasks = text(coord.get("/my-tasks"))
        assert f"{title} 9:00 – 10:00 1 of 1" in tasks, f"round {round_no}: places filled is wrong"


def test_t_03_05_already_signed_up(beach_task, people):
    """EF · UC-3 2b"""
    vol = people("test_vol_01")
    path = vol.signup_path(TASK, "09:00", "10:00")
    vol.post(path)
    assert MSG["already"] in text(vol.post(path))


def test_t_03_06_blocked_volunteer_cannot_sign_up(beach_task, people):
    """EF · UC-3 AC4, 2c"""
    vol4 = people("test_vol_04")
    path = vol4.signup_path(TASK, "09:00", "10:00")
    beach_task.block("test_vol_04")

    resp = vol4.client.post(path, follow_redirects=True)
    assert resp.status_code == 403
    assert MSG["not_allowed"] in text(resp)
    assert MSG["empty_roster"] in text(beach_task.roster())


def test_t_03_07_reminder_the_day_before(app, inbox, beach_task, people):
    """HP · UC-3 AC5; Spec UC-3 diagram"""
    beach_task.post_task(title="Test Driftwood Removal", day=DAY_AFTER)
    vol1, vol2 = people("test_vol_01"), people("test_vol_02")
    vol1.sign_up(TASK)
    vol2.sign_up("Test Driftwood Removal")

    since = len(inbox)
    run_command(app, "send-reminders")

    to_vol1 = mails_to(inbox, vol1.email, since)
    assert len(to_vol1) == 1
    assert TASK in to_vol1[0]["subject"] + to_vol1[0]["text"]
    assert not mails_to(inbox, vol2.email, since)
