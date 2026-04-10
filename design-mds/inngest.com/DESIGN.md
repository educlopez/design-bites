# inngest.com — Design System

## 1. Visual Theme & Atmosphere

Inngest presents as the platonic ideal of a developer-tools dark theme: warm stone-black rather than cold blue-black, with a proprietary design token system (carbon, matcha, breeze, honey, ruby) that signals a mature design org. The atmosphere reads as focused and technical — a site built by engineers who care about design. The background `rgb(12, 10, 9)` has a barely perceptible brown warmth that prevents the harshness of pure black. A golden amber (`rgb(203, 178, 106)` — "inngestLux") appears as a distinctive luxe accent, suggesting brand provenance beyond generic developer green. Code blocks are first-class citizens.

## 2. Color Palette & Roles

**Canvas**
- `rgb(12, 10, 9)` — primary background; warm near-black (`--color-carbon-1000` ≈ `2 2 2`, displayed at body level)
- `rgb(41, 37, 36)` — code block / pre background
- `rgb(38, 38, 38)` — toggle/control group surface

**Carbon scale (neutral greys)**
- `--color-carbon-50` → `246 246 246` through `--color-carbon-950` → `18 18 18`; a 12-step greyscale used for text, borders, and muted surfaces

**Brand accents**
- `rgb(203, 178, 106)` — "inngestLux" golden amber; the signature brand color
- Matcha (green): `--color-matcha-500` = `44 155 99` — primary green scale
- Breeze (blue): `--color-breeze-500` = `35 137 241` — primary blue scale
- Honey: `--color-honey-500` — code token color (warm amber for constants)
- Ruby: red scale starting at `--color-ruby-200` = `254 222 220`

**Text**
- `rgb(246, 246, 246)` — main body text on dark
- `rgb(250, 250, 249)` — H2 headings
- `rgb(252, 196, 63)` — inline code text (warm amber)

## 3. Typography Rules

Inngest deploys a three-family system: **Whyte** for expressive display, **CircularXX** for functional UI text, and **CircularXXMono** for code. Whyte Inktrap appears in blockquotes — a deliberate editorial touch that elevates developer prose.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H1 | Whyte | 72px | 400 | lh 72px — 1:1 ratio, tight |
| H3 | Whyte | 30px | 300 | lh 36px |
| Blockquote | Whyte Inktrap | 18px | 400 | Ink-trap variant for small sizes |
| Body | CircularXX | 16px | 400 | lh 24px |
| P (lead) | CircularXX | 24px | 300 | Large lead paragraphs |
| Links | CircularXX | 14px | 500 | Medium weight for nav |
| Buttons | CircularXX | 14px | 600 | Semi-bold |
| Code | CircularXXMono | 18px | 400 | lh 28px |
| Pre | CircularXXMono | 14px | 400 | lh 20px |

Weight 300 is used extensively — lighter than typical developer sites, giving Inngest an editorial, magazine-like lightness despite the technical content.

## 4. Component Stylings

**Buttons** — Pill shape (`border-radius: 9999px`) for primary CTAs. Standard `6px` radius for secondary/code-adjacent elements. Colors sourced from the token system.

**Code blocks** — `rgb(41, 37, 36)` background, CircularXXMono, amber text (`rgb(252, 196, 63)`). Shiki syntax highlighting with named token variables: honey for constants, blue for strings, teal for keywords.

**Toggle groups** — `rgb(38, 38, 38)` background with `6px` radius; used for tab/mode switching in code demos.

**Shadows** — Minimal and functional: `0px 1px 2px rgba(0,0,0,0.05)` through `0px 20px 25px rgba(0,0,0,0.1)`. No colored glows — shadow system is Tailwind's standard scale applied conservatively.

## 5. Layout Principles

Rich breakpoint system: 15 breakpoints from `520px` to `1536px`. This is a content-heavy marketing site that adapts granularly across viewport widths. The many breakpoints suggest complex multi-column grid layouts that step down progressively. Container system likely uses max-width constraints at key widths (1272px, 1280px, 1350px, 1536px for the widest editorial moments).

Custom column-margin CSS variables (`--column-margin--5`, `--column-margin--6`) indicate a named column grid system, not just utility padding.

## 6. Depth & Elevation

Warm luminance stacking:
- `luminance 0.328` — mid-tone stone surface `rgb(87, 83, 78)`
- `luminance 0.149` — toggle control `rgb(38, 38, 38)`
- `luminance 0.101` — overlay `rgba(28, 25, 23, 0.3)`
- `luminance 0.041` — stone-950 near-black

Tailwind shadow scale applied conservatively — `shadow-sm` through `shadow-xl` equivalents are present but not stacked decoratively. The warm undertone of all surfaces means dark elements never feel cold or blue-shifted.

## 7. Do's and Don'ts

**Do**
- Use Whyte at weight 400 or 300 for display text — the lightness is intentional
- Apply the matcha/breeze/carbon token scales for all color decisions; avoid ad-hoc hex values
- Prioritize `CircularXXMono` in code blocks with amber `rgb(252, 196, 63)` for token text
- Use pill buttons (`9999px`) for primary actions, `6px` for secondary/utility buttons

**Don't**
- Use cold blue-black backgrounds — the warm brown undertone of `rgb(12, 10, 9)` is critical
- Mix font weights aggressively; the system leans light (300–400) except for buttons (600)
- Add decorative colored glows or neon accents — the gold "inngestLux" is sufficient signature
- Ignore the mono font for any technical output, even inline snippets

## 8. Responsive Behavior

15 breakpoints from 520px to 1536px indicate a fully fluid layout system. The wide editorial content (1272px+) contracts into progressively simpler grid arrangements. At mobile widths below 640px, multi-column code demo layouts likely stack vertically. The three-family type system should scale proportionally — Whyte headlines likely use `clamp()` at mobile sizes.

## 9. Agent Prompt Guide

> Build a developer-tools dark marketing page in the style of inngest.com. Background: warm near-black `rgb(12, 10, 9)`. Use Whyte (400/300 weight) for headlines at 72px with 1:1 line-height. Body in CircularXX 16px/400. Code blocks use CircularXXMono on `rgb(41, 37, 36)` with amber code text `rgb(252, 196, 63)`. Accent palette: golden amber `rgb(203, 178, 106)` as signature, matcha green for success states, breeze blue for interactive. Primary buttons are full pills (`border-radius: 9999px`). Surface stack reads warm — no cold greys. Tailwind shadow scale, conservatively applied. Rich breakpoint grid (15 stops, 520px–1536px).

---

*Generated by Sparkbites — extracted from live CSS analysis*
