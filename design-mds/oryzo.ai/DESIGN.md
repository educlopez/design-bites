# Oryzo — Design System Reference

## 1. Visual Theme & Atmosphere

Oryzo is a straight-faced product launch for "the world's most unnecessarily sophisticated cork coaster" — a deadpan parody of AI hype, built by the award-winning studio Lusion. The craft is the joke: the page treats a humble cork disc with the reverent visual language of a flagship silicon launch, so the design has to be genuinely premium for the satire to land. The canvas is a warm, edible palette — cork-cream text on near-black, with a single molten-orange accent that reads like a heat warning. Everything is set in the Halyard variable family, held at a confident medium weight and pushed almost entirely to uppercase, giving the page the clipped, technical cadence of a spec sheet. The atmosphere is luxurious, dry-humored, and obsessively considered: a coaster rendered as if it were a frontier AI model.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(255, 237, 215)` (`#ffedd7`) — cork-cream, the primary text/ink and brand "white"; never pure white
- `rgb(16, 9, 4)` (`#100904`) — espresso black, the page ground and inverted text
- `rgb(56, 36, 22)` (`#382416`) — brown, secondary link/surface fill

**Accent**
- `rgb(220, 80, 0)` (`#dc5000`) — molten orange, the single hot accent: primary buttons, focus borders, progress chips. Used sparingly, like a thermal cue.

