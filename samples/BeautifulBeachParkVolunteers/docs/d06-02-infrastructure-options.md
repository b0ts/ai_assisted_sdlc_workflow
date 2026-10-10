# BeautifulBeachPark Volunteers: Infrastructure Options and Cost Analysis

**Document:** d06-02 · **Step:** 6, Initial Infrastructure · **Version:** 1.0
· **Last updated:** 2026-10-05 · **Status:** Decided
· **Owner:** DevOps Engineer (Initial Infrastructure chat)

> **Sample document.** BeautifulBeachPark, its city, its people, and Parks
> IT are made up, and **every price is made up for illustration**. A real
> project checks current prices with each provider's own price calculator,
> and the rules with the people who run its servers.

## 1. The Decision

**Question:** Where should the volunteer app go live (its application
server, reminder job, database, and email), and who should look after it?

**Why it matters:** This sets the monthly bill, who gets the call when
something breaks, and the rules the code must follow. Moving to a
different setup later means copying all the accounts, sign-ups, and the
block list.

**What is needed:** an application server (a Python web service), a daily
reminder job, a PostgreSQL database with nightly backups, and a way to
send email (d06-01 Section 3). Building, testing, and the stakeholder demo
happen first on a local environment, which is free in every option.

**Sources:** d03-01 v1.1 (Constraints: small budget, no IT staff of the
park's own, up to 500 volunteers; Quality: 99% available, under 2 seconds
on a phone), d04-01 v1.1 (Components, Section 10 Reliability, Section 11
Security & Compliance), d05-01 v1.0 (10 simple text screens, no uploaded
photos), d02-01 v1.0 (hosting estimated at under $60 a month); answers
from Parks IT, 2026-10-03.

## 2. The Options

BeautifulBeachPark belongs to the city parks department. Its IT team,
**Parks IT**, already runs web and database servers in the cloud for the
department's other websites, and the city's email service.

| Option | Plain-language description |
|---|---|
| A: The city's existing servers | The app goes on the servers Parks IT already runs, following their rules. Parks IT installs it, backs it up, and watches it. |
| B: New managed cloud hosting | The park rents its own space from a cloud hosting company, which also restarts the app, installs updates, and makes backups. |
| C: A spare computer in the park office | An unused office computer runs the app, and a volunteer looks after it. |

## 3. Side-by-Side Comparison

| Measure | Option A | Option B | Option C |
|---|---|---|---|
| Fits the expected users (up to 500) | Easily | Easily | Yes |
| Meets 99% availability (PRD Section 6) | Parks IT watches the servers at all hours | Hosting company restarts the app and fixes problems | Depends on office power, internet, and a volunteer |
| Meets Security & Compliance (Spec Section 11) | Encryption, HTTPS, and backups already in place | Built in, but we set it up | Possible, but we must set it up |
| Where the data lives | City's cloud servers, US region | Hosting company, US region | Park office |
| Time to get started | About 2 weeks, for Parks IT's security review | Hours | A few days |
| Maintenance | Parks IT | Hosting company, plus about 1 hour a month from us | A volunteer, about 4 hours a month |
| Skills our team would need | Very few | A little | Server administration |
| Reuses what we already have | Yes: servers, backups, email, and staff | No | The computer only |
| Approval needed from others | Parks IT's security review before going live | None | None |
| Rules we must follow | Parks IT's (d06-01 Section 5.1) | The hosting company's | Our own |

## 4. Cost Analysis

| Cost | Option A | Option B | Option C |
|---|---|---|---|
| Up-front | $0 | $0 | $0 (the computer is already owned) |
| Per month | $0 (servers and email already paid for by Parks IT) | $15 ($12 hosting, $3 email) | $5 (power) |
| Staff or volunteer time per month | About 1 hour from Parks IT | About 1 hour | About 4 hours |
| First-year total | $0 | $180 | $60 |
| Three-year total | $0 | $540 | $180, plus a replacement computer |

The local environment, on the Volunteer Program Manager's laptop, is free
in every option.

**Prices checked:** 2026-10-05: Option A with Parks IT; Options B and C
made up for this sample.

**Based on:** up to 500 volunteers, under 2 GB of data, and about 2,000
emails a month (sign-in links, reminders, and coordinator messages).

## 5. Recommendation

**Recommended option:** A: The city's existing servers

**Why:** The park has no IT staff of its own (PRD Section 7), and the
PRD's 99% availability needs someone watching the servers at all hours.
Parks IT already does that for the department's other websites, with the
encryption, nightly backups, and HTTPS the Spec asks for (Sections 10 and
11), at no new cost.

**What we give up:** Speed and freedom. The app must fit Parks IT's rules,
and their security review takes about two weeks before going live, so it
must be booked early in Step 9.

**What would change the recommendation:** If Parks IT couldn't take the
app, or started charging more than about $15 a month, Option B would be
worth reconsidering.

## 6. Open Questions

- None

## 7. Decision

| Chosen option | Decided by | Date | Infrastructure Decision ID |
|---|---|---|---|
| A: The city's existing servers | Park Manager | 2026-10-06 | INF-1 |
