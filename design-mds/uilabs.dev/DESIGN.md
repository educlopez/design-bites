# uilabs.dev — Design Document

## 1. Visual Theme & Atmosphere

UILabs is a component and interaction lab with a dual personality: the outer shell is clean and light, but it hints at darker, more experimental territory through its typography and accent choices. The page background is a neutral near-white (`rgb(255,255,255)` to `rgb(21,22,18)` in dark surfaces), but the headline typeface — Redaction — is an editorial serif drawn from redacted government documents. It is a conceptually loaded choice for a UI lab. The primary link color is specified in the `display-p3` color space (`color(display-p3 1 0.144 0.4521)`) — a vivid pink-red that only renders at full vibrancy on wide-gamut displays. This is a site built by designers for designers who notice these things.

---

## 2. Color Palette & Roles

| Role | Value | Usage |
|---|---|---|
| Background (light) | `rgb(255, 255, 255)` | Page background |
| Dark surface | `rgb(21, 22, 18)` | Dark sections / code blocks |
| Body text | `rgb(17, 17, 16)` | Primary text |
| Secondary text | `rgb(100, 100, 102)` | Muted labels, captions (blockquote) |
| Border (light) | `rgb(229, 231, 235)` | Component edges |
| Border (dark, hairline) | `hsla(0,0%,100%,.03)` | Dark surface border — nearly invisible |
| Link / accent | `color(display-p3 1 0.144 0.4521)` | Links — vivid pink-red, wide-gamut |
| Button (transparent) | `rgba(0,0,0,0)` | Ghost-style interactive elements |

The design operates with a dark/light duality. The `--color-dark-border` being `hsla(0,0%,100%,.03)` — an almost imperceptible white on dark — shows extreme refinement. The wide-gamut accent is the signature move: intentionally inaccessible to sRGB displays, communicating craft over compatibility.

---

## 3. Typography Rules

**Typefaces:**
- **Redaction** — Used for display/h1. A typeface derived from government redaction bars; serif, historical, conceptually loaded. Weight 400 at large sizes.
- **Inter** — Used for UI text (h2 through body, buttons, inputs). The functional counterpart.

| Context | Size | Weight | Leading | Notes |
|---|---|---|---|---|
| Display (h1) | 73px | 400 | 91.25px | Redaction serif — editorial, unexpected |
| Section label (h2) | 14px | 500 | 20px | Inter — compact, functional |
| Body (p) | 16px | 400 | 24px | Standard Inter body |
| Buttons | 14px | 400 | normal | Minimal, 0.1px tracking |

The 73px Redaction h1 is the design's hero moment — an oversized serif in a context where sans-serif is universal. The contrast between Redaction's editorial weight and Inter's utilitarian clarity creates an identity that says: "we know the rules and we're choosing to break one of them."

---

## 4. Component Styling

Components feature a sophisticated shadow system derived from design tokens: `--ds-shadow-border`, `--ds-shadow-medium`, `--ds-shadow-border-medium`, and `--ds-shadow-large`. The detected shadow (`rgba(0,0,0,0.12) 0px 8px 30px`) is smooth and airy. The `--p-color-bg-fill` custom property and the `text-light-accent` semantic token suggest a structured token system beneath the surface. Ghost buttons (transparent background, black border) are the default interactive state. The Shopify Polaris design system tokens (`--p-color-bg-fill`) appear in the codebase — UILabs likely showcases Shopify-adjacent component work.

---

## 5. Layout Principles

Main content is padded generously: `64px` internal padding with `260px` horizontal margins — a very wide guttered column, placing content in the center third of wide screens. The footer mirrors this with `265px` margins. Breakpoints at `600px` and `640px` define a single mobile-to-desktop transition. The near-identical breakpoint pair (600/640) manages a precise responsive inflection point, likely a grid changing from 1 to 2 columns.

---

## 6. Depth & Elevation

The token system reveals four shadow tiers:
- `--ds-shadow-border`: a border-only ring shadow (no blur)
- `--ds-shadow-medium`: mid-level elevation, the workhorse
- `--ds-shadow-border-medium`: a combined border + medium shadow
- `--ds-shadow-large`: `rgba(0,0,0,0.12) 0px 8px 30px` — the most visible, used for cards and modals

The dark surface border (`hsla(0,0%,100%,.03)`) creates boundary definition on dark backgrounds without visible edges — depth through near-invisibility.

---

## 7. Do's and Don'ts

**Do:**
- Use Redaction only for the primary display headline — it earns its impact through scarcity
- Specify link colors in `display-p3` color space; fall back gracefully for sRGB
- Keep Inter at 14–16px for all UI text; let Redaction carry the editorial voice
- Use the `--ds-shadow-large` shadow only for the most elevated surfaces
- Maintain wide margins (260px+) on desktop to keep content centred and focused

**Don't:**
- Use Redaction for body text or UI labels — it will read as noise, not editorial
- Add color to backgrounds; the duality is light white vs near-black only
- Override the `hsla(0,0%,100%,.03)` dark border with a more visible value
- Introduce a second accent color alongside the display-p3 pink-red
- Reduce margins below the 260px gutters on desktop layouts

---

## 8. Responsive Behavior

Two breakpoints (`600px`, `640px`) keep the responsive system minimal. Below `600px`, the wide margins collapse and the content stack goes single-column. The `64px` padding on `main` likely halves on mobile. The focused breakpoint range suggests this is not a heavily responsive product — it is primarily designed for desktop-first consumption, with mobile as a capable secondary experience.

---

## 9. Agent Prompt Guide

> Build a UI component showcase page in the style of uilabs.dev. White background with near-black text `rgb(17,17,16)`. Use Redaction serif at 73px/400 for the single display headline; use Inter for everything else (14px/500 for labels, 16px/400 for body). Links in `color(display-p3 1 0.144 0.4521)` with sRGB fallback `#ff2574`. Cards float on `rgba(0,0,0,0.12) 0px 8px 30px` shadow. Wide desktop margins (260px+). Two breakpoints only: 600px and 640px. Dark surface sections use `rgb(21,22,18)` with `hsla(0,0%,100%,.03)` hairline borders.

---

*Generated by Sparkbites — extracted from live CSS analysis*
