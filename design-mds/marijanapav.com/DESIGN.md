# marijanapav.com — Design System Reference

## 1. Visual Theme & Atmosphere

Marijana Pavlinić is a brand designer at Vercel, and her site ("Designer crafting brands and websites", with Branding, Digital and Illustration filters) is a restrained, white, grayscale portfolio whose personality lives in a three-font system. Archivo sets the name and intro, Inter runs the body, and IBM Plex Mono shows up as tiny uppercase section labels with wide tracking. The palette is essentially monochrome — white nav, near-black text, soft gray chips — so the work images supply all the colour. The tone is calm, editorial and tool-like, with generous but not extravagant spacing.

---

## 2. Color Palette & Roles

**Foundation**
- `lab(100 0 0)` — white; the sticky nav surface
- `rgb(0, 0, 0)` — default text
- `lab(30.4 0 0)` — dark gray, around `#444`; primary text, nav links and footer
- `lab(11.26 0 0)` — near-black, around `#111`; strongest text and the focus outline

**Neutral surfaces**
- `lab(95.8562 -1.49 -0.0064)` — pale gray (about `#f1f1f1`); the filter-button background (Branding, Digital)
- `lab(92.3762 -1.49 -0.0064 / 0.9)` — light gray at 90 percent opacity; nav bottom border
- `rgb(0, 0, 0)` — `border-panel-border` blocks

There is no chromatic accent; the system is intentionally gray so imagery stays the focus.

---

## 3. Typography Rules

| Role  | Font        | Size | Weight | Line-height | Tracking | Transform |
|-------|-------------|------|--------|-------------|----------|-----------|
| H1    | Archivo     | 16px | 400    | 24px        | normal   | none      |
| H2    | IBM Plex Mono | 12px | 600  | 16px        | 2.4px    | uppercase |
| Body  | Inter       | 16px | 400    | 24px        | normal   | none      |
| P     | Inter       | 14px | 400    | 24px        | normal   | none      |
| Link  | Inter       | 16px | 400    | 24px        | normal   | none      |
| Button| Inter       | 16px | 400    | 24px        | normal   | none      |

**Principles**
- Three voices: Archivo for identity, Inter for reading, IBM Plex Mono for labels.
- Section labels are 12px, weight 600, uppercase, tracking `2.4px` (20 percent of size) — the signature detail.
- The H1 is the same size as body; difference is face, not scale.
- Inter stack falls back to `ui-sans-serif, system-ui`; Plex Mono falls back to Fira Code, Consolas, Monaco.

---

## 4. Component Stylings

**Filter buttons** (`ui-button`: Branding, Digital)
- Background pale gray `lab(95.8562 -1.49 -0.0064)`, text `lab(30.4 0 0)`, no shadow
- Pill-shaped (the extracted radius of `3.35544e+07px` is the Tailwind full-round value)
- Focus: 1px solid `lab(11.26 0 0)` outline

**Text buttons and links**
- Transparent background, dark gray text; the class name `hover:text-theme-1` shows a hover colour change to a theme token (the exact value was not captured)

**Nav**
- White background, 90-percent-opacity gray bottom border, black text

**Border radius**
- Scale of `4px`, `6px`, `8px`, `9px`, `10px`, `15px` plus full-round pills.

**Shadows**
- None detected.

---

## 5. Layout Principles

- Header padding `16px 20px`; footer `0px 20px 32px`; main has `48px` bottom padding.
- Consistent 20px side gutters.
- Breakpoints at `475`, `720`, `768`, `1280`.
- Built with Next.js and Tailwind CSS; images are served at large sizes (3840 wide) for the hero photo.

---

## 6. Depth & Elevation

Flat and bordered. Separation uses hairline borders (the nav's 90-percent-opacity gray rule) and tonal swaps from white to pale gray, never shadows.

---

## 7. Do's and Don'ts

**Do**
- Keep the UI grayscale and let imagery carry colour.
- Use IBM Plex Mono at 12px, weight 600, uppercase with `2.4px` tracking for section labels.
- Use Inter 16px/24px for body and Archivo for the name/intro.
- Use pill-shaped pale gray chips for filters.
- Maintain 20px gutters.

**Don't**
- Don't add brand colour to chrome.
- Don't use shadows for elevation.
- Don't set labels in the body font; the mono label is the system's anchor.
- Don't enlarge the H1; it stays 16px.

---

## 8. Responsive Behavior

Four breakpoints (475, 720, 768, 1280) from small phone to desktop. The 20px gutter and 16px body size remain constant; layout shifts occur through Tailwind responsive utilities.

---

## 9. Agent Prompt Guide

> Build a UI that matches marijanapav.com's design language.

Use a white page with black and dark gray (`#444`-ish, `lab(30.4 0 0)`) text and no accent colour. Set the name/intro in Archivo 16px/24px weight 400, body copy in Inter 16px/24px, and section labels in IBM Plex Mono 12px/16px, weight 600, uppercase, letter-spacing `2.4px`. Use a sticky white nav with a thin light-gray bottom border at 90 percent opacity. Filters are pill buttons with a pale gray background (about `#f1f1f1`), dark gray text, and a 1px near-black focus outline. Corners range 4px to 10px, with full pills for chips. Use 20px page gutters, 16px header padding, 48px bottom padding on main. No shadows; separate with hairlines and tone.

---

*Generated by Sparkbites — extracted from live CSS analysis*
