# AWSMD — Design System Reference

## 1. Visual Theme & Atmosphere

AWSMD is a design and development agency whose site performs the same work it sells. The design is bold, high-contrast, and portfolio-forward: a white canvas interrupted by full-bleed hero sections and colorful service cards that act as product swatches. The palette mixes cool neutrals with expressive accent colors — peach-orange, soft blue, electric indigo — applied per project tile rather than globally. The result feels curated and editorial, like a magazine layout that happens to be interactive. Nothing is subtle about the hero, but the system beneath it is restrained and grid-disciplined.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255,255,255)` — page background, nav surface
- `rgb(0,0,0)` — primary text throughout

**Supporting surfaces**
- `rgb(201,208,213)` — footer (cool blue-gray, desaturated)
- `rgb(241,241,241)` — default button background
- `rgb(153,153,153)` — h3 / secondary label text

**Hero**
- H1 renders in `rgb(255,255,255)` — white text on a dark/image background, full inversion zone

**Service card accents (per-item, not global)**
- `rgb(241,174,134)` — peach-orange service card
- `rgb(144,166,208)` — dusty blue service card

**Portfolio gradient overlays**
- `rgb(95,140,254)` — bright periwinkle gradient
- `rgba(72,88,228,0.4)` — indigo logo overlay at partial opacity

These accent colors exist only on card/tile elements — they never appear in the navigation, forms, or body copy. Color is editorial, not systemic.

---

## 3. Typography Rules

AWSMD uses a single typeface: **Inter**. The choice is pragmatic — Inter's neutrality allows the portfolio imagery and color cards to dominate visually without typographic competition.

**Scale**
| Role | Size | Weight |
|------|------|--------|
| H1 (hero) | Large display | bold |
| H3 | subdued labels | regular |
| Input / form | 20px | 500 |
| Body | standard | 400 |

- 20px at medium weight for inputs is unusually large — forms feel substantial and accessible
- H3 in `rgb(153,153,153)` creates a clear three-level hierarchy without color
- No letter-spacing customization — Inter runs at default tracking throughout

**What's absent:** No display font, no serif contrast. Typography is intentionally background-level to keep visual focus on the work itself.

---

## 4. Component Stylings

**Buttons**
- Default: `rgb(241,241,241)` fill — a light gray that reads as neutral/secondary
- No rounded corners on Fancybox buttons (`--f-button-border-radius: 0`) — the lightbox UI is deliberately rectangular
- `--f-button-hover-bg: #e0e0e0`, `--f-button-active-bg: #d0d0d0` — darkening steps on hover/active

**Swiper / lightbox system**
- Theme color: `#007aff` (Apple blue) — a Swiper default that was not overridden; notable as the only bright hue in the entire system

**Service cards**
- Full-bleed colored backgrounds replace typical card borders
- Black text on colored backgrounds maintains legibility

---

## 5. Layout Principles

The site is structured around distinct full-width sections — hero, services grid, portfolio tiles — that each establish their own visual context. The nav sits transparent over the hero, which is why H1 appears white against a dark background. The footer is a distinct surface color (cool gray), not a continuation of the white page. No explicit grid token is defined in custom properties; layout is handled through standard CSS grid/flex utilities. Swiper is used for portfolio carousels, suggesting content-heavy sections scroll horizontally.

---

## 6. Depth & Elevation

Minimal elevation system. No persistent `box-shadow` on surface components. Depth comes from background-color contrast between sections (white body → colored card → dark hero) rather than shadows or blurs. The lightbox library (Fancybox) uses its own shadow conventions; those are third-party and isolated.

---

## 7. Do's and Don'ts

**Do:**
- Reserve accent colors (peach, blue, indigo) exclusively for portfolio/service cards
- Keep navigation, body, and forms in the black/white/neutral range
- Use full-bleed section backgrounds as the primary layout separator
- Apply color-per-card as an editorial system — each card gets one accent, never shared

**Don't:**
- Override the Swiper `#007aff` without replacing it consistently across the lightbox
- Apply border-radius to lightbox/media buttons — sharp edges are intentional
- Use color in typographic elements — headings and labels stay in neutral grays
- Crowd the color palette — the controlled use of 2-3 accent tones per section is what makes them feel premium

---

## 8. Responsive Behavior

No breakpoints are surfaced in the extracted custom properties, suggesting Tailwind utility breakpoints handle all responsive logic. The Swiper component enables touch-based carousel navigation at mobile sizes, which is likely the primary content interaction on small viewports.

---

## 9. Agent Prompt Guide

> Build a UI that matches AWSMD's design language.

White canvas, black text, no border-radius on UI controls. Use Inter at standard weight — do not customize letter-spacing. Reserve all accent color (peach `rgb(241,174,134)`, dusty blue `rgb(144,166,208)`, periwinkle `rgb(95,140,254)`) for portfolio or service card backgrounds only. The footer is a distinct cool-gray surface `rgb(201,208,213)`. Hero sections fully invert: dark background, white text. Buttons are light gray and rectangular. Keep typography background-level — let imagery and color cards carry the visual weight.

---

*Generated by Sparkbites — extracted from live CSS analysis*
