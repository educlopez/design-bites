# Linear Design System

## 1. Visual Theme & Atmosphere

Linear treats darkness as its native medium — not as a "dark mode" toggled on, but as the foundational canvas upon which every element is deliberately placed. The body background at `rgb(8, 9, 10)` is not quite black; it carries the faintest warmth of near-black charcoal, allowing the layered surfaces above it — `rgb(9, 10, 11)`, `rgb(15, 16, 17)`, `rgb(18, 19, 20)` — to emerge through single-digit luminance increments. This is darkness as architecture: depth is communicated not through dramatic shadows but through almost imperceptible shifts in surface brightness, like rooms lit by distant starlight.

The typographic system reveals Linear's engineering ethos with unusual precision. Inter Variable is the sole typeface, but it is deployed at weight 510 — a value that exists between regular (400) and medium (500), made possible only by variable font technology. This is not an accident or a rounding error. Weight 510 is the signature choice: it creates emphasis that registers subconsciously without ever shouting, a typographic whisper louder than a bold. For subheadings, 590 occupies a similar in-between space — heavier than medium, lighter than semibold — producing a hierarchy that feels calibrated rather than stepped. OpenType features `cv01` and `ss03` are active globally, replacing Inter's default character forms with alternate glyphs that sharpen the geometric precision of the letterforms. Even the monospace choice — Berkeley Mono over the expected SF Mono — signals an aesthetic preference for crafted tools.

The color philosophy is almost entirely achromatic. White text appears at varying opacities — `rgb(247, 248, 248)` for primary content, `rgb(208, 214, 224)` for secondary, `rgb(138, 143, 152)` for tertiary — creating a hierarchy through transparency rather than distinct hue shifts. The single accent, `rgb(94, 106, 210)`, is a muted indigo that reads as calm authority rather than urgent action. Borders drawn in `rgba(255, 255, 255, 0.08)` are barely visible — moonlight on glass — present enough to define boundaries without competing for attention. This is a design system that values information density managed through restraint: every pixel of contrast is earned.

---

## 2. Color Palette & Roles

### Background Surfaces

Linear's depth system is built on a remarkably narrow luminance range. The entire surface hierarchy lives between luminance 0 and 0.089 — a span so compressed that each layer whispers its elevation rather than declaring it.

| Token | Value | RGB | Luminance | Role |
|---|---|---|---|---|
| Surface/Void | `rgb(0, 0, 0)` | 0, 0, 0 | 0.000 | Absolute black — page separator shadows |
| Surface/Base | `rgb(8, 9, 10)` | 8, 9, 10 | 0.035 | Page canvas — the void from which all content emerges |
| Surface/Frame | `rgb(9, 10, 11)` | 9, 10, 11 | 0.038 | Primary frame container, barely distinguishable from base |
| Surface/Card | `rgb(15, 16, 17)` | 15, 16, 17 | 0.062 | Carousel cards, benefit panels — lifted content |
| Surface/FrameBg | `rgb(16, 17, 18)` | 16, 17, 18 | 0.066 | Frame background layer |
| Surface/View | `rgb(18, 19, 20)` | 18, 19, 20 | 0.074 | Active view container |
| Surface/Chat | `rgb(22, 23, 24)` | 22, 23, 24 | 0.089 | Chat/input boxes — the highest elevation in the dark stack |
| Surface/Divider | `rgb(35, 37, 42)` | 35, 37, 42 | 0.145 | Navigation dividers, structural separators |
| Surface/Overlay | `rgba(255, 255, 255, 0.01)` | — | ~0.01 | Ghost overlay — note panels, barely-there containers |
| Surface/Code | `rgba(255, 255, 255, 0.05)` | — | — | Code block background, using white opacity for subtle lift |

### Text Hierarchy

Linear builds its text hierarchy through careful modulation of near-white values, creating a reading experience where importance is felt before it is consciously parsed.

