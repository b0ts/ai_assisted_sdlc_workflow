# [Project name]: Timeline

<!-- Template d01-02, for large or phased projects. Replace every
[placeholder] and the sample dates and durations. Delete all hint comments.
Keep every heading, in this order. -->

**Document:** d01-02 · **Step:** 1, Tracking · **Last updated:** [YYYY-MM-DD]

Dates marked "estimate" may change. The [Tracking Checklist](d01-01-checklist.md)
is the source of truth for status and decisions.

## Timeline

<!-- Tracking spans the whole project. Steps 2 to 10 run in order.
Mark finished steps "done," and the current step "active."
For phased projects, add one section per phase (e.g., "section Phase 2")
and repeat the steps that phase needs. -->

```mermaid
gantt
    title [Project name] timeline
    dateFormat YYYY-MM-DD
    axisFormat %b %d
    section Tracking
    1 Tracking (ongoing)     :t1, 2026-01-05, 2026-03-31
    section Phase 1
    2 Feasibility            :s2, 2026-01-05, 5d
    3 Requirements           :s3, after s2, 7d
    4 Design                 :s4, after s3, 7d
    5 User Experience        :s5, after s4, 5d
    6 Infrastructure         :s6, after s5, 5d
    7 Test Creation          :s7, after s6, 7d
    8 Implementation         :s8, after s7, 14d
    9 Release                :s9, after s8, 3d
    10 Upkeep (ongoing)      :s10, after s9, 2026-03-31
```

## Key Dates

| Milestone | Date | Firm or estimate |
|---|---|---|
| [e.g., Feasibility sign-off] | [YYYY-MM-DD] | [Estimate] |
