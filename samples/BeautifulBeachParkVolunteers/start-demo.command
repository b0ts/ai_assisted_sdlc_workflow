#!/bin/bash
# Starts the app on this Mac for the hands-on review (round 3) and the stakeholder demo:
# made-up data, and a pretend inbox instead of real email. Double-click this file in Finder.
# Leave the window open while you test; close it to stop the app.
cd "$(dirname "$0")" || exit 1
if [ ! -x .venv/bin/python ]; then
  echo "The project's Python isn't set up yet. Follow the setup lines in README.md first"
  echo "(they start with: python3 -m venv .venv)."
  read -r -p "Press Return to close." _; exit 1
fi
. .venv/bin/activate
cd src || exit 1
[ -f .env ] || python infrastructure/setup_local.py
if [ ! -f bbpv-local.db ]; then
  flask --app bbpv seed-demo || { read -r -p "Setting up the demo data failed. Press Return to close." _; exit 1; }
fi
# Port 5050, not Flask's usual 5000: on a Mac, 5000 belongs to AirPlay Receiver, which
# answers "Access denied" instead of the app. The sign-in links use the same address.
export BASE_URL="http://127.0.0.1:5050"
echo
echo "Starting the app. Your browser will open $BASE_URL in a few seconds."
echo "To stop the app, close this window."
echo
( sleep 3; open "$BASE_URL" ) &
flask --app bbpv run --host 127.0.0.1 --port 5050
