"""UC-8: Delete a task (Test Plan Section 7, v1.7; polishing item P-2)."""

from conftest import (
    MSG, NOON, TASK, TOMORROW, delete_confirm_wording, mails_to, run_command, slot_time, target_of, text,
)


def delete_label(title=TASK, day=TOMORROW):
    return f"Delete {title}, {day.strftime('%B')} {day.day}"


def test_t_08_01_delete_a_task_and_tell_the_volunteers(app, inbox, clock, beach_task, people):
    """HP · UC-8 main flow, AC2 to AC4 (PRD v1.4); d05-01 v1.4, UX-9"""
    vol1, vol2 = people("test_vol_01"), people("test_vol_02")
    vol1.sign_up(TASK, "09:00", "10:00")
    vol1.sign_up(TASK, "10:00", "11:00")
    vol2.sign_up(TASK, "09:00", "10:00")

    page = beach_task.get("/my-tasks")
    path = target_of(page, delete_label())
    assert path, "no 'Delete' link for the task on S-6"
    from conftest import elements, my_task_rows
    links = [el for el in elements(page).elements if el["attrs"].get("aria-label") == delete_label()]
    assert len(links) == 1, "the task should have one 'Delete task' button, not one per slot (UX-9)"
    assert "Delete task" in text(page)
    assert [r[0] for r in my_task_rows(page)] == [TASK, TASK], "the slots aren't listed under their task"
    confirm = beach_task.get(path)
    assert delete_confirm_wording(TASK, TOMORROW, 2, 2) in text(confirm)
    assert TASK in text(beach_task.get("/my-tasks")), "opening the confirm page deleted the task"

    since = len(inbox)
    resp = beach_task.post(path, data={"confirm": "yes"})
    assert MSG["task_deleted"] in text(resp)
    assert TASK not in text(beach_task.get("/my-tasks"))
    assert TASK not in text(vol1.open_slots())
    assert TASK not in text(vol1.get("/my-sign-ups"))

    for vol, times in ((vol1, (("09:00", "10:00"), ("10:00", "11:00"))), (vol2, (("09:00", "10:00"),))):
        canceled = [m for m in mails_to(inbox, vol.email, since) if m["subject"].startswith("Canceled:")]
        assert len(canceled) == 1, f"{vol.username} got {len(canceled)} 'canceled' emails"
        assert TASK in canceled[0]["subject"]
        for start, end in times:
            assert slot_time(start, end) in canceled[0]["text"]

    since = len(inbox)
    clock.set(NOON.replace(hour=18))
    run_command(app, "send-reminders")
    run_command(app, "send-emails")
    assert not [m for m in inbox[since:] if m["subject"].startswith("Reminder")], "a deleted task's reminder was sent"


def test_t_08_02_only_the_coordinator_who_posted_it(app, beach_task, people):
    """EF · UC-8 AC1 (PRD v1.4)"""
    path = target_of(beach_task.get("/my-tasks"), delete_label())
    other = people("test_coord_02", role="coordinator")
    assert not target_of(other.get("/my-tasks"), delete_label()), "another coordinator sees 'Delete'"
    vol = people("test_vol_01")
    for person in (other, vol):
        for resp in (person.get(path), person.post(path, data={"confirm": "yes"})):
            assert resp.status_code == 403
            assert MSG["not_allowed"] in text(resp)
    assert TASK in text(beach_task.get("/my-tasks")), "someone else deleted the task"


def test_t_08_03_a_task_nobody_signed_up_for(app, inbox, beach_task):
    """EF · UC-8 1a (PRD v1.4)"""
    path = target_of(beach_task.get("/my-tasks"), delete_label())
    assert delete_confirm_wording(TASK, TOMORROW, 2, 0) in text(beach_task.get(path))
    since = len(inbox)
    assert MSG["task_deleted"] in text(beach_task.post(path, data={"confirm": "yes"}))
    assert TASK not in text(beach_task.get("/my-tasks"))
    assert not inbox[since:], "an email was sent although nobody had signed up"
