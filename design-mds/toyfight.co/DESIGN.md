# ToyFight — Design System Reference

## 1. Visual Theme & Atmosphere

ToyFight brands itself as "The Unmistakably Original® Design Studio," and the home page delivers on that line through typographic craft rather than visual noise. A warm off-white canvas (`rgb(250, 246, 239)`) replaces default web white, giving the page the tactile feel of newsprint or a gallery catalogue. A bespoke condensed display face pairs with a rasterized grotesk and a matching mono, so the site reads as an editorial publication first and a studio portfolio second. Off-palette accents — sugar pink, lavender, highlighter yellow — appear inside masked content blocks, never as UI chrome, so the neutral frame stays intact while the storytelling inside breaks into playfulness. The tone is confident, crafted, a little cheeky, and deeply self-assured in its typographic voice.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(250, 246, 239)` — page canvas (warm off-white / soft paper)
- `rgb(241, 237, 231)` — secondary surface (footer, TOS panels, card surfaces)
- `rgb(13, 13, 14)` — ink (text, borders, inverted button backgrounds)

**Inverted / interactive**
- `rgb(13, 13, 14)` bg + `rgb(241, 237, 231)` fg — the primary link/pill treatment (dark stamp on cream)
- Border matches foreground on inverted elements — a sealed, stamp-like feel

**Playful accents (used inside masked content blocks only)**
- `rgb(233, 227, 243)` — pale lavender
- `rgb(255, 216, 245)` — sugar pink
- `rgb(255, 229, 0)` — highlighter yellow
- `rgb(255, 244, 144)` — soft yellow
- `rgb(253, 237, 212)` — cream peach
- `rgb(220, 220, 220)` — neutral gray (mobile nav surface only)

**Deep surfaces (overlays & media wrappers)**
- `rgb(61, 61, 64)` — slate overlay (transition mask)
- `rgb(28, 28, 30)` — image wrap background
- `rgb(13, 13, 14)` — transition curtain (the ink again, used as a reveal mask)

The system is deliberately bi-tonal at the frame level — cream and ink — and polychrome only where content asks for it. Accents never become UI chrome; they live inside content.

---

## 3. Typography Rules

ToyFight runs three proprietary typefaces in tight rotation, all set at weight 400 — hierarchy is driven by **face, size, and tracking**, never by weight.

**Typefaces**
- **SpeziaCondensed** — the editorial voice: display headlines, long-form body text, links, buttons
- **FKRasterGrotesk** — the operational voice: sub-headings, captions, labels, inputs, UI chrome
- **SpeziaMono** — the metadata voice: timestamps, fine print (declared elsewhere in the system)

**Scale**

| Role   | Font              | Size       | Weight | Line-height | Tracking       | Transform |
|--------|-------------------|------------|--------|-------------|----------------|-----------|
| H1     | SpeziaCondensed   | 36px       | 400    | 54px        | normal         | none      |
| H2     | FKRasterGrotesk   | 12px       | 400    | 19.2px      | normal         | none      |
| H3     | FKRasterGrotesk   | 30.86px    | 400    | 33.94px     | -0.617px       | none      |
| H4     | FKRasterGrotesk   | 12px       | 400    | 13.2px      | -0.24px        | none      |
| Body   | SpeziaCondensed   | 18px       | 400    | 27px        | normal         | none      |
| Link   | SpeziaCondensed   | 18px       | 400    | 27px        | normal         | none      |
| Button | SpeziaCondensed   | 18px       | 400    | 27px        | normal         | none      |
| P      | FKRasterGrotesk   | 11px       | 400    | 11px        | +0.88px        | uppercase |
| Input  | FKRasterGrotesk   | 12px       | 400    | 18px        | normal         | none      |

**Principles**
- Weight is a constant, not a variable. All differentiation comes from face-switching and size jumps.
- Condensed serif-adjacent display face (SpeziaCondensed) for emotional / editorial copy and interactive elements; a rasterized grotesk (FKRasterGrotesk) for anything structural.
- Fine print uses FKRasterGrotesk at 11px, set `uppercase` with `+0.88px` tracking — the rasterized texture survives at tiny sizes where a cleaner grotesk would feel generic.
- Negative tracking only on large FKRasterGrotesk (h3/h4). SpeziaCondensed is left at natural spacing because its condensed forms already carry the tension.

**What's absent:** no webfont italics, no faux-bold, no serif body. Every lazy type trick has been removed from the palette.

---

## 4. Component Stylings

**Links / pills** (primary interactive element)
- Background: `rgb(13, 13, 14)` (ink)
- Text: `rgb(241, 237, 231)` (off-white)
- Border: same as text — a solid ink stamp on cream
- Focus state adds an auto outline at 1px; hover is unchanged (motion-free)

**Secondary links** (nav items)
- Transparent background, ink text, no border
- Focus ring is the only visible interaction — no hover transform, no color shift

**Inputs**
- Transparent background on the cream canvas
- Black text, black border — the field is defined by a hairline, not a filled surface
- 12px FKRasterGrotesk with normal tracking

**Buttons**
- Same SpeziaCondensed 18px as body links, inverted surface treatment

**Border radius**
- `64px`, `999px`, `2px`, `4px` — large pill radii on content blocks and masked labels, hairline radii on inputs/focus outlines.
- The overall shape language still reads rectilinear because radii live on specific content masks, not on chrome.

**Shadows**
- None detected. Depth is never soft.

---

## 5. Layout Principles

- Editorial grid with generous horizontal padding (`~36.4px` on header and footer) that frames content rather than letting it bleed edge-to-edge.
- Footer carries ~54px of top padding — the page ends with breathing room, not a flush cutoff.
- Breakpoints at **768 / 1024 / 1280** — a standard tablet → laptop → desktop set; nothing exotic, because the typography is doing the custom work.
- Horizontal rhythm is type-driven: long condensed headlines set the column width; the rasterized grotesk fills captions underneath.
- Videos and images are wrapped in dark surfaces (`rgb(28, 28, 30)` / `rgb(13, 13, 14)`), so media punches against the cream frame rather than blending with it.
- Body and section elements reset margins/padding to 0 — all spacing is delegated to the frame (header, footer, masked blocks).

---

## 6. Depth & Elevation

Depth is almost entirely flat. The only layering cues are:
- **Surface swap** — `rgb(241, 237, 231)` panels sit on top of the `rgb(250, 246, 239)` canvas (luminance 0.93 vs 0.96), a whisper-thin difference that reads as a subtle card without ever needing a shadow.
- **Transition curtains** — full-bleed ink panels (`rgb(13, 13, 14)`, luminance 0.05) slide across as page-transition masks, creating depth through motion rather than static elevation.
- **Media wrappers** — deep charcoals (`rgb(28, 28, 30)` / `rgb(61, 61, 64)`) frame videos and images, giving them a cinema-like frame.

No `box-shadow` in the extracted system. ToyFight treats shadow as a smell, not a tool.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(250, 246, 239)` as the base canvas — it carries the whole brand warmth.
- Hold every weight at 400 and let face + size do the hierarchy.
- Pair SpeziaCondensed with FKRasterGrotesk; never let one type do both jobs.
- Set fine print as 11px FKRasterGrotesk uppercase with positive tracking.
- Reserve accent colors (lavender, pink, yellow, peach) for masked content blocks, caption chips, or playful inline highlights.
- Frame media with a dark wrapper so it separates cleanly from the cream page.
- Use ink-on-cream pills for primary links/buttons; let secondary links be transparent with ink text.