**Earth / sustainability greens** (scoped to the sustainability section only)
- `rgb(68, 82, 49)` (`#445231`) — deep olive
- `rgb(93, 108, 73)` (`#5d6c49`) — lighter olive
- `rgb(246, 224, 198)` (`#f6e0c6`) — pale oat (the green section's inverted card)

**Neutrals**
- `rgb(108, 95, 81)` (`#6c5f51`) — grey-brown, muted progress/meta surfaces
- `rgba(32, 25, 20, 0.75)` / `rgba(12, 10, 10, 0.92)` / `rgba(0, 0, 0, 0.9)` — layered scrim overlays for media and WebGL canvases

The system is fundamentally bi-tonal — cork-cream on espresso — with orange as the only saturated voice. Greens are a guest palette that appears only where the copy turns to sustainability, never as global chrome.

---

## 3. Typography Rules

Oryzo runs two variable faces: **Halyard Display** (`--display-font`) for nearly everything visible, and **Halyard Text** (`--text-font`) reserved for longer reading copy, with **DM Mono** for technical/spec annotations. Hierarchy is driven by size and the uppercase switch, not by dramatic weight contrast — most type sits at weight 500.

**Typefaces**
- **Halyard Display Variable** — headlines, sub-heads, labels, links: the brand voice
- **Halyard Text Variable** — body / reading copy
- **DM Mono** — `<pre>` blocks, spec callouts, the "model card" technical texture

**Scale** (desktop; sizes scale fluidly, hence the fractional px)

| Role   | Font                 | Size      | Weight | Line-height | Tracking  | Transform |
|--------|----------------------|-----------|--------|-------------|-----------|-----------|
| H1     | Halyard Display      | 68.3px    | 500    | 61.5px      | -1.23px   | none      |
| H2     | Halyard Display      | 28.3px    | 500    | 28.3px      | normal    | uppercase |
| H3     | Halyard Display      | 18.75px   | 500    | 18.75px     | normal    | uppercase |
| H4     | Halyard Display      | 13.3px    | 500    | 14.5px      | normal    | uppercase |
| H5     | Halyard Display      | 12.2px    | 600    | 14.7px      | normal    | uppercase |
| Link   | Halyard Display      | small     | 500    | tight       | normal    | uppercase |
| Pre    | DM Mono              | small     | 400    | 1.33×       | normal    | none      |

**Principles**
- The headline is the only place with negative tracking (`-1.23px`) and tight leading (line-height below font-size) — it sets densely, like a hero stamp.
- Everything structural — H2 through labels and links — is uppercase. Lowercase is reserved for the H1 and reading body, so the page reads as "loud spec sheet, quiet prose."
- Weight is nearly constant (500, with 600 only at the smallest H5) — size and case do the hierarchy work.
- Mono (DM Mono) carries the "AI model card" gag: spec tables, temperature sliders, encryption demos all wear monospace to feel machine-authored.

---

## 4. Component Stylings

**Primary buttons**
- Background `rgb(220, 80, 0)` (orange), text `rgb(16, 9, 4)` (espresso), matching dark border — a hot, solid stamp.
- A secondary button variant inverts to cork-cream `rgb(255, 237, 215)` background with espresso text.

**Links**
- Filled brown `rgb(56, 36, 22)` background, cork-cream text, transparent orange border that animates in on interaction.

**Product option chips** (`product-hero-option-item`)
- Brown `rgb(56, 36, 22)` fill, cork-cream text, live orange `rgb(220, 80, 0)` border — the selected/interactive state of the hero configurator.

**Spec / mono blocks** (`<pre>`)
- Translucent cork tint `rgba(255, 237, 214, 0.11)` over the dark ground, cork-cream mono text — a faint card that reads as a code/console panel.

**Border radius**
- `20px`, `12.5px` for cards and panels; `50%` / `100%` for the many circular elements (the coaster itself, dials, badges). Roundness is a literal motif — the copy brags it's "now 37.9% more circular."

**Shadows**
- None in the extracted system. Depth comes from layered dark scrims over 3D/WebGL, not soft shadows.

---

## 5. Layout Principles

- The page is a vertically-scrolling "launch deck": full-bleed dark sections, each one a self-contained gag (model card, encryption demo, sustainability stats, testimonials), interleaved with WebGL/video product hero moments.
- Numeric/technical callouts (`255678`, `T = 10 / T = 1 / T = 0.1`, friction coefficients, harvest ages) are treated as first-class layout objects — big mono numerals act as section anchors, mimicking a benchmark report.
- A single decisive accent (orange) punctuates an otherwise cork-on-black field, so the eye is led by warmth, not by boxes.
- Media and 3D canvases sit under graduated black scrims (`rgba(12,10,10,0.92)` → `rgba(0,0,0,0.9)`) so text stays legible over motion.

---

## 6. Depth & Elevation

Depth is built from **scrims and 3D**, not from shadow:
- **Layered overlays** — a stack of near-black translucent panels (`rgba(32, 25, 20, 0.75)`, `rgba(12, 10, 10, 0.92)`, `rgba(0, 0, 0, 0.9)`) darken WebGL/video so foreground type floats above the simulation.
- **Surface tints** — the rare lifted card is a whisper-light cork tint (`rgb(246, 224, 198)`, luminance 0.89) on the cream ground, or a faint `rgba(255,237,214,0.11)` panel on the dark ground.
- **The real depth is the canvas** — a Lusion-grade interactive 3D coaster and fluid/Fresnel effects supply the actual sense of dimension; the CSS layer stays deliberately flat so the WebGL reads as the hero.

No `box-shadow` in the system.

---

## 7. Do's and Don'ts

**Do**
- Use cork-cream `#ffedd7` as the brand "white" and espresso `#100904` as the ground — never pure white or pure black for content.
- Set structural type (sub-heads, labels, links) in uppercase Halyard Display at weight 500; reserve lowercase for the H1 and reading copy.
- Let one molten-orange `#dc5000` carry every primary action and hot accent; keep the rest bi-tonal.
- Wear DM Mono for any "technical" element — specs, sliders, numbers, console gags — to sell the AI-model-card conceit.
- Lean into circles: `50%`/`100%` radii, dials, the coaster itself.
- Stack dark translucent scrims over 3D/video so type stays readable on motion.

**Don't**
- Don't introduce pure `#ffffff` or `#000000` for surfaces or text — the warmth is the brand.
- Don't add drop shadows for elevation — use scrim layering and the 3D canvas instead.
- Don't let the greens leak outside the sustainability context; they are a scoped guest palette.
- Don't over-use orange — its power is its scarcity.
- Don't set big headings with positive tracking; the H1 wants tight, dense, slightly negative spacing.

---

## 8. Responsive Behavior

A single hard breakpoint near **768px** (`767.98 / 768`) splits mobile from desktop. A dedicated `mobile-only` espresso surface (`rgb(16, 9, 4)`) swaps in for small screens. Type sizes are fluid (note the fractional px values like `68.3333px`) rather than stepped, so the dense uppercase rhythm holds from phone to desktop. The heavy WebGL/3D moments are the main responsive consideration — they degrade to video/poster frames where the live canvas is too costly.

---

## 9. Agent Prompt Guide

> Build a UI that matches Oryzo's design language.

Set the ground to espresso `#100904` and all text to cork-cream `#ffedd7` — never pure black or white. Use **Halyard Display** (a humanist variable sans) for headlines, sub-heads, labels, and links, all at weight 500; push everything structural to UPPERCASE and keep only the big H1 and reading body in lowercase. The H1 is large (~68px), with tight leading and slightly negative tracking, so it sets as a dense hero stamp. Use a single molten-orange `#dc5000` for every primary button (orange fill, espresso text, dark border) and for live focus/selection borders — keep the rest of the page strictly cork-on-espresso. Render any "technical" element — spec tables, sliders, big benchmark numerals, console gags — in **DM Mono** to sell a deadpan AI-model-card tone. Use circular shapes generously (`border-radius: 50%`/`100%`) and modest `12.5–20px` radii on cards. Add no drop shadows; build depth by stacking near-black translucent scrims (`rgba(0,0,0,0.9)` and friends) over video or WebGL, and let an interactive 3D hero supply the real dimension. Reserve a small olive-green palette (`#445231`, `#5d6c49`, `#f6e0c6`) strictly for a sustainability section. Keep the whole thing premium, dry, and over-engineered — the polish is the punchline.

---

*Generated by Sparkbites — extracted from live CSS analysis*
