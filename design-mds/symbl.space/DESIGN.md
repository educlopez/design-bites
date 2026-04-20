# Symbl — Design System Reference

## 1. Visual Theme & Atmosphere

Symbl tests how your logo performs at every scale — and the tool's own chrome is a demonstration of the same discipline. The page splits vertically down the middle: the left half is a warm concrete-grey canvas (`rgb(184, 184, 184)`) holding the brand plate and an upload zone; the right half is pure `rgb(10, 10, 10)` inkwell — one black field where the designer watches their submitted logo against a worst-case dark backdrop. That split is the entire interface. A single serif wordmark — "Symbl™ — V2" — anchors the lighter half, and everything below it is **Geist Mono** at 9-10px in positive-tracked uppercase: a typographic language that reads like a printmaker's signature block rather than a SaaS dashboard. The atmosphere is dry, cerebral, and confident. There is no marketing gloss, no gradient, no illustration, no hover state doing work it shouldn't. Symbl is the kind of tool a designer builds for other designers — and it shows in every restraint.

---

## 2. Color Palette & Roles

**Foundation — the split canvas**
- `rgb(184, 184, 184)` — left canvas (warm concrete grey, the whole brand frame)
- `rgb(10, 10, 10)` — right canvas (inkwell, worst-case dark test surface)

**Ink & text**
- `rgb(51, 51, 51)` — primary text / borders on the light half
- `rgb(85, 85, 85)` — secondary text (buttons, fine print)
- `rgb(17, 17, 17)` — text on hover (one step darker than secondary)
- `rgb(187, 187, 187)` — link text on the light half (a deliberately low-contrast blue-less hyperlink)
- `rgb(221, 221, 221)` — underline color on links (a fainter shadow of the link color itself)

**Surfaces (within the light half)**
- `rgba(255, 255, 255, 0.52)` — upload-zone fill (semi-transparent white on the concrete)
- `rgb(244, 244, 244)` — hidden-state panel fill (nearly white, luminance 0.96)

**Interactive chrome**
- `rgba(0, 0, 0, 0.04)` button default bg + `rgba(0, 0, 0, 0.12)` border — an almost-invisible pill that darkens on hover
- `rgba(0, 0, 0, 0.08)` button hover bg + `rgb(17, 17, 17)` text — a tonal step, not a color change

The palette is aggressively **monochromatic**: there is no accent color, no brand hue, no status green or red. The only "chromatic" moment is the warm cast of the concrete grey — which is slightly off-neutral on purpose, so the right-hand black field reads as absence rather than as a second color.

---

## 3. Typography Rules

