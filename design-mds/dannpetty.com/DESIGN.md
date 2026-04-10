# DESIGN.md — dannpetty.com

## 1. Visual Theme & Atmosphere

Dann Petty's personal site is a statement of confident minimalism operating in full dark mode. The canvas is near-black — not pure, but a dark charcoal that feels rich and intentional. Against this ground, a single electric lime-yellow accent explodes with deliberate maximum contrast. The palette feels like a designer who understands that restraint plus one bold move creates more impact than many competing colors. The site communicates personality through scarcity: tight Framer Motion animations, a compressed type scale, and almost no decorative surface work. The overall mood is confident, direct, and a little editorial.

---

## 2. Color Palette & Roles

### Background
- **Deep Charcoal** (`rgb(17, 17, 17)` = `#111111`): The primary canvas. Not black — there is just enough visible distinction from pure black to feel intentional rather than default.

### Accent / Highlight
- **Acid Lime** (`rgb(206, 251, 80)` = `#cefb50`): The defining brand color. Used as a surface for a primary highlight card or CTA zone. Luminance 0.855 — extremely bright against the dark ground, designed to create immediate visual hierarchy.

### Neutral Light
- **Light Gray** (`rgb(242, 242, 242)` = `#f2f2f2`): A near-white surface appearing on secondary cards or lighter content zones. Provides visual contrast against the dark ground without introducing full white.

### Text
- **Near-Black Text** (`rgb(0, 0, 0)` = `#000000`): Default text color set on the body — paradoxical on a dark background, suggesting text is placed on light surface areas. Link text inherits browser default blue (`rgb(0, 0, 238)`), signaling raw or lightly styled interactive elements.

---

## 3. Typography Rules

Two variants of Inter handle all type:

**Inter Tight** (28px, weight 700, 33.6px line-height): The display/heading typeface variant. The "Tight" variant's compressed tracking suits dark editorial layouts — headlines are dense and confident.

**Inter SemiBold** (16px, weight 600, 22.4px line-height): Sub-headings and prominent UI labels. Slightly tighter than standard Inter.

**Inter** and fallback sans-serif: Body copy at 14px weight 600 (tight labels) and generic sans at 12px for the smallest UI text. The scale is compact: 28 / 16 / 14 / 12.

Notably absent: no serif, no display typeface, no monospace. The system is a single-family grid of weights and sizes. No letter spacing overrides. No text transforms. Typography communicates through weight and size alone, not stylistic embellishment.

---

## 4. Component Styling

- **Cards / Surfaces**: Three distinct surfaces: deep charcoal (`#111`), light gray (`#f2f2f2`), and lime-acid (`#cefb50`). Cards are differentiated by surface color rather than shadow or border.
- **Links**: Styled with browser-native blue on hover — intentionally raw, suggesting links are functional landmarks rather than styled CTAs.
- **Hover States**: Navigation links shift background from `#111` to `#202020` — a subtle 6-point lightening that confirms interactivity without disruption.
- **Border Radius**: Two values — `500px` (full pill for badge/tag shapes) and `100px` (large-rounded for cards). There are no sharp corners or tight radii. Shapes are soft and rounded throughout.
- **No shadows**: The shadow array is empty. All elevation is handled by surface color contrast.

---

## 5. Layout Principles

- Breakpoints at 1000, 1200, and 1600px suggest a wide-screen first layout with three major breakpoints.
- Content appears in a grid where the lime surface card creates a focal point — one dominant piece, supporting secondary cards.
- No complex sidebar or navigation drawer. The layout is likely a portfolio-style single page with scrollable sections.
- Spacing is minimal at the root level; gap and layout work is handled within Framer's component containers.

---

## 6. Depth & Elevation

No shadows exist in the system. Depth is entirely achieved through:
- **Color contrast**: Lime (#cefb50) against near-black (#111) creates the highest possible visual pop
- **Surface stacking**: Three defined luminance tiers (0.12 dark, 0.85 lime, 0.95 light gray) form a legible elevation ladder
- **Framer Motion**: Implicit animation handling creates perceived depth through movement rather than shadow

---

## 7. Do's and Don'ts

**Do:**
- Reserve the lime accent for one dominant surface or CTA per section. It loses power if repeated.
- Use Inter Tight Bold for all primary headings. Keep weight at 700.
- Apply large pill radii (100–500px) for all card and tag shapes. Sharp corners are alien to this system.
- Keep hover states subtle: a ~6-point background lightening is sufficient.
- Trust the dark canvas — it does not need ornamentation.

**Don't:**
- Add a second accent color. The system is built on a single chromatic pop.
- Use shadows or drop effects. This is a flat, surface-only elevation system.
- Introduce serif or display typefaces. Inter is the entire typographic palette.
- Use text transforms or letter-spacing overrides.
- Place lime text on light backgrounds — it is a background color, not a text color.

---

## 8. Responsive Behavior

Three breakpoints: 1000, 1200, 1600px. The wide-screen orientation (up to 1600px) suggests a design that opens up horizontally on large displays. Below 1000px, layout likely collapses to single-column. The compact type scale (max 28px) requires minimal responsive adjustment. Framer Motion components handle most fluid transitions.

---

## 9. Agent Prompt Guide

> Design a dark-mode portfolio site matching dannpetty.com: background `#111111`, one dominant lime-acid card (`#cefb50`), secondary near-white surfaces (`#f2f2f2`). Inter Tight Bold at 28px for headings, Inter SemiBold 16px for labels. All shapes use large pill radii (100–500px). No shadows. No gradients. Hover states use a 6-point background lightening only.

---

*Generated by Sparkbites — extracted from live CSS analysis*
