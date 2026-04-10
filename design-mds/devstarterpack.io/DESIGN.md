# devstarterpack.io — Design Language

## 1. Visual Theme & Atmosphere

devstarterpack.io communicates utility over beauty. The aesthetic is clean, purposefully unadorned — a developer tool that earns trust by staying out of the way. The palette is almost entirely achromatic, anchored in pure white and near-black, with a single warm amber accent (`#FDDEB3`) that acts as a deliberate surprise — a signal of approachability inside an otherwise stark interface. There is no dark mode, no animation, no illustration. The site's honesty is its design statement: this is scaffolding for builders, so the interface itself behaves like good scaffolding.

The design philosophy is "functional warmth" — systematic enough to feel professional, warm enough not to feel cold.

## 2. Color Palette & Roles

**Foundation**
- `#FFFFFF` — Page background, card surfaces, primary canvas
- `#F5F5F5` / `#F3F3F3` — Secondary surfaces, section backgrounds, hover states
- `#171717` (9% opacity) — Ghost button fill; transparent depth without weight

**Text & Borders**
- `rgb(0, 0, 0)` — All body text, headings, icons; zero ambiguity
- `#E5E5E5` — Border color throughout; light enough to disappear, present enough to divide
- `rgb(0, 0, 0)` at 45% — Muted/secondary text (maps to `--muted-foreground`)

**Accent**
- `#FDDEB3` — Warm amber; used on a single highlight card/surface. Breaks the grey sequence deliberately. Do not dilute by repeating.

**Semantic (via shadcn tokens)**
- Destructive: `hsl(0, 84%, 60%)` — red, reserved for errors only
- Ring/focus: `rgb(0, 95, 204)` — system blue, accessibility only

The entire palette is constructed from HSL zero-saturation values except the amber accent. Colorlessness is a feature.

## 3. Typography Rules

A single typeface system: the OS native stack (`-apple-system`, `system-ui`, Roboto, Helvetica, Arial). No custom webfonts are loaded. This is a conscious performance and neutrality choice — the site renders in whatever the user's system prefers, reinforcing the "tool, not product" framing.

**Scale**
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| H1 | 30px | 600 | 1.0 (tight) |
| H3 | 28px | 600 | 32px |
| H5 | 18px | 600 | 28px |
| Body | 16px | 400 | 24px |
| Paragraph | 18px | 400 | 24px |

H1 line-height equals font-size (1.0), creating compact, confident headings. No letter-spacing adjustments — all tracking is `normal`, leaning into the naturalness of system fonts. Font feature settings are unset; no ligature tuning.

Hierarchy is established by weight (600 vs 400) and size alone — not color, not transform, not tracking.

## 4. Component Stylings

**Buttons**
Three states form a clear ladder: ghost (10% dark fill) → default active (100% `#171717` fill, white text) → hover (20% dark fill on ghost variant). Border-radius: 4px or 6px — small rounding that signals function without softness. No shadows on interactive elements.

**Cards / Surfaces**
Cards use `#F5F5F5` or `#F3F3F3` fills with `#E5E5E5` borders. Radius: 12px for container cards. The amber card (`#FDDEB3`) breaks the neutral surface sequence exactly once per section.

**Tags / Filter Pills**
Small text buttons at 14px, toggling between ghost and filled states. Active state is full dark fill (`#171717`) with white text. No icon, no decoration.

**Borders**
`--border: hsl(0 0% 89.8%)` applied universally. Consistent, never decorative.

## 5. Layout Principles

Built on Tailwind CSS with a standard 5-breakpoint grid (640 / 768 / 1024 / 1280 / 1536px). Sections use generous vertical padding: `80px` top/bottom with `16px` horizontal gutters at mobile. Section margin-bottom is `56px`, creating clear breathing room between content bands.

The layout is content-first and flex-based. No complex grid choreography — rows and columns that make sense. Header padding is compact (`20px` vertical), keeping navigation lightweight. Footer is minimal at `40px` vertical padding.

No max-width container is declared for the body itself; containment happens at the section level.

## 6. Depth & Elevation

Depth is essentially absent. No box shadows appear in the data — the interface is resolutely flat. Elevation is implied only through background color changes (white → light grey → amber). The `rgba(23, 23, 23, 0.1)` ghost button fill and its `0.2` hover counterpart are the closest this design gets to shadow — a subtle darkening that reads as depth without casting one.

Focus states reveal the only elevation-adjacent treatment: a `rgb(0, 95, 204)` outline, system-default. Not designed, not styled — delegated to the browser.

## 7. Do's and Don'ts

**Do**
- Use the achromatic palette as default; treat amber as a singular accent
- Keep heading weight at 600; avoid bold (700+) which would feel heavy against system fonts
- Use 4px / 6px radius on interactive elements, 12px on containers
- Respect the 80px section padding rhythm — don't compress it
- Let borders be `#E5E5E5` or nothing; avoid heavier strokes

**Don't**
- Add custom webfonts — system fonts are the design intent
- Use box-shadows for elevation; the design is intentionally flat
- Repeat the amber accent more than once per view
- Add dark mode variants — this is a single-mode design
- Use color for hierarchy; weight and size do that work

## 8. Responsive Behavior

Five breakpoints follow Tailwind defaults: 640 / 768 / 1024 / 1280 / 1536px. Section padding (`80px 16px`) implies the 16px gutter is the mobile baseline — wider gutters are inherited from container logic at larger breakpoints, not explicit overrides. The header compresses to `20px 16px` padding at all sizes.

No evidence of mobile-specific type scaling — sizes appear fixed across breakpoints. This is a common pattern for developer-tool sites that expect desktop-primary usage.

## 9. Agent Prompt Guide

> Build a UI in the style of devstarterpack.io: pure white canvas, system font stack (no webfonts), achromatic palette with a single warm amber (`#FDDEB3`) accent surface. All text is black or 45% grey. Borders are `#E5E5E5`. Buttons use 4–6px radius and toggle between 10% dark ghost fill and full `#171717` fill. No shadows. Sections have 80px vertical padding. Cards use 12px radius with `#F5F5F5` fill. Keep it flat, functional, and restrained. Only break the grey sequence with amber, and only once.

---

*Generated by Sparkbites — extracted from live CSS analysis*
