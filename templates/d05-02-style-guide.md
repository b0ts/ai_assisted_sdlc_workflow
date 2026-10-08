# [Project name]: Style Guide

<!-- Template d05-02. Replace every [placeholder]. Delete all hint comments
like this one. Keep every heading, in this order.
The Style Guide records the look of the product: colors, fonts, spacing,
reusable parts (components), images, and the voice of its wording. It is
written so that exact values can be copied straight into code or a design
tool, and it is usually matched to the organization's existing website.
The screens themselves go in the UI/UX Document (d05-01). -->

**Document:** d05-02 · **Step:** 5, User Experience · **Version:** [1.0]
· **Last updated:** [YYYY-MM-DD] · **Status:** [Draft / Awaiting sign-off / Approved / Sent back]
· **Owner:** UI/UX Designer (User Experience chat)

## 1. Style Source

<!-- Where the look comes from. Use only brand material the organization
owns or has permission to use. Never copy another organization's logo,
images, or distinctive design. -->

| Item | Details |
|---|---|
| Existing website | [Web address, or "none"] |
| Screenshots or brand files | [File names, and who provided them] |
| Logo | [File name and the versions available, e.g., color and white] |
| Permission to use | [e.g., "Owned by the organization; confirmed by [Name]"] |
| Overall feel | [Three or four words, e.g., "Calm, sunny, friendly, clear"] |

## 2. Colors

<!-- Use exact hex codes. Check every text color against the background it
sits on: WCAG 2.1 AA needs a contrast of at least 4.5 to 1 for normal text
and 3 to 1 for large text. Write the measured ratio, not "passes." -->

| Name | Hex code | Used for | Text on it | Contrast ratio |
|---|---|---|---|---|
| [e.g., Ocean] | [e.g., #0B5E7A] | [e.g., Main buttons, links, header] | [e.g., White #FFFFFF] | [e.g., 7.3 to 1] |
| [e.g., Sand] | [#______] | [e.g., Page background] | [e.g., Dark text #1F2933] | [ ] |
| [e.g., Success] | [#______] | [e.g., "You're signed up" message] | [ ] | [ ] |
| [e.g., Error] | [#______] | [e.g., Error messages] | [ ] | [ ] |

## 3. Typography

<!-- Fonts and sizes. Always give a fallback, in case the font can't load.
Check the font's license allows use on the web or in an app. -->

| Use | Font | Fallback | Size | Weight |
|---|---|---|---|---|
| Page title | [e.g., Nunito] | [e.g., Arial, sans-serif] | [e.g., 28 px] | [e.g., Bold] |
| Section heading | [ ] | [ ] | [ ] | [ ] |
| Body text | [ ] | [ ] | [e.g., 16 px, never smaller] | [e.g., Regular] |
| Small print | [ ] | [ ] | [ ] | [ ] |

**Font license:** [e.g., "Free for web and app use (SIL Open Font License)"]

## 4. Spacing and Layout

| Item | Value |
|---|---|
| Spacing scale | [e.g., 4, 8, 16, 24, 32 px] |
| Page margins | [e.g., 16 px on phones, 32 px on desktops] |
| Maximum content width | [e.g., 720 px] |
| Screen sizes designed for | [e.g., Phone 375 px wide; desktop 1280 px wide] |
| Corner rounding | [e.g., 8 px on buttons and cards] |

## 5. Components

<!-- The reusable parts every screen is built from. Describe each one's
look and every state it can be in. Keep only the rows this product uses,
and add any it needs. -->

| Component | Look | States |
|---|---|---|
| Main button | [e.g., Ocean background, white bold text, 48 px tall, full width on phones] | [Normal, pressed, disabled, loading] |
| Secondary button | [ ] | [ ] |
| Text field | [ ] | [Empty, typing, error, disabled] |
| Card | [e.g., One task or slot, white, soft shadow] | [ ] |
| List | [ ] | [ ] |
| Message banner | [e.g., Success, error, or information] | [ ] |
| Navigation | [e.g., Bar across the bottom on phones] | [ ] |

## 6. Icons and Images

<!-- Every icon set and image, with its source and license. Images made by
AI tools must be listed too, and checked by a person before use. -->

| Item | Source | License or permission | Notes |
|---|---|---|---|
| [e.g., Icons] | [e.g., An open-source icon set] | [e.g., Free to use, credit not required] | [ ] |
| [e.g., Beach photo] | [e.g., The organization's own photo] | [e.g., Owned] | [e.g., Always include a text description] |

## 7. Voice and Tone

<!-- How the product talks to people. The wording in Section 9 of the
UI/UX Document follows these rules. -->

- **Voice:** [e.g., Warm and plain, like a friendly volunteer leader]
- **Do:** [e.g., Use short sentences; say "you"; thank people]
- **Don't:** [e.g., Use technical words or blame the user in errors]
- **Example:** [e.g., "Thanks for helping! You're signed up for Beach
  Cleanup, Saturday 9 to 10."]

## 8. Design Tokens

<!-- Optional. The same values as Sections 2 to 4, written so software can
read them. The Software Engineer can import this file instead of copying
values by hand. If used, save it as a separate file and list it in Section
12 of the UI/UX Document. Write "Not used" if not needed. -->

```json
{
  "color": {
    "primary": "[#______]",
    "background": "[#______]",
    "text": "[#______]",
    "success": "[#______]",
    "error": "[#______]"
  },
  "font": {
    "heading": "[Font name], [fallback]",
    "body": "[Font name], [fallback]"
  },
  "space": [4, 8, 16, 24, 32],
  "radius": 8
}
```

## 9. Change Log

<!-- Newest at the bottom. Add a row for every revision. Never delete
rows. -->

| Version | Date | Change | Reason | Approved by |
|---|---|---|---|---|
| 1.0 | [YYYY-MM-DD] | First version | — | [Name] |
