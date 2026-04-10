# DESIGN.md — coderabbit.ai

## 1. Visual Theme & Atmosphere

CodeRabbit's site is dark-mode developer tooling at its most considered — deep purple-black canvas, an electric teal-green accent, and a thoroughly engineered design token system. The atmosphere is "AI infrastructure built by people who care about craft." The custom `--cr-*` token system signals a mature, systematic approach to design: spacing, font sizes, line heights, and letter-spacing all run through a base unit (`0.125rem`). This is not a theme — it is a design language.

## 2. Color Palette & Roles

The site uses a two-tier color system: brand-named tokens for primary palette, semantic tokens for UI chrome.

| Role | Token | Value |
|------|-------|-------|
| Canvas / deepest background | `--CR-Gray-900` | `#141116` — very dark purple-black |
| Dark surface | `--CR-Gray-700` | `#3a3441` — muted purple-gray |
| Primary accent | `--CR-Green-450` | `#19d59e` — electric teal-green |
| Testimonial hover | `--CR-Testimonial-Hover-Bg` | `#111613` — near-black with green cast |
| Body background | `rgb(9, 8, 12)` | Near-black, slightly purple |
| Body text | `rgb(255, 255, 255)` | Pure white on dark |

**shadcn-layer tokens** (for UI components):
- `--background: 0 0% 98%` — near-white (light mode fallback)
- `--radius: .5rem` — 8px global radius
- `--swiper-theme-color: #007aff` — carousel controls only, not a brand color

The electric green (`#19d59e`) is the brand's defining color — used for CTAs, highlights, and brand moments against the dark canvas.

## 3. Typography Rules

**Typeface**: `scandia` — a licensed humanist sans-serif, falling back to its own placeholder then system sans-serif.

The `--cr-*` token system encodes a full type scale:

| Token | Value | Use |
|-------|-------|-----|
| `--cr-font-size-5` | `2rem` (32px) | Large display |
| `--cr-font-size-4` | `1.75rem` (28px) | Section headings |
| `--cr-font-size-3` | `1.5rem` (24px) | Sub-sections |
| `--cr-font-size-2` | `1.25rem` (20px) | Featured body |
| `--cr-font-size-1` | `1rem` (16px) | Base |
| `--cr-font-size-neg-1` | `.875rem` (14px) | Small labels |
| `--cr-font-size-neg-2` | `.75rem` (12px) | Micro labels |

| Selector | Size | Weight | Notes |
|----------|------|--------|-------|
| h1 | 64px | 500 | Hero display — above the token scale |
| h2 | 32px | 500 | Matches `--cr-font-size-5` |

- Letter-spacing tokens: `--cr-letter-spacing-3: -0.075rem` through `--cr-letter-spacing-0: 0` — negative tracking for large sizes.
- H1 at 64px/500 with `-3%` letter-spacing creates a confident but measured headline.
- H2 at 32px/500 with `-2%` tracking maintains the tightened feel through the page.
- **What's absent**: no ultra-bold weights, no text transforms, no expressive caps.

## 4. Component Stylings

- **Spacing base unit**: `--cr-spacing: 0.125rem` (2px) — all spacing is a named multiple of 2px, from `--cr-spacing-2` (2px) to `--cr-spacing-128` (256px).
- **Primary CTA**: multi-layer shadow system creating a glowing ember effect — see Section 6.
- **Secondary button**: inset shadow with `rgba(255,255,255,0.25)` — subtle glass button.
- **Border-radius**: 8px (`.5rem`) globally — approachable, not sharp.
- **Swiper carousel**: Apple blue (`#007aff`) for controls — isolated use case only.

## 5. Layout Principles

- Spacing system built on 2px base unit with named steps — ensures consistent vertical rhythm.
- Dark canvas with `#141116` and `#3a3441` surfaces creates an implicit layering system without shadows.
- The font scale and spacing scale are both systematic — no ad-hoc values anywhere in the design.
- No detected CSS animations — likely handled by a JS animation library (Framer Motion / GSAP).

## 6. Depth & Elevation

CodeRabbit uses the most sophisticated shadow system in this collection — the primary CTA glows from within:

**Primary CTA shadow (multi-layer glow)**:
- 8 layers of `rgba(153,0,0,*)` ambient shadows at increasing blur radii — deep red atmospheric halo
- `rgba(255,89,0,0.49) 0px -22px 34px 16px inset` — inner orange core glow
- `rgb(255,153,89) 0px -2px 0px 0px inset` — warm amber rim on the bottom edge
- `rgb(255,255,255) 0px 2px 0px 0px inset` — white specular highlight on top edge

**Secondary button**: glass inset shadow with dark inner shadow for pressed-state feel.

This is photorealistic button crafting — it communicates "this CTA glows from within."

## 7. Do's and Don'ts

**Do:**
- Use `scandia` at weight 500 — medium weight is the design's tonal signature.
- Apply negative letter-spacing from `--cr-letter-spacing-*` tokens at all display sizes.
- Use the glowing CTA shadow system for primary actions — it is the brand's most distinctive element.
- Build all spacing from `--cr-spacing` multiples (2px base).

**Don't:**
- Use the electric green (`#19d59e`) as a text color on dark backgrounds — it is a background/highlight color.
- Add flat/matte primary buttons — the glow shadow is the design contract for CTAs.
- Use the Apple blue (`#007aff`) beyond swiper controls — it is not a brand color.
- Deviate from 8px border-radius — the token `--radius: .5rem` is global.

## 8. Responsive Behavior

- 64px h1 needs scaling to ~36–44px on mobile while maintaining negative tracking.
- The 2px base spacing system creates very granular layout control — adapt step counts, not the base unit.
- The CTA glow shadow degrades gracefully — each layer is independent and contributes individually.
- Dark canvas (`rgb(9,8,12)`) is the only background that holds the green accent's contrast ratio.

## 9. Agent Prompt Guide

> Build a developer AI product page in the style of CodeRabbit: near-black purple canvas (`rgb(9,8,12)`), electric teal-green accent (`#19d59e`), dark surface layers (`#141116`, `#3a3441`), scandia or geometric humanist sans at weight 500 with negative letter-spacing, 8px border-radius, 2px-base spacing system, glowing multi-layer CTA button shadow (8-layer red ambient + inner orange glow + amber rim + white specular). Full design token system — no ad-hoc values.

*Generated by Sparkbites — extracted from live CSS analysis*
