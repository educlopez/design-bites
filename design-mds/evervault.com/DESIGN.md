# evervault.com — Design Language

## 1. Visual Theme & Atmosphere

Evervault.com is a security infrastructure company, and its design language encodes that identity at every level. The canvas is near-black (`rgb(1, 3, 20)`) — almost void — suggesting an environment where invisible things happen. Text appears in cool lavender-white tones rather than pure white, giving content a slightly otherworldly, encrypted quality. The accent color is a rich violet (`rgb(102, 51, 238)`) that glows against the dark background, evoking encrypted data streams and cryptographic operations.

This is a dark-mode-first design (the only mode offered) executed with unusual care. The depth system is layered — backgrounds, cards, and nav elements each sit at a distinct luminance level, creating spatial hierarchy through darkness. The type is Roobert for display — a confident geometric sans — paired with Inter for UI text.

The overall atmosphere is: "serious infrastructure for serious engineers, presented beautifully."

## 2. Color Palette & Roles

**Background Layers (darkest to lightest)**
- `rgb(1, 3, 20)` — Page body; near-void dark navy, the deepest layer
- `rgb(42, 43, 58)` — Card surfaces; a dark slate, clearly elevated above background
- `rgb(56, 58, 77)` — Nav buttons, interactive surfaces; one step brighter

**Text**
- `rgb(223, 225, 244)` — Primary text; lavender-white, the signature tone of this palette. Not pure white — the blue cast connects it to the violet accent.
- `rgb(186, 188, 210)` — Link / secondary text; slightly more muted lavender
- `rgb(236, 236, 251)` — Code text; near-white with violet undertone, elevated luminance
- `rgb(94, 96, 119)` — Label / tertiary text; grey-violet, the dimmest text layer
- `#FFFFFF` — Pure white for button labels and maximum-contrast moments

**Brand / Accent**
- `rgb(102, 51, 238)` — Violet; the brand color. Used at 50% opacity as icon backgrounds and at full saturation for border-glow effects on cards.
- `rgba(190, 167, 255, 0.24)` — Soft lavender inset ring on cards; glow effect that suggests illumination from within.

**Absent:** No green "success" color, no red "danger" color visible in the surface layer. Security-focused restraint — no traffic-light signaling.

## 3. Typography Rules

Two typefaces serve distinct roles:

**Roobert** — Display and all heading levels (h1–h4). A geometric sans with warm, approachable character that softens the technical darkness of the palette. Notably, Roobert has `"kern", "liga", "salt"` font features enabled — the "salt" stylistic alternates feature is unusual and suggests specific letterform choices are being applied. Tight negative tracking on H1 (-0.84px at 56px) creates dense, impactful display.

**Inter** — Body text, h5, and all UI elements. The utilitarian complement to Roobert's display personality.

**Scale**
| Role | Font | Size | Weight | Tracking |
|------|------|------|--------|---------|
| H1 | Roobert | 56px | 600 | -0.84px |
| H2 | Roobert | 32px | 500 | -0.32px |
| H3 | Roobert | 24px | 500 | normal |
| H4 | Roobert | 17.6px | 500 | normal |
| H5 | Inter | 14.4px | 500 | normal |
| Body | Inter | 16px | 400 | normal |

The progression from 600 (H1) to 500 (H2–H4) to 400 (body) creates a smooth weight descent. H1 tracking tightens dramatically with scale — standard editorial practice for large display type.

## 4. Component Stylings

**Cards**
`rgb(42, 43, 58)` background with inset glow: `rgba(190, 167, 255, 0.24) 0px 0px 0px 1.5px inset`. This inner-ring glow is the defining card treatment — it reads as the card being lit from within, consistent with the cryptographic/data-handling theme. Combined with layered drop shadows (`rgba(0, 0, 0, 0.25) 0px 8px 16px -4px`), cards feel like illuminated panels floating in darkness.

