# BeautifulBeachPark Volunteers: Maintenance Status Report, 2027-04-23

**Document:** d10-02 · **Step:** 10, Maintenance · **Period:** 2027-03-24 to 2027-04-23
· **For:** Park Manager, Volunteer Program Manager · **Status:** Approved
· **Prepared by:** SRE (Maintenance chat)

> **Sample document.** BeautifulBeachPark, its people, "SampleCloud," and
> "SampleMail" are made up, and every number is made up for illustration.
> This is the third monthly report, which is also the three-month
> success-measure check promised in d09-03.

## 1. Overall Health: Watch

The app is doing its job well, but it is close to three limits at once,
and the summer beach program will push it past them.

## 2. Reliability

| Measure | Target | This period | Last period | Trend |
|---|---|---|---|---|
| Available | 99% | 99.9% | 99.8% | Better |
| Slowest key page | Under 2 seconds | 3.1 seconds (Earth Day, M-3); 1.4 seconds otherwise | 1.5 seconds | Worse at peaks |
| Error pages | Under 1% | 0.02% | 0.03% | Same |
| Alerts reached | — | 0 | 1 (M-1 log entry) | Better |

## 3. Incidents This Period

| ID | What happened | Effect on users | Status |
|---|---|---|---|
| M-3 | Slow pages during the Earth Day Beach Cleanup sign-up rush | 210 volunteers waited up to 3 seconds per page for about 20 minutes; no sign-ups lost | Open: Recommendation 1 |

## 4. Rust Report: Updates and End-of-Support Dates

| Part | Status | Date | Action |
|---|---|---|---|
| SampleMail connection | End of support coming | 2027-06-30 | Move to version 3 by 2027-05-15 (U-4, in progress) |
| Python 3.11 | End of support coming | 2027-10-31 | Move to 3.13 in July (U-5) |
| PostgreSQL | Updated by SampleCloud to 16 | 2027-03-14 | None; tested first (U-3) |
| Claude Code | Updated to a newer model | 2027-03-02 | None; tests and prompts unchanged (U-2) |

## 5. Scale: Growth and Tipping Points

| Limit | Capacity | Highest this period | % used | Likely reached by |
|---|---|---|---|---|
| Database connections | 15 | 14 (Earth Day) | 93% | The first summer program sign-up day, 2027-06-01 |
| Volunteer accounts planned for | 500 (d06-01 assumption) | 468 | 94% | 2027-05 |
| Emails per month | 2,000 (SampleMail plan) | 1,780 | 89% | 2027-05 |

The park plans to announce the summer beach program on 2027-06-01 and
expects about 800 volunteers. At that size, all three limits are passed.

## 6. Costs

| Item | Amount | Source |
|---|---|---|
| Approved monthly limit | $60 | d06-03 |
| Spent this period | $44 | SampleCloud and SampleMail billing |
| Expected next period | $55, and over $60 in June without changes | Growth in emails and database use |

## 7. Success Measures

| Goal | Target | Result | On track? |
|---|---|---|---|
| Fill slots without email chains | 80% of slots filled through the app within 3 months | 84% | Yes |
| Save coordinators' time | Half of today's scheduling hours | 55% saved (coordinator survey, 9 of 11 replied) | Yes |
| Protect volunteers' privacy | Zero emails shown to others | Zero | Yes |

## 8. What People Said

- Coordinators: "Editing a posted task" is still the top request (R-2).
- Volunteers asked for text reminders, already planned for Phase 2.
- Two volunteers noticed the slow pages on Earth Day morning.

## 9. Recommendations

| # | Recommendation | Why | Who | Needed by |
|---|---|---|---|---|
| 1 | Prepare options for more database connections and a larger email plan, with a new Cost Sign-Off Sheet | Two limits at 89% to 93% (Section 5) | DevOps chat | 2027-05-15 |
| 2 | Finish the SampleMail version 3 move | Version 2 stops working 2027-06-30 | SDET and Software Engineer chats | 2027-05-15 |
| 3 | Start Phase 2 in Step 2: text reminders, task editing, and support for 1,000 volunteers | Phase 1 has met its goals, but the park's needs have grown past its design; see d10-03 | Product Manager, through Tracking | Decision by 2027-04-30 |

## 10. Product Fit: New Phase

Phase 1 has met every success measure, so it is doing what it was built
for. But it was designed for 500 volunteers and email only, and the park
now needs more. Phase 1 should keep running, with monthly maintenance, while
Phase 2 is planned. See d10-03.

## 11. Next Report

2027-05-24
