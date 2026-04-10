# Basedash — Design System Reference

## 1. Visual Theme & Atmosphere

Basedash is pure dark-mode minimalism — the kind of design that feels like a live database running at midnight. The canvas is true black, the text is white, and the interaction between them is managed with careful opacity modulation rather than tonal steps. The header uses a frosted-glass technique (`oklab` color space for backdrop), and buttons idle at 50% opacity until hovered — teaching users to interact by revealing what was hidden. The aesthetic is data-tool precision: no decoration, no imagery, only structure and hierarchy through transparency and weight.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(0,0,0)` / `--color-background-1: rgba(0,0,0,1)` — page background (absolute black)
- `rgb(22,22,22)` — elevated surface (dark cards, `luminance: 0.086`)
- `oklab(0 0 0 / 0.85)` — header backdrop (frosted black with translucency)

**Text**
- `rgb(255,255,255)` — primary text
- `rgba(255,255,255,0.7)` — secondary nav text, button default
- `rgba(255,255,255,0.5)` — tertiary / placeholder-level text

**Interactive (opacity-based signaling)**
- Button default: `rgba(255,255,255,0.5)` border + text
- Button hover: `rgb(255,255,255)` — full opacity reveal
- No background fill on buttons — border-only interaction model

**Borders**
- `rgba(255,255,255,0.1)` — header border (barely-there)

The palette has exactly two hues: pure black and pure white. All variation happens through alpha channels.

---

## 3. Typography Rules

Basedash uses system **Inter** with a full fallback stack (`ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto...`). This is a pragmatic choice for a data product — fast loading, system-native rendering, no custom font latency.

**Scale**
| Role | Size | Weight | Leading |
|------|------|--------|---------|
| H1 | 48px | 400 | 48px (1:1) |
| Body / metadata | 14px | 400 | 20px |

- H1 at weight 400 (regular) is unusual and deliberate — it creates a quiet, anti-hype headline that lets the product screenshot carry the visual weight
- 1:1 line-height on H1 maintains the compressed display rhythm
- No letter-spacing customization — Inter runs at default tracking

**What's absent:** No bold display type, no custom font, no letter-spacing. The typographic restraint is a philosophical statement about the product.

---

## 4. Component Stylings

**Buttons (outline/ghost)**
- Default: transparent bg, `rgba(255,255,255,0.5)` border and text
- Hover: full white border and text — a clean, high-contrast reveal
- Focus: system default outline (`rgb(0,95,204)`) — browser-native accessible focus
- The half-opacity default makes buttons feel secondary until touched

**Header**
- `oklab(0 0 0 / 0.85)` backdrop — CSS `oklab` color space usage signals a modern codebase
- `rgba(255,255,255,0.1)` border — nearly invisible bottom edge

**Surface cards**
- `rgb(22,22,22)` — just above absolute black, creates a layered dark surface

**Border radius**
- `--radius-lg: .75rem`, `--radius-xl: 1rem`, `--radius-2xl: 1.25rem` — a three-step radius scale, suggesting generous rounded corners on cards and modals

---

## 5. Layout Principles

Basedash is built on Astro v5 with Tailwind CSS — a content-oriented static site generator. No breakpoints are defined in custom properties (likely all Tailwind utility classes). The absolute-black page with elevated `rgb(22,22,22)` card surfaces creates a two-layer depth model. The frosted header is sticky and always present, anchoring navigation while the page scrolls under it.

---

## 6. Depth & Elevation

The elevation model is simple and effective:
- **Layer 0:** `rgb(0,0,0)` — page
- **Layer 1:** `rgb(22,22,22)` — card / content surface
- **Layer 2:** `oklab(0 0 0 / 0.85)` — header (transparent, above content)

No box-shadows are present. Depth is defined by lightness (in reverse — lighter = elevated in dark mode). The header's translucency adds a frosted-glass overlay effect, implying the highest layer.

---

## 7. Do's and Don'ts

**Do:**
- Use alpha channels as the primary state communication tool — opacity over color changes
- Apply `oklab()` or `rgba()` backdrop effects on sticky UI elements
- Keep H1 at `font-weight: 400` — bold headlines undermine the quiet confidence
- Use the three-step radius scale for cards and containers

**Don't:**
- Add any color — the palette is black + white with alpha only
- Use filled button backgrounds — transparent borders with opacity modulation is the pattern
- Override browser focus styles with custom implementations — the native `rgb(0,95,204)` focus is intentional
- Use lighter grays for body surfaces — `rgb(22,22,22)` is the ceiling

---

## 8. Responsive Behavior

No custom breakpoints in the extracted data — Tailwind handles all breakpoints via utility classes. The site was built on Astro, suggesting primarily static-rendered content with minimal client-side interaction. The header's frosted backdrop likely collapses to a mobile drawer; the button opacity model works equally well at all sizes.

---

## 9. Agent Prompt Guide

> Build a UI that matches Basedash's design language.

Absolute black background `rgb(0,0,0)`. Pure white text at full and partial opacity (`1.0`, `0.7`, `0.5`). H1 is 48px/regular weight with 1:1 line-height — no bold headlines. Buttons are transparent with `rgba(255,255,255,0.5)` border; they reveal to full white on hover. Cards use `rgb(22,22,22)` as the elevated surface. Sticky header uses `oklab(0 0 0 / 0.85)` translucency with a `rgba(255,255,255,0.1)` bottom border. Use radius tokens: `0.75rem`, `1rem`, `1.25rem` for rounded containers. No shadows, no hue, no custom fonts.

---

*Generated by Sparkbites — extracted from live CSS analysis*
