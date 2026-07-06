# jus.design — Design System Reference

## 1. Visual Theme & Atmosphere

jus.design is Justin Farrugia's personal portfolio — "Software Designer," previously founding designer at Maybe, now freelancing and building Curated Supply and CMD Supply — and it reads exactly like that resume: quiet, confident, no ornament. The canvas is a soft studio-grey (`rgb(242, 242, 242)`) rather than paper-white, with pure black text sitting directly on top — a two-tone frame with almost no mid-tones in the base layer. Against that restraint, a single saturated electric blue (`rgb(0, 102, 255)`) carries the entire brand voice, appearing only on the one interactive element that matters: the "Get in touch" action. Small-caps, tracked-out labels ("Malta, GMT+1," a live local clock, "Available for work") sit like a status bar above the fold, giving the page the feel of a designer's dashboard rather than a static brochure. Built on Framer with Framer Motion, the site trades visual noise for timing and restraint — one accent color, one typeface, one gesture.

---

## 2. Color Palette & Roles

**Foundation**
- `rgb(242, 242, 242)` — page canvas (studio grey, not paper-white)
- `rgb(0, 0, 0)` — primary text and default border color on the body
- `rgb(20, 20, 20)` — link ink; the "near-black" used instead of true black for anything interactive

**Accent (reserved for the single primary action)**
- `rgb(0, 102, 255)` — button background; the only saturated color in the system
- `rgb(255, 255, 255)` — button text and border, run against the blue fill

**Link states**
- Default: transparent background, `rgb(20, 20, 20)` text/border, `outline: rgb(20, 20, 20) none 3px`
- Hover: text and border fade to `rgb(136, 135, 135)` — a straight desaturation, no new hue introduced
- Focus: outline becomes `rgb(16, 16, 16) auto 1px` — a genuine keyboard-visible ring, distinct from the hover treatment

**Tonal ramp (surfaces, by luminance)**
- `rgba(255, 255, 255, 0.6)` — luminance 1 — translucent white overlay (glass/highlight layer)
- `rgb(242, 242, 242)` — luminance 0.949 — base canvas
- `rgb(191, 191, 191)` — luminance 0.749 — mid-light divider/surface
- `rgb(136, 135, 135)` — luminance 0.531 — the hover-state grey, reused as a surface tone
- `rgb(20, 20, 20)` — luminance 0.078 — near-black surface/ink

The palette is essentially a five-step monochrome ramp plus one deliberate blue accent. Nothing else competes with that blue — it is spent entirely on the call-to-action.

---

## 3. Typography Rules

Everything routes through **Inter** (and its variable-font sibling), with Framer's fallback chains: `"Inter Variable", "Inter Variable Placeholder", sans-serif` for UI chrome, `Inter, "Inter Placeholder", sans-serif` for text elements.

| Role   | Font              | Size  | Weight | Line-height    | Tracking | Transform |
|--------|-------------------|-------|--------|----------------|----------|-----------|
| h2     | Inter Variable    | 16px  | 400    | 22.4px (1.4)   | normal   | none      |
| Link   | Inter             | 16px  | 400    | 24px (1.5)     | normal   | none      |
| Button | Inter Variable    | 16px  | 400    | 16px (1.0)     | normal   | none      |
| p      | Inter             | 12px  | 500    | 12px (1.0)     | +0.48px  | uppercase |
| body   | sans-serif (root) | 12px  | 400    | normal         | normal   | none      |

**Principles**
- A single weight family carries almost the whole page: `400` for headings, links, and buttons — hierarchy comes from size and role, not boldness.
- The one exception is the `p` role at `500` weight, `12px`, set `uppercase` with `+0.48px` tracking and a tight `12px` line-height — this is the status-bar voice: location, live clock, availability tag. It is visually and functionally distinct from every other text role.
- `h2`, `Link`, and `Button` all carry `font-feature-settings: "cv06", "cv12", "cv13"` — Inter's character-variant stylistic alternates are switched on everywhere text is meant to read as UI rather than metadata, giving the sans a slightly more crafted, less default look without changing the typeface.
- Buttons compress line-height to `1.0` (`16px` on `16px` type) — tight, pill-like, no extra vertical breathing room inside the CTA.
- What's absent: no serif, no monospace, no italics, no bold weights, no display size jump — the type system stays flat and lets color/motion carry emphasis instead.

---

## 4. Component Stylings

**Primary button** (the one accent surface)
- Background: `rgb(0, 102, 255)`; text and border: `rgb(255, 255, 255)`
- Layered shadow: `inset 0 -1px 1px rgba(0,0,0,0.2)`, `inset 0 0 0 1px rgba(0,0,0,0.12)`, two stacked drop shadows `0 1px 3px rgba(0,0,0,0.17)`, and `inset 0 2px 0 rgba(255,255,255,0.15)` — a glossy, slightly convex "pressed-glass" surface rather than a flat fill. This is the only component in the system that gets true depth.
- Inter Variable 16px/400, line-height 16px — set tight, matching the pill shape

**Links**
- No background, no shadow, `rgb(20, 20, 20)` ink with matching border
- Hover fades the whole treatment (text + border + outline color) to `rgb(136, 135, 135)` — a desaturation, not a hue shift, not a transform
- Focus swaps to a native `auto 1px` outline in `rgb(16, 16, 16)` — accessibility is handled by the browser default outline, not a custom ring

**Meta labels** (the `p` role)
- Small, uppercase, tracked-out (`+0.48px`), tight leading — used for the live clock, location, and "Available for work" tag, functioning as a persistent status readout rather than page copy