| Token | Value | Hex | Role |
|---|---|---|---|
| Text/Primary | `rgb(247, 248, 248)` | `#F7F8F8` | Headlines, primary content — near-white with the faintest cool cast |
| Text/Secondary | `rgb(208, 214, 224)` | `#D0D6E0` | Subheadings, descriptions — a blue-grey that recedes gracefully |
| Text/Tertiary | `rgb(138, 143, 152)` | `#8A8F98` | Buttons, metadata, auxiliary text — deliberate dimness |
| Text/Inverse | `rgb(8, 9, 10)` | `#08090A` | Dark text on light surfaces (blockquote contexts) |
| Text/OnAccent | `rgb(255, 255, 255)` | `#FFFFFF` | Pure white reserved exclusively for text on accent-colored backgrounds |

### Brand & Accent

| Token | Value | Hex | Role |
|---|---|---|---|
| Accent/Primary | `rgb(94, 106, 210)` | `#5E6AD2` | Links, CTAs, pulse dots — Linear's signature muted indigo |
| Accent/Mention | `rgb(109, 120, 213)` | `#6D78D5` | @mentions in chat — slightly lighter indigo variant |
| Accent/MentionBg | `rgb(35, 37, 52)` | `#232534` | Mention chip background — indigo-tinted dark surface |
| Accent/Pulse | `rgba(94, 106, 210, 0.15)` | — | Hero pulse dot — accent at 15% opacity for ambient glow |

### Status & Label Colors

Linear uses a curated set of status colors that remain vivid against the dark canvas without becoming garish — each chosen to be instantly distinguishable at small sizes.

| Token | Value | Hex | Role |
|---|---|---|---|
| Status/Red | `rgb(235, 87, 87)` | `#EB5757` | Bug, urgent — warm red with enough orange to avoid alarm |
| Status/Violet | `rgb(139, 92, 246)` | `#8B5CF6` | Feature, enhancement — rich purple |
| Status/Indigo | `rgb(99, 102, 241)` | `#6366F1` | In-progress, tracking — close to brand accent |
| Status/Green | `rgb(16, 185, 129)` | `#10B981` | Complete, healthy — emerald with teal undertone |
| Status/Cyan | `rgb(6, 182, 212)` | `#06B6D4` | Informational, monitoring — cool cyan |

### Data Visualization

| Token | Value | Hex | Role |
|---|---|---|---|
| Chart/Top | `rgb(85, 204, 255)` | `#55CCFF` | Upper bar in monitor charts — bright sky blue |
| Chart/Bottom | `rgb(2, 184, 204)` | `#02B8CC` | Lower bar — darker teal complement |
| Chart/Initiative/Teal | `rgb(15, 51, 56)` | `#0F3338` | Initiative icon background — deep teal |
| Chart/Initiative/Red | `rgb(66, 34, 34)` | `#422222` | Initiative icon background — deep red |

### Contextual Highlights

| Token | Value | Hex | Role |
|---|---|---|---|
| Highlight/Yellow | `rgb(228, 242, 34)` | `#E4F222` | Customer quote cards — electric yellow for visual punch |
| Highlight/Blue | `rgb(28, 133, 232)` | `#1C85E8` | Customer quote cards — vivid blue counterpart |

### Border System

| Token | Value | Role |
|---|---|---|
| Border/Subtle | `rgba(255, 255, 255, 0.08)` | Primary border — moonlight on glass, used for header bottom, code blocks, textarea |
| Border/Input | `rgba(255, 255, 255, 0.02)` | Textarea background doubles as a near-invisible input container |

---

## 3. Typography Rules

### Font Stacks

