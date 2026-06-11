# componine.com — Design Language

## 1. Visual Theme & Atmosphere

Componine is a creative studio that means it. The site opens on a near-black ground — so dark it has a faint warm cast, almost like scorched paper — and saturates the visitor with heavy serif typography, amber flares, and Three.js motion before a single word of copy registers. The atmosphere is deliberately theatrical: this is not a portfolio that lets work speak quietly. The "diabolical edge" from the studio's own description is built into the palette (near-blacks, an olive separator, a cream that leans warm) and into the type choices (Memoir with discretionary ligatures and stylistic alternates active). The result is a dark editorial identity that sits closer to an art publication than a typical agency site.

## 2. Color Palette & Roles

All colors exist in a warm-dark register. No cool greys, no pure white, no saturated neons.

**Backgrounds (dark layer stack)**
- `lab(2.40931 0.896804 1.14596)` → approx. `rgb(6, 5, 4)` — Body background; a near-black with a barely perceptible warm brown undertone. Richer than pure black.
- `rgb(30, 20, 15)` — Textured section (`div.bg-texture`); warmer, darker than body — used for hero/feature areas.
- `rgb(55, 56, 40)` — Separator section; an earthy olive-brown that breaks the all-black monotony without introducing a foreign hue.

**Text & foreground**
- `lab(94.3607 -0.24718 2.65788)` → approx. `rgb(242, 241, 239)` — Primary text; a warm off-white, never pure white. The slight yellow cast keeps it in the warm family.

**Accent**
- `rgb(249, 166, 2)` — Amber/gold; the sole saturated accent. Used sparingly as a container highlight — a single warm flame in the darkness.

**Light surfaces (overlays/panels)**
- `rgb(254, 253, 248)` — Explore panel; a cream near-white that appears on interactive overlays, creating maximum contrast against the dark ground.
- `rgb(229, 227, 223)` — Mid-surface; warm light grey for secondary surface layers.

**Button**
- `lab(35.736 0 0 / 0.75)` — Semi-transparent dark grey; blends into dark backgrounds without fully disappearing.

## 3. Typography Rules

Two typefaces in strong contrast:

**Memoir** — A display serif with character. Used for all headings (h1–h4). The distinguishing feature: OpenType features `"dlig"` (discretionary ligatures) and `"salt"` (stylistic alternates) are active — meaning Memoir renders with alternate letterforms and special ligature pairs that standard fonts don't show. This is a deliberate decision that adds micro-variation and craft to headlines.

**Helvetica Neue / Arial** — A neutral system sans-serif stack for body copy and paragraphs. The starkness of Helvetica Neue against Memoir's ornamentation creates the intended tension.

| Element | Font | Size | Weight | Leading | Tracking | OpenType |
|---------|------|------|--------|---------|---------|---------|
| h1 | Memoir | 32px | 400 | 35.84px (1.12) | −1% | dlig, salt |
| h3 | Memoir | 32px | 400 | 38.4px (1.2) | −1% | dlig, salt |
| h4 | Memoir | 24px | 400 | 28.8px (1.2) | −1% | dlig, salt |
| body / p | Helvetica Neue | 14px | 400 | 19.6px (1.4) | normal | — |

Memoir runs at weight 400 across all heading levels — the size creates hierarchy, not weight. Negative tracking (−1%) tightens the serif headlines for a display-grade appearance at relatively modest sizes. Body copy at 14px keeps information density high without crowding.

## 4. Component Stylings

**Radius** — A single viewport-relative value: `--radius: 6vmin`. This is unconventional and deliberate: the rounding scales with viewport size, so elements feel proportionally rounded on every screen. The only other radius is `999px` (pill) for specific label elements.

**Buttons** — Semi-transparent dark background (`lab(35.736 0 0 / 0.75)`) with warm off-white text. No border visible in default state. Subtle, not prominent — the site does not push CTAs aggressively.

**Separator sections** — The olive-brown `div.separator-section` (`rgb(55,56,40)`) acts as a palette break between dark sections, introducing earth tone rhythm.

**Scroll indicator** — A white line (`rgb(255,255,255)`) used as a progress or scroll cue element; high contrast against the dark ground.

**Custom CSS properties** — `--count: 4`, `--radius: 6vmin`, `--width: 1vmin`, `--duration: 8s` — the duration and count suggest a looping animation or Three.js-driven element on the page.

## 5. Layout Principles

Built on Next.js with Three.js for motion/WebGL. Breakpoints: `520px / 768px / 1024px / 1280px` — a standard four-point responsive ladder.

Spacing is section-driven rather than token-driven (no explicit spacing custom properties beyond the radius). The grid overlay pattern (`div.grid-overlay__column`) suggests a visible baseline or column grid as a design element, not just a layout aid. The `--count: 4` custom property likely drives a four-column overlay grid.

## 6. Depth & Elevation

Depth is built through the warm dark stack and the olive separator, not shadows. A single shadow definition exists. Layers:
- `rgb(6,5,4)` body — deepest
- `rgb(30,20,15)` textured sections — mid depth
- `rgb(55,56,40)` olive separators — surface accent
- `rgb(242,241,239)` text / `rgb(254,253,248)` panels — highest

Three.js adds kinetic depth — motion over a static dark ground is the primary elevation language.

## 7. Do's and Don'ts

**Do:**
- Use the warm near-black `rgb(6,5,4)` — not `#000000`. The warmth is the identity.
- Keep Memoir at weight 400 with `font-feature-settings: "dlig", "salt"` — both features are load-bearing.
- Use Helvetica Neue for body copy; the classic sans against the ornate serif creates the intended tension.
- Apply `border-radius: 6vmin` for viewport-scaled rounding on major containers.
- Use amber `rgb(249,166,2)` as the single warm accent — once, sparingly.
- Keep text at warm off-white `rgb(242,241,239)`, never pure white.

**Don't:**
- Don't add cool greys or blues — the palette is entirely warm.
- Don't bold Memoir headings; the weight 400 restraint is intentional.
- Don't use pixel-fixed border-radius where `6vmin` is the design intent.
- Don't add multiple accent colours; the amber is the sole pop.
- Don't use standard Tailwind sans as body copy — Helvetica Neue is the specific choice.

## 8. Responsive Behavior

Four breakpoints (520 / 768 / 1024 / 1280px):
- Below `520px`: Tight single-column; headings scale down.
- `520px–768px`: Small tablet / large phone.
- `768px–1024px`: Standard tablet to small desktop.
- `1024px–1280px`: Desktop; full layout expression.

The viewport-relative `6vmin` radius means component rounding automatically scales across all breakpoints — no per-breakpoint radius overrides needed.

## 9. Agent Prompt Guide

> "Design in the style of componine.com: near-black warm body `rgb(6,5,4)`, warm off-white text `rgb(242,241,239)`, amber accent `rgb(249,166,2)` used once. Memoir serif at weight 400 with `font-feature-settings: 'dlig', 'salt'` for all headings; Helvetica Neue for body copy at 14px. Border-radius: `6vmin` (viewport-relative) on major containers, `999px` for pills. Olive-brown `rgb(55,56,40)` for section separators. No cool tones, no shadows — depth via warm dark colour stack."

---

*Generated by Sparkbites — extracted from live CSS analysis*
