# whop.com — Design System

## 1. Visual Theme & Atmosphere

Whop occupies the intersection of SaaS ambition and underground-internet energy. The dominant mode is dark — near-black backgrounds with high-contrast off-white text — but the brand refuses to be merely "another dark app." It injects electric bursts of electric-lemon yellow (`#dbf505`) and searing orange-red (`#fa4616`) into an otherwise restrained palette, signalling speed, novelty, and irreverence. The overall atmosphere reads like a neon sign in a blacked-out room: precise, intentional, impossible to ignore. The dual-typeface strategy — a custom grotesque for display, Inter for everything else — keeps the brand voice confident without becoming chaotic.

---

## 2. Color Palette & Roles

### Background & Surfaces
| Role | Value | Usage |
|---|---|---|
| Page canvas | `#111111` | Main content area, section backgrounds |
| Overlay/frosted panel | `rgba(29,29,29,0.85)` | Sticky header — glassmorphic dark panel |
| Elevated surface | `#222222` | Cards, modals |
| Light frosted | `#f9f9f9` | Occasional light-mode inset components |

### Text
| Role | Value | Usage |
|---|---|---|
| Primary text (dark surfaces) | `#eeeeee` | Body copy on dark |
| Primary text (light surfaces) | `#202020` | Body copy on light |
| Muted | `#484848` | Secondary labels, captions |

### Brand & Accent
| Role | Value | Usage |
|---|---|---|
| Blue (CTA) | `#1754d8` | Primary action buttons, links |
| Lemon yellow | `#dbf505` | Hero badges, highlight banners, energy accents |
| Orange-red | `#fa4616` | Warning badges, pricing highlights, urgency signals |
| Orange tint | `rgba(255,40,0,0.176)` | Soft background for orange-bordered elements |

### Borders & Dividers
- Light border (dark context): `rgba(255,255,255,0.106)`
- Dark border (light context): `rgba(0,0,0,0.12)`

---

## 3. Typography Rules

Whop uses a two-tier font system. **AcidGrotesk** — a custom display grotesque — owns all headline moments. **Inter** handles everything functional.

| Selector | Font | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|---|
| H1 | AcidGrotesk | 80px | 700 | 88px | −4.45px |
| H2 | AcidGrotesk | 40px | 500 | 44px | −2.225px |
| Body | Inter | 16px | 400 | 24px | normal |
| Paragraph | Inter | 24px | 400 | 30px | −0.39px |
| Button | Inter | 16px | 500 | 24px | −0.18px |

The aggressive negative tracking on headlines (−4.45px at 80px) is a deliberate compression that makes large type feel dense and authoritative. Body paragraph text sits large at 24px — Whop wants copy to be read, not skimmed. No uppercase transforms are used anywhere; the brand speaks in lowercase confidence.

---

## 4. Component Styling

**Buttons** use 1px inset ring shadows to create a subtle depth layer without elevation:
- Light context: `rgba(255,255,255,0.133) 0 0 0 1px inset, rgba(0,0,0,0.05) 0 1px 2px`
- Dark context: `rgba(0,0,0,0.12) 0 0 0 1px inset, rgba(0,0,0,0.05) 0 1px 2px`

**Border radii** range from `8px` (tight inputs, small chips) to `24px` (large cards, hero panels). The `1.12px` micro-radius on certain elements suggests precise sub-pixel rendering for icon containers.

**Badges** combine colored backgrounds (`bg-lemon-9`, `bg-orange-9`) with matching text at full saturation — no tinting or desaturation for these; they're meant to pop hard.

**Nav header** is frosted glass: `rgba(29,29,29,0.85)` with an 8px vertical padding and a near-invisible white border (`rgba(255,255,255,0.106)`), giving it a floating feel.

---

## 5. Layout Principles

Layout is full-bleed, section-by-section with zero padding at the section and main level — all spacing lives inside components. The header sits at `8px 0` padding, slim and sticky. No max-width container is exposed in the CSS snapshot, suggesting wide or full-viewport layouts with internal column constraints. The dark main canvas extends edge-to-edge, reinforcing immersion.

---

## 6. Depth & Elevation

Depth is achieved almost exclusively through color layering and inset ring shadows rather than traditional drop shadows. The elevation ladder reads:
1. `#111111` — base canvas (darkest)
2. `#222222` — raised cards
3. `rgba(29,29,29,0.85)` — floating header (blur implied by frosted class)
4. `#f9f9f9` / white — highest contrast insets (light-on-dark)

There are no large ambient drop shadows. The inset 1px ring technique is the primary depth signal — minimal, structural, unobtrusive.

---

## 7. Do's and Don'ts

**Do:**
- Use lemon or orange accent only for a single element per view — scarcity is what makes them land
- Apply negative letter-spacing to all display text (at least −0.5% at large sizes)
- Keep structural UI on dark surfaces; reserve white surfaces for focused content insets
- Use Inter at 500 weight for buttons; never 400

**Don't:**
- Use AcidGrotesk below 32px — it loses its character and becomes noise
- Mix lemon and orange in the same visual zone; they clash rather than harmonise
- Add elevation drop-shadows — the brand lives in flatness punctuated by inset rings
- Use any uppercase transforms; the voice is lowercase

---

## 8. Responsive Behavior

No explicit breakpoint data was captured in the CSS snapshot. Based on structural signals: sections are full-bleed at all widths, header collapses to minimal padding. The 24px paragraph size likely scales down on mobile (Inter handles this gracefully). The aggressive H1 tracking (−4.45px) should be proportionally reduced at smaller type sizes.

---

## 9. Agent Prompt Guide

> Build a dark-mode SaaS landing section in the style of whop.com. Use a near-black background (`#111111`), off-white text (`#eeeeee`), and AcidGrotesk (or any condensed grotesque) for headlines at 80px/700 weight with −4.45px letter-spacing. Inject a single electric-lemon (`#dbf505`) or orange-red (`#fa4616`) badge for energy. Body copy uses Inter 24px/400. Buttons carry an inset 1px ring shadow. Border radii: 8–24px. No drop shadows. No uppercase. Keep section padding internal to components — main and section elements have no padding themselves.

---

*Generated by Sparkbites — extracted from live CSS analysis*