| Context | Stack | Philosophy |
|---|---|---|
| UI / Prose | `"Inter Variable", "SF Pro Display", -apple-system, "system-ui", "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif` | Inter Variable first for fine-grained weight control; SF Pro Display as Apple fallback — note the "Display" optical size variant chosen for its superior rendering at larger text |
| Code | `"Berkeley Mono", ui-monospace, "SF Mono", Menlo, monospace` | Berkeley Mono is a premium choice — a monospace designed for beauty rather than just function, signaling that code is a first-class citizen in Linear's world |

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|
| h1 | 64px | 510 | 64px (1.0) | -1.408px | Hero headlines — tight leading creates monumental presence; aggressive negative tracking condenses the display size |
| h2 | 40px | 510 | 44px (1.1) | -0.88px | Section titles — proportional tracking tightens with scale |
| blockquote | 24px | 400 | 31.92px (1.33) | -0.288px | Pull quotes — regular weight at larger size for a calm, editorial voice |
| h3 | 20px | 590 | 26.6px (1.33) | -0.24px | Feature headings — weight steps up to 590 as size decreases, compensating for reduced visual mass |
| h4 | 16px | 590 | 24px (1.5) | normal | Card titles — same weight as h3 but at body size with relaxed leading |
| body | 16px | 400 | 24px (1.5) | normal | Base text — generous line height for readability in dense interfaces |
| p | 15px | 400 | 24px (1.6) | -0.165px | Paragraph text — subtly smaller than body, reducing visual noise in long-form content |
| a | 14px | 510 | 21px (1.5) | normal | Navigation links — the 510 weight makes links feel interactive without underlines |
| button | 13px | 400 | 19.5px (1.5) | normal | Button labels — deliberately light weight; buttons rely on context, not typographic weight, for affordance |
| label | 16px | 400 | 24px (1.5) | normal | Form labels — matched to body for visual consistency |
| input | 16px | 400 | normal | normal | Input text — 16px avoids iOS zoom on focus |
| textarea | 13.33px | 400 | normal | normal | Textarea — compact for multi-line input contexts |
| code | 12.25px | 400 | 15.925px (1.3) | -0.182px | Inline code — tighter leading keeps code blocks compact |
| pre | 14px | 400 | 24px (1.714) | normal | Code blocks — generous leading for readability in longer snippets |

### Typographic Principles

**The 510/590 System**: Linear uses only two non-standard weights — 510 and 590 — both occupying the gaps between conventional weight stops. This is a signature move: 510 (between regular and medium) creates emphasis that feels earned rather than demanded, while 590 (between medium and semibold) provides hierarchy without the bluntness of 600. The result is a type system that whispers its structure.

**Negative Tracking as Scale Increases**: Letter spacing tightens progressively with size — from `normal` at 16px to `-0.88px` at 40px to `-1.408px` at 64px. This optical compensation prevents large text from appearing loose and scattered, maintaining the dense, engineered aesthetic at every scale.

**OpenType Features**: `cv01` (character variant 01) and `ss03` (stylistic set 03) are enabled globally across all non-code text. In Inter, `cv01` provides alternate glyph forms for improved geometric consistency, while `ss03` adjusts specific characters for better readability in UI contexts. These features are deliberately omitted from code and input elements, where standard character recognition matters more than aesthetic refinement.

**The 15px Paragraph**: Body text is 16px but paragraphs are 15px — a 1px reduction that may seem trivial but creates a subtle visual distinction between structural text (labels, headings) and flowing content, reducing the overall density perception without sacrificing readability.

---

## 4. Component Stylings

### Border Radius Scale

Linear's radius system is minimal and purposeful — no `12px` or `16px` "card" radii. Everything feels engineered, not decorated.

| Token | Value | Usage |
|---|---|---|
| Radius/Micro | 2px | Inline code, tight UI elements — barely rounded |
| Radius/Small | 4px | Default interactive elements, chips |
| Radius/Base | 5px | Slightly larger containers |
| Radius/Medium | 6px | Primary buttons, input fields |
| Radius/Large | 8px | Cards, dialog panels |
| Radius/Circle | 50% | Avatars, status dots |
| Radius/Pill | 9999px | Tags, badges, full-round elements |

### Button Patterns

Buttons in Linear are defined by restraint. The default button uses a transparent background with `rgb(138, 143, 152)` text — essentially a ghost button by default, elevating content over chrome.

| Variant | Background | Text Color | Border | Radius |
|---|---|---|---|---|
| Ghost (Default) | `transparent` | `rgb(138, 143, 152)` | None | 6px |
| Primary CTA | `rgb(94, 106, 210)` | `rgb(255, 255, 255)` | None | 6px |
| Code/Inline | `rgba(255, 255, 255, 0.05)` | `rgb(208, 214, 224)` | `rgba(255, 255, 255, 0.08)` | 2px |

### Input & Textarea

