# varchive.ai — Design System

## 1. Visual Theme & Atmosphere

Varchive.ai presents as a refined AI archiving or knowledge tool — clean white primary surfaces with a deep navy/indigo dark layer for section variety. The atmosphere is focused and editorial: generous whitespace, a premium custom typeface, and a restrained color language that signals trust and precision over flashiness. The site avoids the typical "AI product" dark-everything aesthetic in favor of a light, confident foundation.

The standout typographic choice is **Aeonik Pro** — a precise, neutral geometric sans with Swiss modernist roots that elevates the product above standard system-font SaaS. Combined with micro-sized body copy (13px) and generous line heights, the reading experience feels considered and purposeful.

## 2. Color Palette & Roles

| Role | Token | Value | Usage |
|------|-------|-------|-------|
| **Canvas** | `--background` | `#ffffff` | Primary page background |
| **Primary text** | body color | `rgb(23,23,23)` | Near-black body copy |
| **Heading / dark** | header, links | `rgb(34,34,34)` | Headings, active states |
| **Secondary text** | `h3` color | `rgb(51,51,51)` | Subheadings, captions |
| **Footer surface** | oklab value | ~`rgba(0,0,0,0.07)` | Subtle dark footer tint |
| **Border/divider** | footer border | `oklab(0.999994 ... / 0.1)` | 10% opacity white-ish hairline |
| **Deep navy** | implied dark sections | `#251965` estimated | Dark section backgrounds |

The color system is almost entirely achromatic — near-black text on white, with a dark navy layer appearing in select sections. The use of `oklab()` for the footer surface is a modern CSS color space choice, indicating a technically sophisticated implementation.

**No accent color detected.** Interaction and emphasis are handled through typography weight and size, not color.

## 3. Typography Rules

**Typeface:** Aeonik Pro — a premium geometric sans with humanist touches. Used across all roles.

| Selector | Size | Weight | Line Height | Notes |
|----------|------|--------|-------------|-------|
| `h1` | 48px | 400 | 52.8px (1.1×) | Tight leading for display — precise |
| `h3` | varies | 400 | normal | Secondary heading |
| Body / p | 13px | 400 | 19.5px (1.5×) | Intentionally compact; micro-scale |
| Labels | 12px | 400 | normal | Smallest tier |
| `a` | 13px | 400 | normal | Links match body exactly |

The 13px body size is a deliberate choice — it signals information density and sophistication rather than accessibility-first thinking. The 1.1× line height on H1 creates dense display blocks. Aeonik Pro's neutral geometry ensures legibility even at small sizes.

**Notably absent:** No italic, no bold (weight 700), no letter-spacing adjustments, no uppercase styling — the typeface and size scale carry all hierarchy.

## 4. Component Stylings

- **Header** — transparent background over white canvas; dark `rgb(34,34,34)` text navigation
- **Footer** — subtle dark tint via `oklab()` color; hairline border at 10% opacity; understated closing
- **Labels** — form labels at 12px, matching the compact information-dense style
- **Sections** — implied alternation between white and deep navy surfaces for visual pacing
- **Inputs** — contextual; system styling inferred with Aeonik Pro applied

The component system appears minimal in CSS custom properties — likely inline Tailwind-style or a framework-driven approach, with Aeonik Pro doing heavy lifting for visual distinction.

## 5. Layout Principles

- **Spacing tokens:** 40px and 48px padding for section and header contexts — generous but not extravagant
- Likely centered content with max-width constraint (~1200–1440px range)
- Text-heavy sections with 13px compact body copy suggest multi-column or dense information layouts
- Hero likely features large 48px Aeonik Pro heading with brief subtext — quality over quantity approach
- No explicit grid tokens detected; framework-level layout assumed

## 6. Depth & Elevation

- **White → dark navy** — the primary depth model: light sections and dark sections alternate
- **Footer tint** — `oklab()` near-black at 7% opacity creates the softest possible surface distinction
- **Border at 10% opacity** — hairline-weight dividers; barely visible on white, just readable on dark
- No shadows detected — flat surface model throughout
- Aeonik Pro's inherent visual weight creates perceived elevation through typography alone

## 7. Do's and Don'ts

**Do:**
- Use Aeonik Pro as the sole typeface — its neutrality is the identity
- Keep body copy at 13px; resist bumping to 16px — density is intentional
- Use near-black (`#171717`) for text — never pure `#000000`
- Use `oklab()` for the subtlest surface tints — technically appropriate for modern CSS
- Alternate white and deep navy sections for long-page pacing

**Don't:**
- Add accent colors — the system communicates entirely through type and surface contrast
- Use font-weight 700 or bold; Aeonik Pro 400 is the sole weight
- Add shadows or border-radius to containers; the flat, precise aesthetic is deliberate
- Scale body copy above 13px — it would break the information-density character

## 8. Responsive Behavior

No breakpoints explicitly captured. Based on spacing scale (40–48px) and 13px body:

| Behavior | Context |
|----------|---------|
| Mobile | Single column; 48px headings scale to ~32–36px via responsive sizing |
| Desktop | Multi-column possible; dense data sections leverage full width |

The compact 13px body copy gives mobile layouts natural information density without needing font-size reduction.

## 9. Agent Prompt Guide

> "Design in the style of varchive.ai: pure white canvas `#ffffff`, near-black text `rgb(23,23,23)`, Aeonik Pro geometric sans throughout at weight 400, 48px/52.8px display headings, 13px/19.5px compact body copy, deep navy dark sections for contrast, hairline borders at 10% opacity using `oklab()`, no accent colors, no shadows, no bold weights — refined AI-tool aesthetic, Swiss precision, editorial restraint."

*Generated by Sparkbites — extracted from live CSS analysis*
