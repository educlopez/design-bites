# Lumbre — Design System Reference

## 1. Visual Theme & Atmosphere

Lumbre calls itself "a sanctuary for the contemplative mind," a space for "deliberate reading" with "no distractions" and "no endless scrolling," and the interface is built to match that promise. The page sits on a deep, slightly green charcoal (`rgb(28, 30, 29)`) with white text, so it feels like reading by a dim lamp. One grotesk, Neue Montreal, handles nearly everything at weight 400, while a dot-matrix face, Doto, appears uppercase for a few mechanical accents, such as the live date and time readout in the header. Content is arranged into translucent bento blocks (`rgba(255, 255, 255, 0.16)`) with an 8px radius, and spacing is large and quiet. The tone is calm, bilingual (EN / ES toggle), and deliberately slow. It is built with Astro.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(28, 30, 29)` — page canvas (dark green-tinted charcoal)
- `rgb(255, 255, 255)` — primary text, header text, active language link, button border
- `rgb(163, 163, 163)` — muted grey for h2 and the inactive language link

**Surfaces**
- `rgba(255, 255, 255, 0.16)` — translucent glass for `div.bentoBlock` cards and the "View more" button fill

**Text on glass**
- `rgb(0, 0, 0)` — the button label color extracted on the translucent fill

**Unstyled defaults**
- `rgb(0, 0, 238)` — the browser default link blue appears in the extracted `a` and logo link styles. It is the UI's fallback, not a designed brand color; the live site's links read white and grey, so the extraction here is a computed-style artifact.

The palette is effectively monochrome: one near-black, white, one grey and a single translucent white layer. No hue accent is declared.

---

## 3. Typography Rules

**Typefaces**
- **Neue Montreal** — headings, body, links; weight 400 throughout
- **Doto** — dot-matrix display face, used on `p` at weight 800, uppercase
- **Arial** — browser default on `button` and `input`, not customised

**Scale**

| Role   | Font          | Size     | Weight | Line-height | Tracking | Transform |
|--------|---------------|----------|--------|-------------|----------|-----------|
| H1     | Neue Montreal | 30.58px  | 400    | 30.58px     | normal   | none      |
| H2     | Neue Montreal | 18px     | 400    | 22px        | normal   | none      |
| H3     | Neue Montreal | 16px     | 400    | 16px        | normal   | none      |
| H4     | Neue Montreal | 32px     | 400    | 36px        | normal   | none      |
| Body   | Neue Montreal | 16px     | 400    | 16px        | normal   | none      |
| P      | Doto          | 16px     | 800    | 16px        | normal   | uppercase |
| Link   | Neue Montreal | 16px     | 400    | 16px        | normal   | none      |
| Button | Arial         | 13.33px  | 400    | normal      | normal   | none      |
| Input  | Arial         | 16px     | 400    | 16px        | normal   | none      |

**Principles**
- Weight is constant at 400 on Neue Montreal; hierarchy comes from size and colour (h2 steps down to grey `rgb(163, 163, 163)`).
- Line-height equals font size on h1, h3, body, link and input, giving a compact, set-solid texture.
- Doto at weight 800 and uppercase is the single expressive device, a pixel-grid voice used sparingly against the clean grotesk.
- Tracking is never adjusted anywhere in the extracted system.

---

## 4. Component Stylings

**Bento blocks**
- Background `rgba(255, 255, 255, 0.16)`, radius `8px`
- Used for the featured-insight cards (manifesto, essays), each ending in a "View more" action

**Buttons ("View more")**
- Background `rgba(255, 255, 255, 0.16)`, text `rgb(0, 0, 0)`, border `rgb(255, 255, 255)`
- 13.33px Arial (browser default), no shadow
- Default and focus states are visually identical except for a `rgb(16, 16, 16)` auto outline of 1px on focus; no hover state was captured

**Header links**
- Header logo link and the language toggle (EN / ES), 16px Neue Montreal
- Active language `rgb(255, 255, 255)`, inactive `rgb(163, 163, 163)`
- Header gap `24px`

**Inputs**
- 16px Arial, unstyled defaults

**Border radius**
- `8px` — the single radius

**Shadows**
- None detected.

---

## 5. Layout Principles

- `main` uses `0px 64px` horizontal padding, so content is framed by a 64px gutter.
- `section` has `112px 0px` padding with a `-112px` top margin, a spacing offset commonly used so anchor links land cleanly below a fixed header.
- `header` has `32px 0px` padding and a `24px` gap between items.
- `footer` has a `96px` top margin and a `32px` bottom margin.
- `--vh` is set as a custom property (`6px` at capture), indicating a JavaScript-driven viewport height unit.
- Breakpoints: **667 / 768 / 769 / 890 / 1024 / 1025 / 1280 / 1281**, a dense set that implies fine-tuned layouts at each step.

---

## 6. Depth & Elevation

Depth is handled by transparency, not shadow. No `box-shadow` was extracted. The only elevation cue is the `rgba(255, 255, 255, 0.16)` glass layer, which lifts the bento blocks off the `rgb(28, 30, 29)` canvas by lightening it. The effect is quiet and tonal, consistent with the reflective mood.

---

## 7. Do's and Don'ts

**Do**
- Keep the canvas at `rgb(28, 30, 29)` and text at white.
- Use one grotesk at weight 400 and let size and grey value create hierarchy.
- Build cards from a 16% white translucent fill with an `8px` radius.
- Use Doto uppercase for rare mechanical accents such as a clock.
- Keep generous vertical padding (`112px` sections) and a `64px` side gutter.
- Show the language toggle as white-active, grey-inactive.

**Don't**
- Don't add bright accent colours; the palette is monochrome.
- Don't add shadows; use translucency instead.
- Don't use bold on the grotesk; weight stays at 400.
- Don't leave links at browser-default blue (`rgb(0, 0, 238)`); style them in white or grey on this dark canvas.
- Don't rely on Arial for buttons and inputs if you want to match the typographic intent; use Neue Montreal.

---

## 8. Responsive Behavior

A dense breakpoint ladder at **667, 768, 769, 890, 1024, 1025, 1280 and 1281** points to adjustments at many widths, including paired values (768/769, 1024/1025, 1280/1281) typical of min/max-width media query pairs. Horizontal padding of `64px` on `main` is the desktop gutter, and the `--vh` custom property indicates mobile viewport-height correction. The site ships EN and ES versions.

---

## 9. Agent Prompt Guide

> Build a UI that matches Lumbre's design language.

Use a dark green-tinted charcoal canvas `rgb(28, 30, 29)` with white `rgb(255, 255, 255)` text and muted grey `rgb(163, 163, 163)` for secondary headings and inactive links. Set everything in **Neue Montreal** at weight 400: h1 about 30.6px with tight line-height, body and links at 16px. Use **Doto** at weight 800, uppercase, 16px for occasional dot-matrix accents such as a date and time readout. Build cards as translucent bento blocks with `rgba(255, 255, 255, 0.16)` fill and an `8px` radius, with no borders or shadows. Buttons share the same translucent fill with a white border. Frame the page with `0 64px` main padding, `112px` vertical section padding, `32px` header padding and a `24px` header gap. Keep the palette monochrome and the tone calm and unhurried. Make sure links are styled, not browser blue.

---

*Generated by Sparkbites — extracted from live CSS analysis*
