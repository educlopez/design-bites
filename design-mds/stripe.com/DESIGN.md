# Stripe Design Language

## 1. Visual Theme & Atmosphere

Stripe's visual identity is a masterclass in what might be called **technical luxury** -- the rare intersection of engineering precision and editorial elegance. Where most fintech companies lean into corporate blues and bold weights to signal trustworthiness, Stripe does the opposite: it whispers. The entire typographic system rests on font-weight 300 for headlines, a choice so deliberately anti-conventional it becomes a signature. Light type on generous whitespace communicates the same quiet confidence as a Dieter Rams product -- nothing to prove, everything to show.

The palette reinforces this philosophy. There is no true black anywhere in the meaningful UI text hierarchy; the deepest tone is a midnight navy (`rgb(6, 27, 49)`) that softens contrast just enough to feel refined without sacrificing readability. The brand purple `#533AFD` -- an electric, slightly blue-shifted violet -- appears with surgical precision on interactive elements, never as decoration. Backgrounds stay overwhelmingly white or near-white (`rgb(248, 250, 253)`), creating a canvas where the vibrant accent colors of product illustrations (greens, oranges, purples) pop without competing with the interface chrome.

What's equally telling is what's *absent*. Zero CSS shadows were detected. Zero media query breakpoints. This isn't minimalism by omission -- it's a signal of Stripe's engineering architecture. Shadows and responsive logic almost certainly live in JavaScript-driven systems (the site runs on Next.js), keeping the CSS layer surgically clean. The result is a site that feels weightless, as if the interface floats rather than stacks.

---

## 2. Color Palette & Roles

### Brand & Interactive Colors

| Role | Hex | RGB | Context |
|------|-----|-----|---------|
| Brand Purple (Primary CTA) | `#533AFD` | `rgb(83, 58, 253)` | Links, primary buttons, accent borders |
| Purple Hover (Darkened) | `#2E2B8C` | `rgb(46, 43, 140)` | Link/button hover state |
| Purple Tint (Secondary Button) | `#E2E4FF` | `rgb(226, 228, 255)` | Secondary button background & border |
| Purple Soft (UI Button BG) | `#E8E9FF` | `rgb(232, 233, 255)` | Tertiary UI button background |
| Bar Chart Purple | `#7F7DFC` | `rgb(127, 125, 252)` | Billing bar data visualization |

### Neutral & Surface Colors

| Role | Hex | RGB | Context |
|------|-----|-----|---------|
| Deep Navy (Text/Border) | `#061B31` | `rgb(6, 27, 49)` | Button text, primary dark tone |
| Dark Section BG | `#0D1738` | `rgb(13, 23, 56)` | Dark mode feature sections |
| Pure White (Nav BG) | `#FFFFFF` | `rgb(255, 255, 255)` | Navigation, primary surfaces |
| Off-White (Footer/Surface) | `#F8FAFD` | `rgb(248, 250, 253)` | Footer, frosted panels (also at 45% opacity) |
| Card Border | `#E5EDF5` | `rgb(229, 237, 245)` | Bento card border containers |
| Heading Pill BG | `#E3ECF7` | `rgb(227, 236, 247)` | Heading badge/label backgrounds |

### Accent & Illustration Colors

| Role | Hex | RGB | Context |
|------|-----|-----|---------|
| Hero Headline Green | `#81B81A` | `rgb(129, 184, 26)` | h1 headline accent color |
| Success Green | `#00D66F` | `rgb(0, 214, 111)` | Checkout instant button |
| Accent Orange | `#FF6118` | `rgb(255, 97, 24)` | Terminal transaction text |
| Orange Tint | `#FFE0D1` | `rgb(255, 224, 209)` | Terminal transaction background |
| Deep Green (Container) | `#003724` | `rgb(0, 55, 36)` | Book of the week image container |

### Surface Luminance Scale

