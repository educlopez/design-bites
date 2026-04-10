# matte.app — Design System

## 1. Visual Theme & Atmosphere

Matte is a productivity app that treats its visual design as a product feature in itself. Where most tools default to cold UI grays, Matte builds on a warm near-white base and deploys a single vivid coral-orange accent (`#ff6b35`) that signals energy without aggression. The typography is a deliberate hybrid: Space Grotesk for display headings (with a bold, slightly quirky geometric personality), Inter for body copy, and JetBrains Mono for code-adjacent labels in uppercase — a trio that communicates technical competence and creative confidence. Every shadow in the system is pre-named and semantically scaled from `xs` to `xl` plus a special orange glow. The easing functions are craft-level choices: `cubic-bezier(0.34, 1.56, 0.64, 1)` is a spring bounce. This is a product that cares.

## 2. Color Palette & Roles

**Backgrounds (warm neutrals)**

| Role | Variable | Value | Notes |
|---|---|---|---|
| Page base | `--bg-base` | `#f9f9f9` | Warm off-white |
| Card surface | `--bg-surface` | `#ffffff` | Pure white elevation |
| Elevated UI | `--bg-elevated` | `#fcfcfc` | Between base and surface |
| Muted fill | `--bg-muted` | `#f3f3f3` | Disabled, hover backgrounds |

**Text**

| Role | Variable | Value | Notes |
|---|---|---|---|
| Primary | `--text-primary` | `#1a1a1a` | Near-black, not pure |
| Secondary | `--text-secondary` | `#666666` | Captions, metadata |
| Muted | `--text-muted` | `#888888` | Placeholders, tertiary |

**Accent (coral-orange)**

| Role | Variable | Value | Notes |
|---|---|---|---|
| Brand accent | `--accent` | `#ff6b35` | CTAs, active states |
| Light accent | `--accent-light` | `#ff8a5c` | Hover variant |
| Dark accent | `--accent-dark` | `#e55a28` | Pressed/active variant |
| Muted accent | `--accent-muted` | `rgba(255,107,53,0.12)` | Subtle fill on accent elements |
| Accent glow | `--accent-glow` | `rgba(255,107,53,0.2)` | Used in `--shadow-glow` |

**Borders**

| Role | Variable | Value |
|---|---|---|
| Default | `--border` | `#e5e5e5` |
| Subtle | `--border-subtle` | `#f0f0f0` |
| Accent border | `--border-accent` | `rgba(255,107,53,0.3)` |

## 3. Typography Rules

| Selector | Font | Size | Weight | Tracking | Notes |
|---|---|---|---|---|---|
| `h1` | Space Grotesk | 64px | 700 | -2.56px | Tight, bold display |
| `h2` | Space Grotesk | 40px | 700 | -1.2px | Section titles |
| `h3` | Space Grotesk | 20px | 600 | -0.4px | Subheadings |
| `h4` | JetBrains Mono | 10px | 500 | +1.5px | UPPERCASE labels only |
| `body` | Inter | 16px | 400 | normal | 25.6px line-height |
| `p` | Inter | 18px | 400 | normal | 30.6px (1.7×) — generous |
| `a` | Inter | 16px | 400 | normal | Inherits body |

**Key rules:** Space Grotesk at 64px with -2.56px tracking (4% of size) — very tight for high-impact display. JetBrains Mono at h4 with positive tracking and uppercase is used for category labels, metadata chips, or feature tags — a mono typeface used decoratively. Paragraph line-height of 30.6px (1.7×) indicates long-form reading comfort is a design priority.

## 4. Component Stylings

**Buttons**
- The system defines `--ease-spring` (`cubic-bezier(0.34, 1.56, 0.64, 1)`) — a slight overshoot bounce for interactions
- Transitions: `--duration-fast` (150ms), `--duration-normal` (250ms), `--duration-slow` (400ms)

**Links**
- Default: secondary text color `#666666`
- Hover: shifts to primary `#1a1a1a`
- Focus: browser standard `rgb(0, 95, 204) auto 1px`
- Logo hover: `scale(1.02)` — subtle kinetic identity

