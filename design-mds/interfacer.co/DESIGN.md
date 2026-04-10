# interfacer.co — Design System

## 1. Visual Theme & Atmosphere

Interfacer.co is a Framer-built design agency site that wields contrast as personality: stark white expanses broken by a jet-black section and punctuated by electric cyan-green `rgb(27, 255, 227)`. The atmosphere is confident and sparse — a studio that communicates capability through what it omits rather than what it adds. The palette doesn't negotiate: white, black, and one neon. The cyan hovers at the intersection of mint and aqua, giving the brand a fresh, almost digital-natural quality that distinguishes it from both the warm-amber AI space and the cold-blue developer space.

## 2. Color Palette & Roles

**Surface**
- `rgb(255, 255, 255)` — primary canvas
- `rgb(235, 235, 235)` — secondary surface; light grey for card/section differentiation
- `rgb(22, 36, 27)` — deep forest-dark section; a near-black with a green undertone
- `rgb(0, 0, 0)` — maximum contrast dark panel (footer or feature section)

**Accent**
- `rgb(27, 255, 227)` — electric cyan-green; CTA background, hover state, brand signature
- `rgb(25, 255, 227)` — hover variant (marginally different, effectively the same)

**Text**
- `rgb(0, 0, 0)` — body text on white
- `rgb(0, 0, 238)` — browser-default link blue (intentionally unrestyled)

**Absent:** no warm tones, no gradients, no mid-greys beyond `rgb(235, 235, 235)`. The restraint is architectural.

## 3. Typography Rules

Aspekta is the expressive typeface — a geometric sans that carries the brand voice. The base `sans-serif` fallback dominates the default browser-level styles, meaning Aspekta is loaded and applied via Framer's component system rather than at the document root.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| Body/base | sans-serif | 12px | 400 | Framer shell default |
| P / UI text | Aspekta | 12px | 500 | lh 14.4px — tight, label-scale |
| Links | sans-serif | 12px | 400 | Unrestyled |

The type scale is small and functional — 12px throughout suggests either a highly visual layout where text labels rather than narrates, or a design that emphasizes spatial composition over reading. No display-scale headings detected at the CSS extraction layer, which likely means large text is implemented as Framer components with inline styles.

## 4. Component Stylings

**CTA Button** — White background by default, cyan `rgb(25, 255, 227)` on hover. No border. The hover swap is the entire interaction — a clean fill transition that feels electric. Text reads "BOOK A CALL" suggesting uppercase label treatment.

**Pill / Avatar elements** — `border-radius: 100%` for circular elements. `76.63px` radius suggests a large rounded rectangle shape — likely a card or image container with personality.

**Accent blocks** — `rgb(27, 255, 227)` used as div backgrounds for feature highlights, creating cyan-washed content zones.

**Dark section** — `rgb(22, 36, 27)` creates a forest-green-dark panel; subtle chromatic variation from pure black that adds depth without color theatrics.

No shadows. No gradients. Flat surfaces throughout.

## 5. Layout Principles

Standard Framer breakpoints: `809.98px` (tablet), `810px`, and `1199.98px` (wide). Three layout modes: mobile (< 810px), tablet (810–1199px), desktop (> 1199px). Body padding is zero — Framer manages all layout spacing through component margins.

The site is visually organized through color-field sections rather than grid lines: white → grey → dark → cyan blocks create a rhythm that guides the eye without conventional borders or dividers.

## 6. Depth & Elevation

Luminance-based depth with zero shadows:
- `luminance 1.0` — white primary canvas
- `luminance 0.922` — light grey secondary `rgb(235, 235, 235)`
- `luminance 0.72` — cyan accent blocks `rgb(27, 255, 227)`
- `luminance 0.121` — forest dark `rgb(22, 36, 27)`
- `luminance 0.0` — black panel

No box shadows anywhere on the page. Depth is entirely positional and chromatic. The dramatic luminance range (1.0 to 0.0) creates all the hierarchy the design needs.

## 7. Do's and Don'ts

**Do**
- Use the cyan `rgb(27, 255, 227)` exclusively for interactive hover states and accent blocks
- Keep the colour count at three: white, black/dark, cyan
- Apply `border-radius: 100%` for avatars/circular elements, `76.63px` for large rounded cards
- Let section color-fields do layout work — avoid decorative borders or dividers

**Don't**
- Add shadows — the flat surface system is intentional
- Introduce warm tones or gradients; the palette is deliberately cool and binary
- Restyle links away from browser-default blue — the unrestyled link is a deliberate rawness
- Scale up the body text beyond 12px for UI labels; the small text is part of the visual language

## 8. Responsive Behavior

Three breakpoints: mobile (< 810px), tablet (810–1199px), desktop (> 1199px). Framer handles the reflow. At mobile, the full-width color-field sections remain intact — they're background colors, not images, so they reflow naturally. The CTA hover state becomes a tap state on touch devices. The circular elements (`border-radius: 100%`) scale by dimension, not radius.

## 9. Agent Prompt Guide

> Build a design agency landing page in the style of interfacer.co. White canvas with zero decorative elements. Three colors only: white `#ffffff`, near-black `rgb(22, 36, 27)` / pure black `#000000`, and electric cyan `rgb(27, 255, 227)`. Use Aspekta at 12px/500 for all UI text labels. No shadows. Section transitions through full-bleed color fields (white → grey → dark → cyan). CTA button: white fill, cyan hover fill, no border. Fully circular elements use `border-radius: 100%`. Three breakpoints: 810px and 1199px. Framer Motion for interactions.

---

*Generated by Sparkbites — extracted from live CSS analysis*
