# hims.com — Design System

## 1. Visual Theme & Atmosphere

Hims.com presents itself as a modern telehealth brand built entirely on trust and accessibility. The site's visual identity is deliberately restrained — almost aggressively utilitarian — relying on the browser's native system-ui typeface stack and near-zero decorative elements. This is not minimalism as aesthetic; it is minimalism as medical-grade clarity. No custom fonts, no branded colour palette, no shadows. The design language says: *we are not here to impress you, we are here to serve you.*

The result is clinical in the best sense. Content hierarchy is established entirely through font-weight and size relationships. The lack of visual flourish places full attention on the health information and calls to action.

## 2. Color Palette & Roles

**Text**
- `rgb(49, 49, 49)` — Body text; dark charcoal, not pure black — softer on screen for long-form reading

**Backgrounds**
- Transparent (`rgba(0,0,0,0)`) — Body background; the site uses the browser default white canvas
- No custom surface colours detected — zero branded backgrounds

**Interactive**
- `rgb(0, 0, 238)` — Links and anchor borders; pure browser-default blue — a deliberate accessibility-first choice that prioritises recognisability over brand

**Absent:** No brand colour — no signature green, blue, or teal that many telehealth brands adopt. No dark mode. No gradient. The palette is effectively monochrome.

## 3. Typography Rules

Hims uses the **system-ui** font stack (`system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif`). This is the most universal possible choice — every user sees their OS's default sans-serif. On macOS, San Francisco. On Windows, Segoe UI. On Android, Roboto.

**Scale**
- H1: 40px / 600 weight / 50px line-height — compact, confident hero sizing
- H2: 24px / 600 weight / 30px line-height — clear section headers
- Body: 16px / 400 / 18.4px line-height — tight line-height, prioritises density
- Paragraphs: 16px / 400 / 24px line-height — slightly more open than base body
- Links: 12px / 400 — smaller than body text in nav/footer contexts
- Code: `monospace` 12px — fallback for any inline code references

**Note:** No letter-spacing, no text-transform, no OpenType feature settings. Pure default rendering.

**Absence of custom fonts** is the defining typographic statement. This site prioritises loading speed and accessibility above visual differentiation.

## 4. Component Stylings

**Links:** Browser-default blue with underline behaviour. Hover states are not captured — interactive feedback likely handled by Angular component state.

**Inputs:** Transparent background, black border and text. No custom border-radius detected. Bare and functional.

**No shadows detected.** Zero box-shadow values across the entire extracted stylesheet.

**No border radii detected.** All elements use default (0px or browser default) corner treatments.

**Forms:** Minimal styling — Angular's component-scoped CSS handles the detail. The base layer is intentionally blank.

**Navigation and Footer:** No custom surface treatments. Content simply sits on the white canvas.

## 5. Layout Principles

Built with **Angular**, the site relies on component-scoped styles for layout. The single detected breakpoint is 350px — an unusually low value suggesting the layout is fundamentally a single-column mobile-first structure, with desktop simply being a wider version of the same column flow.

No spacing tokens detected at the body or section level beyond zero-margin reset. All spatial rhythm is delegated to Angular component styles. The baseline is extremely clean — a blank canvas with content responsibility pushed to each component.

## 6. Depth & Elevation

There is no elevation system. No shadows, no layered surfaces, no translucency. This is a flat design in the most literal sense — every element exists on the same visual plane.

This choice, combined with the system font and browser-default colours, creates a design that feels less like a branded experience and more like structured HTML. Whether intentional or pragmatic, it signals to users: *the content is the interface.*

## 7. Do's and Don'ts

**Do:**
- Use system-ui for all text — do not override with a custom font.
- Set body text at `rgb(49, 49, 49)` — avoid pure black for readability.
- Use browser-default link blue for all links — accessibility and convention over brand.
- Keep components flat — no shadows, no gradients, no decorative borders.
- Let Angular component styles own layout and spacing.
- Prioritise loading performance — every byte saved is intentional.

**Don't:**
- Add decorative colour surfaces or hero gradients.
- Use custom border radii on form elements or cards.
- Override link colour with brand colour — the blue is intentional.
- Add elevation layers — this design is deliberately depth-free.
- Use `font-weight: 300` or `700` except for specific bold headlines.

## 8. Responsive Behavior

The single breakpoint at 350px is the minimum threshold — below this, the layout makes extreme-small-screen adjustments. Above 350px, everything scales linearly within the single-column flow. There is no multi-column grid, no responsive typography scaling detected at the base CSS level.

Angular's component architecture handles the real responsive complexity internally. The base stylesheet is intentionally sparse.

## 9. Agent Prompt Guide

> Build a healthcare-grade interface in the style of hims.com: white canvas, no custom font — use `system-ui` / `-apple-system` stack. Body text is dark charcoal `rgb(49,49,49)`, not black. Links use browser-default blue. No shadows, no rounded corners, no decorative colour. H1 at 40px/600, H2 at 24px/600, body at 16px/400. Everything is flat and legible. The design philosophy: clarity and trust over brand identity. Component-level styles own spacing and layout — keep the base stylesheet a blank canvas. Mobile-first with a minimum breakpoint at 350px.

---

*Generated by Sparkbites — extracted from live CSS analysis*
