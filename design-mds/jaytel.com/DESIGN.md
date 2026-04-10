# jaytel.com — Design System

## 1. Visual Theme & Atmosphere

Jaytel is a product company that designs like one. The interface is clean, structured, and confident — a white canvas with a single electric-blue accent that does all the heavy lifting. The palette is professionally restrained: off-whites, a thorough grey scale from `#F7F7F7` to `#333`, and one chromatic colour (`#2B47FF`) that appears on every interactive surface.

System-ui is the chosen typeface — a deliberate choice to feel native to the OS, reducing friction and increasing perceived trustworthiness. At small sizes, system-ui's optical properties match the platform's own UI, making Jaytel's interface feel like it belongs in the same ecosystem as the tools it supports.

The layout uses a named grid system with CSS custom properties for columns, gaps, and responsive span patterns. Transitions use a custom spring easing curve, giving interactions a physical feel rather than a linear snap.

---

## 2. Color Palette & Roles

**Neutrals — the foundation:**

| Role | Token | Value | Notes |
|------|-------|-------|-------|
| Page background | `--theme-background` / `--color-white` | `#ffffff` | |
| Surface / cards | `--theme-surface` / `--color-off-white` | `#F3F3F3` | Slight warmth |
| Subtle bg | `--color-grey-50` | `#F7F7F7` | Hover states |
| Dividers | `--color-grey-100` | `#eeeeee` | |
| Secondary text | `--color-grey-200` / `--theme-text-secondary` | `#BABFC5` | |
| Label / tertiary | `--color-grey-500` / `--theme-text-tertiary` | `#73808C` | |
| Mid text | `--color-grey-600` | `#595959` | |
| Strong text | `--color-grey-700` | `#333333` | |
| Primary text | `--theme-text-primary` / `--color-black` | `#000000` | Pure black |
| Off-black | `--color-off-black` | `#0f0f0f` | High contrast alt |

**Accent — the only colour:**

| Role | Token | Value | Notes |
|------|-------|-------|-------|
| Brand / CTA | `--color-primary` / `--theme-accent` | `#2B47FF` | Electric blue |
| Hover accent | `--color-primary-dark` / `--theme-link-hover` | `#245EFF` | Slightly deeper |
| Light blue tint | `--color-light-blue` | `#c5d3dd` | Muted, for info states |

The accent is assertive. It appears on buttons, links, labels, and CTAs. Everything else is achromatic — this contrast makes the blue feel like a system signal rather than decoration.

---

## 3. Typography Rules

Single typeface: **system-ui** (OS-native sans-serif). No web font loaded — this is an intentional performance and authenticity decision.

| Role | Size | Weight | Line Height | Tracking |
|------|------|--------|-------------|----------|
| H2 (section heading) | 24px | 400 | 27.6px (1.15×) | −0.16px |
| Body / dialogs | 16px | 400 | normal | normal |

The type scale is minimal in what was captured — system-ui adapts to whatever the OS renders. Weight 400 is used throughout; differentiation comes from size and colour. No bold headings, no heavy display type — this keeps the interface feeling calm and functional rather than promotional.

Notable: no custom display or serif layer exists. The brand voice is expressed through layout and the accent colour, not typographic personality.

---

## 4. Component Stylings

**Primary Buttons**
- Background: `--theme-button-background` (`#2B47FF`)
- Text: `--theme-button-text` (`#ffffff`)
- Hover: `--color-primary-dark` (`#245EFF`)
- Spring easing transition on all interactive state changes

**Links**
- Default: `--theme-link` (`#2B47FF`)
- Hover: `--theme-link-hover` (`#245EFF`)
- Navigation links use `--color-grey-200` (`#BABFC5`) — deliberately muted

**Cards / Elevated surfaces**
- Background: `--theme-l2-background` (`#ffffff`)
- Shadow: `drop-shadow(0px 20px 32px rgba(0,0,0,0.1))`
- Hover shadow: `drop-shadow(0px 2px 4px rgba(0,0,0,0.05))` — shadow reduces on hover (card "settles")

**Labels**
- Default: `--theme-label` (`#73808C`)
- Accented: `--theme-label-accent` (`#2B47FF`)

