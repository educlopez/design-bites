# Pacôme Pertant — Design System Reference

## 1. Visual Theme & Atmosphere

Pacôme Pertant's portfolio opens with a choice — "enter with sound" or "enter without sound" — before you see a single piece of work, and that gate sets the tone for everything after it. This is a motion & sound designer's site built as an experience, not a brochure. The canvas is near-black (`#0a0a0a`), the type is near-white (`#fafafa`), and the single accent — a toxic, screen-glow green (`#21ffc0`) — is held in reserve like a signal light rather than spent on decoration. A single variable typeface, "Indivisible Variable," runs the entire system at wildly different scales: 19px body copy sits beside 80px display links with -4px tracking, so the same face reads as both quiet prose and a poster headline. Marquee-style repeats ("showreel • 2025 • showreel • 2025…") and huge single-word nav links ("spiral," "list") turn navigation itself into kinetic content. Built in Nuxt, the whole thing is engineered for cinema-first immersion over information density.

---

## 2. Color Palette & Roles

**Foundation**
- `#0a0a0a` — page canvas / body background (`--color-black`, `--color-bg-dark`)
- `#fafafa` — primary text, borders, inverted surfaces (`--color-white`)
- `#171717` — secondary near-black surface, one step lighter than the canvas (`--color-bg-grey`)
- `#e6e6e6` — muted light-gray surface (`--color-grey`)

**Accent**
- `#21ffc0` — the one hue in the system (`--color-pop-green`), a neon signal color held back for a single moment of contrast rather than spread across chrome

**Alpha scrims (black, layered)**
- `#0a0a0a20`, `#0a0a0a40`, `#0a0a0a60`, `#0a0a0a00` — a graduated black-alpha ramp (`--color-bg-dark20/40/60/-transparent`) built for overlays, scrims, and transition curtains rather than flat panels

**Alpha white**
- `#fafafa20` — a soft 20%-opacity white (`--color-white20`), likely a hairline border or ghosted UI element on the dark canvas

**Surfaces (measured luminance)**
- `rgb(250, 250, 250)` on `div.subwrapper` — luminance `.98`, a near-white gate panel (almost certainly the sound-on/sound-off entry screen)
- `rgb(10, 10, 10)` on `div.loader` — luminance `.039`, a near-black loading curtain matching the body

There's a quiet inversion trick in the extracted data: the default `a` selector carries near-black text/border (`rgb(10, 10, 10)`) even though the page body is near-black-on-near-white-text. That only makes sense sitting on the light `.98`-luminance subwrapper — meaning links flip from light-on-dark (in the main dark experience) to dark-on-light the moment they land on the gate panel. The palette isn't a fixed dark theme; it's context-inverted per surface.

---

## 3. Typography Rules

Everything runs on one variable face:

**Typeface:** `"Indivisible Variable"`, falling back to `"Helvetica Neue", "Arial", sans-serif` — declared once for both `--main-font` and `--display-font`, so body copy and hero type are literally the same font file at different axis settings, not a paired system.

**Scale**

| Role | Size | Weight | Line-height | Tracking |
|------|------|--------|-------------|----------|
| Body | 19px | 400 | 19px | -0.76px |
| Paragraph | 24px | 500 | 24px | -0.76px |
| Link (display) | 80px | 500 | 80px | -4px |
| Button | 18px | 500 | 18px | -0.76px |

**Principles**
- Line-height always equals font-size (1:1, no leading) — every text role sits tight to its own box, which reads as intentional and typographically confident rather than cramped, because it's consistent at every scale.
- Tracking compresses as size grows: -0.76px at 19–24px, jumping to -4px at 80px. The bigger the type gets, the harder it's pulled in — the huge display links (nav items, marquee words) feel stenciled rather than stretched.
- Weight is the only lever between body (400) and everything interactive — paragraphs, links, buttons (500). There's no third weight, no italic, no text-transform (`none` throughout) — hierarchy comes from size and weight, never from case.
- One face used at 19px and at 80px without ever swapping families is a deliberate flex of the variable font — it's the same argument ToyFight makes with face-switching, run in reverse: one face, infinite range.

---

## 4. Component Stylings

**Nav / secondary links**
- Transparent background, `#fafafa` text, no border — light-on-dark, no hover captured, focus/motion likely carries the feedback instead

**Display links (the "spiral" / "list" / showreel-scale elements)**
- 80px Indivisible Variable, weight 500, -4px tracking — these aren't captions, they're the primary interactive surface of the homepage
- Flip to dark text (`#0a0a0a`) when sitting on the light `.98`-luminance gate panel

**Buttons**
- 18px, weight 500, -0.76px tracking — same typographic DNA as paragraphs, just smaller and tighter to a button box

**Border radius**
- On-page radii actually used: `100px`, `50px`, `24px`, `20px`, `50%` — large pills and full circles (avatar/toggle-scale elements)
- This diverges from the declared radius token scale (`--radius-xs` 4px → `--radius-full` 9999px, stepping 4/8/12/16/20) — the tokens read like a fuller design-system spec than what's shipped; the UI itself commits to big pills and circles, skipping the small 4–16px increments entirely

