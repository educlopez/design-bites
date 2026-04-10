# DESIGN.md — danielsun.space

## 1. Visual Theme & Atmosphere

Daniel Sun's personal site is an exercise in confident typographic spectacle built on a minimal Framer canvas. The background is pure white; the typography is the design. A massive condensed headline — rendered at over 246px — functions less as text and less as image, occupying the full visual field like a billboard. Beneath it, a restrained body system in Inter Display handles readable prose. The site's chromatic restraint (essentially a black-and-white palette with a single warm yellow tint) keeps focus entirely on the typographic gesture. The personality is maximalist in scale, minimalist in color.

---

## 2. Color Palette & Roles

### Background
- **Pure White** (`rgb(255, 255, 255)`): The universal canvas. No tinting, no texture. The white is a stage for type.

### Surfaces
- **Light Gray 1** (`rgb(245, 245, 245)` ≈ `#f5f5f5`): Secondary content zones or card backgrounds. Near-invisible against white but creates gentle separation.
- **Light Gray 2** (`rgb(242, 242, 242)` ≈ `#f2f2f2`): A step darker — used for further differentiated content blocks.
- **Near-Black** (`rgb(31, 31, 31)` ≈ `#1f1f1f`): The single dark surface — likely a footer or a contact/CTA section. Provides strong contrast anchor at page end.

### Text & Accents
- **Pure Black** (`rgb(0, 0, 0)`): All body and heading text.
- **Warm Yellow Tint** (`rgba(255, 213, 0, 0.15)`): A ghost-yellow highlight applied to a specific interactive element — barely visible, more of a warmth hint than a color statement.
- **Browser Blue** (`rgb(0, 0, 238)`): Raw link color, unoverridden — signals a deliberately raw, editorial approach to interactivity.

---

## 3. Typography Rules

**Reddit Sans Condensed** (246px, weight 900, 221px line-height): The hero typeface. This is not a conventional heading — it is a typographic installation. At weight 900, the condensed letterforms create maximum visual density. The line height is set below the font size (221px vs 246px), causing tight vertical stacking for dramatic effect. This typeface exists in exactly one place: the top of the page.

**Inter Display** (29.63px, weight 500, 38.52px line-height): The secondary typeface for readable content. "Inter Display" is the optical sizing variant of Inter, optimized for sizes above 24px. Used at medium weight for clear, approachable body sections.

Generic **sans-serif** at 12px appears for UI chrome fallback text — essentially invisible Framer placeholder text.

The system has no monospace, no serif, no third typeface. The contrast between a 246px condensed black and a 30px medium sans defines the entire typographic hierarchy.

---

## 4. Component Styling

- **Border Radius**: Three values — `14px` (standard cards), `80px` (pill/large-rounded elements), `32px` (intermediate rounded). Shapes are noticeably soft, never sharp.
- **Links**: Retain browser-native blue. Hover state is null (undefined) — links may animate via Framer Motion rather than CSS hover.
- **Yellow tint surface**: `rgba(255, 213, 0, 0.15)` — a barely-visible warm wash used on a highlighted link/tag. Subtle warmth without chromatic distraction.
- **Interactive states**: Focus uses standard browser outline (`rgb(0, 95, 204)`). The minimal hover investment reinforces the editorial, non-commerce intent.
- **No shadows**: Shadow array is empty throughout.

---

## 5. Layout Principles

Breakpoints at 640, 992, 1200, 1600px suggest a standard Framer responsive ladder. The 640px breakpoint collapses the hero typographic element — the 246px headline requires significant reflow at mobile scales. Layout is built around a single full-width typographic moment at the top, followed by contained content zones. The near-black surface section provides a clear bottom anchor. No sidebar. No complex navigation.

---

## 6. Depth & Elevation

Depth is entirely typographic. The 246px headline creates a visual foreground plane by sheer scale; everything beneath it recedes naturally. The four surface tiers (white → #f5f5f5 → #f2f2f2 → #1f1f1f) provide a luminance ladder that implies depth without shadows. No box-shadows exist anywhere in the system. Framer Motion handles perceived z-axis through scroll-triggered animations.

---

## 7. Do's and Don'ts

**Do:**
- Let the hero headline dominate. It IS the design. Do not compete with it.
- Keep the color palette binary (black on white) with only ghost-level tints for accents.
- Use `14px` radius for standard cards, `80px` for pill shapes.
- Respect the line-height compression on the hero text — tight stacking is intentional.
- Honor the white canvas — never introduce background textures or gradients.

**Don't:**
- Use Reddit Sans Condensed at sizes below ~100px — it loses its architectural quality.
- Add shadows or elevation effects.
- Override the link blue with a brand color — the raw blue is an aesthetic choice.
- Break the two-typeface system by introducing a serif or monospace.
- Add decorative elements to the hero zone. The type is the only ornament.

---

## 8. Responsive Behavior

The 246px hero headline is the primary responsive challenge. Below 640px, it will need to scale dramatically — likely to 80–120px. The Inter Display body copy handles small screens gracefully. The near-black section at the bottom remains full-width. Three-tier breakpoints (640 / 992 / 1200) map to standard mobile / tablet / desktop. The 1600px breakpoint accommodates wide-screen typographic centering.

---

## 9. Agent Prompt Guide

> Build a personal portfolio page matching danielsun.space: pure white background, hero section with Reddit Sans Condensed at maximum weight and size (900 weight, condensed, ~200px+), Inter Display at 30px weight 500 for body sections. Near-black footer surface (`#1f1f1f`). Light gray intermediate sections (`#f2f2f2`). Border radius 14px standard, 80px pill. No shadows. Ghost-yellow tint (`rgba(255,213,0,0.15)`) for highlight tags only. No gradients.

---

*Generated by Sparkbites — extracted from live CSS analysis*