**Border radii:** `8px`, `12px`, `16px`, `24px`, `9999px`, `50%` — a graduated system from modest rounding to full pill to circle.

**Accent glow effect:** `--shadow-glow`: `0 0 40px rgba(255,107,53,0.15)` — applied to featured elements.

## 5. Layout Principles

Sections use `padding: 96px 0px 48px` with `margin: 0px 136px` — large horizontal margins indicate a contained reading width on desktop. Footer: `64px 32px 32px`. The spacing token system is 4-based: `--space-1` (0.25rem) through `--space-24` (6rem).

**Breakpoints:** `768px`, `769px`, `1024px` — minimal, three-state responsive design. The `768px`/`769px` pair suggests a hairline distinction between portrait tablet and landscape/desktop modes.

The `136px` horizontal margin on sections creates a generous editorial column — not a full-bleed layout. Content is centered and constrained for reading focus.

## 6. Depth & Elevation

A fully named, six-level shadow system:

| Token | Value | Use |
|---|---|---|
| `--shadow-xs` | `0 1px 2px rgba(0,0,0,0.04)` | Baseline lift |
| `--shadow-sm` | `0 2px 4px + 0 1px 2px` at 0.04/0.06 | Cards at rest |
| `--shadow-md` | `0 4px 8px + 0 2px 4px` at 0.04/0.06 | Interactive cards |
| `--shadow-lg` | `0 12px 24px + 0 4px 8px` at 0.08/0.04 | Panels, dropdowns |
| `--shadow-xl` | `0 24px 48px + 0 8px 16px` at 0.12/0.06 | Modals, floating UI |
| `--shadow-glow` | `0 0 40px rgba(255,107,53,0.15)` | Accent-highlighted surfaces |

Shadow opacity is extremely low (0.04–0.12) — the system creates depth through blur and spread rather than opacity, keeping surfaces clean.

## 7. Do's and Don'ts

**Do:**
- Use `--accent` (`#ff6b35`) for all primary CTAs and active states — it's the one saturated color
- Apply `--ease-spring` for interactive transforms — the bounce is the brand
- Use JetBrains Mono in uppercase for category/feature labels only
- Apply negative tracking at scale: -2.56px at 64px, -1.2px at 40px
- Use `--shadow-glow` to highlight featured sections with the accent color

**Don't:**
- Use pure black (`#000`) for text — `--text-primary` (#1a1a1a) is intentionally warm
- Skip the spacing token system — the 4px grid is explicit
- Overuse the accent on non-interactive elements
- Use Space Grotesk for body text — it's a display and heading font here
- Apply heavy shadows (>0.12 opacity) — the design reads light and airy

## 8. Responsive Behavior

Three breakpoints: below 768px (mobile), 769–1023px (tablet), 1024px+ (desktop). The `136px` section margins almost certainly collapse to `32px` or `16px` on mobile. The `96px` top section padding likely reduces to `48px` or `32px`. The 64px/40px heading scale will need fluid type or breakpoint overrides for mobile.

Transition timing: `--duration-normal` (250ms) suggests smooth but not sluggish animations across all viewport sizes.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#f9f9f9` (base) / `#ffffff` (surface) / `#fcfcfc` (elevated)
- Accent: `#ff6b35` (brand coral-orange)
- Text: `#1a1a1a` (primary) / `#666666` (secondary) / `#888888` (muted)
- Fonts: Space Grotesk (headings, -tracking) + Inter (body) + JetBrains Mono (UPPERCASE labels)
- Shadow: 6-level named system at 0.04–0.12 opacity

**Prompt starters:**
- "Design a feature card in Matte style: `#f9f9f9` base, `#ffffff` card surface, `--shadow-sm`, 12px corners, Space Grotesk h3 at 20px/-0.4px, Inter body."
- "Build a CTA section: coral `#ff6b35` button with spring easing, `--shadow-glow` highlight, JetBrains Mono uppercase eyebrow label."
- "Create a stats display: Space Grotesk 64px/-2.56px bold number, Inter secondary label, warm neutral background, no decorative elements."

*Generated by Sparkbites — extracted from live CSS analysis*
