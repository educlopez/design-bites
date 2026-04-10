# papatui.com — Design System

## 1. Visual Theme & Atmosphere

Papatui is an e-commerce brand with a distinctly organic, warm character — somewhere between a heritage outdoor brand and a modern sustainable goods shop. The palette is anchored by linen tones and earthy greens, with a terracotta-orange accent that gives the entire system life and warmth. The background is clean white with an off-white dark mode variant, but the brand identity lives in the neutral warm grays (`#d6d2c4`, `#ccc7b5`) and the deep forest green (`#3e4827`) used for headings and buttons. Typography uses Barlow in uppercase with tight letter-spacing for titles and buttons — assertive but not aggressive. SF Mono as the body typeface is an unusual choice for e-commerce, lending a crafted, slightly technical quality that differentiates the brand from generic Shopify stores. The overall feeling: artisanal quality, earthy confidence.

## 2. Color Palette & Roles

**Brand neutrals (the base identity):**

| Role | Value | Usage |
|---|---|---|
| Brand Sand | `#d6d2c4` (`--color--brand`) | Primary brand neutral, labels, title borders, swatches |
| Brand Sand Dark | `#ccc7b5` (`--color--brand-dark`) | Hover/active state of brand sand |
| Brand Sand Light | `#e0ddd3` (`--color--brand-light`) | Soft fill surfaces |

**Text hierarchy:**

| Role | Value | Usage |
|---|---|---|
| Primary Text | `#212322` (`--color--text`) | Body copy — near-black with warmth |
| Text 70% | `rgba(33,35,34,0.7)` | Secondary body text |
| Text 55% | `rgba(33,35,34,0.55)` | Tertiary / supporting |
| Text 20% | `rgba(33,35,34,0.2)` | Disabled, placeholder |
| Alt Text | `#8b8b8b` | Captions, metadata |
| Headings | `#3e4827` (`--color--headings`) | Forest green — all headlines |

**Interactive:**

| Role | Value | Usage |
|---|---|---|
| Button / CTA | `#3e4827` | Primary button fill — forest green |
| Accent | `#db864e` (`--color--accent`) | Terracotta orange — price highlights, promotions |
| Accent Dark | `#d77839` | Hover state of accent |
| Link (on dark) | `#ffffff` | White links on dark backgrounds |
| Link (on light) | `#978d6a` | Muted golden for inline links |

**Status / labels:**

| Role | Value | Usage |
|---|---|---|
| Sale / Low Stock | `#C00000` | Urgency red — sale prices, scarcity |
| In Stock | `#4A9F53` | Positive green confirmation |
| New label | `#e5e5e5` | Light gray label background |
| Highlight label | `#f2eb78` | Soft yellow — custom label variant |
| Background | `#ffffff` | Page canvas |
| Background Dark | `#f2f2f2` | Section alternates, sold-out label bg |
| Drop Shadow | `rgba(33,35,34,0.08)` | Soft shadow on cards and drawers |

## 3. Typography Rules

- **Titles & Buttons: Barlow** — A condensed, rational sans-serif used in `uppercase` with `letter-spacing` for wayfinding. Weight 500. The uppercase transform on both titles and buttons creates a consistent retail cadence.
- **Body: SF Mono** — `"SF Mono", Menlo, Consolas, Monaco, Liberation Mono, Lucida Console, monospace`. Monospaced body text is unexpected in e-commerce but gives Papatui a craft-forward, maker-culture personality.
- **Nav spacing:** `--font--nav-spacing: 36px` — generous horizontal gap between navigation items.

| Element | Family | Weight | Transform | Letter Spacing |
|---|---|---|---|---|
| Titles / Headings | Barlow | 500 | uppercase | `0px` (overridden by border style) |
| Buttons (desktop) | Barlow | 500 | uppercase | 1px |
| Buttons (mobile) | Barlow | 500 | uppercase | `12px` font size |
| Body / product desc. | SF Mono | 400 | none | normal |
| Mega menu | Barlow | — | — | `12` units |