**Don't**
- Don't introduce pure white (`#ffffff`) backgrounds — it kills the warmth.
- Don't add drop-shadows for elevation — surface color swap is the system.
- Don't use bold weights as emphasis; switch face or scale up instead.
- Don't use accent colors as UI chrome (buttons, nav, borders) — they belong inside content.
- Don't use a non-condensed serif or a rounded sans — the face pairing is the signature.
- Don't rely on hover states for feedback; the site barely uses them. Use focus rings and motion-driven transitions instead.

---

## 8. Responsive Behavior

Three breakpoints: **768, 1024, 1280**. Header padding of `36.4014px` hints at a rem/clamp-based system underneath. On smaller screens, the site swaps in a dedicated mobile nav container (`rgb(220, 220, 220)` surface) — the one place gray appears as UI chrome rather than an accent inside content. Typography holds its character across sizes; a 36px condensed headline can compress to a still-expressive 28–32px without losing its voice because the face is doing the work.

---

## 9. Agent Prompt Guide

> Build a UI that matches ToyFight's design language.

Set the canvas to warm off-white `rgb(250, 246, 239)` and ink text `rgb(13, 13, 14)` — never pure white, never pure black. Use **SpeziaCondensed** for display, body, links, and buttons (all at 18–36px, weight 400), and **FKRasterGrotesk** for sub-heads, captions, UI labels, inputs, and fine print (11–12px, weight 400). Fine print should be uppercase with ~0.88px tracking. Hold every weight at 400; drive hierarchy by swapping typeface and scaling size. Primary links/buttons are a solid ink pill (`rgb(13, 13, 14)` bg, `rgb(241, 237, 231)` text) with matching border and no shadow. Secondary links are transparent with ink text — hover is near-invisible, let focus rings do the interaction signaling. Cards live on a `rgb(241, 237, 231)` surface — a whisper above the canvas, no shadow needed. Wrap media in a dark `rgb(28, 28, 30)` or `rgb(13, 13, 14)` frame so it punches against the cream page. Reserve sugar-pink, lavender, highlighter-yellow, and cream-peach accents for masked content blocks only — never for chrome. Keep corners mostly sharp; use `64px` or `999px` radii only on masked content chips. Let typography do the personality; let the palette stay quiet.

---

*Generated by Sparkbites — extracted from live CSS analysis*