**Typefaces**
- **Geist Mono** (weight 300) — the entire body and UI voice: body, inputs, buttons, links, manifesto, build credits
- A **custom serif wordmark** for "Symbl" in the brand plate (not extracted here — it's set as an SVG/image, not live type). The V2 suffix is also serif. The serif appears in the logomark only; the rest of the interface is mono.

**Scale**

| Role | Font | Size | Weight | Line-height | Tracking | Transform |
|------|------|------|--------|-------------|----------|-----------|
| Body | Geist Mono | 16px | 300 | 24px | normal | none |
| Input | Geist Mono | 16px | 300 | 24px | normal | none |
| A (link) | Geist Mono | 9px | 300 | 13.5px | +1.08px | uppercase |
| Button | Geist Mono | 9px | 300 | 13.5px | +0.9px | uppercase |

**Principles**
- **One mono face, one weight (300).** Every piece of UI text is Geist Mono Light. Hierarchy is driven by size + case + tracking, never by weight swap.
- **Tiny uppercase for chrome.** Buttons and links sit at 9px with `+0.9–1.08px` positive tracking and uppercase transform. This is lapidary micro-type — it reads at arm's length as a tight horizontal rule of letters, not as an interactive control. It's the same treatment you see on 1970s Swiss industrial controls.
- **Body prose stays at 16px.** The contrast between 16px body and 9px chrome is extreme — one is meant to be read, the other is meant to be acknowledged.
- **Normal tracking only on the 16px tier.** All micro-type gets positive tracking; all body-size type stays at the default kerning. This is the opposite of the usual design-system rule (negative tracking on display, positive on caps) because Symbl has no display tier — only body and micro.

**What's absent:** no italic, no bold, no second mono, no sans-serif body. Geist Mono + the serif wordmark is the entire typographic system.

---

## 4. Component Stylings

**Buttons** — e.g. "TRY AN EXAMPLE"
- Default: `rgba(0, 0, 0, 0.04)` bg, `rgb(85, 85, 85)` text, `rgba(0, 0, 0, 0.12)` border
- Hover: bg steps to `rgba(0, 0, 0, 0.08)`, text darkens to `rgb(17, 17, 17)` — border unchanged
- No shadow, no transform, no opacity change
- Border-radius: `999px` — full pill, which makes the 9px uppercase text read as a typographic mark rather than a clickable control

**Upload zone** (the primary interaction)
- Background: `rgba(255, 255, 255, 0.52)` — a 52% opaque white over the concrete, so the canvas texture shows through
- Dashed border (implied by the visual — not explicit in the extracted radii)
- Only one border-radius value exists in the system: `999px`. The upload zone appears to use a hairline or no radius.

**Links**
- Color: `rgb(187, 187, 187)` — a muted grey, **not** blue. Links are deliberately low-contrast.
- Underline: `rgb(221, 221, 221)` — even lighter than the link color, so the underline is a whisper
- 9px uppercase with `+1.08px` tracking — same treatment as buttons, no chromatic affordance

**Inputs**
- Transparent background, `rgb(51, 51, 51)` text and border — the field is defined by a hairline, not a fill

**No shadows detected.** Depth is entirely tonal.

---

## 5. Layout Principles

- **Vertical 50/50 split.** The canvas divides cleanly into a light half (brand + upload + instructions) and a dark half (preview field with "DESIGNERS ARE ALREADY USING IT" caption). Both halves run full viewport height.
- **Centered brand plate.** The Symbl wordmark sits roughly 1/3 down the light half, with the tagline ("TEST YOUR LOGO BEFORE THE WORLD DOES.") and primary CTA stacked beneath it — a classic print masthead composition.
- **Footer chrome as type strip.** Bottom-left: "MANIFESTO". Center: "BUILT BY GUILLAUME — ANAGRAM". Bottom-right: "V.2 — 2026-03-27" plus a tiny sphere glyph (blue bauble — one point of chromatic warmth in the whole UI). These are all 9px uppercase Geist Mono — the same class of type as the buttons. Footer is a single horizontal rule of information, not a hierarchy.
- **Zero body/section padding.** The layout is composed inside positioned frames; global elements have `padding: 0, margin: 0`.

---

## 6. Depth & Elevation

Depth is achieved entirely through the **50/50 luminance contrast** between the two canvas halves (0.52 on the light side, 0.04 on the dark side) — a binary figure/ground split that is the primary depth cue of the whole interface. Within each half, additional depth is minimal:

- `rgba(255, 255, 255, 0.52)` upload zone sits ~0.3 luminance above the concrete canvas — a soft paper-on-stone feel
- `rgb(244, 244, 244)` hidden panels sit at 0.96 luminance — near-white, a small step up

No `box-shadow` values exist anywhere in the extracted system. The black half needs no depth because it's doing its job by being deliberately empty.

---

## 7. Do's and Don'ts

**Do**
- Split the frame 50/50 (or 60/40) in concrete `rgb(184, 184, 184)` and inkwell `rgb(10, 10, 10)`. The duality is the brand.
- Use Geist Mono (or any disciplined mono) at weight 300 exclusively. Do not ship a second typeface.
- Scale chrome to 9px uppercase with `+0.9–1.08px` positive tracking. The micro-caps register as brand, not UI.
- Use `999px` (full pill) radius on buttons so the shape reads as a type cartouche rather than a clickable control.
- Keep button hover as a ~4% bg darkening and a tonal text-step — no color change, no shadow, no transform.
- Reserve the serif voice for the wordmark only. The rest of the interface stays mono.
- Treat the footer as a single 9px-type strip with three alignments (left, center, right) — not a layout block.

**Don't**
- Don't introduce a brand accent color. The whole point is that logos are tested against neutral grounds, not against brand palettes.
- Don't use a sans-serif body. Geist Mono is the voice.
- Don't add drop-shadows or glows — they contradict the tool's premise.
- Don't underline links in a contrasting hue. Underlines here are *lighter* than the text.
- Don't set button text at 12px+ — the compression to 9px is what makes the chrome feel inscribed.
- Don't use a warm white. The "white" in this system is `rgba(255,255,255,0.52)` — half-opaque on concrete. Pure white breaks the tonal logic.

---

## 8. Responsive Behavior

No breakpoints were extracted — the site is likely handled by a small set of viewport-width clauses inside the Next.js component tree rather than `@media` rules in stylesheets, or it composes entirely with flexbox and leaves responsive behavior to the 50/50 split resizing fluidly. In practice, the vertical split should collapse to a stacked layout below ~768px (light half on top, inkwell below) so both halves remain visible. The 9px chrome type is already near the minimum legible size; it should not compress further. Any responsive strategy must preserve the split — the black field is not decoration; it's a required test surface.

---

## 9. Agent Prompt Guide

> Build a UI in Symbl's design language.

Split the viewport 50/50: left half `rgb(184, 184, 184)` (warm concrete grey), right half `rgb(10, 10, 10)` (inkwell black). Set body text to **Geist Mono 300 at 16px** on the light side, `rgb(51, 51, 51)` ink. Chrome — buttons, links, labels, footer strip — is **Geist Mono 300 at 9px uppercase** with `+0.9–1.1px` positive letter-spacing. Buttons are full pill (`border-radius: 999px`) with a `rgba(0, 0, 0, 0.04)` background and a `rgba(0, 0, 0, 0.12)` border; on hover, step the background to `rgba(0, 0, 0, 0.08)` and darken text from `rgb(85, 85, 85)` to `rgb(17, 17, 17)`. No color changes, no shadows, no transforms. Links are grey-on-grey (`rgb(187, 187, 187)` text, `rgb(221, 221, 221)` underline) — never blue. Upload zones and surface panels sit at `rgba(255, 255, 255, 0.52)` — half-opaque white — so the concrete shows through. Reserve serif type for a single logomark; everything else is mono. Use the dark half for worst-case logo preview (or any content that benefits from reversed treatment) and leave it otherwise empty. Depth comes from the 50/50 luminance split alone — no shadows anywhere.

---

*Generated by Sparkbites — extracted from live CSS analysis*
