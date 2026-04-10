# gracewalker.ca — Design System

## 1. Visual Theme & Atmosphere

Grace Walker's portfolio radiates warmth and intentional boldness. The dominant surface is a vivid burnt orange — not the flat, digital orange of a dashboard, but one that feels hand-mixed, almost gouache-like. Against this heat, a forest green grounds the identity; it's the ink on the page, the text that speaks. The result is a palette that feels vintage print-design: courageous, editorial, and intimate.

There are no gradients, no glass effects, no dark modes. The design trusts solid color to carry the emotional weight. Work is displayed through color-coded slides — each project gets its own branded hue — turning the portfolio into a gallery of distinct worlds rather than a uniform grid.

The typeface pairing is equally considered: display headings use Tiempos Headline (a serif with editorial gravitas) while everything else runs in Soehne (a refined grotesque with humanist warmth). This serif/sans split mirrors the site's personality: serious craft, approachable voice.

---

## 2. Color Palette & Roles

**Brand & Background**
- Burnt orange `rgb(255, 94, 48)` — page background, primary surface, dominant hue
- Warm parchment `rgb(243, 236, 228)` — link text, card content text, secondary surface tone
- Forest green `rgb(37, 62, 41)` — body text, headings on light surfaces, borders

**Cards & Surfaces**
- Muted orange card `rgb(232, 81, 42)` — card variant on orange background (slight darkening for depth)
- Parchment card `rgb(243, 236, 228)` — light card surface
- Powder blue `rgb(195, 219, 239)` — tertiary card variant, cool contrast to orange dominance
- Silver `rgb(221, 221, 221)` — slider background

**Work Slides (project-specific palettes)**
- Steel blue `rgb(46, 89, 108)`
- Bright blue `rgb(0, 125, 218)`
- Tobacco brown `rgb(69, 59, 49)`
- Deep plum `rgb(49, 38, 68)`
- Crimson `rgb(95, 39, 58)`

**Interaction**
- Links on hover: `opacity: 0.51` (fade, not color change)
- Focus ring: orange `rgb(255, 94, 48)` on parchment links
- Buttons on hover: white `rgba(255, 255, 255, 0.196)` overlay (subtle fill on transparent)

---

## 3. Typography Rules

Two fonts, two roles, zero compromise.

**Tiempos Headline** — display headings only (h2)
- Size: `48px` / Line height: `52.8px` / Weight: 500 (medium)
- Used for section names, hero moments; the editorial voice
- Never used for body copy or navigation

**Soehne** — the system font for everything else
- h1: `24px` / `600` — section sub-headings, navigation labels
- Body/paragraphs: `16px` / `400` / `1.6` line height — readable, open
- Links: `16px` / `600` — bolded to signal interactivity without color alone
- No text transforms, no tracked letter-spacing — type is kept natural and approachable

What's absent: no monospace, no all-caps micro-labels, no small utility text. Type is either content or navigation — never decoration.

---

## 4. Component Stylings

**Cards (`.card`)**
- Three distinct color modes: parchment on green, orange-on-parchment, powder blue on green
- Border radius: `24px` (contained), `30px` (prominent), up to `64px` (pill-adjacent elements)
- Shadow: `rgba(73, 25, 12, 0.3) 5px 5px 10px` — warm, directional, analog
- Inset shadow also present: `rgba(59, 59, 59, 0.2) 5px 0px 10px inset` — gives cards a pressed-paper feel

**Flip Cards (`.flipcard-back`)**
- White reverse face: `rgb(255, 255, 255)` — pure reveal, contrastive against orange world

**Work Slides**
- Each slide is a full-bleed color block with white text
- No radius on slides — they span edge to edge, immersive

**Buttons (`.btn`)**
- Transparent background with 10% white tint: `rgba(243, 236, 228, 0.1)`
- Hover: `rgba(255, 255, 255, 0.196)` — ghostly brightening
- No border, no strong shadow — buttons feel part of the surface

**Sections**
- Padding: `32px` uniform — generous breathing room

---

## 5. Layout Principles

The page is a single scrolling canvas rather than a grid of cards. Each section occupies the full width, with work slides functioning as horizontally scrollable panels (a slider pattern) rather than a masonry grid.

The layout philosophy is spatial: big color blocks, generous padding, nothing cramped. The `page-wrapper` sets orange as the default environment and everything else layers on top. There is no container max-width visible in the CSS — the design stretches to fill its context.

Sections use `32px` horizontal padding, keeping content from touching edges even at narrow widths. Gaps default to `normal` — no explicit flexbox or grid gap values are asserted, suggesting layout is handled by Webflow's built-in spacing utilities.

---

## 6. Depth & Elevation

Depth comes from shadow and color contrast, not blur or transparency stacking.

- **Ambient shadow**: `rgba(0, 0, 0, 0.09) 7px 7px 40px 6px` — diffuse, card-level lift
- **Warm directional shadow**: `rgba(73, 25, 12, 0.3) 5px 5px 10px` — brown-tinted, suggests a warm light source
- **Inset texture shadow**: `rgba(59, 59, 59, 0.2) 5px 0px 10px inset` — gives cards the feel of pressed material

There are no frosted glass effects, no `backdrop-filter`, no z-axis animations noted. The layering is physical — one surface sits on another via shadow, not through blending.

---

## 7. Do's and Don'ts

**Do:**
- Use the orange + forest green pairing as the foundational color contract
- Let each work project define its own slide color (don't force them into orange)
- Pair Tiempos Headline with Soehne — never use Tiempos for body copy
- Apply warm brown-tinted shadows (`rgba(73, 25, 12, ...)`) rather than black shadows
- Use opacity fading (`~0.5`) for link hover, not color changes
- Keep border radii generous: minimum `24px` on cards

**Don't:**
- Don't introduce gradients — the design lives in solid color
- Don't add dark mode — the warmth is structural, not switchable
- Don't use cool-toned grays for text — the green `rgb(37, 62, 41)` is the neutral
- Don't use Tiempos below display sizes — it reads as mismatch at 16px
- Don't use tight letter-spacing or all-caps — the tone is warm, not corporate

---

## 8. Responsive Behavior

No media query breakpoints are surfaced in the CSS data (built in Webflow, which handles breakpoints through its own layout engine). The section padding of `32px` provides a consistent comfortable gutter at all widths. Work slides are designed to scroll horizontally, implying they collapse to single-item views on mobile.

The flip card pattern implies touch devices may need tap-to-flip rather than hover, which should be explicitly handled. No explicit mobile type scale is present — Webflow likely manages this through responsive text sizing in its style panel.

---

## 9. Agent Prompt Guide

Use this block when prompting an AI to generate UI in the style of gracewalker.ca:

```
Design in the style of a warm editorial portfolio. Use a dominant burnt orange background (#FF5E30) with forest green (#253E29) for text. Accent with warm parchment (#F3ECE4) and powder blue (#C3DBEF) for card surfaces. Body font is Soehne (or Inter as substitute) at 16px/400; display headings use a serif like Tiempos Headline or Playfair Display at 48px/500. Cards have 24–30px border radius, a warm brown-tinted directional shadow, and come in 3 color variants. Hover links fade to 50% opacity rather than changing color. Buttons are ghost-style with a transparent white tint. Each project/work item gets its own unique background color. No gradients, no dark mode, no tight letter-spacing.
```

---

*Generated by Sparkbites — extracted from live CSS analysis*
