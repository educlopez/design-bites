# aiverse.design — Design System

## 1. Visual Theme & Atmosphere

Aiverse.design occupies a specific aesthetic territory: warm minimalism. Where most AI product sites go dark and futuristic, this one goes light and analogue — a warm cream background, sand-tone borders, and a serif blockquote typeface (Louize) that wouldn't look out of place in a design magazine. The philosophy is "curated calm": a gallery space, not a control room. The single vivid element — a burnt orange `rgb(236,114,47)` used sparingly as a bullet or accent — punctuates the restraint with editorial precision. The design communicates taste over technology.

## 2. Color Palette & Roles

**Background**
- Page: `rgb(255,249,245)` — warm cream with a hint of peach, not neutral white
- Surfaces: same cream — no panel differentiation, content floats on a unified ground
- Accent section: `rgb(237,224,212)` — deeper sand, marks featured or highlighted zones

**Text**
- Primary: `rgb(0,0,0)` — pure black on cream for maximum legibility
- h1 display: `rgb(170,158,146)` — muted sand tone for the headline itself, an unusual inversion (the largest text is the lightest)
- Secondary / nav links: `rgb(135,113,100)` — warm brown-grey, clearly subordinate
- Hover on secondary: `rgb(6,5,4)` — dark, almost black — simple darkening

**Accent**
- Orange dot/marker: `rgb(236,114,47)` — the only saturated color, used as punctuation
- Black CTA: `rgb(0,0,0)` filled buttons — stark contrast against cream

**Borders**
- Universal: `rgb(226,217,207)` — the design's quiet divider, a warm taupe line used everywhere
- This single border color creates coherence — all elements share the same seam

## 3. Typography Rules

Aiverse uses two typefaces with sharply different roles. The system sans-serif (`ui-sans-serif`) handles all UI — nav, labels, cards, body. Louize, a humanist serif, appears only in the blockquote at `30px` — the single editorial voice in the composition. This restraint makes the serif meaningful.

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| h1 | system-ui | 60px | 300 | −1.5px tracking, tight 48px line-height |
| h3 | system-ui | 48px | 600 | −1.2px tracking — display-weight section head |
| h2 | system-ui | 18px | 600 | Label-scale heading, not structural |
| h4 | system-ui | 18px | 700 | Feature card title |
| body | system-ui | 16px | 400 | Comfortable reading |
| p | system-ui | 14px | 400 | Compact supporting text |
| blockquote | Louize | 30px | 400 | −0.75px tracking, 1.375 line-height |

h1 at weight 300 (light) is the most distinctive choice: a 60px headline that whispers rather than shouts. Combined with the muted `rgb(170,158,146)` color, the title recedes — the opposite of conventional landing page hierarchy. The blockquote Louize serif is the emotional anchor of the page.

## 4. Component Stylings

**Buttons**
- Default: `rgb(242,235,229)` background, `rgb(226,217,207)` border, `rgb(135,113,100)` text
- Hover: background fills to `rgba(237,224,212,0.92)`, text darkens to near-black
- No transform, no shadow on hover — purely colorimetric feedback
- Border radius: effectively full-circle (`3.35544e+07px` — a very large value = pill)

**Navigation links**
- Resting: `rgb(135,113,100)` — warm muted brown
- Hover: `rgb(6,5,4)` — darkens to near-black
- No underline, no background shift

**Input (search)**
- Background: `rgb(255,249,245)` — matches page exactly, no distinction
- Focus: border fades away (`rgba(226,217,207,0.04)`), black ring `rgba(20,20,20,0.96)` at 1.9px appears via box-shadow
- The input effectively disappears into the page until focused — anti-chrome design

**Dividers**
- `div.w-0.5`: `rgb(226,217,207)` — the vertical/horizontal separator line

**Shadows**
- Cards: `rgba(0,0,0,0.1) 0px 10px 15px -3px, rgba(0,0,0,0.1) 0px 4px 6px -4px` — Tailwind `shadow-lg` equivalent
- Elevated cards: `rgba(0,0,0,0.1) 0px 20px 25px -5px` — `shadow-xl` for featured items

## 5. Layout Principles

Header: `16px 32px` padding — compact, flush. Sections have zero padding and margin, relying on internal content spacing. The layout is Tailwind-driven with a single 600px breakpoint — effectively a two-tier responsive system (mobile / everything else). The orange `div.w-5` element acts as a visual bullet or step marker in a timeline/list structure.

Notably, no container max-width is specified via CSS custom properties — the column width is controlled by Tailwind utility classes.

## 6. Depth & Elevation

Two elevation levels are used: standard Tailwind `shadow-lg` for cards and `shadow-xl` for emphasized items. Both use the same `rgba(0,0,0,0.1)` opacity — soft and ambient, never dramatic. The warm background makes shadows appear even more subtle. Surfaces themselves are flat — no gradients or glass morphism. The accent surface `rgb(237,224,212)` creates the only true "panel" distinction.

## 7. Do's and Don'ts

**Do**
- Use `rgb(255,249,245)` as the only background — maintain the unified cream ground
- Apply `rgb(226,217,207)` as the universal border — one border color for the whole system
- Keep the orange `rgb(236,114,47)` rare — one small element per section at most
- Use Louize serif only for extended quotes or editorial moments
- Make h1 light (weight 300) and muted in color — this design bucks conventional hierarchy

**Don't**
- Introduce cool or neutral greys — the palette is warm throughout
- Add dark surfaces or panels — there is no dark layer in this design
- Use weight 800+ for headings — the maximum is 700 (h4 only)
- Apply color to borders except the single taupe token `rgb(226,217,207)`
- Make inputs visually prominent — they should blend into the background

## 8. Responsive Behavior

Single breakpoint at 600px — the design is intentionally simple to adapt. Navigation items marked `.hidden` suggest they collapse below this threshold. The header padding (`16px 32px`) will likely reduce on mobile. Large display text (60px h1) may need to scale down significantly at 600px.

## 9. Agent Prompt Guide

> Design an AI gallery/showcase site in the style of aiverse.design: warm cream background (`rgb(255,249,245)`), universal taupe border (`rgb(226,217,207)`), black text on cream. h1 at 60px weight 300 in warm grey (`rgb(170,158,146)`) — intentionally recessive. Body text 16px system sans-serif. One Louize serif blockquote at 30px for editorial emphasis. Burnt orange (`rgb(236,114,47)`) as single decorative accent. Pill-shaped buttons in sand `rgb(242,235,229)`. Tailwind shadow-lg for card elevation. Hover states darken text color, no transforms. One breakpoint at 600px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
