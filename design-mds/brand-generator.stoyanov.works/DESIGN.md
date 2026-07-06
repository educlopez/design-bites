# Brand Assets Generator (stoyanov.works) — Design System Reference

## 1. Visual Theme & Atmosphere

This is a tool that generates brand assets, and it dresses itself accordingly: the interface reads like a type specimen sheet rather than a SaaS dashboard. The canvas is a warm off-white paper (`rgb(250, 249, 247)`), not clinical white, giving the generator the feel of a print studio worksheet. A single custom grotesk, **Telegraf**, carries every label, link, and button — the kind of geometric sans that brand-identity studios reach for because it's confident at both display and micro sizes. Ink-black text (`rgb(0, 0, 0)`) sits on the paper canvas, and the primary interactive surface flips the relationship entirely: a near-black panel (`rgb(26, 26, 26)`) that reads as a printed swatch or a inverted brand card. The overall atmosphere is restrained, functional, and typographically literate — a tool built by people who care about the thing it produces.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(250, 249, 247)` — page canvas (warm paper white, luminance 0.977)
- `rgb(246, 245, 243)` — secondary surface, a hair dimmer than the canvas (luminance 0.961) — used for adjacent panels/cards
- `rgb(26, 26, 26)` — inverted dark surface (luminance 0.102) — the brand-card / preview panel register

**Text & ink**
- `rgb(0, 0, 0)` — body text and default borders — true black, not the near-black used elsewhere, so body copy reads as the sharpest ink on the page
- `rgb(102, 102, 102)` — input text/border, a mid-gray that keeps unfocused form fields quiet
- `rgb(51, 51, 51)` — select text, a shade lighter than pure black
- `rgb(187, 187, 187)` — link text, a pale gray that recedes against the paper canvas

**Interactive**
- Button: `rgb(34, 34, 34)` background, `rgb(255, 255, 255)` text, `rgb(34, 34, 34)` border — a charcoal-black stamp with white type, the darkest solid chrome on the page
- Link border: `rgb(187, 187, 187)` on the sides and top, dropping to `rgb(85, 85, 85)` on the bottom edge — an asymmetric underline-style border rather than a flat rule
- Select: `rgb(255, 255, 255)` fill, `rgb(51, 51, 51)` text, `rgb(221, 221, 221)` border — the one element that reverts to a conventional white form-field treatment

The palette is essentially monochrome — paper, ink, and a run of grays — with the charcoal button as the only near-black "accent." Color isn't doing brand work here; typography and tonal contrast are.

---

## 3. Typography Rules

**Typeface:** Telegraf (with `system-ui, -apple-system, sans-serif` fallback) — a single custom grotesk used everywhere except one native input, which quietly falls back to `Arial`.

**Scale**

| Role    | Font                          | Size       | Weight | Line-height | Tracking  | Transform |
|---------|-------------------------------|------------|--------|-------------|-----------|-----------|
| Body    | Telegraf                      | 16px       | 400    | normal      | normal    | none      |
| Link    | Telegraf                      | 10px       | 400    | 15px        | 0.2px     | none      |
| Button  | Telegraf                      | 11px       | 400    | normal      | 0.44px    | none      |
| Select  | Telegraf                      | 11px       | 400    | normal      | normal    | none      |
| Label   | Telegraf                      | 11px       | 400    | normal      | 0.44px    | none      |
| Input   | Arial (fallback, not Telegraf)| 13.3333px  | 400    | normal      | normal    | none      |

**Principles**
- Weight never moves — everything sits at 400. Hierarchy comes from size and letter-spacing alone: body copy runs large and loose at 16px, while every UI label (link, button, select, label) drops to 10–11px with small positive tracking to keep the micro-type legible.
- Buttons and labels share the same tracking value (`0.44px`), tying the two together as the same "control" register.
- The native `<input>` is the single typographic outlier — it renders in `Arial` at browser-default size (`13.3333px`) rather than Telegraf, a tell that this one field was left unstyled. Treat this as an implementation gap, not a design decision, when rebuilding the system: give inputs Telegraf at 11–13px to match the rest of the control set.

---

## 4. Component Stylings

**Buttons** (primary action)
- Background `rgb(34, 34, 34)`, text `rgb(255, 255, 255)`, matching border — a solid charcoal stamp, the darkest filled surface in the UI
- Telegraf 11px with 0.44px tracking, no uppercase transform

**Links**
- Transparent background, `rgb(187, 187, 187)` text
- Border present on all sides but asymmetric: `rgb(187, 187, 187)` top/sides, `rgb(85, 85, 85)` bottom — reads as a soft underline rather than a boxed pill
- Telegraf 10px, tightest type on the page

