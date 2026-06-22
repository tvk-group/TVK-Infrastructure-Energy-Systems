# TVK Infrastructure & Energy Systems LTD

Official corporate website for **TVK Infrastructure & Energy Systems LTD** — representing the infrastructure, energy, industrial systems and strategic technology investment activities of the TVK ecosystem.

## Overview

A professional corporate website built with Next.js, TypeScript, and Tailwind CSS. Designed to reflect the positioning of a serious infrastructure and energy company.

## Pages

- **Home** — Hero, core capability areas, development stage overview
- **About** — Mission, vision, long-term industrial strategy
- **Energy Systems** — Renewable energy, intelligence, monitoring, optimization
- **Infrastructure** — Smart, digital, and critical infrastructure technologies
- **Technology** — Industrial AI, analytics, monitoring, automation
- **Projects** — Development-stage project categories
- **Strategic Partnerships** — Collaboration and partnership inquiry
- **Insights** — Industry perspectives and research notes
- **Contact** — Partnership and inquiry form

## Development

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Languages

The site supports **25 languages** with ready-made translations (no Google Translate):

English, Deutsch, Français, Español, Italiano, Português, Nederlands, Polski, Русский, العربية, 中文, 日本語, 한국어, हिन्दी, Türkçe, Svenska, Norsk, Dansk, Suomi, Čeština, Română, Magyar, Ελληνικά, Bahasa Indonesia, Tiếng Việt

Use the language dropdown in the header to switch. URLs follow `/en/`, `/de/about`, etc.

## Deployment

### Vercel (recommended)

1. Connect the repository to [Vercel](https://vercel.com)
2. **Deploy the latest commit** on `main` or `cursor/tvk-corporate-website-ce49` (must be after the Vercel config split)
3. In Vercel **Project Settings → General**, confirm:
   - **Framework Preset:** Next.js
   - **Root Directory:** (empty / repository root)
   - **Output Directory:** (empty — do NOT set to `out`)
4. In **Environment Variables**, remove any of these if present:
   - `NEXT_PUBLIC_BASE_PATH`
   - `STATIC_EXPORT`
   - `GITHUB_PAGES`
5. **Do not "Redeploy" an old deployment** — push a new commit or redeploy the latest commit from the branch

`next.config.ts` is a clean standard Next.js config. GitHub Pages uses a separate `next.config.pages.ts`.

### GitHub Pages

The site also deploys to the `gh-pages` branch on every push to `main`.

**Live URL:** [https://tvk-group.github.io/TVK-Infrastructure-Energy-Systems/](https://tvk-group.github.io/TVK-Infrastructure-Energy-Systems/)

Enable once at **Settings → Pages → Deploy from branch → `gh-pages` / root**.

## Build

```bash
npm run build
npm start
```

## Design System

- **Colors:** White, Steel Gray, Industrial Silver, Deep Navy, Energy Blue, Subtle Green
- **Typography:** IBM Plex Sans (headings), Source Sans 3 (body)
- **Style:** Corporate, industrial, engineering-focused
