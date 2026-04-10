# bygideon.com — Design System Reference

## 1. Visual Theme & Atmosphere

bygideon.com makes an unusual and highly intentional typographic statement: a geometric display serif (Mondwest) for headings paired with JetBrains Mono — a programming font — for every other element. Body text, navigation, buttons, code, and paragraphs all share the same monospaced face. This creates a deeply developer-native, typewriter-meets-art-direction sensibility. The background is a flat mid-grey (`#e6e6e6`) — not white, not dark — giving the page a matte, paper-over-concrete quality. The sole chromatic accent is a vivid orange (`#ff7b42`) that appears as a full surface fill, not a button or badge. There are no shadows, no border radii, no rounded shapes of any kind. The design is raw, confident, and typographically singular.

## 2. Color Palette & Roles

| Role | Value | Usage |
|------|-------|-------|
| Page background | `rgb(230, 230, 230)` | Body — flat mid-grey |
| Near-white surface | `rgb(243, 243, 245)` | Light card fill |
| Warm off-white | `rgb(242, 239, 233)` | Alternate surface tone |
| White | `rgb(255, 255, 255)` | Brightest surface layer |
| Light grey | `rgb(204, 204, 204)` | Structural dividers, secondary surfaces |
| Mid grey | `rgb(179, 179, 179)` | Fine lines, progress bars |
| Orange accent | `rgb(255, 123, 66)` | Hero/feature block fill — sole chromatic hue |
| Dark grey | `rgb(77, 77, 77)` | Dark surface / secondary panel |
| Near-black | `rgb(51, 51, 51)` | Deep dark surfaces |
| Very dark | `rgb(26, 26, 26)` | Darkest containers |
| Black | `rgb(0, 0, 0)` | Pure black elements |
| Body text | `rgb(18, 18, 18)` | Near-black text throughout |
| Code text | `rgb(255, 255, 255)` | White text on dark/code backgrounds |

The system spans a wide greyscale from mid-grey body to near-black panels, with a single vivid orange (`#ff7b42`) as the only chromatic element. This restraint amplifies the orange dramatically when it appears.

## 3. Typography Rules

**Display typeface:** `mondwest` — a geometric serif with architectural, constructed letterforms. Used only for H1 at maximum scale.

**UI/body typeface:** `jetbrains_mono` — a monospaced typeface designed for code editors. Used for absolutely everything else: body, paragraphs, links, buttons, code, pre.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| H1 (Mondwest) | 96px | 400 | 96px | +0.45px |
| Body / UI (JetBrains Mono) | 18px | 400 | 27px | +0.45px |

The H1 is set at 1:1 size-to-line-height (96px/96px) — a tight, display-block headline with no leading. Positive letter-spacing (+0.45px) appears at both scales, giving the monospaced body text its characteristic spaced, typewriter rhythm. Weight variation is entirely absent — 400 throughout. Only size and typeface family carry the hierarchy.

## 4. Component Stylings

**Buttons:** Transparent background, near-black text (`#121212`), no border-radius (sharp corners throughout). No hover states detected in computed styles — the system relies on cursor changes or custom JS interactions.

**Links:** Same as buttons — monospaced, 18px, transparent, sharp-cornered.

**Code blocks:** White text (`#ffffff`) on dark/transparent background — the typeface is already code-native so no extra styling is needed.

**Orange accent block:** Appears as a full `div.flex` container fill (`rgb(255,123,66)`) — a structural section background, not a button. Text on it is near-black (`#121212`) for contrast.

**Borders:** No custom border styling detected. The `lab(91.6229 -0.159115 -2.26791)` border color is computed (approximately a warm light grey) from Tailwind's default border utilities.

## 5. Layout Principles

No breakpoints detected — this may be a single-column layout or breakpoints exist only in Tailwind utility classes. No border-radius values at all — every element is sharp-cornered. The page canvas (`#e6e6e6`) doesn't extend to white, creating a deliberate grey-on-grey print texture. Spacing follows Tailwind defaults without customisation. The wide greyscale surface palette (11 distinct tones from white to black) suggests a deliberately zoned layout where sections are differentiated by fill rather than borders.

## 6. Depth & Elevation

No shadows. No rounded corners. Depth is created entirely through the **greyscale surface progression** — from white (`#fff`) at the top to pure black (`#000`) at the base, with multiple intermediate tones creating visual layering. The orange block cuts through the greyscale as a pure chromatic pop, creating the highest contrast moment on the page. This is a zone-based layout: areas are distinguished by background fill, not elevation cues.

## 7. Do's and Don'ts

**Do:**
- Use JetBrains Mono for all body-level text — the monospaced rhythm is the site's identity
- Reserve Mondwest exclusively for H1 display text at large scale (80px+)
- Apply the orange (`#ff7b42`) as a full-section background fill, not a button or badge
- Use the wide greyscale palette to create section zones — at least 3–4 distinct grey values per layout
- Keep all corners sharp — zero border-radius is a defining characteristic

**Don't:**
- Round any corners — pills, rounded cards, or circular avatars would break the system entirely
- Add shadows — the flat zone-based layout has no elevation metaphor
- Introduce a second accent colour — the orange is a singular, intentional punctuation
- Use any sans-serif or serif typeface other than Mondwest/JetBrains Mono
- Apply weight variation — Regular (400) throughout is the intended design

## 8. Responsive Behavior

No media query breakpoints were detected in the extracted CSS. The system either relies entirely on Tailwind responsive utilities (applied at build time, not computed), or is a largely fixed layout. Given the 96px H1 and wide grey palette, mobile adaptation would require significant type scale reduction and layout reflow. Assume single-column stacking on mobile with reduced H1 size.

## 9. Agent Prompt Guide

> "Design in the style of bygideon.com: flat mid-grey canvas (`#e6e6e6`), Mondwest geometric serif for H1 at 96px/96px with sharp no-leading block. JetBrains Mono for all UI text at 18px/27px. Zero border-radius — every edge is sharp. Single vivid orange (`#ff7b42`) as a full-section fill accent. Wide greyscale palette (white through black) creates section differentiation — no shadows, no borders between zones. No hover states, no colour changes on interaction. Raw, developer-native, typographically singular."

---

*Generated by Sparkbites — extracted from live CSS analysis*
