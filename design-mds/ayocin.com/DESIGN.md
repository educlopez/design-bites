# Ayocin — Design System Reference

## 1. Visual Theme & Atmosphere

Ayocin has the warmth of handmade paper and the precision of a well-designed editorial product. The foundation is a warm parchment — not stark white, not beige, but a specific tone that reads as considered and organic. Against this base, a deep coffee-brown footer and dark warm body text create a monochromatic earth palette with genuine depth. The design avoids the coldness of pure black/white without drifting into nostalgia; it feels contemporary and artisanal simultaneously. Animated lamp gradient accents (warm yellow and coral) add ephemeral life without committing to a permanent accent color.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(252,246,236)` — page background (warm parchment)
- `rgb(239,233,223)` — cursor element, interactive surface (a step darker)
- `rgb(206,193,178)` — hero/full-screen section background (muted sand)
- `rgba(178,162,139,0.1)` — grid overlay at near-invisible opacity

**Text & structure**
- `rgb(0,0,0)` — body text on light bg (true black)
- `rgb(46,37,33)` — dark warm-brown: main content text, footer background, input text
- `rgb(252,246,236)` — reversed text on dark footer

**Interactive**
- `rgb(239,233,223)` — button background (parchment-lighter than base)
- `rgb(46,37,33)` — button border and text

**Accent (ephemeral only)**
- `rgba(255,231,143,0.4)` — warm yellow lamp gradient
- `rgba(255,125,94,0.4)` — coral lamp gradient

The accent colors are translucent overlays used for atmospheric effect. They are never used as button fills, borders, or text colors — the system is defined by earth tones, not these warm glows.

---

## 3. Typography Rules

Ayocin uses a custom typeface — **Systemia** — with Roboto as fallback. Systemia is a geometric display font with personality, contrasting with the typically neutral choices of SaaS products. The use of a custom font is the primary design differentiator; it makes the brand feel proprietary and craft-oriented.

**Scale**
| Role | Size | Weight | Leading |
|------|------|--------|---------|
| H2 (primary heading) | 60px | 500 | 60px (1:1) |
| Input | 12px | 400 | 15.6px |

- Medium weight (500) at 60px for headings — not bold, which keeps the display text elegant
- 1:1 line-height on headings matches the premium compression seen across top-tier product sites
- No letter-spacing adjustment — Systemia is used at its native rhythm
- No OpenType feature settings — the font's character is in its forms, not glyph variants

**What's absent:** No serif counterpoint, no monospace. Systemia carries the entire typographic identity.

---

## 4. Component Stylings

**Buttons**
- Rounded (`border-radius: 20px`, `100%` pill also present)
- Fill: `rgb(239,233,223)` — slightly lighter than the page bg, not white
- Border + text: `rgb(46,37,33)` — dark warm brown
- Effect: the button appears to be cut from the same material as the page, just a lighter slice

**Cursor**
- Custom cursor element at `rgb(239,233,223)` — tracked via `--cursor-x` / `--cursor-y` CSS variables
- Interactive cursor feedback reinforces the tactile, craft-forward personality

**Input fields**
- Transparent background, dark warm-brown border and text
- At 12px/400 weight — small and unobtrusive, suggesting minimal form usage

---

## 5. Layout Principles

Ayocin uses a 6-column-implied grid with breakpoints at 420, 768, 1023/1024, 1280, and 1440px. The 420px mobile breakpoint is unusually specific (smaller than standard 375/390 phones), suggesting deliberate micro-layout care. Full-screen sections (`div.h-screen`) establish vertical rhythm. The footer inverts the color scheme — dark background, light text — functioning as a visual counterweight to the parchment page.

---

## 6. Depth & Elevation

No box-shadows exist in the system. Depth is created through:
- Background color steps (parchment → sand → dark brown)
- The grid overlay (`rgba(178,162,139,0.1)`) — a barely-visible texture layer
- Translucent lamp gradient overlays that float above content

This is an atmospheric depth model, not a material one. There are no cards, no modal shadows, no raised elements. Everything sits in the same plane with color alone creating z-axis sensation.

---

## 7. Do's and Don'ts

**Do:**
- Use Systemia at medium weight (500) for all display text
- Maintain the warm parchment hierarchy: `rgb(252,246,236)` → `rgb(239,233,223)` → `rgb(206,193,178)` → `rgb(46,37,33)`
- Apply lamp gradients at `0.4` opacity maximum — atmospheric only, never structural
- Use pill/rounded borders (`20px` or `100%`) for interactive elements

**Don't:**
- Introduce any cool-toned color (blue, purple, green) — the entire palette is warm earth
- Use the coral/yellow accent colors as solid fills — they exist only as translucent overlays
- Apply box-shadows — depth is tonal, not shadow-based
- Substitute Roboto for Systemia at display sizes — fallback only applies for loading/system rendering

---

## 8. Responsive Behavior

Breakpoints span 420–1440px with twin entries at 1023/1024 (likely `max-width` / `min-width` pair). The custom cursor is a CSS-variable-driven element that may be hidden at mobile sizes. Tailwind CSS handles utility responsiveness. The overall layout likely shifts from multi-column to stacked at 768px, with the 420px breakpoint handling sub-mobile edge cases.

---

## 9. Agent Prompt Guide

> Build a UI that matches Ayocin's design language.

Page background is warm parchment `rgb(252,246,236)`. Text is deep warm-brown `rgb(46,37,33)`. Use Systemia (or an organic geometric font) at 60px/500 weight for headings, with a 1:1 line-height. Buttons are pill-shaped, filled with `rgb(239,233,223)`, bordered in `rgb(46,37,33)`. No shadows — depth comes from background-color steps. Optional: add translucent warm-yellow or coral radial gradients at 0.4 opacity as atmospheric overlays. Footer inverts to dark warm-brown background with parchment text. The entire palette is warm earth tones — no cool grays, no blues.

---

*Generated by Sparkbites — extracted from live CSS analysis*
