# jensonwong.com — Design System

## 1. Visual Theme & Atmosphere

jensonwong.com is a Next.js/Tailwind portfolio that pairs a display serif with a geometric sans — a classic editorial pairing executed with contemporary restraint. **Fraunces** (a variable optical-size serif with expressive character) headlines the H1; **Outfit** carries everything else. The palette is barely-there: a warm near-white body (`rgb(253, 252, 253)`) with a muted charcoal text `rgb(34, 32, 39)` and secondary text in a desaturated purple-grey `rgb(101, 99, 110)`. The atmosphere reads as a thoughtful personal brand — not trying to impress through visual complexity, but through calibrated taste. A Tailwind v4-style design token system underpins the spacing and color scales, bringing engineering discipline to a human-feeling presentation.

## 2. Color Palette & Roles

**Surface**
- `rgb(253, 252, 253)` — body background; barely-warm near-white with a whisper of pink undertone
- `rgb(250, 249, 251)` — secondary surface; slightly cooler, for card/section backgrounds
- `rgb(243, 240, 244)` — tertiary surface; soft lavender-grey for distinctly contained sections
- `rgba(9, 9, 11, 0.7)` — dark overlay (video/media player UI)

**Text**
- `rgb(34, 32, 39)` — primary text; deep charcoal with slight purple undertone
- `rgb(101, 99, 110)` — secondary/label text; muted mid-grey with purple cast

**Tailwind v4 semantic tokens (available but mostly unseen)**
- Red: `--color-red-500: #fb2c36`
- Green: `--color-green-500: #00c758`
- Blue: `--color-blue-200: #bedbff`
- Grey scale: 50–950 fully defined

**Absent from primary UI:** no accent color applied at the component level — the site lives in the neutral-warm register without a signature brand hue.

## 3. Typography Rules

Fraunces for the H1 display role only; Outfit for everything else. This creates a deliberate typographic hierarchy where the headline carries warmth and character, while the body remains neutral and readable.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H1 | Fraunces | 43.2px | 400 | lh 51.84px — generous 1.2× ratio |
| H2 | Outfit | 28px | 500 | lh 42px — 1.5× ratio, airy |
| H5 | Outfit | 16px | 500 | lh 16px — 1:1 tight |
| Body | Outfit | 16px | 400 | lh 24px |
| P | Outfit | 16px | 400 | lh 32px — spacious reading |
| Links / buttons | Outfit | 16px | 400 | lh 24px |

The P element at `lh 32px` (2× font size) creates a double-spaced reading rhythm — generous whitespace between lines makes prose feel unhurried. The Fraunces H1 at weight 400 is unforced, relying on the serif's optical personality rather than weight for presence.

## 4. Component Stylings

**Cards** — Border-radius `8px` for standard components, `24px` for prominent rounded cards. The two-stop radius system is clean and consistent.

**Header** — `position: sticky`, matching the body background color (`rgb(253, 252, 253)`) for a seamless scroll effect where the header is visible but not visually distinct from the page.

**Video/media** — `rgba(9, 9, 11, 0.7)` overlay suggests embedded video with a custom play control UI.

**Buttons** — Outfit at 16px/400, transparent background, inline with text rhythm.

**No shadows detected** — flat surface treatment throughout.

## 5. Layout Principles

Seven breakpoints: `400px`, `480px`, `600px`, `810px`, `1050px`, `1300px`, `1400px`. A thoughtful progressive scale that covers every major viewport class. The Tailwind v4 `--spacing: .25rem` base confirms a 4px grid. Radius tokens run from `--radius-xs: .125rem` to `--radius-2xl: 1rem`, though the applied radii in components use `8px` and `24px` — slightly outside the token scale, suggesting manual overrides.

Custom font weight tokens are defined (`--font-weight-extralight: 200` through `--font-weight-bold: 700`) but Outfit is used at 400 and 500 only — the full weight scale exists as infrastructure but isn't exercised.

## 6. Depth & Elevation

Gentle luminance stacking:
- `luminance 0.99` — sticky header (`rgb(253, 252, 253)`)
- `luminance 0.979` — video container `rgb(250, 249, 251)`
- `luminance 0.946` — section panels `rgb(243, 240, 244)`
- `luminance 0.036` — dark media overlay `rgba(9, 9, 11, 0.7)`

No shadows on structural elements. The surface hierarchy is expressed entirely through the barely-perceptible luminance steps between the near-white variants. The compressed range (0.946–0.99) means depth is felt, not seen — a sophisticated approach.

## 7. Do's and Don'ts

**Do**
- Use Fraunces only for the H1; its display character is diluted if overused
- Apply the P line-height of `32px` at body size — the generosity is part of the voice
- Match the sticky header background exactly to the body color for seamless scroll
- Use `8px` and `24px` as the two radius options — don't add intermediate values

**Don't**
- Add a brand accent color — the neutral-warm palette is the identity
- Mix Outfit weights beyond 400 and 500; the limited weight range is intentional
- Use Fraunces below 36px — at small sizes its optical character becomes noise
- Compress the P line-height; the airy reading rhythm is a deliberate quality signal

## 8. Responsive Behavior

Seven breakpoints provide smooth progressive adaptation from 400px to 1400px. At mobile (400–480px), the Fraunces H1 at 43.2px may need a size step down to ~32px to prevent overflow. Outfit's generous line-height on P elements remains comfortable at all sizes. The `24px` border-radius cards may reduce to `16px` at mobile to feel proportionate. The sticky header persists across all breakpoints, reinforcing the portfolio navigation at scroll depth.

## 9. Agent Prompt Guide

> Build a personal portfolio in the style of jensonwong.com. Barely-warm near-white background `rgb(253, 252, 253)`. Deep charcoal text `rgb(34, 32, 39)` with secondary muted-purple-grey `rgb(101, 99, 110)`. Fraunces serif at 43.2px/400 for H1 only; Outfit geometric sans at 28px/500 for H2, 16px/400 for body. Paragraph line-height `32px` for a spacious reading rhythm. Cards use `border-radius: 8px` and `24px` — no other values. Sticky header matches body background exactly. No accent color. No shadows. Seven breakpoints: 400, 480, 600, 810, 1050, 1300, 1400px. Tailwind v4 token system.

---

*Generated by Sparkbites — extracted from live CSS analysis*
