"""Every message people see, in one place (Spec Section 10).

The wording comes word for word from the UI/UX Document, d05-01 Section 9
(version 1.2), so the tests can match it exactly. Pages, emails, and error
pages all take their messages from here; nothing else writes a message.
"""

# --- d05-01 Section 9 -------------------------------------------------------

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
SIGNED_UP = "You're signed up! We've emailed you the details."
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


# --- d05-01 Section 9, added in v1.2 ----------------------------------------

LINK_INVALID = "This link isn't valid. Please ask for a new one below."
TICK_PRIVACY = "Please tick the box to show you've read the privacy notice."
EMAIL_INVALID = "Please enter a valid email address."
SLOT_GONE = "This slot has already started."
NO_OPEN_SLOTS = "There are no open slots right now. Please check again soon."
CANCELED = "Your sign-up was canceled. The place is open for someone else."
NO_SIGN_UPS = "You haven't signed up for anything yet."
TASK_POSTED = "Task posted."
NO_TASKS = "You haven't posted any upcoming tasks."
TITLE_MISSING = "Please enter a title."
DESCRIPTION_LONG = "Descriptions can be up to 1,000 characters."
DATE_INVALID = "Please choose a date."
TIME_INVALID = "Please enter each slot's start and end time."
NO_SLOTS = "Please add at least one slot."
TOO_MANY_SLOTS = "A task can have up to 10 slots."
MESSAGE_MISSING = "Please write a message."
NO_BLOCKS = "No one is blocked."
NOT_FOUND = "We couldn't find that page."
BAD_REQUEST = "Something was wrong with that request. Please go back and try again."
SERVER_ERROR = "Something went wrong on our side. Please try again in a few minutes."

# Times (d05-01 v1.2, UX-6): "9:00 – 10:00 a.m." on screen, "9:00 to 10:00 a.m." in labels
MORNING = "a.m."
EVENING = "p.m."
RANGE_DASH = " – "
RANGE_TO = " to "

# Words in front of every banner, so status is never shown by color alone (d05-01 Section 10)
BANNER_PREFIX = {"success": "Done:", "error": "Problem:", "info": "Note:"}

# Page titles for the one-message pages
TITLE_NOT_ALLOWED = "Not allowed"
TITLE_NOT_FOUND = "Not found"
TITLE_TRY_AGAIN = "Please try again"
TITLE_SORRY = "Sorry"


def places_text(left):
    if left <= 0:
        return "Full"
    return "1 place left" if left == 1 else f"{left} places left"


def confirm_note(username, reminder_later):
    """Under the slot on S-4. No reminder is promised when the slot is today or tomorrow:
    the confirmation email, sent straight away, is the reminder (PRD v1.2, UC-3)."""
    if reminder_later:
        return f"Signing up as {username}. We'll email you the details now, and a reminder the day before."
    return f"Signing up as {username}. We'll email you the details now."


def counter(count):
    return f"{count} of 500 characters"


# --- Emails (d05-01 Section 9, "Emails") ------------------------------------

def sign_in_email(username, minutes, link):
    return "Your BeautifulBeachPark sign-in link", (
        f"Hello {username},\n\n"
        f"Use this link to sign in to BeautifulBeachPark Volunteers. It works for {minutes} minutes:\n\n"
        f"{link}\n\n"
        "If you didn't ask for it, you can ignore this email.\n"
    )


def confirmation_email(username, title, day, when, description):
    return f"You're signed up: {title}, {day}, {when}", (
        f"Hello {username},\n\n"
        f"You're signed up for {title} on {day}, {when}.\n\n"
        + (f"{description}\n\n" if description else "")
        + "If you can't come, please cancel in the app so someone else can take your place.\n"
    )


def reminder_email(username, title, day, when, description):
    return f"Reminder: {title} tomorrow, {when}", (
        f"Hello {username},\n\n"
        f"This is a reminder that you're signed up for {title} tomorrow, {day}, {when}.\n\n"
        + (f"{description}\n\n" if description else "")
        + "If you can't come, please cancel in the app so someone else can take your place.\n"
    )


def message_email(username, coordinator, text):
    return "A message from a BeautifulBeachPark coordinator", (
        f"Hello {username},\n\n"
        f"{coordinator}, a BeautifulBeachPark coordinator, sent you this message:\n\n"
        f"{text}\n\n"
        "Please don't reply to this email; replies aren't read. "
        "To reach the coordinators, contact the park office.\n"
    )


# --- Screen text: headings, labels, buttons, hints (d05-01 Section 7 and the mockups) ---
# Pages take every word from here (Spec Section 10); T-WD-02 checks that the
# page templates hold no words of their own.

