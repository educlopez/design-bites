# scale.com — Design System

## 1. Visual Theme & Atmosphere

Scale.com is enterprise AI infrastructure, and its design language communicates exactly that: controlled power. The aesthetic is dark, geometric, and slightly futuristic — a site that would feel at home in a Bloomberg terminal crossed with a high-end data center. Deep navy and near-black surfaces create a sense of weight and seriousness befitting a company that processes AI training data at industrial scale.

What distinguishes Scale from generic dark enterprise design is its typographic ambition. The pairing of **Aeonik** (custom geometric display) with **Inter** (functional body) and **Geist Mono** (code/data) creates three clearly differentiated registers. Headings use Aeonik at weights as light as 300 — a counterintuitive choice that reads as confident restraint rather than weakness. When you are Scale, you don't need to shout.

---

## 2. Color Palette & Roles

**Surfaces**
- `#000000` / `rgb(2, 2, 2)` — Primary dark canvas and body background
- `rgb(2, 26, 51)` — Deep navy; dark section panels (near-black with blue cast)
- `rgb(31, 78, 152)` — Mid-blue; secondary section backgrounds and accents
- `rgb(9, 9, 11)` — Near-black surface variant

**Text**
- `#FFFFFF` — Primary text on dark surfaces
- `rgb(163, 163, 163)` — Muted body copy, secondary content
- `rgb(115, 115, 115)` — Tertiary metadata and captions

**Brand Accents**
- `rgb(254, 131, 0)` — Scale orange; primary CTA color, logo accent — a high-energy signal on dark surfaces
- `rgb(0, 112, 243)` — Interactive blue; links and interactive states
- `rgb(17, 24, 39)` — Near-black with slight warm cast; card surfaces

**Borders / Dividers**
- `rgb(38, 38, 38)` — Subtle dark border (near-invisible on black, visible on slightly lighter surfaces)
- `rgba(255, 255, 255, 0.1)` — Translucent white borders for glass-effect dividers

---

## 3. Typography Rules

Scale uses a deliberate three-tier typeface system, each with a distinct job:

**Aeonik** (display) — A custom geometric sans used for all major headings. At 72px/weight 300 for h1, it achieves a rare quality: monumental scale without aggression. Large headlines carry `-1%` letter-spacing (negative, tightening at display sizes). Used up to 89px for the largest display variants.

**Inter** (functional) — The workhorse for body copy, navigation, small headings, and UI labels. At 16px/400 for body, 18px/500 for h4 — Inter handles everything that needs to be reliably read quickly.

**Geist Mono** (data/code) — Referenced in CSS custom properties as a monospace option. Used for code samples, metrics, and any quantitative display where tabular alignment matters.

- **h1**: Aeonik / 72px / weight 300 / `letter-spacing: -1%`
- **h3**: Aeonik / 89px / weight 300 / `letter-spacing: -0.89px` (hero variant)
- **h2**: Inter / 16px / weight 400 (section labels, not visual headings)
- **h4**: Inter / 18px / weight 500
- **body**: Inter / 16px / weight 400 / `line-height: 24px`

The use of light (300) weight for massive display text is a signature choice — it signals mathematical precision over blunt force.

---

## 4. Component Stylings

**Primary CTA buttons**: The Scale orange (`rgb(254, 131, 0)`) appears as the dominant CTA color — maximum energy against dark backgrounds. Pill-shaped (`border-radius: 9999px`).

**Navigation**: Fixed header at 67px height (`--zeitgeist-header-height`). Dark surface, transparent or dark background, keeping the view consistent.

**Cards**: Dark surfaces (`rgb(17, 24, 39)`) with barely-visible borders (`rgb(38, 38, 38)`). Subtle translucent white borders create glass-like panel divisions. No heavy drop shadows — depth through color stratification.

**Data displays**: Geist Mono for metrics and code. Monospace elements are likely tabular and precisely spaced.

**Border radii**: Minimal — primarily `9999px` for pill elements. The majority of layout elements appear to use sharp or barely-rounded corners, reinforcing the precise/technical aesthetic.

---

## 5. Layout Principles

Scale.com operates at enterprise content density — a long-scrolling page with full-bleed section backgrounds that each tell a chapter of the story. Sections shift from deep navy to near-black to mid-blue, creating visual chapters without navigation.

The layout is wide-canvas: content likely spans to large viewport widths given the enterprise audience (primarily desktop). The `--zeitgeist-header-height: 67px` is a small, efficient navigation bar — the product sells itself, not the navigation.

Breakpoints detected at 600, 700, 768, 900, 1000, 1280, 1300px — a thorough ladder suggesting the site adapts carefully across device classes, though the primary experience is clearly optimized for large displays.

---

## 6. Depth & Elevation

Scale achieves depth through chromatic layering on a dark foundation. Pure black gives way to near-black (`rgb(9,9,11)`), then deep navy (`rgb(2,26,51)`), then mid-blue (`rgb(31,78,152)`) — a Z-axis of increasing luminance that reads as background receding to foreground.

Translucent white borders (`rgba(255,255,255,0.1)`) suggest frosted glass card dividers. Box shadows, if present, would be dark-on-dark — subtle glows or inset shadows rather than the drop-shadow patterns common on light-mode sites.

---

## 7. Do's and Don'ts

**Do**
- Layer dark surfaces: pure black → near-black → deep navy → mid-blue
- Use Aeonik at light weights for display — weight 300 is a feature, not a mistake
- Reserve orange exclusively for primary CTAs and the logo mark
- Use Inter for all functional UI text; never use Aeonik at small sizes
- Apply tight negative letter-spacing only at display sizes (72px+)

**Don't**
- Use heavy font weights (600+) for display text — the design relies on light/thin elegance
- Add warm or colorful backgrounds — every surface should read as dark and focused
- Mix Geist Mono into prose contexts — keep it for data, code, and metrics only
- Use rounded corners beyond pill-shaped CTAs — most surfaces are sharp

---

## 8. Responsive Behavior

The seven-breakpoint scale (600 → 1300px) shows intentional adaptation at each tier. The site likely collapses its multi-column feature grid to a stacked layout at 768px and below. The header height is defined via CSS custom property, suggesting it may adjust or collapse to a hamburger menu at mobile.

At 1280–1300px+, full multi-column layouts with large Aeonik display text are the intended experience. The design degrades gracefully but is fundamentally a large-screen product.

---

## 9. Agent Prompt Guide

> "Design in the style of scale.com: dark enterprise aesthetic — pure black canvas, deep navy `rgb(2,26,51)` and mid-blue `rgb(31,78,152)` section layers. Scale orange `rgb(254,131,0)` for primary CTAs only. Aeonik at weight 300 for massive display text (72–89px), Inter for all body. Geist Mono for data. Translucent white borders for glass-panel effects. No warm tones, no illustrations — precision, scale, and restrained power."

---

*Generated by Sparkbites — extracted from live CSS analysis*
