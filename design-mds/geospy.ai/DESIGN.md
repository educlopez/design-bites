# geospy.ai — Design System

## 1. Visual Theme & Atmosphere

GeoSpy AI communicates precision and authority — fitting for a geolocation intelligence product. Built in Framer, the site is surprisingly restrained: mostly white with a near-black section (`rgb(9, 9, 11)`) used as a high-contrast dark block for key messaging. The design avoids the neon/dark palette common in AI tools, opting instead for confident typography at large scale and tight negative-letter-spacing as its primary expressive tool. The type-forward approach lets the technology speak before imagery does. Two font families serve distinct roles: Plus Jakarta Sans commands the headlines, Outfit carries the prose.

## 2. Color Palette & Roles

**Base**
- Background: `rgb(255, 255, 255)` — white
- Near-white: `rgb(250, 250, 250)` — card and panel tint
- Body text: `rgb(0, 0, 0)` — full black (unusual — no softening)
- Heading text: `rgb(9, 9, 11)` — near-black

**Dark section**
- `rgb(9, 9, 11)` — used as a full-bleed dark container, nearly indistinguishable from pure black

**Interactive** (browser defaults — no custom link colour set)
- Links default to `rgb(0, 0, 238)` — unoverridden browser blue (possibly intentional lo-fi choice)

**What's absent:** No brand colour, no accent colour, no gradients, no semantic palette. GeoSpy's colour story is monochromatic with one dark inversion zone.

## 3. Typography Rules

A two-family system where each font has a clearly defined register.

| Element | Font | Size | Weight | Tracking |
|---------|------|------|--------|----------|
| H1 | Plus Jakarta Sans | 60px | 600 | −1.8px |
| H2 | Plus Jakarta Sans | 48px | 600 | −1.92px |
| H4 | Plus Jakarta Sans | 30px | 600 | −1.2px |
| H5 | Plus Jakarta Sans | 24px | 600 | −0.72px |
| `<p>` body | Outfit | 22px | 500 | −0.44px |
| Input | Inter | 14px | 400 | Normal |

All headings are weight 600 — no ultra-bold extremes. The consistent negative tracking (scaling proportionally with font size) creates optical tightening that reads as premium. At 60px with −1.8px tracking, the H1 feels like print editorial rather than web. Body copy at 22px (Outfit, weight 500) is unusually large — content legibility is prioritised over information density.

No uppercase transforms. No condensed weights. Pure size and tracking hierarchy.

## 4. Component Stylings

**Cards/containers** — 12px, 20px, and 50px border radii suggest three tiers: small UI elements, content cards, and pill-shaped tags. The 50px pill is likely used for CTA buttons or highlight badges.

**Shadow** — a single subtle shadow: `rgba(0,0,0,.25) 0 1px 2px` — just enough to lift interactive elements from the page. Nothing more.

**Navigation** — transparent background, no border visible in data.

**Forms** — Inter for inputs at 14px, establishing a clear separation between editorial and functional text.

**Dark section** — the `rgb(9,9,11)` container is a full-bleed inversion. Text within it presumably inverts to white, creating a bold moment without any colour.

## 5. Layout Principles

Section padding is generous: 160px top, 15px sides — implying sections that breathe vertically but are tightly constrained horizontally (likely relying on a max-width inner container). Footer padding of 80px top with 80px gaps suggests deliberate whitespace-as-structure approach.

Framer's breakpoint system at 809.98/810 and 1199.98/1200 creates two primary responsive tiers: mobile (≤809px), tablet (810–1199px), desktop (≥1200px). Clean and standard.

## 6. Depth & Elevation

Elevation is nearly absent. One shadow value covers the entire site. The dark section achieves visual weight through background colour contrast rather than shadow. This creates a flat-but-intentional aesthetic — depth is structural (layout contrast) not decorative (shadow stacking).

## 7. Do's and Don'ts

**Do:**
- Use Plus Jakarta Sans at 600 weight for all headings — never light or bold
- Apply negative tracking that scales with size (~3% of font size)
- Use Outfit at 22px for feature/body paragraphs — the generous size is intentional
- Reserve the near-black `rgb(9,9,11)` fill for a single high-impact dark section
- Keep border radii at three specific sizes: 12px (cards), 20px (containers), 50px (pills)

**Don't:**
- Introduce brand accent colours — the monochrome palette is a deliberate choice
- Override link colours — the unmodified browser blue may be intentional authenticity
- Add decorative shadows beyond the single `rgba(0,0,0,.25) 0 1px 2px`
- Use Inter for editorial content — it's reserved for form inputs only
- Mix heading weights within a section

## 8. Responsive Behavior

Three-tier Framer responsive system:
- **≤809px** — mobile: single column, typography scales down
- **810–1199px** — tablet: intermediate layout
- **≥1200px** — desktop: full multi-column layout

The 160px section top padding on desktop likely compresses to ~80px on mobile. The 22px body copy may scale to 18px at smaller breakpoints. The large heading sizes (60px H1) suggest a display-first design that relies on breakpoint scaling.

## 9. Agent Prompt Guide

> Recreate the geospy.ai aesthetic in Framer or React. White background, pure black text. Use **Plus Jakarta Sans** at 600 weight for all headings: H1 at 60px / −1.8px tracking, H2 at 48px / −1.92px tracking, scaling down proportionally. Use **Outfit** at 22px, weight 500, −0.44px tracking for all body copy. No accent colour — the only colour injection is a full-bleed `rgb(9,9,11)` dark section. Apply a single box-shadow globally for interactive elements: `rgba(0,0,0,.25) 0 1px 2px`. Sections get 160px vertical padding on desktop. Border radii: 12px for cards, 20px for feature containers, 50px for pill buttons.

*Generated by Sparkbites — extracted from live CSS analysis*
