# itsjay.us — Design System

## 1. Visual Theme & Atmosphere

itsjay.us is a personal portfolio that commits entirely to a dark-light duality: a near-black header/navigation shell (oklch dark) wrapping a bright near-white main content area. The effect is cinematic — as if the work lives inside a dark gallery frame. Built on Next.js with Tailwind and using the proprietary **Saans** typeface throughout, the site has a resolved, modern typographic identity. OKLCH color space values signal a contemporary Tailwind v4 setup, where color science takes precedence over legacy hex approximations. The atmosphere is curated and self-assured: a single typeface family at multiple weights, clean transitions, and a shadow system that grounds floating elements.

## 2. Color Palette & Roles

**Dark shell (header, drawer)**
- `oklch(0.205 0 0)` ≈ `rgb(~34, 34, 34)` — dark near-black; body background, header, navigation
- Text on dark: `oklch(0.97 0 0)` ≈ near-white — H3 headings in the dark zone

**Light main content**
- `oklch(0.97 0 0)` ≈ `rgb(~247, 247, 247)` — main content area background; warm near-white
- Text on light: `oklch(0.205 0 0)` — the same dark used as text on light surfaces

**Absent:** no accent color, no brand hue. The chromatic palette is intentionally zero. All meaning is carried by lightness contrast alone.

OKLCH chroma is `0` throughout — perfectly neutral tones. This is deliberate: Saans + neutrals = the work is the color.

## 3. Typography Rules

Saans is used exclusively — for every selector from H2 to buttons. The scale creates hierarchy through weight and size alone, not font switching.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H3 (display) | Saans | 42.24px | 500 | lh 63.36px — 1.5x ratio, airy |
| H2 / body labels | Saans | 16px | 400 | lh 24px |
| H4 (labels) | Saans | 16px | 600 | Uppercase, section markers |
| Body | Saans | 16px | 400 | lh 24px |
| P (meta) | Saans | 14px | 600 | -0.35px tracking, lh 20px — tight label |
| Links | Saans | 16px | 500 | lh 24px |

The H3 at 42.24px with a 63.36px line-height (1.5× ratio) is unusually airy for a display heading — the extra line-height makes it feel like a pulled quote or hero statement rather than a traditional heading. H4 is uppercase and semi-bold — section titling, acting as a navigational landmark.

## 4. Component Stylings

**Cards / Containers** — Border radius `16px` for standard cards, `12px` for tighter elements. The `3.35544e+07px` (≈ infinite) value on some elements means fully rounded pills — likely used for tags or status chips.

**Shadows** — One shadow in use: `rgba(0,0,0,0.25) 0px 25px 50px -12px` — Tailwind's `shadow-2xl`. This large soft shadow on elements within the light main area adds genuine depth, making the work feel elevated off the canvas.

**Dark header frame** — The dark background on body/header with transparent header background creates a persistent dark border at the top, like a matte frame around the content.

**Interactive states** — Buttons use Saans at 16px/400. No hover color changes detected — transitions are likely opacity or transform-based.

## 5. Layout Principles

No CSS breakpoints detected in the data. This either means breakpoints are managed entirely through Tailwind responsive classes (common in Tailwind v4), or the layout is intentionally fixed-width. The dark/light split is structural: the dark shell wraps the lighter content panel, creating a framed composition at any width.

Spacing is Tailwind-standard with no custom spacing tokens.

## 6. Depth & Elevation

The depth model is architectural rather than shadow-based:
- **Dark frame** (oklch 0.205) anchors the periphery
- **Light content** (oklch 0.97) floats as the focal plane
- **shadow-2xl** (`rgba(0,0,0,0.25) 0px 25px 50px -12px`) lifts selected content cards above the light plane

Three layers: dark frame → light surface → elevated card. Simple, resolved, and effective.

## 7. Do's and Don'ts

**Do**
- Use Saans exclusively — font switching destroys the singular typographic voice
- Apply oklch color values; the zero-chroma neutrals are precise and intentional
- Use shadow-2xl for any element meant to "float" above the main content surface
- Make H4 uppercase with weight 600 for section markers; it distinguishes wayfinding from content

**Don't**
- Introduce a brand color — the achromatic palette is the aesthetic position
- Reduce the H3 line-height (1.5×); the airyness is intentional, not an error
- Use warm greys or tinted surfaces; oklch(x 0 0) is chrominance-zero by design
- Add more than one shadow depth level — the single shadow-2xl is sufficient

## 8. Responsive Behavior

No explicit CSS breakpoints detected; Tailwind responsive classes handle reflow. The dark/light split persists across widths — it's a structural concept, not a viewport-dependent layout. On mobile, the dark frame likely becomes a dark top bar; the main content fills the viewport below. The 42.24px H3 display heading may need a smaller step on narrow screens.

## 9. Agent Prompt Guide

> Build a personal portfolio with a dark-frame / light-content split in the style of itsjay.us. Use oklch neutrals only: dark near-black `oklch(0.205 0 0)` for the outer shell, near-white `oklch(0.97 0 0)` for the main content area. Saans typeface throughout, no font mixing. H3 display: 42.24px/500 with 1.5× line-height. H4 section labels: uppercase, 16px/600. Cards use `border-radius: 16px` and `box-shadow: rgba(0,0,0,0.25) 0px 25px 50px -12px`. No accent color. Tailwind v4 setup, OKLCH color space.

---

*Generated by Sparkbites — extracted from live CSS analysis*
