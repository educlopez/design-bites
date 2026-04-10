# Form Nutrition — Design Language Reference

## 1. Visual Theme & Atmosphere

Form Nutrition inhabits the intersection of wellness and authority — a nutrition brand that wants to be taken seriously by athletes and skeptics alike. The design speaks softly but with conviction: clean white space, premium typography, and a restrained color palette anchored in black and natural off-whites. It refuses the garish color conventions of the supplement industry.

Built on WordPress with Gutenberg blocks, the site achieves a level of editorial refinement unusual for its CMS. The spacing system follows a deliberate 8px-based scale (0.44rem → 5.06rem), giving every block room to breathe. The result feels like a high-end print catalog translated to the web — composed, unhurried, and confident in its silences.

---

## 2. Color Palette & Roles

**Foundation**
- `#000000` — Primary text, headings, borders
- `#FFFFFF` — Page background, card surfaces

**Brand Accent**
- `#7A00DF` — Synced block highlight, editorial callout color (vivid purple — used sparingly as a signal, not decoration)

**Status / UI Chrome** (WordPress admin tokens, not design-facing)
- `#007CBA` / `#006BA1` / `#005A87` — Admin theme colors; not present in front-end design

**WordPress Preset Palette** (available, rarely used in hero contexts)
- Standard WP block palette present but subordinate to the brand's own editorial choices

**Typography Colors**
- `#000000` for all display text; consistent with the brand's refusal to use gray-on-white softening

**What's absent:** No gradient on the marketing surface. No illustrated or photographic tinting. The purple accent is used with the discipline of a single drop of ink in water — once is enough.

---

## 3. Typography Rules

Form Nutrition uses **Avenir Next** as its primary typeface, delivered as a custom variant (`"Avenir Next - Regular"`). This is a geometric humanist sans-serif — precise and modern, but warmer than Futura. Body copy and captions both draw from this family.

| Level | Size | Weight | Line Height | Notes |
|-------|------|--------|-------------|-------|
| Display (WP huge) | 42px | — | — | Editorial hero text |
| Large | 36px | — | — | Section headings |
| Medium | 20px | — | — | Sub-headings, callouts |
| Body (normal) | 16px | 400 | 30px | Generous line height for readability |
| Small | 13px | — | — | Captions, legal |
| Figcaption | 15px | 400 | 30px | Avenir Next Regular |

The 30px line height on body text (1.875× ratio) is the site's most distinctive typographic decision — it reads like a well-designed print article, not a web page. This density invites reading rather than scanning.

**What's absent:** No rounded or display typeface. No monospace. No letter-spacing manipulation on body text.

---

## 4. Component Styling

**Cards / Blocks**
- WordPress Gutenberg block grid; standard spacing tokens apply
- Shadows from WP presets: `natural` (6px 6px 9px rgba(0,0,0,0.2)), `deep` (12px 12px 50px rgba(0,0,0,0.4)), `sharp` (6px 6px 0px rgba(0,0,0,0.2))
- The `sharp` shadow (no blur) is notable — it creates a graphic, almost screen-printed quality

**Buttons**
- Consistent with black/white system; no rounded pill shapes implied by the editorial register
- Focus state: 2px admin border width — accessibility-conscious

**Aspect Ratios**
- Full WP preset set: square (1:1), 4:3, 3:4, 3:2, 2:3, 16:9, 9:16
- 3:4 portrait ratio suggests strong vertical product photography

**Spacing Scale**
| Token | Value |
|-------|-------|
| `--spacing-20` | 0.44rem |
| `--spacing-30` | 0.67rem |
| `--spacing-40` | 1rem |
| `--spacing-50` | 1.5rem |
| `--spacing-60` | 2.25rem |
| `--spacing-70` | 3.38rem |
| `--spacing-80` | 5.06rem |

---

## 5. Layout Principles

The layout follows a centered editorial column with generous outer margins. Gutenberg's block spacing controls vertical rhythm via the spacing scale above. The overall impression is a magazine grid: clear vertical flow, distinct section breaks, no sidebar distractions.

The wide line height on body text and the generous spacing steps mean the site breathes more than most e-commerce. This is intentional — Form is selling trust, not urgency.

---

## 6. Depth & Elevation

Three shadow presets define the elevation vocabulary:

- **Natural** — `6px 6px 9px rgba(0,0,0,0.2)`: Soft, directional. Used for product cards that need gentle lift.
- **Sharp** — `6px 6px 0px rgba(0,0,0,0.2)`: No blur, hard-edged. Graphic, editorial — feels like a offset print effect.
- **Deep** — `12px 12px 50px rgba(0,0,0,0.4)`: Heavy ambient shadow for modal or hero overlay elements.

The `sharp` shadow is the most distinctive and brand-aligned — it pairs beautifully with Avenir Next's geometric forms.

---

## 7. Do's and Don'ts

**Do**
- Use 30px line height on body text — it's the site's signature breathing room
- Apply Avenir Next consistently across all text; it unifies the editorial voice
- Favor the `sharp` shadow (no blur) for graphic, high-contrast card effects
- Honor the vertical spacing scale; don't skip levels
- Use the purple accent (`#7A00DF`) once per page maximum — it loses power with repetition

**Don't**
- Use supplement-industry conventions (neon accents, muscle photography with hard gradients)
- Reduce line height below 1.6 — the readability contract breaks
- Mix in the WordPress preset palette colors; they exist for blocks but clash with the editorial voice
- Add decorative borders or dividers; white space does this job

---

## 8. Responsive Behavior

WP preset spacing scales are fixed values (rem-based), not fluid. The site uses standard Gutenberg responsive stacking. Aspect ratio presets suggest images are art-directed across viewports — portrait crops (3:4, 2:3) likely replace landscape (16:9, 3:2) on mobile to maximize vertical product focus.

No CSS custom properties for fluid type were detected — responsive text sizing is handled at the block level, not via a token system.

---

## 9. Agent Prompt Guide

> "Design in the style of Form Nutrition: white background, black text, Avenir Next typeface. Body text at 16px with 30px line height. Editorial spacing with generous vertical rhythm. Cards use a sharp no-blur offset shadow `6px 6px 0px rgba(0,0,0,0.2)` for a graphic, print-inspired quality. The purple accent `#7A00DF` appears once as a focal callout. No gradients, no rounded pill buttons, no supplement-industry energy. Think: high-end print wellness catalog translated to web — composed, authoritative, unhurried."

---

*Generated by Sparkbites — extracted from live CSS analysis*
