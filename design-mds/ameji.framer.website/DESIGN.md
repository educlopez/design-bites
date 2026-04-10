# ameji.framer.website — Design Language

## 1. Visual Theme & Atmosphere

Ameji presents as a minimal, modern design portfolio built on Framer — confident without being loud. The palette sits in a cool near-neutral zone: an off-white body, pure white card surfaces, and a monochromatic range of greys from mid-tone to true black. There is no accent colour in the conventional sense; the visual energy comes entirely from typography scale, negative space, and the bold contrast between black text and pale backgrounds. The atmosphere is professional restraint — the kind of portfolio that trusts the work to carry the page, not the interface.

## 2. Color Palette & Roles

**Background layers**
- `rgb(245, 245, 245)` — Body background; warm-neutral off-white that softens the canvas without yellowing.
- `rgb(255, 255, 255)` — Card and section surfaces (`div.framer-13yxzio`); pure white lifts content above the body.

**Foreground & text**
- `rgb(0, 0, 0)` — Primary text across all elements: headings, body, labels.
- `rgb(145, 145, 145)` — Mid-grey surface (`div.framer-1tiu2on`); used for dividers, secondary containers, or muted backgrounds.

**Input & form surfaces**
- `rgb(232, 232, 232)` — Input field background; slightly darker than body to create a visible field boundary without a hard border.

**Interactive (default browser)**
- `rgb(0, 0, 238)` — Default unvisited link colour (browser default, not overridden). Suggests no custom link styling has been applied — links inherit user-agent styles.

No custom CSS properties are defined. No brand accent colour exists. The palette is intentionally monochromatic.

## 3. Typography Rules

Single typeface, full hierarchy:

**Inter** — Used exclusively, at every level. Framer's fallback chain is `Inter, "Inter Placeholder", sans-serif`.

| Element | Size | Weight | Leading | Tracking |
|---------|------|--------|---------|----------|
| h2 | 48px | 600 | 57.6px (1.2) | −0.96px |
| h3 | 26px | 600 | 31.2px (1.2) | −0.52px |
| p / body | 16px | 400 | 24px (1.5) | −0.16px |
| input | 16px | 500 | 16px (1.0) | −0.16px |

Consistent negative tracking at every size (roughly −2% of font-size) creates a slightly compressed, modern feel. Headings use `600` weight; body uses `400`; inputs use `500` — a deliberate weight step that signals interactivity without full-bold. Line-height for headings is 1.2; body is 1.5.

What is absent: no display serif, no monospace, no uppercase transforms, no font-feature-settings. Inter carries the full typographic load.

## 4. Component Stylings

**Cards** — Pure white `rgb(255,255,255)` on the `rgb(245,245,245)` body, creating a subtle lift without shadow. Framer canvas components.

**Buttons / Pills** — Border radius `99px` (effectively fully-rounded pill). Consistent with a modern SaaS/portfolio aesthetic.

**Navigation link** — `border-radius: 94px` on nav items; pill-shaped nav links. No hover state detected in extracted CSS (Framer Motion likely handles these via JS).

**Inputs** — `rgb(232,232,232)` background, `font-weight: 500`, `line-height: 1.0` (tight). No visible border colour beyond `rgb(0,0,0)` default.

**No shadows** — Shadow array is empty. Elevation is handled purely through surface colour contrast.

## 5. Layout Principles

Framer-generated layout. Breakpoints at: `809px`, `810px`, `1279px`, `1280px`, `1535px` — Framer's standard responsive grid breakpoints (mobile / tablet / desktop / wide / ultrawide).

Body spacing is zero-based (`padding: 0, margin: 0`); all spacing is handled within Framer canvas frames. No gap tokens are exposed at the body level.

The two-step breakpoints (809/810, 1279/1280) are Framer artefacts representing the boundary between layout variants — not custom breakpoints.

## 6. Depth & Elevation

No box-shadows defined anywhere. Depth is created through:
- **Background contrast**: white cards on `rgb(245,245,245)` body.
- **Grey mid-surface** `rgb(145,145,145)`: used as a distinct visual layer for secondary elements.
- **Typography weight**: the 600-weight Inter headlines create strong foreground presence.

Framer Motion likely handles any entrance animations or micro-interactions, but these are not captured in static CSS extraction.

## 7. Do's and Don'ts

**Do:**
- Use Inter at every typographic level — weight and size create all the hierarchy.
- Apply negative tracking consistently: approximately `−0.02em` of the font size.
- Use pill border-radius (`94px`–`99px`) for all interactive elements.
- Keep the background a warm off-white `rgb(245,245,245)` rather than pure white — it's softer.
- Let white cards float on the off-white body as the primary elevation mechanism.

**Don't:**
- Don't introduce accent colours — the design is intentionally monochromatic.
- Don't add drop shadows; they are deliberately absent.
- Don't use `font-weight: 700` or heavier; 600 is the maximum.
- Don't override link colours with custom values if the browser default is acceptable in context.
- Don't use rectangular borders; pill or no-border are the only shapes used.

## 8. Responsive Behavior

Five breakpoints mirroring Framer's standard responsive variants:
- `≤809px`: Mobile layout.
- `810px–1279px`: Tablet layout.
- `1280px–1535px`: Desktop layout.
- `≥1536px`: Wide/ultrawide layout.

Typography scale likely reduces at smaller breakpoints via Framer responsive text sizing. No explicit mobile type overrides are visible in extracted CSS — Framer handles this at the canvas level.

## 9. Agent Prompt Guide

> "Design in the style of ameji.framer.website: warm off-white body `rgb(245,245,245)`, pure white card surfaces, pure black text. Single typeface: Inter with negative tracking (−0.02em), weight 600 for headings / 400 for body. Pill-shaped components (`border-radius: 99px`). No shadows, no accent colour. Depth comes from surface contrast alone. Five responsive breakpoints following Framer's mobile/tablet/desktop/wide/ultrawide grid."

---

*Generated by Sparkbites — extracted from live CSS analysis*
