# krea.ai -- Design System Reference

## 1. Visual Theme & Atmosphere

AI-product UI with polished token-driven theming via oklch colour space. Clean surfaces and strong contrast hierarchy serve the generative tool experience. The palette supports both light and dark modes via CSS custom properties.

The overall mode is **dark**, with a editorial, serif-driven typographic identity. Shadows and elevation are used sparingly to separate key surfaces.

---

## 2. Color Palette & Roles

### Design Tokens

- `var(--background)`: `oklch(100% 0 0)`
- `var(--foreground)`: `oklch(14.5% 0 0)`
- `var(--card)`: `oklch(100% 0 0)`
- `var(--card-foreground)`: `oklch(14.5% 0 0)`
- `var(--popover)`: `oklch(100% 0 0)`
- `var(--popover-foreground)`: `oklch(14.5% 0 0)`
- `var(--primary)`: `oklch(0% 0 0)`
- `var(--primary-foreground)`: `oklch(100% 0 0)`
- `var(--secondary)`: `oklch(97% 0 0)`
- `var(--secondary-foreground)`: `oklch(20.5% 0 0)`
- `var(--muted)`: `oklch(97% 0 0)`
- `var(--muted-foreground)`: `oklch(55.6% 0 0)`

### Computed Roles

- **text (body)**: `oklch(0.985 0 0)`
- **border (body)**: `oklch(1 0 0 / 0.1)`
- **border (header)**: `oklab(0.999994 0.0000455678 0.0000200868 / 0.15)`
- **background (footer)**: `rgb(245, 245, 245)`
- **text (footer)**: `rgb(163, 163, 163)`
- **surface (div.bg-primary-0)**: `rgb(255, 255, 255)`
- **surface (div.bg-primary-200)**: `rgb(229, 229, 229)`
- **surface (div.)**: `rgb(212, 212, 213)`
- **surface (div.embla__progress)**: `rgb(115, 115, 115)`
- **surface (div.bg-primary-800)**: `rgb(38, 38, 38)`
- **surface (section.section-container)**: `rgb(11, 15, 21)`
- **surface (div.header-background)**: `rgba(0, 0, 0, 0.8)`

**Key observations:** Token-driven colour system -- use CSS custom properties as the single source of truth. Never hardcode hex values. Dark-mode-first palette.

---

## 3. Typography Rules

**h1** -- Suisse Intl, 60px, weight 400, line-height 63px

**Hierarchy principle:** A single typeface (Suisse Intl) handles all levels. Size and weight alone establish rhythm.

**What is absent:** No monospace or system-UI fallback. The serif identity is deliberate -- do not substitute.

---

## 4. Component Styling

**Border radii:** No border radii detected -- corners are sharp throughout.

**Interactive states:**
- `button`: tag: button.nav-features-button "Features", default: [object Object], hover: [object Object], focus: [object Object]
- `button`: tag: button.focus-visible:border-ring "Sign up for free", default: [object Object], hover: [object Object], focus: [object Object]
- `button`: tag: button.focus-visible:border-ring "Log in", default: [object Object], hover: [object Object], focus: [object Object]
- `a[href]`: tag: a.block, default: [object Object], hover: null, focus: [object Object]

**Buttons & controls:** Match the typographic register -- serif labels, generous line-height, understated borders.

---

## 5. Layout Principles

Common padding values: 68px 0px 0px, 16px 64px. Flex/grid gaps: 8px.

The dominant padding rhythm (68px 0px 0px) suggests a fixed-pixel grid.

Avoid introducing grid lines, dividers, or decorative rules unless absolutely necessary. Let whitespace do the structural work.

---

## 6. Depth & Elevation

- `element`: `"rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px"`
- `element`: `"rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0) 0px 0px 0px 2px"`
- `element`: `"rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px"`
- `element`: `"rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 6px 0px"`

Use shadows conservatively -- reserve elevation for interactive feedback (dropdowns, modals), not decorative layering.

---

## 7. Do's and Don'ts

**Do:**
- Respect the editorial, serif-driven typographic voice -- every element should speak the same typeface language.
- Use whitespace as a primary design tool. When in doubt, add space rather than elements.
- Reference CSS custom properties exclusively -- never bypass the token layer.
- Keep interactions subtle: micro-transitions at 150-200ms maximum.

**Don't:**
- Do not swap the serif for a sans-serif alternative. The editorial register depends on it.
- Do not add drop shadows, gradients, or decorative textures unless they are already present in the system.
- Do not use colour to communicate hierarchy -- spacing and scale do that work here.
- Avoid centring body text. The layout has a strong left-anchored reading rhythm.

---

## 8. Responsive Behavior

No explicit CSS breakpoints extracted. The layout relies on fluid units, CSS Grid auto-fit, or a single-column mobile-first approach.

Build mobile-first. Use fluid type and spacing where the existing CSS suggests it (clamp(), vw units). Avoid rigid pixel breakpoints if the system uses fluid scaling.

On small screens, collapse multi-column layouts to a single column without compromising the typographic scale. The type should remain readable -- never below 14px rendered size.

---

## 9. Agent Prompt Guide

When generating UI components, extensions, or page sections for **krea.ai**, instruct the agent as follows:

> "Build in the style of krea.ai: ai-product ui with polished token-driven theming via oklch colour space. Use Suisse Intl as the primary typeface. Dark background, light text. Shadows only for modal-level elevation. Token-driven colours via CSS custom properties. No animations -- immediate state changes only. Generous whitespace, strong typographic scale. Sharp corners throughout."

---

*Generated by Sparkbites -- extracted from live CSS analysis*