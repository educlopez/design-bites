# luleav2.framer.website — Design System

## 1. Visual Theme & Atmosphere

luleav2.framer.website is a Framer-built portfolio that balances editorial scale with structural minimalism. The hero typography is bold and cinematic — Inter at 42px with a striking −2.4px letter-spacing — creating the kind of large, tightly-set display text associated with editorial design and high-end agency sites. The canvas is near-white (`#fafafa`) while the footer drops to near-black (`#161616`), creating a dramatic tonal bookend. Multi-layered shadows and generous border-radius values signal a modern, polished aesthetic. The browser-default link blue appearing on anchor elements suggests the design is still partly in a raw Framer state, but the core typographic and layout decisions are deliberate and sophisticated.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(250,250,250)` / `#fafafa` | Page canvas |
| Footer background | `rgb(22,22,22)` / `#161616` | Dark section anchor |
| Primary text | `#000000` | All body and heading text |
| Secondary text | Implied mid-grey | Captions, metadata (inferred) |
| Link colour | `rgb(0,0,238)` | Browser default — anchor elements |
| Anchor hover bg | `rgb(242,242,242)` | Subtle hover surface |

The palette is near-monochrome with the footer dark section as the only significant colour departure. No brand accent or colour hierarchy beyond near-black/near-white contrast. The near-white (`#fafafa`) canvas prevents the harshness of pure white while maintaining cleanliness.

## 3. Typography Rules

**Primary typeface:** Inter  
**Fallback:** System sans-serif

- **H1:** Inter, 42px / 52.5px line-height / −2.4px letter-spacing / weight 400 — large, editorial, tightly tracked
- **Body (p):** Inter, 16px / 25.6px line-height / weight 400 — comfortable reading
- **Navigation / UI text:** Inter, 14px / weight 400–500
- **Button text:** System sans-serif, 12px — likely unstyled Framer default

The H1 at −2.4px tracking on 42px type is the design's most distinctive typographic signature. This negative tracking at display sizes creates the dense, magazine-like quality seen in contemporary portfolio sites. Weight 400 on display text is another deliberate choice — letting tracking and size carry the visual weight rather than boldness.

## 4. Component Stylings

- **Cards / blocks:** Multi-layer shadows (`rgba(0,0,0,0.06)` cascading), `8px`–`16px` border-radius
- **Navigation:** Transparent background, black text
- **Footer:** `#161616` background — full-width dark section
- **Links:** Browser default blue with `#f2f2f2` hover background — partially unstyled
- **Buttons:** System default — unstyled Framer fallback
- **Border-radius scale:** `4px`, `8px`, `16px`, `48px`, `100%` — full range from sharp to circular
- **Shadows:** Multi-layered, low-opacity Framer default shadow stack

## 5. Layout Principles

Framer's layout engine handles grid and spacing, but extracted data shows section-level zero-margin defaults — Framer manages spacing through its canvas system. The `#fafafa` canvas and `#161616` footer suggest a sections-based design where full-width bands define the page rhythm. The large display heading implies a hero section with significant vertical space. Navigation is minimal and transparent, likely sticky.

## 6. Depth & Elevation

- Multi-layer shadow system: 4–5 cascading `rgba(0,0,0,0.06)` shadows create depth on card components
- Footer elevation is achieved through colour contrast (`#161616` vs `#fafafa`) rather than shadow
- Border-radius progression (4→8→16→48→100%) maps to component scale
- Framer's shadow tokens are consistent with the loganliffick.com multi-layer approach

## 7. Do's and Don'ts

**Do:**
- Use Inter at 42px+ with −2.4px tracking for display headings
- Keep body text at Inter 16px / weight 400
- Use `#fafafa` as canvas — avoid pure white
- Use the dark footer (`#161616`) as a visual anchor
- Apply multi-layer shadows to card surfaces at 8px–16px radius

**Don't:**
- Bold the display heading — let tracking and scale do the work
- Add colour accents; the palette is intentionally neutral
- Override link colours until the design is fully resolved
- Use border-radius above 16px for content cards (48px is for pills/avatars only)
- Mix font weights aggressively — 400 and 500 are sufficient

## 8. Responsive Behavior

Breakpoints: 420px, 810px, 1200px (standard Framer three-breakpoint system).  
Display heading (42px) likely scales down significantly at mobile — to ~24–28px. The section-based layout reflows columns to single-stack. The dark footer remains full-width at all breakpoints. Navigation likely becomes a hamburger menu at sub-420px.

## 9. Agent Prompt Guide

> Replicate luleav2.framer.website: `#fafafa` canvas, `#161616` footer. Inter for all type — display heading at 42px/weight 400/−2.4px tracking, body at 16px/weight 400. Monochromatic black-on-near-white. Multi-layer card shadows at `rgba(0,0,0,0.06)`. Border-radius 8px–16px for cards. Section-based layout with full-width dark footer section as anchor. No colour accents. Sophisticated display typography is the brand.

---
*Generated by Sparkbites — extracted from live CSS analysis*
