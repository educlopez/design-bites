# noeinoi.com — Design System

## 1. Visual Theme & Atmosphere

Noeinoi.com operates from a mature, well-structured design system it calls HDS (Hanzo Design System, inferred from the `--hds-` prefix). The aesthetic is dark-first: deep charcoal (`#111111`) as the base reference color, white as the pure inverse. What lifts this above a simple dark theme is the single signature element — a rainbow gradient that arcs across 120 degrees through the full visible spectrum. This gradient is neither decoration nor gimmick; it's the brand marker, the one moment of controlled chaos in an otherwise disciplined monochrome system. The overall mood is confident, modern, and technically precise — the kind of design language a creative studio or SaaS product would choose when they want to appear both serious and memorable.

## 2. Color Palette & Roles

The palette is built on two poles — absolute dark and pure light — with opacity as the primary modulation tool.

| Role | Value | Usage |
|---|---|---|
| Dark Base | `#111111` | Primary surface, text on light, icon fills |
| Dark 80% | `rgba(17 17 17 / .8)` | Secondary text, muted elements |
| Dark 60% | `rgba(17 17 17 / .6)` | Tertiary copy, disabled states |
| Dark 40% | `rgba(17 17 17 / .4)` | Borders, dividers |
| Dark 20% | `rgba(17 17 17 / .2)` | Subtle separators |
| Dark 10% | `rgba(17 17 17 / .1)` | Hover states, background fills |
| Dark 5% | `rgba(17 17 17 / .05)` | Ghost surfaces |
| Light Base | `#ffffff` | Page background, text on dark |
| Light 80% | `rgba(255 255 255 / .8)` | Overlay content |
| Light 60–5% | Stepped alphas | Progressive surface hierarchy |
| Semantic Green | `--hds-ref-color-green-50` | Success states |
| Semantic Red | `--hds-ref-color-red-50` | Error / destructive |
| Semantic Yellow | `--hds-ref-color-yellow-50` | Warning |
| Semantic Blue | `--hds-ref-color-blue-50` | Info / links |
| **Rainbow Gradient** | `linear-gradient(120deg, #ff124f → #ff7a00 → #ffe600 → #19ffb6 → #00c3ff → #8a2bff → #ff00f0 → #ff124f)` | Brand accent, hero treatment |

**What's absent:** No named brand color beyond the gradient. The chromatic identity lives entirely in that one gradient; everything else is achromatic.

## 3. Typography Rules

- **Body / UI:** System UI stack — `-apple-system, system-ui, Segoe UI, Roboto, sans-serif`. Clean, neutral, readable. No custom typeface was loaded for body copy.
- **Font scale:** Token-driven via `--hds-ref-font-size-*` and `--hds-sys-font-size-*`.

| Token | Size | System Alias |
|---|---|---|
| `--hds-ref-font-size-80` | ~80px | Hero display |
| `--hds-ref-font-size-60` | ~60px | Large headings |
| `--hds-ref-font-size-46` | ~46px | Section headings |
| `--hds-ref-font-size-36` | 36px | `--hds-sys-font-size-xl` |
| `--hds-ref-font-size-24` | 24px | `--hds-sys-font-size-ex-med` |
| `--hds-ref-font-size-20` | 20px | Sub-headings |
| `--hds-ref-font-size-18` | 18px | Lead body |
| `--hds-ref-font-size-16` | 16px | Body default |
| `--hds-ref-font-size-12` | 12px | Captions, labels |

The font scale is wide (12–80px) and aliased through semantic tokens — a hallmark of a mature component-based design system.

## 4. Component Stylings

- **Surfaces:** Theme surface uses `--hds-sys-color-primary-default`; on-surface text uses `--hds-sys-color-secondary-default`. Light/dark inversion is baked in at the token level.
- **Opacity system:** Nine opacity steps (5a–90a) enable consistent transparency effects without ad-hoc alpha values.
- **Spacing:** `--hds-ref-size-*` and `--hds-sys-spacing-*` tokens (xs through 80px+) drive all padding and gap values.
- **Rainbow gradient:** Applied as a surface treatment or border — expect it on CTAs, hero banners, or decorative hr elements.
- **Dark mask:** `--hds-sys-color-theme-mask` creates an overlay using the on-surface color — useful for modals and tooltips.

## 5. Layout Principles

- **Spacing scale:** `--hds-ref-size-5` through `--hds-ref-size-80`, plus a `30-rem` variant for fluid spacing. Steps of 5px at small scale, growing non-linearly.
- **Grid:** Not tokenized explicitly, but the systematic spacing implies an 8px base grid with 5px as the micro-unit.
- **Density:** Medium. The wide font scale and explicit spacing tokens suggest layouts that breathe — generous section padding with tight in-component spacing.

## 6. Depth & Elevation

Depth is managed through the opacity stacks. No explicit box-shadow tokens were extracted. The `--hds-sys-color-theme-mask` pattern suggests elevation is communicated via translucent overlays rather than drop shadows — a flat-depth approach common in modern design systems.

## 7. Do's and Don'ts

**Do:**
- Use the rainbow gradient as the brand moment — sparingly, on a single focal element per view
- Lean on the opacity scale (dark-40a for borders, dark-10a for hovers) rather than inventing new grays
- Use semantic color tokens (`green-50`, `red-50`) for status indicators
- Keep typography within the `--hds-sys-font-size-*` aliases — don't freestyle sizes

**Don't:**
- Don't use the rainbow gradient as a background fill — it overwhelms when used broadly
- Don't introduce colors outside the dark/light/semantic set
- Don't break the opacity staircase with arbitrary alpha values
- Don't use body text above `18px` — the scale has a clear lead-body ceiling

## 8. Responsive Behavior

The `--hds-ref-size-30-rem` and `--hds-ref-font-size-12-rem` tokens signal rem-based fluid sizing for responsive contexts. The opacity-based approach to surfaces means dark/light mode switching is handled at the variable level without separate style sheets. The wide font scale (12–80px) implies mobile contexts use the smaller half of the scale and desktop uses the larger.

## 9. Agent Prompt Guide

**Quick reference:**
- Dark: `#111111` | Light: `#ffffff`
- Accent: `linear-gradient(120deg, #ff124f, #ff7a00, #ffe600, #19ffb6, #00c3ff, #8a2bff, #ff00f0, #ff124f)`
- Body: System UI, 16px
- Font scale: 12 / 16 / 18 / 20 / 24 / 36 / 46 / 60 / 80px

**Prompt starters:**
- *"Dark design system, `#111111` base, pure white inverse, single rainbow gradient accent, system-UI type, opacity-stepped color palette, 9-level font scale."*
- *"Mature HDS design system: achromatic palette with alpha steps, semantic status colors, one bold rainbow gradient as brand identifier."*

---

*Generated by Sparkbites — extracted from live CSS analysis*