**Borders**
- `--theme-border`: `#BABFC5` — same as secondary text, consistent mid-grey

---

## 5. Layout Principles

Jaytel uses a named CSS grid system:

- `--grid-columns`: 8 columns
- `--grid-gap`: 16px
- `--grid-width`: 100vw
- Responsive span tokens: `--span-centered-xs/sm/med/lrg/full` — all set to `1 / -1` (full-width on all viewports, suggesting content constrains internally)

Spacing scale is extensive, running from `--spacing-0` (2px) through `--spacing-256` (16rem), providing fine-grained control over padding and margins.

Breakpoints:
- Tablet: `752px`
- Desktop: `1145px`

The layout philosophy is constrained-width content blocks centered within a full-width grid, with generous spacing at the macro level.

---

## 6. Depth & Elevation

Two-tier shadow system using CSS `filter: drop-shadow` (not `box-shadow`):

| Level | Usage | Value |
|-------|-------|-------|
| L2 resting | Cards, panels | `drop-shadow(0px 20px 32px rgba(0,0,0,0.1))` |
| L2 hover | Same cards on hover | `drop-shadow(0px 2px 4px rgba(0,0,0,0.05))` |

The inversion — large shadow at rest, small shadow on hover — suggests cards are in an elevated "floating" default state that settles closer to the surface when interacted with. This is an uncommon and sophisticated interaction pattern.

Page background and surface (`#F3F3F3`) provide a one-step tonal foundation beneath card whites.

---

## 7. Do's and Don'ts

**Do:**
- Use `#2B47FF` exclusively for interactive and branded elements — one accent, used consistently
- Apply system-ui for the native-platform feel; don't substitute a web font
- Use the card shadow inversion on hover — it's a signature interaction
- Leverage the full grey scale semantically: `#BABFC5` for secondary, `#73808C` for labels, `#000` for primary
- Use the spring easing curve for all transitions to maintain physical feel

**Don't:**
- Introduce a second accent colour — the single-blue system is non-negotiable
- Make navigation links prominent; they are intentionally muted (`#BABFC5`)
- Use box-shadow — the system uses `filter: drop-shadow` exclusively for cards
- Go below 752px grid assumptions without testing the 8-column layout
- Use font weights above 400 for body — restraint is the tone

---

## 8. Responsive Behavior

Explicit breakpoints:
- **Mobile**: below 752px
- **Tablet**: 752px+
- **Desktop**: 1145px+

Grid span tokens suggest all content spans full width at mobile/tablet, constraining only through internal padding. The 8-column grid resolves to a single flow at smaller viewports.

The touch targets on buttons (padded with `#2B47FF` fill) are adequately sized. System-ui scales crisply across all display densities. No font-size scaling tokens detected — sizes remain fixed across breakpoints.

---

## 9. Agent Prompt Guide

**Quick reference:**
- Backgrounds: `#ffffff` (page), `#F3F3F3` (surface), `#F7F7F7` (subtle)
- Text: `#000000` → `#333` → `#595959` → `#73808C` → `#BABFC5`
- Accent: `#2B47FF` (all interactive)
- Font: system-ui, 400 weight throughout
- Grid: 8 columns, 16px gap, 752px / 1145px breakpoints

**Prompt to replicate this aesthetic:**
> "Design a SaaS product interface using system-ui at 400 weight. White background, `#F3F3F3` surface. Single accent `#2B47FF` for all buttons and links. Navigation links are muted `#BABFC5`. Cards have `drop-shadow(0px 20px 32px rgba(0,0,0,0.1))` at rest that reduces on hover. All transitions use spring easing."

**Prompt to extend a component:**
> "Create a feature card for jaytel.com. White background with `drop-shadow(0px 20px 32px rgba(0,0,0,0.1))`. Label in `#73808C` system-ui 400. Heading in `#000000`. Body text `#333`. CTA link in `#2B47FF`. On hover, shadow reduces to `drop-shadow(0px 2px 4px rgba(0,0,0,0.05))`."

---

*Generated by Sparkbites — extracted from live CSS analysis*
