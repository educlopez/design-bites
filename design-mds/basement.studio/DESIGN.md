# Basement Studio — Design System Reference

## 1. Visual Theme & Atmosphere

Basement Studio is a development studio site that makes a clear aesthetic argument: black is not absence, it is presence. The canvas is absolute black, the primary type is near-white, and the single accent color — `rgb(255,77,0)` — burns through like a warning light. This is not dark mode as accessibility feature or trend compliance; it is dark mode as creative statement. The secondary typeface, `flauta`, is rendered in uppercase throughout, adding a brutalist, stencil-like quality that contrasts with the geometric precision of the primary `Geist` font. The design is confident, unapologetic, and deeply intentional.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(0,0,0)` — page background (absolute black)
- `rgb(26,26,26)` — input surface, near-black elevated surface

**Text**
- `rgb(255,255,255)` — primary text (nav, body, buttons)
- `rgb(230,230,230)` — h1 display text (slightly softened from pure white)
- `rgb(117,117,117)` — h2 secondary heading (mid-gray)
- `rgb(196,196,196)` — muted button text

**Brand accent**
- `rgb(255,77,0)` — link color, focus ring (a vivid orange-red)

**Shadow**
- `rgba(255,140,0,0.15) 0px 0px 5px 0px` — a warm amber glow, very subtle

The orange accent is the only hue in the system. Its use on links and focus rings makes it a functional signal as much as a brand marker — you cannot ignore it against pure black.

---

## 3. Typography Rules

Basement Studio uses two custom typefaces in deliberate contrast:

**Primary:** `Geist` — the monospace-influenced geometric sans by Vercel, at 600 weight with aggressive negative tracking
**Secondary:** `flauta` — a display/decorative font used on form elements and body text in uppercase with `"ss01"` OpenType feature

**Scale**
| Role | Font | Size | Weight | Tracking |
|------|------|------|--------|----------|
| H1 | Geist | 87px | 600 | -3.48px |
| Body / form | flauta | 14px | 400 | normal |
| Textarea | flauta | 14px | 400 | normal |

- 87px headline with -3.48px tracking is extremely compressed — letters almost touch at the largest sizes, creating a wall-of-type poster effect
- `flauta` is always uppercase — it functions as a labeling/annotation system rather than prose
- The Geist/flauta pairing creates a hierarchy between structural headline content and operational UI text

**What's absent:** No regular-weight body copy font, no serif. The site treats all body text as UI text.

---

## 4. Component Stylings

**Buttons**
- Grid-span buttons: transparent bg, white text; no hover state captured
- Inline-flex buttons: transparent bg, `rgb(196,196,196)` text (muted default)
- Focus ring: `rgb(0,0,0) 0px 0px 0px 2px` (inner) + `rgb(255,77,0) 0px 0px 0px 3px` — the orange brand color as the outer focus ring

**Input fields**
- Background: `rgb(26,26,26)` — a barely-lighter surface than the page
- Text: white
- No visible border in resting state — the input is defined by its background plane

**Shadows**
- Single shadow value: `rgba(255,140,0,0.15) 0px 0px 5px 0px` — an extremely subtle warm orange ambient glow, likely applied to key UI elements or hover states

**Border radius**
- None defined (`borderRadii: []`) — sharp edges throughout. No rounded corners anywhere.

---

## 5. Layout Principles

Sharp grid. No border radius. The layout is built on Next.js + Tailwind CSS with breakpoints at 600, 640, 768, 1024, 1280, 1536, 1920px. The absence of rounded corners is not an oversight — it is part of the brutalist vocabulary. Every container, button, and input is rectangular. Spacing and alignment carry all the structural work.

---

## 6. Depth & Elevation

Depth is minimal and textural:
- `rgb(26,26,26)` input surfaces float slightly above the pure-black page
- The amber glow shadow (`rgba(255,140,0,0.15)`) adds warmth without lifting elements
- Focus rings use the orange accent for the outer ring — depth through color pop, not shadow

No cards, no modals, no layered surfaces in the extracted data. The site appears to operate on a single dark plane with type and glows as the only relief.

---

## 7. Do's and Don'ts

**Do:**
- Use `rgb(255,77,0)` exclusively for links and focus rings — it is the only hue
- Apply extreme negative tracking (-3.48px) to Geist at display sizes
- Force `flauta` to uppercase everywhere — never use it mixed-case
- Keep all corners sharp — no border-radius
- Use the amber glow shadow sparingly for hover feedback

**Don't:**
- Introduce any second accent color — the orange is singular and sacred
- Add rounded corners — the sharp-edge brutalism is deliberate
- Use gray for body copy — grays are reserved for heading hierarchy (`h2`) and muted UI text
- Add box-shadows for elevation — the ambient glow is for warmth, not depth signaling

---

## 8. Responsive Behavior

The breakpoint set spans 600–1920px. At 600px (not 640 — a custom mobile threshold), the layout shifts. The uppercase `flauta` labels and compressed Geist headings likely reflow to stacked layouts but retain their typographic character at all sizes. The focus ring pattern (orange outer ring) is accessible on both dark and light viewport contexts.

---

## 9. Agent Prompt Guide

> Build a UI that matches Basement Studio's design language.

Absolute black background. Geist font at 600 weight, -3.48px tracking for headlines (87px equivalent). All UI labels and form elements use `flauta` in uppercase. The only hue in the system is `rgb(255,77,0)` — applied to links and as the outer focus ring. Inputs are `rgb(26,26,26)` — no border, just a darker plane. Buttons are transparent with white or muted-gray text. No border-radius anywhere. Optional: add `rgba(255,140,0,0.15)` ambient glow shadow on interactive elements.

---

*Generated by Sparkbites — extracted from live CSS analysis*
