# Micah Carroll — Design System Reference

## 1. Visual Theme & Atmosphere

micahcarroll.com strips the personal-site format down to a single move: white type floating on a near-black field. The canvas isn't pure black — `rgb(12, 12, 12)` carries a luminance of 0.047, just enough warmth to avoid the dead flatness of `#000` — and against it, every piece of type, every border, every link renders in flat `rgb(255, 255, 255)`. There is no accent color anywhere in the extracted system. No blue link, no brand hue, no status color. The site reads less like a portfolio and more like a **link hub for a creator's video presence** — the markup exposes a `.creative-container`, a `.sticky-nav` that dims to 60%-opacity black on scroll, and a trio of `.link-link` elements pointing to a main YouTube channel, a retro-gaming channel, and a vlogging channel. The whole thing is quiet, monochrome, and unfussy — a single typeface, a single weight discipline, and restraint standing in for a whole brand system.

---

## 2. Color Palette & Roles

**Foundation — the entire palette**
- `rgb(12, 12, 12)` — page/section canvas (`div.creative-container`), luminance 0.047 — not pure black, but close
- `rgb(255, 255, 255)` — text, borders, and default outline color, used everywhere without variation
- `rgba(0, 0, 0, 0.6)` — sticky nav overlay (`div.sticky-nav`), luminance 0 — a darker, semi-transparent scrim layered above the canvas as you scroll
- `rgba(0, 0, 0, 0)` — transparent body background and transparent link backgrounds; nothing is ever filled

There is no secondary hue, no tint, no status color, and no gradient anywhere in the extracted data. This is a two-value system — near-black and white — with a third, translucent black used purely as a navigational scrim. Depth and hierarchy are never carried by color; they're carried entirely by opacity and size.

---

## 3. Typography Rules

**Typeface:** Inter (`Inter, sans-serif`) — the only font family detected, used for headings, body, and links alike.

| Role | Size | Weight | Line-height | Letter-spacing | Transform |
|------|------|--------|-------------|-----------------|-----------|
| H1   | 32px | 500    | normal      | -0.7px          | none      |
| H3   | 24px | 500    | normal      | -0.7px          | none      |
| Body | 16px | 500    | normal      | -0.7px          | none      |
| P    | 16px | 500    | normal      | -0.7px          | none      |
| Link | 16px | 500    | normal      | -0.7px          | none      |

**Principles**
- **One weight for everything.** Every extracted selector — h1, h3, body, p, a — sits at weight `500`. There is no bold, no light, no italic. Hierarchy is delivered by size alone (32 → 24 → 16), never by weight.
- **A flat -0.7px tracking, regardless of size.** Unlike most type systems that tighten tracking as size grows, this site applies the exact same `-0.7px` letter-spacing across a 32px h1 and a 16px paragraph. It reads as a deliberate, almost mechanical consistency rather than an optically-tuned scale.
- `font-feature-settings: normal` and `text-transform: none` across the board — no OpenType tricks, no uppercase treatments, no small caps.
- No `line-height` override — every selector reports `normal`, leaving the browser's default leading in place. Nothing here is fussed over beyond size and tracking.

---

## 4. Component Stylings

**Links** (`.link-link`, e.g. "Main Youtube Channel," "Retro Gaming Channel," "Vlogging channel you")
- Background: transparent (`rgba(0, 0, 0, 0)`) at all times — links never get a filled pill or button treatment
- Text/border: `rgb(255, 255, 255)` in both default and hover states — color never shifts
- **Hover/focus feedback is opacity-only**: default state is `opacity: 1`, hover (or focus, on the one link that swaps hover for a focus state) drops to `opacity: 0.7`. No transform, no underline change, no box-shadow.
- Default outline is `rgb(255, 255, 255) none 3px` — a 3px white outline defined but not rendered (`none` style) until an interactive/focus-visible state calls for it.

**Sticky nav** (`div.sticky-nav`)
- `rgba(0, 0, 0, 0.6)` background — a translucent scrim, distinct from the opaque `rgb(12, 12, 12)` page canvas, letting whatever sits behind it stay faintly visible.

**Border radius**
- A single value, `4px`, used wherever rounding appears — small and utilitarian, never a pill or a sharp 0.

**Shadows**
- None detected. Every surface is flat; separation comes from the luminance step between canvas (0.047) and nav scrim (0), not from cast shadows.

---

## 5. Layout Principles

