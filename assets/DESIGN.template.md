# Crisp Workspace Design System

This project should feel like a polished workspace application: focused, quiet, modern, and slightly editorial. Use a near-white page, translucent panels, compact sticky navigation, restrained Burgundy accents, and clean text hierarchy.

The goal is not a landing page and not a plain admin template. The interface should feel like a well-made professional tool that is pleasant to keep open for a long time.

## 1. Product Feel

The default mood is:

- crisp
- spacious
- lightweight
- readable
- softly premium
- task-first

The UI should help users scan, create, compare, and review without visual fatigue. Use restraint, but avoid washed-out notebook styling. Surfaces should be clean and bright, with just enough translucency, depth, and typographic care to feel designed.

## 2. Color System

Prefer a near-white neutral system with one dark text color and one small-area accent.

### Core Tokens

- Page: `#fcfcfb`
- Page Alt: `#f7f7f5`
- Surface: `rgba(255, 255, 255, 0.62)`
- Surface Strong: `rgba(255, 255, 255, 0.82)`
- Surface Muted: `rgba(255, 255, 255, 0.5)`
- Text: `#171413`
- Text Soft: `rgba(23, 20, 19, 0.76)`
- Text Muted: `rgba(23, 20, 19, 0.56)`
- Border: `rgba(18, 18, 18, 0.12)`
- Border Soft: `rgba(18, 18, 18, 0.08)`
- Border Faint: `rgba(18, 18, 18, 0.05)`
- Accent: `#7a1f32`
- Accent Ring: `rgba(122, 31, 50, 0.18)`
- Focus: `rgba(122, 31, 50, 0.36)`
- Shadow Soft: `0 10px 30px rgba(29, 21, 19, 0.045)`

### Usage Rules

- Use `#fcfcfb` or a very subtle white-to-page gradient for the app background.
- Use Burgundy only for active states, focus rings, links, small badges, and tiny data highlights.
- Do not use the accent as a large hero fill or full-width band.
- Avoid saturated multi-color palettes. If status colors are needed, keep them muted and secondary to the main system.
- Avoid stark black, pure gray admin chrome, beige-heavy themes, and purple-blue gradient identities.

## 3. Typography

### Fonts

- UI: `Inter, Segoe UI, Helvetica, Arial, sans-serif`
- Optional editorial display: `Libre Baskerville, Georgia, serif`
- Code: `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`

Use sans-serif for nearly all UI. Serif is optional for occasional empty states, markdown content, or editorial headings, but never for dense controls.

### Scale

| Role | Size | Weight | Line Height | Notes |
| --- | --- | --- | --- | --- |
| App/Page Title | 30px-34px | 600 | 1.18 | Use once per view |
| Section Title | 20px-22px | 600 | 1.3 | Main panel headings |
| Card Title | 16px-18px | 600 | 1.35 | Repeated content blocks |
| Body | 14px-16px | 400 | 1.65-1.85 | Default copy |
| Label/Meta | 12px-13px | 500 | 1.45 | Secondary details |
| Eyebrow | 11px-12px | 500 | 1.4 | Uppercase, letter spacing about `0.14em` |

Rules:

- Keep page titles compact and confident, not oversized.
- Use `tracking-tight` lightly for large headings only.
- Do not scale font size with viewport width.
- Text in buttons, pills, tabs, and cards must fit at mobile widths.

## 4. Layout

The app should open directly into useful workspace content.

- Use a sticky top header with a translucent page-colored background and light bottom border.
- Keep navigation compact, text-led, and easy to scan.
- Prefer a generous max width for workspace pages: about `1440px` to `1760px`.
- Use page padding around `16px` mobile, `24px-32px` tablet, `40px` desktop.
- Prefer practical one-column or two-column layouts over decorative hero compositions.
- Use section dividers and whitespace before adding more cards.
- Avoid cards inside cards unless there is a real repeated item or modal-like frame.

Recommended page frame:

- Top sticky header: brand/project label, short description, compact nav or actions.
- Page intro strip: eyebrow, title, one concise description, optional meta/action area.
- Main content: grid or stacked panels with clear task areas.

## 5. Surfaces And Depth