| Surface | Background | Luminance |
|---------|-----------|-----------|
| Navigation | `rgb(255, 255, 255)` | 1.000 |
| Browser Graphic (frosted) | `rgba(248, 250, 253, 0.45)` | 0.979 |
| Card Border | `rgb(229, 237, 245)` | 0.924 |
| Terminal Button | `rgb(255, 224, 209)` | 0.908 |
| Billing Bar | `rgb(127, 125, 252)` | 0.549 |
| Checkout Button | `rgb(0, 214, 111)` | 0.542 |
| Book Container | `rgb(0, 55, 36)` | 0.143 |
| Dark Section | `rgb(13, 23, 56)` | 0.093 |

---

## 3. Typography Rules

### Type Hierarchy

| Element | Font Family | Size | Weight | Line Height | Letter Spacing | Feature Settings |
|---------|-------------|------|--------|-------------|----------------|------------------|
| h1 | sohne-var, "SF Pro Display", sans-serif | 48px | 300 | 55.2px (1.15) | -0.96px | `"ss01"` |
| h2 | sohne-var, "SF Pro Display", sans-serif | 32px | 300 | 35.2px (1.10) | -0.64px | `"ss01"` |
| h3 | sohne-var, "SF Pro Display", sans-serif | 26px | 300 | 29.12px (1.12) | -0.26px | `"ss01"` |
| h4 | sohne-var, "SF Pro Display", sans-serif | 16px | 400 | 22.4px (1.40) | normal | `"ss01"` |
| p | sohne-var, "SF Pro Display", sans-serif | 32px | 300 | 35.2px (1.10) | -0.64px | `"ss01"` |
| body | sohne-var, "SF Pro Display", sans-serif | 16px | 400 | normal | normal | `"ss01"` |
| a | sohne-var, "SF Pro Display", sans-serif | 16px | 400 | normal | normal | `"ss01"` |
| button | sohne-var, "SF Pro Display", sans-serif | 14px | 400 | 14px (1.00) | normal | `"ss01"` |

### Typographic Principles

**The sohne-var Identity.** Stripe commissioned *sohne-var*, a custom variable font from Klim Type Foundry, as the singular typeface across their entire product and marketing. There is no secondary font, no serif pairing, no monospace accent in the marketing layer. This mono-font strategy is a brand decision: one voice, no switching cost, total consistency. The `"SF Pro Display"` fallback ensures Apple device users see a harmonious alternative before the web font loads.

**Weight 300: The Signature Move.** Headlines (h1, h2, h3) and even large paragraph text all use weight 300 -- light. This is profoundly unusual. The vast majority of marketing sites use 600-700 for headlines to create visual hierarchy through mass. Stripe creates hierarchy through *size and negative letter-spacing* instead. The result reads like editorial design: think Wallpaper* magazine, not a SaaS homepage. It signals that the brand is confident enough to not shout.

**OpenType ss01: Stylistic Set 01.** Every single text element carries `font-feature-settings: "ss01"`. This OpenType feature activates an alternate glyph set within sohne-var -- subtle letterform variations that distinguish Stripe's typographic voice from anyone else who might license the base Sohne family. It's the typographic equivalent of a monogram.

**Tight Tracking, Loose Leading.** Headlines use aggressive negative letter-spacing (-0.96px at 48px, -0.64px at 32px, -0.26px at 26px), pulling characters closer together for a dense, modern feel. But line-height ratios stay generous (1.10-1.15), ensuring multi-line headlines breathe. This tension -- tight horizontally, open vertically -- is a hallmark of contemporary Swiss-influenced design.

**Scale Progression.** The type scale moves 48 > 32 > 26 > 16 > 14. Note the jump from h3 (26px) to h4 (16px) -- a deliberate gap that creates a clear separation between display type (the light, tracked headlines) and body type (the regular-weight utility text). The large paragraph size (32px) at weight 300 suggests hero subheadings styled as `<p>` rather than heading elements.

---

## 4. Component Stylings

### Buttons

**Primary CTA (`a.hds-button`)**

| State | Background | Text Color | Border |
|-------|-----------|------------|--------|
| Default | `#533AFD` / `rgb(83, 58, 253)` | `#FFFFFF` | `#FFFFFF` |

