# chanhdai.com — Design System

## 1. Visual Theme & Atmosphere

chanhdai.com is a developer portfolio and component library built with Next.js and Tailwind CSS. Its design philosophy is **clean precision** — a light-mode-first interface that communicates craft through tightly controlled spacing, a strictly defined semantic token system, and restrained use of color. The overall feel is calm and professional, somewhere between a well-maintained open-source documentation site and a personal creative portfolio.

The site runs a comprehensive CSS custom property system built on Zinc (cool grey) tones, with a near-black foreground on pure white. Every color decision maps to a named role (`--background`, `--muted`, `--border`) rather than raw values, revealing a designer who thinks in design tokens, not pixels.

What distinguishes it is the typography pairing: Geist Sans covers the entire interface — no serif, no display typeface, no decorative accent — creating a cohesive, software-native reading experience. The site also includes `--expo-out` easing as a CSS variable, a subtle clue that animations are thoughtfully tuned rather than defaulted.

---

## 2. Color Palette & Roles

All colors defined as CSS custom properties with explicit semantic roles:

**Neutral / structural**:
- `--background`: `#fff` — page canvas
- `--foreground`: `#09090b` — near-black Zinc, primary text
- `--border` / `--input` / `--line`: `#e4e4e7` — consistent border grey
- `--muted`: `#f4f4f5` — subtle fill for inactive areas
- `--muted-foreground`: `#71717b` — secondary/placeholder text
- `--surface`: `#fafafa` — slightly off-white for code blocks and inset areas
- `--ring`: `#9f9fa9` — focus indicator

**Interactive**:
- `--primary`: `#09090b` (background), `--primary-foreground`: `#fafafa` — filled buttons
- `--link`: `#1447e6` — the only pure chromatic color, a strong blue for hyperlinks
- `--secondary`: `#f4f4f5` / `--accent`: `#f4f4f5` — same value, used for ghost/outline button backgrounds

**Status**:
- `--info`: `#009cf5` — informational blue
- `--success`: `#00c758` — confirmation green
- `--destructive`: `#e40014` — error red

**Sidebar system**: Mirrors the main token set with `--sidebar-*` variants, indicating a docs-style navigation panel.

**What's absent**: No dark mode tokens in the default surface. No gradients. No decorative color splashes.

---

## 3. Typography Rules

The site commits entirely to **Geist Sans** — Vercel's open-source typeface — across every element from headings to body to buttons.

| Role | Size | Weight | Line Height | Tracking |
|------|------|--------|-------------|----------|
| H1 | 30px | 600 | 36px | −0.75px |
| H2–H4 | 16px | 500 | 16–24px | none |
| Body | 16px | 400 | 24px | none |
| Paragraphs | 14px | 400 | 20px | none |
| Buttons | 14px | 500 | 20px | none |
| Nav links | 16px | 400 | 24px | none |

Key rules:
- Only H1 uses negative letter-spacing (−0.75px) — everything else runs at default tracking
- The weight range is narrow: 400 (regular) and 500 (medium) for UI, 600 (semibold) for the page title only
- No serif, no monospace, no display face — complete typographic unity
- Buttons use 500 weight at 14px matching paragraph-level sizing, keeping the interface compact
- A custom `--expo-out` easing curve is defined for animation timing, suggesting spring-like transitions

---

## 4. Component Stylings

**Buttons**: Two clear types based on interactive state data:
- **Primary/filled**: `--primary` (`#09090b`) background, `--primary-foreground` text. On hover, slightly transparent (80% opacity on hover). Pill-shaped possible (`3.35544e+07px` radius detected — near-infinite, producing full rounded).
- **Ghost/secondary**: Transparent background, text in `--muted-foreground`, hover brings `--accent` background fill.

**Search bar**: Full-width input with border `--border`, shadow `rgba(0,0,0,0.05) 0px 1px 2px`, and a 3px focus ring in `--ring` (semi-transparent). Keyboard shortcut badge (⌘K) appears inline.

**Border radii**: 6px (inputs, small components), 8px (cards), 12px (larger containers), full-pill for avatars/badges.

**Cards**: Background `--card` (`#fff`) with a 1px inset shadow acting as border (`oklch ring` at 10% opacity), subtle drop shadow on lift. Flat and light.

**Navigation links**: Muted text (`--muted-foreground`) that transitions to full `--foreground` on hover — a clean brightness bump with no transform.

**Progress bar**: Defined via `--bprogress-*` tokens — 2px height, full foreground color, top of page.

---

## 5. Layout Principles

- **Single breakpoint at 600px** — an unusually simple responsive system for a portfolio this polished. The implication is a deliberately minimal layout that works nearly identically on mobile and desktop.
- **Main padding**: `0px 8px` — tight lateral padding, content-forward
- **Header padding**: `8px 8px 0` — compact navigation bar
- **Footer padding**: `0px 8px` — matches main
- Sections have zero padding, relying on child spacing for rhythm
- Layout is almost certainly grid/flex-based per Tailwind conventions, but no explicit grid gaps are exposed in CSS

---

## 6. Depth & Elevation

Elevation is minimal and flat:
- The primary separation mechanism is background color: `--background` (#fff) vs `--surface` (#fafafa) vs `--muted` (#f4f4f5)
- Shadows are very light: `rgba(0,0,0,0.05) 0px 1px 2px` for small lift, `rgba(0,0,0,0.1) 0px 4px 6px -1px` for cards
- Borders use `oklch(0.141/0.1) 0px 0px 0px 1px inset` — an inner ring technique to avoid the "double border" problem with box-border sizing
- No blur effects, no glassmorphism, no dramatic shadows — the aesthetic is deliberately flat with just enough lift to convey interaction affordance

---

## 7. Do's and Don'ts

**Do:**
- Use CSS custom properties for every color decision — never raw hex values in components
- Apply `--link` (`#1447e6`) for all hyperlinks consistently
- Use inset box-shadow for borders (avoids layout shift, cleaner at scale)
- Maintain the two-weight system: 400 for reading, 500 for labels/UI, 600 only for page title
- Use `--expo-out` easing for any UI transitions

**Don't:**
- Introduce hue variation outside the defined `--info`, `--success`, `--destructive` status palette
- Use font-weight 700 — nothing on this site needs bold
- Use borders heavier than 1px
- Stack multiple shadows — keep depth single-layer
- Override Geist Sans with another typeface

---

## 8. Responsive Behavior

With only a 600px breakpoint, this design assumes near-identical behavior between phone and desktop. The implication:

- **<600px**: Likely collapses navigation, reduces content to single column
- **≥600px**: Full layout, sidebar may appear, multi-column grid for component listings

The very simple breakpoint structure suggests most layout work is done through Tailwind's flex/grid utilities rather than responsive CSS rewrites. Type sizes, spacing tokens, and surface colors remain constant across all widths.

---

## 9. Agent Prompt Guide

When recreating or referencing chanhdai.com:

> "Design a clean developer portfolio with Geist Sans as the sole typeface, a Zinc-based neutral palette anchored by near-black `#09090b` on pure white. Use a full semantic token system: `--background`, `--foreground`, `--muted`, `--border`, `--surface`, `--primary`, `--link`. The only hue accent is link blue `#1447e6`. Typography: 30px/600 for page title (−0.75px tracking), 14–16px/400–500 for all UI. Buttons: filled primary (black bg) and ghost variants. Flat elevation using 1px inset box-shadow borders and 1–2px drop shadows. Single breakpoint at 600px."

---

*Generated by Sparkbites — extracted from live CSS analysis*
