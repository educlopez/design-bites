# imgsrc.io — Design System

## 1. Visual Theme & Atmosphere

Imgsrc.io is a developer tool with the clarity and discipline of a well-designed documentation site. Its white canvas and near-black text establish an immediately functional tone — this is software infrastructure, and the design communicates reliability over personality. The use of **Geist Sans** (Vercel's own typeface) alongside a Next.js + Tailwind stack signals a product built within — and comfortable within — the modern Vercel ecosystem.

The atmosphere is clean, compact, and developer-confident. Nothing decorates for its own sake. Shadows are barely there. Borders are fine. The spacing is tight but never cramped. It feels like opening a well-structured terminal window or a tight component library — purposeful precision.

The design system is built on shadcn/ui conventions — the custom property naming (`--background`, `--foreground`, `--muted`, `--radius`) is the exact shadcn/ui token vocabulary, confirming this is a Radix/shadcn-based component system.

## 2. Color Palette & Roles

**Background / Canvas**
- `hsl(0 0% 100%)` / `rgb(255, 255, 255)` — Pure white canvas; `--background`
- `hsl(0 0% 96.1%)` / `rgb(245, 245, 245)` — Secondary/muted surface; `--secondary`, `--muted`, `--accent`
- `hsl(0 0% 89.8%)` / `rgb(229, 229, 229)` — Borders and inputs; `--border`, `--input`

**Text / Foreground**
- `hsl(0 0% 3.9%)` / `rgb(10, 10, 10)` — Near-black; `--foreground`, `--card-foreground`
- `hsl(0 0% 9%)` / `rgb(23, 23, 23)` — Primary interaction colour; `--primary`, button defaults, hover states
- `hsl(0 0% 45.1%)` / `rgb(115, 115, 115)` — Muted foreground; `--muted-foreground` — for captions, secondary labels

**Destructive**
- `hsl(0 84.2% 60.2%)` — Red; `--destructive` — standard error/danger token

**Ring / Focus**
- `hsl(0 0% 3.9%)` / `rgb(10, 10, 10)` — `--ring` — focus ring uses near-black, not the OS blue

**Absent:** No brand colour. No accent hue. The entire system is neutral greyscale — every token in the shadcn variable set maps to a shade between white and near-black.

## 3. Typography Rules

**Geist Sans** (`__GeistSans_3a0388`) is the sole typeface — Vercel's custom geometric sans-serif, designed for interface legibility. The fallback is `ui-sans-serif, system-ui, sans-serif`.

**Scale**
- H2: 14px / 500 weight / 20px line-height — unusually small for a heading; used for section labels or sidebar titles
- H3: 16px / 600 weight / 16px line-height / −0.4px tracking — tighter, more prominent item headings
- Body: 16px / 400 / 24px line-height
- Paragraphs: 14px / 400 / 20px line-height
- Buttons: 14px / 500 / 20px line-height
- Labels: 14px / 500 / 14px line-height (compressed, for form labels)
- Inputs: 14px / 400 / 20px line-height

**The heading size inversion is notable:** H2 (14px/500) is smaller than H3 (16px/600). This suggests H2 is used for metadata/section labels, while H3 is the primary content-level heading in the UI.

**No display type, no large hero headings detected.** The largest element is H3 at 16px — this is a UI-first site, not a marketing site. Content hierarchy is built through weight and colour, not size.

## 4. Component Stylings

**Buttons:**
- Default: white background, near-black border (`rgb(229,229,229)`), near-black text
- Hover: shifts to secondary surface `rgb(245,245,245)`, text darkens to `rgb(23,23,23)`
- Focus: outline removed; ring applied via `box-shadow: 0 0 0 1px rgb(10,10,10)`

**Inputs:**
- Transparent background, `--border` colour border
- Focus: ring applied as box-shadow `0 0 0 1px rgb(10,10,10)` — same as button focus
- Very subtle drop shadow: `rgba(0,0,0,0.05) 0px 1px 2px`

**Cards:** `div.rounded-xl` with white background. Radii use `--radius: 0.5rem` (8px) as base, with variants at 6px, 12px, and `9999px` for pill shapes.

**Shadows:** Two levels only:
- Micro: `rgba(0,0,0,0.05) 0px 1px 2px` — barely-there
- Subtle: `rgba(0,0,0,0.1) 0px 1px 3px, rgba(0,0,0,0.1) 0px 1px 2px -1px`

**Nav:** Transparent background, `rgb(229,229,229)` border — an underline or surrounding border that delineates the nav from page content.

## 5. Layout Principles

Main content area uses `24px 32px` padding (vertical / horizontal) — compact and consistent. Footer matches: `24px 32px`. This symmetry creates a contained, app-shell-like feel.

The layout is **application-style** — no hero, no marketing sections with generous padding. This is a tool UI. Content lives close to edges with precise internal spacing.

**Breakpoints:** 600px, 640px, 768px, 1024px, 1400px — five points, strongly matching Tailwind's default scale (sm: 640, md: 768, lg: 1024) plus a wide-desktop cut at 1400px. The 600px breakpoint adds a step between mobile and sm for medium phones.

## 6. Depth & Elevation

Depth is minimal by design. Only two shadow values exist:

1. `rgba(0,0,0,0.05) 0px 1px 2px` — barely perceptible card lift
2. `rgba(0,0,0,0.1) 0px 1px 3px + 0px 1px 2px -1px` — standard shadcn/ui `shadow-sm` equivalent

Focus states use ring-style box-shadow (`0 0 0 1px near-black`) rather than colour glow — clean and accessible.

The surface hierarchy is: white canvas → `rgb(245,245,245)` secondary → `rgb(229,229,229)` border. Three-step greyscale from canvas to border. Predictable and systematic.

## 7. Do's and Don'ts

**Do:**
- Use Geist Sans for all text — this typeface is load-optimised for Vercel/Next.js deployments.
- Follow the shadcn/ui CSS variable convention (`--background`, `--foreground`, `--muted`, etc.) for all tokens.
- Use `--radius: 0.5rem` (8px) as the base radius. Compound to 12px for cards.
- Apply focus rings as `box-shadow: 0 0 0 1px rgb(10,10,10)` — no OS-blue outline.
- Keep shadows to two levels: 1px micro and 3px subtle.
- Use compact 24px/32px padding for application containers.
- Use `rgb(229,229,229)` for all borders — consistent with `--border` token.

**Don't:**
- Add colour accents. The system is greyscale by design.
- Use large display headings — this is a UI-first system.
- Use `font-weight: 300` or `700` outside of very specific use cases.
- Add decorative shadows larger than 3px blur.
- Override the focus ring with browser default blue — the near-black ring is intentional.
- Break the 24/32px padding rhythm in the main application area.

## 8. Responsive Behavior

Five breakpoints map tightly to Tailwind defaults. The application shell at `24px 32px` padding likely reduces to `16px` or full-width at mobile. Navigation may collapse below 640px.

The 14–16px heading scale means no typographic rescaling is needed at mobile — headings are already compact enough for small screens. This is a notable advantage of UI-scale typography.

The 1400px breakpoint caps the wide-desktop layout — content is likely centered with a max-width container at this point.

## 9. Agent Prompt Guide

> Build in the style of imgsrc.io: white canvas, Geist Sans throughout (14–16px scale, weights 400/500/600 only). Use the full shadcn/ui CSS variable system — `--background: white`, `--foreground: hsl(0 0% 3.9%)`, `--border: hsl(0 0% 89.8%)`, `--radius: 0.5rem`. All surfaces are greyscale: white, `rgb(245,245,245)` secondary, `rgb(229,229,229)` border. Focus rings use `box-shadow: 0 0 0 1px rgb(10,10,10)`, not browser outline. Shadows: two levels, max 3px blur at 5–10% opacity. Application padding: `24px 32px` consistently. Breakpoints: 600, 640, 768, 1024, 1400px. This is a developer tool UI — compact, systematic, zero decoration.

---

*Generated by Sparkbites — extracted from live CSS analysis*
