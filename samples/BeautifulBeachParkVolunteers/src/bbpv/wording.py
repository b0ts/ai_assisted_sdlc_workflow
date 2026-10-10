"""Every message people see, in one place (Spec Section 10).

The wording comes word for word from the UI/UX Document, d05-01 Section 9,
so the tests can match it exactly. Messages marked "added in Step 8" were
not in d05-01; they are listed in the Implementation Record (d08-01).
"""

CHECK_EMAIL = "Check your email. If you have an account, we've sent you a sign-in link."
LINK_EXPIRED = "This link has expired. We've sent a new one."
PRIVACY_NOTICE = (
    "We only ask for a username and an email address. Other volunteers and coordinators "
    "see only your username, never your email. The park's System Administrator can see "
    "your email to keep the app running. We use it only for sign-in links, reminders, "
    "and messages from coordinators."
)
USERNAME_TAKEN = "That username is taken. Please try another."
USERNAME_RULES = "Usernames are 3 to 20 letters, numbers, or underscores."
COULDNT_CREATE = "We couldn't create this account. Please contact the park office."
SIGNED_UP = "You're signed up! We'll email you a reminder the day before."
JUST_TAKEN = "Sorry, this slot was just taken. Here are other open times."
ALREADY = "You're already signed up for this slot."
STARTED = "This slot has already started, so it can't be canceled."
ONE_HOUR = "Each slot must be one hour."
PLACES_RANGE = "Each slot needs 1 to 20 volunteers."
TITLE_LONG = "Titles can be up to 60 characters."
EMPTY_ROSTER = "No one has signed up yet."
BLOCKED = "Blocked."
SENT = "Message sent."
MESSAGE_LONG = "Messages can be up to 500 characters."
UNBLOCKED = "Block removed."
NOT_ALLOWED = "Not allowed. Please contact the park office if you think this is wrong."


def block_confirm(username):
    return (
        f"Block {username}? They won't be able to sign up for any slots. "
        "Only the System Administrator can undo this."
    )


# Added in Step 8 (not in d05-01; listed in d08-01 for the Designer to confirm)
LINK_INVALID = "This link isn't valid. Please ask for a new one below."
TICK_PRIVACY = "Please tick the box to show you've read the privacy notice."
EMAIL_INVALID = "Please enter a valid email address."
TITLE_MISSING = "Please enter a title."
DESCRIPTION_LONG = "Descriptions can be up to 1,000 characters."
DATE_INVALID = "Please choose a date."
TIME_INVALID = "Please enter each slot's start and end time."
NO_SLOTS = "Please add at least one slot."
TOO_MANY_SLOTS = "A task can have up to 10 slots."
TASK_POSTED = "Task posted."
MESSAGE_MISSING = "Please write a message."
CANCELED = "Your sign-up was canceled. The place is open for someone else."
SLOT_GONE = "This slot has already started."
