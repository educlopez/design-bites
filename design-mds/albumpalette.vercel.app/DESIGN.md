# albumpalette.vercel.app — Design System

## 1. Visual Theme & Atmosphere

Album Palette is a music-reactive color extractor that makes its design philosophy literal: the UI adapts to match the album art it's analyzing. The base canvas is pure black — a void that makes extracted colors pop. Everything is ephemeral and cinematic. The "design system" here is partly procedural: the `--border-color` and `--image` CSS custom properties change at runtime based on the selected album, meaning the design is always one palette extraction away from transformation. This is not a static brand — it's a canvas that wears different albums.

## 2. Color Palette & Roles

**Base (invariant)**
- Background: `rgb(0,0,0)` — absolute black, the fixed ground
- Text: `rgb(255,255,255)` on dark areas, `rgb(0,0,0)` on light title logo
- Button resting text: `rgba(255,255,255,0.5)` — half-visible ghost labels

**Dynamic (album-reactive)**
- `--border-color: #e8252c` (default: a vivid cherry red from the demo album art)
- `--image`: the Spotify album cover URL — used as a CSS background-image

**Extracted palette demo (from default album)**
- Dominant: `rgb(232,37,44)` — vivid red (selected/active swatch)
- Light: `rgb(242,135,138)` — coral pink
- Mid-dark: `rgb(138,14,19)` — deep crimson
- Dark: `rgb(113,17,21)` — near-black red
- Deep: `rgb(36,20,20)` — almost-black

**Structural**
- Swatch borders on hover: `--border-color` reactive ring
- Title link: `rgb(0,0,0)` — the logo sits on a white-ish background context

## 3. Typography Rules

Album Palette uses the system sans-serif stack exclusively — no custom fonts loaded, which keeps the experience snappy and the focus entirely on the visual color extraction. The typographic hierarchy is intentionally minimal.

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| body | system sans-serif | 16px | 400 | 24px line-height |
| p | system sans-serif | 16px | 400 | Matches body |
| a (title) | system sans-serif | 36px | 600 | 40px line-height — the logo link |
| button | system sans-serif | 14px | 400 | Light, unassuming |
| input | system sans-serif | 16px | 400 | Search/entry field |

The 36px/600 anchor tag is the page title — "albumpalette" styled as a large bold link. Everything else defers to body text scale. There are no heading elements (h1–h6) defined in the typography data — this is a single-screen app, not a document. The absence of heading hierarchy is intentional: all visual hierarchy comes from color, not text size.

## 4. Component Stylings

**Color swatch tiles**
- Square divs: `w-8` = 32px squares rendered in extracted palette colors
- Active/selected: `ring-2` with `--border-color` reactive border — the selection ring updates to match the dominant color
- Shadow: `rgba(0,0,0,0.1) 0px 20px 25px -5px, rgba(0,0,0,0.1) 0px 8px 10px -6px` — Tailwind `shadow-xl`
- Border radius: `12px` on cards, `9999px` (full pill) on other elements

**Artist/album suggestion buttons**
- Background: `rgba(255,255,255,0.05)` — ghost white, barely visible on black
- Text: `rgba(255,255,255,0.5)` — half-opacity white label
- No hover state defined — focus only (browser default)
- The effect is intentional obscurity: these are hints, not calls to action

**Background fixed panel**
- `div.fixed`: `rgb(0,0,0)` — the persistent black base layer

**Input field**
- Background: transparent on black — the input is essentially invisible until typed in
- Text: white when active

**Title treatment**
- `div.before_conic_title`: `rgba(255,255,255,0.1)` — a subtle conic/radial glow behind the title, the only decorative background element

## 5. Layout Principles

The layout data is sparse by design — this is a single-screen micro-app with minimal structural complexity. No max-width containers, no grid columns, no complex section stacking. The design is centered on a single interaction: type an artist → see the palette. Everything arranges around that vertical flow.

Breakpoints: 640px, 768px, 1024px, 1280px, 1536px — the full Tailwind default breakpoint set. This breadth suggests a responsive grid for the color swatch display that reflows across screen sizes.

## 6. Depth & Elevation

The black background creates inherent depth — anything colored floats above the void. The color swatches use `shadow-xl` to give physical weight to what are essentially data objects. The `rgba(255,255,255,0.1)` title panel glow is the only atmospheric effect. There are no cards, panels, or surface layers — the design trusts negative space and color contrast for all spatial organization.

## 7. Do's and Don'ts

**Do**
- Use pure `rgb(0,0,0)` as the immovable background
- Let the extracted palette provide all color — the UI chrome stays neutral
- Use `rgba(255,255,255,0.05)` for ghost surfaces that need to exist but not compete
- Apply `shadow-xl` to color swatches to give them physical presence
- Use `9999px` border radius for pill shapes on small interactive elements

**Don't**
- Define a static accent color — the design's accent is always dynamically sourced
- Add text hierarchy with headings — this is a tool, not a document
- Use hover states on suggestion buttons — restraint communicates that they're secondary
- Load custom fonts — system sans keeps the focus on the extracted colors, not typography
- Add white backgrounds or light surfaces — the void is the design

## 8. Responsive Behavior

The full Tailwind breakpoint ladder (640–1536px) suggests the color palette grid adapts from a single column on mobile to a multi-column display on desktop. The fixed black background scales independently of content. Input and suggestion buttons likely center-stack on mobile. At 640px, the swatch grid probably collapses from 4–5 columns to 2–3.

## 9. Agent Prompt Guide

> Design a music color-extraction micro-app in the style of albumpalette.vercel.app: pure black (`rgb(0,0,0)`) background, white ghost UI elements at 5–50% opacity. No custom typeface — system sans only, 16px body, 36px/600 title link. Color swatches are 32px squares with `shadow-xl` and a reactive border ring using the dominant extracted color. Suggestion buttons are `rgba(255,255,255,0.05)` background with half-opacity text — intentionally ghostlike. Transparent input on black. A subtle `rgba(255,255,255,0.1)` conic glow behind the title. Full Tailwind breakpoint set for responsive swatch grid. The palette changes everything — the UI changes nothing.

---

*Generated by Sparkbites — extracted from live CSS analysis*
