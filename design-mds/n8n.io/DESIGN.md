# n8n.io — Design System

## 1. Visual Theme & Atmosphere

n8n.io is **dark-mode automation software** wearing a distinctly expressive visual identity. The deep purple-black background (`rgb(14, 9, 24)`) creates a night-sky depth against which hot pink (#ea4b71) and orange-red (#ff492c) glow with neon urgency. Geomanist — used exclusively at weight 400 across all type levels — is a distinctive typeface choice: it has personality without being difficult. The layered shadow system, including inset glows and translucent white borders, suggests a design team that understands how to create depth in a dark environment without relying on flat color blocking alone.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Background | `rgb(14, 9, 24)` → `#0e0918` | Deep purple-black page canvas |
| Card Surface | `rgb(27, 23, 40)` → `#1b1728` | Elevated card backgrounds |
| Primary Text | `rgb(209, 206, 206)` | Main readable content |
| Secondary Text | `rgb(182, 181, 185)` | Muted headings, secondary labels |
| Muted Text | `rgb(153, 153, 153)` | Dialog / tertiary content |
| Hot Pink | `rgb(234, 75, 113)` → `#ea4b71` | Progress indicator, primary accent |
| Orange-Red | `rgb(255, 73, 44)` → `#ff492c` | Secondary hot accent, gradient tiles |
| Border | `rgba(255, 255, 255, 0.1)` | Translucent white card borders |
| Blue Accent | `rgb(7, 122, 199)` | Focus rings, active states (shadow layer) |

A dark palette with two hot accents. The translucent borders are as important as the solid colors for the layered-depth effect.

## 3. Typography Rules

- **Font family**: Geomanist — used for every text role; weight 400 throughout
- **Negative letter-spacing**: H2 at 48px uses -0.96px tracking; H3 at 24px uses -0.48px — optical correction for large display
- **H2**: 48px / 48px — 1:1 line height ratio creates a dense, powerful display scale
- **H3**: 24px / 28.8px — section headers with 1.2x line height
- **Body**: 16px / 24px — comfortable legibility at base reading size
- **P / small**: 15px / 18.75px — slightly compact supporting copy
- **No weight variation** — Geomanist 400 handles all roles; size alone creates hierarchy

| Level | Size | Weight | Line Height | Letter Spacing |
|-------|------|--------|-------------|----------------|
| H2 | 48px | 400 | 48px | -0.96px |
| H3 | 24px | 400 | 28.8px | -0.48px |
| Body | 16px | 400 | 24px | normal |
| P | 15px | 400 | 18.75px | normal |

## 4. Component Stylings

- **Cards**: `rgb(27,23,40)` background, `rgba(255,255,255,0.1)` border — dark glass panels
- **Badge / feature**: `rgba(31,25,42,0.5)` — semi-transparent badge surfaces
- **Gradient tiles**: `rgba(13,10,25,0.28)` overlay with translucent white border
- **Buttons**: `rgba(255,142,93,0.3)` inset glow on CTAs — warm orange halo effect
- **Progress / loading**: Hot pink (#ea4b71) Nuxt loading bar
- **Focus ring**: Blue accent via shadow layer `rgb(7,122,199)`

## 5. Layout Principles

- **Stack**: Nuxt + Tailwind CSS
- **Breakpoints**: Not explicitly extracted — Tailwind defaults
- **Carousel**: vc-* tokens for carousel pagination (4px height bars, 6px margin)
- **Spacing**: Tailwind 4px base unit with section padding at ~81px top / 40px bottom
- **Content layout**: Likely centered max-width container with full-bleed dark background

## 6. Depth & Elevation

Rich layered shadow system:
- **Subtle glow**: `rgba(0,0,0,0.26) 0px 0px 8px 0px` — dark ambient card shadow
- **Button ring**: `rgba(255,255,255,0.2) inset + rgba(8,8,8,0.2) outer` — layered button depth
- **Inset glow**: `rgba(255,255,255,0.12) 0px 6px 12px inset` — inner light reflection
- **Outline**: `rgba(0,0,0,0.44) 0px 0px 0px 1px` — subtle border replacement via shadow
- **Dark panel**: `rgba(0,0,0,0.23) 0px 4px 16px -8px` — diffused underside shadow
- **Surface inset**: `rgba(255,255,255,0.05) 0px 4px 12px inset` — ghost inner glow

## 7. Do's and Don'ts

**Do:**
- Use the full layered shadow system — single shadows look flat in the dark theme
- Apply translucent white borders (`rgba(255,255,255,0.1)`) on all cards
- Use negative letter-spacing on large display headings
- Keep Geomanist at weight 400 — size drives hierarchy, not weight

**Don't:**
- Switch to a light background — the entire shadow and glow system is calibrated for dark
- Use flat solid borders instead of translucent white
- Introduce more than two hot accent colors — pink and orange-red is already a bold pairing

## 8. Responsive Behavior

- Tailwind responsive breakpoints
- Dark background is persistent across all viewport sizes
- Carousel pagination (vc-pgn) uses 4px thin bars — adapts to mobile touch
- Glow effects and translucent borders scale naturally with CSS

## 9. Agent Prompt Guide

> "Design in the style of n8n.io: deep purple-black background (`#0e0918`), hot pink `#ea4b71` and orange-red `#ff492c` accents, Geomanist weight 400 typeface at all levels, negative letter-spacing on display text, layered shadow system with inset glows, translucent white card borders, Nuxt + Tailwind stack."

**Quick reference:**
- Background: `#0e0918`
- Card: `#1b1728`
- Text: `rgb(209, 206, 206)`
- Hot pink: `#ea4b71`
- Orange-red: `#ff492c`
- Font: Geomanist, 400
- Card border: `rgba(255, 255, 255, 0.1)`

*Generated by Sparkbites — extracted from live CSS analysis*