Use subtle glass-like surfaces sparingly. The effect should feel clean, not flashy.

### Panels

- Standard radius: `12px`
- Smaller tiles: `10px`
- Pills: `999px`
- Border: `1px solid var(--border)` or softer
- Background: `var(--surface-strong)` or `var(--surface)`
- Backdrop filter: `blur(12px-16px) saturate(128%-135%)`
- Shadow: `var(--shadow-soft)` only on primary panels

### When To Use Containers

Use containers for:

- forms
- data summaries
- repeated records
- markdown/evaluation results
- modal-like task areas

Avoid containers for:

- every page section
- simple navigation groups
- text that can be grouped by spacing alone

## 6. Components

Prefer shadcn-vue primitives and local shared components. Keep custom raw HTML styling small and token-based.

### Buttons

- Primary: dark text color as fill, white text, rounded pill, medium height.
- Outline: strong surface background, faint border, accent text or border on hover.
- Ghost: transparent background, muted text, accent on hover.
- Use lucide icons in icon buttons when an icon exists.
- Do not use large colored call-to-action blocks.

### Inputs

- Radius around `10px`.
- Background `var(--surface-strong)`.
- Border `var(--border)`.
- Focus ring with `var(--accent-ring)`.
- Placeholder uses muted text.
- Textareas may resize vertically.

### Cards And Tiles

- Use a `panel-hover` style for interactive panels: `translateY(-1px)`, slight border/accent shift, and brighter background.
- Metrics can use smaller translucent tiles with faint borders.
- Empty states should use dashed or faint borders, not heavy illustration.

### Markdown / Rich Text

- Keep line height generous, around `1.85-1.95`.
- Use compact serif headings only if the content is editorial or report-like.
- Code blocks should use soft neutral backgrounds and small radii.
- Blockquotes may use a thin Burgundy left border.

## 7. Motion

Motion should clarify navigation and state changes.

Recommended:

- Route transitions: fade plus `4px-8px` vertical movement, about `180ms-240ms`.
- Entry animation: fade plus `12px-16px` upward movement, about `280ms-320ms`.
- Hover: background, border, or `translateY(-1px)`.

Avoid:

- scale-heavy hover effects
- parallax
- looping decorative animation
- blur-heavy transitions

## 8. shadcn-vue Token Guidance

When using shadcn-vue, map the design system into CSS variables instead of styling every component separately.

Preferred light theme direction:

- `--background`: near white, aligned with `#fcfcfb`
- `--foreground`: near `#171413`
- `--card`: translucent or near white
- `--primary`: near `#171413`
- `--primary-foreground`: white
- `--accent`: very light neutral surface
- `--accent-foreground`: near `#171413`
- `--ring`: Burgundy-tinted focus
- `--border`: faint warm neutral
- `--radius`: around `0.625rem` to `0.75rem`

Keep component variants close to shadcn-vue defaults, but tune surfaces, borders, radii, and focus rings to match this document.

## 9. Do And Do Not

Do:

- Make the first screen useful immediately.
- Use bright neutral surfaces with subtle translucency.
- Keep controls compact and polished.
- Use one accent color consistently.
- Let spacing, alignment, and small typography shifts create hierarchy.
- Check mobile layouts for text wrapping and control overflow.

Do not:

- Recreate a beige notebook look.
- Build marketing heroes for tool screens.
- Use oversized type as the main design gesture.
- Add decorative gradient blobs, bokeh, or ornamental backgrounds.
- Put cards inside cards by default.
- Use multiple competing accent colors.
- Make the UI feel like a generic gray admin dashboard.

## 10. Agent Prompt Guide

Quick style reference:

- "Use a crisp near-white workspace UI with translucent panels."
- "Keep the layout task-first, compact, and polished."
- "Use Burgundy only as a small-area accent."
- "Prefer shadcn-vue primitives with tuned design tokens."
- "Avoid copying old beige guidance."

Iteration guide:

1. Start with a clean layout and useful content hierarchy.
2. Add surfaces only where grouping needs help.
3. Tune type and spacing before adding decoration.
4. Use accent only for interaction and focus.
5. Verify desktop and mobile for readable density, no overlap, and no clipped text.
