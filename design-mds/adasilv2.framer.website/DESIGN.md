# adasilv2.framer.website — Design System

## 1. Visual Theme & Atmosphere

This is a Framer-built portfolio — and it shows in the best way. The design language is soft, rounded, and playful without being juvenile. An off-white near-neutral base (`rgb(251, 251, 251)`) provides the canvas, while a curated set of pastel and saturated blues creates pockets of color that feel hand-placed. An unexpected orange accent (`rgb(254, 99, 1)`) provides the only warm note, used sparingly as a punctuation mark against the cool blue family.

The overall atmosphere is contemporary creative portfolio: approachable, visually curious, and structured by a confident use of card-based sections with generous border radii. DM Sans at tight negative tracking gives the typography a modern editorial edge. This is a designer showcasing taste as much as work.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Background | `rgb(251, 251, 251)` | Page base — near-white, not stark |
| Text / Ink | `rgb(0, 0, 0)` | Primary text and borders throughout |
| Surface White | `rgb(255, 255, 255)` | Cards, elevated containers |
| Surface Off-White | `rgb(251, 251, 251)` | Secondary panels, same as background |
| Surface Subtle Gray | `rgb(247, 247, 247)` | Nested card insets |
| Surface Light Gray | `rgb(245, 245, 245)` | Tertiary sections, dividers |
| Accent Blue (primary) | `rgb(74, 119, 255)` | Primary interactive/highlight element |
| Accent Blue (pale) | `rgb(193, 220, 250)` | Soft background zones, tinted cards |
| Accent Blue (lighter) | `rgb(187, 221, 255)` | Secondary blue panel variant |
| Accent Blue (palest) | `rgb(204, 238, 255)` | Tinted backgrounds, tag chips |
| Accent Orange | `rgb(254, 99, 1)` | Single warm accent — used for emphasis |
| Link (default) | `rgb(0, 0, 238)` | Undecorated browser-default link color |

**What's absent:** No greens, no purples, no reds beyond the orange. The palette is tight — a monochromatic blue range plus one warm pop, grounded by near-blacks and near-whites. The unoverridden link blue (`rgb(0, 0, 238)`) is likely not visible to users; it signals that links are wrapped in custom-styled components.

## 3. Typography Rules

DM Sans is the primary typeface, loaded as a webfont, and it drives all meaningful text:

- **Paragraphs / Display text:** `"DM Sans"` — 28px / weight 600 / line-height 31.2px / letter-spacing **-1.12px**
- **Body / Base:** `sans-serif` — 12px / weight 400 / normal — a generic fallback, not meant to be seen
- **Buttons / Links:** Inherit `sans-serif` at 12px — likely overridden by component-level styles in Framer

**Key insight:** The `p` selector with 28px at weight 600 and -1.12px tracking is almost certainly a hero or section headline mapped to the paragraph tag in Framer's canvas output. The tight negative kerning (-4% at 28px) is a strong stylistic choice — it compresses letters just enough to feel designed rather than typeset.

The 12px base body implies Framer's default system font is vestigial; all real typography is applied via Framer component overrides at a higher specificity level.

## 4. Component Styling

Border radius is a defining trait of this design — multiple values coexist, each serving a different component size:

| Radius Value | Likely Component |
|-------------|-----------------|
| `100px` | Pills, tags, full-round buttons |
| `80.23%` | Circle avatars or icon containers |
| `26px` | Large cards, hero sections |
| `14px` | Medium cards, modals |
| `12px` | Input fields, small cards |
| `10px` / `10.8px` | Buttons, chips |
| `8px` | Small utility elements |

- **Buttons** use `rgba(0, 0, 0, 0.18)` — a semi-transparent dark fill that works on any background without hardcoding a color.
- **No shadows detected** — depth comes from background color layering across the surface scale, not elevation.
- **Interactive states** were not fully captured; Framer typically handles these with motion/transform, not CSS pseudo-class changes.

