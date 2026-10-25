"""Shared layout: head, header, footer and reusable section partials.

Every page in the site is assembled from these pieces by build.py so the
chrome stays identical across all 15 pages.
"""

SITE_NAME = "HER Consulting LLC"
SITE_URL = "https://herconsultingbiz.com"
EMAIL = "lola@herconsultingbiz.com"
PHONE = "217-454-5192"
PHONE_HREF = "+12174545192"
ADDRESS = "Avon, IN 46123"
CERT = "An Indiana Certified Minority Business Enterprise"
PARTNERS_COPY = (
    "We proudly collaborate with a diverse range of clients and partners across "
    "multiple sectors, including education, healthcare, community development, and "
    "government, to drive strategic growth and achieve impactful results."
)

# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------
SERVICE_PAGES = [
    ("grant-readiness.html", "Getting Grant-Ready", "Training, advisory, coaching and technical assistance"),
    ("program-planning-management.html", "Program Planning &amp; Management", "Human-centred design and implementation science"),
    ("program-evaluation-impact.html", "Program Evaluation &amp; Impact", "Measuring, communicating and amplifying impact"),
    ("federal-contracting.html", "Federal Government Contracting", "NAICS-registered federal capabilities"),
    ("state-contracting.html", "State Government Contracting", "Registered UNSPSC codes for state work"),
    ("speaking-engagement.html", "Speaking Engagement Services", "Keynotes, panels, community talks and media"),
]

PORTFOLIO_PAGES = [
    ("portfolio-global.html", "Global Organizations", "Nigeria and the Democratic Republic of Congo"),
    ("portfolio-federal.html", "Federal Agencies", "CDC, NIH, NIMHD and NACDS Foundation"),
    ("portfolio-local.html", "Local Government Agencies", "Indiana Department of Health and FSSA"),
    ("portfolio-nonprofits.html", "Non-Profits", "CICOA Aging and In-Home Services, Direct Relief"),
]

ICONS = {
    "arrow": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h13M12 5l7 7-7 7"/></svg>',
    "chev": '<svg class="chev" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "check": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
    "badge": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.5-4.8 2.5.9-5.4L4.2 7.7l5.4-.8z"/></svg>',
    "mail": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2.5"/><path d="m2.5 6.5 9.5 6.5 9.5-6.5"/></svg>',
    "phone": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "pin": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "up": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
}

PARTNER_LOGOS = [
    ("partner-01.png", "Client and partner logo"),
    ("partner-02.png", "Client and partner logo"),
    ("partner-03.png", "Client and partner logo"),
    ("partner-04.avif", "NHANES"),
    ("partner-05.png", "Client and partner logo"),
    ("partner-06.png", "Client and partner logo"),
    ("partner-07.png", "Client and partner logo"),
    ("partner-08.png", "Client and partner logo"),
    ("partner-09.png", "Client and partner logo"),
    ("partner-10.jpg", "Client and partner logo"),
    ("partner-11.png", "Client and partner logo"),
    ("partner-12.png", "Client and partner logo"),
    ("partner-13.png", "Client and partner logo"),
    ("partner-14.webp", "Client and partner logo"),
    ("partner-15.png", "Client and partner logo"),
]

STATS = [
    (20, "Sponsored Projects"),
    (38, "Peer-review Journal articles"),
    (40, "Poster &amp; Podium Presentation"),
    (30, "Invited Speaking Engagements"),
]


# --------------------------------------------------------------------------
# Partials
# --------------------------------------------------------------------------
def header(active: str) -> str:
    """Site header. `active` is the top-level nav key for the current page."""

    def state(key: str) -> str:
        return ' aria-current="page"' if active == key else ""

    services_items = "".join(
        f'<li><a href="{href}"><strong>{label}</strong><span>{desc}</span></a></li>'
        for href, label, desc in SERVICE_PAGES
    )
    portfolio_items = "".join(
        f'<li><a href="{href}"><strong>{label}</strong><span>{desc}</span></a></li>'
        for href, label, desc in PORTFOLIO_PAGES
    )

    return f"""<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar">
  <div class="wrap topbar__inner">
    <p class="topbar__badge">{ICONS['badge']} {CERT}</p>
    <div class="topbar__links">
      <a href="mailto:{EMAIL}">{ICONS['mail']} {EMAIL}</a>
      <a href="tel:{PHONE_HREF}">{ICONS['phone']} {PHONE}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <nav class="wrap nav" aria-label="Primary">
    <a class="brand" href="index.html">
      <img src="assets/img/logo.png" alt="HER Consulting LLC" width="60" height="34">
      <span class="brand__text">
        <span class="brand__name">HER Consulting LLC</span>
        <span class="brand__tag">Public Health Consulting</span>
      </span>
    </a>

    <ul class="nav__menu" id="nav-menu">
      <li class="nav__item"><a class="nav__link" href="index.html"{state('home')}>Home</a></li>
      <li class="nav__item"><a class="nav__link" href="about.html"{state('about')}>About Us</a></li>
      <li class="nav__item nav__item--has-menu">
        <a class="nav__link" href="services.html"{state('services')}>Services {ICONS['chev']}</a>
        <ul class="dropdown">{services_items}</ul>
      </li>
      <li class="nav__item nav__item--has-menu">
        <a class="nav__link" href="portfolio.html"{state('portfolio')}>Portfolio {ICONS['chev']}</a>
        <ul class="dropdown">{portfolio_items}</ul>
      </li>
      <li class="nav__item"><a class="nav__link" href="contact.html"{state('contact')}>Contact Us</a></li>
    </ul>

    <div class="nav__cta">
      <a class="btn btn--sm" href="contact.html">Contact us {ICONS['arrow']}</a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>"""


