# iamnotsrc.com — Design System

## 1. Visual Theme & Atmosphere

iamnotsrc.com operates in the high-contrast minimalist register of personal portfolio design — crisp white canvas, near-black ink, and zero color decoration. Built in Framer, the site lets typography and motion do the work that other portfolios assign to color. The atmosphere is typographically confident: Inter Display at 68px with aggressive negative tracking creates a display presence that feels editorial, almost print-like. The dark footer (`rgb(15, 15, 15)`) acts as a closing curtain, separating the work from the goodbye. There is no brand color — the only chromatic break is the browser-default link blue `rgb(0, 0, 238)`, which appears to be intentional rather than lazy.

## 2. Color Palette & Roles

**Surface**
- `rgb(255, 255, 255)` — primary canvas; body, main sections
- `rgb(242, 242, 242)` — secondary surface; hover state for one CTA, light card variant
- `rgb(15, 15, 15)` — footer; deep near-black closing section

**Text**
- `rgb(10, 10, 10)` — H1 text; maximum contrast without pure black
- `rgb(3, 3, 3)` — H3 text; near-identical, suggests intentional micro-differentiation
- `rgb(255, 255, 255)` — H2 text on dark surface

**Interactive**
- `rgb(0, 0, 238)` — browser-default link blue, used raw and intentionally as the sole accent
- `rgba(0, 0, 0, 0.08)` — subtle overlay used for a Framer component inset

**Absent by design:** no brand color, no gradients, no tinted surfaces. The palette is a statement about restraint.

## 3. Typography Rules

Inter Display is the sole expressive typeface — deployed at headline scale with extreme letter-spacing compression. Body text falls back to the bare `sans-serif` generic, signaling that prose is secondary to presence.

| Role | Font | Size | Weight | Letter-spacing | Notes |
|---|---|---|---|---|---|
| H1 | Inter Display | 68px | 500 | -3.4px | lh 65.28px — tighter than size |
| H2 | Inter Display | 40px | 500 | -1.6px | lh 44.8px |
| H3 | Inter Display | 32px | 500 | -0.96px | lh 44.8px |
| Body/p | Inter | 16px | 500 | -0.48px | lh 16.96px — tight, label-like |
| Base | sans-serif | 12px | 400 | normal | Framer shell default |

The compressed line height on H1 (65.28px for 68px text) means headlines barely breathe — a deliberate choice that makes text feel dense and resolved, not airy.

## 4. Component Stylings

**CTAs** — Two-state buttons: primary (`rgb(3, 3, 3)` background), secondary (`rgb(242, 242, 242)` background). Hover on primary reveals `rgb(240, 240, 240)` — a nearly invisible inversion to near-white. No border, no icon. Text-only confidence.

**Cards / Sections** — Border radius: `12px` (standard cards), `66px` (pill/tag shapes), `8px` (tighter elements), `100px` (fully round). The large pill radius suggests rounded tag or chip components.

**Links** — Shadow-stacked: five-layer progressive shadow `rgba(0,0,0,0.192)` through `rgba(0,0,0,0.106)` creates a subtle left-leaning drop that hints at physicality without being decorative.

**Framer animations** — Framer Motion is the animation layer; expect entrance transitions and hover states driven by motion rather than CSS.

## 5. Layout Principles

Framer-generated layout with breakpoints at `809px` and `1199px` — a standard tablet/desktop split. Content is structured in large vertical sections with generous padding: `134px 24px 140px` for primary sections, `88px 0px 186px` for footer. The horizontal gutter is tight at `24px`, keeping content flush and intentional.

Three layout widths: mobile (< 809px), tablet (809–1199px), desktop (> 1199px). The tall section padding creates a slow, scrolling-editorial experience where each section feels like a page spread.

## 6. Depth & Elevation

Elevation is achieved almost entirely through progressive link shadows — the five-stop shadow on anchor elements is the most complex depth effect on the page. Card surfaces step lightly:

- `luminance 1.0` — white canvas
- `luminance 0.949` — light grey surface `rgb(242, 242, 242)`
- `luminance 0.059` — footer `rgb(15, 15, 15)`

No box shadows on structural elements. The dark footer creates the deepest visual layer, acting as a ground plane. The `rgba(0,0,0,0.08)` overlay adds a whisper of depth to one Framer component.

## 7. Do's and Don'ts

**Do**
- Apply aggressive negative letter-spacing to Inter Display headings (≥ `-3.4px` at 68px)
- Keep the palette achromatic — the intentional link blue lands harder against zero competition
- Use the five-stop progressive shadow on interactive elements for tactile depth
- Honor the tall section padding; the breathing room is structural, not accidental

**Don't**
- Add a brand color — the browser-default blue is the accent by design
- Lighten Inter Display weights above 500; medium weight at large size is the brand voice
- Reduce section padding to tighten the page — the slowness is intentional
- Use gradients or textured backgrounds — the whiteness is the design

## 8. Responsive Behavior

Three breakpoints: mobile (< 809px), tablet (809–1199px), desktop (> 1199px). Framer handles layout reflow automatically. The H1 at 68px likely scales down at mobile; Inter Display's negative tracking should be loosened proportionally at smaller sizes to maintain legibility. Section padding compresses horizontally to `24px` gutters on all viewport sizes.

## 9. Agent Prompt Guide

> Recreate a minimal personal portfolio in the style of iamnotsrc.com. White canvas, near-black text. Use Inter Display for all headings: H1 at 68px/500 weight with `-3.4px` letter-spacing, line-height tighter than font-size. Body in bare sans-serif fallback. No brand color — use browser-default link blue `#0000ee` as the only accent. Two CTA variants: dark `rgb(3,3,3)` and light `rgb(242,242,242)`, no borders. Footer in `rgb(15,15,15)` with white text. Section padding minimum `134px` vertical. Border-radii: `12px` for cards, `66px` for pill elements. Framer-style entrance animations implied.

---

*Generated by Sparkbites — extracted from live CSS analysis*
