# Tegaki (gkurt.com) — Design System

## 1. Visual Theme & Atmosphere

Tegaki — Japanese for "handwriting" — is a docs site for a library that animates handwriting from any font, and its own interface is built with the same restraint you'd want from a typography tool: it gets out of the way. The canvas is pure white, text sits in a quiet slate (`oklch(0.37 0.013 285.805)`, a warm-neutral zinc-700), and the whole system leans on Tailwind's default zinc scale rather than a custom brand gray. There is exactly one accent color doing real work — indigo, wired in through `--color-accent-*` tokens that alias to `--color-indigo-200/600/900/950` — so every place the eye needs to land (links, primary CTAs, focus states) reads as the same considered indigo, never a competing hue. The page body caps at a narrow `42rem` (672px) container, which gives the hero copy and the three-step "Generate → Bundle → Render" explainer the density of a well-set essay rather than a marketing spread. It's a tool built by someone who cares about letterforms, so the shell stays deliberately plain and lets the animated glyphs be the show.

---

## 2. Color Palette & Roles

**Foundation (light)**
- `#ffffff` (`rgb(255,255,255)`) — page canvas, body background
- `#3f3f46` (`oklch(0.37 0.013 285.805)`, zinc-700) — body text, default link/nav/button ink
- `#18181b` (`oklch(0.21 0.006 285.885)`, zinc-900) — h1 text, the darkest ink on the page
- `rgb(17,24,39)` — h2 text; a separate near-black gray, distinct from the zinc scale used everywhere else (likely inherited from a base/Preflight reset rather than the custom token set)
- `#e4e4e7` (zinc-200) — hairline borders (header bottom border)
- `#d4d4d8` (zinc-300, `oklch(0.871 0.006 286.286)`) — input borders, dialog borders

**Accent**
- `--color-accent-200` → indigo-200 `#c6d2ff`
- `--color-accent-600` → indigo-600 `#4f39f6` — the working accent: primary interactive color
- `--color-accent-900` → indigo-900 `#312c85`
- `--color-accent-950` → indigo-950 `#1e1a4d`

**Surfaces**
- Header: `oklch(0.999994 0.0000497986 none / 0.8)` — near-white at 80% opacity, paired with `--blur-sm: 8px` for a glassy, backdrop-blurred sticky bar
- Card/overlay surface: `rgba(252,252,253,0.85)` at luminance 0.989 — a whisper above pure white, barely distinguishable, which is the point

**Semantic / doc-callout family (Starlight-derived tokens, `--sl-color-*`)**
Each hue ships as a low/base/high triad for admonitions inside docs content:
- Orange/amber: low `amber-950` `#451a03`-range, base `amber-900` `#7b3306`, high `amber-200` `#fee685`
- Green: low `green-950`, base `green-900` `#0d542b`, high `green-200` `#b9f8cf`
- Blue: low `blue-950`, base `blue-900` `#1c398e`, high `blue-200` `#bedbff`
- Purple: low `purple-950`, base `purple-900` `#59168b`, high `purple-200` `#e9d4ff`
- Red: low `red-950`, base `red-900` `#82181a`, high `red-200` `#ffc9c9`

**Dark mode**
- Canvas → `--sl-color-black` = zinc-950 `#09090b`
- Nav surface → `#09090b80` (zinc-950 at 50% alpha) — the same glass-header idea, inverted

The palette is disciplined to a fault: one neutral scale, one accent family, and a bank of semantic hues that only ever surface inside callout boxes. Nothing competes with the indigo CTA.

---

## 3. Typography Rules

