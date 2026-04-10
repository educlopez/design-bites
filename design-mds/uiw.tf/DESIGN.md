# uiw.tf — Design Document

## 1. Visual Theme & Atmosphere

uiw.tf is a design portfolio or UI showcase with the confident minimalism of a creative studio that has nothing to prove. The foundation is pure white (`rgb(255, 255, 255)`) with ink-black text (`rgb(20, 22, 23)`) — one of the most committed black-on-white palettes in the space. The single moment of brand expression is a neon mint-green (`rgb(27, 255, 205)`) appearing on copyable labels — a tooltip-like badge that announces its own interactivity. Inter carries all the type. The atmosphere is studio-grade: precise, unadorned, and aware that every added element costs something.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(255, 255, 255)` | Page and all surfaces |
| Body text | `rgb(20, 22, 23)` | All prose and labels |
| Pure black | `rgb(0, 0, 0)` | Buttons, borders, links |
| Copyable label accent | `rgb(27, 255, 205)` | Interactive copy-badge; neon mint-green |
| Button bg | transparent | Ghost buttons only |
| Shadow | `rgba(0, 0, 0, 0.12) 0px 8px 30px` | Single shadow tier for card elevation |

The palette is as stripped as it gets: white, two values of black, and one electric accent. The neon mint (`rgb(27, 255, 205)`) is the only color decision on the page, and it earns that right by appearing only where something is interactive and copyable. It functions as a UX signal, not a brand color.

---

## 3. Typography Rules

**Typeface:** Inter — universal, neutral, optimized for screen rendering at every size.

| Context | Size | Weight | Leading | Tracking |
|---|---|---|---|---|
| Display headline (h1) | 48px | 700 | normal | normal |
| Body (body) | 16px | 400 | normal | normal |
| Prose (p) | 14px | 400 | 24px | normal |
| Links (a) | 16px | 400 | normal | normal |
| Buttons | 14px | 400 | normal | 0.1px |

Unlike most Inter implementations, uiw.tf applies no negative letter-spacing on headings — the 48px/700 title stands unmodified. This gives the display text a slightly wider, more open presence than tightly-tracked peers. The `0.1px` button tracking is a micro-detail that slightly opens up label legibility. Body text at 14px/24px (`p`) is a dense but comfortable reading rhythm.

---

## 4. Component Styling

Buttons are transparent with black borders — ghost-style throughout, no fills except for the neon mint copyable badge. Links render in pure black with a white background context, making them indistinguishable from body text until hovered. The `rgba(0,0,0,0.12) 0px 8px 30px` shadow is the sole elevation tier — smooth, wide-spread, used to lift cards off the page gently. The main content has substantial side margins (`260px`), creating a focused content column. No border-radius data was explicitly extracted, suggesting standard browser defaults or Tailwind's `rounded` (~4px) values.

---

## 5. Layout Principles

The main element carries `64px` padding with `260px` horizontal margins — centering content into a controlled reading column on wide screens. Footer margins mirror this at `~266px`. This is a deliberately narrow content area on desktop, rejecting the full-width grid approach. Breakpoints at `600px` and `640px` indicate a single responsive inflection: the wide margins collapse to standard mobile padding below `600px`. The layout prioritizes focused reading over spatial generosity.

---

## 6. Depth & Elevation

One shadow tier handles all elevation: `rgba(0, 0, 0, 0.12) 0px 8px 30px`. It is a single, soft, downward-casting shadow — no horizontal offset, no secondary layer. The transparency level (12% black) keeps it airy and non-dramatic. No inner shadows, no border-radius compound shadows, no color-tinted elevation. The neon mint badge likely has no shadow of its own — its color carries all the visual weight needed.

---

## 7. Do's and Don'ts

**Do:**
- Use `rgb(27, 255, 205)` exclusively for interactive copy/reveal elements
- Apply the single shadow (`rgba(0,0,0,0.12) 0px 8px 30px`) only to card-level elements
- Let headings breathe with default letter-spacing — no negative tracking here
- Keep links black on white without color differentiation; hover states carry the signal
- Maintain `260px` desktop margins to preserve the focused column feel

**Don't:**
- Introduce a second accent color alongside the neon mint
- Use the neon mint as a section background or decorative fill
- Apply color to text links in their default state
- Add more than one shadow tier — the single soft shadow is the entire depth vocabulary
- Override button backgrounds with fills (except the copy badge)

---

## 8. Responsive Behavior

Two breakpoints (`600px`, `640px`) define the sole responsive transition. Below `600px`, the `260px` margins collapse and the single-column layout fills the viewport. The `64px` content padding likely reduces to `24px` or `16px` on mobile. The design is intentionally simple to adapt: with no multi-column grids, no complex navigation, and no image carousels, the responsive system is minimal by design.

---

## 9. Agent Prompt Guide

> Build a UI portfolio/showcase in the style of uiw.tf. White background `#ffffff`, text `rgb(20,22,23)`, buttons and borders in pure black `rgb(0,0,0)`. Inter typeface throughout: 48px/700 for display headings (no letter-spacing adjustments), 14px/400/24px for body. Single accent: neon mint `rgb(27,255,205)` for copyable/interactive label badges only. One shadow tier: `rgba(0,0,0,0.12) 0px 8px 30px` for card elevation. Desktop layout in a focused column with 260px side margins. Two breakpoints: 600px and 640px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
