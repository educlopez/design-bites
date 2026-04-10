# DESIGN.md — bfcm.stripe.com

## 1. Visual Theme & Atmosphere

Stripe's Black Friday / Cyber Monday promotional site is an exercise in restrained commercial elegance. The design philosophy rejects the seasonal kitsch of most sale pages — no aggressive reds, no countdown-timer panic. Instead, it presents financial technology as a premium product, using measured whitespace, a muted slate palette, and a single proprietary typeface to project calm authority. The atmosphere reads as "infrastructure for serious commerce" rather than "sale event." Visitors are invited to slow down and trust, not urged to act in haste.

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Page background | `rgb(255, 255, 255)` | Pure white — clean slate |
| Body text / primary text | `rgb(66, 84, 102)` | Slate-blue, not harsh black — feels engineered |
| Footer / deep text | `rgb(10, 37, 64)` | Near-navy for high-contrast anchoring |
| Nav + overlays | `rgba(0,0,0,0)` | Transparent nav keeps focus on content |
| Surface accent | `rgba(214, 214, 214, 0.5)` | Frosted glass panel for highlighted modules |

The absence of a strong accent color is intentional. Stripe's brand blue does not appear here — the promotional page is deliberately neutral, letting merchant content and metrics speak. No greens, no oranges, no celebratory hues.

## 3. Typography Rules

**Typeface**: `sohne-var` (variable font) — a custom Stripe brand face, falling back to Helvetica Neue then Arial.

| Selector | Size | Weight | Notes |
|----------|------|--------|-------|
| h1 | 32px | 700 | Bold anchors for section titles |
| body | 16px | 400 | Comfortable reading size |
| nav | 13px | 400 | Compact utility text |
| button | 14px | 400 | Unassuming CTA labels |

- Letter-spacing defaults to `normal` — sohne-var has excellent built-in spacing.
- No text transforms, no all-caps, no decorative ligature sets beyond defaults.
- The variable nature of sohne-var allows the design to stretch weight subtly across viewport sizes without swapping fonts.
- **What's absent**: no serif typefaces, no display-only fonts, no expressive mixing. Typography is a tool, not a statement here.

## 4. Component Stylings

- **Buttons**: 14px / weight 400 — deliberately understated, letting copy carry the CTA weight.
- **Nav**: transparent background, slate text — contextual, not dominating.
- **Frosted surface panels**: `rgba(214, 214, 214, 0.5)` — used for featured metric cards or highlighted modules.
- **No explicit border-radius tokens** — components likely use Stripe's own internal radius system (typically 6–8px on cards).
- **No shadows detected** — elevation is handled through color planes, not drop shadows.

## 5. Layout Principles

- Zero margin and padding on body and section elements — custom spacing grid takes over entirely.
- The layout is marketing-page structured: full-bleed sections stacked vertically, each owning its own visual zone.
- Whitespace is not incidental but deliberate; it signals that this is a premium product, not a bargain bin.
- No asymmetric or editorial layout cues — the structure is clean, grid-aligned, axis-respecting.

## 6. Depth & Elevation

Depth is minimal and conceptual rather than physical. The frosted panel (`rgba(214,214,214,0.5)`) implies a glass layer above the white ground. No box-shadows appear in the extracted data — Stripe BFCM opts for chromatic separation (light gray vs white vs slate) over shadow-based depth. This creates a flat-but-layered appearance: the page looks dimensional without being skeuomorphic.

## 7. Do's and Don'ts

**Do:**
- Use `sohne-var` for all text; never substitute a generic sans-serif as a stylistic choice.
- Keep body copy in slate (`rgb(66, 84, 102)`) — it reads cleanly without the harshness of pure black.
- Use whitespace aggressively between sections — the premium feel comes from what is not there.
- Maintain transparent nav so the page background bleeds through on scroll.

**Don't:**
- Add seasonal colors (red, green, orange) — this site's power comes from resisting that impulse.
- Use uppercase labels or tight tracking — that would undercut the calm authority.
- Add decorative shadows or layered drop effects — elevate through color, not shadow.
- Mix in a second typeface for display purposes.

## 8. Responsive Behavior

- Section padding scales via the custom spacing system (no explicit breakpoint tokens detected).
- The scrollbar is explicitly suppressed (`--scrollbarWidth: 0px`) for a seamless scroll experience on desktop.
- Button and nav text sizes (13–14px) are near the smallest comfortable reading size — suitable for desktop; mobile variants likely increase to 15–16px.
- Full-bleed sections adapt well to width changes since margin/padding originates from the component level.

## 9. Agent Prompt Guide

> Recreate a UI in the style of Stripe's BFCM landing page: pure white background, body text in `rgb(66, 84, 102)` (slate-blue), single variable sans-serif (`sohne-var` or substitute Helvetica Neue), generous section whitespace, transparent navigation, and frosted glass surface panels at 50% opacity. Buttons should be small-weight, unassuming. No accent colors. Depth through color contrast only, never shadows.

*Generated by Sparkbites — extracted from live CSS analysis*
