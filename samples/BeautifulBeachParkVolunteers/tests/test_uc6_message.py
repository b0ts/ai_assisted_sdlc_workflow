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