The primary CTA is a solid brand purple button with white text. The site's radius scale (4-6px) suggests a tight, barely-rounded rectangle -- not the fully-rounded buttons trending elsewhere. This restraint is deliberate: rounded rectangles feel more engineered, more controlled.

**Secondary CTA (`a.hds-button` variant)**

| State | Background | Text Color | Border |
|-------|-----------|------------|--------|
| Default | `#E2E4FF` / `rgb(226, 228, 255)` | `#533AFD` / `rgb(83, 58, 253)` | `#E2E4FF` |

The secondary button inverts the relationship: purple tint background with purple text. The border matches the background, creating a flat, borderless appearance. This ghost-button approach maintains hierarchy without introducing new colors.

**UI Button (`button.hds-ui-button`)**

| State | Background | Text Color | Border |
|-------|-----------|------------|--------|
| Default | `#E8E9FF` / `rgb(232, 233, 255)` | `#000000` | `#000000` |

Utility buttons use an even lighter purple tint with black text -- clearly tertiary in the visual hierarchy.

### Border Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| radius-sm | 4px | Tight containers, inputs, compact UI |
| radius-md | 5px | Mid-size cards, secondary elements |
| radius-base | 6px | Primary cards, buttons, modals |

The radius scale is remarkably compressed: only 2px separates the smallest from the largest value. This near-uniform rounding creates a consistent, engineering-precise feel. There are no large radii (12px+, 999px) -- Stripe avoids the playful, fully-rounded aesthetic entirely.

### Interactive States

**Links (`a.hds-link`)**

| State | Color | Border Color | Opacity | Box Shadow | Transform |
|-------|-------|-------------|---------|------------|-----------|
| Default | `#533AFD` / `rgb(83, 58, 253)` | `#533AFD` | 1.0 | none | none |
| Hover | `#2E2B8C` / `rgb(46, 43, 140)` | `#2E2B8C` | 0.6 | none | none |
| Focus | *Not captured* | -- | -- | -- | -- |

Link hover behavior is notable: the color shifts from bright purple to a deep indigo *and* opacity drops to 0.6. This double-dimming creates a pronounced but elegant state change. The lack of transform on hover (no translateY, no scale) reinforces the restrained, no-gimmick philosophy.

### Product Illustration Components

| Component | Background | Text Color | Role |
|-----------|-----------|------------|------|
| Terminal transaction button | `#FFE0D1` | `#FF6118` | Orange warm accent |
| Checkout instant button | `#00D66F` | `#000000` | Green success/action |
| Billing plan bar | `#7F7DFC` | `#000000` | Indigo data visualization |
| Heading badge (`h4.hds-heading`) | `#E3ECF7` | `#FFFFFF` | Blue-gray label |

---

## 5. Layout Principles

### Spacing System

| Element | Padding | Margin | Gap |
|---------|---------|--------|-----|
| body | 0px | 0px | normal |
| main | 0px | 0px | normal |
| section | 16px | 0px | 8px |
| header | 0px | 0px | normal |
| footer | 0px 16px | 0px | normal |

### Whitespace Philosophy

**Zero-margin architecture.** Every structural element (body, main, header, footer) uses 0px margin. Spacing is controlled exclusively through padding and flex/grid gaps, not margin collapse. This is a modern CSS best practice that eliminates the unpredictable behavior of margin collapsing and signals a component-driven spacing model where each module manages its own whitespace.

**Horizontal consistency.** Footer padding (`0px 16px`) matches section padding (16px), suggesting a 16px base horizontal unit at the viewport edge. Internal spacing likely multiplies from this base (16, 32, 48, 64, 80).

**Component-driven density.** The extracted values (16px section padding, 8px section gap) represent the structural skeleton. Stripe's actual component spacing is almost certainly more elaborate, managed through JavaScript-driven or CSS-in-JS approaches. The intentionally minimal CSS layer reinforces the philosophy of component encapsulation.

**The luxury of emptiness.** Stripe's homepage is defined as much by what isn't there as by what is. Content is constrained to roughly 1080-1200px with substantial side margins. The whitespace *is* the design -- it creates the perception of luxury that dense, information-packed fintech competitors lack.

