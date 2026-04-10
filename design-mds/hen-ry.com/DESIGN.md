# hen-ry.com — Design System

## 1. Visual Theme & Atmosphere

Hen-ry.com is a creative portfolio that wraps its work in deep, almost nocturnal darkness. The base canvas is a near-black deep purple (`rgb(11, 1, 29)`) — not neutral black, but something warmer and more saturated, like the bottom of a wine glass. This single choice sets the entire emotional register: intimate, crafted, and slightly mysterious.

Against that dark foundation, the site uses lavender-tinged whites and soft purples as accent and interactive colours, creating a sense of soft luminescence rather than harsh contrast. The result feels more like a gallery at night than a portfolio on a screen. GSAP-powered animations and a custom cursor (`div.cursor` in `rgb(181, 171, 203)`) reinforce the sense of a space that breathes and responds.

Whitespace is used generously — sections have significant bottom margins (`69px`) without rigid padding, letting content float. The overall effect is curated quietness.

## 2. Color Palette & Roles

**Background / Canvas**
- `rgb(11, 1, 29)` — Primary canvas, deep purple-black; used on `body` and `div.hero-overlay`

**Surfaces**
- `rgba(255, 255, 255, 0.03)` — Nav background; barely-there frosted layer
- `rgba(255, 255, 255, 0.04–0.05)` — Card and pill surfaces; ghostly, barely visible
- `rgb(235, 227, 255)` — Success state surface; soft lavender
- `rgb(181, 171, 203)` — Custom cursor and textarea background; muted mauve

**Text**
- `rgb(210, 218, 228)` — H2 headings; cool blue-white for secondary hierarchy
- `rgb(51, 51, 51)` — Used across body/labels — notably dark, rendering nearly invisible against the dark background (intentional CSS override likely at component level)

**Accent / Feedback**
- `rgb(208, 156, 252)` — Error message background; soft purple
- `rgb(45, 38, 65)` — Nav border; a slightly lighter purple-grey separator

**Absent:** No green CTAs, no brand-primary red or blue. The palette deliberately avoids conventional accent colours.

## 3. Typography Rules

The entire site runs on **Inter V** — a variable-font version of Inter. This choice signals precision: variable axes allow per-element optical tuning without loading multiple weight files.

**Scale**
- H1: 88px / 500 weight / −1.76px tracking — bold, tightly tracked hero type
- H2: 36px / 400 weight / −0.36px tracking — relaxed but controlled
- H3: 48px / 500 weight / −0.48px tracking
- H5: 32px / 500 weight / −0.32px tracking
- Body: 16px / 400 / 1.6 line-height
- Paragraphs: 14px / 300 weight / 32px line-height — deliberately light and airy

**Feature settings:** H2 and paragraphs explicitly disable contextual alternates (`calt 0`) and ligatures (`liga 0`), preferring `cv06` — a deliberate OpenType choice for character legibility at small sizes.

**Notable absence:** No serif, no monospace, no display typeface. Pure typographic restraint.

## 4. Component Stylings

**Navigation:** Near-invisible background (`rgba(255,255,255,0.03)`), bordered in muted purple (`rgb(45, 38, 65)`). Low-profile by design — doesn't compete with content.

**Custom Cursor:** A `div.cursor` element in muted mauve (`rgb(181, 171, 203)`). A signature touch marking this as a crafted experience.

**Pills / Badges:** `div.hero-pill` at `rgba(255,255,255,0.05)` — ghost chips that whisper rather than shout. Rounded to `999px`.

**Popups:** Light surface (`rgb(245, 245, 247)`) against the dark background — strong enough contrast to feel modal.

**Forms:** Textarea in muted lavender (`rgb(181, 171, 203)`) with semi-transparent border. Inputs are bold-weighted (`700`), labels also bold — form fields feel intentional.

**Shadows:** Inset purple glow (`rgba(168, 128, 255, 0.1) 0px 0px 4px 2px inset`) on key elements — the signature depth effect.

**Border radii:** Generous variety — 8px, 10px, 14px, 24px, 32px up to full `999px` pills. Cards use 20–32px; small elements use 8–12px.

## 5. Layout Principles

Built in **Webflow**, the layout relies on section-level spacing with horizontal margins (`0px 10px 69px` on sections). The grid is single-column-dominant at the section level, with horizontal wrapping inside.

Content blocks float with generous vertical rhythm. The lack of a rigid column grid is intentional — this is a portfolio, not a SaaS dashboard. Each section is treated as a composed piece.

**Breakpoints:** 479/480px (mobile), 600px (mid), 767/768px (tablet), 991/992px (desktop).

## 6. Depth & Elevation

Depth is handled through three techniques:

1. **Alpha-based layering:** Surfaces use `rgba(255,255,255,0.03–0.05)` — nearly invisible but distinct from the base black.
2. **Inset purple glow:** `rgba(168, 128, 255, 0.1) 0px 0px 4px 2px inset` — soft ambient light from within.
3. **Drop shadows:** `rgba(20, 20, 43, 0.06–0.08) 0px 2px 12px 0px` — subtle dark-tinted drop shadows that suggest physical lift.
4. **Hero overlay:** `rgba(11, 1, 29, 0.8)` — darkens hero background media to unify contrast.

There is no hard border-based elevation. Depth is felt, not drawn.

## 7. Do's and Don'ts

**Do:**
- Use deep purple-black as the base. Never substitute with neutral black or dark grey.
- Apply Inter V with negative letter-spacing on headings.
- Use translucent white surfaces (`rgba(255,255,255,0.03–0.05)`) for card backgrounds.
- Add the inset purple glow for interactive or highlighted components.
- Use full-pill `999px` radius for badges and tags.
- Honour generous vertical spacing — don't compress sections.

**Don't:**
- Use browser-default link blue (`rgb(0,0,238)`) — it's detected but is a default fallback, not intentional.
- Add bright primary colours (red, green, yellow). The palette is intentionally muted.
- Use system-ui or any typeface other than Inter V.
- Add hard box borders in white or light grey — use alpha-blended edges instead.
- Skip the cursor customisation — it's part of the experience.

## 8. Responsive Behavior

The site uses a Webflow-style breakpoint model with 6 stages: 479px, 600px, 768px, 992px. At mobile widths, the 10px horizontal section margin keeps content breathing. No evidence of drastic layout restructuring — the design is primarily vertical-flow and degrades gracefully.

Typography likely scales down at mobile but the variable font nature of Inter V means optical weight stays controlled. The popup and form components are designed to be full-width at narrow viewports.

## 9. Agent Prompt Guide

> Recreate the aesthetic of hen-ry.com: a dark-mode portfolio built on a near-black deep purple canvas (`#0B011D`). Use Inter V (variable font) throughout — 88px/500 for hero headings with −1.76px tracking, 36px/400 for secondary headings. Surfaces should be barely-there translucent white overlays (`rgba(255,255,255,0.03)`), not solid cards. Signature depth: inset purple glow (`rgba(168,128,255,0.1) 0 0 4px 2px inset`). Use muted lavender (`#B5ABCB`) for the custom cursor and interactive form elements. Border radii: 8–14px for small elements, 24–32px for cards, 999px for pills. No bright accent colours — keep the palette within the deep purple and cold white range. Generous vertical spacing; sections breathe.

---

*Generated by Sparkbites — extracted from live CSS analysis*