**Selects**
- White fill (`rgb(255, 255, 255)`), `rgb(221, 221, 221)` border, `rgb(51, 51, 51)` text
- The only component that keeps a conventional filled-field look rather than the transparent/ink treatment used elsewhere

**Inputs**
- Transparent background, `rgb(102, 102, 102)` text and border — a quiet, low-contrast field defined by a thin gray hairline
- Falls back to system `Arial` rather than Telegraf (see Typography section) — worth normalizing if extending this system

**Labels**
- Telegraf 11px, 0.44px tracking — same register as buttons, reinforcing that labels and actions belong to the same control layer

**Shadows / radii:** none detected in the extracted styles — depth and shape are not part of this system's vocabulary at the base-element level.

---

## 5. Layout Principles

- Body has zero padding/margin at the root — the page delegates all spacing to inner containers rather than the document root.
- Three tonal surfaces do the layout work instead of borders: the paper canvas (`rgb(250, 249, 247)`), a barely-dimmer secondary surface (`rgb(246, 245, 243)`), and the near-black inverted panel (`rgb(26, 26, 26)`). Sectioning is achieved through luminance steps, not rules or shadows.
- No breakpoints were captured in the extracted data — treat the layout as needing verification at tablet/mobile widths rather than assuming a specific grid.
- Given the tool's purpose (generating brand assets), expect a control column (selects, inputs, labels, buttons) paired with a live preview area — the dark `rgb(26, 26, 26)` surface is the natural candidate for that preview/output panel, contrasting against the paper-toned control surfaces.

---

## 6. Depth & Elevation

Depth here is entirely tonal, not shadow-based — no `box-shadow` or border-radius values were detected anywhere in the system. Three luminance steps carry all the elevation cues:
- Canvas (`luminance 0.977`) → secondary surface (`luminance 0.961`) is a whisper-thin step, just enough to separate a panel from the page without a border.
- The inverted dark surface (`luminance 0.102`) is the one dramatic jump in the system — it doesn't sit "above" the canvas so much as it flips polarity, functioning as a distinct register (likely the preview/output zone) rather than a raised card.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(250, 249, 247)` as the base canvas — never pure white.
- Set all UI type in Telegraf; reserve size (10–16px) and tracking (0.2–0.44px) as the only hierarchy tools, keeping weight fixed at 400.
- Use the charcoal `rgb(34, 34, 34)` fill exclusively for the primary button — it should stay the darkest filled surface on the page.
- Treat the near-black `rgb(26, 26, 26)` surface as a polarity flip (dark panel/preview), not as a shadow-elevated card.
- Give links their asymmetric border treatment (lighter top/sides, darker bottom) rather than a flat underline.

**Don't**
- Don't introduce drop shadows or border-radius for elevation or shape — none exist in the source system; tonal contrast alone carries depth.
- Don't let inputs fall back to system `Arial` — extend the Telegraf treatment to every form control, including native inputs.
- Don't add bold or heavier weights for emphasis — this system communicates hierarchy through size and tracking only.
- Don't treat the select's white-fill, gray-border look as the template for other controls — it's the one component that differs from the transparent/ink language everything else uses.

---

## 8. Responsive Behavior

No breakpoints were present in the extracted styles, so responsive rules should be treated as unverified rather than absent. Given the compact micro-type scale already in use (10–11px controls, 16px body), the system has headroom to hold its type sizes across viewports without needing aggressive scaling — the main responsive risk is the control-column-plus-preview-panel layout implied by the two-tone canvas/dark-surface pairing, which will likely need to stack vertically on narrow screens.

---

## 9. Agent Prompt Guide

> Build a UI that matches the Brand Assets Generator's design language.

Set the canvas to warm paper white `rgb(250, 249, 247)` — never pure white — with a secondary surface at `rgb(246, 245, 243)` for adjacent panels. Use **Telegraf** (fallback `system-ui, sans-serif`) for every UI element: body at 16px, buttons and labels at 11px with 0.44px tracking, links at 10px with 0.2px tracking and an asymmetric border (light top/sides, `rgb(85, 85, 85)` bottom). Hold weight at 400 everywhere; let size and tracking carry hierarchy. Make the primary button a solid charcoal stamp — `rgb(34, 34, 34)` background, white text, matching border. Give inputs a transparent background with `rgb(102, 102, 102)` text/border (and style them in Telegraf rather than letting them fall back to system Arial). Reserve a near-black `rgb(26, 26, 26)` surface for a preview/output panel — a polarity flip against the paper canvas, not a shadow-raised card. Skip drop shadows and border-radius entirely; this system carries depth through tonal contrast alone.

---

*Generated by Sparkbites — extracted from live CSS analysis*