---

## 6. Depth & Elevation

### The Absence of Shadows

Zero CSS shadows were detected across the entire Stripe homepage. This is one of the most revealing data points in the extraction.

This doesn't mean Stripe's interface is flat -- far from it. The homepage features layered card compositions, floating UI mockups, and dimensional product illustrations. But depth is achieved through:

1. **Background color contrast** rather than drop shadows -- white cards on `#F8FAFD` off-white surfaces
2. **Border differentiation** using the subtle blue-gray `#E5EDF5`
3. **Translucent overlays** -- the browser graphic window uses `rgba(248, 250, 253, 0.45)`, a frosted-glass effect without shadow geometry
4. **JavaScript-driven visual effects** (gradients, animations, WebGL) that don't appear in static CSS shadow declarations
5. **Illustration and imagery** that create perceived depth through visual design rather than CSS elevation

Stripe's famous multi-layer shadows (like `rgba(50, 50, 93, 0.25) 0px 50px 100px -20px`) are a hallmark of their *product UI* (Dashboard, Checkout, Elements). The marketing homepage achieves dimensionality through composition rather than box-shadow stacking, keeping the CSS footprint minimal and the visual approach more editorial.

### Elevation Strategy

| Level | Technique | Example |
|-------|-----------|---------|
| Ground | White/off-white backgrounds | Main content areas (`#FFFFFF`) |
| Raised | Blue-tinted border fill (`#E5EDF5`) | Bento cards (`.modular-solutions-bento-card__border`) |
| Floating | Semi-transparent surfaces | Browser graphic (`rgba(248, 250, 253, 0.45)`) |
| Dramatic | Dark background contrast | Dark mode sections (`#0D1738`) |

---

## 7. Do's and Don'ts

### Do's

1. **Do use weight 300 for display text.** Headlines, hero copy, and large paragraphs should feel light and editorial. Reserve weight 400 for body copy and UI elements only.
2. **Do activate OpenType `ss01`** on all text elements. This is non-negotiable for achieving Stripe's typographic character with sohne-var.
3. **Do use deep navy (`#061B31`) instead of pure black** for text. The subtle warmth prevents the harsh contrast of `#000000` on white, reducing eye strain and adding sophistication.
4. **Do keep border radii between 4-6px.** Stripe's corners are barely rounded -- precise, not playful. Avoid fully-rounded pills or sharp 0px corners.
5. **Do use the brand purple (`#533AFD`) exclusively for interactive elements** -- links, CTAs, and active states. Never as background fills for large areas (use the purple tints `#E2E4FF` / `#E8E9FF` instead).
6. **Do create depth through background color and borders** rather than box-shadows on the marketing layer. Let surfaces differentiate through subtle luminance shifts.
7. **Do apply negative letter-spacing to headlines** proportionally: -0.96px at 48px, -0.64px at 32px, -0.26px at 26px (roughly -2% of font size).

### Don'ts

1. **Don't use bold (600-700) weights for headlines.** This single mistake will destroy the Stripe aesthetic faster than anything else. Weight 300 is the identity.
2. **Don't introduce secondary typefaces.** No serif accents, no monospace for "technical" feel, no display fonts for hero sections. sohne-var does everything.
3. **Don't use pure black (`#000000`) as a primary text color.** The deep navy hierarchy (`#061B31` for primary, lighter values for secondary) is essential to the refined palette.
4. **Don't add large border radii (12px+) or fully rounded corners.** The 4-6px range is deliberate. Larger radii make the design feel consumer/playful rather than technical/professional.
5. **Don't rely on opacity alone for hover states.** Stripe combines color shift (to `#2E2B8C`) *and* opacity reduction (0.6) for link hovers -- both are needed for the effect to feel intentional.
6. **Don't use the accent colors (green, orange) in UI chrome.** These are strictly for product illustrations and data visualization. Interface elements stay in the purple-navy-white palette.
7. **Don't crowd the layout.** If it doesn't feel like there's "too much" whitespace, there isn't enough. Stripe's density is closer to a magazine spread than a SaaS dashboard.

