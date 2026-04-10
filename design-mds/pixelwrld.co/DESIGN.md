# pixelwrld.co — Design System

## 1. Visual Theme & Atmosphere

Pixelwrld.co is a design or creative portfolio built in Framer that lives in a light, airy register — near-white backgrounds, softened grey tones, and a single signature design decision: pill-shaped containers with a `30px` border radius. The aesthetic is modern, approachable, and minimal without being sparse. The absence of bold accent colors keeps the focus on content and imagery. The overall mood is clean agency portfolio — confident enough to strip decoration, warm enough not to feel clinical.

## 2. Color Palette & Roles

**Backgrounds**
- `rgb(247, 247, 247)` — Site background; barely-off-white, slightly warmer than pure `#F7F7F7`
- `rgb(228, 228, 228)` — Card / panel surface; visible separation from background
- `rgba(226, 226, 226, 0.8)` — Semi-transparent panel layer; frost-like overlay effect

**Text & Ink**
- `rgb(0, 0, 0)` — All primary text; no grey softening in the type system

**Interactive / Link**
- `rgb(0, 0, 238)` — Browser-default blue on external links (Threads); notable as the only color in the system

**Borders**
- `rgb(0, 0, 0)` — Borders are ink-black where present

The palette is essentially monochromatic. The single instance of `rgb(0, 0, 238)` on external links suggests browser defaults were not overridden — an intentional choice to signal "this is an outbound link."

## 3. Typography Rules

**Inter** is the sole custom typeface, appearing on paragraphs and body content. Generic `sans-serif` is used at the base (`body`, `a`) suggesting Framer's own baseline, with Inter layered in for rendered content.

| Role | Family | Size | Weight |
|------|--------|------|--------|
| Body / Paragraphs | Inter | 16px | 400 |
| Base / Links | sans-serif (system) | 12px | 400 |

Line height on Inter paragraphs is tight: `19.2px` (1.2×), giving text a compact, editorial density. No display sizes, no bold weights, no tracking adjustments. Typography is deliberately invisible — Inter at 16px/400 is the neutral default of the web.

## 4. Component Styling

**Pill containers**: `border-radius: 30px` is the defining component shape. Applied to cards, tags, or callout elements — creating a rounded, badge-like vocabulary throughout.

**Panels**: Three surface levels stack within the grey-on-grey system: `#F7F7F7` (page), `#E4E4E4` (card), `rgba(226,226,226,0.8)` (overlay/frosted panel). The translucent layer creates a subtle depth effect without blur.

**Links**: Black by default; browser-default blue (`rgb(0,0,238)`) on social/external links. No custom hover states detected.

**No shadows detected.** Cards are differentiated purely through background color contrast.

## 5. Layout Principles

A dense, multi-tiered breakpoint system drives fine-grained responsive behavior: `479, 480, 649, 650, 799, 800, 999, 1000, 1727`. This suggests a Framer canvas with explicit layout variants at every common device width — likely a masonry or grid layout that reflows at each step. The `1727px` upper breakpoint accommodates wide-monitor displays.

Framer's absolute-positioned layout model means spacing is canvas-set rather than token-driven. No custom CSS spacing properties were declared.

## 6. Depth & Elevation

No box shadows. Depth is achieved through the three-step grey surface stack: page → card → semi-transparent overlay. The `0.8` opacity on the third surface creates a glass-like effect that implies layering without blur. No border-radius on body or text elements — the `30px` radius is reserved for containers only.

## 7. Do's and Don'ts

**Do:**
- Apply `border-radius: 30px` consistently to pill/card containers — this is the design's signature
- Use `#F7F7F7` as the base; let `#E4E4E4` cards read as elevated
- Use Inter at 16px/400 for all body content; keep line-height at 1.2–1.3
- Let the semi-transparent grey (`rgba(226,226,226,0.8)`) handle overlay moments
- Allow external links to use browser-default blue — it's an intentional signal

**Don't:**
- Don't introduce accent colors — the monochrome palette is load-bearing
- Don't add box shadows (the system uses surface color for elevation)
- Don't reduce border-radius below 20px on pill elements — it loses the signature shape
- Don't increase font weight above 400 — bold is absent from this system
- Don't add letter-spacing or text-transform; this is a neutral typographic voice

## 8. Responsive Behavior

Nine breakpoints span from `479px` to `1727px`, with paired transitions at most steps (e.g., `479/480`, `649/650`). The paired breakpoints suggest Framer generates a "less than" and "greater than" variant for each device tier. Layout fluidly adapts across mobile (≤479), large mobile (480–649), tablet (650–799), desktop-small (800–999), desktop (1000–1727), and wide (1727+).

## 9. Agent Prompt Guide

> Build a portfolio card layout in the pixelwrld.co style. Background is `#F7F7F7`. Cards use `#E4E4E4` with `border-radius: 30px` and no box-shadow. An optional frosted overlay layer uses `rgba(226,226,226,0.8)`. Typography is Inter at 16px/400 with 1.2 line height. Text is `#000000`. No accent colors — the only color in the system is browser-default blue on external links. No shadows. Depth comes from the background contrast between surface levels, not elevation. Responsive layout adapts at 480, 650, 800, and 1000px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
