"""Sending email: the test inbox, the pretend inbox, or a real email service.

Which one is used depends on the settings (d08-02 Section 5):

- TEST_INBOX (tests only): a Python list; each email is appended to it.
- EMAIL_SERVICE=pretend (the local environment and the stakeholder demo):
  emails are kept in memory and shown at /pretend-inbox. Nothing is sent.
- EMAIL_SERVICE=smtp (Parks IT's servers): sent through the city email
  service, using SMTP_HOST, SMTP_PORT, SMTP_USER, and SMTP_PASSWORD.
"""

import smtplib
import threading
from email.message import EmailMessage

from flask import current_app

_pretend_lock = threading.Lock()


def send(to, subject, text):
    app = current_app
    mail = {"to": to, "from": app.config["EMAIL_FROM"], "subject": subject, "text": text}
    inbox = app.config.get("TEST_INBOX")
    if inbox is not None:
        inbox.append(mail)
        return
    service = app.config["EMAIL_SERVICE"]
    if service == "pretend":
        with _pretend_lock:
            app.extensions["pretend_inbox"].append(mail)
            del app.extensions["pretend_inbox"][:-200]
        return
    if service == "smtp":
        msg = EmailMessage()
        msg["From"], msg["To"], msg["Subject"] = mail["from"], to, subject
        msg.set_content(text)
        with smtplib.SMTP(app.config["SMTP_HOST"], int(app.config["SMTP_PORT"]), timeout=20) as smtp:
            smtp.starttls()
            if app.config.get("SMTP_USER"):
                smtp.login(app.config["SMTP_USER"], app.config["SMTP_PASSWORD"])
            smtp.send_message(msg)
        return
    raise RuntimeError(f"Unknown EMAIL_SERVICE {service!r}: use 'pretend' or 'smtp'")
