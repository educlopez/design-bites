# alexandravaldivieso.com — Design Language

## 1. Visual Theme & Atmosphere

Alexandra Valdivieso's site reads as a high-end fashion portfolio: opulent yet restrained, built on the tension between stark white and near-black surfaces. The design borrows from editorial print — large-scale serif headlines that crowd the line height, full-bleed imagery overlaid with translucent washes, and a navigation that disappears into the background until needed. Colour accent (a single coral-pink) is held back like a designer's signature, appearing only on accessibility elements and hover moments. The overall atmosphere is confident silence: the work speaks, the interface steps aside.

## 2. Color Palette & Roles

**Background layer**
- `#ffffff` — Primary canvas; body and content sections.
- `rgb(241, 243, 249)` — Slightly cool off-white surface (`div.top-bun`); used to separate hero from content without hard lines.

**Foreground & text**
- `rgb(0, 0, 0)` — Body copy and navigation labels.
- `rgb(241, 243, 249)` — Headline text rendered over dark imagery; cool ivory that lifts off dark backgrounds.
- `rgb(255, 255, 255)` — Link labels and CTA text on dark or coloured backgrounds.

**Dark surfaces**
- `rgb(28, 28, 28)` — Mobile/overlay menu background (`div.header-menu-bg`); near-black that keeps brand warmth without going full black.

**Accent**
- `rgb(255, 105, 127)` — Coral-pink; used exclusively on the skip-link and accent moments. Signals interaction, not decoration.

**Overlay**
- `rgba(0, 0, 0, 0.5)` — Semi-transparent image overlay (`div.fluidImageOverlay`); controls photo luminance without masking the image entirely.

No custom CSS properties or tokens are defined — all values are hardcoded, consistent with a Squarespace/fluid grid build.

## 3. Typography Rules

Two typefaces, clearly ranked:

**Gilda Display** — Display / editorial serif. Used for `h2` headlines at `77.44px / 78px` line-height (tight ratio near 1:1), `font-weight: 400`, letter-spacing `−1.55px`. The tight leading and negative tracking create dense, poster-like type blocks. No uppercase transform — the elegance is in the letterform itself.

**Open Sans** — Functional sans. Used for body paragraphs (`p`, `div`) and buttons at `16px`. Weight stays at `400`; no tracking adjustments. Its neutrality deliberately recedes behind the display face.

What is absent: no monospace, no variable fonts, no font-feature-settings beyond defaults, no uppercase transforms. The typographic palette is intentionally minimal — two roles, two typefaces, nothing else.

## 4. Component Stylings

**Navigation** — Transparent background over hero; switches to `rgb(28, 28, 28)` for the mobile overlay menu. No visible border or shadow on default state.

**Floating cart** — Background matches the coral accent `rgb(255, 105, 127)` family, positioned absolutely. Rounded with `300px` radius (effectively pill/circle).

**Image overlays** — `rgba(0,0,0,0.5)` wash applied via `div.fluidImageOverlay`. No blur, no gradient — a clean flat dim.

**Buttons** — Open Sans 16px, weight 400. No apparent shadow, no border-radius tokens beyond `50%` (circular) and `300px` (pill). CTAs are text-weight, not bold.

**Border radii available:** `50%` (circular avatars/icons) and `300px` (pill buttons/badges). No intermediate radii — sharp rectangles or maximum-curve pills only.

## 5. Layout Principles

Section-based vertical rhythm: each `section` carries `padding-top: ~56px`, `margin: 0`. Content is full-width by default, constrained by inner containers. The grid is fluid (Squarespace fluid engine); no explicit grid or flex gap tokens are exposed.

One responsive breakpoint detected: `768px`. The layout collapses from a horizontal editorial arrangement to stacked single-column at mobile. The header switches to an overlay menu pattern at this threshold.

## 6. Depth & Elevation

No box-shadows are defined anywhere in the extracted CSS. Depth is created entirely through:
- **Layered photography** with the `rgba(0,0,0,0.5)` overlay.
- **Surface luminance contrast** between the `#f1f3f9` off-white zone and the `#1c1c1c` dark menu.
- **Typography scale** — the 77px display headline creates visual weight without chrome.

This is a deliberately flat, photography-first design: the images supply all the three-dimensionality.

## 7. Do's and Don'ts

**Do:**
- Use Gilda Display only for primary headlines; never for body or UI labels.
- Keep the coral `rgb(255, 105, 127)` scarce — one accent per view.
- Allow full-bleed images to dominate sections; reduce UI chrome around them.
- Use pill shapes (`300px` radius) for any CTA buttons.
- Keep text on dark-image sections in `rgb(241, 243, 249)` ivory, not pure white — it reads warmer.

**Don't:**
- Don't add intermediate grey surfaces — the palette is white, near-black, and one accent.
- Don't use bold or semibold weights; both typefaces stay at `400`.
- Don't introduce additional typefaces; two roles are the ceiling.
- Don't add drop shadows — they conflict with the flat, editorial tone.
- Don't use uppercase transforms on the display face; it loses its elegance.

## 8. Responsive Behavior

Single breakpoint at `768px`:
- Desktop: horizontal editorial layouts, large display typography, transparent nav.
- Mobile: stacked single-column, `rgb(28, 28, 28)` overlay navigation, type scale reduces proportionally.
- The 77px headline will need significant reduction on mobile (suggest ~40–48px) to avoid overflow, though no explicit mobile type scale is defined in the CSS.
- Cart floats as a fixed pill element at both breakpoints.

## 9. Agent Prompt Guide

> "Design in the style of alexandravaldivieso.com: white editorial canvas, one coral accent `rgb(255,105,127)`, Gilda Display for headlines at near-1:1 line-height with negative tracking, Open Sans 400 for body. No shadows. Full-bleed photography with `rgba(0,0,0,0.5)` overlays. Pill buttons (`border-radius: 300px`). Mobile collapses at 768px to stacked layout with dark overlay nav `rgb(28,28,28)`. Keep UI chrome minimal — the imagery does the visual work."

---

*Generated by Sparkbites — extracted from live CSS analysis*