def footer() -> str:
    service_links = "".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label, _ in SERVICE_PAGES
    )
    portfolio_links = "".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label, _ in PORTFOLIO_PAGES
    )

    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo.png" alt="HER Consulting LLC" width="74" height="42">
        <p>Public Health Awareness. Action. Impact. Partnering with organizations and individuals to strengthen Public Health Awareness, Access, and Action.</p>
        <span class="footer-badge">{ICONS['badge']} {CERT}</span>
      </div>

      <div>
        <h5>Services</h5>
        <ul class="footer-links">{service_links}</ul>
      </div>

      <div>
        <h5>Portfolio</h5>
        <ul class="footer-links">{portfolio_links}
          <li><a href="about.html">About Us</a></li>
        </ul>
      </div>

      <div>
        <h5>Get in touch</h5>
        <div class="footer-contact">
          <div>{ICONS['pin']} <span>{SITE_NAME}<br>{ADDRESS}</span></div>
          <a href="mailto:{EMAIL}">{ICONS['mail']} <span>{EMAIL}</span></a>
          <a href="tel:{PHONE_HREF}">{ICONS['phone']} <span>{PHONE}</span></a>
        </div>
        <a class="btn btn--sm" style="margin-top:1.4rem" href="contact.html">Start a conversation {ICONS['arrow']}</a>
      </div>
    </div>

    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> {SITE_NAME}. All rights reserved.</p>
      <nav aria-label="Footer">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Portfolio</a>
        <a href="contact.html">Contact Us</a>
      </nav>
    </div>
  </div>
</footer>

<button class="to-top" type="button" aria-label="Back to top">{ICONS['up']}</button>"""


def stats_section() -> str:
    cells = "".join(
        f"""<div class="stat reveal">
          <div class="stat__num"><span data-count="{value}">0</span>+</div>
          <h4>{label}</h4>
        </div>"""
        for value, label in STATS
    )
    return f"""<section class="section section--tight section--deep">
  <div class="wrap">
    <div class="stats">{cells}</div>
  </div>
</section>"""


def partners_section() -> str:
    logos = "".join(
        f'<img src="assets/img/{src}" alt="{alt}" loading="lazy">'
        for src, alt in PARTNER_LOGOS
    )
    return f"""<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Valued Clients and Partners</span>
      <h2>Valued Clients and Partners</h2>
      <p>{PARTNERS_COPY}</p>
    </div>
  </div>
  <div class="marquee reveal">
    <div class="marquee__track">{logos}</div>
  </div>
</section>"""


def cta_section(
    title: str = "We&rsquo;ve got you covered.",
    body: str = (
        "HER Consulting LLC continues to deliver tailored solutions that drive strategic "
        "growth and operational excellence for a diverse range of clients across multiple sectors."
    ),
    primary: tuple = ("about.html", "Learn more"),
    secondary: tuple = ("contact.html", "Contact us"),
) -> str:
    return f"""<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <span class="eyebrow" style="color:#7fd4ff">Under HER Leadership</span>
        <h2>{title}</h2>
        <p>{body}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--light" href="{primary[0]}">{primary[1]} {ICONS['arrow']}</a>
        <a class="btn btn--outline-light" href="{secondary[0]}">{secondary[1]}</a>
      </div>
    </div>
  </div>
</section>"""


# --------------------------------------------------------------------------
# Document shell
# --------------------------------------------------------------------------
DOCUMENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{site_url}/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site_name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{site_url}/assets/img/logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#06172a">
<link rel="icon" href="assets/img/logo.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.className+=" js";</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ProfessionalService","name":"HER Consulting LLC","description":"Public Health Awareness. Action. Impact.","url":"{site_url}","email":"{email}","telephone":"{phone}","address":{{"@type":"PostalAddress","addressLocality":"Avon","addressRegion":"IN","postalCode":"46123","addressCountry":"US"}},"founder":{{"@type":"Person","name":"Dr. Omolola (Lola) Olatunde"}}}}
</script>
</head>
<body>
{header}
<main id="main">
{body}
</main>
{footer}
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