- The structural elements are nearly unstyled: `section` carries `0px` padding/margin, and `body` keeps the browser-default `8px` margin with `0px` padding — this is a site that leans on component-level spacing (inside `.creative-container` and similar wrappers) rather than global rhythm rules.
- `header` is the one structural exception, carrying `0px 0px 8px` padding — an 8px breathing gap under the header content before whatever follows begins.
- Breakpoints sit at **430 / 768 / 1024 / 1440** — a small-phone cutoff (430, matching modern large-phone viewport widths) alongside the standard tablet/laptop/desktop set, suggesting the layout is tuned as much for phone-sized video/link taps as for desktop browsing.
- No CSS custom properties were detected — the system carries no design tokens in the cascade; values are applied directly per element.

---

## 6. Depth & Elevation

Depth here is almost nonexistent, and what little exists is opacity-driven rather than shadow-driven:
- **Canvas vs. nav scrim** — the page sits at luminance 0.047 (`rgb(12, 12, 12)`); the sticky nav overlays a `rgba(0, 0, 0, 0.6)` scrim on top, functionally darker (effective luminance trends toward 0) without introducing a new hue.
- **Interaction depth is opacity, not elevation** — hovering or focusing a link doesn't lift it, shadow it, or recolor it; it simply dims to 70% opacity. This is the site's only "elevation" language.
- No `box-shadow` values were extracted anywhere in the system.

---

## 7. Do's and Don'ts

**Do**
- Set the canvas to `rgb(12, 12, 12)` — not pure black — and keep all text and borders at flat `rgb(255, 255, 255)`.
- Hold every weight at `500` and drive hierarchy purely through size (32px → 24px → 16px).
- Apply the same `-0.7px` letter-spacing across every text size, from h1 down to body — don't taper it.
- Use opacity (`1` → `0.7`) as the entire interaction language for links; skip color shifts, underlines, and transforms.
- Keep border radius at a restrained `4px` wherever rounding is needed.
- Layer a `rgba(0, 0, 0, 0.6)` scrim for sticky/overlay navigation rather than a new opaque color.

**Don't**
- Don't introduce a second hue or accent color — this system is white-on-near-black and nothing else.
- Don't vary font weight for emphasis; the whole site sits at 500.
- Don't add drop-shadows or elevation effects — the system has none, and depth is handled by opacity and luminance alone.
- Don't scale letter-spacing down as text gets larger — the flat -0.7px tracking is a deliberate signature here, not an oversight.
- Don't fill link backgrounds or add borders on hover — the only hover signal is dimming to 70% opacity.

---

## 8. Responsive Behavior

Four breakpoints — **430, 768, 1024, 1440** — cover phone, tablet, laptop, and desktop. The inclusion of 430 (rather than a rounder 480 or 375) signals the layout was checked against modern large-phone viewports specifically, consistent with a site whose primary content is likely consumed via phone taps on outbound video links. Typography carries no responsive overrides in the extracted data — the 32/24/16px scale and the flat -0.7px tracking appear to hold constant across breakpoints, letting the layout (not the type) do the adapting.

---

## 9. Agent Prompt Guide

> Build a UI that matches micahcarroll.com's design language.

Set the page canvas to `rgb(12, 12, 12)` — a soft near-black, not pure `#000`. Set all text, borders, and default outlines to flat `rgb(255, 255, 255)`; do not introduce any second color or accent hue anywhere in the interface. Use **Inter** as the only typeface, at a constant weight of `500` for every role — headings, body, links — and drive hierarchy purely through size: 32px for top-level headings, 24px for sub-heads, 16px for body text and links. Apply a flat `-0.7px` letter-spacing uniformly across all of those sizes; do not taper it down for smaller text. Give links a transparent background at all times, matching text color to the canvas foreground (`rgb(255, 255, 255)`), and make the entire interaction model opacity-based: default `opacity: 1`, hover/focus `opacity: 0.7` — no color change, no underline, no transform, no shadow. Keep border radius restrained at `4px`. For a sticky or overlay navigation bar, use a translucent `rgba(0, 0, 0, 0.6)` scrim rather than a new opaque surface color. Add no box-shadows anywhere — this system communicates depth only through the luminance gap between the near-black canvas and the darker nav scrim. Target breakpoints at 430 / 768 / 1024 / 1440px, keeping typography constant across all of them.

---

*Generated by Sparkbites — extracted from live CSS analysis*
