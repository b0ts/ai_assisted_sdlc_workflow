# [Project name]: Infrastructure Options and Cost Analysis

<!-- Template d06-02. Use this to compare the different ways to provide
the infrastructure, such as cloud vs. on-premises, or managed vs.
self-managed, and what each will cost. Compare the options side by side so
the stakeholders can see the trade-offs. Replace every [placeholder].
Delete all hint comments like this one. Keep every heading, in this order.
The chosen option is copied into Sections 1 and 5 of the System
Infrastructure Document (d06-01), and its costs are carried into the Cost
Sign-Off Sheet (d06-03). -->

**Document:** d06-02 · **Step:** 6, Initial Infrastructure · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting decision / Decided]
· **Owner:** DevOps Engineer (Initial Infrastructure chat)

## 1. The Decision

**Question:** [One sentence, e.g., "Where should the web server,
application server, and database run, and who should look after them?"]

**Why it matters:** [One or two sentences: what depends on this choice,
what it costs each month, and why it is hard to change later.]

**What is needed:** [The pieces from d06-01 Section 3, e.g., "a web
server, an application server, a database, and nightly backups."]

**Sources:** [d03-01, d04-01, and d05-01 versions, and the sections that
drive this choice, e.g., PRD Users and Constraints, Spec Security &
Compliance]

## 2. The Options

<!-- Two to four options. Describe each in plain language, for someone
who is not technical. Common choices: cloud with managed services (the
provider does the maintenance), cloud with self-managed servers, on-premises
(computers the organization owns, in its own building), or hybrid (some of
each). -->

| Option | Plain-language description |
|---|---|
| A: [e.g., Cloud, managed services] | [e.g., We rent space from a cloud provider, which also installs updates and makes backups.] |
| B: [e.g., Cloud, self-managed] | [e.g., We rent computers from a cloud provider but look after them ourselves.] |
| C: [e.g., On-premises] | [e.g., We buy a server and keep it in the office.] |

## 3. Side-by-Side Comparison

<!-- Keep the rows that matter for this project, and add others that do.
Mark each cell with a short phrase, not a score. -->

| Measure | Option A | Option B | Option C |
|---|---|---|---|
| Fits the expected users (PRD Section 3) | [ ] | [ ] | [ ] |
| Meets speed and reliability (PRD Section 6) | [ ] | [ ] | [ ] |
| Meets Security & Compliance (Spec Section 11) | [ ] | [ ] | [ ] |
| Where the data lives | [ ] | [ ] | [ ] |
| Time to get started | [ ] | [ ] | [ ] |
| Growing as users increase | [ ] | [ ] | [ ] |
| Maintenance: who installs updates and fixes problems | [ ] | [ ] | [ ] |
| Skills our team would need | [ ] | [ ] | [ ] |
| Reuses what we already have | [ ] | [ ] | [ ] |
| Fits the constraints (PRD Section 7) | [ ] | [ ] | [ ] |

## 4. Cost Analysis

<!-- Label every number as an estimate. Never invent prices: use the
providers' own price calculators or quotes, and record when you checked.
AI price knowledge can be out of date. If a price is unknown, write "TBD"
and list it under Open Questions. Staff time counts as a cost even when it
is volunteer time. -->

| Cost | Option A | Option B | Option C |
|---|---|---|---|
| Up-front (equipment, setup, licenses) | [$ estimate] | [$ estimate] | [$ estimate] |
| Per month (bills, power, internet) | [$ estimate] | [$ estimate] | [$ estimate] |
| Staff or volunteer time per month | [Hours] | [Hours] | [Hours] |
| First-year total | [$ estimate] | [$ estimate] | [$ estimate] |
| Three-year total | [$ estimate] | [$ estimate] | [$ estimate] |

**Prices checked:** [YYYY-MM-DD, and the source for each option, e.g.,
"Provider's price calculator," "Quote from vendor"]

**Based on:** [The assumptions behind the numbers, e.g., "up to 500
users, 2 GB of data, photos under 200 KB each."]

## 5. Recommendation

**Recommended option:** [Letter and name]

**Why:** [Two or three sentences linking the recommendation to specific
users, quality requirements, Security & Compliance items, and the
budget.]

**What we give up:** [The main drawback of the recommended option, stated
honestly.]

**What would change the recommendation:** [e.g., "If a law required the
data to stay in our own building, Option C would be required."]

## 6. Open Questions

<!-- Write "None" if empty. -->

- [Question, and who can answer it]

## 7. Decision

<!-- Filled in after the stakeholders decide. The DevOps Engineer
recommends; the stakeholders decide. The chosen option's costs then go on
the Cost Sign-Off Sheet (d06-03). -->

| Chosen option | Decided by | Date | Infrastructure Decision ID |
|---|---|---|---|
| [Option] | [Name or group] | [YYYY-MM-DD] | [e.g., INF-1] |
