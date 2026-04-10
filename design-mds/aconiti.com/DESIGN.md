# aconiti.com — Design System

## 1. Visual Theme & Atmosphere

Aconiti commits to a single bold statement: an electric blue that covers the entire canvas. This is not an accent-on-white design — the brand color *is* the background. Everything else surrenders to it. White text on pure blue creates maximum contrast with zero visual noise, producing a UI that feels confident, almost declarative. There are no gradients, no textures, and no competing hues. The effect is clean to the point of austerity, recalling early SaaS landing pages but executed with modern type restraint.

The absence of drop shadows and decorative radius suggests a site that trusts its color and typography alone to carry the experience. This is a brand-led design, not a component-led one.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Brand / Background | `rgb(17, 115, 255)` | Full-page background, body fill |
| Primary Text | `rgb(255, 255, 255)` | All headings, paragraphs, links |
| Surface Light | `rgb(255, 255, 255)` | Cards or inset panels |
| Surface Subtle | `rgb(245, 245, 245)` | Secondary card surfaces |
| Border Default | `rgb(229, 231, 235)` | Dividers, subtle outlines |

**What's absent:** There are no dark neutrals, no secondary accent colors, and no semantic colors (error red, success green). The palette is intentionally monochromatic — blue + white, nothing else. This signals a focused MVP or a brand identity page rather than a feature-rich app.

## 3. Typography Rules

Two typefaces share the work, each with a defined role:

- **Switzer** — Used for headings (h1–h2), paragraphs, and links. A geometric grotesque that reads as contemporary and neutral. The h1 is set at only 17px / weight 500, which is deliberately understated — this is not a hero-headline design.
- **Inter** — The body fallback, 16px / weight 400 / 24px line-height. Familiar, reliable, invisible.

**Key insight:** The type scale is compressed. H1 at 17px, H2 at 14px, body at 16px — these sizes barely differ, implying a layout that relies on color, spacing, and whitespace rather than typographic hierarchy. No uppercase transforms, no tracked-out labels, no display sizes. The voice is quiet and informational.

## 4. Component Styling

- **Links** render as white text on blue — no underline cues visible in the extracted state. Hover states were not captured, suggesting minimal interactive feedback or CSS-in-JS based transitions.
- **Buttons** likely inherit the white-on-blue pattern with border or fill inversion on hover.
- **Cards/Surfaces** use white (`#ffffff`) or near-white (`rgb(245,245,245)`) backgrounds as islands of contrast against the blue field.
- **Borders** use `rgb(229, 231, 235)` — a Tailwind `gray-200` equivalent — for subtle internal separators.
- **Border radius** is not extracted (no values), implying either sharp corners or values set inline/via utility classes rather than at the element level.

## 5. Layout Principles

Built on **Next.js + Tailwind CSS**, the layout follows utility-first conventions:

- Breakpoints: `640 / 768 / 1024 / 1280 / 1536px` — standard Tailwind responsive scale, used verbatim.
- Zero padding on `body` and `main`, meaning all spacing is handled at the component level via utility classes.
- Likely uses max-width containers centered with `mx-auto`, consistent with Tailwind's default layout idiom.
- The compressed type scale suggests a layout-driven by compact information density, not expansive hero sections.

## 6. Depth & Elevation

Depth is conspicuously absent. No box shadows were detected on any element. No blur, no gradient overlays, no layered z-index stacking via visual cues.

This is a **flat design** in the purest sense — all elements exist on the same visual plane. The only separation comes from background color changes between sections (blue body vs. white cards). Elevation is communicated through color contrast, not shadows.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(17, 115, 255)` as the dominant background — lean into the boldness.
- Pair Switzer for display/UI text with Inter as the system fallback.
- Keep the type scale tight and the color palette constrained to blue + white.
- Use white card surfaces sparingly — they're meant to be exceptions, not the norm.
- Maintain borderless or lightly bordered components; shadows undermine the flat aesthetic.

**Don't:**
- Introduce secondary accent colors — a second hue would shatter the monochromatic tension.
- Use heavy font weights or large display sizes; the understated scale is intentional.
- Add gradients or background images — the solid blue is a deliberate creative choice.
- Use dark text on the blue background; white-only ensures legibility and consistency.

## 8. Responsive Behavior

The site uses all six standard Tailwind breakpoints (`sm: 640`, `md: 768`, `lg: 1024`, `xl: 1280`, `2xl: 1536`). The dual breakpoint at `767/768` suggests explicit max-width overrides for mobile edge cases — a common pattern when fine-tuning layout collapse behavior.

No font-size scaling was detected across breakpoints, implying the compressed type scale is fixed rather than fluid. Layout reflow likely happens at `md` (768px) where single-column mobile gives way to a multi-column structure.

## 9. Agent Prompt Guide

Use this when generating UI in the style of aconiti.com:

> Build a flat, high-contrast interface where `rgb(17, 115, 255)` is the page background and all text is pure white. Use Switzer (geometric grotesque) for headings and UI labels; Inter for body text. Keep the type scale compressed: headings at 14–17px, body at 16px, no large display sizes. Add no shadows, no gradients, and no secondary colors. White card surfaces (`#fff`) appear only as exception panels. Use Tailwind's standard breakpoints. The design philosophy: brand color as canvas, silence as composition.

---

*Generated by Sparkbites — extracted from live CSS analysis*
