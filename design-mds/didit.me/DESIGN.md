# Didit — Design System Reference

Didit is identity and fraud infrastructure — one API, 25+ modules for KYC, KYB, AML, biometric auth, and wallet screening. The landing page is a polished, predominantly light developer-product site that reserves darkness for emphasis: the footer inverts to pure black and individual UI mock-ups render on deep charcoal surfaces so they read like real product screenshots against the white canvas. The overall register is clinical precision softened by warm micro-accents — a site that says "serious infrastructure" without the grey-on-grey monotony of older developer tools.

---

## 1. Visual Theme & Atmosphere

Didit operates in a light-dominant mode with a deliberate dual-register strategy. The primary experience is clean white (`rgb(255, 255, 255)` canvas, `rgb(249, 249, 249)` surface, `rgb(237, 237, 237)` elevated) lit by a single electric blue (`rgb(37, 103, 255)`) that acts as the sole chromatic engine. Then, at key moments — the footer, the dark demo blocks, the "Built for developers" code section — the page flips to near-black (`rgb(13, 13, 13)`) with white text, creating a full 180° luminance inversion that punctuates the scroll rhythm.

The product UI mocks embedded in the page are rendered on `rgba(40, 40, 40, 0.7)` overlays, making them feel like actual dashboard screenshots rather than flat illustrations. These dark surfaces anchor the page's sense of real, deployed software. Status indicators (green `rgb(16, 185, 129)`, red `rgb(255, 95, 87)`, amber `rgb(254, 188, 46)`) appear as colored dots inside these mocks — the only warm-spectrum color on the page, and only inside the product chrome.

The brand identity is built on precision, not personality. The typography does the heavy lifting; the rest of the page is light, ordered, and undecorated.

---

## 2. Color Palette & Roles

**Foundation (light mode)**
- `rgb(255, 255, 255)` — `--canvas`: page background, card backgrounds
- `rgb(250, 249, 245)` — `--cream`: warm off-white alternate surface
- `rgb(249, 249, 249)` — `--surface`: default card and section surface
- `rgb(237, 237, 237)` — `--elevated` / `--line`: borders, dividers, elevated surfaces
- `rgb(40, 40, 40)` — `--ink`: primary text color
- `rgb(93, 93, 93)` — `--muted`: secondary / subdued text
- `rgb(13, 13, 13)` — `--accent-black`: deepest surface, used in footer and dark code sections

**Accent**
- `rgb(37, 103, 255)` — `--blue`: CTA buttons, active states, focus rings, link highlights. A vivid electric blue — noticeably saturated against the neutral ground, which makes it effective at the single accent point it occupies.
- `rgb(27, 79, 224)` — `--blue-deep`: pressed / hover state of the primary blue
- `rgb(234, 241, 255)` — `--blue-soft`: tinted chip and badge backgrounds
- `rgb(247, 249, 255)` — `--blue-tint`: very pale blue wash for hover surfaces

**Status (used exclusively inside product UI mocks)**
- `rgb(230, 245, 236)` bg / `rgb(10, 125, 47)` fg — success
- `rgb(255, 247, 224)` bg / `rgb(154, 107, 0)` fg — warning
- `rgb(251, 233, 229)` bg / `rgb(182, 58, 46)` fg — danger
- `rgb(16, 185, 129)` — terminal-style "live" indicator dot
- `rgb(255, 95, 87)` — red traffic-light dot (macOS window chrome illusion)
- `rgb(254, 188, 46)` — amber traffic-light dot
- `rgb(40, 200, 64)` — green traffic-light dot

**Dark inversion (footer, code blocks)**
- `rgb(13, 13, 13)` bg / `rgb(255, 255, 255)` fg — full inversion
- `rgba(255, 255, 255, 0.1)` — border color on inverted surfaces

The system is monochromatic at the structural level and uses the blue exclusively for interaction affordances. Status colors and the green "live" dot are the only warm-spectrum touches and they are consciously contained within UI mocks.

---

## 3. Typography Rules

Didit commits to a single typeface system: **Inter** for all UI text, and **JetBrains Mono** for all code. The OpenType features `"cv11", "ss01"` are active across every Inter node — enabling Inter's alternate digit forms and contextual alternates, which gives the type a slightly more distinctive quality than default Inter rendering.

**Typefaces**
- **Inter** — the only UI face: display headlines, subheadings, body, buttons, navigation
- **JetBrains Mono** — code blocks, API snippets, terminal demos

**Scale**

| Role | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| H1 | 56px | 500 | 58.8px (1.05) | -1.4px |
| H2 | 44px | 500 | 50.6px (1.15) | -1.1px |
| H3 | 36px | 500 | 40px (1.11) | -0.9px |
| Body | 16px | 400 | 24px (1.5) | normal |
| Button | 16px | 700 | 24px (1.5) | normal |
| Code | 12px | 400 | 19.5px (1.625) | normal |

