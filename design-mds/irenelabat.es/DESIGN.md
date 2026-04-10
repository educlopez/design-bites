# irenelabat.es — Design Language

## 1. Visual Theme & Atmosphere

Irene Labat's portfolio is built on controlled darkness and expressive type — a Spanish creative director's digital voice translated into extreme typographic scale. The dominant feeling is theatrical: near-black backgrounds recede into near-invisibility while oversized display text fills the viewport like a cinema title card. There is no decoration; the work is the decoration. Every choice points toward restraint in structure and extravagance in letterforms. The palette is intentionally limited to two tones — dark and bone — so the typography can breathe without competition.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(39, 34, 36)` — deep charcoal-brown | Page canvas, body |
| Foreground / Text | `rgb(238, 233, 221)` — warm bone | All text, borders, nav |
| Surface accent | `rgb(238, 233, 221)` — same bone | Divider, content blocks |
| Transparent overlay | `rgba(0, 0, 0, 0)` | Header, floating layers |

The palette is binary: background against foreground, nothing else. No grays, no tints, no accent hues. The bone white reads warm against the brown-black, avoiding the cold sterility of pure #fff on #000. This warmth is the only color personality.

**What's absent:** No accent colors, no gradients, no shadows, no success/error states.

## 3. Typography Rules

The site makes a single typeface family — **PolySans** — do all the work, but in radically different cuts:

| Cut | Usage | Size |
|---|---|---|
| `polysans-slimwide` | Hero display headings (h2) | ~243px, line-height 1:1, tracking −4.87px |
| `polysans-slim` | Section headers (h4) | ~55px, line-height 1:1 |
| `polysans-italic` | Body or contrast type | — |
| `polysans-neutral`, `polysans-median` | Supporting text | — |
| `polysans-bulkywide`, `polysans-neutralwide` | Potentially decorative | — |

The headline tracking is aggressively negative (−4.87px at 243px), pulling letters into near-ligature contact. Line heights match font size exactly (1:1), creating tight typographic blocks that behave like graphic elements. No mixed-family pairing — PolySans alone handles the full typographic range.

**What's absent:** No serif, no monospace, no system fallback beyond `sans-serif`.

## 4. Component Styling

- **Navigation links** transition via opacity to `0.65` plus a horizontal translate (`+15.9px`) on focus — a subtle rightward drift that signals interactivity without changing color.
- **Buttons / CTAs:** No dedicated button surface detected. Actions are likely typographic links.
- **Work items:** Navigation items are numbered text labels (e.g., "01. Violeta") — the numbering is the UI.
- **Borders:** Used as structural lines, always in bone `rgb(238, 233, 221)`, never decorative.
- **No cards, no shadows, no rounded corners.**

## 5. Layout Principles

- Full-bleed sections with zero default padding on `main`, `section`, and `footer`.
- Header uses `30px 0` padding — minimal vertical breathing room at top.
- Breakpoints: 576px, 600px, 768px, 950px, 1024px — a dense responsive ladder suggesting careful reflow of oversized type at each step.
- Layout is likely a vertical scroll of full-screen sections, each dominated by a single headline.
- The WordPress-based architecture suggests custom block templates rather than a CSS framework.

## 6. Depth & Elevation

This site lives entirely in 2D. No shadows, no blur, no elevation. Depth is achieved typographically — scale creates hierarchy, proximity creates grouping. The near-black background is the "floor"; text floats above it by pure contrast. Interactive feedback uses opacity and translation instead of shadow or glow.

## 7. Do's and Don'ts

**Do:**
- Use `polysans-slimwide` for hero text only — its condensed width and negative tracking are for large scale.
- Maintain the binary palette strictly. Add nothing that isn't bone or near-black.
- Keep line-heights at or near 1:1 for display sizes.
- Use opacity + translate for hover/focus states, not color changes.

**Don't:**
- Introduce rounded corners or card surfaces — this design has zero border-radius.
- Add box-shadows or drop-shadows of any kind.
- Use color to signal state — opacity is the signal here.
- Mix in a second typeface family; PolySans's width variety is the contrast system.

## 8. Responsive Behavior

The dense breakpoint ladder (576, 600, 768, 950, 1024px) indicates the 243px headline shrinks progressively — likely stepping down through the `--h*` custom property scale (h380 → h290 → h200 → h98 → h83 → h60). At mobile widths the typographic block reflows to fill the narrower viewport while preserving the 1:1 line-height rhythm. Header padding likely increases proportionally to prevent optical compression.

## 9. Agent Prompt Guide

> Build a portfolio section in the style of irenelabat.es: near-black background (`#272224`), bone text (`#EEE9DD`), no shadows, no rounded corners. Use a wide condensed display font at extreme scale (200px+) with −4px to −5px letter-spacing and 1:1 line-height. Navigation uses numbered text labels. Interactive states change opacity to ~0.65 and translate +16px horizontally — no color shift. Layout is full-bleed vertical sections with minimal padding. No accent colors, no gradients, no decorative elements.

---

*Generated by Sparkbites — extracted from live CSS analysis*
