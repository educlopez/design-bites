# higgsfield.ai — Design System

## 1. Visual Theme & Atmosphere

Higgsfield.ai occupies the aggressive end of AI-product dark design — a near-black canvas punctuated by electric chartreuse, the kind of neon accent that reads as computational power made visible. The atmosphere is cinematic and tech-forward: deep voids of `rgb(15, 17, 19)` create depth, while `rgb(209, 254, 23)` flashes like a monitor refresh. It's a site that wants to feel like a tool that's already running. The footer inverts the palette entirely — bright lime on near-black — as if the interface acknowledges its own energy at the bottom. Uppercase headings reinforce the commanding, machine-like tone.

## 2. Color Palette & Roles

**Background / Canvas**
- `#0f1113` (`rgb(15, 17, 19)`) — primary page background, near-black with a cool tint
- `#1c1e20` (`rgb(28, 30, 32)`) — card/module surfaces
- `#131517` (`rgb(19, 21, 23)`) — deepest inset panels

**Accent / Signal**
- `#d1fe17` (`rgb(209, 254, 23)`) — primary brand accent; CTA highlights, header icon tint, footer background
- `rgba(209, 254, 23, 0.1)` — ghost badge background with lime tint

**Secondary Accents**
- `rgb(237, 21, 114)` — hot pink used sparingly for visual interruption
- `rgb(31, 155, 197)` — blue inset highlight on specific interactive surfaces

**Text**
- `#f7f7f8` (`rgb(247, 247, 248)`) — primary body text on dark
- `#ffffff` — links and headings at full contrast
- `rgb(20, 21, 26)` — text reversed on the lime footer

**Danger/Status**
- `rgba(230, 72, 61, 0.15)` — low-opacity error surface

## 3. Typography Rules

The type system pairs **Space Grotesk** (headings) with the system sans-serif stack for body. All headings are uppercase — this is not a stylistic suggestion but a core brand rule enforced via `text-transform: uppercase`.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H2 | Space Grotesk | 36px | 700 | Uppercase, lh 40px |
| H3 | Space Grotesk | 16px | 700 | Uppercase, tight tracking `-4%` |
| Body | System sans-serif | 16px | 400 | lh 24px |
| Small / UI | System sans-serif | 14px | 400–500 | lh 20px |
| Dialogs | Inter | 14px | 400 | lh 24px |

No serif. No display type. The system-sans fallback for body text signals confidence — the brand doesn't need a premium font everywhere, Space Grotesk carries the identity.

## 4. Component Stylings

**Buttons** — Borderless by default. The lime CTA uses glow shadows `rgba(209, 254, 23, 0.48)` as focus ring, not a border. Primary action buttons sit on the near-black surface without outlines.

**Cards / Panels** — Rounded at `8px`, `12px`, `14px`, and `16px` — a loose scale suggesting iteration rather than rigid system. Dark surface `rgb(46, 48, 49)` for card bodies.

**Badges** — Pill shape (`border-radius: 3.35544e+07px` ≈ fully round), lime tint background, lime text.

**Toasts** — React Toastify configured with white background (`#fff`) and standard semantic colors; these are app-layer UI, not marketing layer.

**Inset shadows** — Used for button depth: `rgba(0,0,0,0.43) 0px -3px 0px 0px inset` gives buttons a pressed-bottom feel.

## 5. Layout Principles

Narrow breakpoints at **440px** and **480px** only — this is effectively a two-mode layout: mobile and everything else. Content lives in a single-column centered flow on mobile, expanding to wider editorial grids on desktop. The lack of a mid-range tablet breakpoint suggests the design was conceived desktop-first with a minimal mobile adaptation.

Spacing is Tailwind-standard, no custom CSS variables for spacing. Sections use generous vertical breathing room driven by padding classes.

## 6. Depth & Elevation

Depth is achieved through **luminance contrast**, not shadows. The surface stack reads:
- `luminance 0.84` — lime accent panels
- `luminance 0.186` — card bodies
- `luminance 0.116` — hover/transition surfaces
- `luminance 0.081` — deepest panels
- `luminance 0.067` — overlay scrim `rgba(17,17,17,0.5)`

Shadows are reserved for interactive feedback (focus glow on buttons) and the pink accent block (complex inset + drop combination). The dark-mode-first design means elevation is read as lightness, not shadow.

## 7. Do's and Don'ts

**Do**
- Use `#d1fe17` only for one element per viewport — its power comes from scarcity
- Apply `text-transform: uppercase` to all Space Grotesk headings
- Pair lime with near-black (`#131517`) for maximum contrast
- Use border-radius `8–16px` for cards; pill (`9999px`) only for badges/tags

**Don't**
- Introduce warm neutrals or beige — the cool near-black palette is deliberate
- Use Space Grotesk in lowercase for headings — it loses brand character
- Add drop shadows on dark cards — use luminance steps instead
- Overuse the hot pink `rgb(237, 21, 114)` accent; it's a surprise, not a system color

## 8. Responsive Behavior

Two breakpoints only: `440px` and `480px`. The design collapses to a single-column stack below 440px. Navigation likely converts to a drawer or hidden state. Typography scale does not appear to step down with clamp — sizes are fixed, implying the layout reflows content rather than rescaling type.

No mid-range breakpoints means tablet visitors see the desktop layout from 481px upward — acceptable for a landing/marketing page but worth monitoring for 768px viewports.

## 9. Agent Prompt Guide

> Build a dark AI-product landing page in the style of higgsfield.ai. Use a near-black background (`#0f1113`), electric chartreuse accent (`#d1fe17`) applied to exactly one focal element per section. All headings in Space Grotesk, uppercase, bold. Body in system sans-serif. Cards use `border-radius: 12px` with surface color `rgb(46, 48, 49)`. Lime badges are fully rounded pills with `rgba(209, 254, 23, 0.1)` fill. Button focus states use lime glow shadow, not a border. Footer inverts: lime background with dark text. Only two breakpoints: 440px and 480px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
