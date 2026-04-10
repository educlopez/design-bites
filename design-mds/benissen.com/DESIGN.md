# Benissen — Design System Reference

## 1. Visual Theme & Atmosphere

Benissen is a Framer-built portfolio or product site that uses darkness as its canvas and deploys color with pop-art boldness. The base is a dark charcoal — not pure black, a warm near-black — and against it, a curated set of vivid accent colors performs: electric orange, coral red, soft purple. The design reads as energetic and direct, the kind of interface that has opinions and is not afraid to show them. It is contemporary creative-tool territory: dark mode by conviction, color by deliberate punch, system fonts by pragmatism.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(28,28,28)` — page background (warm dark charcoal)
- `rgb(38,38,38)` — input surface (one step lighter)
- `rgb(46,46,46)` — link background (mid-dark)

**Text**
- `rgb(255,255,255)` — h1, primary headings
- `rgb(224,224,224)` — h3, secondary headings (softened white)
- `rgb(0,0,0)` — text on colored button surfaces (for legibility)

**Accent colors (functional, not decorative)**
- `rgb(255,93,13)` — primary CTA button fill (vivid orange)
- `rgb(255,51,51)` — highlight / alert surface (coral red)
- `rgb(122,100,255)` — secondary action button (soft electric purple)

**Link color**
- `rgb(0,0,238)` — browser-default blue (unrestyled links — intentional raw web aesthetic or oversight)

**Neutral surface**
- `rgb(150,150,150)` — mid-gray content surface

The three-color accent system (orange, red, purple) operates as a vibrant triad against the dark base. Orange is primary/CTA, purple is secondary, red signals urgency or featured content.

---

## 3. Typography Rules

Benissen uses the system font stack: `system-ui, -apple-system, "Segoe UI", Roboto, Oxygen, Ubuntu...`. This is Framer's default — either a deliberate choice to let OS fonts handle the type, or a starting-point that was never customized. The result is a neutral, system-native type experience that puts zero friction between user and content.

**Scale**
| Role | Size | Weight | Tracking |
|------|------|--------|----------|
| H1 | 24px | — | — |
| H3 | 14px | — | -0.14px |
| Body | 14px | 400 | -0.14px |

- H1 at 24px is surprisingly restrained for a dark-mode creative site — suggests Benissen uses large visual elements (images, colorblocks) rather than type as the primary hero
- `-0.14px` tracking at 14px is minimal but present — a subtle tightening
- No custom weight variation captured — the system font stack handles weight natively

**What's absent:** No custom font, no display type, no significant letter-spacing. The visual drama comes from color and Framer animations, not typography.

---

## 4. Component Stylings

**Buttons — Orange CTA**
- Background: `rgb(255,93,13)` — vivid orange
- Text: `rgb(0,0,0)` — black for maximum legibility on bright fill
- No border (transparent border)

**Buttons — Purple action**
- Background: `rgb(122,100,255)` — soft electric purple
- Text: `rgb(0,0,0)`
- No border

**Buttons — Default ghost**
- Transparent background, black border + text
- This appears to be a light-mode-artifact in the Framer component layer

**Input fields**
- Background: `rgb(38,38,38)` — slightly lighter than page
- Text: white
- No visible border (`rgba(237,237,237,0)` — transparent)

**Framer-specific surfaces**
- `div.framer-1sncmsb`: `rgb(255,51,51)` — a red content block
- Framer Motion is in use — animations and transitions are Framer-driven

---

## 5. Layout Principles

Framer-generated layout with breakpoints at 399/400 (mobile), 799/809.98 (tablet pair), and 1199.98/1200 (desktop boundary). The paired breakpoints (e.g., 399/400, 1199.98/1200) are a Framer convention for `max-width` / `min-width` media queries that create clean, non-overlapping breakpoint zones. No explicit grid column system is defined in CSS custom properties — layout is managed entirely through Framer's canvas.

---

## 6. Depth & Elevation

No box-shadows in the extracted data. Framer handles motion and depth through its animation system rather than static CSS shadows. Elevation is communicated through:
- Background color steps: `28,28,28` → `38,38,38` → `46,46,46`
- Color-contrast: vivid accent buttons "pop" above the dark base through saturation, not shadow

---

## 7. Do's and Don'ts

**Do:**
- Use orange `rgb(255,93,13)` for primary CTAs, purple `rgb(122,100,255)` for secondary actions
- Keep button text black on all colored fills — contrast over style
- Use the charcoal staircase for surfaces: `28` (page) → `38` (input) → `46` (link bg)
- Let Framer Motion handle all transitions and micro-interactions

**Don't:**
- Restyle anchor tags to hide the default blue — it appears intentional here
- Mix colored fills on adjacent buttons — orange and purple should not appear in the same button row
- Add box-shadows — the depth model is purely color-contrast based
- Override the system font stack with a custom font unless the brand decision is explicit

---

## 8. Responsive Behavior

Framer breakpoints at 400/810/1200px. The paired `799/809.98` entries suggest Framer's auto-generated responsive breakpoint pairs rather than manual authoring. At mobile (below 400px), the layout likely switches to single-column. The vivid accent buttons should maintain their visual weight at all sizes — avoid reducing font-size or padding to the point where color blocks feel small.

---

## 9. Agent Prompt Guide

> Build a UI that matches Benissen's design language.

Warm charcoal background `rgb(28,28,28)`. System font stack at 14px body and 24px headings. Primary CTA button: `rgb(255,93,13)` fill, black text, no border, no radius (or minimal). Secondary action button: `rgb(122,100,255)`, same treatment. Featured/alert surfaces use `rgb(255,51,51)`. Inputs are `rgb(38,38,38)` with transparent borders and white text. All accent colors use black text for legibility. No box-shadows — depth comes from background-color stepping. Use Framer Motion (or equivalent) for all transitions. Breakpoints at 400, 810, 1200px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