| Property | Value | Notes |
|---|---|---|
| Background | `rgba(255, 255, 255, 0.02)` | Nearly invisible — inputs emerge from context, not from decoration |
| Border | `rgba(255, 255, 255, 0.08)` | The same moonlight border used throughout |
| Text | `rgb(208, 214, 224)` | Secondary text color — inputs do not compete with headings |
| Font Size | 16px (input) / 13.33px (textarea) | Input at 16px prevents iOS zoom; textarea is compact |

### Card / Container Patterns

| Component | Background | Border | Radius |
|---|---|---|---|
| Benefit Card | `rgb(15, 16, 17)` | — | 8px |
| Frame Container | `rgb(16, 17, 18)` | — | — |
| Chat Box | `rgb(22, 23, 24)` | — | — |
| Note Panel | `rgba(255, 255, 255, 0.01)` | — | — |
| Code Block | `rgba(255, 255, 255, 0.05)` | `rgba(255, 255, 255, 0.08)` | 2px |

---

## 5. Layout Principles

### Spacing System

Linear's spacing data reveals an interface built on zero-padding structural elements — the body, sections, header, and footer all carry `0px` padding and margin. This is characteristic of a CSS-in-JS architecture where spacing is applied at the component level rather than through global structural rules.

| Element | Padding | Margin | Gap | Insight |
|---|---|---|---|---|
| body | 0px | 0px | — | Clean slate — all spacing delegated to components |
| main | 72px 0px 0px | 0px | — | Top offset for sticky header (~72px header height) |
| section | 0px | 0px | — | Sections are compositional shells, not spacing containers |
| header | 0px | 0px | — | Header manages its own internal spacing |
| footer | 0px | 0px | — | Footer is self-contained |

### Grid & Density Philosophy

The absence of gap values in structural elements, combined with the compressed luminance hierarchy (surfaces differing by 1-3 RGB values), reveals a layout strategy centered on **visual proximity through surface color** rather than whitespace. Elements belong together because they share a surface, not because they are spaced apart. This enables the information-dense interfaces Linear is known for — project boards, issue lists, and timelines where every pixel carries meaning.

### Structural Observations

- **72px header offset**: A fixed top navigation creates predictable content positioning
- **No CSS custom properties detected**: Linear's empty `customProperties` object confirms a CSS-in-JS approach — design tokens live in JavaScript, not in the cascade. This keeps the design system programmatic and type-safe
- **Next.js detected**: The framework choice aligns with their performance-first philosophy — server rendering keeps initial paint fast despite the dense UI

---

## 6. Depth & Elevation

### Shadow System

Linear's approach to depth is defined by what it does not do. There are no sprawling, colorful box-shadows. Every shadow is pure black at low opacity — depth without drama.

| Level | Value | Semantic Name | Usage |
|---|---|---|---|
| Hairline | `rgba(0, 0, 0, 0.03) 0px 1.2px 0px 0px` | Hairline | Subtle bottom-edge definition — a 1.2px shadow at 3% opacity creates the barest suggestion of separation, like a pencil line |
| Ring | `rgba(0, 0, 0, 0.33) 0px 0px 0px 1px` | Ring | A 1px spread-only shadow functioning as a border — no blur, no offset. At 33% opacity against the dark canvas, this creates contained elements without the brittleness of actual borders |
| Elevated | `rgba(0, 0, 0, 0) 0px 8px 2px, rgba(0, 0, 0, 0.01) 0px 5px 2px, rgba(0, 0, 0, 0.04) 0px 3px 2px, rgba(0, 0, 0, 0.07) 0px 1px 1px, rgba(0, 0, 0, 0.08) 0px 0px 1px` | Layered Elevation | Five-layer composite shadow — each layer progressively stronger from 0% to 8%, building depth through accumulation rather than a single dramatic cast. The result is photorealistic but understated |
| Press | `rgba(0, 0, 0, 0.4) 0px 1px 0px 0px` | Press | A single 1px bottom shadow at 40% — the darkest shadow in the system. Used for pressed or inset states, giving tactile feedback |

### Depth Philosophy

