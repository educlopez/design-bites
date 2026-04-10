# jamesbaduor.com — Design System

## 1. Visual Theme & Atmosphere

James Baduor's portfolio reads as a study in calibrated restraint. The palette is warm near-white — not clinical white — with a four-step background gradient from pure white through cream to a cool sage-tinted grey. Every surface has a reason to exist: navigation floats on transparent, content settles onto `#fbfaf9`, and interactive zones recede further into `#f5f7f4`. The effect is spatial without relying on shadows.

Typography is the workhorse of expression here. Inter is set at unusually small sizes with consistent negative letter-spacing, creating a compressed, editorial feel. There are no decorative flourishes, no gradients, no illustrations. The design communicates personality through proportion and negative space alone.

Tokens are fully systematised — every colour, spacing value, and type size is defined as a CSS custom property. This is a bespoke component system, not a utility framework, and it shows.

---

## 2. Color Palette & Roles

| Role | Token | Hex | Notes |
|------|-------|-----|-------|
| Primary text | `--foreground-primary` | `#171717` | Near-black, not pure black |
| Secondary text | `--foreground-secondary` | `#7c7d7b` | Warm mid-grey |
| Tertiary text | `--foreground-tertiary` | `#a5a6a3` | Captions, metadata |
| Inverse text | `--foreground-white` | `#ffffff` | On dark surfaces |
| Page background | `--background-primary` | `#ffffff` | Nav region |
| Content background | `--background-secondary` | `#fbfaf9` | Main content area |
| Subtle surface | `--background-tertiary` | `#f5f7f4` | Cards, inset zones |
| Divider fill | `--background-quaternary` | `#e8eae7` | Borders as filled regions |
| Primary border | `--border-primary` | `#e8eae7` | Matches quaternary bg |
| Secondary border | `--border-secondary` | `#f5f7f4` | Matches tertiary bg |

The palette is warm-neutral throughout — note the slight green-grey bias in `#f5f7f4` and `#e8eae7`. No accent colour exists; hierarchy is achieved through opacity and tonal step alone. The absence of a branded accent colour is a deliberate choice that keeps focus on the work.

---

## 3. Typography Rules

Single typeface: **Inter** (variable, loaded via Next.js font optimisation). Every size is set with negative tracking to tighten the optical feel at small sizes.

| Role | Token | Size | Weight | Line Height | Tracking |
|------|-------|------|--------|-------------|----------|
| Main title / H1 | `--font-main-title-*` | 24px | 500 | 1.4 | −0.64px |
| Caption / labels | `--font-caption-*` | 16px | 500 | 1 | −0.32px |
| Body primary | `--font-body-primary-*` | 15px | 400 | 1.6 | −0.32px |
| Body secondary | `--font-body-secondary-*` | 13px | 400 | 1.6 | 0 |
| Buttons | `--font-button-*` | 13px | 600 | 1 | −0.26px |

Noteworthy: h1 is only 24px — this is not a loud portfolio. The title size would be body text on most sites. This compression forces the layout and content to carry weight instead of size. The 1.6 line-height on body creates generous reading rhythm for a small base size.

No display type, no serif, no type mixing. Hierarchy is weight and colour only.

---

## 4. Component Stylings

**Buttons**
- Padding: `10px 14px`
- Border radius: `88px` (fully pill-shaped)
- Font: 13px / 600 / −0.26px tracking
- Background: foreground-primary (`#171717`) — inverted from page
- Text: foreground-white

**Navigation**
- Transparent background (`rgba(0,0,0,0)`) — floats over content
- Uses foreground-primary text

**Cards / Inset blocks**
- Background: `--background-tertiary` (`#f5f7f4`)
- Border: `--border-primary` (`#e8eae7`)
- No border-radius specified — likely sharp or very low radius

**Status / badge elements**
- Use secondary and tertiary foreground for deemphasised states
- The `div.bg-foreground-primary` surface confirms dark-on-light inversion patterns exist for featured elements

---

## 5. Layout Principles

The layout uses a flex-based main column. Content width is constrained, not full-bleed. Spacing uses the 4-step background system as implicit zoning — the background colour communicates layer depth more than padding alone.

- Base body padding: `0px` — section-level components own their own spacing
- Tight typographic scale means more visual content per viewport
- Navigation is positioned outside the main flow
- No grid framework tokens are declared — spacing is component-owned

The overall philosophy: whitespace through tonal shift, not padding. Sections are separated by surface colour changes rather than explicit gaps.

---

## 6. Depth & Elevation

Shadows are absent. Depth is communicated entirely through the four-tier background system:

| Level | Surface | Luminance |
|-------|---------|-----------|
| 0 — Page | `#ffffff` | 1.00 |
| 1 — Content | `#fbfaf9` | 0.981 |
| 2 — Cards | `#f5f7f4` | ~0.96 |
| 3 — Borders / dividers | `#e8eae7` | ~0.92 |
| Inverse | `#171717` | ~0.01 |

This is a flat design with tonal depth. Elements never appear to float; they nest. No `box-shadow`, no `filter: drop-shadow`, no backdrop blur.

---

## 7. Do's and Don'ts

**Do:**
- Use the 4-step background system for zoning — never skip levels
- Apply negative letter-spacing consistently at every size
- Keep the title no larger than 24px medium; scale through colour not size
- Use pill buttons (`border-radius: 88px`) for all primary actions
- Let negative space speak — resist adding more elements when a tonal shift will do

**Don't:**
- Introduce accent colours or any chromatic hue
- Use font weights above 600 or below 400
- Add box-shadows or drop-shadows — they break the flat tonal system
- Mix font sizes aggressively; the scale is intentionally compressed
- Use uppercase text transforms — the design is entirely lowercase/sentence case

---

## 8. Responsive Behavior

Built with Next.js App Router. The token system includes no explicit breakpoint variables, suggesting responsive behaviour is handled at the component level via Tailwind or CSS media queries.

- Navigation is transparent and likely collapses to a mobile menu pattern
- The flex layout of `main` adapts naturally to single-column on narrow viewports
- Button padding (`10px 14px`) is touch-friendly at its current size
- Typography sizes do not appear to scale with viewport — the compressed scale reads well at mobile sizes

No detected breakpoint tokens. Layout is expected to be single-column mobile-first, expanding to a constrained max-width container on desktop.

---

## 9. Agent Prompt Guide

**Quick reference:**
- Background sequence: `#ffffff` → `#fbfaf9` → `#f5f7f4` → `#e8eae7`
- Text sequence: `#171717` → `#7c7d7b` → `#a5a6a3`
- Font: Inter, sizes 13–24px, always with negative tracking
- Buttons: pill shape (`border-radius: 88px`), dark fill, 13px/600

**Prompt to replicate this aesthetic:**
> "Design a minimal portfolio section using only Inter. Background is warm off-white `#fbfaf9`. Primary text is near-black `#171717`. Use tonal surface shifts (`#f5f7f4`, `#e8eae7`) instead of shadows for depth. All buttons are fully pill-shaped. Font sizes stay between 13–24px with negative letter-spacing. No accent colours. No decorative elements."

**Prompt to extend a component:**
> "Add a card component to jamesbaduor.com's design system. Background `#f5f7f4`, bordered by `#e8eae7`, body text `#171717` at 15px/400/−0.32px, label `#7c7d7b` at 13px/400. No shadow. Pill button `#171717` if an action is needed."

---

*Generated by Sparkbites — extracted from live CSS analysis*
