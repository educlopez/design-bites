# Coming Soon New York — Design System

## 1. Visual Theme & Atmosphere

Coming Soon New York projects an editorial minimalism rooted in fashion retail. The palette is anchored to a true white and true black core — clean, undecorated, with no gradient softness — punctuated by a vivid indigo accent (#4a4af4) that acts as the site's sole point of brand color energy. Typography is handled entirely by Söhne, a geometric grotesque with humanist undertones, lending authority without coldness. The overall atmosphere is confident and curated: a gallery that sells.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Background | `#ffffff` | Page canvas |
| Foreground / Text | `#101820` | Near-black, warm undertone |
| Footer background | `#000000` | Hard black anchor |
| Footer text | `#ffffff` | Full contrast |
| Brand accent | `#4a4af4` | Indigo — CTAs, brand emphasis |
| Accent light | `#A8A9FC` | Soft indigo for hover/disabled states |
| Accent dark | `#2F2FC1` | Deep indigo for active states |
| Overlay | `rgba(25,25,37,0.9)` | Near-black modal scrim |
| Neutral 2 | `#F0F5F7` | Light grey tint for cards/surfaces |
| Muted text | `#6D6E71` | Secondary copy, captions |
| Button primary bg (inverse) | `#ffffff` | White on dark contexts |
| Alert / Sold Out | `rgb(222,28,36)` | Warning red, used sparingly |
| Sale / Promo | `rgb(255,93,155)` | Hot pink for promotional tags |

The palette is essentially monochrome with a single vivid hue. Do not introduce warm tones or gradients.

---

## 3. Typography Rules

**Primary typeface:** Söhne (Klim Type Foundry) with a system-sans fallback stack.

| Level | Size | Weight | Line Height | Tracking | Notes |
|-------|------|--------|-------------|----------|-------|
| h2 (hero) | 60px | 500 | 64px | -0.6px | Editorial headline |
| Body / h1 computed | 16px | 400 | 24px | normal | Default text |

- OpenType features `kern`, `liga`, `lnum`, `pnum` are active — proportional numbers, ligatures.
- No text transforms, no uppercase forcing.
- Letter-spacing is subtle: only negative on large display text.
- Söhne is a premium custom typeface — if unavailable, the fallback chain (apple-system, Helvetica) retains the humanist grotesque character.

---

## 4. Component Styling

- **Primary button (light context):** White background, near-black text (#0c0c14). Hover → light grey (#e5e5e9) with muted text (#313142).
- **Primary button (dark context):** Inverts to match — white on dark.
- **Secondary buttons:** Ghost style, white text on dark backgrounds.
- **Sold Out state:** Red background (#de1c24) with white text — clearly distinct, non-interactive appearance.
- **Overlays:** Semi-opaque dark scrim `rgba(25,25,37,0.9)` — does not completely black out, retains depth.
- Spacing tokens: `2px`, `24px`, `40px` — tight micro-spacing, comfortable paragraph spacing.
- Minimum button width: 48px.
- No border-radius tokens defined — components are sharp-cornered.

---

## 5. Layout Principles

- Sections carry 60px padding — breathing room without excess.
- Footer has 60px vertical padding with a 120px top margin separating it from content.
- Header gaps of 60px create generous nav spacing.
- No grid tokens are exposed — layout is compositionally controlled rather than grid-systematic.
- The site is viewport-height aware (`--vh: 8px` suggests JS-calculated vh).

---

## 6. Depth & Elevation

- No box-shadow tokens are used. Elevation is communicated through color contrast alone (white surface vs. black footer, dark overlay vs. content).
- The overlay system (`rgba(25,25,37,0.9)`) is the primary depth mechanism for modals.
- Flat, paper-like surfaces — consistent with editorial fashion aesthetics.

---

## 7. Do's and Don'ts

**Do:**
- Use indigo (#4a4af4) exclusively as the accent — one brand color, applied purposefully.
- Keep type in Söhne; rely on weight and size for hierarchy, not colour.
- Maintain hard black/white contrast for primary surfaces.
- Use the muted grey (#6D6E71) for metadata and supporting copy.

**Don't:**
- Introduce gradients or multi-stop colour fills.
- Add border-radius to buttons or cards — the design is deliberately square-cornered.
- Use the sale pink (#ff5d9b) outside promotional/tag contexts.
- Override the OpenType feature settings — they are intentional.

---

## 8. Responsive Behavior

- Viewport height is dynamically calculated via JS (`--vh`), accommodating mobile browser chrome.
- Sections collapse from 60px padding — no specific breakpoint tokens are exposed in CSS custom properties.
- The transition curve is `cubic-bezier(0.25, 0.1, 0.25, 1)` (ease) at 0.1s — fast, subtle micro-interactions.
- Mobile should retain the editorial sparsity; avoid stacking too many visual elements.

---

## 9. Agent Prompt Guide

> Build a fashion e-commerce interface using the Coming Soon New York design language. Use Söhne (or Helvetica as fallback) at 400/500 weight. Background is white (#ffffff), text near-black (#101820), footer black (#000000). Single brand accent: indigo #4a4af4 for CTAs and interactive states. No border-radius, no gradients, no shadows. Section padding 60px. Buttons are flat rectangles with white/indigo fills. OpenType features: kern, liga, lnum, pnum. Transitions at 0.1s ease.

---

*Generated by Sparkbites — extracted from live CSS analysis*
