# monologue.to — Design System

## 1. Visual Theme & Atmosphere

monologue.to is a study in textural contrast. The body background lands on a mid-tone grey (`rgb(84,84,84)`) — neither the safety of white nor the drama of black — which gives every surface placed on top of it an automatic sense of lift. The headline typography is Instrument Serif, a sophisticated editorial serif with tight negative tracking, paired with DM Mono for body copy. This pairing creates a tension between the literary and the technical that feels entirely intentional. A cyan-teal accent system (`rgb(44,204,255)` family) provides the only warm light in an otherwise cool, shadowed environment. The overall mood is: after-dark editorial — like a well-designed magazine read at night.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Body background | `rgb(84, 84, 84)` | Mid-grey canvas |
| Deep background | `rgb(6, 47, 52)` | Dark teal — sections, panels |
| Primary text | `rgb(0, 0, 0)` | Body copy |
| Heading text | `rgb(255, 255, 255)` | White on dark surfaces |
| Cyan accent | `rgb(68, 204, 255)` | Highlight elements, feature blocks |
| Cyan glow | `rgba(0, 225, 255, 0.12)` | Subtle tinted backgrounds |
| Teal mid | `rgb(25, 208, 232)` | Secondary accent, decorative |

The palette is cool throughout: grey, teal, cyan. No warm tones. The mid-grey body creates a ground that neither fights the dark panels nor washes out the white text.

---

## 3. Typography Rules

**Display typeface:** Instrument Serif — elegant, editorial. Used for all H1/H2/H3 at large sizes with aggressive negative letter-spacing.

**Body typeface:** DM Mono — a monospaced font for body paragraphs, reinforcing a technical, notebook-like quality in running text.

| Context | Size | Weight | Letter-spacing | Notes |
|---|---|---|---|---|
| H1 | 52px / 52px lh | 400 | -0.2px | Tight, display |
| H2 | 72px / 72px lh | 400 | -2.16px | Cinematic scale |
| H3 | 48px / 48px lh | 400 | -0.1px | Section heading |
| Body (p) | 14px / 19.6px lh | 400 | +0.3px | DM Mono, slightly open |

- Display headings are always weight 400 — the scale and tracking do the work, not boldness.
- The H2 at `-2.16px` tracking is dramatic: characters nearly touch at 72px, creating a typographic block.
- Body in DM Mono at positive tracking softens the monospace density for reading comfort.

---

## 4. Component Stylings

- **Feature div (`framer-1i0160s`):** Solid cyan `rgb(68,204,255)` background — the brightest surface in the composition.
- **Tinted glass panel (`framer-KJjVM`):** `rgba(0,225,255,0.12)` — near-transparent cyan tint over the grey, suggesting Framer's glassmorphism layer.
- **Deep section (`framer-1esnzm0`):** Dark teal `rgb(6,47,52)` — used for content-heavy sections that need visual separation.
- **Buttons:** Translucent `rgba(255,255,255,0.12)` — white glass on dark backgrounds.
- **Shadows:** Layered inset shadows on glass components — both white highlights and black fills create a convex pill effect. `rgba(255,255,255,0.63) inset` for highlight, `rgba(0,0,0,0.7) inset` for depth. Framer-native glassmorphism approach.

---

## 5. Layout Principles

- Section padding: `10px` — minimal. Framer controls layout through absolute positioning, not CSS flow.
- Breakpoints: `809.98 → 810 → 1199.98 → 1440px` — four distinct layout states, covering mobile, tablet, desktop, and wide.
- The Framer origin means layout is canvas-based. CSS breakpoints trigger layout-mode switches rather than fluid reflow.
- Visual hierarchy relies on scale (72px headings dominating) more than whitespace.

---

## 6. Depth & Elevation

Rich layered depth — the standout characteristic of this design:
- **Inset highlights** (`rgba(255,255,255,0.63) inset`) create a lit-from-above glass surface.
- **Inset shadows** (`rgba(0,0,0,0.7) inset`) deepen the bottom of pill/card shapes.
- **Drop shadows** (`rgba(0,0,0,0.25) 0px 4px 4px`) ground floating elements.
- The mid-grey body background means surfaces have tonal distance without requiring extreme contrast.

---

## 7. Do's and Don'ts

**Do:**
- Use Instrument Serif at display scales with strong negative tracking for headings.
- Use DM Mono for body text — preserve the editorial-technical contrast.
- Apply the cyan accent to a single focal element per section.
- Layer inset shadows on glass-style components for physical depth.

**Don't:**
- Use warm colours — the entire palette is cool.
- Apply bold weights to serif headings — regular weight at large scale is the system.
- Use white as a background — the mid-grey ground is essential to the composition.
- Flatten components. The depth system is load-bearing for this design.

---

## 8. Responsive Behavior

Four breakpoints provide a nuanced responsive curve:
- **< 810px (mobile):** Single-column, typography scales down, large display headings reflow.
- **810–1199px (tablet):** Mid-density layout, likely two-column grids.
- **1200–1439px (desktop):** Primary designed experience.
- **1440px+ (wide):** Constrained max-width, centred.

Framer's canvas-based layout means breakpoint transitions may involve distinct component arrangements rather than fluid reflow.

---

## 9. Agent Prompt Guide

> "Design in the style of monologue.to: mid-grey `rgb(84,84,84)` background, Instrument Serif for display headings at weight 400 with strong negative letter-spacing. DM Mono for body text. Cyan `rgb(68,204,255)` as the single accent. Use glass panels with layered inset shadows for depth. Dark teal `rgb(6,47,52)` for alternate section backgrounds. No warm tones. Editorial, nocturnal, technically refined."

---

*Generated by Sparkbites — extracted from live CSS analysis*
