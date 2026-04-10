# syrn.com — Design Document

## 1. Visual Theme & Atmosphere

Syrn is a fashion e-commerce brand with a distinctly editorial sensibility. The design operates with the restrained confidence of a contemporary clothing label: white ground, black type, minimal ornamentation. But beneath that classical restraint lives a single electric decision — the quick-add badge accent is a sharp acid yellow-green (`#e6ff7d`), landing like a neon price tag in an otherwise monochrome store. The typographic choice of Neue Haas Unica W1G reinforces this duality: a typeface with Swiss modernist roots used in a fashion-forward context. The atmosphere is premium without being precious, and functional without being clinical.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `#ffffff` | Page, header, drawer |
| Foreground / text | `#333333` | All body copy |
| Pure black | `rgb(0, 0, 0)` | Borders, headings, buttons |
| Accent (badge/highlight) | `#e6ff7d` (acid yellow-green) | Badges, quick-add CTA, progress fills |
| Brand teal (buttons) | `rgb(8, 63, 74)` | Button text/border on interactive elements |
| Notification bg | `rgb(18, 31, 54)` | Dark navy for toast / notification panels |
| Notification border | `rgb(190, 229, 235)` | Teal-tinted edge on notification panels |
| Overlay | `rgba(0, 0, 0, 0.4)` | Drawer and modal scrim |

The palette is binary in spirit: black and white, then the acid yellow as the single charged interruption. The teal (`rgb(8, 63, 74)`) is a dark, earthy complement — it appears in CTAs and the progress fill, never decoratively.

---

## 3. Typography Rules

**Typeface:** Neue Haas Unica W1G — a Swiss grotesque with clean curves, slightly warmer than Helvetica. Signals craft and premium positioning without the tech-product associations of Geist or Inter.

| Context | Size | Weight | Leading | Notes |
|---|---|---|---|---|
| Section headings (h2) | 19.2px | 700 | 49.5px | Generous line height, editorial spacing |
| Labels / eyebrows | 12px | 700 | 30px | Uppercase — the only instance of text-transform |
| Buttons | 10px | 400 | 12px | Deliberately small; refined, not loud |
| Inputs | 16px | 400 | normal | Standard form legibility |

The use of uppercase at 12px/700 for labels is a classically editorial move — it gives hierarchy without size. Buttons at 10px are unusually small, which communicates restraint and confidence: the brand doesn't need to shout. No letter-spacing adjustments on headings; the typeface is trusted to handle its own rhythm.

---

## 4. Component Styling

Buttons are ghost-style by default — transparent background, black border matching the brand tone. The teal (`rgb(8, 63, 74)`) appears as text and border color, not as fill, maintaining the light feel. Badges use the acid yellow-green fill with black text for maximum contrast. Shadows are soft and enveloping: `rgba(0,0,0,0.2) 0px 0px 25px` for card/drawer overlays and `rgba(63,63,68,0.4) 0px 4px 10px` for lifted UI elements. Border radii are intentionally minimal — only `2px` (nearly sharp) and `50%` (for circular avatar/badge elements). No pill buttons; everything is close to a right angle.

---

## 5. Layout Principles

The page width is capped at `90rem` (1440px) with `20px` horizontal margins (`14px` on mobile), keeping content tight against the viewport edge — an editorial choice that prioritizes full-bleed imagery. Breakpoints at `820px` and `860px` are narrow, close together, suggesting a single critical transition point for the product grid. The Swiper integration (detected via `--swiper-theme-color`) indicates carousel-based product browsing rather than static grids.

---

## 6. Depth & Elevation

Two shadow styles define the depth vocabulary:
- **Ambient glow:** `rgba(0,0,0,0.2) 0px 0px 25px` — used for drawers and overlays; a soft omnidirectional halo
- **Directional card lift:** `rgba(63,63,68,0.4) 0px 4px 10px` — a grounded, slightly warm shadow for interactive product cards

The `rgba(0,0,0,0.4)` drawer overlay is the strongest depth signal on the page, used to focus the user on the slide-in cart or filter panel. No colored shadows; depth is strictly achromatic.

---

## 7. Do's and Don'ts

**Do:**
- Use `#e6ff7d` sparingly — only for badges and promotional highlights
- Keep borders at `2px` radius or square; avoid rounding
- Set labels and eyebrows in uppercase at 12px/700
- Use the dark navy (`rgb(18, 31, 54)`) only for notification/toast contexts
- Trust Neue Haas Unica to carry hierarchy without aggressive sizing

**Don't:**
- Use the acid yellow as a background color on large surfaces
- Increase button font sizes above 12px — the small scale is intentional
- Add decorative gradients or drop shadows on text
- Introduce a second accent color; the teal and acid yellow must not compete
- Use `50%` radius on rectangular elements — reserve it for avatars/icons only

---

## 8. Responsive Behavior

Mobile uses `14px` side margins (tighter than desktop's `20px`), suggesting near-full-bleed images on small screens. The breakpoints at `820px` and `860px` are unusually close, likely handling a specific product grid reflow from 2-column to 3-column. No standard mobile-first breakpoint ladder; the responsive system is bespoke to the Shopify theme structure. Carousels replace grids below the primary breakpoint.

---

## 9. Agent Prompt Guide

> Recreate a fashion e-commerce interface in the style of syrn.com. White background (`#ffffff`), dark foreground (`#333333`), borders and type in pure black. Typography is Neue Haas Unica W1G — headings at 19px/700 with generous line height, button labels at 10px/400. One accent only: acid yellow-green `#e6ff7d` for badges and highlights. Shadows are soft and omnidirectional (`rgba(0,0,0,0.2) 0 0 25px`). Border radius is `2px` maximum — almost square. Buttons are ghost/outlined. Uppercase labels at 12px add hierarchy without size.

---

*Generated by Sparkbites — extracted from live CSS analysis*