**Nav Buttons**
`rgb(56, 58, 77)` fill with `rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset` — a white top-edge shine that catches light. Combined with multiple box-shadow layers for depth.

**Icon Backgrounds**
`rgba(102, 51, 238, 0.5)` with `rgb(102, 51, 238)` border — glowing violet icon containers. The translucency lets background card color show through while maintaining brand presence.

**Buttons**
Transparent background with white text and white border. Ghost buttons on dark backgrounds.

## 5. Layout Principles

Sections use `128px 0px 160px` padding — tall, spacious vertical rhythm. Header uses `51.2px` horizontal padding. The generous spacing at section level creates a cinematic, unhurried reading pace appropriate to a complex technical product.

Breakpoints: 1199 / 1200 — a binary responsive system. The design appears to have two states: mobile/tablet (under 1200px) and desktop (1200px+). This suggests a simpler responsive model than multi-breakpoint competitors.

## 6. Depth & Elevation

Three-tier elevation via background luminance:
1. Background: `rgb(1, 3, 20)` — luminance ~0.003
2. Cards: `rgb(42, 43, 58)` — luminance ~0.099
3. Nav buttons: `rgb(56, 58, 77)` — slightly higher

Each tier is reinforced with shadows:
- **Base shadow**: `rgba(0, 0, 0, 0.25) 0px 8px 16px -4px, rgba(0, 0, 0, 0.25) 0px 4px 8px -2px`
- **Inner light**: `rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset` — simulates a top-edge light source
- **Inner depth**: `rgba(0, 0, 0, 0.12) 0px -1px 24px 0px inset` — bottom-edge darkening
- **Glow ring**: `rgba(190, 167, 255, 0.24) 0px 0px 0px 1.5px inset` — violet inner border

This multi-layer shadow approach is sophisticated: each shadow layer serves a distinct perceptual role (elevation, light source, depth, brand glow).

## 7. Do's and Don'ts

**Do**
- Use `rgb(1, 3, 20)` as the baseline; never substitute a softer dark (charcoal, grey-black)
- Apply the lavender-white (`rgb(223, 225, 244)`) for primary text — never pure white for body
- Use Roobert with `"kern", "liga", "salt"` features enabled for headings
- Apply the violet glow ring (`rgba(190, 167, 255, 0.24)`) to card inner borders
- Combine multiple shadow layers: outer drop + inner light + inner depth

**Don't**
- Use bright, saturated secondary colors — this palette is intentionally monochromatic except violet
- Set H1 line-height above 1.0 at 56px; the 1:1 ratio is essential for display density
- Switch to light mode or introduce light-mode surfaces
- Use plain 1px borders without the glow effect — borders here always carry luminance
- Flatten the shadow system to a single box-shadow; the layering is the effect

## 8. Responsive Behavior

Binary responsive breakpoint at 1200px. Below 1200px, section padding likely compresses and single-column layouts activate. The 51.2px header padding may reduce to a mobile-friendly gutter.

No type scaling detected across breakpoints — Roobert at 56px may remain fixed or use a separate mobile scale not captured here. Consider a mobile H1 of ~36–40px for comfortable reading.

## 9. Agent Prompt Guide

> Build a UI in the style of evervault.com: near-void dark navy background (`rgb(1, 3, 20)`), lavender-white primary text (`rgb(223, 225, 244)`). Use Roobert for all headings with `"kern", "liga", "salt"` features, -0.84px tracking at large sizes. Body text is Inter at 16px. Cards are `rgb(42, 43, 58)` with a violet inner glow ring (`rgba(190, 167, 255, 0.24) 0px 0px 0px 1.5px inset`) and layered drop shadows. Accent color is `rgb(102, 51, 238)` for icon containers and border glow. Sections have 128px top / 160px bottom padding. This is dark-mode-only — no light mode surfaces. The aesthetic is encrypted, spatial, and precise.

---

*Generated by Sparkbites — extracted from live CSS analysis*