---

## 8. Responsive Behavior

### Breakpoint Strategy

Zero CSS media query breakpoints were detected. This is characteristic of Stripe's architecture:

1. **JavaScript-driven responsiveness.** Built on Next.js, Stripe handles viewport adaptation through React component logic, CSS-in-JS conditional styles, or container queries rather than traditional `@media` breakpoints in stylesheets.

2. **Fluid typography.** While the extracted values show fixed pixel sizes (48px, 32px, 26px), these are computed values at the captured viewport width. The actual implementation likely uses `clamp()` or viewport-relative units for smooth scaling.

3. **Component-level adaptation.** Rather than global breakpoints that reflow the entire page, individual components (the bento grid, the product graphics, the navigation) manage their own responsive behavior independently.

### Recommended Responsive Implementation

| Viewport | Suggested h1 Size | Suggested Body | Layout Strategy |
|-----------|-------------------|----------------|-----------------|
| < 640px | 28-32px | 16px | Single column, stacked sections |
| 640-1024px | 36-40px | 16px | Two-column grids, condensed bento |
| 1024-1440px | 48px | 16px | Full layout as extracted |
| > 1440px | 48-56px | 16px | Max-width container, centered |

### Tech Stack

| Property | Value |
|----------|-------|
| Framework | Next.js (detected) |
| Implication | Server-side rendering, React component architecture, likely CSS Modules or styled-components |

---

## 9. Agent Prompt Guide

### Quick Reference

| Property | Value |
|----------|-------|
| Primary Font | `sohne-var, "SF Pro Display", sans-serif` |
| Font Feature | `font-feature-settings: "ss01"` |
| Headline Weight | 300 (light) |
| Body Weight | 400 (regular) |
| Brand Purple | `#533AFD` |
| Text Color (Primary) | `#061B31` (deep navy) |
| Surface White | `#F8FAFD` |
| Card Border | `#E5EDF5` |
| Border Radius | 4-6px |
| Shadow Strategy | None in CSS (depth via color/borders) |
| Link Hover | Color shift to `#2E2B8C` + opacity 0.6 |

### Example Prompts

**Landing Page Hero:**

> Create a hero section in the Stripe style: sohne-var font at 48px weight 300 with -0.96px letter-spacing and font-feature-settings "ss01". Use a vivid green (#81B81A) for the headline color against a white background. CTA button in solid #533AFD with white text at 14px weight 400, border-radius 6px. Generous vertical padding (120px+). No shadows anywhere.

**Product Feature Card:**

> Build a bento-grid feature card like Stripe's homepage. White background, 1px border in #E5EDF5, border-radius 6px. Title at 26px weight 300 in deep navy #061B31 with -0.26px letter-spacing. Body text at 16px weight 400. Internal padding of 32-48px. No box-shadow -- elevation comes from the border and background contrast against an #F8FAFD page surface. All text uses sohne-var with font-feature-settings "ss01".

**Navigation Bar:**

> Design a Stripe-style navigation: white background (#FFFFFF), no shadow, no border. Logo left-aligned, nav links at 16px weight 400 in #061B31. Link hover transitions to #2E2B8C at 0.6 opacity. Primary CTA button in #533AFD with white text, border-radius 6px. Total height roughly 64px. Font: sohne-var with ss01.

**Dark Section:**

> Create a dark feature section with background #0D1738 (Stripe's deep navy). Headlines in white at 32px weight 300 with -0.64px letter-spacing. Use #7F7DFC (soft purple) for data visualization elements and #00D66F for success indicators. Secondary button with #E2E4FF background and #533AFD text. All text uses sohne-var with font-feature-settings "ss01". Zero shadows.

**Button System:**

> Implement a three-tier button system: Primary is solid #533AFD background with white text. Secondary is #E2E4FF background with #533AFD text and matching border. Tertiary is #E8E9FF background with black text. All at 14px weight 400, border-radius 4-6px, no shadows. Hover on links shifts color to #2E2B8C and opacity to 0.6.

---

*Generated by Sparkbites -- extracted from live CSS analysis*
