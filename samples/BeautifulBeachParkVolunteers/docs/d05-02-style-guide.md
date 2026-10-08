# BeautifulBeachPark Volunteers: Style Guide

**Document:** d05-02 · **Step:** 5, User Experience · **Version:** 1.0
· **Last updated:** 2026-09-29 · **Status:** Approved
· **Owner:** UI/UX Designer (User Experience chat)

> **Sample document.** BeautifulBeachPark, its website, and its people are
> made up. The colors and contrast ratios are real and were measured.

## 1. Style Source

| Item | Details |
|---|---|
| Existing website | BeautifulBeachPark's pretend website, `www.beautifulbeachpark.example` (made up for the sample) |
| Screenshots or brand files | Home page and events page screenshots, provided by the Volunteer Program Manager |
| Logo | Text wordmark "BeautifulBeachPark" with a wave line under it; no separate logo files in Phase 1 |
| Permission to use | Owned by the park; confirmed by the Park Manager, 2026-09-26 |
| Overall feel | Calm, sunny, friendly, clear |

## 2. Colors

The website's turquoise (#3FB8C9) has a contrast of only 2.4 to 1 with
white text, which fails WCAG 2.1 AA. It is kept for decoration only, and
buttons use the darker Ocean instead.

| Name | Hex code | Used for | Text on it | Contrast ratio |
|---|---|---|---|---|
| Ocean | #0B5E7A | Main buttons, links, header bar | White #FFFFFF | 7.3 to 1 |
| Sand | #F7F1E3 | Page background | Driftwood #2B2B2B | 12.6 to 1 |
| White | #FFFFFF | Cards and forms | Driftwood #2B2B2B | 14.2 to 1 |
| Pebble | #5F6B73 | Secondary text, such as "2 places left" and "Full" | On White | 5.5 to 1 |
| Foam | #E3F2F7 | Information banners | Driftwood #2B2B2B | 12.3 to 1 |
| Seagrass | #2E7D4F | Success banner, such as "You're signed up!" | White #FFFFFF | 5.0 to 1 |
| Coral | #B3261E | Error banners; the Block button | White #FFFFFF | 6.5 to 1 |
| Turquoise | #3FB8C9 | Wave line under the wordmark only; never behind text | — | Decoration only |

## 3. Typography

| Use | Font | Fallback | Size | Weight |
|---|---|---|---|---|
| Page title | Nunito | "Segoe UI", Arial, sans-serif | 28 px | Bold |
| Section heading | Nunito | "Segoe UI", Arial, sans-serif | 20 px | Bold |
| Body text | Nunito | "Segoe UI", Arial, sans-serif | 18 px, never smaller than 16 px | Regular |
| Small print | Nunito | "Segoe UI", Arial, sans-serif | 16 px | Regular |

**Font license:** Nunito is free for web and app use under the SIL Open
Font License.

## 4. Spacing and Layout

| Item | Value |
|---|---|
| Spacing scale | 4, 8, 16, 24, 32 px |
| Page margins | 16 px on phones, 32 px on desktops |
| Maximum content width | 720 px |
| Screen sizes designed for | Phone 375 px wide first; desktop 1280 px wide |
| Corner rounding | 8 px on buttons, cards, and fields |

## 5. Components

| Component | Look | States |
|---|---|---|
| Main button | Ocean background, white bold text, 48 px tall, full width on phones | Normal, pressed (darker), disabled (Pebble, with the reason written below), loading ("Working…") |
| Secondary button | White background, Ocean border and text, 48 px tall | Normal, pressed, disabled |
| Danger button | Coral background, white text; always followed by a confirm step | Normal, pressed, disabled |
| Text field | White, 1 px Pebble border, label above, 48 px tall | Empty, typing (Ocean border), error (Coral border and message below), disabled |
| Card | White, 8 px corners, soft shadow; one task or slot per card | Normal, full (Pebble text "Full", no button) |
| Message banner | Full-width strip with a written word first: "Done:", "Problem:", or "Note:" | Success (Seagrass), error (Coral), information (Foam) |
| Navigation | Ocean header with the wordmark; volunteers: "Open slots" and "My sign-ups"; coordinators: "My tasks" | Current page underlined |

## 6. Icons and Images

| Item | Source | License or permission | Notes |
|---|---|---|---|
| Icons | None in Phase 1 | — | Text labels only, so every action is spelled out |
| Task photos | The park's own photos | Owned by the park | Shown as gray boxes in mockups; each needs a text description |
| AI-generated images | Not used | — | The Park Manager asked for real park photos only |

## 7. Voice and Tone

- **Voice:** Warm and plain, like a friendly volunteer leader.
- **Do:** Use short sentences; say "you"; thank people; say what to do
  next.
- **Don't:** Use technical words, or blame the person in an error.
- **Example:** "Thanks for helping! You're signed up for Beach Cleanup,
  Saturday 9 to 10."

## 8. Design Tokens

Saved as [`assets/design-tokens.json`](../assets/design-tokens.json) and
listed in Section 12 of the UI/UX Document.

```json
{
  "color": {
    "primary": "#0B5E7A",
    "background": "#F7F1E3",
    "surface": "#FFFFFF",
    "text": "#2B2B2B",
    "textSecondary": "#5F6B73",
    "info": "#E3F2F7",
    "success": "#2E7D4F",
    "error": "#B3261E",
    "decoration": "#3FB8C9"
  },
  "font": {
    "heading": "Nunito, \"Segoe UI\", Arial, sans-serif",
    "body": "Nunito, \"Segoe UI\", Arial, sans-serif"
  },
  "space": [4, 8, 16, 24, 32],
  "radius": 8
}
```

## 9. Change Log

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | 2026-09-29 | First version | — | Park Manager (D7, 2026-09-30) |
