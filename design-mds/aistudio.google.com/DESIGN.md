# aistudio.google.com — Design System

## 1. Visual Theme & Atmosphere

Google AI Studio is a dark workspace — not merely dark-themed, but intentionally low-stimulation to keep focus on the model output. The visual language is minimal Angular Material: flat surfaces, no shadows, soft rounded corners. The palette is deliberately close to neutral with a single blue accent (`#0842A0`), signaling trust and Google's brand without screaming it. The experience says "professional workbench" over "consumer product." What's notably absent: gradients, illustrations, decorative elements — this is developer infrastructure dressed in calm authority.

## 2. Color Palette & Roles

**Background**
- Page / body: `rgb(31,31,31)` — dark charcoal, not pure black, reduces eye strain
- Code blocks: `rgb(31,31,31)` — matches body, code blends with content layer
- Model badge: `rgba(37,37,37,0.5)` — slightly elevated, semi-transparent

**Text**
- Primary: `rgb(212,212,212)` — light grey, not white, reduces contrast harshness
- Links: `rgb(135,169,255)` — periwinkle blue, readable on dark background, Google tint

**Accent / Action**
- Primary buttons: `rgb(8,66,160)` — deep Google blue, high confidence action
- Hover state: `rgb(60,60,60)` on nav items — subtle surface reveal on hover

**Interactive**
- Nav hover background: `rgb(60,60,60)` / border: `rgb(62,62,62)` — barely-there lift
- Default nav opacity: `0.9` — items start slightly faded, become full on hover

**Borders**
- No explicit border tokens — separation is implied by background contrast, not drawn lines

## 3. Typography Rules

AI Studio makes an unusual choice: Inter Tight for h1, regular Inter for everything else. This pairing is the same typeface family at different optical widths — creating hierarchy through compression rather than weight or size change.

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| h1 | Inter Tight | 28px | 300 | Light weight — calm, not commanding |
| body | Inter | 14px | 400 | Compact reading size, 20px line-height |
| p | Inter | 14px | 500 | Medium weight — body copy gets emphasis |
| a | Inter | 14px | 500 | Same as paragraph, consistent reading weight |
| button | Inter | 14px | 500 | Action text matches content weight |
| code/pre | monospace | 14px | 400 | System monospace, no custom code font |

The 14px baseline is small but appropriate for a tool interface where information density matters. Line-height of 20px (1.43 ratio) is tight — a workspace rhythm, not a reading rhythm. Notably, h1 at weight 300 is deliberately light — this is not a product page, it's a tool, and the headline doesn't need to sell.

## 4. Component Stylings

**Buttons**
- Background: `rgb(8,66,160)` — deep blue, solid fill
- Text: `rgb(226,226,229)` — slightly warm white
- Border radius: `12px` / `16px` / `32px` — pill and rounded rectangle variants
- No shadow — elevation is communicated through color alone

**Navigation links**
- Default: transparent background, `rgb(212,212,212)` text, opacity `0.9`
- Hover: `rgb(60,60,60)` background fills in, opacity becomes `1.0`
- Border: `rgb(62,62,62)` appears on hover — a hairline container materializes

**Code blocks**
- Surface: `rgb(31,31,31)` — matches body, no visual distinction
- Font: system monospace, 14px — undecorated, raw

**Model badge**
- `rgba(37,37,37,0.5)` — frosted glass-like pill, semi-transparent over the dark base

## 5. Layout Principles

Generous page margins: `main` has `0 141px` horizontal margins — a wide content column with breathing room on large screens. Section spacing is dramatic: `50px 0px 250px` on section elements — the 250px bottom margin creates long scrolling space between content blocks, giving each section room to breathe and be read in isolation.

Header is padded `30px 60px 0` with `130px` bottom margin — a very deliberate separation between navigation and content. The overall feel is airy for a dark interface, which prevents claustrophobia.

Breakpoints: 600px, 768px, 1046px — standard tablet-first responsive ladder.

## 6. Depth & Elevation

Shadow array is empty — there are no drop shadows in this design. Zero. Depth is expressed entirely through background color steps: `rgb(31,31,31)` base → `rgba(37,37,37,0.5)` mid → `rgb(8,66,160)` accent. The semi-transparent model badge is the closest thing to layering. This creates a flat, focused atmosphere where the UI doesn't compete with content.

## 7. Do's and Don'ts

**Do**
- Use dark charcoal `rgb(31,31,31)` as the base surface — not pure black
- Keep text at `rgb(212,212,212)` — grey, not white
- Use `rgb(8,66,160)` exclusively for primary action buttons
- Rely on background color changes for hover states, not shadows or transforms
- Use generous section spacing (100px+) to separate content zones

**Don't**
- Add box shadows — this design is intentionally shadowless
- Use bright or saturated accent colors — one blue, that's all
- Mix font weights aggressively — the palette is 300/400/500 only
- Use Inter Tight outside of h1 — the condensed variant is reserved for top-level headings
- Create visual noise with borders — separation is contextual, not drawn

## 8. Responsive Behavior

At 1046px the layout begins to adapt. The `141px` side margins on `main` likely collapse at tablet widths. The 600px breakpoint is the mobile threshold. Angular's Material component system handles most responsive behavior. No custom dark/light mode toggle is visible in the CSS — this is dark-only by design.

## 9. Agent Prompt Guide

> Design an AI workspace tool in the style of Google AI Studio: dark charcoal background (`rgb(31,31,31)`), light grey text (`rgb(212,212,212)`), single deep blue accent (`rgb(8,66,160)`) for primary actions. Inter Tight at weight 300 for headlines, Inter at 400–500 for everything else, all at 14px baseline. No shadows anywhere. Hover states are background reveals (`rgb(60,60,60)`) not transforms. Wide page margins (140px+), dramatic section spacing (200px+ bottom). Rounded corners 12–32px. Periwinkle links (`rgb(135,169,255)`). Flat, focused, developer-grade.

---

*Generated by Sparkbites — extracted from live CSS analysis*
