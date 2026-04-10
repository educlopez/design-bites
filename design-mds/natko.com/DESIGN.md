# natko.com — Design System

## 1. Visual Theme & Atmosphere

natko.com is a portfolio that refuses compromise. Built around Aeonik — a premium geometric grotesque — the entire typographic system runs on a single typeface across every size, from the 76px hero heading down to 16px body copy. The canvas is transparent/white, creating a clean, gallery-like neutrality that allows the work itself to carry the visual weight. What's striking is the scale ambition: a 76px headline at a 1:1 line-height (no extra leading) and a 48px H3 at tight tracking create monolithic type forms on the page. The mood is confident, European, and editorial — the kind of portfolio that shows rather than tells.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | transparent / white | Gallery-style canvas |
| Primary text | `rgb(0, 0, 0)` | Body copy, UI text |
| Hero heading | `rgb(255, 255, 255)` | H2 on dark/image sections |
| Caption / metadata | `rgb(183, 183, 183)` | Figcaptions, secondary labels |
| Border / divider | `rgb(229, 231, 235)` | Subtle structural lines |
| Shadow | `rgba(138,147,175,0.2) 0px 3px 6px` | Card lift |

The palette is intentionally minimal — black, white, and a single warm grey for hierarchy. No brand colour, no accent. The work is the colour. The subtle periwinkle-tinted shadow (`rgb(138,147,175)`) adds a barely perceptible personality to card elevations.

---

## 3. Typography Rules

**Typeface:** Aeonik Regular exclusively — a single weight, a single family, across every element. The hierarchy is constructed entirely through size.

| Context | Size | Line Height | Notes |
|---|---|---|---|
| H1 / nav label | 20px | 28px | Same size as body — nav is type-only |
| H2 (hero) | 76px | 76px | 1:1 ratio — monolithic block |
| H3 (section) | 48px | 56px | Slightly airy — breathable at this scale |
| Body (p) | 20px | 34px | Generous 1.7× line height — long-form reading |
| Body (base) | 16px | 24px | Default rhythm |
| Links / UI | 16px | 24px | Identical to base — no visual distinction by default |
| Figcaption | 16px | 24px | Inherits body — differentiated by `rgb(183,183,183)` |

- Weight 400 everywhere without exception. Aeonik's geometry does the structural work that bold would do elsewhere.
- No letter-spacing modifications, no `text-transform`. Aeonik Regular is trusted at defaults.
- The hero H2 at 76px/76px (zero extra leading) creates a solid typographic form, not a text block.

---

## 4. Component Stylings

- **Cards:** Subtle elevation via `rgba(0,0,0,0.05) 0px 0px 2px, rgba(138,147,175,0.2) 0px 3px 6px` — whisper-light, barely distinguishable from the page surface.
- **Inner highlight:** `rgb(255,255,255) 0px 1px 0px inset` — a 1px white line at the top of card components, simulating a lit edge.
- **Figcaptions:** `rgb(183,183,183)` — the standard muted-text treatment for image labels.
- **Footer:** Zero padding/margin — likely a full-bleed element handled by its internal layout.
- **Borders:** `rgb(229,231,235)` — the same tone as Tailwind's default `border-gray-200`, suggesting familiarity without being derivative.

---

## 5. Layout Principles

- No body-level padding — the layout container is managed at the component level.
- Nine breakpoints (`600, 640, 728, 768, 800, 984, 1024, 1100, 1496px`) — the most granular of all five sites. This is a custom-crafted responsive system, not a framework grid.
- Breakpoint density in the 600–800px range suggests careful attention to the awkward tablet-portrait zone.
- The 1496px upper bound implies a generous max-width container for large displays.

---

## 6. Depth & Elevation

Intentionally light-touch:
- The `3px 6px` drop shadow with 20% opacity is the primary elevation token — nearly imperceptible.
- The `1px white inset` edge highlight adds physical texture to cards without visual noise.
- No high-contrast shadows, no dark overlays. The design communicates through space and scale, not depth metaphors.

---

## 7. Do's and Don'ts

**Do:**
- Use Aeonik Regular at all levels — size is the only hierarchy tool.
- Set the hero H2 at a 1:1 line-height for typographic mass.
- Use `rgb(183,183,183)` for any metadata, caption, or secondary label text.
- Apply the periwinkle-tinted shadow (`rgba(138,147,175,0.2)`) to cards for barely-there elevation.

**Don't:**
- Add bold or heavier weights — the mono-weight system defines the calm authority.
- Introduce accent colours — the neutral palette is the point.
- Add letter-spacing or uppercase transforms — they would fight Aeonik's refined defaults.
- Use heavy box shadows — the 20% opacity ceiling is strict.

---

## 8. Responsive Behavior

Nine breakpoints create a smooth progressive experience:
- **600–800px (mobile-to-portrait tablet):** Several micro-adjustments. Typography likely scales, multi-column collapses to single.
- **800–1024px (landscape tablet):** Mid-density arrangements. The 20px body paragraph likely tightens.
- **1024–1496px (desktop):** Primary designed experience. Full typographic scale active.
- **1496px+ (wide):** Constrained max-width, work displayed at generous scale.

The dense breakpoint system suggests fine-tuned column and spacing adjustments rather than dramatic layout shifts.

---

## 9. Agent Prompt Guide

> "Design in the style of natko.com: white/transparent background, pure black text, Aeonik Regular at all weights. Hero headline at 76px with 1:1 line-height. Body at 20px with 34px line height — generous, readable. Only three text colours: black for content, white for headings on dark sections, `rgb(183,183,183)` for captions. Cards use a whisper shadow: `rgba(138,147,175,0.2) 0px 3px 6px` plus 1px white inset top. No accent colour. Gallery-calm, European editorial portfolio aesthetic."

---

*Generated by Sparkbites — extracted from live CSS analysis*
