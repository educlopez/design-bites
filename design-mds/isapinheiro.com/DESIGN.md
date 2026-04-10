# isapinheiro.com — Design Language

## 1. Visual Theme & Atmosphere

Isa Pinheiro's portfolio is a study in cinematic darkness. Built in Framer, the site uses near-total black as its ground — not the fashionable off-black of most dark portfolios, but a true ink-deep `rgb(9, 8, 11)` that reads almost as void. Against it, white text and white-on-dark photography create maximum contrast with zero compromise. The visual language is editorial — sparse, deliberate, unhurried. Large section padding (392px top) signals content that arrives with patience, not urgency. This is a portfolio that breathes deeply between moments.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Base background | `rgb(9, 8, 11)` — near void black | Body, dark sections |
| Text / headings | `rgb(255, 255, 255)` — pure white | h1 and primary content |
| Light surface | `rgb(255, 255, 255)` — white | Card or highlight panels |
| Mid-dark surface | `rgb(46, 46, 46)` — dark charcoal | Secondary content panels |
| Deep surface | `rgb(9, 8, 11)` — matching body | Immersive hero zones |

Three surface levels — void, charcoal, white — give the layout depth without color. No warm tones, no brand hues. The white is a spotlight, not an ambient fill.

**What's absent:** No accent colors, no gradients, no tinted overlays, no shadows, no border-radius.

## 3. Typography Rules

A single family — **Helvetica Now Display Regular** — carries all primary content. This is a deliberate professional choice: the "Display" optical size is optimised for large rendering, giving clean curves and open counters that hold up at headline scale.

| Element | Family | Size | Weight | Line-height |
|---|---|---|---|---|
| h1 / Headings | Helvetica Now Display Regular | 48px | 400 | 53.76px (1.12) |
| Body / p | Helvetica Now Display Regular | 14px | 400 | 19.32px (1.38) |
| Navigation / links | sans-serif (system) | 12px | 400 | normal |

Weight is uniformly Regular (400) — there is no bold. Hierarchy is created through size alone, not weight contrast. The 14px body at 1.38 line-height is tight but readable for short passages. No letter-spacing adjustments; no text transforms.

**What's absent:** No italic usage, no bold, no monospace, no decorative display fonts.

## 4. Component Styling

- **Framer-powered layout:** Components are positioned absolutely within Framer's canvas model.
- **No border-radius** detected anywhere — all surfaces are sharp-cornered.
- **No box-shadows** — elevation is conveyed through color contrast between surfaces alone.
- **Links** default to `rgb(0, 0, 238)` (browser blue) for navigation items like "About" and "Work" — an intentional anti-design move, leaning into raw web vernacular.
- **Focus states** use the default browser outline (`rgb(0, 95, 204) auto 1px`) without customisation.
- **Section spacing** is generous: 392px top padding on sections, 68px horizontal — content is an event, not a feed.

## 5. Layout Principles

- Framer canvas with absolute positioning — not a flow-based document layout.
- Breakpoints at 0px, 809–810px, and 1199–1200px, indicating three distinct layout states: mobile, tablet, desktop.
- Footer sits close to the bottom with `padding: 0 68px 25px` — same horizontal rhythm as sections.
- The near-zero `gap: 8px` on sections and footer suggests stacked content groups with tight internal spacing but large outer breathing room.
- No grid framework; layout is compositional and viewport-relative.

## 6. Depth & Elevation

Depth is achieved through surface luminance steps: void (0.034) → charcoal (0.18) → white (1.0). No shadows, no blur, no z-axis trickery. The three surfaces create a clear foreground/midground/background reading without requiring any additional visual effects. Interactive states rely on Framer Motion animations, not CSS shadow transitions.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(9, 8, 11)` as the default background — not `#000`, not `#111`. The near-void is specific.
- Keep all text in pure white or system-link blue on dark surfaces.
- Pair large section padding (300px+) with compact body text (14px) for editorial pacing.
- Let Framer Motion handle all transitions — avoid CSS keyframes here.

**Don't:**
- Add border-radius — every surface is sharp.
- Introduce warm tones or accent colors; the palette is deliberately achromatic.
- Use font weights above 400 — this design communicates through scale, not weight.
- Reduce section top padding to "fix whitespace" — the breathing room is the design.

## 8. Responsive Behavior

Three breakpoints define three layout states. The headline (48px) likely scales down significantly on mobile. The 68px horizontal padding on sections compresses at the 810px breakpoint. At mobile (below 810px), the absolute Framer layout reflows to a stacked single-column arrangement. Navigation items ("About", "Work") likely collapse or become a toggle at narrow widths.

## 9. Agent Prompt Guide

> Build a portfolio page in the style of isapinheiro.com: near-void black background (`rgb(9, 8, 11)`), pure white headings, Helvetica Now Display Regular at 48px/weight 400 for hero. Body text at 14px/1.38 line-height. No bold, no italic, no border-radius, no shadows. Three surface levels: void, `rgb(46,46,46)` charcoal, and white. Sections have 392px top padding and 68px horizontal padding — layout is expansive and cinematic. Use browser-default blue for navigation links as a deliberate vernacular choice.

---

*Generated by Sparkbites — extracted from live CSS analysis*