## 5. Layout Principles

Built in **Framer** with **Framer Motion** — layout is canvas-based rather than CSS-grid-driven:

- Breakpoints: `809.98 / 810 / 1199.98 / 1200 / 1648.98px` — Framer's precise fractional breakpoints are characteristic of its responsive canvas system. The paired `N.98 / N` values indicate Framer's max-width/min-width breakpoint bracketing.
- Three major layout zones: mobile (≤810px), tablet (810–1200px), desktop (1200–1648px), and large desktop (≥1648px).
- Section padding at 15px on `section` elements — modest, relying on internal component spacing for breathing room.
- Card-based layout with nested surfaces (white → off-white → subtle gray) creates visual depth without shadows.

## 6. Depth & Elevation

No box shadows are present, yet the design feels layered. This is achieved through the **surface luminance cascade**:

1. `rgb(255, 255, 255)` — topmost cards (luminance 1.0)
2. `rgb(251, 251, 251)` — page background / secondary panels (0.984)
3. `rgb(247, 247, 247)` — inset elements (0.969)
4. `rgb(245, 245, 245)` — deepest gray layer (0.961)

Each step is a 1.5–2% luminance drop — subtle enough to feel atmospheric rather than structural. Combined with generous border radius and Framer Motion's enter animations, the result reads as layered without needing shadows.

## 7. Do's and Don'ts

**Do:**
- Use DM Sans at weight 600 with negative letter-spacing (-1.12px at 28px) for all display text.
- Layer background surfaces using the luminance cascade: white → 251 → 247 → 245.
- Use the blue accent family (`rgb(74, 119, 255)` and its pastel variants) for color blocks and highlights.
- Apply `100px` radius for pills and tags; `14–26px` for cards and sections.
- Use `rgba(0, 0, 0, 0.18)` for button fills — it adapts to any surface color.
- Reserve `rgb(254, 99, 1)` orange for a single punctuation point; never use it broadly.

**Don't:**
- Use shadows — the design deliberately avoids them.
- Use `rgb(0, 0, 238)` for visible links; override with the blue accent palette.
- Mix border-radius scales arbitrarily — each value corresponds to a component size tier.
- Use the 12px sans-serif body as a real text style; all content type should be DM Sans.
- Add additional colors beyond the blue family + orange — the palette is intentionally contained.

## 8. Responsive Behavior

Framer's canvas-based responsive system produces five breakpoint zones:

- **Mobile** (≤809px): Single-column stack, full-width cards
- **Tablet** (810–1199px): Likely 2-column grid or mixed layout
- **Desktop** (1200–1648px): Full multi-column with sidebar or grid
- **Large Desktop** (≥1648px): Expanded canvas, wider gutters

The fractional breakpoints (`809.98`, `1199.98`) are Framer-specific — they prevent simultaneous rule firing at exact pixel boundaries. When replicating outside Framer, round to the nearest integer.

Typography may scale across breakpoints via Framer's built-in responsive text nodes, even though this wasn't captured in the CSS extraction.

## 9. Agent Prompt Guide

Use this when generating UI in the style of adasilv2.framer.website:

> Build a modern creative portfolio UI with a Framer aesthetic. Background: `rgb(251, 251, 251)`. Text: black. Use DM Sans, weight 600, 28px, -1.12px letter-spacing for all headings. Layer card surfaces from white → 247 → 245 for depth without shadows. Accent with a blue family: primary `rgb(74, 119, 255)`, soft `rgb(193, 220, 250)`, pale `rgb(204, 238, 255)`. Add one orange moment: `rgb(254, 99, 1)`. Border radius: 100px pills, 26px large cards, 12–14px standard cards. Buttons: `rgba(0,0,0,0.18)`. Five responsive breakpoints at 810/1200/1648px. The philosophy: soft layering, tight type, a color palette that feels curated not computed.

---

*Generated by Sparkbites — extracted from live CSS analysis*
