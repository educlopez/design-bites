# lynnandtonic.com — Design System

## 1. Visual Theme & Atmosphere

Lynn Fisher's personal site is a study in deliberate contrast and craft. The palette is built on warm antique tones — a creamy beige that evokes letterpress paper — punctuated by a single, unapologetic red. The typography leans fully into custom display serifs: Hubano-Rough for massive headlines, SydoniaAtramentiqua for body and links, creating a hand-lettered, editorial warmth that feels personal rather than polished. Shadows are absent entirely; depth comes from the `light-dark()` CSS function toggling between light and dark modes, where dark mode inverts the emotional register — dark background, red text, a more confrontational mood. The overall effect is a designer's portfolio that wears its craft visibly. Nothing is generic; every element is deliberate.

## 2. Color Palette & Roles

| Role | Variable | Value | Notes |
|---|---|---|---|
| Background | `--bg-color` | `light-dark(#e4e2d7, #111)` | Warm parchment / near-black |
| Surface (code blocks) | `--pre-bg` | `light-dark(white, black)` | Pure white / pure black |
| Text | `--text-color` | `light-dark(black, #ff3b3b)` | Black on light; vivid red on dark |
| Accent / Brand | `--red` | `#ff3b3b` | Buttons, focus rings, dark-mode text |
| Supporting warm | `--beige` | `#e4e2d7` | Background in light mode |
| Muted / Borders | `--light-color` | `light-dark(rgba(0,0,0,0.3), rgba(255,59,59,0.3))` | Soft separator tones |
| Focus accent | `--focus-color` | `light-dark(#ff3b3b, white)` | Keyboard focus outlines |

**Absent:** Blues, greens, purples, neutrals. This palette is aggressively minimal — two base tones plus one accent.

## 3. Typography Rules

| Selector | Font | Size | Weight | Notes |
|---|---|---|---|---|
| `h1` | Hubano-Rough | 96px | 300 | Display only; 1:1 line-height |
| `h2` | SydoniaAtramentiquaBold | 24px | 300 | Serif subheadings |
| `body` | SydoniaAtramentiquaRegular | 19.2px (≈1.2rem) | 300 | 1.6× line-height, comfortable reading |
| `a` | SydoniaAtramentiquaLight | 16px | 550 | Uppercase navigation links |
| `button` | SydoniaAtramentiquaRegular | ~14px | 600 | Control labels |

**Scale tokens:** `--font-xs` (.85rem) → `--font-sm` (1rem) → `--font-base` (1.2rem) → `--font-md` (1.5rem) → `--font-lg` (2.3rem) → `--font-xl` (3rem) → `--font-xxl` (6rem).

**Key rules:** Weight 300 dominates — this is a light, elegant serif experience. The `h1` at 96px with weight 300 creates a paradox of scale and delicacy. Navigation links use uppercase as the only transformation applied. No tracking (letter-spacing) adjustments.

## 4. Component Stylings

**Navigation links**
- Default: transparent bg, black text, no shadow
- Hover: `scale(1.05)` transform — subtle kinetic feedback
- Focus: beige fill + black 6px offset box-shadow + red 4px solid outline

**Buttons (mode toggle)**
- Transparent background, beige border and text (dark mode context)
- Focus: 6px/4px offset black box-shadow + red outline — very tactile, keyboard-first

**Border radii:** Only `4px` detected — corners are nearly sharp, not rounded.

**Code blocks:** White (`--pre-bg`) on light, black on dark — isolated reading surfaces.

## 5. Layout Principles

The site uses a fluid, custom-coded layout with no CSS framework. Spacing is intentionally sparse at the structural level (body/header/main all have zero padding/margin in their base state). Breakpoints are tight and mobile-first: 350px, 499px, 500px, 690px — indicating a heavily hand-tuned responsive design rather than a grid system.

**Philosophy:** Content breathes at its own rhythm. No columns, no cards, no grid frameworks. The layout feels like a single long-form editorial page.

## 6. Depth & Elevation

No box shadows are used anywhere. Depth is achieved entirely through:
- **Color mode contrast** — the `light-dark()` function provides a dramatic mode switch
- **Typography scale** — the 6rem `--font-xxl` versus .85rem `--font-xs` creates visual hierarchy through size alone
- **Focus states** — the offset double-shadow on interactive elements creates the only true "lift" effect in the system

## 7. Do's and Don'ts

**Do:**
- Use `--red` (#ff3b3b) as the sole accent — it appears on hover, focus, and dark-mode text
- Use the `light-dark()` CSS function for all theme-adaptive values
- Keep borders dotted or solid using `--border-dotted` / `--border-solid` tokens
- Apply `scale(1.05)` on interactive hover — it's the site's signature micro-interaction
- Use uppercase for navigation-level links only

**Don't:**
- Add box shadows or elevation layers — this site is intentionally flat
- Introduce additional accent colors or neutrals
- Use rounded corners beyond 4px
- Mix sans-serif fonts — the entire voice is in SydoniaAtramentiqua
- Use heavy font weights; 300–600 is the full range

## 8. Responsive Behavior

Breakpoints: `350px`, `499px`, `500px`, `690px` — all below typical desktop thresholds. This suggests:
- Primary design is **mobile-first and content-driven**
- The extra-large headline (96px h1) likely collapses to use `--font-xl` (3rem) or `--font-lg` (2.3rem) on smaller screens
- Navigation probably stacks or simplifies below 500px
- No tablet/desktop grid breakpoints detected — layout scales continuously rather than snapping

Touch targets: The scale hover interaction works well on desktop; on touch the transform is skipped (no hover state on mobile).

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#e4e2d7` (light) / `#111` (dark)
- Accent: `#ff3b3b`
- Text: `black` (light) / `#ff3b3b` (dark)
- Font: Hubano-Rough (display) + SydoniaAtramentiqua family (all else)

**Prompt starters:**
- "Design a project card in the lynnandtonic.com style: warm beige background, SydoniaAtramentiqua serif, red accent on hover, sharp 4px corners, no shadows."
- "Build a dark-mode nav toggle using only color inversion — beige to near-black, black text to red."
- "Create a typographic hero section: Hubano-Rough headline at 96px weight 300, SydoniaAtramentiqua body, a single red CTA link in uppercase."

*Generated by Sparkbites — extracted from live CSS analysis*
