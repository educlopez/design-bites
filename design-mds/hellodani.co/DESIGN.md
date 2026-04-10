# hellodani.co — Design System

## 1. Visual Theme & Atmosphere

hellodani.co is a designer portfolio that rejects the grey-on-white digital default in favour of a warm, tactile world. The background is `rgb(246, 245, 241)` — an aged-parchment cream — and the colour palette draws from a bold, primary-adjacent set that feels more like printed collateral than a screen. The combination of **Libre Baskerville** (an approachable serif) with **Inter** for body text creates a vintage-editorial-meets-contemporary-digital tension. The four accent colours (red, pink, yellow, blue) appear as distinct blocks — card backgrounds, decorative elements — rather than as gradients or blends. Built in Framer with Motion animations, the site likely uses these blocks with entrance animations. The whole thing reads like a hand-designed portfolio zine that happens to be interactive.

## 2. Color Palette & Roles

**Base**
- Background: `rgb(246, 245, 241)` — warm cream/parchment
- Primary text: `rgb(0, 0, 0)` — pure black (against the cream, this feels warm rather than harsh)
- Surface elevated: `rgb(255, 255, 255)` — pure white cards

**The four accent blocks** (the signature palette)
- Red: `rgb(253, 30, 31)` — primary link colour AND a colour block
- Pink: `rgb(255, 143, 202)` — soft hot pink block
- Yellow: `rgb(255, 203, 65)` — warm amber-yellow block
- Blue: `rgb(0, 21, 212)` — deep royal blue block

**Neutral surface tiers**
- Cream: `rgb(246, 245, 241)` — page background
- Light cream: `rgb(228, 227, 221)` — slightly darker neutral block
- Black: `rgb(0, 0, 0)` — used as a surface (dark sections)

**Link colour** — `rgb(253, 30, 31)` — red as default link colour is a bold, print-inspired choice.

**What's absent:** No grey palette, no muted colours, no gradients. The palette is deliberately limited to cream + 4 saturated colours + black.

## 3. Typography Rules

A pairing of editorial serif and contemporary sans.

| Element | Font | Size | Weight | Tracking |
|---------|------|------|--------|----------|
| H1 | Libre Baskerville | 40px | 400 | −0.6px |
| H2 | Libre Baskerville | 40px | 400 | −0.6px |
| H3 | Libre Baskerville | 24px | 400 | −0.4px |
| `<p>` | Inter | 16px | 400 | −0.48px |
| Links | Inter | 16px | 400 | −0.48px |

Libre Baskerville at weight 400 (not bold — the italic/roman variant does the expressive heavy lifting). The serif is used consistently across all heading levels with the same weight, differentiating only by size. H1 and H2 share identical specifications — this suggests they're used in different contexts rather than a strict hierarchy.

Inter at 16px handles all reading text. The −0.48px tracking on prose (about −3% of font size) brings Inter slightly tighter than its default — making it feel more considered.

**Body fallback** — `sans-serif` at 12px normal — this is the browser body default, suggesting custom font loading may occasionally miss. Real content is set via more specific selectors.

## 4. Component Stylings

**Colour blocks** — the four accent blocks appear as full-fill rectangular containers (Framer frames). Border radii: 16px, 24px, 32px, 8px — suggesting different blocks have different radii, creating variety within a unified shape language.

**No shadows** — zero shadow values detected. The cream background and coloured blocks create depth through colour contrast rather than elevation.

**Navigation** — transparent, 40px bottom padding, 16px gap between items.

**Footer** — 32px padding, 32px gap — generous breathing room.

**Framer Motion** — the detected stack confirms animations are used; the colour blocks likely animate in on scroll.

**Cards** — `rgb(255, 255, 255)` white surface floating on the cream background.

## 5. Layout Principles

Section gap of 24px — tight, editorial pacing. The header has a generous 40px bottom padding, creating clear separation between nav and content. The 32px footer padding maintains the generous bottom margin expected of portfolio sites. Only two standard responsive breakpoints: ~640px (mobile) and 1440px (wide desktop).

Framer's layout engine handles much of the grid logic not visible in CSS selectors.

## 6. Depth & Elevation

No shadows at all — this is the flattest design in the collection. Depth is achieved entirely through:
1. **Background contrast** — white cards over cream background
2. **Saturated colour blocks** — the four accent colours visually advance/recede based on their lightness (blue is darkest, yellow/pink/red are mid-range)
3. **Black sections** — `rgb(0,0,0)` surfaces for maximum contrast moments

The absence of shadow combined with pure black and vibrant colour gives the site an ink-on-paper tactility.

## 7. Do's and Don'ts

**Do:**
- Keep the background at `rgb(246, 245, 241)` — never pure white or grey
- Use Libre Baskerville at weight 400 only — no bold headings
- Set red (`rgb(253, 30, 31)`) as the default link colour — it's the brand interaction signal
- Treat the four accent blocks as illustration/colour-field elements, not UI backgrounds
- Vary border radii across accent blocks: 8px, 16px, 24px, 32px for visual rhythm

**Don't:**
- Use gradients — the aesthetic is flat, opaque colour blocks
- Add shadows — they contradict the print-inspired flatness
- Bold the Libre Baskerville headings — the weight 400 serif voice is intentional
- Use Inter for headings — the serif/sans split is strict
- Mix the four accent colours in the same component — each block stands alone

## 8. Responsive Behavior

Two main breakpoints (640px mobile, 1440px wide). The 40px H1/H2 at 40px scales reasonably to mobile without aggressive reduction. The four colour blocks likely stack vertically on mobile where they're arranged in a grid on desktop. Framer handles the responsive reflow.

The cream background and flat colour approach means no shadow or gradient recalculation at different screen sizes — a maintenance advantage of flat design.

## 9. Agent Prompt Guide

> Recreate the hellodani.co aesthetic in Framer or React. Background: `rgb(246,245,241)` (warm cream). Text: pure black `#000`. Use **Libre Baskerville** at weight 400 for H1/H2 at 40px, −0.6px tracking. Use **Inter** at 16px for all body and links. Links are red: `rgb(253,30,31)`. Build four colour block elements: red `rgb(253,30,31)`, pink `rgb(255,143,202)`, yellow `rgb(255,203,65)`, blue `rgb(0,21,212)`. These are opaque, flat-filled containers — no gradients, no shadows. Cards are pure white `#fff` on the cream background. No shadows anywhere. Border radii on blocks vary: 8px, 16px, 24px, 32px. Add Framer Motion entrance animations to the colour blocks on scroll.

*Generated by Sparkbites — extracted from live CSS analysis*
