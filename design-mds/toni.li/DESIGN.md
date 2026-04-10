# toni.li — Design System

## 1. Visual Theme & Atmosphere

Toni.li reads as a warm minimalist personal site — the kind of space that feels handcrafted rather than templated. A transparent canvas lets the browser's default white show through, while a sand-beige card tone (`rgba(198, 188, 169, 0.1)`) gives groupings a faint warmth without committing to a colored background. Text sits in a desaturated warm brown (`rgb(72, 71, 70)`) rather than pure black, softening the reading experience and evoking aged paper.

The type stack is entirely system UI — no custom fonts loaded. This is a deliberate choice: the site trusts the user's operating system to provide the right typeface, keeping the bundle lean and the rendering native. Built with Tailwind CSS and SvelteKit, the design feels understated and fast.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| **Canvas** | transparent / `#fff` (browser default) | Page background |
| **Primary text** | `rgb(72, 71, 70)` | Header, nav, body copy |
| **Warm card** | `rgba(198, 188, 169, 0.1)` | List/card groupings — barely-there warmth |
| **Border** | `rgb(229, 231, 235)` | Hairline separators (Tailwind `gray-200`) |
| **Input surface** | contextual | Form fields inherit system styling |

The palette is deliberately restrained — no accent color beyond the warm card tint. Hierarchy comes from contrast between `rgb(72,71,70)` text and the near-white background, not from color variation. Any link or interactive accent would stand out dramatically against this neutral base.

## 3. Typography Rules

**Typeface:** System UI stack — `system-ui, -apple-system, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue`. No custom fonts.

| Selector | Size | Weight | Line Height | Notes |
|----------|------|--------|-------------|-------|
| `body` | 16px | 400 | 24px (1.5×) | Ideal reading rhythm |
| `p` | 16px | 400 | 24px | Matching body — consistency above all |
| `a` | 16px | 400 | 24px | Same as prose; links blend into text |
| `button` | 16px | varies | 24px | System font, no custom button styling |

No letter-spacing, no text-transform, no weights above 400 detected. The heading scale wasn't captured distinctly — likely matches the 16px / 24px rhythm or steps to 20–24px naturally.

**Notably absent:** No custom typeface, no display size above ~24px, no italic or uppercase styles.

## 4. Component Stylings

Tailwind's utility classes style components inline; no CSS custom properties for components.

- **Navigation** — transparent background, warm brown text, hairline bottom border in `rgb(229,231,235)`
- **List groups** — `rgba(198,188,169,0.1)` warm-tinted background, subtle visual grouping without hard borders
- **Buttons/inputs** — inherit system UI styling; likely minimal custom treatment
- **Links** — full-width 16px, no underline override evident; blend into running text

## 5. Layout Principles

- **Two breakpoints:** `640px` and `768px` — Tailwind's `sm` and `md` breakpoints
- Single-column centered layout likely at all sizes; content width constrained to ~`365px` on mobile contexts
- `64px` gap / padding values used for section spacing
- `2px` gap for tight inline groupings
- Padding-first layout model typical of Tailwind compositions

## 6. Depth & Elevation

No shadows. No border-radius detected. Depth is achieved through:

1. **The warm card tint** — `rgba(198,188,169,0.1)` is barely perceptible, acting as a gentle grouping layer
2. **Border hairlines** — `rgb(229,231,235)` single-pixel dividers define separation without visual weight
3. **Typographic rhythm** — consistent 1.5× line height creates vertical breathing room that reads as spaciousness

## 7. Do's and Don'ts

**Do:**
- Use `rgb(72,71,70)` for all text — never pure black
- Use system fonts; the lean load time is part of the brand
- Keep all type at 16px / 24px line height for reading comfort
- Use hairline borders (`rgb(229,231,235)`) as the only visual separator
- Apply the warm tint sparingly — one grouping layer per view

**Don't:**
- Load a custom typeface — it breaks the system-native aesthetic
- Introduce color accents without considered intent; this palette is silent
- Use `font-weight: 700` or bold in running text
- Add shadows or elevation layers — the design is deliberately flat
- Use uppercase or tracked text for labels

## 8. Responsive Behavior

| Range | Behavior |
|-------|----------|
| `< 640px` | Mobile single column |
| `640px – 767px` | Tailwind `sm` — likely wider single column |
| `≥ 768px` | Tailwind `md` — may introduce a sidebar or two-column layout |

At all sizes, the type scale remains 16px — no responsive font scaling detected.

## 9. Agent Prompt Guide

> "Design in the style of toni.li: transparent/white canvas, all text in warm desaturated brown `#484746`, system UI font stack at 16px/24px line height, weight 400 throughout, warm card groupings at 10% `rgba(198,188,169)`, hairline borders in `#e5e7eb`, no shadows, no custom typeface, no accent colors — minimal, personal, native-feeling."

*Generated by Sparkbites — extracted from live CSS analysis*
