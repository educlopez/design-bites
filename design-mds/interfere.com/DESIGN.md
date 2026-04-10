# interfere.com — Design System

## 1. Visual Theme & Atmosphere

Interfere.com inhabits the high-end editorial end of white-background SaaS design — the kind of site that would pass for a premium magazine if the copy were fiction. Built on Next.js with Tailwind, it distinguishes itself through typographic duality: InterVariable for the functional contemporary voice and HeldaneText (a serif) reserved specifically for blockquotes. This typographic counterpoint signals intellectual seriousness. The palette is nearly monochromatic white with body text at `rgba(0,0,0,0.875)` — not quite full black, a deliberate softening that prevents harshness. A light footer `lab(96.868 -0.0000298023 0)` (near white with imperceptible warmth) provides grounding without darkness.

## 2. Color Palette & Roles

**Surface**
- `rgb(255, 255, 255)` — primary canvas
- `rgb(252, 252, 252)` — secondary surface; near-white with microscopic differentiation
- `lab(96.868 -0.0000298023 0)` — footer background; a perceptually uniform near-white

**Text**
- `rgba(0, 0, 0, 0.875)` — primary text at 87.5% opacity; softer than pure black
- `rgba(0, 0, 0, 0.608)` — secondary / muted text; nav links, button labels at rest
- Hover on muted text → `rgba(0, 0, 0, 0.875)` — opacity increase as interaction cue

**Data visualization accents** (present as transparent washes)
- `rgba(0, 192, 64, 0.016)` — near-invisible green tint
- `rgba(0, 163, 47, 0.043)` — green wash
- `rgba(0, 143, 74, 0.81)` — solid green indicator
- `rgba(223, 38, 0, 0.82)` — solid red indicator
- `rgba(255, 32, 0, 0.03)` — ghost red wash

These suggest a live data/chart component where green/red encode positive/negative values — the only color in an otherwise achromatic design.

## 3. Typography Rules

The pairing of InterVariable and HeldaneText is the design's most opinionated choice. InterVariable handles everything functional; HeldaneText (serif) handles the reflective or quoted.

| Role | Font | Size | Weight | Letter-spacing | Notes |
|---|---|---|---|---|---|
| H1 | InterVariable | 56px | 500 | -0.56px | lh 56px — 1:1 |
| H3 | InterVariable | 24px | 500 | -0.24px | lh 32px |
| Body / H2 | InterVariable | 15px | 400 | normal | lh 24px |
| P (small) | InterVariable | 13px | 500 | normal | lh 20px |
| Blockquote | HeldaneText | 28px | 400 | -0.28px | lh 36px — serif editorial |
| Buttons | InterVariable | 15px | 400 | normal | — |

The H1 at 56px with 1:1 line-height and -0.56px tracking compresses tightly — headlines sit as dense blocks. The muted-to-full opacity hover on nav links is the interaction system without any color involvement.

## 4. Component Stylings

**Links / Nav** — Default at `rgba(0,0,0,0.608)`, hover to `rgba(0,0,0,0.875)`. Pure opacity shift. No underlines, no color change — interaction exists only in weight of presence.

**Cards / Surfaces** — `border-radius: 6px` standard, `8px` and `12px` for larger containers, `16px` for pill-adjacent shapes. All backed by white or near-white — no dark card variants.

**Inset shadow system** — `rgba(0,0,0,0) 0px 0px 0px 0.5px inset` plus `rgba(0,0,0,0.06) 0px 0px 0px 0.5px` creates a hairline border effect through shadow layering rather than `border` properties. Technically precise and renders crisply.

**Data indicators** — Colored bars or pills using green/red at high opacity (`0.81`, `0.82`) against the white canvas for clear semantic encoding.

## 5. Layout Principles

A single breakpoint at `600px` — strikingly minimal for a Next.js/Tailwind site. This suggests the design is primarily a desktop experience with a minimal mobile adaptation, rather than a mobile-first build. Content is left to reflow naturally between 600px and desktop widths. Tailwind's grid system at desktop likely uses 12-column grids. Section padding is zeroed in CSS (Tailwind utility classes carry all spacing).

## 6. Depth & Elevation

Almost entirely flat. The hairline inset shadow (`0.5px`) is the subtlest possible elevation signal — it renders as a drawn border rather than a shadow. The luminance range is compressed:

- `luminance 1.0` — white surfaces
- `luminance 0.988` — near-white variant
- `luminance 0.471` / `0.396` — transparent green/red washes (data vis)
- `luminance 0.0` — `rgba(0,0,0,0.875)` overlay for dark modal or tooltip layer

No drop shadows on structural elements. Elevation is expressed through containment and the hairline border technique.

## 7. Do's and Don'ts

**Do**
- Use `rgba(0,0,0,0.875)` for primary text — full black is too harsh for this register
- Reserve HeldaneText exclusively for blockquotes; don't let the serif bleed into UI
- Apply the opacity-shift pattern for interactive states: `0.608` → `0.875` on hover
- Use the hairline inset shadow `rgba(0,0,0,0.06) 0px 0px 0px 0.5px` as your border system

**Don't**
- Add colored accents beyond the data-vis green/red; the achromatic palette is the identity
- Use `border` properties for card outlines — the shadow-based hairline is the technique
- Introduce the serif at body scale — HeldaneText belongs only in blockquote context
- Over-engineer breakpoints; the single `600px` breakpoint is a feature, not an oversight

## 8. Responsive Behavior

One breakpoint at `600px`. Below 600px: likely single-column stack with full-width sections. The H1 at 56px may need a `clamp()` or size step at mobile to prevent overflow on narrow screens — this appears to be handled through Tailwind responsive prefixes rather than CSS custom properties. The hairline shadow border technique renders correctly at all densities.

## 9. Agent Prompt Guide

> Build a premium editorial SaaS landing in the style of interfere.com. White background. Primary text at `rgba(0,0,0,0.875)`, secondary/nav at `rgba(0,0,0,0.608)` with hover transition to full opacity. InterVariable for all UI type: H1 56px/500 with 1:1 line-height, body 15px/400. HeldaneText serif at 28px/400 exclusively for blockquotes. No colored brand accents — only green/red at high opacity for data indicators. Cards use `border-radius: 6–8px` with hairline borders via `box-shadow: rgba(0,0,0,0.06) 0px 0px 0px 0.5px`. One breakpoint at 600px. Flat surfaces throughout.

---

*Generated by Sparkbites — extracted from live CSS analysis*
