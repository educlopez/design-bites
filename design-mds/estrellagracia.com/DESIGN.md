# Estrella Gracia — Design System Reference

## 1. Visual Theme & Atmosphere

Estrella Gracia's portfolio is a Valencia-based designer's calling card built in Framer, and it leans on typography and a single electric blue to carry the brand. The canvas is a soft off-white (`rgb(248, 248, 248)`) with pure black text, and headings switch to Sentient, a contemporary serif, set small (18px) with tight negative tracking so it reads as a refined editorial voice rather than a shouty display face. Body and UI copy sit in Inter and Stack Sans Text, a clean grotesk pairing that keeps the serif special. One saturated azure (`rgb(0, 128, 255)`) is the signature, used on the "Let's talk!" call to action and on social handles, while a deep navy (`rgb(14, 26, 62)`) appears as a dark counter-surface. The site also shows small personal touches (local city, a playful "probably sunny" line and a live clock), which keeps the tone warm and human.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(248, 248, 248)` — page canvas (soft off-white)
- `rgb(0, 0, 0)` — primary text
- `rgb(95, 95, 95)` — secondary heading gray (h3)

**Brand accent**
- `rgb(0, 128, 255)` — azure; primary CTA background and inline handle links
- `rgb(220, 237, 255)` — pale blue; CTA hover background

**Deep surface**
- `rgb(14, 26, 62)` — midnight navy block, the darkest surface (luminance 0.104)

**Surfaces & glass**
- `rgba(255, 255, 255, 0.8)` — translucent white layer (frosted overlay)
- `rgba(165, 165, 165, 0.15)` — faint gray wash for subtle panels
- `rgb(146, 146, 146)` — mid gray surface

The system is a neutral frame with exactly one chromatic voice. Blue is an action color, not decoration.

---

## 3. Typography Rules

Three families, each with a clear job.

- **Sentient** (serif fallback) — headings; 18px, weight 400, line-height 21.6px, letter-spacing -0.72px
- **Inter** — paragraphs; 16px, weight 500, line-height 19.2px
- **Stack Sans Text** — links; 15px, weight 400, line-height 21px, letter-spacing -0.45px
- **Inter Medium** — buttons; 16px, weight 500, letter-spacing -0.2px

| Role   | Font            | Size | Weight | Line-height | Tracking |
|--------|-----------------|------|--------|-------------|----------|
| H3     | Sentient        | 18px | 400    | 21.6px      | -0.72px  |
| P      | Inter           | 16px | 500    | 19.2px      | normal   |
| Link   | Stack Sans Text | 15px | 400    | 21px        | -0.45px  |
| Button | Inter Medium    | 16px | 500    | normal      | -0.2px   |

**Principles**
- Negative tracking everywhere (-0.2px to -0.72px): the type is pulled tight, which gives a confident, designed feel at small sizes.
- Headings are small. Hierarchy comes from the serif switch and gray tone (`rgb(95, 95, 95)`), not from scale.
- Body text uses weight 500 rather than 400, so even paragraphs have presence on the light canvas.

---

## 4. Component Stylings

**Primary CTA ("Let's talk!")**
- Background `rgb(0, 128, 255)`; hover swaps to `rgb(220, 237, 255)` pale blue
- Pill-shaped (`100px` radius present in the system)
- No box-shadow, no transform on hover; the color swap is the whole interaction

**Text links (Work, @handles)**
- Transparent background; handles use `rgb(0, 128, 255)`
- Focus shows a 1px auto outline; no hover change was captured

**Copy-to-clipboard email**
- The email address is a "Copy component" with a "Copied" confirmation state, a small utility micro-interaction.

**Border radius**
- `100px`, `16px`, `10px`, `4px` — a four-step scale from pill to near-square.

**Shadows**
- None detected.

---

## 5. Layout Principles

- Framer-generated layout with breakpoints at **809 / 1199 / 1439 / 1600**, so the page reflows at tablet, laptop and wide-desktop widths.
- Body margin and padding are 0; spacing is handled inside Framer frames.
- Content is sparse: contact details, location, a live time readout and social links (LinkedIn, Instagram, Behance, YouTube) sit as a compact column rather than a full navigation system.
- Large dark navy blocks (`rgb(14, 26, 62)`) break up the light page and give sections weight.

---

## 6. Depth & Elevation

Depth is built from surface color and translucency, not shadow.
- Off-white canvas `rgb(248, 248, 248)` (luminance 0.973) under frosted white `rgba(255, 255, 255, 0.8)` overlays.
- A faint gray wash (`rgba(165, 165, 165, 0.15)`) for secondary panels.
- The navy block (`rgb(14, 26, 62)`) is the single high-contrast depth cue.
- Framer Motion handles animated transitions between states.

---

## 7. Do's and Don'ts

**Do**
- Keep the canvas soft off-white `rgb(248, 248, 248)`, never pure white.
- Use azure `rgb(0, 128, 255)` only for actions and handles.
- Set headings in a serif (Sentient) and everything else in a clean grotesk.
- Apply negative letter-spacing to small text.
- Swap to pale blue `rgb(220, 237, 255)` for hover.

**Don't**
- Don't add drop shadows; use surface and translucency.
- Don't scale headings up to create hierarchy; this system keeps them small.
- Don't introduce a second saturated color beside the azure.
- Don't leave links in the browser default blue (`rgb(0, 0, 238)`); that value only appears as an unstyled fallback in the extraction.

---

## 8. Responsive Behavior

Breakpoints at **809, 1199, 1439 and 1600px** (Framer's standard set). Type sizes are small and fixed, so they carry across breakpoints without needing fluid scaling; layout changes happen in the Framer frames. The pill radius and compact CTA remain usable at touch size.

---

## 9. Agent Prompt Guide

> Build a UI that matches Estrella Gracia's design language.

Use a soft off-white canvas `rgb(248, 248, 248)` with black text. Set headings in **Sentient** (serif) at ~18px, weight 400, letter-spacing -0.72px, in gray `rgb(95, 95, 95)`. Set paragraphs in **Inter** 16px weight 500, links in **Stack Sans Text** 15px with -0.45px tracking, and buttons in Inter Medium 16px. The only accent is azure `rgb(0, 128, 255)`: a pill-shaped (`100px`) CTA that turns pale blue `rgb(220, 237, 255)` on hover, plus blue inline handles. Use a midnight navy block `rgb(14, 26, 62)` for one dark section. No shadows; use translucent white `rgba(255, 255, 255, 0.8)` overlays for depth. Keep personal touches: location, a live clock, and a click-to-copy email.

---

*Generated by Sparkbites — extracted from live CSS analysis*
