# gxuri.in — Design System

## 1. Visual Theme & Atmosphere

gxuri.in is a developer portfolio built with an unusual level of systems thinking. The CSS variable set reveals a designer who thinks in easing curves — a full suite of named easing functions (ease-in-quad through ease-in-out-circ) encoded as custom properties signals that animation is a first-class design concern, not an afterthought. The visual aesthetic is typographically austere: helveticaNeue, uppercase navigation, near-black on white. The colour system uses oklch() for accents — an advanced choice that ensures perceptual uniformity across the palette. The result is a portfolio that communicates technical precision and typographic discipline simultaneously.

## 2. Color Palette & Roles

**Base**
- Background: `#fff` (via `--background`)
- Foreground: `#121212` (via `--foreground`) — very dark, not pure black
- Muted surface: `#f5f4f3` (via `--muted`) — warm off-white for card backgrounds
- Muted text: `#4f4f4e` — dark slate for secondary content

**Brand accents** (oklch, perceptually uniform)
- Primary (blue): `oklch(.65 .25 260)` — mid blue with high chroma
- Secondary (teal): `oklch(.7 .2 180)`
- Tertiary (orange): `oklch(.68 .22 40)`
- Success (green): `oklch(.65 .2 145)`
- Warning (yellow): `oklch(.75 .2 70)`
- Error (red): `oklch(.62 .25 25)`
- Info (blue): `oklch(.65 .2 220)`

**Surfaces**
- Light muted: `rgb(245, 244, 243)` — the only detected surface tint
- Dark inversion: `rgb(18, 18, 18)` — full dark block for contrast sections

**Code syntax** (`--code*` properties)
- `#00bfff` — cyan for keywords/strings
- `#4dc398` — mint for values
- `#6c6c6c80` — grey at 50% for comments

**What's absent:** No shadows. No decorative effects. No gradients. The design is resolute in its flatness — depth comes only from the dark/light surface contrast.

## 3. Typography Rules

One font, rigorously applied: **helveticaNeue** (custom loaded, not the system fallback).

| Element | Size | Weight | Case | Tracking |
|---------|------|--------|------|----------|
| Body | 16px | 400 | Normal | Normal |
| `<p>` | 16px | 400 | Normal | Normal |
| `<a>` | 16px | 400 | UPPERCASE | Normal |
| Button | 16px | 400 | Normal | Normal |

Headline sizes are not captured in the CSS data — they are likely set inline or via Tailwind utility classes not extracted. All sizes remain at 16px in the available data, suggesting a flat typographic hierarchy where size differentiation happens through case, weight variation (likely in practice, not captured), and spacing rather than dramatic size jumps.

The uppercase navigation links are the typographic signature — a choice that references print design and Swiss graphic tradition rather than digital UI conventions.

## 4. Component Stylings

**Navigation** — transparent, uppercase links in `#121212`. No background, no border.

**Cards** — `#f5f4f3` fill (muted warm grey), `12px` border-radius. The `3.35544e+07px` max-radius value indicates some elements use `overflow: hidden` with a high border-radius for pill/circle shapes.

**Buttons** — styled with oklch primary (`oklch(.65 .25 260)`) — blue. The custom easing tokens suggest hover/press animations use custom curves rather than CSS defaults.

**Code blocks** — a full syntax highlighting palette encoded as custom properties: cyan, mint, grey, with 50% opacity comments.

**Dark section** — `rgb(18, 18, 18)` background for contrast zones. The `--invert: invert(1)` custom property suggests images or icons flip to light mode when inside dark sections.

## 5. Layout Principles

No media query breakpoints were detected — this suggests either a fully fluid/relative layout or that breakpoints are handled via JavaScript/container queries rather than CSS media queries. The main content has no padding applied via the extracted selectors, indicating layout is built entirely with utility classes not captured at the element level.

The easing function variables (`--ease-out-expo`, etc.) are named following CSS Tricks conventions, suggesting smooth entrance animations for sections and interactive elements are a key part of the layout experience.

## 6. Depth & Elevation

No shadows detected. Zero. Depth is achieved through two mechanisms:
1. **Surface contrast** — `#f5f4f3` vs `#ffffff` vs `#121212` dark sections
2. **Colour temperature** — the oklch accent colours pop against achromatic neutrals

This is a maximally flat design philosophy where elevation is implied by contrast alone. It demands meticulous content hierarchy because there are no visual cues beyond placement and colour.

## 7. Do's and Don'ts

**Do:**
- Use oklch() for all accent colours — the perceptual uniformity is intentional
- Apply uppercase to navigation and label elements — it's the typographic signature
- Use the custom easing properties for all transitions and animations
- Leverage `#f5f4f3` as the only card/muted surface tint
- Apply `--invert: invert(1)` to icons and images within the `rgb(18,18,18)` dark sections
- Use the named easing curves: `--ease-out-expo` for entrance, `--ease-in-out-quart` for state changes

**Don't:**
- Add shadows — the design is intentionally shadowless
- Use system Helvetica — the custom `helveticaNeue` is the brand typeface
- Use more than one surface tint (`#f5f4f3`) per layout — restraint is the aesthetic
- Mix the oklch accent palette promiscuously — each colour maps to a semantic role
- Use gradients or decorative backgrounds

## 8. Responsive Behavior

No detected CSS breakpoints indicates a fluid layout strategy. This likely means:
- Percentage-based or viewport-relative widths
- A single content column that adjusts gracefully
- No dramatic layout reflows — content stacks rather than pivots

The uppercase link pattern maintains legibility across all sizes since uppercase Helvetica is highly readable even at 14–16px.

## 9. Agent Prompt Guide

> Build in the gxuri.in style: one font (Helvetica Neue), near-black (`#121212`) text on white. Uppercase all navigation links. Use `#f5f4f3` for card surfaces. Apply oklch accents for interactive elements — primary blue: `oklch(.65 .25 260)`, secondary teal: `oklch(.7 .2 180)`, tertiary orange: `oklch(.68 .22 40)`. Encode easing curves as CSS custom properties: `--ease-out-expo: cubic-bezier(.19,1,.22,1)` etc. No shadows, no gradients. Contrast sections use `rgb(18,18,18)` dark fill with `filter: invert(1)` on icons. The visual language is flat, technical, and Swiss.

*Generated by Sparkbites — extracted from live CSS analysis*
