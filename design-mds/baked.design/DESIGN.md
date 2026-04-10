# baked.design — Design System Reference

## 1. Visual Theme & Atmosphere

baked.design is a Framer-built agency site with a deliberately confident, editorial character. The palette sits between corporate polish and dark creative — near-black backgrounds anchor the brand, punctuated by a deep navy accent block and crisp white content surfaces. The overall mood is focused and premium, projecting trustworthiness without coldness. Motion (Framer Motion) is present but restrained; the site moves to guide attention, not to entertain. There are no gradients, no illustrative decorations. Typography leans into tight negative tracking for a compressed, modern headline feel. The absence of custom CSS properties signals a Framer-native build — everything is composed through Framer's visual layer rather than a token-driven system.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Page background | `rgb(23, 23, 23)` | Body / dark sections |
| Near-black surface | `rgb(33, 33, 33)` | Secondary dark cards |
| Dark card | `rgb(84, 84, 84)` | Mid-tone surfaces, dividers |
| Content surface | `rgb(255, 255, 255)` | Cards, light sections |
| Off-white | `rgb(250, 250, 250)` | Subtle panel fill |
| Warm light | `rgb(242, 241, 237)` | Feature backgrounds |
| Brand accent | `rgb(37, 84, 138)` | CTA blocks, highlight sections |
| Link / interactive | `rgb(0, 0, 238)` | Default browser-blue links |

The palette is essentially two-temperature: dark (near-black) and light (white/off-white), bridged by the navy accent. No warm or saturated hues appear outside the accent block. The browser-default link blue (`rgb(0, 0, 238)`) is a deliberate choice — raw and unrefined, echoing a web-native confidence.

## 3. Typography Rules

**Primary typeface:** Inter Display (with Inter Display Placeholder fallback) — a high-fidelity variable display cut optimised for large sizes.

**Body fallback:** `sans-serif` (system default) — used for base-level UI, suggesting inter is loaded only for editorial content.

| Level | Size | Weight | Tracking | Line Height |
|-------|------|--------|----------|-------------|
| Display / paragraphs | 24px | 400 | −0.9px | 28px |
| Body UI | 12px | 400 | normal | normal |

The tight −0.9px letter-spacing on 24px text is the defining typographic gesture — it compresses the Inter Display letterforms into a dense, confident headline rhythm. No uppercase transforms, no variable weights beyond regular. What's absent is notable: no declared heading hierarchy (h1–h6), no weight variation — Framer builds visual hierarchy through size and positioning, not CSS selectors.

## 4. Component Stylings

**Buttons / CTAs:** White background with browser-blue text and border. Pill shapes appear via `99px` and `999px` border radii. No hover states detected in CSS — Framer handles hover transforms in its own layer.

**Cards:** Rounded at `24px` or `12px`. Light surfaces (`#fafafa`, `#f2f1ed`) against the dark page. Minimal borders.

**Nav / links:** Transparent background, browser-blue text. Focus state adds a `rgb(0, 95, 204) auto 1px` outline — accessible but default-browser styled.

**Chip / tag elements:** `4px` radius for small inline components.

## 5. Layout Principles

Built entirely in Framer's absolute/relative canvas model. Breakpoints at **809.98px** and **1199.98px** define three tiers: mobile (<810px), tablet (810–1199px), desktop (≥1200px). Spacing is Framer-generated — no CSS custom property scale exists. Sections stack vertically with no detected gap/padding patterns at the CSS level; all composition happens in Framer's visual layer. Content width feels generous on desktop with full-bleed dark sections anchoring the page rhythm.

## 6. Depth & Elevation

Shadowless. No `box-shadow` values are present anywhere in the extracted data. Elevation is communicated entirely through **color contrast** — dark page vs light cards creates the sense of lift. The navy accent block (`rgb(37, 84, 138)`) reads as the highest-emphasis surface simply by being the only chromatic element. Z-index layering exists in Framer's component tree but is not surfaced as CSS custom properties.

## 7. Do's and Don'ts

**Do:**
- Use near-black (`#171717`) as the default page canvas for dark sections
- Apply tight negative tracking (−0.9px) on Inter Display at 24px+ sizes
- Use the navy accent (`#25548A`) sparingly — one section, one CTA
- Keep border radii generous (24px, 99px) for primary interactive elements
- Let color contrast do the heavy lifting — avoid decorative shadows

**Don't:**
- Introduce gradients or textured backgrounds — the system is flat and intentional
- Use the browser-default link blue as the only interactive affordance on dark backgrounds (contrast fails)
- Add weight variation beyond regular (400) — this system relies on size, not weight, for hierarchy
- Override Framer's motion layer with CSS animations — duplication creates jank

## 8. Responsive Behavior

Three breakpoints: **mobile** (<810px), **tablet** (810–1199px), **desktop** (≥1200px). Layout reflow is managed by Framer's responsive variants — not CSS Grid or Flexbox media queries. Text scaling is not fluid (no `clamp()` detected); sizes are fixed per breakpoint. Expect column-to-stacked transitions at the 810px threshold.

## 9. Agent Prompt Guide

> "Design in the style of baked.design: dark near-black canvas (`#171717`), white card surfaces, a single navy accent block (`#25548A`). Use Inter Display at 24px with −0.9px letter-spacing for all headline text. Pill-shaped CTAs (border-radius: 99px) with white fill and browser-blue label. No shadows — elevation through color contrast only. Framer Motion for subtle entrance animations. Three-column desktop layout collapses at 810px."

---

*Generated by Sparkbites — extracted from live CSS analysis*
