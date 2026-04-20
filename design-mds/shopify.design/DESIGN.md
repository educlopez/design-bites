# Shopify Design — Design System Reference

## 1. Visual Theme & Atmosphere

`shopify.design` is Shopify's design-team home page, and it announces itself the way a magazine cover does — with one enormous typographic statement filling almost the entire viewport. "Make the new normal" is set at **215 pixels** in a bespoke serif (**AntiqueLegacy**), cranked to a condensed line-height and pulled inward with heavy negative tracking (`-8.6px`). Everything below that masthead is quiet on purpose: a white page, black ink, a single green status dot ("● LIVE"), and a horizontal carousel of artifact cards whose colors do the polychrome work. The page reads as editorial rather than product-marketing — it is a studio publication, not a conversion landing. Whitespace is generous, chrome is almost invisible, and the tension lives entirely in the head-over-heart contrast between a giant serif and tiny, unstyled Times supporting copy. This is the house voice of a team confident enough to let one display face carry the whole brand.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255, 255, 255)` — page canvas (pure white)
- `rgb(0, 0, 0)` — ink (text, borders, CTAs)
- `rgb(230, 230, 230)` — hero-live-line divider (luminance 0.90)

**Brand accents (carousel card pairs — each card is a two-color duet)**
- `rgb(28, 59, 54)` forest green + `rgb(107, 255, 145)` neon mint
- `rgb(184, 196, 219)` periwinkle + `rgb(79, 39, 48)` oxblood
- `rgb(223, 213, 203)` putty + `rgb(254, 67, 42)` vermillion
- `rgb(79, 39, 48)` oxblood + `rgb(255, 170, 199)` bubblegum pink
- `rgb(2, 37, 172)` ultramarine + `rgb(255, 170, 199)` pink
- `rgb(255, 170, 199)` pink + `rgb(254, 67, 42)` vermillion
- `rgb(254, 67, 42)` vermillion + `rgb(255, 170, 199)` pink

**Interactive chrome**
- `rgb(0, 0, 0)` — button-pill background (solid black)
- `rgba(0, 0, 0, 0.04)` — faint border on hero cards
- `rgb(26, 26, 26)` — focus ring (2px solid)

The system is **bi-tonal at the frame** (pure white + pure black) and **polychrome inside content**. Every accent color is paired — never applied solo — so the palette reads as a set of curated duets rather than a swatch library.

---

## 3. Typography Rules

**Typefaces**
- **AntiqueLegacy** (serif, display weight 500) — the sole personality face: h1, h2, h3, and p. This is a condensed, high-contrast revivalist serif — 19th-century wood-type energy in a digital shell.
- **Times** — unstyled fallback for body, links, buttons, and dialogs. Explicitly not a "design" face. Shopify lets it remain raw Times so that nothing competes with AntiqueLegacy.

**Scale**

| Role | Font | Size | Weight | Line-height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| H1   | AntiqueLegacy | 215.3px | 500 | 150.7px | −8.61px | none |
| H2   | AntiqueLegacy | 40px    | 500 | 34px    | −1.2px  | none |
| H3   | AntiqueLegacy | 56.0px  | 500 | 47.6px  | −2.24px | none |
| P    | AntiqueLegacy | 22px    | 400 | 24.2px  | −0.44px | none |
| Body | Times | 16px | 400 | normal | normal | none |
| A / Button | Times | 16px | 400 | normal | normal | none |

**Principles**
- **Scale-driven hierarchy.** h3 (56px) is larger than h2 (40px) — the conventional ramp is broken because h3 is used as a section masthead while h2 is used as an item label. Size follows visual role, not semantic rank.
- **Negative tracking scales with size.** −8.6px at 215px, −2.24px at 56px, −1.2px at 40px — tight optical kerning for a display face, never applied to body Times.
- **Weight contrast is extreme but simple.** 500 (semibold-ish) for display in the house serif, 400 for any supporting prose. No italics, no bolds beyond 500.
- **Body text is intentionally mundane.** Using Times (not a branded face) for captions and labels is a move: it keeps AntiqueLegacy rare enough to feel like a headline every time it appears.

---

## 4. Component Stylings

**Hero grid cards** (the floating artifact tiles under the h1)
- Default: white bg, near-invisible `rgba(0, 0, 0, 0.04)` border, box-shadow barely there (`rgba(0,0,0,0) 0px 0.66px 1.71px`)
- Hover: shadow deepens dramatically — `rgba(0, 0, 0, 0.07) 0px 8.2px 21.2px` — and the card scales up ~0.87% (`matrix(1.00871, ...)`)
- Focus: 2px solid ring in `rgb(26, 26, 26)` (near-black, deliberately not full black)

**Button pill** (header CTA, "Demo Night Vol. 2 · Apr 22")
- Background: white pill with faint tonal outline
- Border-radius: `9999px`
- Black icon + tiny avatar glyph to the left of text
- Secondary variant: `rgb(0, 0, 0)` solid pill (e.g. `.btn-pill`)

**Links**
- Inline, unstyled Times — only visible because the focus ring (`rgb(0, 95, 204) auto 1px`) appears on keyboard interaction
- Hover state is null in the extracted data — the page doesn't rely on hover feedback for navigation

**Border radii**
- `9999px` — button pills, the green live dot
- `24px`, `24.07px`, `14.22px` — generous card corners (varies per breakpoint)
- `3px` — hairline radii on the live line