On a near-black canvas, traditional shadows (which darken their surroundings) are nearly invisible. Linear solves this in two ways: (1) the **ring shadow** technique, using `0px 0px 0px 1px` spread to create hairline borders that respond to background color, and (2) **multi-layer composite shadows** that accumulate subtle opacity rather than relying on a single dramatic blur. The five-layer elevated shadow is particularly notable — its top layer is literally 0% opacity, a mathematical ghost, while the lower layers build just enough perceived depth for dropdowns and overlays. This is shadow engineering, not shadow decoration.

---

## 7. Do's and Don'ts

### Do

- **Use the 510/590 weight pair** for emphasis hierarchy — these in-between weights are Linear's signature. Regular (400) for body, 510 for emphasis, 590 for strong emphasis.
- **Build surface depth through 1-3 RGB value increments** — the difference between `rgb(8, 9, 10)` and `rgb(15, 16, 17)` is the entire elevation model. Subtlety is the strategy.
- **Apply `rgba(255, 255, 255, 0.08)` borders** as your universal separator — this single value handles header borders, code blocks, and input fields. Consistency through constraint.
- **Use ring shadows (`0 0 0 1px`) for contained elements** rather than CSS borders — they render more consistently at sub-pixel levels and blend with the dark canvas.
- **Enable `cv01` and `ss03` OpenType features** on all UI text — these character variants are integral to Linear's typographic identity. Omit them only for code and input elements.
- **Let the 15px/16px body split work for you** — structural UI at 16px, flowing content at 15px. The distinction is felt, not seen.
- **Tighten letter-spacing proportionally as size increases** — `-0.24px` at 20px, `-0.88px` at 40px, `-1.408px` at 64px. Large text must earn its density.

### Don't

- **Don't use saturated accent colors** — Linear's indigo (`#5E6AD2`) is deliberately muted. Bright blue or purple would feel juvenile against the achromatic system.
- **Don't add border-radius above 8px** for rectangular elements — the scale tops at 8px for cards. No `12px`, no `16px`, no "friendly" pill shapes on containers.
- **Don't use white text at full opacity for body content** — even primary text is `rgb(247, 248, 248)`, not `rgb(255, 255, 255)`. Pure white is reserved exclusively for text on accent backgrounds.
- **Don't apply shadows with colored tints** — every shadow in the system is pure `rgba(0, 0, 0, ...)`. Colored shadows would break the achromatic depth model.
- **Don't use weight 600 (semibold) or 700 (bold)** — the heaviest weight in the entire system is 590. Bold text has no place in Linear's restrained hierarchy.
- **Don't put spacing on structural elements** — sections, headers, and footers carry zero padding. Spacing is a component concern, not a structural one.
- **Don't mix border techniques** — choose either `rgba(255, 255, 255, 0.08)` CSS borders or `rgba(0, 0, 0, 0.33) 0 0 0 1px` ring shadows, not both on the same element.

---

## 8. Responsive Behavior

### Breakpoints

| Breakpoint | Width | Strategy |
|---|---|---|
| Mobile | 600px | Compact layout — stacked content, touch-friendly targets |
| Small | 640px | Minor layout adjustments |
| Tablet | 768px | Two-column layouts begin |
| Desktop | 1024px | Full sidebar + content panels |
| Wide | 1280px | Maximum content width, expanded feature showcases |

### Responsive Philosophy

Linear's breakpoint system reveals a **mobile-aware but desktop-first** approach. The dense, information-rich interfaces that define the product naturally expand to fill wider viewports, while collapsing to simplified, stacked layouts on mobile. The 600px breakpoint — notably not 576px or 480px — suggests custom mobile targeting rather than adherence to a framework's defaults.

### Touch & Interaction Considerations

- **16px input font size** prevents iOS auto-zoom on focus — a deliberate mobile accommodation
- **Button text at 13px with 19.5px line height** creates compact touch targets that still meet minimum sizing requirements
- **72px header offset** accommodates both desktop navigation and mobile fixed headers
- **No `gap` values on structural elements** means responsive spacing is handled entirely through component-level logic, allowing fine-grained control at each breakpoint

---

## 9. Agent Prompt Guide

