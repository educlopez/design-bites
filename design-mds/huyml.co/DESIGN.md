# huyml.co — Design System Reference

## 1. Visual Theme & Atmosphere

Huy Phan's portfolio ("Award-winning designer", launched 2023, with FWA, CSSDA and Behance recognition) is built in Framer and treats colour as a rotating swatch library. The base is a flat light gray, `rgb(236, 236, 236)`, and onto it the site drops project panels in saturated reds, electric blue, lime, lavender, pink and deep navy. Type is tiny: 12px body, with a custom display face, BT Glyphius, set uppercase at 23px for headings, and a custom grotesk, BT Grotesk Medium, for copy and buttons. The result reads like a brand sample book: small, controlled typography framing big blocks of colour.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(236, 236, 236)` — page background
- `rgb(0, 0, 0)` — body text
- `rgb(24, 24, 24)` — button text
- `rgb(255, 255, 255)` — heading text (over dark or coloured panels)

**Neutral surfaces**
- `rgb(255, 255, 255)`, `rgb(255, 253, 226)` (warm cream), `rgb(235, 232, 226)`, `rgb(227, 232, 236)`, `rgb(229, 227, 219)`, `rgb(219, 216, 205)`

**Dark surfaces**
- `rgb(0, 0, 0)`, `rgb(20, 20, 20)`, `rgb(33, 33, 37)`, `rgb(38, 38, 38)`, `rgb(61, 61, 61)`, `rgb(5, 18, 54)` (midnight navy), `rgb(26, 44, 70)`, `rgb(28, 20, 86)`

**Project colour panels (the accent system)**
- Blues: `rgb(4, 87, 212)`, `rgb(0, 112, 255)`, `rgb(60, 40, 227)`, `rgb(0, 211, 255)`
- Reds and oranges: `rgb(186, 55, 55)`, `rgb(255, 0, 0)`, `rgb(255, 90, 54)`, `rgb(255, 101, 66)`
- Lime and yellow: `rgb(206, 255, 69)`, `rgb(223, 255, 107)`, `rgb(247, 226, 115)`, `rgb(250, 237, 188)`
- Pinks and purples: `rgb(251, 193, 212)`, `rgb(195, 171, 255)`, `rgb(199, 179, 255)`
- Earth tones: `rgb(185, 189, 171)`, `rgb(213, 200, 176)`

Link text reads `rgb(0, 0, 238)`, the browser default blue; the extractor found links left unstyled at the element level.

---

## 3. Typography Rules

Two proprietary faces, both at small sizes.

| Role    | Font                | Size | Weight | Line-height | Tracking | Transform |
|---------|---------------------|------|--------|-------------|----------|-----------|
| H2      | BT Glyphius Regular | 23px | 400    | 23px        | 0.23px   | uppercase |
| P       | BT Grotesk Medium   | 12px | 500    | 15.6px      | 0.12px   | none      |
| Button  | BT Grotesk Medium   | 12px | 500    | 12px        | normal   | none      |
| Body    | sans-serif fallback | 12px | 400    | normal      | normal   | none      |

A custom property, `--bt-grotesk-responsive-font-size: 12px`, drives the grotesk size.

**Principles**
- Headings use solid line-height (23px on 23px) and uppercase, giving a compact, poster-like line.
- Copy tracking is slightly open (0.12px, 1% of size).
- Hierarchy comes from face and case rather than from size jumps.

---

## 4. Component Stylings

**Menu button** (`btnmenu`)
- Transparent background, white text; focus shows a 1px auto outline

**Project links** (e.g. studio names)
- Transparent background; text is the default link blue `rgb(0, 0, 238)`

**Project panels**
- Rounded `8px` containers filled with one of the swatch colours above

**Border radius**
- `8px` only.

**Shadows**
- None detected.

---

## 5. Layout Principles

- Page structure is a Framer layout of absolutely controlled panels (`framer-*` classes) over the gray canvas.
- Body padding and margin are `0`; spacing is set by the Framer frames.
- An unusually dense breakpoint ladder: 800, 1099, 1100, 1199, 1200, 1439, 1440, 1799, 1800, 1919, 1920, 2199, 2360, 2399, 2400 — the layout is tuned for large and ultra-wide monitors.
- Content is a numbered "Selected work" index (01, /00) with category and title lines.

---

## 6. Depth & Elevation

Flat. No shadows. Layering comes entirely from colour planes: light neutrals (luminance 0.85 to 1.0) against saturated and near-black panels (luminance 0 to 0.37), plus Framer Motion transitions between them.

---

## 7. Do's and Don'ts

**Do**
- Start from the `rgb(236, 236, 236)` canvas.
- Use full-panel colour fills, one per project, drawn from the palette.
- Set display headings in an uppercase condensed-style face at about 23px with solid leading.
- Keep body copy at 12px with a medium-weight grotesk.
- Round panels at `8px`.

**Don't**
- Don't use shadows.
- Don't mix more than one swatch colour inside a single panel.
- Don't scale headings dramatically; keep the small-type scale.
- Don't leave links in default blue on a final build; the source site does, but it is not a brand colour.

---

## 8. Responsive Behavior

Breakpoints from 800 up to 2400 show that the site adapts at many widths, with extra attention paid to 1100, 1200, 1440, 1800, 1920 and 2400. Typography stays at 12px/23px sizes throughout, so scaling is handled by Framer's frame sizing rather than by fluid type.

---

## 9. Agent Prompt Guide

> Build a UI that matches huyml.co's design language.

Set the page background to `rgb(236, 236, 236)` with black text. Use a custom display face (BT Glyphius, or a compact grotesque substitute) for H2s at 23px/23px, uppercase, 0.23px tracking, white on dark or coloured panels. Use a medium-weight grotesk (BT Grotesk Medium) at 12px, weight 500, line-height 15.6px for copy and buttons. Build the page as a stack of `8px`-radius colour panels, each in a single bold swatch: blue `rgb(4, 87, 212)`, lime `rgb(206, 255, 69)`, red `rgb(186, 55, 55)`, lavender `rgb(195, 171, 255)`, pink `rgb(251, 193, 212)`, navy `rgb(5, 18, 54)`. No shadows. Number the work index (01, 02, ...) and keep labels tiny. Let colour blocks provide the drama and keep type small and tight.

---

*Generated by Sparkbites — extracted from live CSS analysis*
