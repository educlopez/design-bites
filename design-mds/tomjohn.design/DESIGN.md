# tomjohn.design — Design System

## 1. Visual Theme & Atmosphere

Tom John's portfolio is a study in deliberate darkness — a near-black canvas (`rgb(33, 33, 33)`) that forces every element to earn its place with light. The atmosphere is hushed and editorial: no gradients, no decorative borders, no visual noise. Typography does all the heavy lifting, switching between bright white headlines and 60%-opacity secondaries to create depth without introducing additional colors. The result feels like a well-curated gallery at night — intimate, confident, and free of anything superfluous.

Built on Framer, the site relies on motion (Framer Motion) rather than decoration for engagement. Hover states use the mildest possible tint (`rgba(255, 255, 255, 0.05)`) — barely there, but enough to signal interactivity.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| **Canvas** | `rgb(33, 33, 33)` | Page background — the dominant tone |
| **Primary text** | `rgb(255, 255, 255)` | H1 headings, hero copy |
| **Secondary text** | `rgba(255, 255, 255, 0.6)` | H2 labels, captions, metadata |
| **Tertiary text** | `rgb(221, 221, 221)` | H3 and supporting copy |
| **Hover surface** | `rgba(255, 255, 255, 0.05)` | Link/card hover state |
| **Transparent** | `rgba(0, 0, 0, 0)` | Default element background |

No accent color. No brand hue. The only color is luminance — things glow out of the dark or recede into it. This restraint is the design statement.

## 3. Typography Rules

**Typeface:** Inter (with Inter Placeholder fallback) — a single family across all roles.

| Selector | Size | Weight | Line Height | Notes |
|----------|------|--------|-------------|-------|
| `h1` | 24px | 400 | 28.8px (1.2×) | Deceptively small for a hero — intimacy over grandeur |
| `h2` | 12px | 400 | normal | Used as section labels / caps-style metadata |
| `body/p` | 12px | 400 | 16.8px (1.4×) | Compact reading size |
| `a` | 12px | 400 | normal | Same scale as body |

No letter-spacing adjustments. No text transforms. No bold weights. The hierarchy is built entirely on size differential (24px vs 12px) and opacity modulation in color — a two-level scale that creates focus without visual complexity.

**Notably absent:** No display typeface, no italic, no uppercase styling, no weight variation beyond 400.

## 4. Component Stylings

No explicit component tokens are defined in CSS. Components emerge from minimal context:

- **Links** — `rgba(255,255,255,0.05)` background on hover; hairline refinement, not a full button treatment
- **Cards/surfaces** — implied by dark background with typography grouping; no borders, no shadows
- **Tags/labels** — H2 text at 12px with reduced opacity acts as a tagging system
- **Motion layer** — Framer Motion handles transitions; CSS is intentionally static

The emptiness of the component layer is intentional: Tom John's portfolio speaks through layout and imagery, not UI chrome.

## 5. Layout Principles

- **Two breakpoints:** `809.98px` (tablet) and `810px` / `1399.98px` (desktop cap)
- Likely a centered single-column or constrained two-column grid at desktop
- Generous whitespace inferred from typography scale — 24px headings with 28.8px line height breathe naturally
- Framer's layout engine handles column reflow; no manual grid system exposed in CSS

## 6. Depth & Elevation

No shadows. No borders. No blur layers. Depth is achieved purely through:

1. **Opacity gradation** — white at 100%, 60%, and ~87% creates three perceived layers
2. **Animation** — Framer Motion lifts elements into focus temporally rather than spatially
3. **Background contrast** — the dark canvas ensures any foreground element reads as elevated simply by existing

## 7. Do's and Don'ts

**Do:**
- Use Inter exclusively; don't introduce a second typeface
- Maintain the 12px / 24px two-step size system
- Use white-on-dark; never dark-on-dark
- Keep hover states to near-invisible tints — no color fills, no borders on hover
- Let motion carry interactivity weight

**Don't:**
- Add accent colors or brand hues — monochromaticism is the identity
- Use `font-weight: 700`; bold reads as jarring against this palette
- Add box shadows or card borders — they break the gallery aesthetic
- Use uppercase or letter-spacing for hierarchy — the current system achieves it through size and opacity alone

## 8. Responsive Behavior

| Range | Behavior |
|-------|----------|
| `< 810px` | Mobile layout (tablet-down) |
| `810px – 1399px` | Standard desktop |
| `> 1400px` | Likely capped or wider layout |

Typography scale appears to hold constant — at 24px max, even the headline is already compact enough to work at mobile width without adjustment.

## 9. Agent Prompt Guide

> "Design in the style of tomjohn.design: dark near-black canvas `#212121`, white text at full and 60% opacity for hierarchy, single Inter typeface at 12px and 24px only, weight 400 throughout, zero accent colors, hover states as barely-visible white tints, no shadows or decorative borders, motion-first interactivity via subtle entrance animations."

*Generated by Sparkbites — extracted from live CSS analysis*
