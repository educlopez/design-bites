# Cuvii Labs — Design System Reference

## 1. Visual Theme & Atmosphere

Cuvii Labs presents itself as a "Signal interface effects gallery," and the whole page behaves like an instrument panel. The canvas is true black (`lab(0 0 0)`) with white text, and every piece of copy is set in Departure Mono, a pixel-flavored monospace. Telemetry-style readouts frame the page: labels such as `SCAN018`, `FMT 1680`, `COLS06`, `X 0000`, `Y 0000`, `RES 0000×0000`, `DPR 0` and a `[+] LABS · cuvii` mark make the interface feel like a calibrated lab console. The intro line, "This is lab work I made with AI," and the Traditional Chinese subtitle (實驗室 BY CUVII) add a quiet, honest tone. Effects and motion are the product; the chrome stays out of their way with tiny type, hairline insets and a restrained grayscale.

---

## 2. Color Palette & Roles

Colors are expressed in the `lab()` color space and are essentially neutral.

- `lab(0 0 0)` — page canvas (pure black)
- `lab(100 0 0)` — primary text, nav and borders (pure white)
- `lab(5.81 -0.29 -0.88)` — header surface (near-black, a hair cool)
- `lab(39.45 -0.25 -0.71)` — footer text and inset outlines (dim gray)
- `lab(59.83 -1.04 -5.12)` — figcaption text (cool mid-gray)
- `rgb(201, 201, 203)` — the `.blinky` surface (light gray indicator element, luminance 0.789)

Outlines are drawn with white at low alpha: `lab(100 0 0 / 0.12)` and `lab(100 0 0 / 0.08)` as 1px inset rings, and `lab(14.16 -0.48 -1.41)` as a 1px dark ring. There is no chromatic accent; color lives inside the effects themselves.

---

## 3. Typography Rules

One family for everything: **Departure Mono**, with Noto Sans TC (and PingFang TC / Microsoft JhengHei) as the CJK fallback, then system monospace.

| Role       | Size | Weight | Line-height | Tracking | Transform |
|------------|------|--------|-------------|----------|-----------|
| H1 / Body / P | 16px | 400 | 24px | normal | none |
| Link       | 16px | 400    | 16px        | normal   | none      |
| Button     | 12px | 400    | 12px        | 1.68px   | uppercase |
| Figcaption | 10px | 400    | 10px        | 1.2px    | none      |

**Principles**
- H1 is the same size as body (16px). There is no display scale; hierarchy is created by caps, tracking and tone.
- Buttons are uppercase 12px with wide 1.68px tracking, reading like control labels.
- Captions drop to 10px with 1.2px tracking, like instrument annotations.
- Weight is always 400.

---

## 4. Component Stylings

**Buttons**
- Transparent background, white text, uppercase 12px Departure Mono, 1.68px tracking
- Defined by 1px inset rings (`lab(100 0 0 / 0.12)`), not fills

**Nav and links**
- White on black, 16px mono, no decoration captured

**Figcaptions**
- 10px, `lab(59.83 -1.04 -5.12)` cool gray, 1.2px tracking

**Status indicators**
- `.blinky` element in `rgb(201, 201, 203)` acts as a blinking indicator light

**Border radius**
- A single fully-round value (pill/circle) for indicators and chips.

**Shadows**
- Only inset 1px rings used as borders. No drop shadows.

---

## 5. Layout Principles

- A declared grid: `--grid-format: 1680px`, 6 columns, 32px margin, 16px gutter, 8px baseline.
- Shell max width follows the grid format (1680px); the gallery rail is inset 40px; the top bar is `2rem` tall.
- Sections carry 24px top padding, the footer 4px; body and main have no padding.
- Everything snaps to the 8px baseline, which is why the readouts feel mechanical.
- A `--boot-frame` variable hints at an animated boot sequence driving the load state.

---

## 6. Depth & Elevation

Depth is expressed through luminance steps and hairline rings rather than shadow:
- Pure black canvas, a near-black header (`lab(5.81 ...)`), then gray footer text.
- 1px inset rings at 8% and 12% white to separate cells.
- The gallery effects themselves provide the depth and motion; the frame stays flat.

---

## 7. Do's and Don'ts

**Do**
- Use true black and white with a mono typeface throughout.
- Keep small, uppercase, widely tracked labels for controls.
- Show telemetry readouts (coordinates, resolution, DPR, format) as part of the UI.
- Separate cells with 1px translucent white rings.
- Respect the 8px baseline and 6-column grid.

**Don't**
- Don't introduce a proportional typeface or heavy weights.
- Don't add accent colors or drop shadows; let the effects supply color.
- Don't enlarge the headline; H1 stays at body size.
- Don't use filled buttons.

---

## 8. Responsive Behavior

Breakpoints at **720 and 900px**. The 1680px grid with 32px margins compresses down through these two steps, and type sizes (16 / 12 / 10px) are constant, so the interface stays dense and instrument-like at every width.

---

## 9. Agent Prompt Guide

> Build a UI that matches Cuvii Labs' design language.

Use a pure black canvas `lab(0 0 0)` and white text `lab(100 0 0)`. Set everything in **Departure Mono** (fallback Noto Sans TC, then system monospace) at weight 400: 16px body and H1 with 24px line-height, 12px uppercase buttons with 1.68px tracking, 10px captions with 1.2px tracking in a cool gray `lab(59.83 -1.04 -5.12)`. Build on a 6-column grid, 1680px max, 32px margin, 16px gutter, 8px baseline. Define controls with 1px inset white rings at 8-12% alpha, never fills or shadows. Add telemetry readouts (SCAN, FMT, COLS, X/Y, RES, DPR) and a blinking gray indicator `rgb(201, 201, 203)`. Keep the frame neutral so the effects are the only thing with color.

---

*Generated by Sparkbites — extracted from live CSS analysis*