**Title border:** `--font--title-border: 1` with `3px` size — a bottom border decoration on heading elements.

## 4. Component Stylings

- **Primary buttons:** Forest green `#3e4827` fill, white text, uppercase Barlow, `1px` letter-spacing. Hover uses `--accent-dark` or shade.
- **Product labels:** Pill-shaped badges in `#d6d2c4` (brand), `#e5e5e5` (new), `#f2eb78` (custom highlight), `#c00000` (discount), `#f2f2f2` (sold out).
- **Announcements bar:** `announcement__link__text` and `announcement__bg` components — likely a top-of-page promotional strip.
- **Drawers:** `--color--drawer-bg: #ffffff` — slide-over panels (cart, filters) on clean white.
- **Product cards:** Transparent background (`--color--product-bg: rgba(0,0,0,0)`) — images bleed to page background. Drop shadow `rgba(33,35,34,0.08)` on hover.
- **Okendo reviews:** `--oke-*` tokens present — integration with the Okendo review platform, using brand button and font styles.

## 5. Layout Principles

- **Mobile scale:** `--octane-mobile-scale: 1` — explicit mobile typography scaling token.
- **Sticky header:** `--header-is-sticky` variable — header locks to viewport top.
- **Spacing:** 20px, 30px, 36px, 48px values suggest an 8px base grid with comfortable retail-scale whitespace.
- **Nav spacing:** `36px` gap between nav items — wide, airy navigation.
- **Product grid:** Standard Shopify-style responsive grid implied by the stack (product forms, drawers, announcement bars).

## 6. Depth & Elevation

- **Drop shadow:** `rgba(33,35,34,0.08)` — an 8% warm-tinted shadow. Softer than a pure black shadow, aligned with the brand's warm color temperature.
- **Background alpha:** `rgba(255,255,255,0.8)` for the sticky header — frosted glass effect on scroll.
- **No hard borders** on primary surfaces — depth is communicated via shadow and background contrast alone.

## 7. Do's and Don'ts

**Do:**
- Use forest green `#3e4827` for all primary CTAs and headings — it's the color of decision
- Use terracotta `#db864e` only for pricing, promotions, and genuine accent moments
- Apply Barlow in uppercase for all interactive labels and headings
- Use SF Mono for body copy — it's the brand's personality differentiator, keep it

**Don't:**
- Don't use `#C00000` outside of sale/urgency contexts — it reads as alarm
- Don't use `#f2eb78` yellow for more than one label type per page
- Don't mix Barlow (non-uppercase) with the headline style — the uppercase transform is non-negotiable
- Don't replace SF Mono with a more conventional sans for body — that would erase the brand's distinctiveness

## 8. Responsive Behavior

- `--font--button-mobile-size: 12px` — buttons reduce from 13px desktop to 12px mobile.
- `--octane-mobile-scale: 1` — a scaling multiplier ready to be overridden for larger-display mobile optimization.
- Header becomes sticky on scroll (`--header-is-sticky`).
- Mega menu and nav spacing (`36px`) collapse on mobile — expect a hamburger pattern.
- Drawer components (cart, filters) are optimized for touch: full-height slide-overs with white canvas.

## 9. Agent Prompt Guide

**Quick reference:**
- Background: `#ffffff` | Body text: `#212322`
- Headings + buttons: `#3e4827` (forest green)
- Accent: `#db864e` (terracotta)
- Brand neutral: `#d6d2c4` (warm sand)
- Title font: Barlow, 500, uppercase
- Body font: SF Mono, 400

**Prompt starters:**
- *"Artisanal e-commerce brand: white canvas, forest green `#3e4827` headings and CTAs, terracotta `#db864e` accents, warm sand `#d6d2c4` brand neutrals, Barlow uppercase titles, SF Mono body."*
- *"Heritage outdoor/craft shop aesthetic: earthy greens and terracotta, monospace body type (SF Mono), uppercase Barlow for navigation and buttons, minimal shadows."*

---

*Generated by Sparkbites — extracted from live CSS analysis*