**Grid & rhythm tokens**
- `--grid-margin: 30px`, `--grid-gutter: 16px`, column formula derived from both
- Gap scale: `--gap-xs` 10 → `--gap-s` 15 → `--gap-m` 30 → `--gap-l` 60 → `--gap-xl` 90 → `--gap-xxl` 120 → `--gap-xxxl` 180, plus one-off `--gap-20` and `--gap-45`
- The scale roughly doubles at each step (10→15→30→60→90→120→180), giving section spacing a strong, deliberate jump rather than a fine-grained ramp

**Motion primitives**
- `--ease-spring` — a custom spring curve authored as a `linear()` easing function (not a simple cubic-bezier), signaling hand-tuned bounce
- `--ease-quad-in-out: cubic-bezier(.455,.03,.515,.955)`
- `--ease-expo-out: cubic-bezier(.19,1,.22,1)`
- Three named eases for three different jobs (springy, symmetric, decelerating) is a strong signal this site treats transitions as a first-class part of the brand, consistent with a sound/motion designer's showcase

**Shadows**
- None detected. Depth never comes from drop-shadow here.

---

## 5. Layout Principles

- Viewport-locked custom properties (`--vw: 100vw`, `--vh: 100vh`, `--ivh: 100dvh`) point to full-bleed, edge-to-edge hero and video sections — exactly what a showreel-led portfolio needs.
- `body` and `main` are reset to zero margin/padding; `main` carries a flat `20px` gap — all real spacing is delegated to the gap/grid token scale, not ad hoc CSS.
- Breakpoints sit at **420 / 900 / 1024 / 1400** — a hand-picked set, not framework defaults (420 instead of the usual 480, 900 instead of 768), suggesting the layout was tuned against real content (the 80px display links) rather than generic device buckets.
- Built on Nuxt (Vue) — consistent with the hashed asset filenames and the CSS custom-property-heavy, design-token-driven approach.

---

## 6. Depth & Elevation

There is no shadow system here — `shadows: []` across the whole extraction. Depth is communicated two other ways:

- **Luminance swap** — the near-black canvas (`.039`) and the near-white gate surface (`.98`) sit at opposite ends of the scale with nothing in between; when one replaces the other (loader → subwrapper), it reads as a hard cut, not a soft lift.
- **Alpha-black scrims** — the `20/40/60%` black ramp exists specifically to darken/overlay content in transitions (video scrims, curtain reveals) rather than to create card-style elevation.

Depth here is temporal (transition curtains, easing curves) far more than spatial (shadow, blur).

---

## 7. Do's and Don'ts

**Do**
- Anchor the canvas at `#0a0a0a` with `#fafafa` text — never pure black/white.
- Spend `#21ffc0` sparingly, as a single signal accent — not as a secondary UI color.
- Run body and display type off the same variable face; shift weight (400→500) and size, not family.
- Compress tracking as size increases — keep small text near -0.76px and let display type pull in toward -4px.
- Use big pill (`50px`/`100px`) or full-circle (`50%`) radii on interactive chrome; skip small increments.
- Reserve the near-white `.98`-luminance surface for gate/overlay moments (sound on/off, loaders) — it's a mode switch, not a card background.
- Drive transitions with named custom eases (spring / quad-in-out / expo-out) instead of default browser easing.

**Don't**
- Don't add a second accent hue — the green is singular.
- Don't reach for box-shadow for elevation — this system has none; use luminance and alpha-black scrims instead.
- Don't use small border radii (4–20px) on primary UI — the shipped interface skips straight to pills and circles.
- Don't apply text-transform — every role in the extracted data is `none`; case changes aren't part of this system's hierarchy vocabulary.
- Don't treat the dark theme as fixed — links and text invert to dark-on-light the moment they sit on a light surface (the gate panel). Design components to flip, not to assume one background forever.

---

## 8. Responsive Behavior

Breakpoints at **420, 900, 1024, 1400** are custom-tuned rather than framework-default, which tracks with a site whose hero content is 80px display type — the layout has to make hard calls earlier (420 vs. the common 480) to keep that type from breaking awkwardly on small phones. The `--ivh: 100dvh` custom property (alongside plain `100vh`) signals deliberate handling of mobile viewport quirks (address-bar resize) for the full-bleed video/hero sections. Expect the huge display links and marquee text to scale down in size before they ever wrap or lose their negative tracking — the compression is part of the voice at every breakpoint.

---

## 9. Agent Prompt Guide

> Build a UI that matches Pacôme Pertant's design language.

Set the canvas to near-black `#0a0a0a` with near-white `#fafafa` text — never pure black or pure white. Run everything off a single variable typeface at 400 weight for body/paragraph copy and 500 weight for links, buttons, and display type; keep line-height equal to font-size at every scale. Compress letter-spacing as size increases: -0.76px at 18–24px, pulling to -4px at 80px+ for hero-scale display links. Spend the neon accent `#21ffc0` once, deliberately — as a signal, never as chrome. Skip small border-radius values entirely; commit to large pills (`50px`, `100px`) or full circles (`50%`) on interactive elements. Build depth through luminance jumps (a `.039` dark surface vs. a `.98` light gate surface) and layered black-alpha scrims (`20/40/60%`), not box-shadow — there is none in this system. Animate transitions with custom eases — a hand-authored spring curve, a symmetric quad-in-out, and a decelerating expo-out — rather than default CSS easing. Let full-bleed, viewport-locked (`100dvh`) hero/video sections carry the visual weight, and treat navigation itself as kinetic, oversized display type rather than a small utility bar.

---

*Generated by Sparkbites — extracted from live CSS analysis*
