# markflow.app — Design System

## 1. Visual Theme & Atmosphere

Markflow is a developer-focused markdown tool that dresses itself in warm sand tones instead of the cold grays typical of the category. The design system is built on Radix UI's full color palette — all 30+ color families are available — but the active palette narrows to amber/orange for brand identity and sand/stone neutrals for surfaces. The result is a tool that feels warmer and more approachable than most developer utilities without sacrificing the clarity and information density the audience expects. Cal Sans headlines give the marketing layer a confident editorial presence, while Inter handles all functional UI. The absence of decorative patterns and the use of only subtle shadows reinforces the product's core promise: distraction-free writing.

## 2. Color Palette & Roles

**Brand (Amber/Orange)**

| Role | Value | Notes |
|---|---|---|
| Primary CTA | `--orange9` → `hsl(24, 94%, 50%)` ≈ `#f76808` | Buttons, primary actions |
| Primary hover | `rgba(247, 104, 8, 0.9)` | 10% opacity reduction on hover |
| Accent background | `--orange4` → amber tint | Subtle accent fills |
| Focus ring | `--orange7` | Focus states on inputs |
| Link hover | `rgb(247, 104, 8)` | Inline link hover color |

**Surfaces (Sand)**

| Role | Variable | Notes |
|---|---|---|
| Page background | `--background` → `--sand1` ≈ `hsl(50, 20%, 99%)` | Near-white warm |
| Muted background | `--muted` → `--sand2` | Cards, secondary fills |
| Card surface | `--card` → `--sand3` | Slightly warmer card bg |
| Border | `--border` → `--sand6` | Dividers, container edges |
| Input border | `--input` → `--sand7` | Form field outlines |

**Text**

| Role | Variable | Notes |
|---|---|---|
| Foreground | `--foreground` → `--sand12` ≈ `hsl(50, 6%, 10%)` | Primary text, near-black warm |
| Muted text | `--muted-foreground` → `--sand11` | Secondary labels, captions |
| Secondary text | `rgb(112, 111, 108)` | Tertiary navigation |

**Destructive:** `--destructive` → `--tomato9`

## 3. Typography Rules

| Selector | Font | Size | Weight | Tracking | Notes |
|---|---|---|---|---|---|
| `h1` | Cal Sans | 72px | 700 | -0.72px | `calt`/`rlig` features on |
| `h2` | Cal Sans | 48px | 700 | normal | Tight 1:1 line-height |
| `h3` | Cal Sans | 20px | 600 | -0.5px | Section headers |
| `body` | Inter | 16px | 400 | normal | 24px line-height |
| `p` | Inter | 14px | 600 | normal | Semi-bold paragraphs |
| `a` | Inter | 16px | 400 | normal | No transform |
| `button` | Inter | 14px | 500 | normal | Medium weight |

**Philosophy:** Cal Sans is used exclusively for headings — its optical calibration and tight `-0.72px` tracking at 72px creates authority. Inter handles everything functional. The `p` at 600 weight is unusual and suggests that paragraph-level text in this product context often carries label or feature-description weight. No serif fonts; no display mixing.

## 4. Component Stylings

**Primary button**
- Background: `rgb(247, 104, 8)` — amber-orange
- Text: white
- Hover: `rgba(247, 104, 8, 0.95)` — barely perceptible lightening
- Focus: double ring — `rgb(253, 253, 252) 0 0 0 2px` inner white, `rgb(255, 179, 129) 0 0 0 4px` outer peach

**Navigation links**
- Default: `rgb(27, 27, 24)` — warm near-black
- Hover: color shifts to `rgb(247, 104, 8)` — amber
- Focus: browser default `rgb(0, 95, 204) auto 1px`

**Border radii:** `4px`, `6px`, `8px`, `12px`, `9999px` — a graduated corner system from near-sharp to full pill.

**Shadows (elevation system):**
- Level 1: `rgba(0,0,0,0.05) 0 1px 2px` — barely visible lift
- Level 2: `rgba(0,0,0,0.05) 0 2px 4px inset` — inset for pressed states
- Level 3: `rgba(0,0,0,0.1) 0 10px 15px -3px, rgba(0,0,0,0.1) 0 4px 6px -4px` — card elevation
- Level 4: `rgba(0,0,0,0.1) 0 20px 25px -5px` — modal/popover elevation

## 5. Layout Principles

Built with Next.js and Tailwind CSS. Footer uses `0 32px` padding. Body and main reset to zero. Breakpoints: `600px`, `640px`, `768px`, `1024px`, `1280px`, `1400px`, `1536px` — a complete Tailwind-style responsive grid. The design respects standard container widths rather than custom breakpoints.

**Spacing scale:** Tailwind-compatible 4px grid (`--radius: 0.5rem`). Spacing tokens from 4px to macro layout values are inherited from the sand/radix token system.

## 6. Depth & Elevation

A four-level shadow system — all shadows are black at very low opacity (0.05–0.1), producing near-invisible but semantically meaningful elevation. The inset shadow (`level 2`) signals pressed/active states. Shadows follow the standard CSS layered approach: outer glow at larger blur, sharper shadow at smaller spread.

No colored shadows. No glow effects. Depth is structural, not decorative.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(247, 104, 8)` / `--orange9` for all primary CTAs — it's the singular brand color
- Apply the double-ring focus style: inner white, outer peach (`rgb(255, 179, 129)`)
- Use Cal Sans only for headings — never body copy
- Apply negative tracking (`-0.72px`) on 72px+ headlines
- Use sand tones for all neutral surfaces — avoid pure whites or cold grays

**Don't:**
- Use the full Radix palette decoratively — it's a system resource, not a visual language
- Add heavy shadows (>0.1 opacity) — the elevation system is intentionally subtle
- Mix amber with other saturated accent colors
- Use `p` element for running prose at 600 weight if content is truly body text — adjust selector specificity
- Apply rounded corners larger than `12px` on non-pill elements

## 8. Responsive Behavior

Breakpoints follow Tailwind defaults: `sm` (640px), `md` (768px), `lg` (1024px), `xl` (1280px), `2xl` (1536px), plus a `600px` custom mobile breakpoint. The pattern suggests:
- Mobile-first with standard Tailwind utility classes
- Single-column layout below 640px
- Two-column feature grids from 768px
- Max-width containers at 1280px/1400px

Footer horizontal padding (`32px`) remains constant — likely constrained by a container wrapper.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: Sand (`hsl(50, 20%, 99%)`)
- Primary: `#f76808` (amber-orange)
- Text: Warm near-black `hsl(50, 6%, 10%)`
- Fonts: Cal Sans (headings) + Inter (body/UI)
- Radius: 4–12px (components) / 9999px (pills)

**Prompt starters:**
- "Build a pricing card in Markflow style: sand-toned background (`--sand3`), Cal Sans heading at 20px, Inter body at 16px, amber-orange CTA button with double-ring focus state."
- "Design a navigation bar: warm `--sand1` background, Cal Sans logo, Inter nav links that shift to `#f76808` on hover."
- "Create a feature section with Tailwind: warm neutrals, amber accent, subtle `box-shadow` elevation at 0.05 opacity, 8–12px border radius."

*Generated by Sparkbites — extracted from live CSS analysis*
