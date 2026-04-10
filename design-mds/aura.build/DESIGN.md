# Aura — Design System Reference

## 1. Visual Theme & Atmosphere

Aura presents a clean, modern developer-tool aesthetic built entirely on a neutral grayscale foundation. The design is unapologetically minimal — white canvas, near-black text, light gray borders — with no brand color in sight. What distinguishes it from generic SaaS is the precision in its typographic scale and the care given to interactive focus states: double-ring focus rings signal accessibility consciousness. The overall atmosphere feels like a well-designed IDE sidebar: functional, uncluttered, and designed for extended use without visual fatigue.

---

## 2. Color Palette & Roles

**Page & Surface**
- `hsl(0 0% 100%)` / `rgb(255,255,255)` — page background
- `hsl(0 0% 98%)` — card and popover surfaces
- `hsl(0 0% 96%)` — sidebar accent / subtle hover fills
- `hsl(0 0% 90%)` — footer background, border default

**Text**
- `hsl(0 0% 9%)` / `rgb(23,23,23)` — primary foreground (headings, body)
- `rgb(115,115,115)` — secondary text (h3 labels, captions)

**Interactive**
- `hsl(0 0% 20%)` — sidebar primary, focus ring outer color
- `hsl(0 0% 45%)` — muted text and secondary actions

**Code / Syntax**
- Background: `rgb(38,38,38)` — dark code block surface
- Foreground: `rgb(245,245,245)` — code text

**Slider (subtle)**
- Track: `rgba(0,0,0,0.05)`
- Active: `rgba(0,0,0,0.1)`

The palette contains zero hue. Every decision is lightness-based — the design trusts contrast ratios over color to communicate hierarchy.

---

## 3. Typography Rules

Aura uses a single typeface — **Inter** — with an unusually rich set of OpenType features: `"calt"`, `"rlig"`, `"salt"`, `"ss01"`, `"ss02"`. This combination activates contextual alternates, discretionary ligatures, and multiple stylistic sets, making the type feel custom-tuned even without a custom font.

**Scale**
| Role | Size | Weight | Tracking |
|------|------|--------|----------|
| H1 | 60px | 500 | -0.16px |
| Label / UI text | 14px | 500 | -0.16px |

- H1 at medium weight (500) rather than bold keeps headlines approachable and avoids visual aggression
- Line-height on H1 is 1:1 (60/60) — same compressed ratio as premium product UIs
- `-0.16px` tracking appears to be applied universally, not just at display sizes — creating a cohesive tightness throughout

---

## 4. Component Stylings

**Input fields**
- Default: white bg, `rgb(230,230,230)` border, `rgb(23,23,23)` text
- Focus: double-ring — inner `rgb(255,255,255)` 2px, outer `rgb(51,51,51)` 4px — a clear and accessible focus indicator
- No hover state on inputs — the jump from resting to focus is direct

**Sidebar**
- Distinct token set (`--sidebar-*`) with its own background, border, ring, and accent values
- Sidebar primary `hsl(0 0% 20%)` is darker than body text, suggesting active navigation items

**Code blocks**
- Dark surface (`rgb(38,38,38)`) islands within the light-mode page — high contrast inversion zones

---

## 5. Layout Principles

Aura uses a wide breakpoint range: 600, 640, 768, 1024, 1280, 1400, 1536, 1920px. The presence of 1920px signals that the layout is designed for large desktop displays, likely for a dashboard or canvas product. The footer carries a slightly off-white background (`rgb(250,250,250)`) — a near-invisible surface shift that defines the page bottom without a hard line. No explicit column grid or max-width is surfaced in the custom properties, suggesting layout is utility-class driven.

---

## 6. Depth & Elevation

Depth is minimal and functional. The primary elevation signal is the double-ring focus state — not a shadow, but a border-outset technique. Code block dark islands create visual depth through contrast inversion rather than shadow. No `box-shadow` values appear on interactive components, keeping the UI resolutely flat.

---

## 7. Do's and Don'ts

**Do:**
- Apply all Inter OpenType features: `font-feature-settings: "calt", "rlig", "salt", "ss01", "ss02"`
- Use the double-ring focus pattern (`2px white inner + 4px dark outer`) on all interactive inputs
- Treat the grayscale palette as absolute — do not introduce hue for decoration
- Use dark code blocks as contrast anchors within the light canvas

**Don't:**
- Add box-shadows to surface components — depth is achieved through background lightness steps
- Use `font-weight: 700` casually — medium (500) is the intended display weight
- Introduce color tokens for interactive states — use lightness shifts only
- Mix custom font stacks with system fonts in the same context

---

## 8. Responsive Behavior

Aura's breakpoint set is granular at the low end (600/640/768) and sweeps to large-screen targets (1400/1536/1920). The header uses a transparent background on the page but retains a `rgba(230,230,230,0.3)` border at low opacity — it effectively disappears until needed. At mobile sizes, the sidebar accent system (`--sidebar-*`) likely collapses into a drawer pattern.

---

## 9. Agent Prompt Guide

> Build a UI that matches Aura's design language.

Use Inter exclusively with `font-feature-settings: "calt", "rlig", "salt", "ss01", "ss02"`. The entire palette is grayscale: white page, `rgb(23,23,23)` text, `rgb(230,230,230)` borders, `rgb(250,250,250)` footer surface. H1 is 60px/500 weight with a 1:1 line-height. Interactive focus states use a double-ring: 2px white inner, 4px dark outer. Elevate code or technical content with a dark `rgb(38,38,38)` island surface. Avoid all box-shadows and all color except on the code syntax surface.

---

*Generated by Sparkbites — extracted from live CSS analysis*
