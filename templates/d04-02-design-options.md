# [Project name]: Design Options Comparison

<!-- Template d04-02. Use this when there is a real choice to make about
the type of application or its overall design, such as web app vs.
app-store app, or building a feature vs. using an outside service. Compare
the options side by side so the stakeholders can see the trade-offs.
Replace every [placeholder]. Delete all hint comments like this one. Keep
every heading, in this order. The chosen option is copied into Section 3
and the Design Decisions table of the Spec (d04-01). -->

**Document:** d04-02 · **Step:** 4, Design · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting decision / Decided]
· **Owner:** Software Architect (Design chat)

## 1. The Decision

**Question:** [One sentence, e.g., "Should the product be a web app, an
app-store app, or both?"]

**Why it matters:** [One or two sentences: what depends on this choice, and
why it is hard to change later.]

**PRD source:** [d03-01, version, and the sections that drive this choice,
e.g., Users, Quality Requirements, Constraints]

## 2. The Options

<!-- Two to four options. Describe each in plain language, for someone
who is not technical. -->

| Option | Plain-language description |
|---|---|
| A: [e.g., Web app] | [e.g., Visitors open a web address in their phone's browser. Nothing to install.] |
| B: [e.g., App-store app] | [e.g., Visitors download an app from Apple's App Store or Google Play.] |
| C: [e.g., Both] | [e.g., A web app first, with an app-store app added later.] |

## 3. Side-by-Side Comparison

<!-- Keep the rows that matter for this project, and add others that do.
Mark each cell with a short phrase, not a score. -->

| Measure | Option A | Option B | Option C |
|---|---|---|---|
| Fits the users (PRD Section 3) | [ ] | [ ] | [ ] |
| Covers the Must-have use cases | [ ] | [ ] | [ ] |
| Getting started for users | [ ] | [ ] | [ ] |
| Devices it works on | [ ] | [ ] | [ ] |
| Works offline | [ ] | [ ] | [ ] |
| Access to phone features (GPS, camera, alerts) | [ ] | [ ] | [ ] |
| How updates reach users | [ ] | [ ] | [ ] |
| Estimated cost to build | [Estimate] | [Estimate] | [Estimate] |
| Estimated cost to run and maintain | [Estimate] | [Estimate] | [Estimate] |
| Time to first release | [Estimate] | [Estimate] | [Estimate] |
| Security and privacy | [ ] | [ ] | [ ] |
| Fits the constraints (PRD Section 7) | [ ] | [ ] | [ ] |

<!-- Label every cost and time as an estimate. Never invent numbers; write
"TBD" and list it under Open Questions. -->

## 4. Recommendation

**Recommended option:** [Letter and name]

**Why:** [Two or three sentences linking the recommendation to specific
users, use cases, quality requirements, and constraints.]

**What we give up:** [The main drawback of the recommended option, stated
honestly.]

**What would change the recommendation:** [e.g., "If offline use becomes a
Must-have, Option B would be better."]

## 5. Open Questions

<!-- Write "None" if empty. -->

- [Question, and who can answer it]

## 6. Decision

<!-- Filled in after the stakeholders decide. The Architect recommends;
the stakeholders decide. -->

| Chosen option | Decided by | Date | Spec Design Decision ID |
|---|---|---|---|
| [Option] | [Name or group] | [YYYY-MM-DD] | [e.g., DD-1] |
