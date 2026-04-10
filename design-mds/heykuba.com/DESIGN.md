# heykuba.com — Design System

## 1. Visual Theme & Atmosphere

heykuba.com is a dark-mode-first Framer portfolio that treats darkness as a design medium rather than a preference. The near-black canvas (`rgb(10, 10, 10)`) isn't just an inverted light theme — it's the intentional context for one high-impact accent: `rgb(255, 98, 59)`, a warm orange-red that punches with maximum contrast. The design is sparse to the point of severity: one font (Geist), small type sizes, conservative spacing, and no shadows. What makes it distinctive is the structural contrast — the dark body gives way to a light-grey footer (`rgb(240, 240, 240)`), creating a double-inversion: dark page → light footer, rather than the typical light page → dark footer. Built in Framer, the site relies on Motion animations to provide what the static CSS cannot show.

## 2. Color Palette & Roles

**Base**
- Background: `rgb(10, 10, 10)` — near-black (warm, not pure black)
- Body text: `rgb(0, 0, 0)` — this reads as white in context (CSS may not have overridden the default for the dark background; actual rendered text is likely white)
- Heading text: `rgb(255, 255, 255)` — confirmed white on dark

**The signature accent**
- `rgb(255, 98, 59)` — a warm orange-red. Used as a full-fill surface block (not just an icon or button). High luminance contrast against the dark background.

**Footer inversion**
- Background: `rgb(240, 240, 240)` — light grey, sharp contrast from the dark body
- Footer text: implied black (matching standard text)

**Button**
- `rgba(0, 0, 0, 0.2)` — near-transparent dark button overlay

**Surfaces**
- `rgba(255, 255, 255, 0.04)` — barely-visible white tint for contained sections
- `rgb(10, 10, 10)` — body default, deep dark
- `rgb(0, 0, 0)` — pure black for maximum depth moments

**What's absent:** No secondary accent, no gradients, no dark-blue or purple tones common in dark-mode SaaS. No shadows.

## 3. Typography Rules

One font only: **Geist** — Vercel's open-source geometric sans-serif.

| Element | Size | Weight | Tracking |
|---------|------|--------|----------|
| H1 | 27px | 400 | −0.81px |
| H2 | 20px | 400 | −0.2px |
| `<p>` | 13px | 400 | −0.13px |

The H1 at 27px weight 400 is intentionally understated for a portfolio — this is not a "look at me" scale. Geist at weight 400 everywhere: no bold, no medium. The typographic personality is communicated through tightened tracking (−0.81px on H1, proportionally scaling down) and restrained size rather than weight drama.

The body font (`sans-serif`, 12px) is the browser default — Geist doesn't override the `<body>` element directly, relying on more specific selectors for real content.

Paragraph text at 13px line-height 17.55px (1.35×) is compact — information-dense rather than reading-comfortable. This is a portfolio that assumes the viewer scans rather than reads.

## 4. Component Stylings

**The orange block** — `rgb(255, 98, 59)` as a full-fill Framer frame. The luminance (0.551) puts it exactly at mid-range — it advances against the dark and retreats against the footer's light grey.

**Border radii** — only two: `40px` and `200px`. Both are large, pill-like. No sharp corners, no small radii. Every container is generously rounded.

**Buttons** — `rgba(0,0,0,.2)` fill — a darkened overlay on the dark background, creating a very subtle depression.

**Section** — 148px top / 80px bottom padding, 40px horizontal — generous internal breathing room.

**Footer** — light grey fill with 40px horizontal padding, 10px gap.

**No shadows** — the dark background makes shadows irrelevant; the near-black-to-black surface contrast handles depth.

## 5. Layout Principles

Section padding of 148px top is unusually generous — the hero section breathes extensively. The 40px horizontal padding on sections and the footer creates consistent horizontal rhythm. No complex grid evident in the extracted data — Framer likely handles the layout structure.

Two responsive breakpoints: 809/810 and 1199/1200 — matching Framer's standard tablet/desktop tier system.

## 6. Depth & Elevation

Dark-mode depth without shadows:
1. `rgb(10, 10, 10)` — base canvas
2. `rgb(0, 0, 0)` — deepest black for maximum depth pockets
3. `rgba(255,255,255,.04)` — nearly-invisible surface tint (~4% white) for subtle panel separation
4. `rgb(255, 98, 59)` — the orange accent pops forward at maximum contrast

The light-grey footer (`rgb(240,240,240)`) is the strongest contrast element on the page — it paradoxically creates the most visual "weight" by being the lightest value in a dark composition.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(10,10,10)` as the dark background — warm near-black, not cool pure black
- Apply the orange accent (`rgb(255,98,59)`) as a large fill block — it works at scale
- Keep all border radii large: 40px or 200px — no small/medium radii
- Use the footer `rgb(240,240,240)` as the inversion moment — it's the design's punchline
- Apply Geist weight 400 universally — the uniform weight is deliberate

**Don't:**
- Add shadows — the dark background makes them invisible and unnecessary
- Bold text — weight 400 across the board is the design voice
- Introduce secondary accent colours — the orange works because it's singular
- Use small border radii (below 16px) — the design commits to generous rounding
- Treat the footer as secondary — the light/dark inversion is a structural feature

## 8. Responsive Behavior

Two Framer-standard breakpoints: ≤809px (mobile) and 810–1199px (tablet) and ≥1200px (desktop). The 148px top section padding likely reduces to ~80px on mobile. The generous rounding (40px/200px radii) maintains its visual character at all sizes. The single orange accent colour works as a visual anchor across all viewport widths.

## 9. Agent Prompt Guide

> Recreate heykuba.com: near-black background `rgb(10,10,10)`, white headings `rgb(255,255,255)`. Use **Geist** weight 400 for all text — H1 at 27px / −0.81px tracking, H2 at 20px, body paragraphs at 13px. Only one accent colour: `rgb(255,98,59)` (warm orange-red) used as a large fill block, not a button colour. All border radii are large: 40px for standard containers, 200px for pill shapes. No shadows — depth comes from black-on-near-black surface shifts and `rgba(255,255,255,.04)` subtle panel tints. The footer inverts to `rgb(240,240,240)` light grey — maximum contrast against the dark body. Section padding: 148px top, 80px bottom, 40px sides. Framer Motion for scroll entrance animations on the orange block.

*Generated by Sparkbites — extracted from live CSS analysis*
