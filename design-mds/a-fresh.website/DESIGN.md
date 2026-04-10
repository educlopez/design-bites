# a-fresh.website — Design System

## 1. Visual Theme & Atmosphere

a-fresh.website commits fully to a dark, near-black aesthetic lit by a single electric accent: a vivid chartreuse-green (`rgb(188, 254, 47)`). The palette is intentionally minimal — almost everything is black or white, and the one accent colour does all the expressive work. The result feels like a product-focused SaaS landing page shot in night mode: premium, focused, and a little edgy. GSAP-powered animations add kinetic energy without sacrificing legibility. What's absent is as notable as what's present: no gradients, no photography, no decorative illustration — just clean typography, stark contrast, and one bold highlight that functions almost like a neon sign in the dark.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page background | `rgb(20, 20, 20)` | Body, main canvas |
| Deep surface | `rgb(12, 12, 12)` | Darkest card / overflow-hidden layers |
| Elevated surface | `rgb(30, 30, 30)` | Card backgrounds, containers |
| Primary text | `rgb(255, 255, 255)` | All body copy, nav, footer |
| Inverted text | `rgb(0, 0, 0)` | Text on white/accent backgrounds |
| CTA background | `rgb(255, 255, 255)` | Subscribe / primary button |
| Accent — electric lime | `rgb(188, 254, 47)` | Hero highlight, glow effect |
| Accent — soft lime | `rgb(173, 229, 130)` | Secondary surface highlight |
| Error / badge | `rgb(252, 165, 165)` bg / `rgb(153, 27, 27)` text | Status badges, error states |
| Border / divider | `rgb(229, 231, 235)` | Subtle structural borders |
| Nav active bg | `rgba(255, 255, 255, 0.10)` | Selected nav item pill |
| Nav inactive | opacity `0.5` on white | Unselected nav items |

The colour system is strictly binary (dark canvas, white content) with the lime accent reserved for moments of emphasis — glow shadow, feature callouts, hero elements.

## 3. Typography Rules

The site is entirely set in **Inter** — a pragmatic, neo-grotesque sans-serif that reads cleanly at all sizes. The notable choice is restraint: no bold weights, no italics, no decorative typefaces. Everything runs at weight 400 (regular) except buttons, which step up to 500 (medium).

| Element | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|
| h1 | 36px | 400 | 45px (1.25) | −0.9px |
| h4 | 24px | 400 | 36px (1.5) | normal |
| body / p / a / input | 16px | 400 | 24px (1.5) | normal |
| button | 14px | 500 | 21px (1.5) | normal |

The negative letter-spacing on `h1` (−0.9px) tightens large display text for a more refined, typographically considered look — a subtle but deliberate move. Body text line height of 1.5 keeps long-form content airy without waste.

## 4. Component Styling

**Buttons**: White background, black text, weight 500, 14px. Borderless (`rgba(0,0,0,0)`). Rounded at 8–12px. No hover state detected — interaction likely handled via GSAP transforms.

**Nav pills**: Active state uses `rgba(255,255,255,0.10)` glass background. Inactive links fade to 50% opacity, brightening to full on hover — a clean opacity-toggle pattern.

**Cards / surfaces**: Three elevation levels via background darkness (20 → 30 → 12). Border radius ranges 6px–24px; larger radii (24px) on prominent cards, tighter (6–8px) on inline components.

**Badges / tags**: `rgb(252, 165, 165)` background with `rgb(153, 27, 27)` text — a warm red-on-pink combination for status or error labels.

**Glow effect**: The lime accent appears as a diffuse box-shadow: `rgb(188, 254, 47) 0px 0px 15px 0px` — no spread, just a soft luminous halo. Used sparingly for maximum impact.

## 5. Layout Principles

Tight, mobile-first spacing with a generous breakpoint ladder (640 / 844 / 1080 / 1536 / 1920px). The 844px breakpoint suggests iPhone landscape optimisation. Sections use minimal padding (16px horizontal, 16px top, 8px bottom) — content sits close to the edges, giving a dense, information-rich feel. The `div.pr-[40px]` pattern suggests asymmetric right-padding for text blocks paired with visual elements. No large gutters or excessive whitespace — every pixel earns its place.

## 6. Depth & Elevation

Depth is created almost entirely through **background luminance** rather than shadows. Three distinct surface levels:

- `rgb(12, 12, 12)` — luminance 0.047 (deepest, behind-the-scene layer)
- `rgb(20, 20, 20)` — luminance 0.078 (base canvas)
- `rgb(30, 30, 30)` — luminance 0.118 (elevated cards)

The one real shadow is the lime glow (`0px 0px 15px`) applied to a single hero element. No drop shadows, no blurs elsewhere — flatness is intentional, with the glow acting as a single moment of theatrical depth.

## 7. Do's and Don'ts

**Do:**
- Use lime accent (`rgb(188, 254, 47)`) as a singular focal point — one hero element, never scattered
- Use opacity (0.5 → 1.0) for nav state transitions instead of colour changes
- Keep type in Inter at 400 weight; only bump to 500 for actionable elements
- Maintain the three-tier surface system (12 / 20 / 30) for spatial hierarchy
- Apply negative letter-spacing only at display sizes (32px+)

**Don't:**
- Introduce additional accent colours — the lime is the entire expressive budget
- Use shadows beyond the signature lime glow
- Add border-radius above 24px or mix many different radii in one view
- Use font weights above 500 — heaviness breaks the calm authority of the design
- Place white text on the lime surface — contrast ratio fails

## 8. Responsive Behavior

Five breakpoints: 640 / 844 / 1080 / 1536 / 1920px. The 844px point is unusual — it targets iPad mini portrait and iPhone landscape specifically, signalling careful attention to mid-size viewports. Built with Tailwind CSS so breakpoints are utility-class driven. Section padding stays constant (16px) across sizes; layout likely shifts from single-column stacking to multi-column grids at the 1080px threshold.

## 9. Agent Prompt Guide

> "Design in the style of a-fresh.website: near-black dark mode (`#141414` base), single electric lime accent (`#BCFE2F`), Inter font at regular weight throughout, white CTA buttons, three-tier background depth (12/20/30 darkness levels), subtle lime glow on hero elements, opacity-based navigation states, tight 16px section padding, border radii 6–24px, Tailwind utilities, GSAP for motion. No gradients, no bold type, no additional accent colours."

---

*Generated by Sparkbites — extracted from live CSS analysis*
