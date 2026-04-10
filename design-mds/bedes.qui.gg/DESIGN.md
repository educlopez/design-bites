# bedes.qui.gg — Design System Reference

## 1. Visual Theme & Atmosphere

bedes.qui.gg is a personal site that makes a deliberate and rare choice: an entirely serif typographic system. Where most developer portfolios reach for Inter or a geometric grotesque, this site sets IBM Plex Serif as its sole typeface — every selector from `body` to `button` uses it. The result is warm, literary, and unhurried, closer to an online essay or personal journal than a portfolio. The colour system is warm parchment-like neutrals — off-whites with a subtle yellow-brown temperature. There are no shadows, no gradients, no border radius variation (a single `4px`). The design philosophy here is restraint through editorial confidence: good typography does the work, decoration is absent by design. Built with Tailwind CSS.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Page canvas | `rgb(253, 253, 252)` | Near-white with warm undertone |
| White surface | `rgb(255, 255, 255)` | Elevated cards (`bg-gray-00`) |
| Body text | `rgb(99, 99, 94)` | Default text — warm grey |
| Heading text | `rgb(33, 32, 28)` | H1, hover states — deep warm black |
| Warm border tint | `rgba(32, 16, 0, 0.063)` | Subtle warm-tinted dividers |
| Subtle fill | `rgba(37, 37, 0, 0.027)` | Near-invisible section backgrounds |
| Focus ring | `rgb(0, 144, 255)` | System blue inset focus ring |

The palette is warm-neutral — every value carries a slight yellow-brown temperature rather than true grey. The two text tones (`#63635e` body, `#21201c` heading) create a gentle, non-harsh reading contrast. The system has no chromatic accents; the only saturated colour is the browser's focus ring.

## 3. Typography Rules

**Sole typeface:** IBM Plex Serif — a humanist serif with high legibility at body sizes and genuine character at display sizes. Fallback: `Georgia, "Times New Roman", serif`.

**No weight variation beyond two values:** 400 (Regular) for body, paragraphs, headings (h1, h2), links, and buttons; 700 (Bold) only for h3.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| Display / paragraphs | 24px | 400 | 32px | normal |
| H1 | 24px | 400 | 32px | normal |
| H2, body, links, buttons | 16px | 400 | 24px | normal |
| H3 | 16px | 700 | 24px | normal |

The near-flat hierarchy (h1 and paragraphs share 24px/400) suggests that visual structure comes from spacing and placement rather than type weight or size shifts. No letter-spacing manipulation — IBM Plex Serif is trusted to handle its own optical spacing.

## 4. Component Stylings

**Buttons:** No background fill, IBM Plex Serif, body-sized text in warm grey (`#63635e`). On hover, text darkens to `#21201c`. On focus, an inset ring in `rgb(0, 144, 255)` at 2px appears — the only chromatic moment in the system.

**Links:** Same treatment as buttons — transparent background, serif text, hover brightens to deep warm black.

**Cards:** White surface (`rgb(255,255,255)`) against the near-white canvas creates a minimal lift. `4px` border-radius is the only rounding in the system.

**Borders:** Warm-tinted at very low opacity (`rgba(32,16,0,0.063)`) — barely perceptible dividers that add structure without weight.

**Shadows:** None. Zero shadows in the entire system.

## 5. Layout Principles

Section horizontal padding is `64px`. Footer uses a negative horizontal margin (`-16px`) to allow full-bleed edge-to-edge treatments. No detected breakpoints — this may be a deliberately minimal responsive setup, or breakpoints exist in Tailwind's config rather than inline styles. The single `4px` border radius and absence of a multi-step spacing scale points to a hand-authored, opinionated layout rather than a design system grid.

## 6. Depth & Elevation

No shadows. No blur effects. Depth is achieved solely through the two-tone warm-neutral colour relationship: `rgb(253,253,252)` canvas vs `rgb(255,255,255)` card. The difference is subtle enough to feel paper-like rather than digital. The warm-tinted border tint at 6.3% opacity traces edges without casting weight. This is a deliberately flat, print-inspired elevation system.

## 7. Do's and Don'ts

**Do:**
- Use IBM Plex Serif for every text element — the mono-typeface system is the identity
- Let warm grey (`#63635e`) be the default text colour; reserve deep black (`#21201c`) for headings and hover states
- Keep border radius to 4px only — no pill shapes, no circular avatars
- Use focus rings as the only chromatic moment in the page
- Trust whitespace and line-height to create reading rhythm — avoid decorative dividers

**Don't:**
- Introduce a sans-serif typeface — even for UI chrome or metadata
- Add shadows or elevation layers — the flat paper aesthetic is intentional
- Use letter-spacing manipulation — IBM Plex Serif sets its own spacing
- Introduce colours beyond the warm neutral palette — no accent hues
- Add more than two type weights — Regular and Bold are the full range

## 8. Responsive Behavior

No media query breakpoints were detected in the extracted CSS. Either the site is a fixed-layout personal page, or all responsive behaviour is handled via Tailwind utility classes at build time (not captured in computed styles). Section padding (`64px`) may not collapse on mobile — consider overriding for small screens if adapting this system.

## 9. Agent Prompt Guide

> "Design in the style of bedes.qui.gg: warm parchment canvas (`rgb(253,253,252)`), IBM Plex Serif as the sole typeface for every text element. Body text in warm grey (`#63635e`), headings in deep warm black (`#21201c`). No shadows, no gradients, no rounded shapes beyond 4px. Flat, print-like elevation through subtle warm-tinted borders. Let typographic rhythm and whitespace create all structure. No accent colours — the focus ring blue is the only chromatic moment."

---

*Generated by Sparkbites — extracted from live CSS analysis*
