# syntaxui.com — Design Document

## 1. Visual Theme & Atmosphere

SyntaxUI operates in the space where developer tooling meets modern SaaS aesthetics. The overall feeling is clean, confident, and technical — a white canvas that lets interactive component previews do the talking. There is no decorative noise: no gradients on backgrounds, no hero illustrations, no ambient texture. The single deliberate injection of personality is the primary accent, a vivid crimson-pink (`rgb(251, 58, 93)`), which appears on CTAs only. Everything else defers to neutral gray values. The atmosphere reads like a well-lit workshop: functional, purposeful, and quietly proud of what it builds.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `#ffffff` / transparent | Page, surfaces, cards |
| Body text | `rgb(0, 0, 0)` | All prose, labels |
| Border / divider | `rgb(229, 231, 235)` | Component edges, input rings |
| Primary CTA | `rgb(251, 58, 93)` | Primary buttons only |
| CTA label | `rgb(255, 255, 255)` | Text on primary buttons |
| Subtle elevation | `rgba(24, 24, 27, 0.1)` | Ring shadow on interactive elements |

The palette is intentionally minimal: one accent, one neutral, one white. No secondary accent colors exist. This keeps attention locked on the UI component being demonstrated, never on the surrounding chrome.

---

## 3. Typography Rules

**Typeface:** Geist Sans — Vercel's own variable font, signalling a Next.js / Vercel ecosystem product.

| Context | Size | Weight | Leading | Tracking |
|---|---|---|---|---|
| Display headline (h1) | 48px | 700 | 48px (tight) | -1.2px |
| Body / prose | 16px | 400 | 24px | normal |
| Links, buttons | 16px | 400 | 24px | normal |

Tight letter-spacing on headings (-1.2px) compresses the headline into a sharp, confident slab. Body text uses a comfortable 1.5 leading ratio. There are no decorative typefaces, no serif, no monospace in the UI layer. The absence of a code font in the detected typography is notable — component previews likely rely on browser defaults or syntax highlighters.

---

## 4. Component Styling

Buttons follow a two-track system: the primary action gets the `rgb(251, 58, 93)` fill, while secondary and ghost variants stay transparent with a hairline `rgba(24, 24, 27, 0.1)` ring. Shadows on cards and panels use standard Tailwind-style `shadow-md` equivalents (`0 10px 15px -3px rgba(0,0,0,0.1)` + `0 4px 6px -4px rgba(0,0,0,0.1)`). Input fields receive a subtle inner ring (`rgba(250, 250, 250, 0.1) 1px inset`) suggesting dark-mode-ready component previews embedded in the light interface. No border-radius data was extracted, suggesting the site uses Tailwind's default rounded-md values throughout.

---

## 5. Layout Principles

The grid is wide and generous. Footer margins are fixed at `0px 112px` — roughly an 8-column centered container. Breakpoints span `416 / 600 / 640 / 768 / 1024 / 1280 / 1536px`, a near-complete Tailwind breakpoint ladder. Spacing is 8px-grid derived. No explicit gap values appear on the main layout, meaning component grids manage their own internal rhythm. The feel is single-column on mobile, expanding to a multi-column component gallery on desktop.

---

## 6. Depth & Elevation

Depth is handled through shadow rather than color. Two shadow tiers are used:
- **Hover / active ring:** `rgba(24, 24, 27, 0.1) 0px 0px 0px 1px` — a barely-there outline that confirms focus without lifting the element
- **Card elevation:** `0 10px 15px -3px rgba(0,0,0,0.1)` — Tailwind's `shadow-md`, giving component cards a gentle float

There are no dramatic drop shadows. Elevation is used to differentiate interactive layers from static content, not to create visual drama.

---

## 7. Do's and Don'ts

**Do:**
- Use `rgb(251, 58, 93)` exclusively for primary CTAs — never as a decorative accent
- Maintain `rgb(229, 231, 235)` for all borders and dividers
- Keep backgrounds white or transparent; avoid colored section backgrounds
- Apply `-1.2px` letter-spacing on any display-weight headline
- Use Geist Sans for all text; do not introduce a second typeface

**Don't:**
- Add gradient backgrounds or hero illustrations — the site earns attention through component quality
- Use more than one accent color
- Apply heavy shadows (`shadow-xl` or above) on page-level containers
- Mix font weights below 400 — the scale stops at regular
- Use border-radius values that pill-shape buttons (no `rounded-full`)

---

## 8. Responsive Behavior

The breakpoint ladder mirrors Tailwind's default config almost exactly. Key transitions:
- Below `640px`: single-column layout, footer margins collapse to zero
- `640–1024px`: two-column component grid
- `1024px+`: full multi-column gallery with `112px` side margins

The `416px` breakpoint suggests a custom adjustment for small Android devices. No horizontal scroll patterns or fixed-position overlays were detected; the layout reflows cleanly.

---

## 9. Agent Prompt Guide

> Build a component showcase page in the style of syntaxui.com. Use Geist Sans at 16px/400 for body and 48px/700/-1.2px for headings. Background is pure white. One accent color only: `#fb3a5d` for primary CTAs. All other surfaces are white with `rgb(229,231,235)` borders. Cards float on Tailwind `shadow-md`. No decorative elements — let the component preview be the hero. Responsive at Tailwind's standard breakpoints with 112px horizontal margins on desktop.

---

*Generated by Sparkbites — extracted from live CSS analysis*
