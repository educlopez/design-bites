# harshitbeni.com — Design System

## 1. Visual Theme & Atmosphere

Harshit Beniwal's portfolio is a Framer-built showcase that treats color as its primary storytelling device. The base is a cool light gray (`rgb(243, 244, 246)`) — a near-invisible neutral that stays out of the way. Against this quiet backdrop, a collection of vivid, pure-hue color blocks announce each project: purple, gold, orange, green, sky blue, red. The effect is a bento-grid of energy, each tile radiating its own personality.

There is no attempt at a monochromatic or tonal palette. The design philosophy is additive — bring in the colors, let each one claim space, trust the layout to give them order. The overall impression is playful confidence: a designer who knows how to handle color without letting it become chaos.

The typography is minimal to the point of being anonymous — Inter at small sizes, system sans-serif as fallback — which is intentional. The type steps aside so the color work and project visuals can dominate. The UI chrome is nearly invisible.

---

## 2. Color Palette & Roles

**Base**
- Light gray `rgb(243, 244, 246)` — page background, header background (at 80% opacity for blur/frosted effect)
- Slightly darker gray `rgb(229, 231, 235)` — subtle surface variant
- Medium gray `rgb(209, 213, 219)` — borders and dividers

**Project Color Blocks** (the visual identity)
- Electric purple `rgb(93, 64, 245)` — bold, primary project card
- Gold/amber `rgb(234, 174, 8)` — warm accent project
- Burnt orange `rgb(223, 128, 63)` — earthy warm project
- Mint green `rgb(85, 177, 134)` — calm, natural project
- Sky blue `rgb(73, 169, 248)` — light, airy project
- Coral red `rgb(219, 84, 78)` — energetic, urgent project

**Interactive**
- Electric blue `rgb(16, 98, 255)` — primary CTA link (`.framer-NgNdV`)
- Browser-default link blue `rgb(0, 0, 238)` — link color for standard anchor elements (unoverridden)

**Buttons**
- Dark translucent `rgba(0, 0, 0, 0.86)` — showreel/play button
- White `rgb(255, 255, 255)` — resume/secondary button

**Surfaces**
- `rgba(255, 255, 255, 0.6)` — frosted white overlay (for layered panels)
- `rgba(0, 0, 0, 0.16)` — dark overlay for modal-like contexts

---

## 3. Typography Rules

Typography is intentionally understated — the design was built in Framer where visual components dominate, and text serves a purely functional role.

**Inter** — primary display font (where specified)
- Paragraphs/labels: `12px` / `600` / `16px` line-height — tight, small, badge-like

**System sans-serif** — fallback for most elements
- Body: `12px` / `400` / `normal` — extremely compact; the site operates at a small type scale
- Links, buttons, navigation: all at `12px` / `400`

What's absent: no display serif, no large-scale headline treatment, no monospace. The site does not use type as a brand statement — the color blocks carry that responsibility. There are no text transforms, no tracked letter-spacing, no typographic hierarchy beyond bold/regular.

**Note:** The 12px base size is notably small for body text. It works in the context of a visually-dense bento layout where labels are secondary to image/color content.

---

## 4. Component Stylings

**Navigation / Header**
- Sticky header: `rgba(243, 244, 246, 0.8)` — frosted glass against the light gray page
- Padding: `24px 16px` — comfortable mobile-first spacing
- Nav links: browser-default blue with translucent hover fill (`rgba(236, 237, 240, 0.53)`)

**Project Color Tiles**
- Full-bleed color fills with no border, no shadow on the tile itself
- Large border radii: `32px`, `36px`, `40px` — very rounded, almost squircle-shaped
- Avatar/circle elements at `50%` radius

**Buttons**
- Showreel button: dark near-black `rgba(0,0,0,0.86)` with subtle shadow `rgba(0,0,0,0.2) 0 1px 2px`
- Resume button: white with minimal shadow `rgba(0,0,0,0.03) 0 1px 2px`
- Both use the small `4px` or `6px` radius
- No hover states defined — Framer handles hover via its own motion system

