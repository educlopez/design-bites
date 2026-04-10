# fiasco.design — Design Reference

## 1. Visual Theme & Atmosphere

Fiasco Design is a creative agency whose visual identity embodies structured chaos with editorial sophistication. The off-white canvas (`#F8F9F3`) — slightly green-tinted — creates warmth that differentiates it from clinical whites. The typographic system is the most layered in this collection: three distinct typefaces (Area Normal, HAL Timezone, Gooper) each occupying a strict role, with the serif-sans-serif switching creating constant typographic rhythm.

The color palette is a curated set of bold, named brand hues: yellow, green, blue, pink, orange — each with tint and shade variants. The yellow (`#FFF714`) appears as a full-page page transition wipe, making the transition itself a brand moment.

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Background (off-white) | `#F8F9F3` (--off-white) | Green-tinged canvas |
| White | `#E9EAE2` (--white) | Slightly warm white for surfaces |
| Primary text | `#1D1E19` (--black / --off-black) | Near-black with green tint |
| Footer | `#151612` (--off-black-shade) | Darkest near-black |
| Page transition | `#FFF714` (--yellow) | Full-screen wipe color |
| Accent green | `#03AC47` (--green) | CTA buttons |
| Accent blue | `#84BDFF` (--blue) | Feature highlights |
| Accent pink | `#FCC5FE` (--pink) | Card / section accent |
| Accent orange | `#FD6B01` (--orange) | Update tiles, category tags |
| Label/muted | `#585E6A` | Form labels, secondary text |

Every brand color has tint (+lighter) and shade (+darker) variants, plus an off-black tint at 5% opacity for subtle surfaces.

## 3. Typography Rules

Three typefaces, three distinct roles — no overlap:

| Element | Family | Size | Weight | Notes |
|---------|--------|------|--------|-------|
| H1 | Area Normal | 53px | 400 | −1.08px tracking, sans-serif display |
| H2 | HAL Timezone | 30px | 400 | −0.4px tracking, editorial serif |
| H3 | Area Normal | 30px | 400 | −0.4px tracking |
| H4 | HAL Timezone | 19px | 400 | −0.4px tracking, editorial serif |
| Body | Area Normal | 20px | 400 | −0.4px tracking, generous size |
| Para / emphasis | Gooper | 19px | 700 | UPPERCASE, −0.4px tracking — bold serif |

HAL Timezone is a distinctive display serif with clock/timezone associations. Gooper at 700 uppercase is a structural accent — used for short, punchy labels. Area Normal at 20px body copy is unusually generous.

## 4. Component Stylings

- **Cards:** Near-flat (3–4px radius), using brand color fills from the full palette
- **Pill buttons:** 800px radius — fully pill-shaped for CTAs
- **Update tiles:** Brand-colored backgrounds (orange, blue, pink) — `article.tile-update`
- **Page transition:** Full-screen yellow wipe (`div.c-PageTransition`)
- **Forms:** Textarea with 5% off-black tint background, 193px border
- **CTA buttons:** Blue fill (`#204CE5`) from WordPress form submit
- **Small shadows:** 1px card shadow (`rgba(18,25,97,0.08)`) and large overlay shadow (28px, `rgba(0,0,0,0.16)`)

## 5. Layout Principles

- 24 breakpoints — extremely granular, hand-crafted responsive system
- Spans from 200px (narrow) to 1600px+
- Section padding minimal (0px) — content is flush, controlled by inner padding
- Typography-led composition — section areas defined by type blocks, not card grids
- 44px large pill used for primary interactive elements

## 6. Depth & Elevation

- **Cards:** 1px ambient shadow in brand blue-tinted dark (`rgba(18,25,97,0.08)`)
- **Overlays:** 28–80px deep drop shadows for floating/popup elements
- **No backdrop blur** — shadows are decisive, not diffuse
- Surfaces are defined by background color fills, not elevation shadows in the flat sense

## 7. Do's and Don'ts

**Do:**
- Alternate between Area Normal and HAL Timezone for heading hierarchy
- Use the full brand color palette — each color has a designated context
- Apply the yellow page transition wipe as a brand signature
- Use Gooper uppercase at 700 for short, high-impact labels
- Set body copy at 20px — the generous size is part of the identity

**Don't:**
- Mix typefaces beyond the three-family system
- Use rounded corners on cards — keep radius at 3–4px (near-flat)
- Apply brand colors arbitrarily — orange for updates, blue for links, yellow for transitions
- Reduce body type below 20px — the generous scale is intentional

## 8. Responsive Behavior

- 24 breakpoints from 200px to 1600px — one of the most granular systems possible
- Typography scales through multiple stages — not just mobile/desktop
- Tile layouts reflow from multi-column to single-column progressively
- Brand color assignments are preserved across all breakpoints

## 9. Agent Prompt Guide

> "Design in the style of fiasco.design: green-tinged off-white canvas (`#F8F9F3`), three-typeface system — Area Normal for display body, HAL Timezone serif for editorial headings, Gooper bold uppercase for labels. Rich named brand palette: yellow, green, blue, pink, orange — each used in specific contexts. Near-flat card corners (3–4px). Pill-shaped CTAs (800px radius). Yellow full-screen page transitions. Shadow using brand-tinted dark."

---

*Generated by Sparkbites — extracted from live CSS analysis*
