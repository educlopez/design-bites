# Wild Week Athens 2026 — Design System Reference

## 1. Visual Theme & Atmosphere

Wild Week's Athens edition leans hard into classical archaeology — a pale ash-grey canvas (`rgb(203, 203, 203)`) that reads like aged limestone, a single saturated ultramarine (`rgb(7, 85, 187)`) borrowed from vase-painting and Greek passport pages, and display type set in **Albertus Nova Light** that echoes carved stone lapidary letters. The page behaves like a printed exhibition catalogue: no gradients, no shadows, no glossy UI. Content blocks sit on slightly warmer stone-toned surfaces (`rgb(221, 220, 215)`) that separate by luminance swap rather than by outline, and the copy block layout — "THE FACTS" with single-letter indices D / P / H / I — reads as a museum placard. The tone is archaic, wry, deliberately unhurried. Not a tech brand. Not a hotel brand. Something closer to a private invitation printed on cardstock.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(203, 203, 203)` — page canvas (ash-grey stone)
- `rgb(0, 0, 0)` — ink (body text, borders)
- `rgb(7, 85, 187)` — Greek ultramarine (links, logotype, accent surfaces)

**Warm stone surfaces (content blocks)**
- `rgb(232, 232, 232)` — lightest panel (luminance 0.91)
- `rgb(221, 221, 214)` / `rgb(221, 220, 215)` / `rgb(220, 219, 213)` — a micro-gradient of sand-warmed stones (luminance 0.86–0.87), used almost interchangeably to break full-bleed monotony
- `rgb(255, 255, 255)` — hard white (rarely, reserved for inset content)

**Accent surface**
- `rgb(7, 85, 187)` — ultramarine block with black text — a single chromatic moment that carries the brand

**Interactive**
- Links: ultramarine default → darker royal `rgb(5, 68, 150)` on hover (a subtle tonal step, not a color swap)

The palette is deliberately narrow: one canvas grey, one pure ink, one saturated blue. The "warm stones" family exists only to give large panels faint tonal variation — you should never see more than two of them side-by-side.

---

## 3. Typography Rules

**Typefaces**
- **Albertus Nova Light** (weight 300) — the entire editorial voice: headlines, sub-heads, body prose, links. Albertus is a 1930s lapidary face with slightly flared serifs — it evokes inscriptions.
- **system sans-serif** — body fallback and tiny labels only

**Scale**

| Role | Font | Size | Weight | Line-height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| H1   | Albertus Nova Light | 24px | 300 | 28.8px | +0.96px | uppercase |
| H2   | Albertus Nova Light | 18px | 300 | 21.6px | +0.72px | uppercase |
| P    | Albertus Nova Light | 10px | 300 | 15px    | +0.1px  | none      |
| A    | Albertus Nova Light | 10px | 300 | 15px    | +0.1px  | none      |
| Body (fallback) | sans-serif | 12px | 400 | normal | normal | none |

**Principles**
- Weight is locked at **300** across every heading and body element — the typographic character comes entirely from Albertus Nova's shape, not from bold/light contrast.
- All display type is **uppercase** with positive tracking (`+0.72px` to `+0.96px`). This is not a trend choice — uppercase + wide tracking is what lapidary faces were designed for.
- Body paragraphs drop to 10px with near-zero tracking — almost fine-print scale — because the aesthetic is reference material, not a marketing page.
- OpenType features are explicitly enabled (`cv03, cv04, cv09, cv11, blwf`). The designer is hand-picking alternate glyphs — which means the type is doing deliberate decorative work.

**What's absent:** no sans-serif display, no italics, no heavy weights, no modern geometric grotesk. The entire page talks in one carved voice.

---

## 4. Component Stylings

