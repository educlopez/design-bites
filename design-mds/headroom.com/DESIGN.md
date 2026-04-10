# headroom.com — Design System

## 1. Visual Theme & Atmosphere

Headroom is the most systemically complete design in this collection. The CSS reveals an obsessive token architecture: a full blue-scale with 13 opacity stops, a complete pastel palette with 14 hues × 3 tonal levels (light/mid/dark), a dark-mode-ready token system, and component-level tokens for buttons, banners, dialogs, accordions, and switches. The product (meditation and mental wellness) is rendered visually as: bold electric blue (`#335cff`) against clean white, with the footer in that same vivid blue — a confident, active brand statement. TWK Lausanne as the headline typeface brings a refined editorial quality. The design reads as "institutional clarity with warm confidence" — not cold-tech, not soft-wellness, but a specific middle register.

## 2. Color Palette & Roles

**Brand blue** (the identity colour)
- `hsl(230 100% 54%)` — `#335cff` — used for the primary CTA and the entire footer
- `hsl(234.55 100% 97.84%)` — `#e8ebff` — pale blue tint

**Neutrals**
- Body text: `#171717` — near-black (warm)
- Muted text: `#5c5c5c` / `#737373` / `#a3a3a3` — three grey tiers
- Borders: `#ebebeb` — light grey
- Backgrounds: `#fff` (white) / `#f7f7f7` (near-white) / `#1c1c1c` (dark surfaces)

**Pastel accent system** (14 hues, 3 tiers each — e.g. lilac, purple, pink, red, orange, brown, yellow, lime, sage, green, emerald, teal, blue, neutral)
- Light tier: very pale, ~94% lightness — for background zone tinting
- Mid tier: ~50% lightness — for icon fills
- Dark tier: ~80% lightness — for stronger accents within light contexts

**Semantic**
- Error: `hsl(0 100% 43%)` / dark: `hsl(0 100% 34%)`
- Warning: `hsl(25 89% 52%)`
- Success: `hsl(142 100% 34%)`

**What's absent:** No gradients. No shadows on the main design (extraordinary for a SaaS site). The blue is used full-saturation — no tints in structural elements.

## 3. Typography Rules

Two-tier system: **TWK Lausanne** for all brand-facing elements, system sans-serif for UI.

| Element | Font | Size | Weight | Tracking |
|---------|------|------|--------|----------|
| H1 | TWK Lausanne | 84px | 700 | −0.168px |
| H2 | TWK Lausanne | 120px | 500 | −3.6px |
| Body | System sans | 13.2px | 400 | Normal |
| `<p>` labels | System sans | 11px | 700 | −0.275px |
| Button | TWK Lausanne | 14.8px | 500 | Normal |
| Input | TWK Lausanne | 14.8px | 400 | Normal |

The H2 at 120px with −3.6px tracking is the most dramatic typographic choice in this collection — cinematic, poster-scale. Weight 500 keeps it refined rather than aggressive. The contrast between this headline weight and the 11px label text (body) creates extreme hierarchy. Buttons use TWK Lausanne — a choice that maintains brand voice in interactive elements.

## 4. Component Stylings

**Buttons** — the token system reveals four types:
- *Primary* — `#335cff` fill, white text, inset shadow for depth
- *Neutral* — `#5c5c5c` fill
- *Neutral-soft* — `#ebebeb` fill
- *Text* — transparent background

All buttons: `0.375rem` border-radius (`6px`), weight 500 at 0.875rem (14px), inset shadow: `0 0 0 1px` border ring + `0px 1px 2px` ambient.

**Accordion** — full token set: 0.625rem radius (10px), 0.2s ease-out animation, hover states via `#f7f7f7`.

**Dialog/Banner** — 1.25rem radius (20px) — noticeably rounder than other components.

**Consent widgets** — extensive consent management system with its own token set (c15t pattern), suggesting GDPR/privacy is a product feature.

**Footer** — full-bleed `#335cff` blue background with white/60% opacity links.

## 5. Layout Principles

Main content: 128px top and bottom padding — generous breathing room. No horizontal padding on `<main>` (uses inner containers). Six breakpoints from 400px to 1400px give thorough responsive coverage. The 400px breakpoint (below typical 480px) suggests small phone optimisation.

The footer-as-brand-moment (full blue) is a layout statement: the exit of every page is the brand itself.

## 6. Depth & Elevation

Unusual for a marketing site: no shadows on content surfaces. The entire depth language is:
- Button inset shadow (subtle border ring + 1px ambient)
- Dialog card shadow: `0 1px 2px rgba(0,0,0,.05)` — barely visible
- Banner shadow: `0 16px 32px -12px rgba(14,18,27,.1)` — floating panels

The vivid blue footer and blue fixed elements create visual weight through colour saturation, not shadow.

## 7. Do's and Don'ts

**Do:**
- Use TWK Lausanne at 120px, weight 500, −3.6px for the hero headline
- Apply `#335cff` only to the primary CTA and the footer — treat it as a punctuation colour
- Build the full token set: buttons, banners, dialogs each get their own variables
- Use 6px radius for buttons, 20px for dialogs, 10px for accordions
- Apply the pastel accent palette to category/tag colour coding (14 hues × 3 tiers)

**Don't:**
- Add shadows beyond the three minimal values
- Use blue anywhere in body content — it's reserved for brand moments
- Mix TWK Lausanne at body sizes — system fonts handle reading text
- Use pure black — `#171717` is the warmest dark available
- Ignore the dark-mode token set — it's built in and should be wired up

## 8. Responsive Behavior

Six breakpoints (400–1400px). The 120px H2 headline presumably scales aggressively — likely to 48–60px at mobile. The body text at 13.2px may remain consistent (it's already compact). The footer blue fills the viewport at all widths, making it a persistent brand element regardless of screen size.

The `--banner-max-width: 440px` and `--dialog-max-width: 28rem` constrain overlay content for readability on wide screens.

## 9. Agent Prompt Guide

> Build in the headroom.com style: white background, `#171717` text. Use **TWK Lausanne** for all headings and buttons. Hero headline at 120px, weight 500, −3.6px tracking. Set up a full token system for buttons (`--button-primary: #335cff`, `--button-border-radius: .375rem`, `--button-font-weight: 500`). Footer is full-bleed `#335cff` blue with white text — the single brand colour moment. System sans-serif for all body copy at 13.2px. No decorative shadows. Buttons use inset box-shadow for border: `inset 0 0 0 1px var(--button-primary)`. A complete pastel category palette (14 hues × light/mid/dark) for any tag or label system. The only shadow on surface elements should be `0 1px 2px rgba(0,0,0,.05)`.

*Generated by Sparkbites — extracted from live CSS analysis*
