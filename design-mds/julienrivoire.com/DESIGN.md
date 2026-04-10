# julienrivoire.com — Design System

## 1. Visual Theme & Atmosphere

Julien Rivoire's site is a study in radical minimalism — a near-blank canvas that puts the work front and center. The design language is deliberately stripped of decoration: no gradients, no shadows, no rounded corners. The palette is pure black on transparent white, with a dark charcoal surface appearing as a stage for content. The atmosphere is that of a printed portfolio — ink on paper — where silence and space carry as much weight as the content itself. This is a site that trusts its work to do the talking, and refuses to compete with it.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|---|---|---|
| **Text / Primary** | `rgb(0, 0, 0)` — Pure Black | Body text and borders |
| **Secondary Text / Headings** | `rgba(0, 0, 0, 0.75)` — 75% Black | Headings and links; slight opacity softens hierarchy |
| **Page Background** | Transparent / White | No explicit background set |
| **Content Surface** | `rgb(26, 26, 26)` — Near Black | Dark panel/stage for featured content |
| **Link / Icon Color** | `rgba(0, 0, 0, 0.75)` — Muted Black | Echoes heading color |

The palette is binary. There is no accent color, no brand hue — only pure black and its opacity variants against white. The single dark surface (`#1a1a1a`) provides a dramatic counterpoint, likely used as a full-bleed section or image backdrop.

---

## 3. Typography Rules

| Element | Font | Size | Weight | Line Height | Notes |
|---|---|---|---|---|---|
| `body` | Times | 11.52px | 400 | normal | Serif base — classically editorial |
| `h2` | Gravity Variable, Icons | 18.432px | 700 | 1:1 (tight) | Variable font; display weight headings |
| `a` (icons) | Icons | 22px | 400 | 1:1 | Icon font used for navigation/links |

Times as the body font is a deliberate, opinionated choice — it signals craft and editorial intent rather than tech-forward neutrality. The display font "Gravity Variable" provides a modern, geometric contrast to the classical serif base. No `text-transform`, no `letter-spacing` overrides — the type is used raw, at its own proportions. Notably small base size (11.52px) reinforces the dense, print-like quality.

---

## 4. Component Stylings

**Navigation / Links**
- Font: Icons (icon font, 22px)
- Color: `rgba(0,0,0,0.75)` — slightly receded
- No underline treatment detected; likely relies on icon clarity alone
- No hover states extracted — interaction is implied, not animated

**Headings (h2)**
- Gravity Variable at 700 weight, 18.432px
- Line height equals font size — zero leading, tight stacking
- Color matches link opacity (`0.75`)

**Body Content**
- Times at 11.52px — dense and compact
- No padding on body; content flush to edges
- No border radius anywhere — everything is hard-edged

**Animated Cursor**
- Custom CSS property `--following-width: -400px` with `--following-animation-duration: 450ms` — suggests a custom following/trailing cursor animation

---

## 5. Layout Principles

- Zero body padding and margin — content bleeds to viewport edges
- No detected grid system or breakpoints — likely a single-column or canvas-based layout
- Spacing is purely contextual, not systematic
- The dark surface (`#1a1a1a`) is the only structural container detected — likely a full-width hero or portfolio stage
- Absence of gap values implies flex/grid are not used at the body level

---

## 6. Depth & Elevation

No shadows detected. No border radii. Depth is achieved purely through color contrast — the stark shift from white ground to `#1a1a1a` surface creates a single, dramatic layer. This is a flat-with-purpose aesthetic: elevation is spatial, not ornamental.

---

## 7. Do's and Don'ts

**Do:**
- Use pure black and opacity variants for all text hierarchy
- Keep surfaces either white or `#1a1a1a` — no mid-tones
- Use Times for body copy when an editorial, print-like feel is needed
- Let whitespace and silence define the layout
- Honor the 450ms animation timing for cursor/motion effects

**Don't:**
- Add rounded corners — everything is hard-edged
- Introduce gradients, shadows, or decorative borders
- Use sans-serif for body copy — the serif is a core identity choice
- Add color accents or brand hues
- Add explicit padding/margins that break the flush-to-edge aesthetic

---

## 8. Responsive Behavior

No breakpoints were detected in the extracted CSS. The site either uses a single fluid layout that adapts without explicit media queries, or is primarily designed for desktop viewports. The icon font navigation (22px) and compact type scale (11.52px body) suggest a desktop-first experience. Mobile adaptation, if any, likely uses percentage widths or viewport units rather than named breakpoints.

---

## 9. Agent Prompt Guide

**Quick color reference:**
- Background: transparent / white
- Text: `#000000` / `rgba(0,0,0,0.75)`
- Dark surface: `#1a1a1a`

**Prompt to recreate this style:**
> "Design a portfolio page in the style of julienrivoire.com: pure black text on white, Times serif body at small scale (11.52px), a bold variable display font for headings, zero padding, no rounded corners, no shadows, and a single full-bleed dark panel (#1a1a1a) as a stage for featured work. Atmosphere: printed editorial, silent, confident."

**Prompt for a component in this system:**
> "Create a project card with hard edges, no shadow, no radius, white background, black text in Times, heading in a bold variable sans-serif. No decorative elements."

*Generated by Sparkbites — extracted from live CSS analysis*