**Cards / Bento Items**
- Shadows: `rgba(0,0,0,0.2) 0 1px 2px, rgba(0,0,0,0.12) 0 1px 2px -1px` — subtle, ground-level lift
- Secondary card shadow: `rgba(0,0,0,0.03) 0 1px 2px-1px, rgba(0,0,0,0.05) 0 1px 2px` — barely perceptible

**Footer**
- `120px` top padding — dramatic separation from content

---

## 5. Layout Principles

Built with Framer's native layout engine, the site uses a bento-grid aesthetic: irregular tile sizes, each with its own color, assembled into a cohesive page. The main content has `0px` gap, meaning items sit flush or Framer's layout system manages spacing internally.

Sections have `60px 16px 80px` padding — generous vertical breathing room, mobile-friendly horizontal gutters. The 16px side padding is intentionally narrow, letting content reach close to the viewport edge for a more immersive feel on small screens.

The layout is not a standard responsive grid — it's a designed composition where each tile's size and position is defined visually in Framer, then rendered as fixed coordinates at each breakpoint.

---

## 6. Depth & Elevation

Depth is minimal by design — the color contrast between tiles provides inherent separation without relying on shadows.

- **Tile shadows**: `rgba(0,0,0,0.2) 0 1px 2px` — just enough to separate tiles from the background
- **Glass headers**: frosted opacity (`0.8`) provides perceived depth through transparency
- **Overlay surfaces**: `rgba(255,255,255,0.6)` for layered panels — suggests content floating over the color tiles

No dramatic elevated shadows, no blur-heavy glass. The design is flat by default, with color doing the work that shadow would otherwise do.

---

## 7. Do's and Don'ts

**Do:**
- Use the light gray `rgb(243, 244, 246)` as the neutral base — it's warm enough to not feel clinical
- Let project tiles define their own bold color identity — no enforcing a unified palette on content
- Apply very large border radii (32–40px) to color tiles for the Framer-portfolio squircle feel
- Keep typography minimal and small — type is functional, color is expressive
- Use frosted glass (`rgba(243, 244, 246, 0.8)`) for sticky navigation headers

**Don't:**
- Don't bring the browser-default link blue into custom components — override with `rgb(16, 98, 255)` at minimum
- Don't add heavy drop shadows — the color tiles create their own visual weight
- Don't use the project colors (`purple, gold, orange`) as text or background outside their designated tiles
- Don't scale type up aggressively — the small type is a stylistic choice, not a limitation
- Don't replicate the 12px system size in a text-heavy product — this scale works for a visual portfolio only

---

## 8. Responsive Behavior

Framer handles responsive layout at six breakpoints (`719.98, 720, 809, 810, 1199, 1199.98px`) — notably pairs of values just above/below thresholds, suggesting pixel-perfect breakpoint control. At mobile, the bento grid likely reflows to a single-column stack.

Section padding `60px 16px 80px` is already mobile-friendly. The header's `24px 16px` padding scales naturally. The big color tiles with `32–40px` radii maintain their character even at narrow widths — if anything, they become more impactful as full-width blocks on mobile.

---

## 9. Agent Prompt Guide

Use this block when prompting an AI to generate UI in the style of harshitbeni.com:

```
Design a visual portfolio in the Framer bento-grid style. Base background is light cool gray (#F3F4F6). Each project gets its own bold color tile: choose from electric purple (#5D40F5), gold (#EAA608), burnt orange (#DF803F), mint green (#55B186), sky blue (#49A9F8), or coral red (#DB544E). Tiles use very large border radii (32–40px). Typography is small and functional — Inter at 12px/600 for labels, system sans-serif for navigation. Navigation header uses frosted glass (background-color at 80% opacity of the page color). Shadows are minimal: 0 1px 2px with very low opacity. No gradients, no dark mode. Framer Motion animates tile reveals on scroll. CTAs use near-black (#000000CC) or white fills with subtle shadows.
```

---

*Generated by Sparkbites — extracted from live CSS analysis*
