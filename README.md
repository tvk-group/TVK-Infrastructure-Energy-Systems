# TVK Infrastructure & Energy Systems LTD

Official corporate website for **TVK Infrastructure & Energy Systems LTD**.

## Run locally

```bash
npm install
npm run dev
```

Open http://localhost:3000 — redirects to `/en/`.

## Languages (25)

English, Deutsch, Français, Español, Italiano, Português, Nederlands, Polski, Русский, العربية, 中文, 日本語, 한국어, हिन्दी, Türkçe, Svenska, Norsk, Dansk, Suomi, Čeština, Română, Magyar, Ελληνικά, Bahasa Indonesia, Tiếng Việt

Use the **language dropdown** in the header. No Google Translate — all content is pre-translated.

## Deploy to Vercel (recommended)

The site builds as a **static export** to the `/out` folder. `vercel.json` is included.

### Option A — Vercel Dashboard (quick fix)

1. Open your project in [Vercel Dashboard](https://vercel.com)
2. Go to **Settings → General**
3. Set these values **exactly**:

| Setting | Value |
|---------|-------|
| Framework Preset | **Other** |
| Root Directory | *(leave empty)* |
| Build Command | `npm run build` |
| Output Directory | `out` |
| Install Command | `npm install` |

4. Go to **Deployments → Redeploy** the latest `main` commit
5. Visit your URL — it should redirect to `/en/`

### Option B — GitHub Actions (automatic)

Add these secrets to the repository (**Settings → Secrets → Actions**):

- `VERCEL_TOKEN` — from Vercel Account Settings → Tokens
- `VERCEL_ORG_ID` — from Vercel project settings
- `VERCEL_PROJECT_ID` — from Vercel project settings

Push to `main` — the workflow `.github/workflows/vercel.yml` deploys automatically.

### If you still see 404

The Vercel error `NOT_FOUND` means the deployment has **no files to serve**. This happens when:

- **Output Directory** is wrong (must be `out`, not empty or `.next`)
- You redeployed an **old commit** before the static export fix
- **Framework Preset** is Next.js but Output Directory is `out` (use **Other** instead)

**Fix:** Set Output Directory to `out`, Framework to **Other**, redeploy latest `main`.

## GitHub Pages

1. **Settings → Pages → Source:** Deploy from branch `gh-pages` / root
2. Live URL: https://tvk-group.github.io/TVK-Infrastructure-Energy-Systems/en/

## Build commands

```bash
npm run build        # Vercel / static hosting → outputs to /out
npm run build:pages  # GitHub Pages (with basePath)
```
