# monos.framer.website — Design System

## 1. Visual Theme & Atmosphere

monos.framer.website is a dark-mode product site built with absolute consistency. The canvas is near-black `rgb(21,21,21)` — not true black, which would read as pure void, but a warm dark that retains material presence. The entire typographic system is built on Inter and Inter Tight: humanist, legible, designed for screen. The colour vocabulary is restrained to near-monochrome, with a blue link state as the only active-state chromatic signal. The design communicates product credibility through discipline: no gradients, no decorative motion, no personality injections. This is a SaaS or utility product that wants to be trusted.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page background | `rgb(21, 21, 21)` | Near-black canvas |
| Primary heading | `rgb(244, 244, 245)` | Off-white — H1 |
| Secondary heading | `rgb(205, 205, 208)` | Dimmed grey — H2 |
| White text | `rgb(255, 255, 255)` | H3, active/highlighted content |
| Link colour | `rgb(0, 0, 238)` | Default browser blue — links |
| Paragraph text | `rgb(205, 205, 208)` (implied) | Body reading text |
| Shadow / outline | `rgba(0,0,0,0.1) 0px 0px 0px 2px` | Subtle focus ring |

The absence of a custom brand accent is notable. The blue link colour is unmodified browser default — a choice that either signals rawness or deliberate anti-branding. No bright accent, no colour-coded categories.

---

## 3. Typography Rules

**Primary typeface:** Inter Tight (medium-weight, condensed) — used for headings and labels. Its condensed proportions allow larger font sizes in constrained space.

**Secondary typeface:** Inter (regular) — used for H2 and general content, providing optical relief next to the tighter variant.

**Body typeface:** Inter-Medium — body paragraphs at 14px, medium weight. Slightly heavier than typical body weight, which maintains legibility on the dark background.

| Context | Family | Size | Weight | Line Height |
|---|---|---|---|---|
| H1 | Inter Tight | 32px | 500 | 44px |
| H2 | Inter | 32px | 400 | 40px |
| H3 | Inter Tight | 20px | 500 | 32px |
| Body (p) | Inter-Medium | 14px | 500 | 20px |

- H1 and H2 share the same font size (32px) but differ in family and weight — a subtle hierarchy signal through texture, not scale.
- No letter-spacing modifications — Inter's optical spacing is trusted as-is.
- No uppercase transforms anywhere.

---

## 4. Component Stylings

- **Section rhythm:** `padding: 32px 0px`, `gap: 32px` — a consistent 32px module governs both internal spacing and section separation.
- **Focus / outline:** `rgba(0,0,0,0.1) 0px 0px 0px 2px` — the single shadow token, used as a subtle outline/ring.
- **Links:** Unmodified browser blue — either intentionally utilitarian or likely overridden per-component in Framer.
- **Buttons:** Not explicitly detected in CSS — likely handled via Framer's built-in component system.
- **Surfaces:** No elevated cards or modal shadows detected. Sections are distinguished by type treatment, not background colour changes.

---

## 5. Layout Principles

- Section spacing is consistently 32px — used as both gap and padding, creating a predictable modular grid.
- Six breakpoints (`0, 809, 810, 1199, 1439, 1440px`) give granular control across device classes.
- The paired breakpoints (e.g. `809/810`, `1199/1200`) are characteristic of Framer's canvas layout engine switching between preset modes.
- Body has no default padding — layout is entirely Framer-managed at the component level.

---

## 6. Depth & Elevation

Flat. The one shadow token (`2px outline ring`) is a UI state indicator, not an elevation expression. No drop shadows, no layered backgrounds, no blur effects. On a dark background, hierarchy is achieved entirely through the luminance steps in the type colour system (255 → 244 → 205).

---

## 7. Do's and Don'ts

**Do:**
- Use Inter Tight at medium weight for all headings and prominent UI labels.
- Apply the three-step text luminance system: full white for emphasis, `rgb(244,244,245)` for primary, `rgb(205,205,208)` for secondary.
- Use 32px as the base spacing module — padding and gap together.
- Keep backgrounds at `rgb(21,21,21)`. Avoid true black.

**Don't:**
- Add decorative colour accents — the design is intentionally monochromatic.
- Use drop shadows or card elevations — depth is not part of the vocabulary.
- Mix Inter Tight and Inter randomly — Tight for structural headings, Inter for flowing text.
- Reduce paragraph weight below 500 — lighter weights lose legibility on dark backgrounds.

---

## 8. Responsive Behavior

Six breakpoints define four distinct layout states:
- **0–809px (mobile):** Compact, single-column. 32px module likely halved.
- **810–1199px (tablet):** Two-column or wide-column arrangements.
- **1200–1439px (desktop):** Primary experience. Full component widths.
- **1440px+ (wide):** Constrained, centred layout.

Framer canvas transitions mean layout changes may be non-fluid — components reposition as discrete states rather than reflowing.

---

## 9. Agent Prompt Guide

> "Design in the style of monos.framer.website: dark background `rgb(21,21,21)`, Inter Tight medium for headings, Inter regular for body. Use three text luminance levels: `rgb(255,255,255)` for highlighted content, `rgb(244,244,245)` for primary headings, `rgb(205,205,208)` for secondary. 32px spacing module throughout. No decorative colour. No shadows. Flat, dark, typographically disciplined SaaS aesthetic."

---

*Generated by Sparkbites — extracted from live CSS analysis*
