# skills.smoothui.dev — Design System

## 1. Visual Theme & Atmosphere

SmoothUI Skills is a developer-focused component showcase that takes the "modern developer tool" aesthetic and adds genuine personality through a single explosive accent: electric indigo (`rgb(38, 1, 253)`). The base is a barely-there off-white (`rgb(251, 252, 253)`) — so close to white it reads as white, but avoids flatness. Against this near-clinical background, the electric blue functions like a neon sign in a quiet room: unmissable, brand-defining, and technically expressive (it mirrors the kinds of colors you'd see in a WebGL color picker or shader output).

The type system pairs Geist — Vercel's custom geometric sans — with Geist Mono for code samples, creating an explicit "this is for developers" signal without resorting to clichés. The overall mood is: sharp, capable, slightly playful.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Page background | `rgb(251, 252, 253)` | Canvas — near-white |
| Primary text | `oklch(0.18 0.005 250)` | Body copy, headings |
| Secondary text | `oklch(0.45 0.005 250)` | Buttons, labels, meta |
| Electric accent | `oklch(0.458 0.305 268.13)` / `rgb(38, 1, 253)` | CTAs, active states, slider handles |
| White | `rgb(255, 255, 255)` | Text on accent, icon fills |
| Surface tint | `rgb(241, 242, 243)` | Subtle component backgrounds |
| Ruler surface | `rgba(251, 252, 253, 0.95)` | Floating UI chrome |

The use of `oklch` for text colors is notable — this is a perceptually uniform color space, ensuring the slight blue-grey tint in the dark text is consistent across display gamuts. The accent color intentionally lives at maximum chroma in oklch space: vivid, electric, impossible to miss.

## 3. Typography Rules

**Primary:** `Geist` → `Inter` → `system-ui` → `-apple-system` → `sans-serif`
**Monospace:** `Geist Mono` → `JetBrains Mono` → `Fira Code` → `monospace`

| Element | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|
| H1 | 40px | 600 | 46px | -0.8px |
| H2 | 28px | 500 | 35px | -0.7px |
| Body | 15px | 400 | 24.375px | normal |
| Paragraphs | 14px | 400 | 22.75px | normal |
| Links | 14px | 500 | 20px | normal |
| Code | 11px | 400 | 11px | normal |

Negative letter-spacing on headings (−0.8px at h1, −0.7px at h2) is a deliberate choice to make large type feel tighter and more premium — a common pattern in modern dev-tool marketing. The body type at 15px with a 1.625 line-height is optimally comfortable for reading documentation or component descriptions.

## 4. Component Stylings

- **Buttons:** Transparent default with `oklch` accent on hover/active. Electric indigo shadow (`rgba(38, 1, 253, 0.3) 0 1px 3px`) on primary CTAs.
- **Slider handle:** `rgb(38, 1, 253)` fill — the accent color is used to brand interactive demo components.
- **Code blocks:** `Geist Mono` at 11px with 1:1 line-height — tight, dense, code-terminal aesthetic.
- **Border radii:** `4px` (inputs, tags), `6px` (buttons, cards), `18px` (pills/chips), `0px 0px 6px 6px` (bottom-only rounding on dropdown/panel bottoms).
- **Shadows:** Two-level system — `oklch(0 0 0 / 0.08) 0 1px 3px` (surface lift) + `oklch(0 0 0 / 0.06) 0 4px 12px` (card float).
- **Tag/copy button:** `rgb(0, 17, 101)` darker variant of accent — used for code tags, keeping the blue family cohesive.

## 5. Layout Principles

- Section vertical rhythm: `margin-bottom: 96px` per section — generous breathing room between demos.
- Header bottom margin: `24px` — close to content it labels.
- Footer: `padding: 80px 0 64px` — structured, book-like bottom.
- Single breakpoint at `768px` — clear mobile/desktop split, no intermediate tablet states.
- Stack: **Astro v6** + **Tailwind CSS** — static-first with interactive islands for demos.

## 6. Depth & Elevation

Two-layer shadow system using oklch:
- **Layer 1 (subtle lift):** `oklch(0 0 0 / 0.08) 0px 1px 3px` — barely perceptible, used on card edges.
- **Layer 2 (card float):** `oklch(0 0 0 / 0.06) 0px 4px 12px` — soft diffuse shadow for floating panels.
- **Accent glow:** `rgba(38, 1, 253, 0.3) 0 1px 3px` — a colored shadow on primary action elements. This is the only colored shadow in the system and is used sparingly.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(38, 1, 253)` as the single accent — it's the entire brand personality in one color.
- Apply negative letter-spacing (`-0.7px` to `-0.8px`) to headings at h1/h2 scale.
- Use `Geist` for UI text and `Geist Mono` for any code or technical strings.
- Keep section spacing generous (96px between sections).
- Use border-radius consistently: `6px` for interactive components, `18px` for pill elements.

**Don't:**
- Dilute the accent with secondary accent colors.
- Use warm tones — the palette is cool-neutral throughout.
- Apply box-shadows without the oklch color system — use the defined shadow tokens.
- Reduce code block font below 11px.
- Add decorative text transforms or uppercase styles.

## 8. Responsive Behavior

Hard breakpoint at `768px`. Below this:
- Demo components likely stack vertically.
- Side-by-side code/preview panels collapse.
- The ruler/slider UI adapts to touch targets.
- Type sizes appear to remain constant (no clamp detected) — the scale is already compact enough for mobile.

## 9. Agent Prompt Guide

> Build a SmoothUI-style developer component site: near-white background (`#fbfcfd`), Geist typeface, electric indigo accent (`rgb(38,1,253)` / `oklch(0.458 0.305 268.13)`). Heading size scale from 40px (−0.8px tracking) down to 14px body. Use `6px` border-radius for components, `18px` for pills. Two-shadow system: 8% opacity lift + 6% opacity float. Single breakpoint at 768px. Code in Geist Mono at 11px. Everything else stays cool-neutral.

---

*Generated by Sparkbites — extracted from live CSS analysis*
