# yevhenyurchuk.com — Design System

## 1. Visual Theme & Atmosphere

Yevhen Yurchuk's portfolio is a study in reduction. White canvas, black type, and a single interaction pattern — hover inverts a navigation item to black with white text — constitute the entire design vocabulary. There are no gradients, no shadows, no accent colours, no custom fonts beyond Inter. The aesthetic is deeply Swiss: grid-driven, typographically precise, deliberately silent. What makes it distinctive is not what it has, but what it refuses to have. The work is the visual; the interface gets out of its own way.

The only moment of designed movement is the portfolio thumbnail grid, where nav-items switch between a light-grey resting state (`#f2f2f2`) and a fully inverted black state on hover. No easing, no interpolation — just a hard binary flip that feels confident rather than crude.

---

## 2. Color Palette & Roles

### Foundation
| Role | Value | Usage |
|---|---|---|
| Canvas | `#ffffff` | Page and section backgrounds |
| Primary text | `#000000` | All body text, headings, borders |
| Muted text | — | Not present — binary black/white only |

### Interactive
| Role | Value | Usage |
|---|---|---|
| Nav item resting | `#f2f2f2` | Unselected portfolio thumbnail background |
| Nav item active | `#000000` | Selected thumbnail — full inversion |
| Active text | `#ffffff` | Text inside active/selected nav item |
| Focus ring | `rgb(0,95,204)` | Browser-default focus outline (unoverridden) |

What is conspicuously absent: no brand accent colour, no blue links, no grey hierarchy. The colour system is binary by design.

---

## 3. Typography Rules

Inter is the sole typeface. Sizes are unusually small by modern standards — the body baseline is 12px, paragraph/link text at 13px — suggesting this site is designed for a desktop audience comfortable with information density.

| Selector | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| Body | Inter | 12px | 400 | 14.4px (1.2) |
| Paragraph | Inter | 13px | 400 | 15.6px (1.2) |
| Link / anchor | Inter | 13px | 400 | 15.6px (1.2) |

Line height is a consistent 1.2 ratio across all sizes — tight, editorial, deliberate. No letter-spacing adjustments. No weight variation. No uppercase. Typography achieves hierarchy purely through size differences and spatial separation, not weight or colour.

---

## 4. Component Styling

**Portfolio thumbnails (nav-items)** are the primary component. They sit in a grid with `gap: 4px` between items and `margin-bottom: 60px` between sections. Each thumbnail:
- Default: `#f2f2f2` background, black text
- Hover: `#000000` background, white text (hard inversion, no transition)
- Active: `#000000` background, white text (persistent)
- Focus: browser-default blue outline ring (`rgb(0,95,204)`)

**Border radii**: Two values only — `4px` (inputs, compact elements) and `70px` (pill badges or tags). The jump from 4px to 70px with nothing in between suggests a strict two-tier shape system: either sharp-cornered or fully pill.

**Shadows**: None. Zero. Not even a 1px input shadow. The visual flatness is absolute.

---

## 5. Layout Principles

Main content uses minimal padding: `4px 5px 4px 4px` — barely a hairline inset. The asymmetry (5px right vs 4px elsewhere) may be a pixel-rounding artifact or intentional optical balance. Sections use `margin-bottom: 60px` to create breathing room between content groups, with `gap: 4px` inside grids. The tight inner padding combined with generous inter-section margin creates a rhythm of "dense cluster → white pause → dense cluster."

Two breakpoints at 498px and 959px suggest a three-tier responsive strategy (mobile / tablet / desktop).

---

## 6. Depth & Elevation

This system has no elevation model. There are no shadows, no blurs, no layered surfaces. All elements sit on the same flat plane. The only sense of depth comes from the black/white inversion on hover, which creates a visual foreground/background flip without any spatial metaphor. Depth is semantic (selected vs. not) rather than physical.

---

## 7. Do's and Don'ts

**Do:**
- Use hard binary hover states (no transitions) — the aesthetic depends on instant feedback
- Keep type small and tight (12–13px, 1.2 line-height) — the site is designed for density
- Maintain the 60px inter-section margin as the sole spacing gesture of significance
- Allow browser-default focus rings to show — accessibility is handled by native behaviour without custom overrides

**Don't:**
- Add any accent colour — the binary palette is the entire identity
- Introduce shadows or elevation — flatness is structural, not accidental
- Use font weights above 400 — weight variation is entirely absent
- Scale Inter above ~16px for body text — the micro-size choice is intentional

---

## 8. Responsive Behavior

Three tiers: mobile (< 498px), tablet (498–959px), desktop (> 959px). The `gap: 4px` thumbnail grid likely shifts from multi-column on desktop to fewer columns or single-column on mobile. Main padding collapses (already minimal). The 12–13px type sizes would benefit from a modest scale-up on mobile, though no CSS override was captured.

---

## 9. Agent Prompt Guide

> Build a portfolio grid in the style of yevhenyurchuk.com. Pure white canvas, pure black text. Single font: Inter at 12–13px / weight 400 / 1.2 line-height. No letter-spacing. No accent colours. Portfolio items are thumbnail links with a `#f2f2f2` default background that hard-inverts to `#000000` with white text on hover — no CSS transition, instant swap. Grid gap: `4px`. Inter-section margin: `60px`. No shadows anywhere. Border radius: either `4px` or `70px` — nothing in between. Focus rings use browser defaults. The typography creates all hierarchy; the hover state creates all interaction feedback.

---

*Generated by Sparkbites — extracted from live CSS analysis*
