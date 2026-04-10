# apple.com — Design System

## 1. Visual Theme & Atmosphere

Apple's web design language is the most systematized in the industry. Every token has a semantic name, every spacing value is calculated, and the entire system is built to support both light and dark modes without structural changes. The atmosphere is premium minimalism: white space as a material, typography as the primary visual element. There is an almost aggressive clarity — page backgrounds are pure white, text is near-black, and the single accent color (blue `#0066CC`) appears only where genuine action is invited. The design system (`sk-` prefix tokens) reads like a design language specification rather than a stylesheet.

## 2. Color Palette & Roles

**Backgrounds (semantic fills)**
- Primary: `rgb(255, 255, 255)` — white
- Secondary: `rgb(250, 250, 252)` — `--sk-fill-secondary`; barely-perceptible cool tint
- Tertiary: `rgb(245, 245, 247)` — `--sk-fill-tertiary`; for card surfaces
- Quaternary: `rgb(232, 232, 237)` — `--sk-fill-gray-quaternary`; dividers, borders

**Text hierarchy**
- Primary: `rgb(29, 29, 31)` — warm near-black (`--sk-body-text-color`)
- Secondary: `rgb(110, 110, 115)` — mid-grey
- Tertiary: `rgb(134, 134, 139)` — lighter grey

**Accent (action only)**
- Blue: `rgb(0, 113, 227)` — `--sk-fill-blue`; buttons, interactive elements
- Link blue: `rgb(0, 102, 204)` — `--sk-body-link-color`; text links
- Focus ring: `#0071E3`

**Status / contextual**
- Green: `rgb(3, 161, 14)` — success
- Red: `rgb(227, 0, 0)` — error/destructive
- Orange: `rgb(245, 99, 0)` — warning
- Yellow: `rgb(255, 224, 69)` — highlight

**Special surfaces**
- Nav (frosted): `rgba(250, 250, 252, 0.8)` with backdrop blur
- Dark nav variant: `#161617`
- Environmental teal/cream: `rgb(84,140,140)` / `rgb(246,246,238)` — product photography context colors

## 3. Typography Rules

Two SF Pro optical variants, used with precision:

**SF Pro Display** — for large type (28px+). Used for h1 (80px / 600 / -1.2px tracking), h3 (28px), h5 (24px), and large paragraph text (21px). The negative tracking on the hero (-1.2px) is characteristic of Apple's large-display typesetting.

**SF Pro Text** — for small, dense type. Used for body (17px / 400 / -0.374px), h2 (12px), h4 (14px), navigation, and links. Negative tracking persists even at small sizes — a deliberate Apple signature.

- **Body**: 17px / 400 / 25px line-height / -0.374px tracking — unusually generous for body copy
- **Hero h1**: 80px / 600 / 84px line-height / -1.2px — tall and tight
- **Buttons**: 18px / 300 — light weight, unusual for CTAs

The total absence of third-party typefaces is the strongest possible design statement: this system doesn't exist without the Apple ecosystem.

## 4. Component Stylings

**Navigation**: Frosted `rgba(250,250,252,0.8)` at 44px height. Sticky, with translucency effect. Dark variant for dark pages.

**Cards**: `rgb(245, 245, 247)` — tertiary fill. No visible shadows in base system; elevation through background color only.

**Buttons**: 18px / 300 weight — light and confident. Focus ring: `#0071E3` at `1px` offset.

**Links**: `rgb(0,102,204)` — distinguished from button blue, consistent with web convention but Apple-toned.

**Focus management**: Dedicated `--sk-focus-color`, `--sk-focus-offset`, and `--sk-focus-offset-container` tokens — accessibility is a first-class design consideration.

**Border radii**: Not prominently varied; system relies on Apple's platform conventions.

## 5. Layout Principles

Max content width: `1680px` with `90px` padding on large viewports (`--viewport-content-padding-lg`). Three breakpoints: 320px, 834px, 1024px. The layout system is fluid between breakpoints, not stepping.

The `--apps` specific tokens (`--more-apps-col: 8`, icon grids) show product-specific layout overrides layered onto the base system. This modularity is core to how Apple manages hundreds of pages with one system.

## 6. Depth & Elevation

Apple's web design deliberately avoids shadows. The four-step fill hierarchy (`white → secondary → tertiary → quaternary`) creates depth through lightness value alone. The frosted nav achieves depth through transparency, not shadow. This is a conscious aesthetic choice aligned with the flat-design era Apple popularized.

## 7. Do's and Don'ts

**Do**
- Use the semantic `sk-` fill tokens in order (primary → secondary → tertiary) for surface elevation
- Apply negative letter-spacing to all type; it's baked into every size
- Reserve blue exclusively for interactive/action elements
- Maintain 17px body text — do not drop below for legibility

**Don't**
- Use drop shadows; Apple's system doesn't
- Mix in non-system fonts; SF Pro is non-negotiable on Apple's own pages
- Use red, orange, or green for decoration; they're semantic status colors
- Deviate from the 1680px max-width container

## 8. Responsive Behavior

Three defined breakpoints: 320px (small), 834px (medium), 1024px (large). Viewport-specific variables adjust nav heights and content padding proportionally. The hero at 80px would likely scale to ~40–48px on mobile. The 8-column app grid (`--more-apps-col: 8`) probably halves or quarters on small screens.

## 9. Agent Prompt Guide

> Implement Apple.com's design system: white page, near-black text (`rgb(29,29,31)`), SF Pro Display for 28px+ headings with negative tracking, SF Pro Text for body at 17px. Single action accent blue (`rgb(0,113,227)`). Four surface levels for elevation via background fills — no drop shadows. Max-width 1680px, frosted nav at 44px. The design earns its premium feel through precision, not decoration.

---

*Generated by Sparkbites — extracted from live CSS analysis*
