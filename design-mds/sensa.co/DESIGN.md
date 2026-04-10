# sensa.co — Design System

## 1. Visual Theme & Atmosphere

Sensa.co is a masterclass in section-based storytelling. Rather than committing to a single palette, the site cycles through vivid, high-contrast section backgrounds — pink, deep maroon, midnight navy, cerulean, golden yellow, emerald green, purple — each one a distinct chapter in a visual narrative. The design philosophy is theatrical: every scroll brings a new scene, a new emotional temperature. The overall canvas is black, which acts as the stage itself, allowing each colorful section to perform in front of it.

What holds the chaos together is Gelion — a custom display typeface that carries massive weight at 88px+, used almost exclusively in white. The typography acts as the constant identity across shifting backgrounds. This is a Framer-built site that leans fully into the platform's section-swap capabilities, using them not as gimmick but as deliberate narrative architecture.

---

## 2. Color Palette & Roles

**Base**
- `#000000` — Page and body background (the stage)
- `#FFFFFF` — Primary display text color on all dark/vivid sections

**Section Backgrounds (sequential palette)**
- `rgb(254, 179, 200)` — Blush pink (opening/hero section)
- `rgb(97, 0, 51)` — Deep maroon/burgundy (dramatic contrast section)
- `rgb(5, 1, 66)` — Midnight navy (technical/deep-dive section)
- `rgb(207, 241, 255)` — Light cerulean (light relief section)
- `rgb(252, 227, 143)` — Warm golden yellow (energetic mid-section)
- `rgb(22, 124, 63)` — Emerald green (positive/growth section)
- `rgb(111, 69, 214)` — Electric purple (creative/bold section)
- `rgb(31, 78, 152)` — Deep royal blue (closing section)
- `rgb(2, 26, 51)` — Near-black navy (footer / darkest tier)

**Utility**
- `rgb(118, 118, 118)` — System UI select border (browser default — not styled)

**Absent**: There is no persistent brand accent color. Color is used narratively, not systematically. The browser-default link blue (`rgb(0, 0, 238)`) appears on `a` elements, suggesting links are either rare or intentionally unstyled.

---

## 3. Typography Rules

**Gelion Medium** is the sole declared typeface and it is used at striking scale. A custom humanist display sans, Gelion carries authority without the geometric coldness of typefaces like Aeonik or Monument Grotesk. The "Medium" weight at regular `font-weight: 400` is deceptive — it reads as substantial at display sizes.

- **h1**: Gelion Medium / 88px / `line-height: 73.92px` (tighter than font size — compressed, impactful)
- Body / prose text: appears to use default sans-serif fallback — Gelion may only appear in hero and section headlines

The compressed line-height on h1 (73.92px for 88px font) is a deliberate display technique: text stacks tight, creating a dense block of words that reads as a unit rather than separate lines. This is typical of editorial and brand-first design.

No secondary functional typeface is explicitly declared — utility text likely falls back to the system sans. This is consistent with a Framer site where prose sections may use default text styling.

---

## 4. Component Stylings

**Section containers**: Full-width Framer sections (`section.framer-*`) each carry their own `backgroundColor` — the component is the color. No padding, no border, no card. The section IS the surface.

**Overlaid content panels** (`div.framer-1hs0cr3`): Appear as content blocks within sections, sometimes carrying a contrasting background to their parent section — deep maroon panel on pink background, cerulean panel on navy background — creating nested depth.

**No buttons extracted**: Primary CTAs are either not present on the page extract or are rendered as Framer-native components without a standard `button` selector. Their styling is inferred rather than confirmed.

**Navigation**: Transparent (`rgba(0,0,0,0)`) on the black background — effectively invisible until scroll changes context. Links default to browser blue (unstyled), suggesting nav links may be handled via Framer's visual layer.

**Select element**: Browser-default styling detected — no custom form component system.

---

## 5. Layout Principles

This is a full-viewport, section-by-section layout. Each `section.framer-*` likely fills 100vw and is sized to its content. The black body background bleeds between sections during scroll, creating a brief void that resets the eye before the next color environment appears.

No explicit breakpoints were detected — consistent with Framer's visual responsive system, which does not generate standard CSS breakpoints in the traditional sense. Framer handles responsive behavior through its own layout engine.

The Framer component class naming (`framer-1ugcfr2`, `framer-1pvqxd2`, etc.) confirms this is a Framer-published site. Layout is designed in the Framer canvas, not in code.

---

## 6. Depth & Elevation

Depth is achieved through section-nesting rather than shadow. The `div.framer-1hs0cr3` panels sit within section backgrounds at contrasting luminance levels — a light cerulean panel against a midnight navy section creates perceived elevation without any CSS shadow property.

The black body background that shows between sections creates a subtle gap-frame effect — each section feels like a physical card in a stack rather than a continuously scrolling page.

No `box-shadow` values were detected in the data.

---

## 7. Do's and Don'ts

**Do**
- Use full-bleed section backgrounds as the primary design unit
- Let white text on vivid backgrounds carry the headline hierarchy
- Maintain black (`#000000`) as the base canvas — it makes every color pop
- Compress line-height for display headings (below 1.0× font size) for editorial density
- Use sequential color sections as emotional pacing, not random decoration

**Don't**
- Apply the section colors as UI element colors (they are narrative backgrounds, not brand accents)
- Add shadows, cards, or elevation layers — the design is flat by architecture
- Style links with custom colors — the deliberate absence of link styling is itself a choice
- Mix Gelion Medium with dense body copy — it is a display typeface, use it large or not at all

---

## 8. Responsive Behavior

No standard CSS breakpoints are extracted — Framer handles responsive layout through its own system. The design likely adapts through Framer's built-in responsive stack behavior, reducing column counts and scaling typography at mobile widths.

The full-bleed section model is inherently responsive: each section fills its viewport regardless of width. Font sizes at 88px+ would require significant scaling at mobile (likely dropping to 48–56px via Framer's responsive text settings).

---

## 9. Agent Prompt Guide

> "Design in the style of sensa.co: black canvas stage (`#000000`) with full-bleed vivid sections — cycling through blush pink, deep maroon, midnight navy, cerulean, golden yellow, emerald green, and electric purple. White Gelion Medium display text at 88px+ with compressed line-height. No persistent brand accent color — color is used narratively per section. Flat, shadow-free. Each section is a scene change, not a scroll position."

---

*Generated by Sparkbites — extracted from live CSS analysis*
