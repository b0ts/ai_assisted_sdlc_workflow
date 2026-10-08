# [Project name]: Maintenance Status Report, [YYYY-MM-DD]

<!-- Template d10-02. Save each report as
d10-02-maintenance-status-report-YYYY-MM-DD.md (the sample keeps one file).
Replace every [placeholder]. Delete all hint comments. Keep every heading,
in this order. Aim for two pages or fewer, in plain language, for
stakeholders who may not be technical.
The SRE writes this report on the rhythm set in d10-01 Section 1 (monthly
is typical), from the Maintenance Log, the logs, the dashboards, and the
alerts. It ends with a Product Fit verdict. If the verdict is "New phase"
or "Sunset," also write d10-03. Never write real users' personal
information here; use counts. -->

**Document:** d10-02 · **Step:** 10, Maintenance · **Period:** [YYYY-MM-DD] to [YYYY-MM-DD]
· **For:** [Audience] · **Status:** [Draft / Awaiting sign-off / Approved]
· **Prepared by:** SRE (Maintenance chat)

## 1. Overall Health: [Healthy / Watch / Action needed]

[One or two sentences explaining why.]

## 2. Reliability

<!-- Compare each measure with its target (d03-01, d04-01, d06-01). -->

| Measure | Target | This period | Last period | Trend |
|---|---|---|---|---|
| Available | [e.g., 99%] | [%] | [%] | [Better / Same / Worse] |
| Slowest key page | [e.g., under 2 seconds] | [Seconds] | [Seconds] | [Trend] |
| Error pages | [e.g., under 1%] | [%] | [%] | [Trend] |
| Alerts reached | — | [Number] | [Number] | [Trend] |

## 3. Incidents This Period

<!-- From d10-01 Section 4. Write "None." if empty. -->

| ID | What happened | Effect on users | Status |
|---|---|---|---|
| [M-1] | [Summary] | [Who, how many, how long] | [Fixed / Open] |

## 4. Rust Report: Updates and End-of-Support Dates

<!-- From d10-01 Sections 2 and 3: what was updated, what is waiting, and
every part reaching end of support in the next 12 months. -->

| Part | Status | Date | Action |
|---|---|---|---|
| [Part] | [Updated / Update waiting / End of support coming] | [YYYY-MM-DD] | [Action] |

## 5. Scale: Growth and Tipping Points

<!-- Compare usage with each known limit. Flag any limit above 70% of its
capacity, and say when it is likely to be reached. -->

| Limit | Capacity | Highest this period | % used | Likely reached by |
|---|---|---|---|---|
| [e.g., Database connections] | [Number] | [Number] | [%] | [YYYY-MM-DD / Not soon] |

## 6. Costs

| Item | Amount | Source |
|---|---|---|
| Approved monthly limit | [$] | d06-03 |
| Spent this period | [$] | [Provider billing] |
| Expected next period | [$] | [Reason] |

## 7. Success Measures

<!-- From the PRD (d03-01 Section 2). Is the product still doing the job it
was built for? -->

| Goal | Target | Result | On track? |
|---|---|---|---|
| [Goal] | [Target] | [Result] | [Yes / Too early / No] |

## 8. What People Said

<!-- Summarized, with no personal details. -->

- [Feedback]

## 9. Recommendations

<!-- Most important first. Each one says who would do it. The SRE
recommends; the stakeholders decide in the Tracking chat. -->

| # | Recommendation | Why | Who | Needed by |
|---|---|---|---|---|
| 1 | [Recommendation] | [Evidence] | [Chat or role] | [YYYY-MM-DD] |

## 10. Product Fit: [Keep running / New phase / Sunset]

[Two or three sentences: does the product still serve the need it was
built for? If "New phase" or "Sunset," see d10-03.]

## 11. Next Report

[YYYY-MM-DD]
