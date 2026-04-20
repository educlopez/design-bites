# Variant — Design System Reference

## 1. Visual Theme & Atmosphere

Variant is "endless designs for your ideas — just scroll," and the homepage is built to stage exactly that: a dark editorial canvas (`rgb(34, 34, 34)`) on which a right-hand grid of dashed-outline cards will fill with generated variations as the user scrolls. The left column holds the entire brand — a small pixel-grid glyph, a wordmark in the house display face, a two-sentence manifesto set in a custom warm off-white (`rgb(240, 237, 229)`), two discreet chrome buttons, and a prompt input pinned to the bottom. The tone is quietly cinematic. Nothing in the composition competes with the content that will stream in from the right. Typography does emotional work — a condensed "Variant Neue Display" for headlines, a "Variant Neue Text" for body — while the color system is strictly monochromatic grays plus warm cream ink, with blues and corals reserved entirely for application-state chrome the user rarely sees. This is a product homepage that behaves like a portfolio: most of the design effort is in *restraint*.

---

## 2. Color Palette & Roles

**Foundation (the monochrome frame)**
- `rgb(34, 34, 34)` — page canvas (`--color-gray-dark`) — an off-black editorial charcoal
- `rgb(7, 7, 6)` — button surface / deeper frame (`.app` container) — nearly black, very slightly warm
- `rgb(30, 30, 28)` — homepage input container — a step above the page dark, warm-toned
- `rgb(240, 237, 229)` — cream ink (`--color-white` equivalent via brand) — used for all body/heading text
- `rgb(255, 255, 255)` — pure white, reserved for absolute-contrast moments (body default, before override)

**Accent — present in design tokens, absent from the homepage hero**
- `#2688f9` / `#3a86ff` / `#3291ff` — a trio of primary/secondary/tertiary blues (product UI only)
- `rgb(59, 130, 246)` / `rgb(37, 99, 235)` — accent + brand blue (product UI)
- `rgb(248, 113, 113)` — coral accent (billing / past-due states)
- `rgba(223, 99, 78, *)` — the "past due" family (error text, backdrop, hover bg, border, modal bg)
- `red`, `green`, `yellow`, `blue` — CSS-named semantic slots (success/error/warning/info)

**The transparency ladder — the system's real vocabulary**
- A full `rgba(255, 255, 255, 0.03 → 0.90)` ramp (`--color-white-03` through `--color-white-90`) and a mirror `rgba(0, 0, 0, *)` ramp
- This ramp is the primary depth vocabulary: almost every border, divider, and hover state is expressed as a white-on-black percentage rather than as a separate grey value

**Supporting grays**
- `#222222` dark / `#363636` medium / `#dadada` light / `#ccc` lighter — named, but used sparingly

The palette is disciplined: a black-ink frame, a cream-paper text color, and a whisper of blue/coral only when the app's state demands it. The homepage itself reads as **two colors** (charcoal + cream) enriched by ~15 gradations of transparency.

---

## 3. Typography Rules

**Typefaces (all proprietary)**
- **Variant Neue Display** — condensed display face, used for H1 ("Endless designs for your ideas, *just scroll.*")
- **Variant Neue Text** — body face, used for paragraphs, buttons, and inline `<Variant>` brand mentions
- **Inter** — fallback only, never the designed default

**Scale**

| Role | Font | Size | Weight | Line-height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| H1   | Variant Neue Display | 32px | 400 | 36px | +0.32px | none |
| Body | Inter (fallback) | 16px | 400 | normal | normal | none |
| P    | Variant Neue Text | 14px | 400 | 24px | +0.28px | none |
| Button | Variant Neue Text | 11px | 400 | 11px | +0.22px | none |

**Principles**
- **Weight locked at 400.** Hierarchy comes from face (Display vs Text), size, and tracking — not from bold/light contrast.
- **Positive tracking on every tier.** H1 +0.32px, P +0.28px, Button +0.22px — a consistent ~1% wider-than-default. This makes the condensed display feel open and the body copy feel composed.
- **Italic as a stylistic device, not an emphasis tool.** The hero headline sets "just scroll." in italic serif/italic display — a deliberate typographic gesture that signals product voice, not syntactic emphasis.
- **Button type is tiny.** 11px with +0.22px tracking, line-height equal to font-size (compression of 0) — buttons read as labels, not as affordances.

