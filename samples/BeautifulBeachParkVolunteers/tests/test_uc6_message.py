"""UC-6: Message a volunteer (Test Plan Section 7)."""

from conftest import MSG, TEST_EMAIL_RE, body, mails_to, target_of, text


def test_t_06_01_message_relayed_without_revealing_emails(inbox, beach_task, people):
    """HP · UC-6 AC1"""
    vol = people("test_vol_01")
    vol.sign_up()
    path = target_of(beach_task.roster(), "Message test_vol_01")
    assert path, "no 'Message' link on S-8"

    form = beach_task.get(path)
    assert not TEST_EMAIL_RE.search(body(form)), "S-9 shows an email address"

    since = len(inbox)
    resp = beach_task.post(path, data={"message": "Please bring gloves tomorrow."})
    assert MSG["sent"] in text(resp)
    assert not TEST_EMAIL_RE.search(body(resp))

    sent = mails_to(inbox, vol.email, since)
    assert len(sent) == 1
    mail = sent[0]
    assert "Please bring gloves tomorrow." in mail["text"]
    assert "no-reply" in mail["from"].lower() or "noreply" in mail["from"].lower()
    everything = " ".join(str(v) for v in mail.values())
    assert beach_task.email not in everything, "the coordinator's email was in the message"


def test_t_06_02_message_length_bounds(inbox, beach_task, people):
    """BC · UC-6 AC2, 1a"""
    vol = people("test_vol_01")
    vol.sign_up()
    path = target_of(beach_task.roster(), "Message test_vol_01")

    since = len(inbox)
    assert MSG["sent"] in text(beach_task.post(path, data={"message": "a" * 500}))
    assert len(mails_to(inbox, vol.email, since)) == 1

    since = len(inbox)
    resp = beach_task.post(path, data={"message": "b" * 501})
    assert MSG["message_long"] in text(resp)
    assert not mails_to(inbox, vol.email, since)


def test_t_06_03_counter_and_back_to_the_roster(inbox, beach_task, people):
    """HP · d05-01 v1.2, S-9 and UC-6 flow; round 1, R-9"""
    vol = people("test_vol_01")
    vol.sign_up()
    roster_path = beach_task.roster_path()
    path = target_of(beach_task.roster(), "Message test_vol_01")

    form = beach_task.get(path)
    assert "0 of 500 characters" in text(form), "S-9 has no character counter"

    resp = beach_task.post(path, data={"message": "See you at the north entrance."})
    assert MSG["sent"] in text(resp)
    assert resp.request.path == roster_path, "Send didn't return to the roster"
    assert "test_vol_01" in text(resp)


def test_t_06_04_a_line_break_counts_as_one_character(inbox, beach_task, people):
    """BC · UC-6 AC2 (PRD v1.3); d05-01 v1.3, S-9 counter; round 2, R2-1

    Browsers send each line break in a form as two characters (CR LF). The
    counter counts one, so the server must too.
    """
    vol = people("test_vol_01")
    vol.sign_up()
    path = target_of(beach_task.roster(), "Message test_vol_01")

    message = "\r\n".join(["m" * 70] * 7)  # 490 letters + 6 line breaks = 496 counted
    message += "m" * 4  # = 500 counted, 506 as sent
    since = len(inbox)
    assert MSG["sent"] in text(beach_task.post(path, data={"message": message}))
    sent = mails_to(inbox, vol.email, since)
    assert len(sent) == 1
    assert "m" * 70 + "\n" + "m" * 70 in sent[0]["text"].replace("\r\n", "\n")

    since = len(inbox)
    resp = beach_task.post(path, data={"message": message + "m"})
    assert MSG["message_long"] in text(resp)
    assert not mails_to(inbox, vol.email, since)
