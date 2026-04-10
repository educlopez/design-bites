# imagine.dev — Design System

## 1. Visual Theme & Atmosphere

Imagine.dev presents a rare design posture in the developer tools space: confident restraint. Where most dev-tool sites reach for drama through dark themes and neon accents, imagine.dev uses a warm off-white background (`rgb(238, 238, 241)`) and an extremely tight greyscale palette. The atmosphere is quiet, focused, and typographically precise — closer to a well-designed print publication than a software landing page.

Built in **Svelte**, the site is leaner and more intentional than most. Every element earns its place. The choice of **Neue Haas Grotesk Display** — a premium, historically significant grotesque — at featherweight `200` across nearly every element signals extreme typographic confidence. Light weights in premium typefaces are harder to execute well; they require precise spacing and sizing. Here, they work.

The dark footer anchoring an otherwise light page creates clear structural closure. The contrast between the warm-grey canvas and the near-black (`rgb(24, 24, 27)`) footer and primary text is intentional and studied.

## 2. Color Palette & Roles

**Background / Canvas**
- `rgb(238, 238, 241)` — Primary page background; warm grey with a hint of blue — not paper white, not cool grey
- `rgb(255, 255, 255)` — Card/panel surfaces within the canvas
- `rgb(237, 237, 240)` / `rgb(215–217, 215–217)` — Dividers and subtle surface variants

**Text / Foreground**
- `rgb(24, 24, 27)` — Near-black; primary text, footer background, borders
- `rgb(172, 172, 175)` — Muted/secondary text; labels and captions
- `rgb(238, 238, 241)` — Light text on dark backgrounds (footer, dark cards)

**Interactive / Component**
- `rgb(244, 244, 247)` — Button default background (light mode buttons)
- `rgb(156, 163, 175)` / `rgb(85, 85, 85)` — Progress indicators, muted UI elements

**Absent:** No accent colour whatsoever. No brand colour, no blue, no green, no highlight. This is an intentional commitment to pure greyscale as a system.

## 3. Typography Rules

**Neue Haas Grotesk Display** is the singular typeface throughout. No fallback beyond the generic `sans-serif`. This is a high-confidence, font-loaded stack — the entire typographic personality depends on this font loading.

**Scale — near-universal weight 200**
- H1: 60px / 200 weight / 64px line-height / −1.5px tracking — graceful display type, light as air
- H2: 24px / 200 weight / 32px line-height — deliberately delicate for a section header
- H3: 14px / 200 weight / 20px line-height — micro, used for labels or sub-categories
- Body: 16px / 200 weight / 24px line-height
- Paragraphs: 14px / **500 weight** / 19.25px line-height — the lone exception; paragraphs use medium weight for readability contrast against the light-weight headings
- Buttons: 16px / 200 weight

**The inversion:** Headings are light, body paragraphs are medium. This reverses the conventional hierarchy. Large type is ethereal; small text is anchored. The result is a page that reads with unusual grace.

**No letter-spacing on body text.** Only H1 uses negative tracking.

## 4. Component Stylings

**Buttons:** Two distinct types:
- Light button: `rgb(244, 244, 247)` background, `rgb(24, 24, 27)` text and border, layered shadow (inner white/dark, outer drop) — a classic pressed-button depth effect
- Dark button (`.bg-primary`): `rgb(24, 24, 27)` background, `rgb(172, 172, 175)` text — inverted, subdued

**Hover on dark button:** `oklab(0.999994 … / 0.06)` — barely-there white tint, near-imperceptible change. Very restrained interactivity.

**Input fields:** Transparent background, white border at 24% opacity on dark areas (`oklab(… / 0.24)`), no background fill. Clean ghost inputs.

**Shadows:** Extremely nuanced — multi-layer shadows combining drop shadow (`0px 1px 1px, 0px 2px 5px`), inset top highlight (`0px 3px 0px 0px inset`), inset bottom shadow (`0px -2px 0px 0px inset`), and inset bottom border (`0px 1px 0px 0px inset black`). This is a button that feels physically pressed.

**Border radii:** 8px (default), 12px, 15px, 16px, 20px, `3.35544e+07px` (effectively infinite — full pill).

## 5. Layout Principles

Section gap is `16px 80px` (row / column) — wide column gap for a grid layout. Header has `96px` horizontal padding. Footer uses `80px` top / `96px` bottom padding — generous and intentional closure.

The Svelte architecture keeps component styles encapsulated. The layout appears to use a 12-column grid system (class `col-span-12` observed). Content spans full width at the container level; internal layout uses the column grid for feature arrangements.

**Breakpoints:** 480px, 600px, 767px — three-point mobile-first scale. Compact compared to most modern sites, suggesting a relatively simple responsive restructuring.

## 6. Depth & Elevation

Elevation is achieved through **multi-layer button shadows** that simulate physical press depth. This is the most sophisticated shadow use in the dataset — not mere drop shadows but a full light-physics simulation:

- Top highlight (inset, slight white): simulates light from above
- Bottom shadow (inset, slight dark): simulates ground shadow
- Bottom border (inset, black): crisp edge definition
- Outer drop shadow (2–5px): card lift from surface

Cards use `rgba(0,0,0,0.04–0.08) 4px 0 20px` — lateral shadows suggesting panels floating above the canvas from the side.

The `oklab` colour space usage in hover states and borders is a modern CSS4 signal — this site is deliberately using cutting-edge CSS.

## 7. Do's and Don'ts

**Do:**
- Use `neue-haas-grotesk-display` exclusively — weight 200 for all UI, weight 500 for paragraph body text.
- Use the warm off-white canvas (`rgb(238, 238, 241)`), not white or cool grey.
- Apply the multi-layer button shadow to all button components.
- Use `rgb(24, 24, 27)` as your near-black text and border colour.
- Keep the palette strictly greyscale — no colour accents.
- Use `oklab` for transparent borders and hover overlays where supported.
- Apply 80–96px horizontal padding to major layout containers.

**Don't:**
- Use colour. The system is deliberately monochromatic.
- Swap Neue Haas Grotesk for a system font or Inter.
- Make headings heavier than 200 weight — the lightness is the brand.
- Add gradients or photographic backgrounds.
- Use border-radius above 20px for non-pill elements.
- Simplify the button shadow to a single-layer drop shadow — the depth physics matter.

## 8. Responsive Behavior

Three breakpoints (480, 600, 767px) give a lean responsive model. The 12-column grid likely collapses from multi-column feature rows to single-column stacks below 767px. The 96px header padding likely reduces significantly at mobile. Section gaps (`16px 80px`) probably shift to column-only at narrow widths.

The `3.35544e+07px` border-radius value (a floating point maximisation) is a Svelte/CSS quirk for full-pill rounding without `9999px` — functions identically.

## 9. Agent Prompt Guide

> Build in the style of imagine.dev: warm off-white canvas `rgb(238,238,241)`, near-black `rgb(24,24,27)` as text and UI colour, pure greyscale with zero accent colour. Font: Neue Haas Grotesk Display, weight 200 throughout — except paragraphs which use weight 500 for contrast. H1 at 60px/−1.5px tracking. Multi-layer button shadows simulating physical depth: inset top highlight + inset bottom shadow + inset bottom border + outer drop. Horizontal container padding 80–96px. Footer dark background (`rgb(24,24,27)`). Interactive hover states use near-imperceptible oklab overlays. Svelte component architecture — styles are scoped. Three breakpoints: 480, 600, 767px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