**Border radius**
- `50px`, `999px` — full pill shapes for the button and any chip-like element
- `10px`, `20px` — soft-rounded corners for cards/content blocks
- `130px` — large radius reserved for the oversized portrait/avatar frame, softening a big square image into something closer to circular without fully rounding it

**Shadows**
- Reserved almost entirely for the button (see above); a near-identical second variant (`inset 0 -1px 1px rgba(0,0,0,0.2)`, `inset 0 0 0 1px rgba(0,0,0,0.12)`, two `0 1px 3px rgba(0,0,0,0.17)` drops) without the top highlight likely represents the button's pressed/active state — same glossy family, one layer quieter.

---

## 5. Layout Principles

- Single-column, centered hero composition: portrait, name, role, one-line bio, then a status row (availability, clock, location) and a single CTA — the whole above-the-fold is a personal dashboard, not a marketing grid.
- Minimal nav surface (`Work`, `About`) — navigation is secondary to the hero's introduction.
- Breakpoints at `809.98px` / `810px` / `1199.98px` — Framer's standard two-step mobile/tablet boundary plus a desktop cutoff; the tight `809.98/810` pairing is a generator artifact marking exactly where the mobile layout hands off to tablet.
- Body-level spacing resets to zero (`padding: 0, margin: 0, gap: normal`) — every real spacing decision lives inside Framer's canvas frames, not in global CSS.
- The oversized portrait image (`1080×1080` / `1464×1464` source) anchors the layout visually before any text is read — the page leads with a face, then a title, then a sentence.

---

## 6. Depth & Elevation

Depth is almost entirely suppressed except in one place. The five-step luminance ramp (1 → 0.949 → 0.749 → 0.531 → 0.078) exists for tonal separation between overlays, canvas, dividers, and ink — not for shadow-based elevation. The translucent white overlay (`rgba(255,255,255,0.6)`, luminance 1) suggests a glass/highlight layer used sparingly, likely on hover or image treatments.

The single exception is the primary button: a genuinely glossy, multi-layer inset+drop shadow stack that gives it a convex, tactile quality against an otherwise flat page. That contrast is intentional — everything else is quiet so the one clickable blue surface reads as unmistakably interactive.

---

## 7. Do's and Don'ts

**Do**
- Use `rgb(242, 242, 242)` as the base canvas — never pure white; it keeps the page feeling like a studio surface, not a document.
- Reserve `rgb(0, 102, 255)` for exactly one thing: the primary call-to-action. Do not spread it across nav, links, or borders.
- Set links in `rgb(20, 20, 20)`, not true black, and fade them to `rgb(136, 135, 135)` on hover — a desaturation, never a hue change.
- Give the primary button the full glossy shadow stack (inset highlight + inset border + double drop shadow) — it's the one place depth is allowed.
- Use the uppercase, tracked `12px/500` label style for live/status metadata (clock, location, availability) — keep it visually separate from body and links.
- Turn on Inter's `cv06/cv12/cv13` character-variant features on UI text (headings, links, buttons) for a slightly more crafted default sans.
- Use `999px`/`50px` radii for pills and CTAs, `10px`/`20px` for cards, and reserve a large radius like `130px` for oversized portrait/avatar frames only.

**Don't**
- Don't introduce a second accent color — the system is built around exactly one saturated hue.
- Don't add shadows to links, nav, or cards — depth belongs to the button alone.
- Don't use font weights above `400` outside the uppercase meta-label role (`500`) — there is no bold voice in this system.
- Don't set body copy in uppercase — that transform is reserved for the small status-bar label role.
- Don't flatten the button's shadow to a single flat drop-shadow — the glossy multi-layer stack is the signature, not incidental.

---

## 8. Responsive Behavior

Three Framer-generated breakpoints: `809.98px` (mobile ceiling), `810px` (tablet floor), and `1199.98px` (desktop ceiling) — a standard mobile → tablet → desktop three-tier system with no extra ultrawide tier. Because body spacing is zero and all layout lives in Framer canvas frames, responsive behavior is handled per-frame rather than via global type or spacing overrides; the hero's single-column, centered composition is built to compress gracefully since it never depended on a multi-column grid to begin with.

---

## 9. Agent Prompt Guide

> Build a UI that matches jus.design's design language.

Set the canvas to studio grey `rgb(242, 242, 242)` — never pure white — with black (`rgb(0, 0, 0)`) body text and near-black `rgb(20, 20, 20)` for links. Use **Inter** (Variable weight for UI chrome, static for text) everywhere, held at weight `400` for headings/links/buttons at `16px`; the one exception is a small uppercase status-label role at `12px/500` with `+0.48px` tracking and tight `1.0` line-height, reserved for live/meta info like a clock or location tag. Turn on Inter's `cv06/cv12/cv13` character-variant features on interactive text. Reserve one saturated accent, electric blue `rgb(0, 102, 255)`, for exactly one primary CTA button — white text and border on the blue fill, with a genuinely glossy shadow stack (inset top highlight, inset border, two soft drop shadows) so it reads as the single tactile, clickable surface on an otherwise flat page. Links have no background; on hover, fade text/border/outline to mid-grey `rgb(136, 135, 135)` rather than shifting hue, and let focus rely on a native `1px auto` outline. Use pill radii (`50px`/`999px`) for buttons and chips, softer `10px`/`20px` radii for cards, and a large `130px` radius only for oversized portrait or avatar frames. Keep everything else — nav, cards, dividers — flat and shadow-free; depth and color are both spent on the same single button.

---

*Generated by Sparkbites — extracted from live CSS analysis*
