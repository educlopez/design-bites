# shader.se — Design System

## 1. Visual Theme & Atmosphere

Shader.se is the rare product that wears its concept on its sleeve: a creative tool for shader programming communicated through a design that feels like it *is* a shader. The canvas is pure black (`rgb(0,0,0)`) — not dark grey, not near-black, but absolute void — against which warm cream text (`rgb(252, 249, 243)`) glows like light through paper. The typographic choice reinforces this: STIX Two Text is a scholarly serif designed for scientific and mathematical publishing. The result is a site that feels like an illuminated manuscript or a mathematics textbook — intellectually serious, visually warm, deeply unconventional for a web tool.

No gradients, no borders, no shadows. Depth comes entirely from the contrast between black and cream, and from the semantic weight of the typeface.

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background | `rgb(0, 0, 0)` | Page canvas — absolute black |
| Foreground / text | `rgb(252, 249, 243)` | All text, links, UI labels |
| Focus ring | `rgb(255, 255, 255)` | Accessibility focus (white on black) |

CSS custom properties confirm the naming philosophy:
- `--background: #fff` (internal reference — inverted from actual use)
- `--foreground: #fcf9f3` (the warm cream tone)

Two colors. No tints, no shades, no accent. The design deliberately refuses decoration — the shader canvas itself is the visual product; everything else is typographic scaffolding.

## 3. Typography Rules

**Typeface:** `STIX Two Text` — a Unicode-complete serif developed for scientific journals. Every character choice here is a statement: this is a tool for people who write equations, not just code.

| Element | Size | Weight | Line Height |
|---|---|---|---|
| All elements | 16px | 400 | 24px (1.5) |

Remarkably flat typography hierarchy — every selector (`h1`, `h2`, `body`, `p`, `a`, `button`) shares identical size, weight, and line-height. Hierarchy is purely structural (HTML semantics) and spatial (margin/padding). This is a bold editorial choice: the content itself dictates importance, not typographic scale.

No letter-spacing adjustments, no transforms, no feature settings. Pure, unstyled text.

## 4. Component Stylings

- **Buttons:** Transparent background, cream text (`rgb(252, 249, 243)`). On focus: full white text and white outline — stark and functional.
- **Navigation:** Transparent over the black canvas. No background fill, no border.
- **No border-radius** detected — all elements are sharp-cornered or follow natural browser defaults.
- **No shadows** — elevation is meaningless on a black canvas; everything is flat.
- **No card components** in the traditional sense — the interface is likely a single full-bleed canvas with minimal chrome.

## 5. Layout Principles

- Zero margin/padding on body and all structural elements. Sections have a `-1px` margin — likely a technique to prevent sub-pixel gaps between full-bleed sections.
- Breakpoints: `640`, `768`, `1024`, `1280`, `1536`px — a full Tailwind-like responsive set, suggesting the layout adapts gracefully across all device sizes despite the minimalist design.
- The `--vw: 1svw` and `--vh: 8px` custom properties suggest viewport-relative sizing for the interactive canvas elements.
- Stack: **Next.js** — server-rendered, likely with a heavy client-side interactive canvas.

## 6. Depth & Elevation

None. The design philosophy actively rejects depth cues. On a black background with no shadows, borders, or gradients, the only "depth" is the luminance contrast between black and cream. Interactive elements gain weight through typography, not elevation.

This is an intentional artistic decision: the shader viewport is the only three-dimensional object on the page.

## 7. Do's and Don'ts

**Do:**
- Use absolute black (`#000`) as background — no softening to dark greys.
- Use warm cream (`#fcf9f3`) for all text and UI elements — never pure white in body copy.
- Apply `STIX Two Text` at 16px/400 weight — do not vary size or weight across the type system.
- Let white space and HTML structure carry hierarchy.
- Reserve pure white (`#fff`) for focus rings and accessibility states only.

**Don't:**
- Introduce any mid-tone colors, accent hues, or tints.
- Use card components, elevated surfaces, or glassmorphism.
- Apply letter-spacing, text-transform, or decorative font features.
- Add border-radius — keep all corners sharp.
- Use shadows of any kind.

## 8. Responsive Behavior

Full Tailwind breakpoint coverage (`sm/md/lg/xl/2xl`) despite the minimalist surface. The layout is likely a single-column editorial structure at mobile and expands to a split-pane editor + preview at wider viewports. The custom `--vw` and `--vh` properties manage the interactive shader canvas proportionally across viewport sizes.

## 9. Agent Prompt Guide

> Build a shader.se-style UI: absolute black canvas (`#000`) with warm cream text (`#fcf9f3`). Single typeface: STIX Two Text at 16px, weight 400, line-height 1.5. No size variation, no weight variation — pure flat typographic hierarchy. No shadows, no borders, no border-radius. Accent-free. Reserve pure white (`#fff`) only for focus states. Think: illuminated manuscript meets scientific computing terminal.

---

*Generated by Sparkbites — extracted from live CSS analysis*