**What's absent:** no webfont bold, no sans-serif display alternative, no rounded/decorative face. The two-family system (Display + Text) is the whole palette.

---

## 4. Component Stylings

**Primary button** — e.g. "Sign up / Sign in"
- Background: `rgb(7, 7, 6)` (slightly-warmer-than-black)
- Text: `rgb(240, 237, 229)` (cream)
- Border: `rgba(255, 255, 255, 0.1)` — a 10% white hairline, the house bordering style
- No shadow. No transform on hover (hover is `null` in the extracted data for the suggestion button — the button doesn't respond visually until focus)
- Focus: adds native `rgb(0, 95, 204) auto 1px` outline

**Ghost / chrome button** — e.g. the "+" icon in the homepage input
- Background: transparent
- Text: `rgba(255, 255, 255, 0.5)` — 50% white (soft)
- Border: `rgba(255, 255, 255, 0.5)` matching
- Hover: background becomes `rgba(255, 255, 255, 0.07)` — a 7% white wash, the text and border don't change
- The hover pattern here — bg darkens by ~7%, text holds still — is Variant's signature interaction grammar

**Homepage input**
- Container background: `rgb(30, 30, 28)` (warmer than the page)
- Border: `rgba(255, 255, 255, 0.1)` (same 10% white as buttons)
- Inline action icons (+, @, send) sit at 50% white, hover to 7% white bg

**Dashed grid cards** (the variation slots)
- Stroke: dashed `rgba(255, 255, 255, 0.1)` (implied from the extracted palette — the 10% white is the house divider)
- Corners: `6px` or `8px` (the only two border-radii in the extracted system)
- Content: empty until scroll fills them; each card eventually holds a rendered design

**Border radii**
- `12px` (`--border-radius` token — base)
- `6px` and `8px` (actual usage on buttons/cards)

**Shadows** — none in the extracted system. Depth is entirely a percentage of white.

---

## 5. Layout Principles

- **Two-column, asymmetric.** Left column: ~240–300px fixed brand + controls rail. Right column: flex-fill grid of dashed variation tiles (2–3 columns depending on width).
- **Max content width.** `--max-width: 1100px` — a conservative editorial width that prevents the variation grid from feeling infinite.
- **Bottom-pinned input.** The homepage prompt sits at the bottom of the left rail, inside a warm-toned container — a "footer" in visual hierarchy but a primary action in behaviour.
- **Breakpoints: 600, 764, 900, 932, 980.** An unusually dense cluster between 900 and 980 suggests the layout has a specific treatment for laptop-class widths (likely the point where the 2-column fold collapses to 1).
- Global `body/main/section { padding: 0, margin: 0 }` — all spacing is delegated to inner containers, never to global resets.

**Z-index layer system (from custom properties)**
- `--z-panel`, `--z-sidebar`: 2000
- `--z-chat-topbar`: 2005
- `--z-detail-view`: 2010
- `--z-options-menu`: 2020
- `--z-chat-topbar-left`: 2025
- `--z-sidemodel`: 2050
- `--z-stylemodal`: 2100

A 100-point band starting at 2000 — tightly choreographed, no ad-hoc values. This is a product built expecting many overlapping surfaces.

---

## 6. Depth & Elevation

Variant communicates depth through **warmth and transparency**, not through shadow:

- Canvas `rgb(34, 34, 34)` → app container `rgb(7, 7, 6)` → input container `rgb(30, 30, 28)` — three closely-spaced dark surfaces where the depth cue is a 3–30 point shift in luminance and a ~2° shift in warmth. The page literally feels like paper-on-paper but in the dark register.
- Borders are almost always `rgba(255, 255, 255, 0.1)` — a 10% white hairline that registers as "the edge of something" without drawing attention to itself.
- There are **no box-shadows** in the extracted system. This is deliberate — shadows on a near-black page collapse to invisible or require heavy gradients that would conflict with the editorial tone.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(34, 34, 34)` as the page canvas — pure black kills the editorial warmth.
- Pair with `rgb(240, 237, 229)` (cream) for text — never pure white on this canvas.
- Express borders and dividers as `rgba(255, 255, 255, 0.1)`. If you need a softer line, drop to 0.05; if you need a stronger one, go to 0.15. Keep the ramp consistent.
- Use the `rgba(255, 255, 255, 0.07)` wash as the hover state for ghost buttons — the number is precise.
- Set all body and heading type at weight 400 in the Variant Neue pair, with slight positive tracking (`+0.2px` to `+0.3px`).
- Reserve blues and corals for product chrome (billing states, error states, primary action) — never for marketing/brand surfaces.
- Let italic serve as a *stylistic* gesture in headlines ("just scroll.") — it's not italicized for emphasis, it's italicized for voice.

**Don't**
- Don't add drop-shadows — the palette has no room for them and the editorial mood rejects them.
- Don't introduce new blues or accent colors outside the existing token list. The `--color-primary-blue` / `--color-secondary-blue` / `--color-tertiary-blue` trio is deliberate; don't mint a fourth.
- Don't use bold weights to create hierarchy. Switch face (Display ↔ Text) or scale up/down instead.
- Don't apply button hover transforms (scale, translate) — Variant's interactions are pure tonal shifts.
- Don't set body text in pure white `#ffffff`. The cream `rgb(240, 237, 229)` is load-bearing for the brand warmth.
- Don't use border-radii larger than 12px. The card/chip language is subtle rectilinear, not pill.

---

## 8. Responsive Behavior

Breakpoints are dense — **600 / 764 / 900 / 932 / 980** — with the 900/932/980 triplet suggesting very specific treatments around laptop-class widths. The most likely layout flow:

- **<600px** — single column, brand stack on top, dashed grid beneath, input pinned to bottom of viewport
- **600–900px** — still single-column but with wider gutters; the variation grid is 1–2 cards wide
- **900–980px** — the tipping point where the two-column layout engages (left rail pins to the side, variation grid fills the remainder)
- **>980px** — the full desktop layout with the 1100px max-width constraining the grid

The input container and buttons carry their sizes through every breakpoint — type does not compress. This is a design that assumes a pointer + keyboard first and treats mobile as a graceful-degradation case.

---

## 9. Agent Prompt Guide

> Build a UI that matches Variant's design language.

Set the canvas to `rgb(34, 34, 34)` (warm charcoal — never pure black) and body ink to `rgb(240, 237, 229)` (cream — never pure white). Use **Variant Neue Display** for headlines (32px, weight 400, `+0.32px` tracking — italic permitted as a stylistic flourish) and **Variant Neue Text** for body (14px, weight 400, `+0.28px` tracking) and buttons (11px, weight 400, `+0.22px` tracking, line-height = font-size). Hold every weight at 400; hierarchy comes from face + size + tracking. Primary buttons are `rgb(7, 7, 6)` background, `rgb(240, 237, 229)` text, `rgba(255, 255, 255, 0.1)` border, no shadow, no transform. Ghost buttons are transparent with `rgba(255, 255, 255, 0.5)` text and border; hover adds a `rgba(255, 255, 255, 0.07)` background wash — text and border don't change. Inputs sit in a warm `rgb(30, 30, 28)` container with the same 10% white border. Use `rgba(255, 255, 255, 0.1)` for every divider, hairline, and card edge — it's the house stroke. Reserve the token blues (`#2688f9`, `#3a86ff`, `#3291ff`) and corals (`rgba(223, 99, 78, *)`) strictly for product states (primary action, billing, error) — never for landing-page chrome. Corners are `6px` or `8px`, never pills. No drop-shadows anywhere. Depth is always expressed as a percentage of white over the charcoal frame.

---

*Generated by Sparkbites — extracted from live CSS analysis*
