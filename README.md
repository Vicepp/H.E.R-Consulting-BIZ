# HER Consulting LLC — Website

A rebuild of [herconsultingbiz.com](https://herconsultingbiz.com/) as a modern,
fast, fully static site. **All copy is carried over verbatim from the original
site** (plus the Services page content supplied by the client); only the design,
structure, and code are new.

- 15 pages, none empty
- 53 images pulled from the original site and served locally
- No frameworks, no build step required to deploy — plain HTML/CSS/JS
- Responsive, keyboard-accessible, dark-section design system

---

## Run it locally

Any static server works. The simplest options:

```bash
# Option A — Node (recommended)
npm run dev            # serves the site at http://localhost:3001

# Option B — Python, no install needed
python -m http.server 3001
```

Then open <http://localhost:3001>.

You can also just double-click `index.html` — every internal link uses a real
`.html` filename, so the site works straight off the filesystem too.

---

## Deploy to Vercel

The repo is a zero-config static site. Either:

**From the dashboard** — import the repo at
[vercel.com/new](https://vercel.com/new). Leave *Framework Preset* as **Other**,
leave *Build Command* and *Output Directory* empty. Deploy.

**From the CLI**

```bash
npm i -g vercel
vercel          # preview deployment
vercel --prod   # production deployment
```

`vercel.json` already handles:

- long-lived caching for `/assets/*`
- security headers
- 301 redirects from every old WordPress URL (`/about-us`, `/our-portfolio`,
  `/federal-angencies`, `/non-profits`, `/federal-contracting-2`, …) to the new
  pages, so existing links and search rankings keep working

After the first deploy, point `herconsultingbiz.com` at Vercel under
**Project → Settings → Domains**.

---

## Editing content

Page content lives in Python data files and is compiled into the HTML. To change
copy:

1. Edit `_src/content.py` (all page copy) or `_src/layout.py` (header, footer,
   contact details, nav).
2. Run the build:

   ```bash
   npm run build          # or: python _src/build.py
   ```

3. Commit the regenerated `*.html` files.

Editing a generated `.html` file directly also works, but the change will be
overwritten the next time the build runs.

### Where things are

| Path | What it is |
| --- | --- |
| `index.html` … `contact.html` | Generated pages (committed, served by Vercel) |
| `assets/css/style.css` | The whole design system |
| `assets/js/main.js` | Nav, scroll reveals, counters, marquee, contact form |
| `assets/img/` | All 53 images from the original site |
| `_src/content.py` | Every piece of page copy |
| `_src/layout.py` | Header, footer, shared sections, `<head>` template |
| `_src/build.py` | Page assembly + `sitemap.xml` generation |
| `vercel.json` | Caching, headers, legacy URL redirects |

---

## Pages

| Page | File |
| --- | --- |
| Home | `index.html` |
| About Us | `about.html` |
| Services (01/02/03) | `services.html` |
| Getting Grant-Ready | `grant-readiness.html` |
| Program Planning & Management | `program-planning-management.html` |
| Program Evaluation & Impact | `program-evaluation-impact.html` |
| Federal Government Contracting | `federal-contracting.html` |
| State Government Contracting | `state-contracting.html` |
| Speaking Engagement Services | `speaking-engagement.html` |
| Portfolio (hub, all sectors) | `portfolio.html` |
| Portfolio — Global Organizations | `portfolio-global.html` |
| Portfolio — Federal Agencies | `portfolio-federal.html` |
| Portfolio — Local Government Agencies | `portfolio-local.html` |
| Portfolio — Non-Profits | `portfolio-nonprofits.html` |
| Contact Us | `contact.html` |

---

## Contact form

The form validates in the browser and then opens the visitor's email client with
the message pre-filled to `lola@herconsultingbiz.com`. There is no server
component, so nothing can break and there is nothing to maintain.

If you'd rather have submissions arrive as real emails without the visitor's mail
app opening, add a form backend later — a Vercel Serverless Function with Resend,
or a hosted service like Formspree — and point the form's `action` at it. The
markup is already set up for that.
