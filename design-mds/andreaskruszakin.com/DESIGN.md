# andreaskruszakin.com — Design Language

## 1. Visual Theme & Atmosphere

Andreas Kruszakin's portfolio occupies a distinctive corner of the designer-portfolio space: sky-blue as the dominant surface colour, not as accent. The background is a washed periwinkle-blue (`rgb(165,219,255)`), shifting to a slightly more saturated sibling on cards (`rgb(138,208,255)`). There is no dark mode, no white canvas — the sky-blue ground is the identity. Against it, a serif headline font (Recia) and a monospace body font (Spline Sans Mono) create an unusual editorial pairing that feels simultaneously bookish and technical. Built in Framer, the layout is fluid and animation-forward, but the design system underneath is spare: two fonts, a blue-and-black palette, tight negative tracking, and careful use of rounded corners. The atmosphere reads as thoughtful craft — a product designer who thinks in systems but has a clear visual point of view.

## 2. Color Palette & Roles

The entire site lives in a blue-and-black world. No warm neutrals, no off-whites, no accent pop.

**Backgrounds**
- `rgb(165, 219, 255)` — Body background; a calm sky blue. The defining colour of the site's identity.
- `rgb(138, 208, 255)` — Card/section surface; slightly more saturated to create layer differentiation without leaving the blue family.

**Text & foreground**
- `rgb(0, 0, 0)` — Body text and headings; pure black on the blue ground. High contrast, direct.

**Interactive**
- `rgb(0, 0, 238)` — Link default colour; the browser-default blue that reads as a deliberate, retro-informed choice rather than an oversight. On hover: no change observed (text-only interaction).

**Borders**
- `rgb(0, 0, 0)` — Border colour matches text; clean, consistent.

## 3. Typography Rules

Two typefaces in intentional contrast:

**Recia** — A contemporary serif with editorial presence. Used for headings.

**Spline Sans Mono** — A refined monospace face. Used for body/paragraph text, an unusual choice that signals technical rigor without sacrificing readability.

| Element | Font | Size | Weight | Leading | Tracking |
|---------|------|------|--------|---------|---------|
| h1/headings | Recia | — | 500 | — | −0.8px |
| body / p | Spline Sans Mono | 17px | 400 | 26px (1.53) | −0.85px |

Both faces are negative-tracked — the letter-spacing compression (-0.8px / -0.85px) tightens the overall texture and signals intentionality. The heading weight (500) is medium, not bold — headline authority comes from the serif's intrinsic presence, not from weight. Using monospace for prose is a strong identity decision: it separates Kruszakin's voice from every Söhne or Inter portfolio in the space.

## 4. Component Stylings

**Cards / sections** — Surface colour shifts from body (`rgb(165,219,255)`) to card (`rgb(138,208,255)`). No borders needed; the luminance delta creates the boundary.

**Radius** — Two values used: `14px` for smaller elements (tags, chips), `48px` for larger containers (likely CTA buttons or featured blocks). Both values read as intentional, leaning toward pill-like rather than sharp.

**Shadows** — One inset shadow present, adding subtle depth to surfaces without lifting them.

**Links** — Browser-default blue (`rgb(0,0,238)`) maintained as a deliberate choice; the anachronistic colour feels knowing rather than accidental in this editorial context.

## 5. Layout Principles

Built on Framer. Breakpoints cluster around a dense responsive ladder: 599 / 600 / 809 / 810 / 999 / 1000 / 1199 / 1200 / 1365 / 1492px — Framer's auto-generated breakpoints from canvas-size presets. The layout is likely a single-column reading column on mobile, expanding to a wider grid at 810px+ and a full desktop layout at 1200px+.

Spacing is Framer-managed (no explicit CSS custom property tokens). The negative letter-spacing on both font roles means copy looks deliberately compressed — content density is higher than the airy background colour would suggest.

## 6. Depth & Elevation

Depth is handled via background-colour shifts within the blue family rather than shadows or borders. The two-step background stack (`rgb(165,219,255)` → `rgb(138,208,255)`) provides enough luminance contrast to define card boundaries. A single inset shadow adds tactile quality to surface elements. The overall effect is flat-with-texture rather than fully flat.

## 7. Do's and Don'ts

**Do:**
- Use `rgb(165,219,255)` as the page ground — it is the primary identity colour, not an accent.
- Pair Recia (serif) with Spline Sans Mono (monospace) as a deliberate editorial contrast.
- Apply negative letter-spacing (−0.8px to −0.85px) to all type roles.
- Keep text pure black (`rgb(0,0,0)`) — the blue ground handles atmosphere, not the text colour.
- Use `48px` radius on large containers and `14px` on small chips; don't mix arbitrary values.

**Don't:**
- Don't replace the sky-blue ground with white or off-white — the colour is the identity.
- Don't substitute a sans-serif for Spline Sans Mono in body text; the monospace texture is load-bearing.
- Don't add warm colours; the palette is blue-and-black only.
- Don't add heavy drop shadows; inset shadow is the extent of elevation language.
- Don't use medium/large type weights — the restrained weight (400/500) preserves the editorial calm.

## 8. Responsive Behavior

Framer's fine-grained breakpoint ladder (10 breakpoints) means the layout reflows at many intervals rather than at the standard three or four. Key transitions:
- Below `600px`: Single-column mobile; compact spacing.
- `810px+`: Wider grid; likely two-column case studies.
- `1200px+`: Full desktop canvas; maximum content width.

Light mode only — no dark mode observed.

## 9. Agent Prompt Guide

> "Design in the style of andreaskruszakin.com: sky-blue page background `rgb(165,219,255)`, card surface `rgb(138,208,255)`, pure black text `rgb(0,0,0)`. Recia serif for headings (weight 500, negative-tracked −0.8px); Spline Sans Mono for body text (17px, weight 400, negative-tracked −0.85px). Border-radius: 48px on large containers, 14px on small chips. No colour accents beyond the retro browser-blue `rgb(0,0,238)` for links. Depth via background colour steps, not shadows. Framer-generated responsive breakpoints at 600 / 810 / 1200px."

---

*Generated by Sparkbites — extracted from live CSS analysis*