**Principles**
- A single weight axis covers most use cases: 400 for prose, 500 for display, 700 for button labels only. There is no intermediate semi-bold in the main hierarchy — the jump from 400 to 500 to 700 is intentional and clean.
- Aggressive negative tracking on display sizes: -1.4px at 56px, -1.1px at 44px, -0.9px at 36px. This creates tight headline blocks that read as single visual units — a developer-product convention that communicates precision.
- Body text sits at a conventional 16px/24px with tracking left at `normal` (`--tracking-body: -.011em` defined as a token but the live computed value is `normal`). Reading comfort is prioritized at body scale.
- `cv11` and `ss01` are the only OpenType features active. Code elements do not inherit them — JetBrains Mono renders at its default settings.
- The `--tracking-display: -.02em` token confirms the display negative-tracking is systematic, not incidental.

---

## 4. Component Stylings

**Buttons**
- Primary CTA: `rgb(37, 103, 255)` background, white text, 8px border-radius, `--shadow-md` (`0 6px 16px rgba(15, 23, 42, 0.1)`) plus a secondary blue glow shadow `rgba(37, 103, 255, 0.45) 0px 8px 24px -8px`. The glow shadow is a signature detail — it makes the blue button read as slightly illuminated.
- On dark surfaces: ghost button with `rgba(255, 255, 255, 0.15)` hover fill, `rgb(237, 237, 237)` border, transitioning from 80% white to 100% white text on hover.
- Focus ring: a 2px blue ring `rgb(37, 103, 255)` with a 2px white inner gap — the accessibility-first focus pattern.
- Border-radius uses `--radius: .5rem` (8px) for buttons; `--radius-pill: 9999px` for status chips and tags.

**Cards and surfaces**
- Cards sit on `rgb(249, 249, 249)` (`--surface`) with `rgb(237, 237, 237)` borders. The luminance difference from the white canvas is minimal — cards are implied, not framed.
- `--card-padding: 1.25rem` is the standard interior padding.
- `--radius-callout: .625rem` and `--radius-editorial: .875rem` define progressively softer radii for callout blocks and editorial sections.
- Chip elements use `0 0 0 / .04` fill (4% black), creating near-invisible fills that register as distinct from pure white only at close range.

**Code blocks**
- JetBrains Mono at 12px, weight 400, line-height 19.5px. Color `rgb(212, 212, 216)` — the off-white used for code in dark contexts.
- The API demo block uses a live terminal aesthetic: `POST` method label in blue, response with a `201 Created` status indicator, curl syntax highlighted.

**Shadow system**
Five named shadows covering a range from hairline to editorial depth:
- `--shadow-subtle`: `0 1px 2px -1px rgba(0,0,0,0.08)` — border substitute for borderless cards
- `--shadow-sm`: `0 1px 2px rgba(0,0,0,0.04)` — inputs, subdued cards
- `--shadow-md`: `0 6px 16px rgba(0,0,0,0.06)` — standard cards
- `--shadow-lg`: `0 24px 48px rgba(0,0,0,0.08)` — modals, overlays
- `--shadow-editorial`: `0 40px 80px rgba(0,0,0,0.15)` — hero product screenshots

---

## 5. Layout Principles

- Max content width is `--page-max-width: 1200px`, horizontally centered, with sections using `--section-gap: 4rem` vertical rhythm.
- The page stacks vertically in clear thematic bands: hero → logos → feature pillars → product UI demo → developer section → pricing → footer. Each band is full-width but content-constrained at 1200px.
- Breakpoints: 640 / 768 / 1000 / 1024 / 1100 / 1280 / 1400. A more granular set than typical, with 1000 and 1100 as custom tablet/intermediate breakpoints suggesting precise mid-range layout adjustments for the demo UI.
- The workflow builder demo is a visually significant element: a multi-step drag-and-drop pipeline rendered as an interactive screenshot. It uses the dark overlay surface (`rgba(40, 40, 40, 0.7)`) to read as a real product, not a marketing illustration.
- The API code section uses a two-column layout: marketing copy on the left, a dark code panel on the right. The contrast between the white page and the black code surface creates a strong anchor point mid-page.
- Spacing is component-level throughout — structural elements (body, main, section, header, footer) all carry zero padding and margin, consistent with a component-driven CSS architecture.

---

## 6. Depth & Elevation

The elevation system is primarily shadow-based rather than surface-color-based, which is unusual for a light-mode product site and signals a deliberate design choice:

