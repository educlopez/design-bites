# unroot.design — Design System

## 1. Visual Theme & Atmosphere

Unroot is a design agency or studio site built around a deep purple cosmological identity — dark indigo backgrounds, violet accents, and periwinkle blue blocks that together evoke something between a digital observatory and an independent design collective. The palette transitions from pale sky blue through violet to near-black navy, creating a sense of depth that feels cosmic without being cliché.

The typography pairs Recoleta (a warm retro-serif with ink-trap character) with Figtree (a clean geometric sans), creating a tension between the nostalgic and the contemporary. This dual-voice system is unusual and memorable: display type carries warmth and history, body copy carries clarity and modernity.

## 2. Color Palette & Roles

| Role | Token | Value | Usage |
|------|-------|-------|-------|
| **Deep canvas** | `div.n-section` bg | `rgb(29,4,102)` | Dark hero/section backgrounds |
| **Footer / deep** | `section.footer-wrapper` | `rgb(83,11,163)` | Footer surface — deep violet |
| **Violet accent** | `--accent-purple` | `#974bec` | Primary accent, interactive elements |
| **Strong violet** | `--violet-bg` | `#6402e1` | Hover states, bold accents |
| **Periwinkle blue** | `div.artifact-central-block` | `rgb(139,170,243)` | Featured content blocks |
| **Soft purple** | `div.projects-add-block` | `rgb(153,111,200)` | Secondary content blocks |
| **Light blue bg** | `e8f2ff` | `#e8f2ff` | Possibly light-mode section |
| **Text** | `rgb(255,255,255)` | White | All text on dark backgrounds |

The palette is a continuous purple-blue gradient expressed as discrete surfaces. No warm tones, no neutrals except white text. Color is the design system.

## 3. Typography Rules

**Display:** Recoleta — a revival serif with Art Deco-meets-1970s warmth, ink traps, and expressive curves.  
**Body/UI:** Figtree — a clean geometric sans-serif with friendly proportions.

| Selector | Size | Weight | Letter Spacing | Notes |
|----------|------|--------|----------------|-------|
| `h1` | ~45.5px | 400 | -2.32px | Recoleta; negative tracking on large sizes |
| `h2` | 68px | 400 | tight | Recoleta display; very large |
| Body | 20px | 400 | -0.4px | Figtree; comfortable reading |
| Nav links | 20px | 400 | -0.4px | Figtree; consistent with body |
| Tags | small | 400 | normal | Figtree small labels |

The negative letter-spacing on Recoleta at large sizes (-2.32px) is intentional — the typeface's wide letterforms need compression to feel designed rather than default. Figtree uses a slight -0.4px tracking throughout to feel snug.

**Notably absent:** No monospace, no ultra-bold weights, no uppercase text-transform despite the visual boldness of the color system.

## 4. Component Stylings

- **Artifact block** — periwinkle `rgb(139,170,243)` rectangular panel; likely a featured project showcase
- **Projects add block** — soft purple `rgb(153,111,200)` surface; secondary project card
- **Navbar links** — 20px Figtree, -0.4px tracking, white on transparent; space-efficient navigation
- **Tag wrapper** — `.div.tag-wrapper`; small pill labels, likely with purple background
- **Footer** — deep violet `rgb(83,11,163)` surface; full-width, high contrast
- **Motion variable** — `--moving-coefficient: 1.65` and `--video-move-vw: 209vw` suggest parallax or scroll-driven animations

## 5. Layout Principles

- Full-bleed section-based layout; each `div.n-section` is a viewport-spanning context
- The `209vw` movement value suggests horizontal scroll or wide parallax motion effects
- Content blocks (artifact, projects) likely arranged in asymmetric grid within sections
- No max-width token detected — likely full-viewport or very wide container
- Generous spacing between sections implied by the cosmic, unhurried atmosphere

## 6. Depth & Elevation

- **Color depth gradient** — `rgb(29,4,102)` (deepest) → `rgb(83,11,163)` → `rgb(153,111,200)` → `rgb(139,170,243)` creates a natural light-source-from-deep model
- **Motion as depth** — parallax (moving coefficient 1.65) creates Z-axis perception without static shadows
- White text at 100% opacity — no opacity gradations needed when contrast is already extreme
- No box shadows detected; the dark palette makes them invisible and unnecessary

## 7. Do's and Don'ts

**Do:**
- Use Recoleta exclusively for display sizes (h1, h2); never for body or UI text
- Pair every Recoleta heading with Figtree body copy for tonal balance
- Keep text white — no gray tones needed against these rich backgrounds
- Use the color-as-depth model: darker = deeper in hierarchy
- Apply negative tracking to Recoleta at large sizes (-2px at 68px)

**Don't:**
- Use Recoleta for small labels or UI elements — it breaks at tiny sizes
- Add warm or neutral tones to the palette; the entire identity is cool purple-blue
- Use the periwinkle or soft purple for text — they're background/surface colors only
- Introduce gradients; the flat-surface color system is deliberate

## 8. Responsive Behavior

No explicit breakpoints captured. The `209vw` motion value and viewport-filling sections suggest:

| Behavior | Context |
|----------|---------|
| Mobile | Single-column sections; motion effects likely disabled or reduced |
| Desktop | Full parallax / scroll-driven motion; wide asymmetric layouts |

The 68px H2 will need responsive scaling — `clamp()` or viewport-relative units assumed.

## 9. Agent Prompt Guide

> "Design in the style of unroot.design: deep indigo sections `rgb(29,4,102)`, violet footer `rgb(83,11,163)`, periwinkle featured blocks `rgb(139,170,243)`, soft purple cards `rgb(153,111,200)`, all text white, Recoleta serif for display headings with -2px letter-spacing, Figtree sans for body at 20px/-0.4px tracking, scroll-driven parallax motion, no warm tones, no shadows — cosmic design-studio aesthetic."

*Generated by Sparkbites — extracted from live CSS analysis*
