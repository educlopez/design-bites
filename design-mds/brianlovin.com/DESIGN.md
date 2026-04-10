# brianlovin.com — Design System Reference

## 1. Visual Theme & Atmosphere

Brian Lovin's personal site is a masterclass in systematic minimalism. Built with Next.js and Tailwind CSS, it uses a rigorously named token system — every colour role is declared as a CSS custom property rather than a raw value. The site has a dual-sidebar application layout (212px primary, 350px secondary) that feels like a productivity tool or design app rather than a portfolio page. The palette is achromatic except for a single warm orange brand colour (`#fc532a`) that appears as both a text and background accent. The typography is Inter throughout — clean, neutral, and system-compatible. What defines this design is its token discipline: the entire colour system is semantic, mapping display names like `--text-color-secondary` to neutral scale values. Shadows are absent; borders are the primary separation mechanism.

## 2. Color Palette & Roles

The colour system is fully semantic — tokens map to a neutral scale anchored at `--color-neutral-*`.

| Token | Approximate Value | Role |
|-------|------------------|------|
| `--background-color-main` | `color-neutral-50` | Page background (near-white) |
| `--background-color-primary` | `color-white` | Primary surfaces, sidebars |
| `--background-color-secondary` | `color-neutral-50` | Secondary panels |
| `--background-color-tertiary` | `color-neutral-100` | Hover/active states |
| `--background-color-quaternary` | `color-neutral-200` | Deepest background fill |
| `--background-color-elevated` | `color-white` | Elevated cards, modals |
| `--text-color-primary` | `color-neutral-900` | Primary body text |
| `--text-color-secondary` | `color-neutral-600` | Secondary/muted text |
| `--text-color-tertiary` | `color-neutral-500` | Tertiary/placeholder text |
| `--text-color-brand` | `#fc532a` | Brand accent text |
| `--background-color-brand` | `#fc532a` | Brand accent fills |
| `--border-color-primary` | `#0000001f` (12% black) | Primary borders |
| `--border-color-secondary` | `#00000017` (9% black) | Secondary/subtler borders |
| `--color-neutral-850` | `#1d1d1d` | Near-black utility |

The orange `#fc532a` is the sole hue in an otherwise fully greyscale system. It appears rarely but unmistakably.

## 3. Typography Rules

**Sole typeface:** Inter (with Inter Fallback) — variable-ready, system-compatible, universally neutral.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| H1 / display paragraphs | 24px | 600 | 32px | normal |
| Body | 16px | 400 | 24px | normal |
| Links | 20px | 400 | 28px | normal |
| Buttons | 18px | 500 | 28px | normal |

The weight range is purposeful: 400 for reading, 500 for interactive affordance, 600 for headings. No extreme weights (700+), no italic emphasis detected. No letter-spacing manipulation — Inter's optical defaults are trusted. The scale is compact and app-like: nothing above 24px was detected, reinforcing the productivity-tool aesthetic.

## 4. Component Stylings

**Navigation sidebar:** Sticky, white background, 212px wide. Subtle `12%` black border separates panes.

**Buttons:** Transparent background by default (`oklab(0 0 0 / 0)`). On hover: `oklab(0 0 0 / 0.08)` — an 8% black overlay. Clean, flat, no border change on hover. Focus uses standard browser outline.

**Links:** Transparent background, near-black text. No hover state detected in computed styles — likely handled via Tailwind group/hover utilities.

**Borders:** Two tiers — `--border-color-primary` at 12% black opacity and `--border-color-secondary` at 9%. These are the primary depth cues in the entire system.

**Extreme border-radius:** `3.35544e+07px` (≈ 33 million px) — a common technique for guaranteed pill/circle shapes regardless of element size. All interactive elements with rounding use this value.

## 5. Layout Principles

Two-sidebar application layout: `--primary-sidebar-width: 212px`, `--secondary-sidebar-width: 350px`. Content area fills the remainder. Single breakpoint at **600px** for mobile collapse. The token-driven colour system implies a design that scales across light/dark themes (though only light mode data was captured). Spacing follows Tailwind's default scale — no custom spacing tokens detected.

## 6. Depth & Elevation

No shadows anywhere in the system. Elevation is communicated through:
1. **Background colour tiers** — four levels (`main`, `primary`, `secondary`, `tertiary`) create visual layering
2. **Transparent border opacity** — 12% and 9% black borders trace edges without shadows
3. **`background-color-elevated`** — explicitly maps to white for components that need to "float"

This is a pure border-and-background elevation system. Shadows would break the flat, app-like precision.

## 7. Do's and Don'ts

**Do:**
- Use semantic colour tokens exclusively — never hard-code neutral values
- Reserve `#fc532a` for a single brand moment per view — it reads loudest when rare
- Use the 8% black hover overlay (`oklab(0 0 0 / 0.08)`) for all interactive states
- Separate layout panes with `--border-color-primary` (12% black) — no divider lines with height
- Use Inter weight 500 for buttons, 600 for headings, 400 everywhere else

**Don't:**
- Add shadows — the system communicates depth through colour tiers only
- Break the token chain with raw hex values in components
- Use the orange accent for more than one or two elements per view
- Introduce type sizes above 24px — this system's visual register is compact
- Use Inter at weights above 600 — the system deliberately avoids heavy text

## 8. Responsive Behavior

Single breakpoint at **600px** — below this, the dual-sidebar layout likely collapses to a single-column stacked view. The narrow mobile threshold (vs typical 768px) suggests the full layout is usable on tablets, with only phones getting a simplified view. Sidebar widths (212px, 350px) are fixed — no fluid scaling detected.

## 9. Agent Prompt Guide

> "Design in the style of brianlovin.com: Next.js app with semantic CSS token system, Inter typeface (400/500/600 weights), light neutral background (`color-neutral-50`). Dual-sidebar layout (212px + 350px). Single warm orange accent (`#fc532a`) for brand moments only. No shadows — use background-color tiers and transparent borders (12% black) for elevation. Pill shapes via extreme border-radius. Minimal hover states: 8% black overlay. Token-first: every colour must map to a named semantic variable."

---

*Generated by Sparkbites — extracted from live CSS analysis*
