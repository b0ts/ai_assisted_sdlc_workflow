# BeautifulBeachPark Volunteers: Design Options Comparison

**Document:** d04-02 · **Step:** 4, Design · **Version:** 1.0
· **Last updated:** 2026-09-14 · **Status:** Decided
· **Owner:** Software Architect (Design chat)

> **Sample document.** BeautifulBeachPark and its people are made up, and
> **every cost and time is made up for illustration**.

## 1. The Decision

**Question:** Should BeautifulBeachPark Volunteers be a web app, an
app-store app, or both?

**Why it matters:** Everything else in the Spec, and the costs in Step 6,
depend on this choice. Switching later would mean rebuilding the screens.

**PRD source:** d03-01 v1.0: Users (volunteers of all ages, mostly on
phones), Quality Requirements (current phone and desktop browsers), and
Constraints (small budget, no IT staff).

## 2. The Options

| Option | Plain-language description |
|---|---|
| A: Web app | Volunteers and coordinators open a web address in any browser, on a phone or a computer. Nothing to install. |
| B: App-store app | Volunteers download an app from Apple's App Store or Google Play. Coordinators would still need a web page or their own copy of the app. |
| C: Both | A web app first, with an app-store app added later. |

## 3. Side-by-Side Comparison

| Measure | Option A: Web app | Option B: App-store app | Option C: Both |
|---|---|---|---|
| Fits the users (PRD Section 3) | Yes: works for every age and device | Partly: some volunteers won't install an app for one-hour tasks | Yes |
| Covers the Must-have use cases | All of UC-1 to UC-7 | All, but coordinators need a second version | All |
| Getting started for users | Tap a link on the park website | Find, download, and install | Either |
| Devices it works on | Any current phone or computer browser | iPhone and Android only, as two versions | All |
| Works offline | No; slots must be checked live anyway | Partly | Partly |
| Access to phone features (GPS, camera, alerts) | Limited; not needed by any use case | Full | Full, in the app |
| How updates reach users | Instantly, for everyone | After app-store review; users must update | Both ways |
| Estimated cost to build | About 8 weeks part-time (d02-01) | About twice Option A: two versions plus coordinator screens | Option A now, plus Option B later |
| Estimated cost to run and maintain | Under $60 a month for hosting (d02-01) | Hosting, plus yearly app-store fees, plus two versions to update | Highest |
| Time to first release | Before 2027-03-01 | Likely after 2027-03-01 | Web app before 2027-03-01 |
| Security and privacy | Emails stay on the server | Same, but more places to keep updated | Same as B |
| Fits the constraints (PRD Section 7) | Yes | No: costs and maintenance too high with no IT staff | Not in Phase 1 |

## 4. Recommendation

**Recommended option:** A: Web app

**Why:** Volunteers of all ages, mostly on phones, can sign up from a link
on the park website with nothing to install. No use case needs offline use
or phone features, and one version keeps the cost within the small budget
and the work within reach of a park with no IT staff.

**What we give up:** Phone notifications. Reminders come by email instead,
which some volunteers may miss.

**What would change the recommendation:** If a later phase needs offline
use or phone alerts, Option C (adding an app later) would be worth a new
look.

## 5. Open Questions

- None

## 6. Decision

| Chosen option | Decided by | Date | Spec Design Decision ID |
|---|---|---|---|
| A: Web app | Park Manager | 2026-09-14 | DD-1 |
