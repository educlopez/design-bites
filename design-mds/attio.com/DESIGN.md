# Attio — Design System Reference

## 1. Visual Theme & Atmosphere

Attio presents itself as precision-engineered enterprise software with a refined, almost academic restraint. The aesthetic is bright and clean — white surfaces, near-black type, no decorative flourish — yet it avoids the sterility of generic SaaS by leaning into micro-detail: tight negative tracking on headlines, carefully tuned font-feature settings, and a layered z-index architecture that signals genuine UI complexity. The overall feeling is a well-lit workspace: nothing shouts, nothing hides. Trust is built through consistency rather than spectacle.

---

## 2. Color Palette & Roles

**Foundation**
- `#ffffff` / `--color-white-100` — page background, card surfaces
- `--color-primary-background` — semantic alias for page BG (light mode default)
- `--color-black-0` — banner/announcement bar backgrounds (near-black accent)
- `--color-black-50` — overscroll bottom tint

**Text hierarchy**
- `--color-black-400` — primary body and button text
- `--color-black-300` — hover state text
- `--color-black-200` — active/pressed text
- `--color-white-900` — disabled foreground

**Interactive surfaces**
- `--color-white-100` — button default background (outline variant)
- `--color-white-300` — ghost button hover background
- `--color-white-400` — ghost button active background
- `--color-white-500` — disabled button border

**Borders**
- `--color-white-800` — outline button default border
- `--color-black-700` — outline button hover/focus border
- `--color-black-500` — outline button active border

No brand color is used decoratively. The palette is deliberately achromatic — color is used only to communicate state, not identity.

---

## 3. Typography Rules

Attio uses two typefaces from the same Inter family — `interDisplay` for headings and `inter` for body — combined with the `"ss03"` OpenType feature enabled globally. This subtle stylistic set likely affects specific character forms (e.g., lowercase `l` disambiguation), reinforcing trust and legibility in a data-dense product.

**Scale**
| Role | Font | Size | Weight | Tracking |
|------|------|------|--------|----------|
| H1 | interDisplay | 64px | 600 | -1.28px |
| H2 | interDisplay | (inferred smaller) | 600 | negative |
| Body / Input | inter | 16px | 500 | -0.16px |

**Key decisions:**
- Headlines carry significant negative letter-spacing, creating a compressed, premium feel
- Line-height on H1 equals font-size (64/64) — a deliberate 1:1 ratio that reads as intentional density
- 500 weight on body text is heavier than typical, improving readability in small UIs
- No serif, no display font experimentation — type is a tool, not a statement

---

## 4. Component Stylings

**Buttons — Outline variant**
- Default: white bg, `white-800` border, `black-400` text
- Hover: border upgrades to `black-700` — border does the signaling, background stays static
- Active: background shifts to `white-300`, border to `black-500`
- Disabled: border recedes to `white-500`, text to `white-900`

**Buttons — Ghost variant**
- Transparent by default; hover adds `white-300` fill
- State changes are incremental and low-contrast — designed for toolbar/icon contexts

**Z-index system (explicit, documented)**
- Mobile nav overlay: 90 / content: 91
- Site header: 92
- Navigation menu: 93
- Dialog overlay: 100 / content: 101

This explicit stacking ladder is a sign of a mature component library.

---

## 5. Layout Principles

Attio uses a multi-height header model with distinct desktop and mobile sub-header states. Desktop sub-header has a set pixel height; mobile sub-header collapses to `0px` when hidden and expands to `63px` when visible. Layout is header-driven — the page background color is a semantic alias, not a hardcoded value, meaning themes can be swapped cleanly. Notably absent: a defined grid system or column count in the extracted data, suggesting layout is handled per-section with flexbox/grid utilities rather than a global scaffold.

---

## 6. Depth & Elevation

Depth is handled architecturally through z-index layers rather than shadow. No `box-shadow` values appear on surface-level elements. The absence of shadow as a depth tool is a deliberate choice — Attio's UI feels flat but layered, not skeuomorphic. Dialogs and menus announce their elevation through z-index and overlay, not blur or lift.

---

## 7. Do's and Don'ts

**Do:**
- Use `--color-*` tokens — never hardcode hex values
- Enable `"ss03"` feature setting on all Inter instances for character consistency
- Apply negative letter-spacing on any heading above 24px
- Follow the documented z-index ladder precisely; never improvise stacking values
- Keep button state changes subtle — border/text shifts, not background floods

**Don't:**
- Introduce color outside the achromatic system for decoration
- Use `font-weight: 400` for body text — 500 is the minimum
- Add box-shadows to compete with the z-index elevation model
- Skip the semantic `--color-page-background` alias in favor of `white`

---

## 8. Responsive Behavior

Breakpoints: mobile-first with a key transition at ~768px (inferred from sub-header mobile/desktop split). The sub-header height variable `--site-header-subheader-height` switches between mobile and desktop values via CSS custom property reassignment — no media query needed in components, only in the `:root` or layout shell. This pattern keeps components ignorant of viewport size.

---

## 9. Agent Prompt Guide

> Build a UI that matches Attio's design language.

Use `interDisplay` (semi-bold, -1.28px tracking) for headings and `inter` (medium weight, -0.16px tracking) for all body and form text. Enable `font-feature-settings: "ss03"` globally. The palette is fully achromatic: white surfaces, near-black text, border-driven interactive states. Never use color decoratively — state changes happen through border-color and background shifts within the white/off-white range. Respect the z-index ladder: nav overlays at 90-91, header at 92, menus at 93, dialogs at 100-101. Components should be stateless regarding viewport — use CSS custom property reassignment at the layout shell level for responsive behavior, not media queries inside components.

---

*Generated by Sparkbites — extracted from live CSS analysis*