SCREEN = {
    # Every page
    "site_name": "BeautifulBeachPark Volunteers",
    "wordmark": "BeautifulBeachPark",
    "default_title": "Volunteers",
    "main_menu": "Main",
    "nav_open_slots": "Open slots",
    "nav_my_sign_ups": "My sign-ups",
    "nav_my_tasks": "My tasks",
    "nav_blocked": "Blocked volunteers",
    "home_link": "Go to the home page",
    # S-1 Sign In
    "sign_in_title": "Sign in",
    "sign_in_intro": "We'll email you a link to sign in. There's no password to remember.",
    "email_label": "Email",
    "send_link_button": "Send me a sign-in link",
    "new_here": "New here?",
    "create_account_link": "Create an account",
    "demo_notice_title": "Local demo.",
    "demo_notice": "Emails aren't really sent.",
    "open_pretend_inbox": "Open the pretend inbox",
    "demo_notice_end": "to find your sign-in link.",
    # S-2 Create Account
    "create_account_title": "Create an account",
    "username_label": "Username",
    "username_hint": "3 to 20 letters, numbers, or underscores. This is the only name others will see.",
    "privacy_title": "Your privacy.",
    "privacy_tick": "I've read this",
    "create_account_button": "Create account",
    "have_account": "Already have an account?",
    "sign_in_link": "Sign in",
    # S-3 Open Slots, S-4 Confirm, S-5 My Sign-Ups, cancel confirm
    "open_slots_title": "Open slots",
    "sign_up_button": "Sign up",
    "confirm_title": "Confirm sign-up",
    "confirm_button": "Confirm",
    "back_to_open_slots": "Back to open slots",
    "my_sign_ups_title": "My sign-ups",
    "cancel_button": "Cancel",
    "see_open_slots": "See the open slots",
    "cancel_title": "Cancel this sign-up?",
    "cancel_place_opens": "Your place will open for someone else.",
    "yes_cancel": "Yes, cancel",
    "keep_sign_up": "Keep my sign-up",
    # S-6 My Tasks, S-7 Post a Task
    "my_tasks_title": "My tasks",
    "post_task_button": "Post a task",
    "col_task": "Task",
    "col_slot": "Slot",
    "col_filled": "Places filled",
    "col_roster": "Roster",
    "roster_link": "Roster",
    "post_task_title": "Post a task",
    "title_label": "Title",
    "title_hint": "Up to 60 characters.",
    "description_label": "Description",
    "date_label": "Date",
    "slots_heading": "Slots",
    "slots_hint": "Each slot is one hour, with 1 to 20 volunteers. Up to 10 slots. Leave unused rows empty.",
    "ends_label": "Ends",
    "places_label": "Volunteers needed",
    "add_slot_button": "+ Add another slot",
    "post_button": "Post task",
    # S-8 Roster, S-9 Message, block confirm
    "roster_title": "Roster",
    "message_button": "Message",
    "block_button": "Block",
    "roster_privacy": "Usernames only. Volunteers' emails are never shown.",
    "back_to_my_tasks": "Back to my tasks",
    "message_title": "Message a volunteer",
    "message_label": "Message",
    "send_button": "Send",
    "back_to_roster": "Back to the roster",
    "block_title": "Block a volunteer",
    "yes_block": "Yes, block",
    "dont_block": "Don't block",
    # S-10 Blocked Volunteers
    "blocked_title": "Blocked volunteers",
    "blocked_hint": "Usernames only. Only you, the System Administrator, can undo a block.",
    "col_username": "Username",
    "col_blocked_by": "Blocked by",
    "col_date": "Date",
    "col_action": "Action",
    "account_deleted": "(account deleted)",
    "undo_block_button": "Undo block",
    "stays_blocked": "Stays blocked",
    # Pretend inbox (local demo only)
    "inbox_title": "Pretend inbox",
    "inbox_notice_title": "Local demo only.",
    "inbox_notice": ("This page shows the emails the app would have sent, newest first. It exists only "
                     "in the local environment, with made-up accounts, and is turned off on the live servers."),
    "inbox_empty": "No emails yet.",
}


def sign_out_link(username):
    return f"Sign out ({username})"


def page_title(title):
    return f"{title} · {SCREEN['site_name']}"


def sign_up_label(title, hours):
    return f"Sign up for {title}, {hours}"


def cancel_label(title, day, hours):
    return f"Cancel {title}, {day}, {hours}"


def roster_label(title, hours):
    return f"Roster for {title}, {hours}"


def message_label(username):
    return f"Message {username}"


def block_label(username):
    return f"Block {username}"


def undo_block_label(username):
    return f"Undo block for {username}"


def message_heading(username):
    return f"Message {username}"


def message_hint(username):
    return (f"{username} gets it by email from the park's no-reply address. "
            "Neither of you sees the other's email.")


def slot_start_label(number):
    return f"Slot {number} starts"


def places_filled(filled, places, full=False):
    return f"{filled} of {places}" + (" (Full)" if full else "")


def roster_summary(day, when, filled, places):
    return f"{day}, {when} · {filled} of {places} places filled"


def cancel_summary(title, day, when):
    return f"{title}, {day}, {when}. {SCREEN['cancel_place_opens']}"


def mail_header(to, subject):
    return f"To {to} · {subject}"