**Links**
- Default: ultramarine `rgb(7, 85, 187)` text, no underline by default (Framer's link-text component manages this inline)
- Hover: darkens one step to `rgb(5, 68, 150)` — royal blue. No background flash.
- Focus: native 1px `rgb(0, 95, 204)` ring, not customised

**Logotype / Hero plate**
- The "WILD WEEK" wordmark is a hand-drawn treatment — not derived from the body face. It sits at full-bleed scale with an amphora silhouette positioned behind it.

**Content panels**
- Background: one of the warm-stone family (`rgb(221, 220, 215)` range)
- Border: none — separation comes from luminance swap against the ash-grey canvas
- Border-radius: `4px` or `8px` — small, paper-like corners, not pill shapes

**Buttons / CTAs**
- Minimal — the design avoids solid CTAs in favor of simple uppercase link text. Interaction cues live in the copy ("RSVP", "APPLY") rather than in chrome.

**No shadows detected.** Depth is entirely flat.

---

## 5. Layout Principles

- **Editorial split layout**: a dominant hero stage with the wordmark + amphora, then a two-column facts/imagery grid, then a marble-frieze illustration that runs nearly full-bleed.
- **Indexed labels**: facts use single-letter keys (D. / P. / H. / I.) flush-left with right-aligned values — a catalogue-entry pattern borrowed from archaeological records.
- Body padding is zero at the element level; all composition happens inside Framer's nested frames (noticeable from the unusually granular breakpoint list: 809, 810, 1389, 1390, 1399, 1400, 1599, 1799 — Framer's responsive ramps).
- Content prefers long horizontal strips over contained cards — the frieze is allowed to bleed nearly edge-to-edge, reinforcing the "sculptural relief" frame.

---

## 6. Depth & Elevation

Depth is almost entirely **absent**. No `box-shadow` values in the extracted system. Separation between surfaces is achieved through two devices:

1. **Luminance stepping** — ash canvas (0.80) → warm stone panel (0.86) → lightest panel (0.91) → white (1.0). Adjacent surfaces sit only ~0.05 apart, which reads as the faintest shadow of paper-on-paper rather than a clear elevation change.
2. **A single saturated block** — the ultramarine panel breaks the near-monochrome composition and acts as the visual anchor. It's the only "loud" surface on the page.

The absence of shadows is doctrinal. Adding one would collapse the lithograph atmosphere.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(203, 203, 203)` as the canvas — it carries the limestone atmosphere.
- Lock typography to Albertus Nova Light at weight 300 for every heading and every body run.
- Set all display type **uppercase** with `+0.7px` to `+1px` tracking.
- Reserve `rgb(7, 85, 187)` for the logotype, links, and at most one full-bleed accent panel per view.
- Use the warm-stone surface family (`rgb(221, 220, 215)` ±) for content cards — never pure white, never dark grey.
- Treat body copy as reference prose — 10px, barely tracked, Albertus in text weight.
- Label sections with terse alphabetic indices (D / P / H / I) rather than icons or emoji.

**Don't**
- Don't introduce a second typeface as display — the page survives on Albertus alone.
- Don't use bold weights. Hierarchy comes from size + case + tracking, never from weight.
- Don't add drop-shadows, blurs, or gradients — depth must stay flat.
- Don't use rounded pill buttons. Interaction is text-first, chrome-last.
- Don't swap the ultramarine for a brighter or darker blue — `rgb(7, 85, 187)` is specifically passport / bureaucratic-blue, not royal, not electric.
- Don't rely on hover micro-animations — the page moves almost not at all.

---

## 8. Responsive Behavior

Framer's unusually dense breakpoint list — **809, 810, 1389, 1390, 1399, 1400, 1599, 1799** — suggests the layout is designed around fixed compositions at small laptop, large laptop, and desktop widths, with 1-pixel pairs handling Framer's internal snap boundaries rather than meaningful user-facing breakpoints. Content scales by swapping grid layouts rather than reflowing type; the Albertus wordmark is an SVG/image, not live type, so it holds its proportions at any width. Body text never changes from 10px — which means on narrow screens the facts table becomes the primary reading surface while the hero plate shrinks proportionally.

---

## 9. Agent Prompt Guide

> Build a UI in the Wild Week Athens style.

Set the canvas to `rgb(203, 203, 203)` (ash-grey limestone) and text to pure black. Use **Albertus Nova Light** at weight 300 for every headline and every body element — never switch weight, never switch family. All headings are uppercase with `+0.7px–+1px` letter-spacing. Body copy is tiny (10px), lightly tracked, set in the same face. Use `rgb(7, 85, 187)` — a saturated passport-blue — for links, logotype, and one full-bleed accent panel. Link hover darkens to `rgb(5, 68, 150)` with no background change. Content panels sit on warm stones in the `rgb(221, 220, 215)` family, stepped ~0.05 in luminance from the canvas — separation is tonal, never bordered, never shadowed. Use small border-radii only (`4px` / `8px`), never pills. Organise information as catalogue entries: single-letter indices (D / P / H / I) flush-left, values right-aligned. Treat the page like a museum placard — archaic, unhurried, and confident that the typographic voice is doing the whole job.

---

*Generated by Sparkbites — extracted from live CSS analysis*
