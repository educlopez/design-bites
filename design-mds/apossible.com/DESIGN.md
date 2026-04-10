# apossible.com — Design System

## 1. Visual Theme & Atmosphere

Apossible occupies a specific aesthetic territory: archival editorial. The palette is warm off-white approaching parchment, the typefaces are Swiss rationalism (Neue Haas Unica) paired with monospaced technicality (IBM Plex Mono), and the spacing system is codified down to CSS variables for every scale step. This is the work of a studio that treats design infrastructure as seriously as design output. Nothing is accidental. The warmth of the off-white background (`hsla(51, 9%, 94%)`) is not generic — the 51° hue angle gives it the faintest yellow-olive undertone, like aged paper.

## 2. Color Palette & Roles

**Backgrounds**
- Page ground: `hsla(51, 9%, 94%)` — warm off-white with olive undertone
- Dark mode / hero sections: `hsla(51, 0%, 12%)` — warm near-black
- Nav: `rgb(255, 255, 255)` — clean white strip

**Text**
- Primary: `rgb(51, 51, 51)` (`--text-black: #333`) — dark charcoal, not black
- Secondary: `#999` (`--text-grey`)
- Tertiary: `#aaa` (`--text-light-grey`)
- On-dark: `#FFFFFF`

**Accent color family** (named `--colour-1` through `--colour-8`)
An earth-tone gradient: sage green (`#797d62`) → warm sand (`#9b9b7a`) → dusty rose (`#d9ae94`) → pale gold (`#f1dca7`) → butter yellow (`#ffcb69`) → amber (`#e8ac65`) → terracotta (`#d08c60`) → warm brown (`#997b66`). Used for photography tints, section accents, or illustration.

**Borders / structural**
- Off-white border: `hsla(51, 33%, 94%)` — slightly richer than bg
- Grid lines: `hsla(51, 33%, 94%, 0.21)` — barely visible structure
- Button borders: `hsla(0, 0%, 50%, 0.25)` — neutral grey

**Shadows**
- Default shadow: `0 0 20px rgba(0,0,0,0.1)` — soft, diffuse, single-layer

## 3. Typography Rules

Two typefaces, two voices:

**Neue Haas Unica W04 Regular** — the structural voice. Used for all headings (h1–h4), body, navigation links. Weight is always 400 — no bold, no italic. All display impact comes from size and spacing, not weight.
- All headings (h1–h4): 16px — deliberately flat hierarchy
- h3 exception: 12px / uppercase / 0.9px letter-spacing — used as section labels
- Body: 16px / 21px line-height / 0.16px tracking

**IBM Plex Mono** — the technical voice. Used for paragraphs, h5, figcaptions, code-adjacent content. This pairing of sans for structure and mono for content is an inversion of convention — and makes the site feel like printed editorial from a design-tech intersection.
- Paragraphs: 12px / 17px line-height
- No bold weight on mono

The type scale is defined via CSS custom properties (`--size-s: 12px` through `--size-xl: 60px`) but the extracted selectors show a very compressed range in practice.

## 4. Component Stylings

**Border radii**: Four named values — `--outer-border-radius: 4px`, `--inner-border-radius: 3px`, `--tiny-border-radius: 2px`, `--image-border: 6px`. Extremely small and precise. Nothing is pill-shaped.

**Images**: `6px` border-radius — slightly more than structural elements, treating images as physical objects.

**Buttons**: 0px font-size on the base button selector — buttons are likely icon-only or custom-rendered. No visible filled button style in base.

**Animation easing**: Two named easings — `--bounce: cubic-bezier(0,0.73,0.12,1.71)` (overshooting spring) and `--fast-easing: cubic-bezier(0.16, 1, 0.3, 1)` (expo-out). Motion is intentional and characterful.

## 5. Layout Principles

A CSS-variable-driven grid: `--grid-size: 130px`, `--content-width: 480px`, `--content-container-margin: clamp(45px, 3.5vw, 70px)`. Content is narrow by design — 480px is a prose column. The 130px grid module suggests a structured, module-based layout for work samples.

Menu dimensions are codified: `--menu-width: 260px`, `--menu-title-height: 40px`. The layout system is precise and pre-specified, not emergent.

## 6. Depth & Elevation

Shallow, diffuse single shadow: `0 0 20px rgba(0,0,0,0.1)`. Elevation is used sparingly — the design philosophy prefers surface differentiation (warm off-white vs white nav) over shadow stacking.

## 7. Do's and Don'ts

**Do**
- Use IBM Plex Mono for body copy — the unconventional pairing is the identity
- Keep headings at 400 weight regardless of size
- Use the earth-tone color palette (`--colour-1` through `--colour-8`) for imagery and accents
- Honor the tight border-radius values (2–6px); avoid rounding to 8px or beyond

**Don't**
- Introduce bold weights — the entire system runs at regular weight
- Use shadow stacking or layered depth effects
- Apply bright or saturated colors; the earth-tone palette defines the warmth ceiling
- Use pure black; `#333` is the darkest text tone

## 8. Responsive Behavior

No explicit breakpoints in the extracted data — likely a single pivot point using `clamp()` for margins. The `--content-container-margin` uses `clamp(45px, 3.5vw, 70px)`, showing fluid rather than stepped layout adaptation. The narrow 480px content column adapts gracefully to mobile without restructuring.

## 9. Agent Prompt Guide

> Design with apossible.com's language: warm parchment background (`hsla(51,9%,94%)`), Neue Haas Unica at 400 weight for all structure, IBM Plex Mono for body copy and captions. Heading hierarchy through size only — no bold. Accents from an earth-tone palette (sage to terracotta). Tiny border radii (2–6px). Single diffuse shadow at `rgba(0,0,0,0.1)`. The design feels archival, editorial, and technically precise.

---

*Generated by Sparkbites — extracted from live CSS analysis*
