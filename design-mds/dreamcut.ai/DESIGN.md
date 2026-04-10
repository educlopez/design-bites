# Dreamcut AI — Design System

## 1. Visual Theme & Atmosphere

Dreamcut AI leans into the cinematic AI-tool aesthetic: a dark charcoal base (#171717) with pure system fonts and an indigo/violet accent for interactive elements. There is no custom typeface — the design trusts the OS default sans-serif stack entirely, a deliberate choice that keeps the interface feeling native, fast, and cross-platform neutral. The hero section is massive (160px top, 860px bottom padding) — built for dramatic first impact with a full-viewport scrolling reveal. The overall tone is tool-first with cinematic ambition.

---

## 2. Color Palette & Roles

| Role | Value | Notes |
|------|-------|-------|
| Page background | `#171717` | Near-black charcoal |
| Header | transparent | Nav floats over content |
| Primary text (header) | `#ffffff` | White on dark |
| Button text | `rgb(212,212,212)` | Slightly muted white |
| Textarea bg | `rgba(38,38,38,0.6)` | Semi-transparent input surface |
| Textarea text | `rgb(229,229,229)` | Off-white |
| Textarea border top | `rgba(255,255,255,0.2)` | Subtle top edge |
| Textarea border sides | `rgba(82,82,82,0.5)` | Mid-grey sides |
| Select bg | `rgb(64,64,64)` | Medium dark for dropdowns |
| Label text | `rgb(163,163,163)` | Cool grey for form labels |
| Border reference | `rgb(229,231,235)` | Tailwind gray-200 |
| CTA accent | Tailwind indigo-500/600 | Interactive primary buttons |

The palette is Tailwind dark mode vocabulary — charcoals, cool greys, and white — with Tailwind indigo as the CTA accent. No warm tones anywhere.

---

## 3. Typography Rules

**Typeface:** System UI stack — `ui-sans-serif, system-ui, sans-serif` plus emoji fallbacks. No custom fonts.

| Level | Size | Weight | Line Height | Tracking |
|-------|------|--------|-------------|----------|
| h1 | 60px | 500 | 60px | -1.5px |
| h2 | 36px | 500 | 40px | normal |
| h3 (label) | 12px | 500 | 16px | normal |

- Weight 500 (medium) is the single weight used across all heading levels.
- h1 has a 1:1 line-height ratio (60px/60px) — tight, cinematic headline setting.
- No letter-spacing on h2/h3 — only the hero headline gets the -1.5px compression.
- The decision to use system fonts is a product statement: this is a utility, not a brand exhibition.
- Tailwind CSS generates the actual utility classes — no design-token typography system.

---

## 4. Component Styling

- **Textarea:** Semi-transparent dark bg with asymmetric border — lighter on top, mid-grey on sides, creating a subtle depth illusion.
- **Select/Dropdown:** Solid dark grey (#404040) — distinct from textarea.
- **Elevation shadow (tier 1):** `rgba(0,0,0,0.05) 0 1px 0, rgba(0,0,0,0.1) 0 4px 4px, rgba(0,0,0,0.15) 0 10px 10px, rgba(0,0,0,0.1) 0 -1px 0 inset` — card with bottom glow.
- **Elevation shadow (tier 2):** `rgba(0,0,0,0.1) 0 20px 25px -5px, rgba(0,0,0,0.1) 0 8px 10px` — standard shadow-xl equivalent.
- CTA buttons use Tailwind indigo classes — part of the indigo-500/600 range.
- No border-radius tokens — relies on Tailwind's rounded utilities.

---

## 5. Layout Principles

- Section padding: 160px top, 860px bottom — an extreme bottom pad designed for scroll-driven narrative reveal.
- Footer padding: 8px — essentially absent, just clearance.
- Header transparent, floating over the hero — no sticky bar interruption of the hero experience.
- Tailwind utility-first layout — no custom spacing tokens exposed.

---

## 6. Depth & Elevation

- Two shadow tiers: card-level (10px blur) and panel-level (25px blur) — both use black alpha stacks.
- Textarea uses an asymmetric border-color trick for pseudo-depth (lighter top edge).
- No gradients, no glow effects beyond the shadow stacks.
- The extreme bottom section padding creates depth through vertical space, not visual decoration.

---

## 7. Do's and Don'ts

**Do:**
- Trust the system font — it's intentional, not a placeholder.
- Apply indigo only to primary interactive CTA elements.
- Use the 1:1 line-height on hero headlines (h1 60px/60px).
- Use the two-tier shadow system for cards: subtle (10px) and prominent (25px).

**Don't:**
- Add custom fonts or brand typefaces — system UI is the design choice.
- Introduce warm colours (cream, amber, brown) into this cold dark palette.
- Use more than two shadow tiers — keeps the elevation grammar simple.
- Break the transparent header convention with a filled nav background.

---

## 8. Responsive Behavior

- Footer at 8px padding — nearly invisible on all screen sizes; footer content is minimal by design.
- The 860px bottom section padding must collapse significantly on mobile (this is likely animation/scroll trigger space).
- System font stack ensures optimal rendering on every OS/device without loading overhead.

---

## 9. Agent Prompt Guide

> Build an AI tool interface using Dreamcut's dark utility aesthetic. Background #171717, text white. System font stack: ui-sans-serif, system-ui, sans-serif. Headings at weight 500 — h1 at 60px with 1:1 line-height and -1.5px tracking. CTA buttons in Tailwind indigo. Form inputs use semi-transparent dark backgrounds (rgba(38,38,38,0.6)) with subtle asymmetric borders. Two shadow tiers: card (10px) and panel (25px). No custom typefaces, no warm tones, no gradients. Tailwind utility classes throughout.

---

*Generated by Sparkbites — extracted from live CSS analysis*