**Shadow** — only one value present:
- `rgba(0, 0, 0, 0.12) 0px 24px 32px 0px` — the heavy "lift" on focused/hovered cards

---

## 5. Layout Principles

- **Masthead-first composition.** The h1 occupies the upper 60–70% of the viewport. Everything else is supporting.
- **Padded frame.** `header { padding: 24px 48px 48px }` and `footer { padding: 0px 48px 164px }` — 48px side rails hold every major rail off the edge, and the footer gets a deep 164px bottom breather so the page ends like a magazine spread, not a flushed container.
- **Horizontal card carousel** sits under the hero — 3 visible tiles with large border-radii, arranged as a strip the viewer scrolls through.
- **Live strip.** A thin horizontal line with "● LIVE" on the left and "FROM ARTIFACT ●" on the right divides hero from carousel. The green dot is the only non-monochrome pixel in the upper fold.
- Gap usage is sparse: headers use `gap: 32px`, section/body containers use `normal` — the layout is composed, not gridded.

---

## 6. Depth & Elevation

Depth is almost entirely a **hover affordance** — the page at rest is flat. There is exactly one shadow value in the system:

- **Hero card hover shadow** — `rgba(0, 0, 0, 0.12) 0px 24px 32px` — a 24px vertical lift that only engages on interaction, paired with a 0.87% scale up.

The default card shadow is `rgba(0, 0, 0, 0)` — a transparent placeholder that preserves the layer stacking without actually drawing anything. Static depth is communicated instead through luminance swap:

- Canvas `rgb(255, 255, 255)` (1.00) → live-line `rgb(230, 230, 230)` (0.90) → carousel fills (0.16–0.84)

The effect: the page feels like a printed editorial until you touch it, at which point the cards lift.

---

## 7. Do's and Don'ts

**Do**
- Use pure `#ffffff` as the page background and pure `#000000` for text — the contrast is part of the editorial stance.
- Let the display serif (AntiqueLegacy or a similarly condensed high-contrast serif) do the heavy lifting — headlines should feel oversized against their container.
- Apply negative letter-spacing that scales with size: roughly `−4%` of font-size at display ranges.
- Reserve chromatic accents for *pairs* inside content cards — never apply them to chrome, never let a single accent stand alone.
- Use `rgb(26, 26, 26)` (not pure black) for focus rings — a subtle warmth that keeps the keyboard indicator from competing with body ink.
- Keep supporting copy in Times (or equivalent unstyled serif). Make the house display face rare.

**Don't**
- Don't use a sans-serif anywhere in the display system — the whole brand identity rests on a condensed serif.
- Don't apply drop-shadows to static surfaces. Shadows are an interactive reward, not a depth cue.
- Don't introduce a third color into a carousel card — each card is a two-color composition.
- Don't round buttons to small radii like 6–8px. Use either a **full pill** (9999px) or a **generous card corner** (14–24px). Nothing in between.
- Don't add background fills to buttons except the black variant — the system's default CTA is a bordered pill, not a coloured fill.
- Don't crowd the hero — the h1 needs the 215px scale to work; smaller hero typography breaks the voice.

---

## 8. Responsive Behavior

No media queries were extracted (breakpoints array is empty) — Shopify Design uses CSS container queries or clamp-based scaling rather than fixed breakpoints. The h1 at `215.273px` with `−8.61091px` tracking is clearly computed via `clamp(...)` or `vw`-based sizing, since those sub-pixel values are the output of viewport math. Cards keep border-radii in a small set (`24px`, `24.07px`, `14.22px`) — the `14.22` and `24.07` variants are derived values that suggest the radii are expressed as a percentage of card width and resolve slightly differently at each viewport. In practice the responsive strategy is: the display serif rescales fluidly, the horizontal carousel reduces visible tiles, and the 48px header rail holds firm as the frame. No separate mobile treatment has been observed in the extracted data.

---

## 9. Agent Prompt Guide

> Build a UI that matches Shopify Design's editorial voice.

Set the canvas to pure white `rgb(255, 255, 255)` and text to pure black `rgb(0, 0, 0)`. Use a **condensed high-contrast serif** (AntiqueLegacy, or a substitute like Canela Deck or GT Sectra Display) at **semibold 500** for every headline. The hero h1 should run at ~215px with `−8.6px` tracking — computed via `clamp()` — and dominate the upper fold. Drop to 40px for sub-heads, 22px for lead paragraphs. Use **unstyled Times** (or equivalent serif system stack) at 16px 400 for all supporting copy, labels, and links — do not style these; their plainness is the point. Accent color pairs live only inside content cards: pair `rgb(28, 59, 54)` with `rgb(107, 255, 145)`, `rgb(2, 37, 172)` with `rgb(255, 170, 199)`, or `rgb(79, 39, 48)` with `rgb(254, 67, 42)` — never use a solo accent. Chrome is bi-tonal: white fields with `rgba(0, 0, 0, 0.04)` hairline borders, black pill CTAs at `border-radius: 9999px`, and a focus ring in `rgb(26, 26, 26)` at 2px. Apply drop-shadow (`rgba(0, 0, 0, 0.12) 0 24px 32px`) only on hover — static surfaces stay flat. Keep header padding at `24px 48px 48px` and footer padding at `0 48px 164px`. Let the typography do the talking.

---

*Generated by Sparkbites — extracted from live CSS analysis*
