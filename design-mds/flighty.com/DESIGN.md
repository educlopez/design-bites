# Flighty — Design Language Reference

## 1. Visual Theme & Atmosphere

Flighty presents a clean, app-marketing aesthetic rooted in pure white and black, with the design philosophy of "get out of the way." The typography and layout do the heavy lifting; decoration is minimal. The site reads more like polished product documentation than a traditional marketing page — confident, airy, and precise.

The only color that breaks the monochrome foundation comes from flight-status metaphors: reds, ambers, and greens that map directly to on-time, delayed, and cancelled states. This is deliberate — color carries semantic weight, never decorative purpose. When you see warm amber here, it means something.

The overall mood is premium utility: a tool built for frequent flyers who trust data more than aesthetics.

---

## 2. Color Palette & Roles

**Foundation**
- `#FFFFFF` — Page background, card surfaces, default containers
- `#000000` — Primary text, borders, button text

**Status / Semantic Colors** (the only color used expressively)
- `rgb(217, 45, 32)` — Alert/cancelled indicator (deep red)
- `rgb(247, 144, 9)` — Warning/delayed indicator (amber)
- `rgb(3, 152, 85)` — On-time/confirmed indicator (green)
- `rgb(254, 240, 199)` — Warm amber tint, background wash for warning states
- `rgb(254, 223, 137)` — Amber mid-tone for contrast layering within alerts

**What's absent:** No brand accent color. No gradients. No decorative tints. The palette intentionally refuses personality — trust is built through restraint.

---

## 3. Typography Rules

Flighty commits entirely to **pangramSansRounded** — a single rounded sans-serif used from the largest headline down to form inputs. The fallback is `"pangramSansRounded Fallback"`, suggesting a custom subset load strategy.

| Level | Size | Weight | Line Height |
|-------|------|--------|-------------|
| H1 | 40px | 700 | 46px |
| Body / Input | 16px | 400 | 24px |

**Feature settings:** `"ss02", "ss03"` are active throughout — these typically enable alternate digit forms or ligatures in pangramSansRounded, adding subtle typographic polish that most visitors won't consciously notice.

The type scale is tight. No dramatic size jumps, no display-level heroics. Rounded letterforms soften what would otherwise feel clinical. Letter spacing is left at `normal` — letting the font's native proportions breathe.

**What's absent:** No serif. No monospace. No text transforms or uppercase labels.

---

## 4. Component Styling

**Cards / Feature blocks**
- White background (`rgb(255, 255, 255)`)
- Layered box-shadow using stacked `rgba(0,0,0,0.06)` values across 6 levels (0px, 1px, 3px, 6px, 12px, 24px spreads)
- This produces a soft, realistic floating effect — not the flat card style common in design systems
- Border radius: `8px` for components, with pill-shaped elements using `~33.5M px` (effectively 50%)

**Status indicators**
- Small `h-2` height strips (likely 8px bars) using the semantic red, amber, green palette
- Used inline within flight cards to communicate delay severity at a glance

**Buttons**
- Transparent background by default
- Black text, black border
- No hover state data captured — likely rely on opacity transitions

**Inputs**
- Same pangramSansRounded as body, maintaining visual consistency throughout the interface

---

## 5. Layout Principles

The layout system uses standard flexbox composition. Spacing is utility-driven (Tailwind classes detected from selectors like `div.flex`, `div.group`). The page builds vertically with generous internal padding, letting content breathe.

No complex grid system is evident from the CSS data. The hierarchy is achieved through typography weight and size alone, not spatial drama.

Side padding and section spacing are not expressed as CSS custom properties — the site relies on utility classes, keeping layout logic co-located with markup.

---

## 6. Depth & Elevation

The shadow system is the most technically sophisticated part of the design. A single compound shadow value stacks 6 layers, all at `rgba(0,0,0,0.06)`, creating a naturally diffused lift that reads more like ambient light than a drop shadow.

```
0px 0px 0px 4px  | ambient ring
0px 1px 1.5px    | contact shadow
0px 3px 3px -1.5 | near lift
0px 6px 6px -3px | mid lift
0px 12px 12px -6 | far lift
0px 24px 24px -12| atmospheric
```

No colored shadows. No inset shadows. Elevation is purely neutral.

---

## 7. Do's and Don'ts

**Do**
- Use color exclusively for semantic status (red = problem, amber = caution, green = good)
- Maintain the white/black foundation for all structural elements
- Layer the 6-stop shadow stack for cards that need to lift off the page
- Use `ss02`/`ss03` OpenType features when loading pangramSansRounded
- Keep border-radius consistent: `8px` for cards, `9999px` for pills

**Don't**
- Introduce decorative color — any non-semantic color will feel wrong here
- Mix font families; pangramSansRounded's rounded personality only works as a singular voice
- Use heavy drop shadows with color tint — the aesthetic depends on neutral elevation
- Add border decorations to text-heavy sections; white space is the divider

---

## 8. Responsive Behavior

The CSS data shows minimal responsive breakpoint logic — no custom properties for fluid type or spacing. The layout likely relies on Tailwind responsive prefixes directly in markup. The lack of `clamp()` or viewport-relative sizes suggests a more stepped responsive approach.

Breakpoints are not explicitly declared as CSS variables, indicating a utility-class-driven responsive strategy rather than a systematic token approach.

---

## 9. Agent Prompt Guide

> "Design in the style of Flighty: clean white background, black text, pangramSansRounded font with `ss02`/`ss03` features enabled. Use color only for semantic status states (red `#D92D20`, amber `#F79009`, green `#039855`). Cards float with a 6-level `rgba(0,0,0,0.06)` compound shadow. Border radius 8px on cards, full-pill on badges. No decorative color, no serif, no gradients. The design should feel like a premium iOS app's marketing site — precise, airy, trustworthy."

---

*Generated by Sparkbites — extracted from live CSS analysis*
