# DESIGN.md — charlieosborne.co

## 1. Visual Theme & Atmosphere

Charlie Osborne's portfolio is a study in disciplined whitespace and Inter Display's geometric precision. The design philosophy is "quiet confidence" — a developer/designer portfolio that communicates taste without performance. The near-white background, compressed heading line-height, and tight negative letter-spacing on h1 create a layout that feels editorial without being theatrical. The atmosphere is calm, contemporary, and personal.

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Background | `rgb(255, 255, 255)` | Pure white canvas |
| Body / primary text | `rgb(10, 10, 10)` | Near-black — same depth as Niki Studio, different context |
| Accent / highlight | `rgb(236, 75, 34)` | Warm orange-red — used on key visual moments |
| Border (heading context) | `rgb(207, 203, 201)` | Warm pale gray — extremely light |
| Glass overlay 1 | `rgba(255, 255, 255, 0.17)` | Light panel over image sections |
| Glass overlay 2 | `rgba(214, 214, 214, 0.5)` | Silver-glass floating panel |

The orange-red accent (`rgb(236, 75, 34)`) is used sparingly — likely for hover states, active markers, or a signature personal element. Its warmth contrasts effectively with the cool white base.

## 3. Typography Rules

**Typefaces**: `Inter Display` for large headings; `Inter` for body and supporting text — the correct split between display-optimized and body-optimized optical variants.

| Selector | Size | Weight | Notes |
|----------|------|--------|-------|
| h1 | 46px | 600 | Compressed line-height (41.86px — below font-size) |
| h4 | 11.5px | 600 | Micro-label scale with slight positive tracking |
| body | 16px | 400 | Standard readable baseline |

- **Compressed line-height on h1** (41.86px at 46px font-size): lines overlap slightly — creates dense, tightly-packed display blocks. This is a deliberate typographic signature.
- **h1 letter-spacing: -0.46px** — 1% negative tracking tightens Inter Display letterforms into an engineered block.
- **h4 at 11.5px with +0.115px tracking** — micro-labels with gentle positive tracking for legibility at small scale.
- The Inter Display / Inter split at different sizes is the correct OpenType strategy.
- **What's absent**: no serif fonts, no ultra-bold weights, no variable font features.

## 4. Component Stylings

- **Glass surface 1**: `rgba(255,255,255,0.17)` — light overlay panels on image sections.
- **Glass surface 2**: `rgba(214,214,214,0.5)` — silver-glass panels, more opaque.
- **Orange accent**: `rgb(236,75,34)` — on headings and interactive elements.
- **Borders**: warm pale gray (`rgb(207,203,201)`) — barely-there dividers.
- **No border-radius tokens detected** — component-level or framework-defined.
- **No shadows** — depth through glass and color only.

## 5. Layout Principles

- Whitespace drives the layout — sections breathe with deliberate empty space.
- The compressed h1 line-height creates dense text blocks that contrast with surrounding air.
- Micro-labels (h4 at 11.5px) categorize content without adding visual weight.
- Framer-based layout uses fixed-grid with responsive column drops.

## 6. Depth & Elevation

Two glass surfaces provide depth:
- `rgba(255,255,255,0.17)` for light image overlays
- `rgba(214,214,214,0.5)` for more substantial floating panels

The warm-gray border and glass panels together suggest a layered card-over-white pattern. No box shadows — elevation is purely through transparency and color.

## 7. Do's and Don'ts

**Do:**
- Use Inter Display for headings above 32px — the optical adjustments matter.
- Apply the compressed line-height (0.91x of font-size) on h1 — it's the signature gesture.
- Reserve the orange-red for one deliberate moment per section.
- Use h4 at 11.5px with +0.115px tracking as the label/category style.

**Don't:**
- Use Inter (body) at display sizes — Inter Display exists for this reason.
- Increase h1 line-height to match font-size — the compression is intentional.
- Apply the orange-red to body text or navigation.
- Add shadows — glass transparency is the elevation model.

## 8. Responsive Behavior

- 46px h1 with -0.46px tracking will need scaling to ~28–32px on mobile.
- Compressed line-height (below font-size) can break on mobile if not capped — requires `line-height: 1` or `min-height` handling.
- Micro h4 at 11.5px is at the readable limit — mobile browsers may auto-scale.
- Glass panels need `backdrop-filter` for the frosted effect — include fallback.

## 9. Agent Prompt Guide

> Build a personal portfolio in the style of Charlie Osborne: white background, near-black text (`rgb(10,10,10)`), Inter Display at 46px/600 weight with compressed line-height (41.86px) and -0.46px letter-spacing, Inter for body text, orange-red accent (`rgb(236,75,34)`) used once per section, glass panels (`rgba(255,255,255,0.17)`, `rgba(214,214,214,0.5)`), micro-labels at 11.5px with +0.115px tracking. No shadows, no border-radius tokens.

*Generated by Sparkbites — extracted from live CSS analysis*
