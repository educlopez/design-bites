# harshsingh.me — Design System

## 1. Visual Theme & Atmosphere

harshsingh.me is the cleanest expression of the modern developer portfolio: light off-white canvas, system fonts, deliberate whitespace, no decorative flourishes. Built with Astro and Tailwind, it prioritises content legibility and quiet confidence over visual spectacle. The defining characteristic is restraint — the CSS reveals no custom brand colours, no decorative shadows beyond a single subtle card lift, and a flat typographic scale where headings and body copy share the same 16px base size, differentiated only by weight. The −2% letter-spacing applied universally gives the text a modern, editorial tightness without requiring a custom typeface.

## 2. Color Palette & Roles

**Base** (oklch colour space — modern, perceptually uniform)
- Background: `oklch(0.97 0 0)` — warm near-white (≈`#f7f7f7`)
- Primary text: `oklch(0.205 0 0)` — very dark grey (≈`#2a2a2a`), not pure black
- Secondary/link text: `oklch(0.556 0 0)` — medium grey (≈`#737373`)

**Surfaces**
- No distinct surface tints detected beyond the base background
- A single card shadow implies white card surfaces on the off-white background

**Borders/Dividers**
- Uses `oklch(0.205 0 0)` for border colour (same as text — unified, not a separate grey)

**What's absent:** No accent colour, no brand colour, no dark mode, no coloured surfaces. This is a zero-accent design — the only colour is grey at different luminance levels.

## 3. Typography Rules

One font stack: `system-ui, -apple-system, Inter, sans-serif` — defaulting to the native OS font with Inter as a named fallback. This is a conscious choice: the portfolio should feel native to the user's device.

| Element | Size | Weight | Tracking |
|---------|------|--------|----------|
| H1 | 16px | 600 | −2% |
| H2 | 16px | 500 | −2% |
| Body | 16px | 400 | −2% |
| `<p>` | 16px | 300 | −2% (line-height: 22px) |
| Links | 16px | 400 | −2% |
| Button | 16px | 400 | −2% |

Every element is 16px. The entire typographic hierarchy is communicated through **weight alone**: 600 (headings) → 500 (sub-headings) → 400 (body) → 300 (prose). The −2% letter-spacing (`-0.02em`) is applied universally — it's the singular typographic personality choice. Paragraphs use a slightly shorter line-height (22px vs 24px for body) — a subtle density shift for reading comfort.

## 4. Component Stylings

**Cards** — implied by the single shadow: `rgba(0,0,0,.25) 0 3px 7.5px` — a clean, relatively pronounced lift for a minimal design. No background or border specified.

**Links** — `oklch(0.556 0 0)` — mid-grey, not underlined (typical for portfolios where links blend into content). No hover data extracted.

**Buttons** — 16px, system font, weight 400. No visual differentiation from body text in the CSS — buttons are likely styled with minimal decoration.

**Border radius** — only two values detected: `6px` (small elements like tags/chips) and the computed max (`3.35544e+07px`) for pill shapes.

**Sections** — 48px top margin spacing, 64px bottom margin on footer — simple breathing room, no padding.

**What's absent:** No shadows on navigation, no card borders, no background fills on interactive states.

## 5. Layout Principles

Pure vertical rhythm: sections spaced with 48px top margins. The layout is single-column. No horizontal padding at the `<main>` level — gutters are applied contextually. No breakpoints detected in CSS data, suggesting a fluid layout or Tailwind responsive utilities that don't appear in element-level extraction.

The footer carries generous space: `48px 0 64px` margin — the design breathes most at the bottom.

## 6. Depth & Elevation

One shadow. That's the entire elevation system:
- `rgba(0,0,0,.25) 0 3px 7.5px` — for cards/panels

This single shadow is notably more pronounced (`opacity: 0.25` at 7.5px blur) than is typical for minimal portfolios. It creates a distinct "floating card" effect against the off-white background without requiring border or background colour changes.

No glassmorphism, no multiple elevation tiers, no coloured shadows.

## 7. Do's and Don'ts

**Do:**
- Apply `letter-spacing: -0.02em` globally to all text
- Use weight 600/500/400/300 as the complete typographic hierarchy at 16px
- Keep the background `oklch(0.97 0 0)` — the warm near-white is deliberate
- Use the single card shadow (`rgba(0,0,0,.25) 0 3px 7.5px`) for any floating UI
- Keep links at `oklch(0.556 0 0)` — medium grey, not blue

**Don't:**
- Introduce brand or accent colours — this is a zero-accent design
- Vary font sizes beyond 16px base — weight alone creates hierarchy
- Add custom typefaces — system fonts are the aesthetic
- Use dark backgrounds or dark mode patterns
- Add borders to cards — the shadow alone defines separation

## 8. Responsive Behavior

No extracted breakpoints — likely fully fluid or Tailwind responsive classes. The single-column layout with vertical margin rhythm adapts gracefully to any width. The 16px type scale at all levels means no headline overflow issues on mobile. The 48px section spacing may reduce to 24–32px on mobile via responsive utilities.

## 9. Agent Prompt Guide

> Recreate harshsingh.me: off-white background `oklch(0.97 0 0)`, very dark text `oklch(0.205 0 0)`. Use `system-ui, -apple-system, Inter, sans-serif` — no custom font. Set ALL text to 16px. Build hierarchy through weight only: 600 (name/H1), 500 (section titles), 400 (body), 300 (prose paragraphs). Apply `letter-spacing: -0.02em` universally. Secondary/link text is `oklch(0.556 0 0)` — mid grey. Cards use one shadow: `rgba(0,0,0,.25) 0 3px 7.5px`. No accent colour, no borders on cards, no dark sections. Section spacing is 48px top margin. The design should feel like a beautifully formatted plain-text document.

*Generated by Sparkbites — extracted from live CSS analysis*
