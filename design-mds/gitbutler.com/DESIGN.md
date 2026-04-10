# GitButler — Design Language Reference

## 1. Visual Theme & Atmosphere

GitButler is a developer tool for Git branch management, and its design language reflects exactly that: warm, structured, and systematically thorough. The site opens on a warm off-white base (`rgb(243,242,241)`) — not the cold white of most developer tools, not the dark background of a terminal app. It occupies a middle register: professional but approachable, technical but not austere.

The design system is exceptionally mature. CSS custom properties govern everything — backgrounds, text, borders, semantic states, button variants, diff colors, z-index layers, hover states via `color-mix()`, and even custom cursors. This is the CSS of a team that has shipped a production desktop application and brought that token discipline to the web.

The prevailing mood is a warm stone-and-teal: earthy neutrals punctuated by a teal "pop" accent that signals interactivity without aggression.

---

## 2. Color Palette & Roles

**Foundation**
- Body background: `rgb(243,242,241)` — Warm off-white, almost parchment
- Primary text: `rgb(28,25,23)` — Warm near-black (stone-900 territory)
- `--bg-1` through `--bg-3`: Layered background surfaces
- `--bg-mute`: `clr-gray-95` — muted/disabled surface
- `--bg-overlay`: `hsl(0 0% 83.9% / 0.45)` — semi-transparent overlay

**Accent / Interactive ("pop")**
- `--clr-pop-*` scale: The primary action color — a teal/cyan family
- `--bg-pop`: `clr-pop-95` (very light teal wash for active regions)
- `--fill-pop-bg`: Used for focused elements and primary button fills

**Semantic Colors**
- Safe/green: `hsl(158 67.5% 84.3%)` base, graduated scale
- Warn/amber: `hsl(35 81.4% 81%)` base, `--clr-warn-*` scale
- Danger/red: `--clr-danger-*` scale (diff deletions, destructive actions)
- Purple: `--clr-purple-*` — integrated commits, secondary highlights

**Diff Vocabulary** (unique to a git tool)
- Addition line: `hsl(157 82.1% 89%)` background, `hsl(154 70% 76.5%)` highlight
- Deletion line: `hsl(355 100% 95.1%)` background, `hsl(346 93.4% 88%)` highlight
- Count badges in complementary tints for each state

**Borders**
- `--border-1`: `clr-gray-60`, `--border-2`: `clr-gray-70`, `--border-3`: `clr-gray-80`
- Three-level border system for nesting depth

**What's absent:** No pure black. No pure white. Everything is warmed — the palette lives in the 5% gray-brown range rather than stark neutrals.

---

## 3. Typography Rules

Three semantic font roles:

- **`--font-default`** → `var(--text-fontfamily-default), sans-serif` — **Inter** is the runtime sans-serif (confirmed by `Inter, sans-serif` on blockquotes)
- **`--font-accent`** → `var(--text-fontfamily-accent), serif` — A serif used for editorial/marketing moments
- **`--font-mono`** → `var(--text-fontfamily-mono), monospace` — Used in diff views, code blocks, commit messages

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Blockquote / body | 16px | 400 | 24px |
| Lexical input | 0.8125rem (13px) | — | — |

Inter at 16px/24px is the standard developer-tool reading size — familiar, trusted, invisible in the best sense. The serif accent font appears in marketing contexts to add warmth and credibility.

**Transition system:**
- `--transition-fast: .05s ease` | `--transition-medium: .15s ease` | `--transition-slow: .2s ease`

---

## 4. Component Styling

**Buttons** — A fully specified variant system:
- Solid: fill with pop color, icon at 80% opacity
- Outline variants: pop, gray, danger, purple — each with explicit border, background, text tokens
- Hover: `color-mix(in srgb, fill, white 10%)` — subtle lightening, not a swap
- Outline hover background: 25% opacity fill

**Z-Index Layers** (named, not magic numbers)
- `--z-ground: 1` | `--z-lifted: 2` | `--z-floating: 3` | `--z-modal: 4` | `--z-tooltip: 5` | `--z-blocker: 9999`

**Border Radius**
- `--radius-xl: 20px` — the largest declared radius
- Warm, softly rounded without being pill-shaped

**Custom Cursors** — `cursor-default.svg` and `cursor-pointer.svg` — the site has custom cursor artwork, reinforcing its polished desktop-app aesthetic.

**Layout**
- `--layout-col-gap: 20px`
- `--layout-side-paddings: 80px` — generous outer margin, desktop-first

**Art scene tokens** — `--art-scene-bg: hsl(175 46.4% 89%)`, `--art-scene-fill` — custom illustration zones with coordinated teal-mist backgrounds.

---

## 5. Layout Principles

The layout is desktop-first with 80px side paddings that scale down responsively. Column gaps at 20px maintain tight but breathable internal spacing. The token system suggests panel-based layouts (like the desktop app) with clear surface layering.

Three background levels (`--bg-1`, `--bg-2`, `--bg-3`) plus muted and popup variants enable complex nested UI without relying on borders or shadows for separation.

---

## 6. Depth & Elevation

Elevation is achieved through a combination of:
1. **Background lightness stepping** via the `--bg-1/2/3` token chain
2. **Border weight progression** via `--border-1/2/3`
3. **Color-mix hover states** that lighten surfaces by 4% on interaction — subtle kinetic feedback
4. Named z-index layers for consistent modal/tooltip stacking

The `--bg-overlay` (semi-transparent warm gray at 45% opacity) creates modal backdrops that don't completely disconnect from the page below.

---

## 7. Do's and Don'ts

**Do**
- Use warm off-white (`rgb(243,242,241)`) as the base — never pure white
- Apply the three-tier background system (`--bg-1/2/3`) for depth within panels
- Use `color-mix()` for hover states — don't swap colors, mix them
- Follow the named z-index layer system; never use arbitrary z values
- Apply the diff color vocabulary consistently: green family for additions, red family for deletions

**Don't**
- Use pure black text — `rgb(28,25,23)` is the warm anchor, not `#000`
- Skip the semantic color families for status — all danger/safe/warn/purple states have token chains
- Use generic `cursor: pointer` without the custom SVG cursor assets
- Apply `border-radius` beyond `20px` — the system lives in soft-rounded, not pill territory

---

## 8. Responsive Behavior

The layout system uses explicit padding tokens rather than fluid values. The `--layout-side-paddings: 80px` suggests a stepped responsive reduction (likely 80px → 40px → 16px).

Transition speeds are tokenized but fixed — no responsive motion preference system detected, though the `.05s` fast transition is fast enough for all devices.

---

## 9. Agent Prompt Guide

> "Design in the style of GitButler: warm off-white base `rgb(243,242,241)`, near-black text `rgb(28,25,23)`. Inter as the primary sans-serif; a serif accent font for editorial moments; monospace for code/diffs. Teal 'pop' accent for interactive elements. Three-level background layering for panel depth. Buttons use `color-mix()` hover lightening. `20px` border radius, named z-index layers, 80px side padding. Semantic diff colors: green family for additions, red family for deletions. No pure black or white — everything warmed. Custom cursor SVGs. Professional developer-tool energy that feels warm, not cold."

---

*Generated by Sparkbites — extracted from live CSS analysis*