### Quick Reference

| Property | Value |
|---|---|
| Background | `rgb(8, 9, 10)` |
| Primary Text | `rgb(247, 248, 248)` |
| Secondary Text | `rgb(208, 214, 224)` |
| Muted Text | `rgb(138, 143, 152)` |
| Accent | `rgb(94, 106, 210)` |
| Border | `rgba(255, 255, 255, 0.08)` |
| Font Family | `"Inter Variable"` |
| Monospace | `"Berkeley Mono"` |
| Body Weight | `400` |
| Emphasis Weight | `510` |
| Strong Weight | `590` |
| Body Size | `16px / 24px` |
| Primary Radius | `6px` |
| Card Radius | `8px` |
| Ring Shadow | `rgba(0, 0, 0, 0.33) 0 0 0 1px` |
| OpenType Features | `"cv01", "ss03"` |

### Example Prompts

**Prompt 1 — Hero Section**
> Build a hero section in the style of Linear. Use a `rgb(8, 9, 10)` background. The headline should be Inter Variable at 64px, weight 510, line-height 1.0, letter-spacing -1.408px, color `rgb(247, 248, 248)`, with OpenType features `cv01` and `ss03` enabled via `font-feature-settings: "cv01", "ss03"`. Below it, a subtitle at 20px weight 590 in `rgb(208, 214, 224)` with -0.24px letter-spacing. Add a primary CTA button with `rgb(94, 106, 210)` background, white text, 6px border-radius, and no border. The overall feel should be dark, precise, and information-dense — contrast achieved through typography weight, not color.

**Prompt 2 — Card Grid**
> Create a grid of feature cards on a `rgb(8, 9, 10)` page background. Each card should use `rgb(15, 16, 17)` background with 8px border-radius — no visible border, depth comes from the 7-point RGB difference between card and canvas. Card titles in Inter Variable at 16px weight 590, `rgb(247, 248, 248)`. Body text at 15px weight 400, `rgb(208, 214, 224)`, letter-spacing -0.165px. Use the five-layer composite shadow for hover elevation: `rgba(0,0,0,0) 0px 8px 2px, rgba(0,0,0,0.01) 0px 5px 2px, rgba(0,0,0,0.04) 0px 3px 2px, rgba(0,0,0,0.07) 0px 1px 1px, rgba(0,0,0,0.08) 0px 0px 1px`.

**Prompt 3 — Navigation Header**
> Build a fixed navigation header with transparent background. Use a bottom border of `rgba(255, 255, 255, 0.08)` — one pixel of moonlight — to separate it from content. Navigation links in Inter Variable at 14px weight 510, `rgb(138, 143, 152)`, transitioning to `rgb(247, 248, 248)` on hover. Include a nav divider element at `rgb(35, 37, 42)`. The overall header height should be approximately 72px, matching Linear's main content top padding offset.

**Prompt 4 — Issue/Task List**
> Design an issue list interface on `rgb(18, 19, 20)` (view surface). Each row uses the ring shadow technique — `rgba(0, 0, 0, 0.33) 0 0 0 1px` — instead of CSS borders, creating contained rows that blend with the dark canvas. Issue titles at 14px weight 510, `rgb(247, 248, 248)`. Metadata in `rgb(138, 143, 152)` at 13px. Status dots use the label color palette: red `#EB5757`, violet `#8B5CF6`, indigo `#6366F1`, green `#10B981`, cyan `#06B6D4` — each at 50% border-radius. The chat input area at the bottom should use `rgb(22, 23, 24)` — the highest elevated dark surface.

**Prompt 5 — Code Block**
> Render a code block using Berkeley Mono at 12.25px, weight 400, line-height 1.3, letter-spacing -0.182px, color `rgb(208, 214, 224)`. Background is `rgba(255, 255, 255, 0.05)` with a `rgba(255, 255, 255, 0.08)` border and 2px border-radius. For larger code blocks (pre), increase to 14px with 24px line-height. Do NOT enable OpenType features cv01/ss03 on code elements — these are reserved for the Inter Variable UI face only.

---

*Generated by Sparkbites — extracted from live CSS analysis*
