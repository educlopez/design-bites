# kuntz.io — Design System

## 1. Visual Theme & Atmosphere

Daniel Kuntz's site is a full dark-mode creative portfolio that pairs a custom display font with a clean grotesque workhorse. The design is cinematic and intentional — pure black surfaces, white type, and a custom cursor that implies motion and interactivity before the user has clicked anything. The easing curve (`cubic-bezier(0.65, 0, 0.35, 1)`) used throughout creates a weighted, decelerating motion that feels considered and physical. This is a site that treats animation as part of the design language, not an afterthought. The result is high-contrast, dark-studio energy with a tactile undercurrent.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|---|---|---|
| **Page Background** | `rgba(0,0,0,0)` / Black | Full dark — likely `#000` or near-black body |
| **Primary Text** | `rgb(255, 255, 255)` — White | All body text, headings, links |
| **Borders** | `rgb(255, 255, 255)` — White | Unified with text; monochromatic borders |
| **Header** | Transparent background, white text | Floats over content |
| **Custom Cursor** | `rgba(255, 255, 255, 0.25)` — 25% White | Soft frosted cursor circle overlay |

The palette is binary and extreme: pure black backgrounds, pure white type. No mid-tones, no accents, no brand color. The only tonal variation is the 25% white cursor overlay — a whisper of softness in an otherwise absolute system. This is a deliberate statement of confidence.

---

## 3. Typography Rules

| Element | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| `h1` | Dakota Outline | 26px | 400 | normal |
| `h2` | Innovator Grotesk | 20px | 400 | normal |
| `body` | Innovator Grotesk | 16px | 400 | normal |
| `a` (links) | Innovator Grotesk | 16px | 400 | normal |

Two fonts, two roles: Dakota Outline (a display/outline typeface) for the primary identity headline, and Innovator Grotesk (a custom sans-serif) for all supporting content. The outline style of Dakota creates negative space within the letterforms — letters you look through rather than at — which is a rare and confident typographic choice. Innovator Grotesk provides clarity and neutrality throughout the rest of the interface. No letter-spacing overrides, no text transforms — both fonts are used straight.

---

## 4. Component Stylings

**Links / Navigation**
- White text, transparent background
- 1px border radius (effectively none — hard-edged)
- Hover state extracts to `opacity: 0` → `1` transition — links fade in/out
- Custom cursor (`div.custom-cursor`) with 25% white fill follows the pointer

**Buttons / CTAs**
- Not explicitly extracted but implied to use Innovator Grotesk in white on dark
- Consistent with the link system

**Header**
- Transparent background — content-agnostic
- White text and borders
- No shadow, no backdrop blur detected

**Interactive States**
- Hover: opacity-based transitions (fade in/out)
- Focus: outline in white (`rgb(255,255,255) none 0px` — no visible focus ring detected, which may be an accessibility concern)
- Transform: none detected — no scale or lift effects

---

## 5. Layout Principles

- Body: zero padding, 40px bottom margin
- Single detected breakpoint: **768px** — the primary mobile/tablet threshold
- Spacing is minimal and component-level; no design token system
- The layout likely uses full-viewport sections (cinematic scroll) given the dark, immersive aesthetic
- Gap values not extracted — spacing managed per-component

---

## 6. Depth & Elevation

No shadows detected. Border radius: 4px on one element (likely a tag or badge) — everything else is hard-edged. Depth in this system is entirely theatrical: the dark background recedes, light content emerges. The custom cursor adds a single kinetic layer above the page surface. Motion (via the custom easing) creates temporal depth — things arrive and depart with weight.

---

## 7. Do's and Don'ts

**Do:**
- Use Dakota Outline exclusively for the primary display headline
- Keep Innovator Grotesk for all body and UI copy
- Maintain pure black/white — no accent colors, no greys
- Apply the custom cubic-bezier `(0.65, 0, 0.35, 1)` for all transitions
- Use opacity (fade) as the primary interaction signal
- Use a custom cursor to add personality without visual noise

**Don't:**
- Add colored accents or gradients — this system lives and dies in black and white
- Use rounded corners beyond 4px (and only sparingly)
- Add drop shadows — the darkness itself is the depth
- Mix in additional typefaces
- Use abrupt linear transitions — the weighted easing is core to the identity

---

## 8. Responsive Behavior

Single breakpoint at **768px**. Below this threshold the layout collapses to a single-column mobile view. The cinematic, full-bleed desktop experience likely simplifies to a vertical scroll with larger touch targets. The minimal component set (no complex navigation, no sidebar) makes the responsive transition straightforward. Dakota Outline at 26px remains legible at mobile scale without needing rescaling.

---

## 9. Agent Prompt Guide

**Quick color reference:**
- Background: `#000000` black
- Text & borders: `#ffffff` white
- Cursor overlay: `rgba(255,255,255,0.25)`

**Prompt to recreate this style:**
> "Design a dark creative portfolio page in the style of kuntz.io: pure black background, white text only, Dakota Outline display font for the hero heading, Innovator Grotesk for body, no accent colors, custom circular cursor at 25% white opacity, all transitions use cubic-bezier(0.65,0,0.35,1). Atmosphere: cinematic, dark studio, motion-aware."

**Prompt for a component:**
> "Create a project card: black background, white text in Innovator Grotesk, Dakota Outline label, no shadow, no border radius, hover fades in content using cubic-bezier(0.65,0,0.35,1)."

*Generated by Sparkbites — extracted from live CSS analysis*