No custom webfont — Tegaki runs entirely on the system UI stack, which fits a technical tool that wants to feel native and fast rather than branded:
- **Sans**: `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"` (extended with `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", Arial` on most elements)
- **Mono**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace` — reserved for code

**Scale**

| Role | Selector | Font stack | Size | Weight | Line-height |
|---|---|---|---|---|---|
| H1 | `h1` | full sans stack | 44px | 600 | 52.8px |
| H2 | `h2` | short `system-ui, sans-serif` | 24px | 600 | 42px |
| Body | `body` | full sans stack | 16px | 400 | 28px |
| Paragraph | `p` | short `system-ui, sans-serif` | 14px | 400 | 24.5px |
| Link | `a` | full sans stack | 16px | 400 | 28px |
| Button | `button` | full sans stack | 14px | 400 | 24.5px |
| Input | `input` | full sans stack | 16.8px | 400 | 29.4px |

**Tokens on hand**: `--text-xs: .75rem`, `--text-sm: .875rem`, `--text-lg: 1.125rem`, `--font-weight-medium: 500`, `--font-weight-semibold: 600`, `--leading-snug: 1.375`.

**Principles**
- H1 is the only place weight jumps to 600 at real display size (44px) — everything else stays at 400, with H2 as the sole other semibold moment.
- Note the split font-stack: `h1`/`body`/`a`/`button`/`input` get the long emoji-inclusive stack; `h2`/`p` get the terser `system-ui, sans-serif`. Preserve that split rather than normalizing to one stack — it's evidence of two authoring passes (base Tailwind Preflight vs. a later custom pass) and it's harmless to keep.
- Line-heights run generous relative to size (28px on 16px body, 1.75×) — this is a reading-comfort choice appropriate to documentation prose, not a display-tight system like a marketing hero.
- Letter-spacing is `normal` everywhere; no tracking tricks, no uppercase labels detected.

---

## 4. Component Stylings

**Links (default nav/CTA link, e.g. "Skip to content", "GitHub", site title)**
- Transparent background, zinc-700 text and border-color, no visible hover treatment captured
- Focus state is dramatic and intentional: background flips to zinc-800 (`oklch(0.274 0.006 286.033)`), text/border go white, and a five-layer elevation shadow appears (see §6) — the link visually lifts off the page on focus rather than just changing color

**Buttons** (e.g. the search trigger, "SearchCtrlK")
- White background, zinc-700 text, zinc-300 border, no shadow at rest
- Focus swaps to the browser default outline (`auto 1px`, `rgb(16,16,16)`) rather than a custom ring — deliberately unstyled, letting the OS focus indicator do the job

**Inputs**
- White background, zinc-900 text, zinc-300 border — a plain hairline field, 16.8px type, no fill color change on focus captured

**Dialogs**
- White background, black text, zinc-300 border — same hairline language as inputs, just elevated into a modal

**Border radius**
- `4px, 6px, 8px, 12px` — a tight, restrained scale. Nothing pill-shaped; this is a developer-tool corner language, not a consumer-app one.

**Shadows**
- Resting shadow (cards/header): `0 1px 3px rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1)` — Tailwind's stock `shadow-sm`, barely perceptible
- Focus/"lift" shadow: `0 25px 7px rgba(0,0,0,.01), 0 16px 6px rgba(0,0,0,.03), 0 9px 5px rgba(22,24,29,.08), 0 4px 4px rgba(0,0,0,.16), 0 4px 2px rgba(0,0,0,.04)` — a five-layer stack that fades from a huge, near-invisible outer glow down to a tight, denser shadow near the element. This is the signature depth cue of the whole system.

---

## 5. Layout Principles

- Content container caps at `--container-2xl: 42rem` (672px) — noticeably narrower than a typical marketing site's 1200px+ container, which is exactly right for a docs/reading-first product.
- `main` carries `0 0 18px` padding — content sits nearly flush to the header, with a small settling gap at the bottom.
- `section` padding is `0 24px 24px` — horizontal breathing room with no top padding, so sections stack tightly under whatever precedes them.
- `header` padding is `12px 24px` — a compact, low-profile bar, reinforced by the 8px backdrop blur and 80%-opacity background so page content is faintly visible scrolling underneath it.
- `footer` uses `margin: 24px 0 0` and a `24px` gap between children — the footer is built as a flex/grid row with consistent 24px rhythm rather than nested block spacing.
- Base spacing unit is `--spacing: .25rem` (4px) — the whole system is a 4px grid underneath, standard Tailwind default.
- Detected stack: **Astro** (v7.0.3) with **Svelte** islands and **Tailwind CSS** — the Svelte islands are almost certainly the animated-handwriting canvas demos embedded in the docs; the surrounding shell is static Astro.

---

## 6. Depth & Elevation

Elevation here is a story told twice: almost flat at rest, dramatic on focus.

- **At rest**: depth is nearly nonexistent. The header's only separation from content is an `#e4e4e7` (zinc-200) hairline border plus the blur/opacity trick — no shadow does the work of separating chrome from content.
- **Cards/dialogs**: the stock `shadow-sm` (`1px 3px` + `1px 2px -1px`, both at 10% black) is the only resting shadow in the system — deliberately quiet.
- **Focus is where elevation lives**: interactive elements (the skip-link, and by extension any link/button carrying this focus treatment) jump from flat to a five-layer, feathered shadow stack on `:focus`, simultaneously inverting to a zinc-800 background. It reads as the element physically lifting toward the user the moment it's addressed by keyboard or assistive tech — an unusually generous, accessibility-forward interaction, not just a color-swap focus ring.
- **Dark mode** repeats the same low-key philosophy: `--sl-color-bg-nav: #09090b80` is the same translucent-blur nav idea, just inverted tonally.