- Most cards read flat — the luminance delta between `rgb(255, 255, 255)` canvas and `rgb(249, 249, 249)` surface is so small (luminance ~1.0 vs ~0.976) that borders carry the differentiation.
- The shadow vocabulary creates a clear hierarchy from `--shadow-subtle` (hairline, ~1px) to `--shadow-editorial` (dramatic, 80px spread), with the editorial shadow used for the hero product screenshot to make it feel like a physical object lifted off the page.
- The blue CTA button uses both a standard box-shadow AND a colored glow shadow (`rgba(37, 103, 255, 0.45)`). This double-shadow technique — neutral shadow for depth, colored shadow for brand emphasis — is the page's most distinctive elevation detail.
- Dark sections (the footer, the developer feature block) achieve depth through full luminance inversion rather than shadow: jumping from `rgb(255, 255, 255)` to `rgb(13, 13, 13)` creates a hard boundary that functions as the deepest UI layer on the page.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(37, 103, 255)` as the sole interactive accent. Reserve it for CTAs, active states, focus rings, and links only — never as a decorative element.
- Apply negative letter-spacing at display sizes: -1.4px at 56px, -1.1px at 44px, -0.9px at 36px. Never use positive or zero tracking for headings in this system.
- Enable `font-feature-settings: "cv11", "ss01"` on all Inter UI text.
- Use `--shadow-editorial` (`0 40px 80px rgba(0,0,0,0.15)`) for hero product images to give them physical presence against the white page.
- Reserve the dark inversion (`rgb(13, 13, 13)` background, white text) for developer-focused or footer sections — the contrast is meaningful precisely because it is rare.
- Keep status colors (success, warning, danger, the traffic-light trio) inside product UI mocks only. They are product chrome, not page chrome.
- Use JetBrains Mono for all code, `12px / 19.5px`, no OpenType features.

**Don't**
- Don't introduce a second accent color. The page's authority comes from one blue, used cleanly.
- Don't remove the blue glow shadow from primary CTA buttons — it is the brand fingerprint of the interactive layer.
- Don't use weight 600 or 700 outside of button labels. The typographic hierarchy runs 400/500; 700 is reserved exclusively for CTAs.
- Don't use `--radius-pill` (9999px) on rectangular containers — it belongs only on small chips, tags, and status badges.
- Don't place status colors (green success, red danger, amber warning) in navigation or section UI. They are scoped to product-within-page mock contexts.
- Don't use shadows with colored tints in the structural page chrome — the blue glow is an exception because it is on the primary CTA; all other shadows are pure `rgba(0,0,0,...)`.

---

## 8. Responsive Behavior

Seven breakpoints (640 / 768 / 1000 / 1024 / 1100 / 1280 / 1400) reflect a product page with complex mid-range layout requirements. The custom 1000 and 1100 breakpoints suggest the demo UI blocks reflow at intermediate laptop sizes before reaching the standard 1024 tablet breakpoint.

- At 768px the page enters tablet layout: the two-column developer section likely stacks, navigation compresses to a hamburger.
- The workflow builder demo is the most layout-sensitive component — its multi-step pipeline visualization would need to either horizontally scroll, vertically reflow into a numbered list, or switch to a simplified static representation on small screens.
- Typography scales smoothly across breakpoints: the `--tracking-display: -.02em` token is relative (em), so tracking preserves the proportional condensing effect regardless of the rendered size.
- Touch targets for the workflow builder and the interactive pricing table need minimum 44px touch areas on mobile — the `--radius-pill: 9999px` tags are small enough at default size to require careful padding on touch surfaces.

---

## 9. Agent Prompt Guide

> Build a page section that matches Didit's design language.

Set the canvas to `rgb(255, 255, 255)` with `rgb(40, 40, 40)` text. Use **Inter** for all UI text with `font-feature-settings: "cv11", "ss01"` active; use **JetBrains Mono** for any code or API snippet. For display headings set weight 500, negative letter-spacing (`-1.4px` at 56px, `-1.1px` at 44px, `-0.9px` at 36px) — this is the non-negotiable typographic fingerprint. Body text at 16px / 24px / weight 400 / no tracking.

The primary interactive color is `rgb(37, 103, 255)`. Use it for CTA buttons, links, and focus rings only — never decoratively. Primary buttons carry a double shadow: `0 6px 16px rgba(15, 23, 42, 0.1)` (neutral depth) plus `rgba(37, 103, 255, 0.45) 0px 8px 24px -8px` (blue glow). Focus ring is a 2px blue ring with 2px white inner gap.

Cards sit on `rgb(249, 249, 249)` with `rgb(237, 237, 237)` borders and `0 6px 16px rgba(0,0,0,0.06)` shadow. Border-radius is `8px` for cards, `9999px` for tags/chips only.

For developer or code sections, invert to `rgb(13, 13, 13)` background with white text — this is the most visually impactful contrast move in the system and should be used sparingly. Inside those dark sections, render code in JetBrains Mono at 12px, `rgb(212, 212, 216)`.

Max content width is `1200px`, section vertical gap is `4rem`. Keep spacing at the component level; structural elements carry zero padding.
