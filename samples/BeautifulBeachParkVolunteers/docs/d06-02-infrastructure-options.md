# BeautifulBeachPark Volunteers: Infrastructure Options and Cost Analysis

**Document:** d06-02 · **Step:** 6, Initial Infrastructure · **Version:** 1.0
· **Last updated:** 2026-10-05 · **Status:** Decided
· **Owner:** DevOps Engineer (Initial Infrastructure chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up, and **every price is made up for
> illustration**. A real project checks current prices with each
> provider's own price calculator.

## 1. The Decision

**Question:** Where should the volunteer app's application server,
reminder job, and database run, and who should look after them?

**Why it matters:** This sets the monthly bill, and who gets the call when
something breaks. Moving to a different setup later means copying all the
accounts, sign-ups, and the block list.

**What is needed:** an application server (a Python web service), a daily
reminder job, a PostgreSQL database with nightly backups, and an
email-sending service (d06-01 Section 3), in a test and a production
environment.

**Sources:** d03-01 v1.1 (Constraints: small budget, no IT staff, up to
500 volunteers; Quality: 99% available, under 2 seconds on a phone),
d04-01 v1.1 (Components, Section 10 Reliability, Section 11 Security &
Compliance), d05-01 v1.0 (10 simple text screens, no uploaded photos),
d02-01 v1.0 (hosting estimated at under $60 a month).

## 2. The Options

All three options use the same email-sending service (SampleMail), because
the Spec leaves that choice to Step 6 and every option needs one.

| Option | Plain-language description |
|---|---|
| A: Cloud, managed services | We rent space from SampleCloud, which also restarts the app if it stops, installs updates, and makes backups. |
| B: Cloud, self-managed | We rent a small computer from SampleCloud, and a volunteer installs and updates everything. |
| C: On-premises | The park buys a small server and keeps it in the park office. |

## 3. Side-by-Side Comparison

| Measure | Option A | Option B | Option C |
|---|---|---|---|
| Fits the expected users (up to 500) | Easily | Easily | Yes |
| Meets 99% availability (PRD Section 6) | Provider restarts the app and fixes problems at any hour | Depends on a volunteer being free | Depends on office power and internet |
| Meets Security & Compliance (Spec Section 11) | Encryption, HTTPS, and backups built in | Possible, but we must set it up | Possible, but we must set it up |
| Where the data lives | SampleCloud, US region | SampleCloud, US region | Park office |
| Time to get started | Hours | A few days | Weeks (order and install) |
| Maintenance | Provider | A volunteer, about 4 hours a month | A volunteer, about 6 hours a month |
| Skills our team would need | Very few | Server administration | Server administration and hardware |

## 4. Cost Analysis

| Cost | Option A | Option B | Option C |
|---|---|---|---|
| Up-front | $0 | $0 | $1,500 |
| Per month | $40 ($35 hosting, $5 email) | $25 ($20 hosting, $5 email) | $25 ($20 power and internet, $5 email) |
| Volunteer time per month | About 1 hour | About 4 hours | About 6 hours |
| First-year total | $480 | $300 | $1,800 |
| Three-year total | $1,440 | $900 | $2,400 |

**Prices checked:** 2026-10-05, made up for this sample.

**Based on:** up to 500 volunteers, under 2 GB of data, and about 2,000
emails a month (sign-in links, reminders, and coordinator messages).

## 5. Recommendation

**Recommended option:** A: Cloud, managed services

**Why:** The park has no IT staff (PRD Section 7), and the PRD's 99%
availability can't wait for a volunteer to be free. Option A includes the
restarts, encryption, and nightly backups the Spec asks for (Sections 10
and 11) with the least work, and stays under the $60 a month estimated in
Feasibility.

**What we give up:** About $15 a month more than Option B.

**What would change the recommendation:** A skilled volunteer who commits
to regular maintenance would make Option B worth reconsidering.

## 6. Open Questions

- None

## 7. Decision

| Chosen option | Decided by | Date | Infrastructure Decision ID |
|---|---|---|---|
| A: Cloud, managed services | Park Manager | 2026-10-06 | INF-1 |
