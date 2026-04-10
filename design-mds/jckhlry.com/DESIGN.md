# jckhlry.com — Design System

## 1. Visual Theme & Atmosphere

jckhlry.com is a Framer-built portfolio that commits to a radical typographic gesture: **Geist Mono at 12px, uppercase, as the H1**. There is no display scale, no hero font at 72px — the name and primary identity are rendered in a monospace label at exactly the same size as body text. The atmosphere is deliberately anti-decorative: pure white canvas, pure black ink, no accent color, no gradients, no shadows, no border radius. What remains is negative space, structure, and the conceptual weight of choosing a developer monospace font as a design statement. The Framer Motion layer likely provides the kinetic quality that static CSS cannot convey here.

## 2. Color Palette & Roles

**Total palette:**
- `rgb(255, 255, 255)` — canvas and only background color
- `rgb(0, 0, 0)` — all text; H1, body ink
- `rgb(0, 0, 238)` — browser-default link blue; present but likely unstyled by choice
- `rgba(0, 0, 0, 0)` — transparent link/button backgrounds

**What is absent:** no brand hue, no grey scale, no tinted surfaces, no dark mode. The two-color palette (`#fff` / `#000`) is the design.

## 3. Typography Rules

Geist Mono for headings and all identity-layer text; browser-default sans-serif for body and links. The deliberate use of a monospace fallback for body text (`sans-serif` generic) suggests body text is minimal or the Framer components provide their own typography.

| Role | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H1 (identity) | Geist Mono | 12px | 500 | Uppercase; `lh: 9.6px` — tighter than size |
| Body | sans-serif | 12px | 400 | Framer shell default |
| Links | sans-serif | 12px | 400 | Unstyled |

The H1 line-height of `9.6px` is actually smaller than the `12px` font size — lines of text technically overlap. At uppercase, this may render as tightly-packed all-caps lettering that reads as a single visual block. The OpenType features enabled on Geist Mono (`"blwf"`, `"cv03"`, `"cv04"`, `"cv09"`, `"cv11"`) indicate careful character-level refinement: stylistic alternates and below-baseline form variants for specific glyphs.

Navigation items ("WORK", "PLAYGROUND") — also uppercase, likely also Geist Mono — dim to ~52% opacity on hover rather than changing color, creating a ghosting effect.

## 4. Component Stylings

**Navigation links** — Default full opacity, hover → `opacity: 0.52`. No color change, no transform, no underline. The opacity-fade is the sole interactive language.

**Surfaces** — One surface detected: `rgb(255, 255, 255)` at full luminance. No card components, no elevated panels, no inset sections. The page is a single plane.

**Border radii** — None detected. Zero radius everywhere — all corners are sharp right angles.

**Shadows** — None. Not even a `box-shadow: none` reset appears in extracted data.

**The absence is intentional:** no hover fills, no button styles, no card borders. Interaction happens through opacity and Framer Motion transitions.

## 5. Layout Principles

Framer breakpoints at `809.98px` (tablet) and `1199.98px` (desktop) — three layout modes: mobile, tablet, desktop. Body padding is zero. Layout is entirely driven by Framer's component system. The minimalism suggests large white space sections with sparse content, possibly portfolio project entries as a list or grid.

No custom spacing system detected — Framer handles all spacing internally.

## 6. Depth & Elevation

There is no elevation. One luminance level (`1.0` — pure white). No shadows, no dark panels, no transparent overlays. The only "depth" present is the conceptual depth of the opacity-fade hover state, which creates a figure-ground relationship between active and inactive navigation items.

This is a zero-elevation design — it exists entirely in 2D.

## 7. Do's and Don'ts

**Do**
- Use Geist Mono uppercase at 12px for identity/label text; that's the brand signature
- Enable OpenType features `"blwf"`, `"cv03"`, `"cv04"`, `"cv09"`, `"cv11"` on Geist Mono
- Express interaction exclusively through opacity: `1.0` active → `0.52` inactive/hover
- Let white space do structural work — no borders, no dividers

**Don't**
- Add a brand color — the two-color monochrome is the aesthetic statement
- Introduce rounded corners — sharp right angles are an intentional design choice
- Use shadows or elevation — the flat single-plane design is the concept
- Scale Geist Mono up for display; the deliberate small-scale identity is the point

## 8. Responsive Behavior

Three breakpoints: mobile (< 810px), tablet (810–1199px), desktop (> 1199px). Framer manages layout reflow. The 12px text remains legible at all sizes — it's not a display problem but a philosophical choice. On mobile, the navigation likely collapses. The work grid adapts from multi-column to single-column. The white space breathing room is preserved across breakpoints.

## 9. Agent Prompt Guide

> Build a minimal portfolio in the style of jckhlry.com. Pure white canvas (`#fff`), pure black text (`#000`). Geist Mono for all identity and label text at 12px/500/uppercase with OpenType features `"cv03", "cv04", "cv09", "cv11"`. Body in bare `sans-serif` at 12px. Zero border radius — all sharp corners. No shadows. No accent color. Navigation links fade to `opacity: 0.52` on hover — that is the only interaction state. No card surfaces, no elevated panels. Three Framer breakpoints: 810px and 1199px. All animation via Framer Motion.

---

*Generated by Sparkbites — extracted from live CSS analysis*