---

## 7. Do's and Don'ts

**Do**
- Keep the canvas pure white in light mode; use zinc-950 (`#09090b`) as its dark-mode mirror, not pure black.
- Use indigo (`--color-accent-600` / `#4f39f6`) as the single accent — don't introduce a second "brand" hue outside the semantic callout set.
- Cap reading content at `42rem` — resist widening the container just because there's screen space.
- Reserve the five-layer "lift" shadow for focus/keyboard-interaction states — it's a focus signature, not a generic hover effect.
- Keep border radii small (4–12px); this is a dev-tool corner language, not a rounded consumer one.
- Let the system UI font stack do the talking — no custom webfont to load or maintain.

**Don't**
- Don't add hover-color transitions where none were captured — this system signals interactivity through focus states, not hover.
- Don't reach for the semantic hues (amber/green/blue/purple/red) outside doc-callout/admonition contexts — they're scoped to Starlight-style `--sl-color-*` tokens, not general UI chrome.
- Don't apply heavy box-shadows at rest — depth is reserved for the focus moment.
- Don't unify the two typeface stacks (`h1`/`body`/`a`/`button`/`input` vs. `h2`/`p`) — the split is harmless and native to how the tokens were authored.
- Don't use pill-shaped (`999px`) radii — nothing in the extracted radius set goes past `12px`.

---

## 8. Responsive Behavior

No explicit breakpoints were captured in the extracted data, but the token set (`--container-2xl: 42rem`, a 4px base spacing grid, and the compact `12px 24px` header padding) points to a mobile-first, single-column-first layout that simply lets its already-narrow 672px container become the full viewport width on small screens — there's little need for a dramatic breakpoint overhaul when the desktop container was never wide to begin with. The blurred, 80%-opacity sticky header is lightweight enough to persist across all viewport sizes without a mobile-specific simplification.

---

## 9. Agent Prompt Guide

> Build a UI that matches Tegaki's design language.

Use a pure white canvas (`#ffffff`) in light mode and zinc-950 (`#09090b`) in dark mode — never pure black. Body text is zinc-700 (`#3f3f46`), headings step down to zinc-900 (`#18181b`) for h1. Set type in the system UI stack (`ui-sans-serif, system-ui, sans-serif...`) at 16px/28px for body, 44px/600-weight/52.8px for h1, 24px/600-weight/42px for h2 — hold everything else at weight 400. Use indigo (`#4f39f6`) as the one accent color for links, primary actions, and focus rings; don't introduce a second brand hue. Cap content width at `42rem` (672px) so pages read like well-set prose, not a marketing spread. Keep resting elevation minimal — a bare `shadow-sm` (`1px 3px rgba(0,0,0,.1)`) at most — but give focus states a dramatic five-layer lift shadow (`25px 7px`, `16px 6px`, `9px 5px`, `4px 4px`, `4px 2px`, fading from 1% to 16% black opacity) paired with an inverted zinc-800 background, so keyboard focus visibly elevates the element. Use small border radii (4–12px), zinc-200/300 hairline borders for chrome (headers, inputs, dialogs), and reserve amber/green/blue/purple/red only for doc-style callout boxes. Reach for `ui-monospace` for any code.

---

*Generated by Sparkbites — extracted from live CSS analysis*
