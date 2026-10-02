# mitul.ca — Design System Reference

## 1. Visual Theme & Atmosphere

Mitul Shah's personal site ("Photographer, design engineer, and a bit more") is a quiet, single-column portfolio held together by one decision: a saturated ultramarine blue, `rgb(2, 16, 147)`, set against an otherwise neutral page. Nearly everything is small — 14px text on 21px leading — and the only large moment is a 24px name heading. The page is set entirely in a custom face named `chico`, in weights 400 and 500, so the personality comes from the letterforms rather than from scale or decoration. The footer flips to a solid blue block with near-white text, which turns the end of the page into a deliberate colour stamp. The tone is understated, precise, and a little playful ("doing what I can't").

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(0, 0, 0)` — body text; the body background is transparent, so the browser canvas shows through
- `rgb(217, 217, 217)` — neutral gray surface used on flex blocks (placeholders, cards)

**Accent (the brand colour)**
- `rgb(2, 16, 147)` — deep ultramarine: nav text, outlined link text, footer background, filled button background
- `rgb(252, 252, 252)` — soft white: text and borders on top of the blue

**Focus**
- `rgb(16, 16, 16)` — the 1px auto focus outline

The system is effectively one hue. Blue appears either as text on the page or as a filled surface with near-white text; there is no second accent.

---

## 3. Typography Rules

One typeface, `chico` (with a `chico Fallback`), carries every element.

| Role   | Font  | Size | Weight | Line-height | Tracking |
|--------|-------|------|--------|-------------|----------|
| H1     | chico | 24px | 500    | 36px        | normal   |
| H2     | chico | 14px | 500    | 21px        | normal   |
| H3     | chico | 14px | 500    | 21px        | normal   |
| Body   | chico | 14px | 400    | 21px        | normal   |
| P      | chico | 14px | 400    | 21px        | normal   |
| Link   | chico | 14px | 500    | 21px        | normal   |
| Button | chico | 14px | 500    | 21px        | normal   |

**Principles**
- Hierarchy is made with weight (400 vs 500) and a single size jump (14px to 24px), always on a 1.5 line-height.
- Section headings are the same size as body; only weight separates them.
- No uppercase transforms, no letter-spacing, no OpenType features.

---

## 4. Component Stylings

**Filled pills / buttons** (Email, Public Archive, Guestbook)
- Background `rgb(2, 16, 147)`, text and border `rgb(252, 252, 252)`
- Text-weight 500, 14px
- Focus adds a `rgb(16, 16, 16)` auto outline at 1px; hover capture showed no change

**Outlined / ghost links** (nav, role link, "doing what I can't")
- Transparent background, text and border `rgb(2, 16, 147)`

**Border radius**
- `2px` and `4px` only — small, nearly square corners.

**Shadows**
- Two stacks exist: a layered raised shadow (`rgba(8, 8, 8, 0.08) 0px 4px 4px`, `rgba(8, 8, 8, 0.2) 0px 1px 2px`, plus white inset highlights `rgba(255, 255, 255, 0.12) 0px 6px 12px inset` and `rgba(255, 255, 255, 0.2) 0px 1px 1px inset`) giving a tactile, pressed-glass feel, and a standard Tailwind small shadow (`rgba(0, 0, 0, 0.1) 0px 1px 3px`).

---

## 5. Layout Principles

- Single narrow column; no detected breakpoints in the extracted CSS.
- Body and section padding/margin are all `0` — spacing is handled by inner elements.
- The footer has `96px 0px` vertical padding, the largest spacing value found; it gives the closing blue block real weight.
- Built on Next.js and Tailwind CSS (utility classes such as `flex`, `bg-accent`).

---

## 6. Depth & Elevation

Mostly flat. Depth comes from two sources: the `rgb(217, 217, 217)` gray blocks (luminance 0.851) against the page, and the inset-highlight shadow stack, which makes certain elements look like small physical keys. The footer (luminance 0.105) is the only large dark plane.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(2, 16, 147)` as the single accent, as text or as a filled surface.
- Put `rgb(252, 252, 252)` text on blue, not pure white.
- Keep text at 14px/21px and use weight 500 for emphasis.
- Keep radii at 2px or 4px.
- Give the footer generous (96px) vertical padding.

**Don't**
- Don't add a second accent colour.
- Don't swap the custom face for a generic system sans.
- Don't use uppercase, wide tracking, or heavy weights.
- Don't use large corner radii.

---

## 8. Responsive Behavior

No breakpoints were detected, which fits a single fluid column built with Tailwind utilities. Because text is small and set on a 1.5 ratio, the layout reads the same at any width; the blue footer block is the element that anchors the bottom of the page on every screen size.

---

## 9. Agent Prompt Guide

> Build a UI that matches mitul.ca's design language.

Use a single custom sans (`chico`, or the closest geometric-humanist substitute) for everything: 14px/21px body at weight 400, 14px/21px links and headings at weight 500, and one 24px/36px weight-500 name heading. Text is black on the default canvas. The only colour is ultramarine `rgb(2, 16, 147)`: use it for nav and ghost-link text, for filled pill buttons with `rgb(252, 252, 252)` text and border, and for a full-width footer block with `96px 0` padding. Use `rgb(217, 217, 217)` for neutral blocks. Corners are `2px` or `4px`. For tactile controls, use the layered shadow `rgba(8, 8, 8, 0.08) 0 4px 4px, rgba(8, 8, 8, 0.2) 0 1px 2px` with white inset highlights. Focus is a 1px `rgb(16, 16, 16)` auto outline. Keep everything in one narrow column and let the type and the one blue do the work.

---

*Generated by Sparkbites — extracted from live CSS analysis*
