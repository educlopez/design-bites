# topazlabs.com — Design System

## 1. Visual Theme & Atmosphere

Topaz Labs presents as a premium dark-mode software product — AI video and photo enhancement tools dressed in a deep charcoal environment that communicates precision and power. The base is near-black (`rgb(24,24,24)`) with a carefully curated secondary palette that nods to natural materials: cream (`#f2f0ee`), stone (`#757678`), and slate (`#a8a7a3`). These earthy neutrals soften what could otherwise feel clinical.

Two functional accent colors cut through the dark: a vivid blue (`#2276f5`) for primary actions and progress, and a live-indicator red (`rgb(255,33,86)`) reserved for urgency states. Built on Webflow, the system is token-driven with an extensive CSS custom property architecture — evidence of a mature, systematized design process.

## 2. Color Palette & Roles

**Foundations:**

| Role | Token | Value | Usage |
|------|-------|-------|-------|
| **Canvas** | `--color--black` | `#000` | Deep backgrounds |
| **Surface** | body bg | `rgb(24,24,24)` | Default page surface |
| **Cream** | `--color--cream` | `#f2f0ee` | Light section backgrounds |
| **Stone** | `--color--stone` | `#757678` | Muted body text, captions |
| **Slate** | `--color--slate` | `#a8a7a3` | Secondary text, borders |
| **White** | `--color--white` | `#fff` / `#ffffff8c` | Headlines, ghost tints |

**Functional:**

| Role | Token | Value |
|------|-------|-------|
| **Primary action** | `--_topaz-brand---color-blue-hover` | `#2276f5` |
| **Progress/active** | `div.v26-video-bar-progress` bg | `rgb(45,129,255)` |
| **Live/alert** | `div.v26-live-indicator` bg | `rgb(255,33,86)` |
| **Success** | `--success-bg` / `--success-text` | `#d4edda` / `#155724` |
| **Error** | `--error-bg` / `--error-text` | `#f8d7da` / `#721c24` |
| **Dark deep** | `--b2--bg-dark` | `#0a0a1a` |

## 3. Typography Rules

**Typeface:** Area Normal (via `area-normal-edit, area-normal`) — a geometric display face with editorial presence.

Typography data shows H1 at `14.7px` for the Webflow admin layer; the public-facing product marketing likely scales to 48px+ display headings. The system uses `--vai4-text-grey` token for subdued text.

| Selector | Approx. Size | Weight | Notes |
|----------|-------------|--------|-------|
| `h1` (marketing) | 48–80px estimated | 400–500 | Area Normal, tight leading |
| `h3` | varies | 400 | Stone/slate color |
| Body | 16px | 400 | Slate `#a8a7a3` tones |
| `button` | 14–16px | 500 | White on dark, blue on hover |

**Notably absent:** No serif face. No monospaced font for UI. Letter-spacing is minimal — the typeface's geometry does the optical work.

## 4. Component Stylings

Rich component token system via CSS custom properties:

- **Buttons** — dark black background by default; `#2276f5` blue on hover; white text throughout
- **Video progress bar** — `rgb(45,129,255)` fill, dark track
- **Live indicator badge** — `rgb(255,33,86)` red pill; high contrast white text
- **Divider** — `--color--line-divider-light` at `#a8a7a340` (25% opacity) — hair-thin separators
- **Nav dividers** — `.v25-nav-divider` class; consistent 1px treatment
- **Icon buttons** — `.v26-icon-button`; square or circular, dark surface

**Spacing tokens:**
- `--spacing--x-small` — tight component internal spacing
- `--border-radius--ui-mobile` — consistent radius on UI elements

## 5. Layout Principles

- **Wide-screen first:** Breakpoints at `809`, `1199`, `1439`, `2559px` — built for 1440+ wide desktop monitors
- Dark surface sections alternate with cream `#f2f0ee` light sections for pacing
- Product UI screenshots likely occupy full-bleed regions
- Webflow grid system; section-level max-width with horizontal padding

## 6. Depth & Elevation

- **Dark deep** (`#0a0a1a`) for the deepest layers (modals, popovers)
- **Canvas** (`#181818`) as mid-ground surface
- **Hover state** (`--vai4-dark-hover`) lifts interactive elements slightly
- White at `#ffffff8c` (~55% opacity) for ghost/overlay surfaces
- Divider lines at 25% opacity rather than full — elevation expressed through translucency
- Shadows minimal; depth comes from background-color steps between `#000` → `#0a0a1a` → `#181818`

## 7. Do's and Don'ts

**Do:**
- Use `#2276f5` blue only for primary actions and progress states
- Reserve the red `rgb(255,33,86)` exclusively for live/urgent UI states
- Alternate dark and cream sections for long-form marketing pages
- Use token names (`--color--stone`, `--color--slate`) — the system is built for semantic reuse
- Keep white text at full opacity for headlines; use stone/slate for supporting copy

**Don't:**
- Mix the blue accent with other colorful elements — it must stay singular as the primary CTA color
- Use the red for anything decorative; it's a functional signal color
- Apply cream backgrounds in dark product UI; cream is for marketing/light sections only
- Override the spacing tokens with hardcoded values

## 8. Responsive Behavior

| Breakpoint | Context |
|-----------|---------|
| `< 810px` | Mobile |
| `810 – 1199px` | Tablet/small desktop |
| `1200 – 1439px` | Standard desktop |
| `1440 – 2559px` | Wide desktop (primary design target) |
| `≥ 2560px` | Ultra-wide / 4K |

The multi-breakpoint range suggests full responsive polish with layout reflows at each step. Mobile likely collapses video showcases to stacked cards.

## 9. Agent Prompt Guide

> "Design in the style of topazlabs.com: deep charcoal canvas `#181818`, primary text in white, supporting text in stone `#757678` and slate `#a8a7a3`, cream `#f2f0ee` for light sections, single blue accent `#2276f5` for CTAs, red `rgb(255,33,86)` for live/alert states only, Area Normal typeface, dividers at 25% opacity, alternating dark/light sections for content pacing — professional AI software aesthetic."

*Generated by Sparkbites — extracted from live CSS analysis*
