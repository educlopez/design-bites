# kuldar.com — Design System

## 1. Visual Theme & Atmosphere

Kuldar's personal site is a masterclass in contemporary portfolio restraint. Built entirely on the Satoshi typeface — a geometric neo-grotesque — it speaks in a single typographic voice with minimal color, no decoration, and surgical use of space. The palette leans on near-black backgrounds with warm off-white text, giving the impression of a dark studio rather than a bright screen. Focus states are marked with a vivid amber oklch color, the only moment of personality in an otherwise disciplined, monochromatic system. The atmosphere is confident, modern, and curator-like: everything unnecessary has been removed.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|---|---|---|
| **Primary Text** | `oklch(0.922 0 0)` ≈ `#EBEBEB` | Off-white; warm, easy on dark backgrounds |
| **Body Background** | `#000045` / `rgb(0, 0, 69)` approx | Deep navy-black; near-midnight |
| **Secondary Text** | `#999994` | Muted warm grey for supporting content |
| **Focus / Accent** | `oklch(0.795 0.184 86.047)` ≈ Amber | Keyboard focus outlines; only accent in the system |
| **Borders / Dividers** | `oklch(0.922 0 0)` | Same as text — unified, monochromatic |

The color system is near-monochrome with a single functional accent. The use of oklch for the focus color is a deliberate modern CSS choice — it ensures perceptual uniformity. No decorative colors exist; every value serves a legibility or state purpose.

---

## 3. Typography Rules

| Element | Font | Size | Weight | Line Height | Letter Spacing |
|---|---|---|---|---|---|
| `h1` | Satoshi | 24px | 700 | 27px (1.125) | -0.6px |
| `body` | Satoshi | 16px | 400 | normal | normal |
| `a` (links) | Satoshi | 16px | 400 | normal | normal |

A single-family system — Satoshi throughout. The display heading is tight (27px line height on 24px type) with subtle negative tracking (-0.6px), giving headlines a compact, professional snap. Body text is set at comfortable defaults. No text-transform, no ornamental letter-spacing — the type does its job cleanly. The absence of a serif or display contrast font keeps the system cohesive and fast to load.

---

## 4. Component Stylings

**Links**
- Default: `oklch(0.922 0 0)` text, transparent background
- Focus: dashed amber outline (`oklch(0.795 0.184 86.047) dashed 2px`) — accessible and visually distinct
- Hover: not extracted (likely subtle opacity or underline)
- No border radius on link states

**Buttons**
- Rounded (`rounded` class detected) — the only rounded element in the system
- Likely uses the same Satoshi type and monochrome color palette

**Header / Navigation**
- Transparent background — floats over content
- White text, no border

**Interactive States**
- Focus is the primary interactive signal — amber dashed outline, 2px
- Transform and box-shadow absent from interactive states — no scale/lift effects

---

## 5. Layout Principles

- Body has no explicit padding or margin — content manages its own spacing
- Gap values used contextually within flex/grid children
- No formal spacing scale detected — spacing is component-level, not system-level
- Breakpoints: large viewport limit detected (~33,554,432px — effectively no max-width constraint, or a CSS artifact)
- The layout philosophy is single-column or asymmetric grid, tightly controlled

---

## 6. Depth & Elevation

No shadows detected. Border radius appears only on button-type elements (`rounded`). The dark background creates inherent depth contrast between the page and any lighter surfaces. Elevation is achieved through color value shifts rather than drop shadows — a flat dark-mode aesthetic where surface hierarchy is implied by darkness level, not shadow stacking.

---

## 7. Do's and Don'ts

**Do:**
- Use Satoshi exclusively — one font, full stop
- Keep the palette near-monochrome: near-black bg, off-white text, grey secondaries
- Use oklch amber only for focus states — don't repurpose it as a brand accent
- Apply negative letter-spacing to headings (-0.6px) for professional snap
- Rely on whitespace and type scale for hierarchy, not color

**Don't:**
- Mix in serif or display fonts — the mono-family system is intentional
- Add drop shadows or gradients — this is a flat dark system
- Use the amber focus color decoratively
- Add heavy borders or decorative dividers
- Overcrowd the layout — restraint is the brand

---

## 8. Responsive Behavior

No conventional breakpoints (e.g., 768px, 1024px) were detected. The site likely uses fluid typographic scales and percentage-based layouts that adapt naturally. The 24px heading and 16px body remain legible across viewports without needing responsive overrides. The single dark surface and minimal component set means there is little to reflow.

---

## 9. Agent Prompt Guide

**Quick color reference:**
- Background: `#000045` (deep navy-black)
- Primary text: `oklch(0.922 0 0)` ≈ `#EBEBEB`
- Secondary: `#999994`
- Accent (focus only): `oklch(0.795 0.184 86.047)` — amber

**Prompt to recreate this style:**
> "Design a personal portfolio page in the style of kuldar.com: deep near-black background (#000045), off-white text in Satoshi, single-font system, no decorative colors, amber dashed focus outlines as the only accent. Atmosphere: dark studio, confident minimalism, every element earns its place."

**Prompt for a component:**
> "Create a project list item: Satoshi 16px, off-white text on dark background, no shadow, no border, subtle secondary label in #999994, amber dashed outline on keyboard focus only."

*Generated by Sparkbites — extracted from live CSS analysis*
