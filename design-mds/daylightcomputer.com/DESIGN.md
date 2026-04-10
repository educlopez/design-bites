# DESIGN.md — daylightcomputer.com

## 1. Visual Theme & Atmosphere

Daylight Computer's site evokes warmth, intentionality, and a philosophy of calm computing. The palette is rooted in natural, earthy tones — warm creams, olive darks, and a single amber accent — that feel organic against the sterile backgrounds typical of tech hardware brands. This is a product positioned against digital overstimulation, and the design embodies that: no blues, no saturated tech colors, no hard whites. The typographic pairing of a custom ABC Arizona Flare serif with ABC Room sans creates a feeling of considered craft, like a boutique hardware journal rather than a consumer electronics page. The signature amber CTA button literally glows on hover through a box-shadow bloom effect — subtle theatre in an otherwise restrained environment.

---

## 2. Color Palette & Roles

### Body & Text
- **Olive Black** (`rgb(23, 25, 15)` = `#17190f`): The primary text color. Not gray, not pure black — a dark olive that leans warm and organic. Used across all body copy.
- **Warm White** (`rgb(250, 245, 242)` = `#faf5f2`): Secondary surface and text on dark backgrounds. A cream rather than white.

### Backgrounds
- **Dark Olive** (`rgb(24, 25, 15)`): Footer and primary dark surface. Matches the olive black text family — the entire dark system is olive-shifted.
- **Muted Cream** (`rgb(250, 245, 242)`): Main light card surfaces. The site's default light background is cream, not white.
- **Frosted Nav** (`rgba(232, 222, 216, 0.8)`): Navigation bar with 80% opacity warm blush — a frosted glass effect rooted in the warm palette.
- **Olive Overlays** (`rgba(67, 70, 38, 0.9)`, `rgba(39, 40, 25, 0.9)`, `rgba(88, 91, 61, 0.9)`): Dark olive overlay surfaces for image-over-text zones. All deep, all olive-green in hue.

### Accent
- **Amber** (`rgb(255, 157, 0)` = `#ff9d00`): The single chromatic accent. Used exclusively on the primary CTA button. On hover, emits an amber glow via `box-shadow: rgba(249, 157, 4, 0.565) 0px 0px 15.7px 0px`.

### Borders
- **Light Gray** (`rgb(229, 231, 235)` = `#e5e7eb`): Standard border color — the only neutral-cool element in an otherwise warm system.

---

## 3. Typography Rules

**ABC Arizona Flare** (`__abcArizonaFlareFont`): A custom-licensed serif with optical character. Used for hero and display headings:
- H1 hero: 56px / 56px line-height, weight 300 (light) — editorial and spacious
- H2 display: 44px / 48px, weight 300 — maintains the lightness
- Secondary display: 27px / 34px, weight 500 — mid-weight for subheadings

The weight-300 serif at large sizes creates a refined, book-like aesthetic. The custom `--text-scale-*` CSS properties signal a fluid typography system scaling with viewport width.

**ABC Room** (`__abcRoomFont`): A custom sans-serif for all UI and body copy:
- Labels and nav: 16px, weight 500
- Body: 15px / 24px
- Small UI: 14px / 20px, weight 400
- Buttons: 14–16px weight 500

No monospace. No system fallback faces beyond the serif/sans-serif generic. The two ABC typefaces are the typographic identity — both custom, both warm in proportion.

The fluid type scale (`--text-scale-screen-max`, `--text-scale-screen-min`, `--text-scale-offset`) means sizes are not fixed — they grow and shrink continuously with viewport width.

---

## 4. Component Styling

- **CTA Button**: Amber fill (`#ff9d00`), dark olive text. On hover: amber glow bloom via box-shadow. The hover effect is the site's most expressive micro-interaction.
- **Navigation**: Frosted blush bar (`rgba(232,222,216,0.8)`) with `0.1` opacity border — clearly a backdrop-filter bar floating over content.
- **Cards**: Cream surfaces (`#faf5f2`) with olive dark text. Rounded at various radii inferred from Tailwind utilities.
- **Image overlays**: Three distinct olive-dark overlays for feature image zones — tonal depth without leaving the warm palette.
- **Border Radius**: Not explicitly listed in the data, suggesting Tailwind's default utility classes handle all radii.

---

## 5. Layout Principles

Tailwind CSS breakpoints inferred from the standard scale. The fluid type scale expands layout breathing room at larger viewports. The Shopify integration suggests an e-commerce purchase flow exists alongside the editorial content. Navigation uses a `nav-menu-addon` pattern, suggesting a hamburger or slide-out menu. Sections are full-width with centered content columns, typical of hardware product landing pages.

---

## 6. Depth & Elevation

The amber CTA button hover glow (`box-shadow: rgba(249,157,4,0.565) 0px 0px 15.7px 0px`) is the only explicit elevation effect. Otherwise, depth is achieved through:
- Olive dark overlays on image sections (the image bleeds through at ~10% opacity)
- The frosted nav bar creating a sense of floating above content
- Tonal warmth gradient from cream light surfaces to olive-dark footer

---

## 7. Do's and Don'ts

**Do:**
- Use the amber accent exclusively for the primary CTA. One glowing button per page.
- Keep the warm palette intact: olive blacks, cream whites, no grays, no cool blues.
- Use ABC Arizona Flare at weight 300 for display text. Heaviness kills the editorial quality.
- Apply the amber glow box-shadow on button hover — it is the signature interaction.
- Use the fluid type scale — static font sizes undermine the system's responsiveness.

**Don't:**
- Introduce cool-toned colors. Even borders are a warm gray.
- Use pure white (`#ffffff`) as a surface. The system uses cream (`#faf5f2`).
- Set the serif at weight 700+ — it is a light-weight editorial face.
- Add blue link colors or standard tech color accents.
- Flatten the olive dark footer — the warm dark anchor is essential to page rhythm.

---

## 8. Responsive Behavior

The `--text-scale-*` fluid type system means type scales continuously rather than snapping at breakpoints. The Tailwind-standard breakpoints handle layout reflow. Navigation converts to drawer/hamburger at mobile. The amber CTA should remain full-width on small screens. Cream and olive surfaces stack vertically without losing their tonal relationship.

---

## 9. Agent Prompt Guide

> Build a hardware product page matching daylightcomputer.com: warm cream background (`#faf5f2`), olive-black text (`#17190f`), olive-dark footer (`#18190f`). ABC Arizona Flare serif weight 300 for hero headlines (56px), ABC Room sans weight 500 for UI. Single amber CTA button (`#ff9d00`) with hover glow: `box-shadow: rgba(249,157,4,0.565) 0px 0px 16px 0px`. Frosted nav with `rgba(232,222,216,0.8)`. No blue tones. No pure white. Warm throughout.

---

*Generated by Sparkbites — extracted from live CSS analysis*
