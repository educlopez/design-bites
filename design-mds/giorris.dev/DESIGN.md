# Giorris.dev — Design Language Reference

## 1. Visual Theme & Atmosphere

Giorris.dev is a developer portfolio that wears its craft on its sleeve. The design philosophy is dark-first, system-informed, and deliberately expressive — almost the opposite of the minimal white-space portfolio. A near-black canvas (`#0C0C0C`) is punctuated by an electric mint accent (`#00FFBC`) that reads like a terminal cursor brought to life. The effect is confident and technical, but the choice of Fraunces serif for display text prevents it from feeling cold.

What makes giorris.dev unusual is the depth of its token system. This is not a site that sprinkles CSS variables for convenience — it has tokens for atomic design hierarchy levels, a complete semantic status palette, and a fluid type scale built with `clamp()`. The site exposes its design system thinking as a kind of authorial signature.

---

## 2. Color Palette & Roles

**Foundation**
- `--color-bg: #0C0C0C` — Near-black page background (not pure black, intentionally warm)
- `--color-dark: #161616` — Card surfaces, secondary backgrounds, raised elements
- `--color-light: #F3F3F3` — Primary text on dark backgrounds
- `--color-white: #FFFFFF` — Emphasis text, highlights

**Accent**
- `--color-accent: #00FFBC` — The brand's single defining color: electric mint/cyan-green. Used for interactive highlights, active states, and focal points.

**Borders**
- `--color-border: #B2B2B2` — Visible borders, standard dividers
- `--color-border-muted: #585858` — Subtle separators, de-emphasized structure

**Semantic States**
- `--color-success: #10B981` — Emerald green
- `--color-info: #3B82F6` — Solid blue
- `--color-warning: #F59E0B` — Amber
- `--color-error: #EF4444` — Red

**Atomic Design Vocabulary Colors** (unique to this site)
- Atom: `#10B981` | Molecule: `#3B82F6` | Organism: `#F59E0B` | Template: `#8B5CF6` | Page: `#EF4444` | Effect: `#06B6D4`
- These colors annotate the site's own component architecture — the design system documents itself visually

**Overlay Surfaces**
- `rgba(21,21,21,0.6)` — Strong overlay (modal backdrops, drawers)
- `rgba(21,21,21,0.4)` — Medium overlay (hover states, layered panels)

**What's absent:** No warm tones. No photography tinting. The palette is cool, technical, and systematic — emotion comes from contrast, not hue.

---

## 3. Typography Rules

A two-family system with a clear hierarchy:

- **`Lexend Deca`** — `--font-family-base`: The workhorse. A reading-optimized sans-serif designed to reduce visual stress. Used for all body copy, labels, and UI text.
- **`Fraunces`** — `--font-family-serif`: The personality font. A variable optical-size serif used for display headings. Its ink-trap details at large sizes add warmth to the dark canvas.

**Fluid Type Scale** (via `clamp()`)

| Step | Min | Max | Typical Use |
|------|-----|-----|-------------|
| step-0 | 1.13rem | 1.5rem | Body / base |
| step-1 | 1.35rem | 1.88rem | Small headings |
| step-2 | 1.62rem | 2.34rem | Sub-sections |
| step-3 | 1.94rem | 2.93rem | Section heads |
| step-4 | 2.33rem | 3.66rem | Large display |
| step-5 | 2.80rem | 4.58rem | Hero sub |
| step-6 | 3.36rem | 5.72rem | Hero display |

**Article-specific scale** (capped for reading width)
- H1: clamp(2.25rem → 2.5rem), H2: clamp(1.5rem → 1.6rem), Body: 1.125rem

The spacing scale mirrors the type scale via `--spacing-step-*` tokens — vertical rhythm is mathematically tied to type size.

**Transition:** `--transition-default: .3s ease` applied consistently across interactive elements.

---

## 4. Component Styling

**Cards / Panels**
- Background: `--color-dark` (`#161616`) lifted from the `#0C0C0C` base
- Border: `--color-border-muted` (`#585858`) for subtle edge definition
- No rounded corners detected — the design favors sharp edges, consistent with its technical register

**Atomic Labels**
- Each atomic design level gets its own color token — components are visually tagged by their place in the hierarchy
- This is genuinely unusual: the design system annotates itself, turning the component library into living documentation

**Interactive States**
- Accent color (`#00FFBC`) applied on hover/focus to links, buttons, and interactive elements
- Overlay surfaces use the semi-transparent dark system for depth without lightness

---

## 5. Layout Principles

Container max-width: `--breakpoint-container: 1200px` with `--container-width: 90%` — consistent inner margins regardless of viewport.

The spacing system is token-driven with 20 explicit steps from `0.0625rem` to `16rem`. This granularity suggests thoughtful vertical rhythm decisions rather than ad-hoc spacing. Steps are named numerically (`--space-4`, `--space-8`, etc.) mapping to a 4px base unit.

Spacing steps (`--spacing-step-*`) alias the fluid type sizes, meaning section padding grows proportionally with the type scale — the page breathes more on large screens, contracts gracefully on small ones.

---

## 6. Depth & Elevation

No box-shadows detected in the data. Depth is achieved through background lightness contrast:
- Base canvas: `#0C0C0C`
- Raised surface: `#161616` (+14 luminance points)
- Overlay: `rgba(21,21,21,0.6)` semi-transparent layer

This approach is characteristic of dark-mode-first design: elevation is expressed through lightness steps, not shadows. Adding a shadow to a dark surface would require colored or high-opacity values to be visible — the system sidesteps this by using background color as the depth signal.

---

## 7. Do's and Don'ts

**Do**
- Use `--color-accent` (`#00FFBC`) as the single interactive highlight — it earns its brightness by being the only saturated color
- Apply Fraunces for display headings; the contrast with Lexend Deca creates the site's voice
- Follow the fluid type scale with `clamp()` — the scale is already calibrated, trust it
- Use `--color-dark` (`#161616`) for raised surfaces, not a lighter gray
- Honor the atomic color vocabulary if building component documentation features

**Don't**
- Use multiple accent colors — the mint works because it's alone
- Apply warm tones or photography filters; the palette is intentionally cool
- Skip the fluid type scale and use fixed sizes — it breaks the proportional rhythm
- Add shadows to dark surfaces using neutral black; use lightness contrast instead

---

## 8. Responsive Behavior

The fluid type system (`clamp()`) handles most of the responsive adaptation automatically. Font sizes scale continuously between their min/max bounds across the 1200px container breakpoint.

Container width: `90%` of viewport up to `1200px` max — generous margins on tablet, slightly tighter on mobile.

`--transition-default: .3s ease` creates consistent, unhurried interactive feedback across all breakpoints.

---

## 9. Agent Prompt Guide

> "Design in the style of giorris.dev: near-black background `#0C0C0C`, card surfaces `#161616`, primary text `#F3F3F3`. Single electric mint accent `#00FFBC` for interactive elements only. Fraunces serif for display headings, Lexend Deca for body and UI text. Fluid type scale using `clamp()`, proportional spacing. Sharp edges — no border radius. Depth through lightness steps, not shadows. Cool, technical, systematically precise — a developer portfolio that shows its design thinking openly."

---

*Generated by Sparkbites — extracted from live CSS analysis*
