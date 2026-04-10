# arcade.la — Design System

## 1. Visual Theme & Atmosphere

Arcade.la is a creative studio site built in Framer that wears its tool choice openly — and turns it into an advantage. The design vocabulary is minimal to the point of austerity: near-black canvas, white typography, a single typeface, no decorative elements. What makes it distinctive is what's absent — no color palette, no gradient, no component library complexity. The atmosphere is confident void: a dark room where the work is the only light source. The few interactive moments (link hover adding `rgba(255,255,255,0.15)` tint) are quiet, barely perceptible gestures.

## 2. Color Palette & Roles

**Backgrounds**
- Page/body: `rgb(15, 15, 15)` — near-absolute black, not quite pure
- Raised surface: `rgb(36, 36, 36)` — the only visible elevation step
- Frosted/glass element: `rgba(255, 255, 255, 0.1)` — a single translucent element

**Text / Interactive**
- Primary text: expected white/near-white (based on dark bg convention; base `color` was `rgb(0,0,0)` on body — likely overridden by Framer-generated classes)
- Links: `rgb(0, 0, 238)` — browser-default blue used intentionally on a dark canvas, a deliberate retro-web gesture

**Hover state**
- Link hover background: `rgba(255, 255, 255, 0.15)` — subtle white tint, no color shift

The palette has two effective tones: near-black and near-white. The browser-default link blue is a provocation — not laziness.

## 3. Typography Rules

**Manrope** — the sole named typeface. A geometric humanist sans-serif with strong personality across weights. Used for paragraphs and primary content at 14px.

The base `body` selector falls back to generic `sans-serif` at 12px — this is Framer's generated base, not the designed type setting. Manrope at 14px is the actual type system.

- **Paragraphs**: 14px / 400 / 19.6px line-height (1.4× ratio — comfortable)
- No heading selector extractions — Framer likely uses custom class names for display text
- No mono font — this is a purely prose typographic system
- No letter-spacing adjustments — type is set neutrally

The restraint in the type system matches the visual restraint. Weight variation, if any, would be achieved through Manrope's full weight range (200–800) but only regular is confirmed.

## 4. Component Stylings

**Links**: Browser-default link blue (`rgb(0,0,238)`) on a dark background creates maximum contrast with an intentionally anti-design feel — referencing early web aesthetics. Hover adds a white tint background without changing text color.

**Pill/circular elements**: `100px` border-radius — full pill, used for buttons or tags.

**Structural elements**: `2px` border-radius — almost square, for cards or frames.

**No shadows**: Empty shadows array confirms zero drop-shadow usage across all components.

**Framer-specific**: Component selectors use Framer's generated class names (`.framer-KukGW`, `.framer-1m8a7i8`) — the design is tightly coupled to Framer's runtime.

## 5. Layout Principles

Three breakpoints: 799.98px, 800px, and 1399.98px — a Framer convention where pairs of values prevent overlap at exact pixel boundaries. This suggests three layout states: mobile, tablet, desktop.

The body `padding: 0px, margin: 0px` with footer at `0px gap` indicates a layout that allows Framer components to breathe through their own internal spacing rather than a global rhythm system.

No max-width container extracted — likely full-bleed sections with Framer's internal column constraints.

## 6. Depth & Elevation

One raised surface at `rgb(36,36,36)` — 21 luminance points above the canvas. No shadows whatsoever. The `rgba(255,255,255,0.1)` element (likely a glass card or modal surface) is the only depth gesture. This is an extremely flat design, using darkness itself as the spatial medium.

## 7. Do's and Don'ts

**Do**
- Use the intentional browser-default blue (`rgb(0,0,238)`) for links — it's a design choice
- Keep surfaces near-black with minimal differentiation
- Use Manrope for all text; let its humanist character provide warmth
- Apply `rgba(255,255,255,0.15)` for hover states — never change color or add shadows

**Don't**
- Introduce color accents beyond the blue link convention
- Add shadows or gradients — the void aesthetic requires restraint
- Use more than two surface tones
- Fight the Framer-generated structure; work with its spacing system

## 8. Responsive Behavior

Three breakpoints at ~800px and ~1400px. Framer's layout engine handles column reflow. At mobile, single-column with full-bleed sections. The minimal design scales cleanly — no complex component recomposition needed. Typography stays at 14px across breakpoints.

## 9. Agent Prompt Guide

> Recreate arcade.la's design: near-black canvas `rgb(15,15,15)`, single Manrope typeface at 14px regular, no shadows, no color accents except intentional browser-default blue `rgb(0,0,238)` for links. Two surface tones only. Hover states add `rgba(255,255,255,0.15)` background — nothing else changes. Full-pill buttons (`100px` radius) versus near-square structural elements (`2px`). The design philosophy is confident minimalism: the absence of decisions IS the decision.

---

*Generated by Sparkbites — extracted from live CSS analysis*
