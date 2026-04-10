<p align="center">
  <a href="https://sparkbites.dev">
    <img src="https://sparkbites.dev/opengraph-image.jpg" alt="Sparkbites — Web Design Inspiration Directory" width="100%" />
  </a>
</p>

<h1 align="center">design-bites</h1>

<p align="center">
  <strong>Design systems decoded for AI agents.</strong><br />
  Curated <code>DESIGN.md</code> files auto-extracted from the world's best-designed websites.
</p>

<p align="center">
  <a href="https://sparkbites.dev">Website</a> &bull;
  <a href="#available-design-systems">Browse files</a> &bull;
  <a href="#how-to-use">Get started</a> &bull;
  <a href="https://x.com/educalvolpz">Twitter</a>
</p>

---

## What is DESIGN.md?

A `DESIGN.md` file encodes a website's **complete visual language** in plain markdown so AI agents can generate consistent, on-brand UI — no Figma exports, no JSON tokens, no special tooling.

Introduced by [Google Stitch](https://stitch.withgoogle.com), it follows the same convention as `AGENTS.md`:

| File | Read by | Defines |
|------|---------|---------|
| `AGENTS.md` | Coding agents | How to **build** the project |
| `DESIGN.md` | Design agents | How the project should **look** |

> *"Tell your AI agent to follow the DESIGN.md and watch it nail the visual language on the first try."*

---

## How to use

**1. Pick a design system** from the [table below](#available-design-systems).

**2. Copy the file** into your project root:

```bash
# Download directly
curl -o DESIGN.md https://raw.githubusercontent.com/educlopez/design-bites/main/design-mds/linear.app/DESIGN.md
```

**3. Tell your AI agent to use it:**

```
Use DESIGN.md as the design reference for this UI task.
```

Works with **Claude**, **Cursor**, **GitHub Copilot**, **Google Stitch**, and any AI tool that reads project files.

---

## Available design systems

| Website | Category | Preview |
|---------|----------|---------|
| [**Linear**](https://linear.app) | Developer Tools | [`DESIGN.md`](./design-mds/linear.app/DESIGN.md) |
| [**Stripe**](https://stripe.com) | Fintech | [`DESIGN.md`](./design-mds/stripe.com/DESIGN.md) |
| [**Vercel**](https://vercel.com) | Developer Tools | [`DESIGN.md`](./design-mds/vercel.com/DESIGN.md) |

> More coming soon. [Request a website](https://github.com/educlopez/design-bites/issues/new?title=Request:+website-name.com&labels=request) by opening an issue.

---

## What's inside each file

Every `DESIGN.md` follows a **9-section standard format**:

```
1. Visual Theme & Atmosphere    — the design philosophy and mood
2. Color Palette & Roles        — every color with its semantic purpose
3. Typography Rules             — font stacks, scale, OpenType features
4. Component Stylings           — buttons, cards, inputs + hover/focus states
5. Layout Principles            — spacing, grid, whitespace philosophy
6. Depth & Elevation            — shadow system and surface hierarchy
7. Do's and Don'ts              — design guardrails and anti-patterns
8. Responsive Behavior          — breakpoints and collapsing strategy
9. Agent Prompt Guide           — ready-to-paste prompts for AI agents
```

### Example: Linear's typography section

```markdown
## 3. Typography Rules

Inter Variable is the sole typeface, deployed at weight 510 — a value between
regular (400) and medium (500), made possible only by variable font technology.
This is the signature choice: emphasis that registers subconsciously without
ever shouting. OpenType features cv01 and ss03 are active globally, replacing
Inter's default character forms with alternate glyphs that sharpen the geometric
precision of the letterforms.

| Element | Size  | Weight | Line Height | Letter Spacing | Features      |
|---------|-------|--------|-------------|----------------|---------------|
| h1      | 64px  | 510    | 64px (1.0)  | -1.408px       | "cv01","ss03" |
| h2      | 40px  | 510    | 44px (1.1)  | -0.88px        | "cv01","ss03" |
| body    | 16px  | 400    | 24px (1.5)  | normal         | "cv01","ss03" |
```

---

## How these are generated

Unlike hand-curated alternatives, design-bites are **auto-extracted from live websites** using a two-step pipeline:

### Step 1 — CSS Extraction (Playwright)

A headless browser navigates each website and extracts:

- Computed styles for 14+ element types (h1-h6, body, p, a, button, input, code...)
- CSS custom properties (design tokens)
- Color palette with deduplication and noise filtering
- Font families, weights, OpenType features (`font-feature-settings`)
- Box shadows, border radii, spacing scale
- Media query breakpoints
- Surface/background hierarchy sorted by luminance
- **Interactive states** — hover and focus captured via real mouse/keyboard simulation
- Runtime tech stack detection (Next.js, Nuxt, Astro, Svelte, Tailwind, GSAP...)

### Step 2 — AI Analysis (Claude)

The raw CSS data is interpreted to produce the narrative layer:

- Design philosophy and visual mood
- Semantic color roles (why this blue, not just which blue)
- Typographic principles (why weight 510, not just that it's 510)
- Component patterns and interaction design rationale
- Actionable do's and don'ts
- Ready-to-use prompts for AI agents

**Every value comes from the actual CSS.** The narrative explains *why* — that's what separates a useful DESIGN.md from a raw data dump.

---

## About

**design-bites** is powered by [Sparkbites](https://sparkbites.dev) — a curated directory of inspiring websites for designers and developers. We analyze each site's typography, color palettes, tech stacks, and design patterns.

design-bites extends that analysis into a format AI agents can consume directly.

---

## Contributing

Want to add a website? [Open an issue](https://github.com/educlopez/design-bites/issues/new?title=Request:+website-name.com&labels=request) with the URL and we'll generate it.

Found an error in a DESIGN.md? PRs are welcome.

## License

MIT
