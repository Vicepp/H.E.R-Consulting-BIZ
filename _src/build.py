"""Static site generator for HER Consulting LLC.

Run:  python _src/build.py
Writes the finished .html files into the project root, where Vercel serves
them as a zero-config static site.
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content as C  # noqa: E402
import layout as L  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I = L.ICONS


# ==========================================================================
# Small helpers
# ==========================================================================
def crumbs(*trail) -> str:
    """trail = (label, href) pairs; the last item is the current page."""
    parts = []
    for idx, (label, href) in enumerate(trail):
        if href and idx < len(trail) - 1:
            parts.append(f'<a href="{href}">{label}</a><span>/</span>')
        else:
            parts.append(f"<span>{label}</span>")
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def page_hero(eyebrow, title, body="", trail=None, actions="", extra="") -> str:
    return f"""<section class="page-hero">
  <div class="wrap">
    {crumbs(*trail) if trail else ""}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    {f"<p>{body}</p>" if body else ""}
    {actions}
    {extra}
  </div>
</section>"""


def ticks(items) -> str:
    return '<ul class="ticks">' + "".join(
        f"<li>{I['check']}<span>{item}</span></li>" for item in items
    ) + "</ul>"


def feature_cards(pillars) -> str:
    out = []
    for idx, (title, points) in enumerate(pillars, start=1):
        out.append(f"""<article class="feature reveal">
      <span class="feature__badge">{idx:02d}</span>
      <h3>{title}</h3>
      {ticks(points)}
    </article>""")
    return '<div class="grid grid--2">' + "".join(out) + "</div>"


def service_cards() -> str:
    out = []
    for s in C.SERVICES:
        out.append(f"""<article class="card reveal">
      <span class="card__icon"><img src="assets/img/{s['icon']}" alt="" loading="lazy" width="34" height="34"></span>
      <h3>{s['title']}</h3>
      <p>{s['copy']}</p>
      <a class="textlink" href="{s['href']}">Learn More {I['arrow']}</a>
    </article>""")
    return '<div class="grid grid--3 service-stack">' + "".join(out) + "</div>"


def category_nav(active=None) -> str:
    out = []
    for href, label, icon, key in C.PORTFOLIO_CATEGORIES:
        count = len(C.PORTFOLIO_PROJECTS[key])
        cur = ' aria-current="page"' if key == active else ""
        out.append(f"""<a class="cat reveal" href="{href}"{cur}>
      <img src="assets/img/{icon}" alt="" loading="lazy" width="42" height="42">
      <b>{label}</b>
      <span>{count} project{"s" if count != 1 else ""}</span>
    </a>""")
    return '<div class="cats">' + "".join(out) + "</div>"


def project_cards(key, numbered=True) -> str:
    label = next(l for _, l, _, k in C.PORTFOLIO_CATEGORIES if k == key)
    green = key in ("local", "nonprofits")
    out = []
    for idx, (title, client, body) in enumerate(C.PORTFOLIO_PROJECTS[key], start=1):
        num = f'<span class="card__num">{idx:02d}</span>' if numbered else ""
        out.append(f"""<article class="project reveal">
      <span class="project__tag{' project__tag--green' if green else ''}">{label}</span>
      {num}
      <h3>{title}</h3>
      <p class="project__client">{client}</p>
      <p>{body}</p>
    </article>""")
    return '<div class="projects">' + "".join(out) + "</div>"


def similar_projects_cta() -> str:
    return f"""<section class="section section--tight">
  <div class="wrap center reveal">
    <h2 style="font-size:clamp(1.4rem,1.1rem+1.4vw,2rem)">You have similar projects?</h2>
    <div class="btn-row" style="justify-content:center;margin-top:1.5rem">
      <a class="btn" href="contact.html">Contact Us {I['arrow']}</a>
    </div>
  </div>
</section>"""


def portfolio_intro_section() -> str:
    return f"""<section class="section section--tight">
  <div class="wrap">
    <div class="split split--narrow-media">
      <div class="reveal">
        <span class="eyebrow">{C.PORTFOLIO_INTRO_TITLE}</span>
        <h2>{C.PORTFOLIO_INTRO_LEAD}</h2>
        <p class="lede" style="margin-top:1.1rem">{C.PORTFOLIO_INTRO_BODY}</p>
      </div>
      <div class="split__media split__media--blob reveal">
        <img src="assets/img/illus-project-complete.png" alt="Illustration of a completed project" loading="lazy">
      </div>
    </div>
  </div>
</section>"""


# ==========================================================================
# Pages
# ==========================================================================
def home() -> str:
    points = "".join(f"<li>{I['check']}<span>{p}</span></li>" for p in C.MISSION_POINTS)

    highlights = "".join(
        f"""<article class="project reveal">
      <span class="card__num">{idx:02d}</span>
      <h3>{title}</h3>
      <p>{body}</p>
      <a class="textlink" style="margin-top:1.2rem" href="{href}">View portfolio {I['arrow']}</a>
    </article>"""
        for idx, (title, body, href) in enumerate(C.HIGHLIGHTS, start=1)
    )

    return f"""<section class="hero">
  <div class="wrap hero__inner">
    <div>
      <div class="hero__chip">
        <img src="assets/img/mbe-badge.jpg" alt="" loading="lazy" width="40" height="40">
        <span>
          <b>Certified MBE</b>
          <span>State of Indiana</span>
        </span>
      </div>
      <span class="eyebrow">Home Of The</span>
      <h1>Public Health Awareness. <span class="accent">Action. Impact.</span></h1>
      <p class="hero__sub"><strong>at HER Consulting LLC</strong><br>{C.MISSION}</p>
      <ul class="hero__points">{points}</ul>
      <span class="hero__kicker"><b>MBE</b> {L.CERT}</span>
      <div class="btn-row">
        <a class="btn" href="services.html">Learn More {I['arrow']}</a>
        <a class="btn btn--outline-light" href="contact.html">Contact us</a>
      </div>
    </div>

    <div class="hero__media">
      <div class="hero__frame">
        <img src="assets/img/hero-a.png" alt="Community members joining hands in a circle" width="746" height="516">
      </div>
      <div class="hero__frame hero__frame--float">
        <img src="assets/img/hero-b.png" alt="A diverse group of people smiling together" width="864" height="580" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Our Services</span>
      <h2>We Help in&hellip;</h2>
    </div>
    {service_cards()}
  </div>
</section>

{L.stats_section()}

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Portfolio</span>
      <h2>Project Highlights</h2>
    </div>
    <div class="projects">{highlights}</div>
    <div class="btn-row reveal" style="justify-content:center;margin-top:clamp(2rem,4vw,3rem)">
      <a class="btn" href="portfolio.html">Learn more {I['arrow']}</a>
    </div>
  </div>
</section>

{L.cta_section()}
{L.partners_section()}"""


def about() -> str:
    background = "".join(f"<p>{p}</p>" for p in C.COMPANY_BACKGROUND)

    awards = "".join(
        f"""<div class="award reveal">
      <img class="award__icon" src="assets/img/award.png" alt="" loading="lazy" width="40" height="40">
      <div>
        <b>{title}</b>
        <span>{org}</span>
      </div>
    </div>"""
        for title, org in C.AWARDS
    )

    team = "".join(
        f"""<article class="member reveal">
      <div class="member__photo"><img src="assets/img/{img}" alt="{name}" loading="lazy"></div>
      <div class="member__body">
        <span class="member__name">{name}</span>
        <span class="member__role">{role}</span>
        <p class="member__bio" data-expert-bio>{bio}</p>
      </div>
    </article>"""
        for img, name, role, bio in C.TEAM
    )

    quotes = "".join(
        f"""<figure class="quote reveal">
      <span class="quote__mark" aria-hidden="true">&ldquo;</span>
      <blockquote><p>{body}</p></blockquote>
      <footer>
        <cite>{who}</cite>
        <small>{org}</small>
      </footer>
    </figure>"""
        for body, who, org in C.TESTIMONIALS
    )

    return f"""{page_hero(
        "about us",
        "About Us",
        C.TAGLINE + " " + C.MISSION,
        trail=[("Home", "index.html"), ("About Us", None)],
        actions=f'<div class="btn-row"><a class="btn" href="services.html">Our services {I["arrow"]}</a><a class="btn btn--outline-light" href="portfolio.html">See the portfolio</a></div>',
    )}

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="stack reveal">
        <span class="eyebrow">Company Background</span>
        {background}
      </div>
      <div class="split__media split__media--blob reveal">
        <img src="assets/img/illus-multitasking.png" alt="Illustration of a consultant managing multiple projects" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split split--reverse">
      <div class="stack reveal">
        <span class="eyebrow">Our Founder and Owner</span>
        <h2>Our Founder<br>and Owner</h2>
        <p>{C.FOUNDER_BIO}</p>
        <div class="btn-row" style="padding-top:0.6rem">
          <a class="btn" href="speaking-engagement.html">Book a speaking engagement {I['arrow']}</a>
        </div>
      </div>
      <div class="split__media split__media--framed reveal">
        <img src="assets/img/dr-olatunde.png" alt="Dr. Omolola (Lola) Olatunde" loading="lazy">
        <img src="assets/img/mbe-badge.jpg" alt="Indiana Certified Minority Business Enterprise digital badge"
             loading="lazy" style="width:112px;position:absolute;right:-10px;bottom:-22px;border-radius:16px;box-shadow:var(--shadow-lg)">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">why we're the best</span>
      <h2>Awards</h2>
      <p><em>{C.AWARDS_INTRO}</em></p>
    </div>
    <div class="awards">{awards}</div>
  </div>
</section>

<section class="section section--tint team-section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">why we're the best</span>
      <h2>Subject Matter Experts</h2>
      <p>{C.SME_INTRO}</p>
    </div>
    <div class="team">{team}</div>
  </div>
</section>

{L.stats_section()}
{L.cta_section()}

<section class="section section--deep">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Testimonials</span>
      <h2>Client Testimonials</h2>
    </div>
    <div class="quotes">{quotes}</div>
  </div>
</section>

{L.partners_section()}"""


def services() -> str:
    """Services page — the 01 / 02 / 03 structure of HER CONSULTING SERVICES."""

    # Jump list across the top
    jump = '<div class="cats">' + "".join(
        f"""<a class="cat reveal" href="#service-{s['num']}">
      <img src="assets/img/{s['icon']}" alt="" loading="lazy" width="42" height="42">
      <b><span style="color:var(--blue)">{s['num']}</span> &nbsp;{s['title']}</b>
      <span>{len(s['blocks'])} focus areas</span>
    </a>"""
        for s in C.SERVICES_PAGE
    ) + "</div>"

    sections = []
    for idx, s in enumerate(C.SERVICES_PAGE):
        blocks = "".join(
            f"""<article class="feature reveal">
        <h3>{title}</h3>
        {f'<p style="margin-bottom:1.15rem">{sub}</p>' if sub else ""}
        {ticks(items)}
      </article>"""
            for title, sub, items in s["blocks"]
        )

        tagline = f'<p class="lede" style="margin-top:1rem">{s["tagline"]}</p>' if s["tagline"] else ""
        header = (
            f'<p style="margin-top:1rem;font-family:var(--font-display);font-weight:600;'
            f'letter-spacing:0.02em;color:var(--ink)">{s["header"]}</p>'
            if s["header"] else ""
        )

        sections.append(f"""<section class="section{' section--tint' if idx % 2 else ''}" id="service-{s['num']}">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:820px">
      <span class="eyebrow">HER Consulting Services</span>
      <div style="display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap">
        <span style="font-family:var(--font-display);font-size:clamp(2.4rem,2rem+2vw,3.4rem);font-weight:700;line-height:1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent">{s['num']}</span>
        <h2 style="margin:0">{s['title']}</h2>
      </div>
      {tagline}
      {header}
      <div class="btn-row" style="margin-top:1.8rem">
        <a class="btn btn--ghost" href="{s['href']}">Full details {I['arrow']}</a>
      </div>
    </div>
    <div class="grid grid--2">{blocks}</div>
  </div>
</section>""")

    remaining = [p for p in L.SERVICE_PAGES if p[0] not in {s["href"] for s in C.SERVICES_PAGE}]
    more = "".join(
        f"""<a class="card reveal" href="{href}">
      <h3>{label}</h3>
      <p>{desc}</p>
      <span class="textlink">Explore {I['arrow']}</span>
    </a>"""
        for href, label, desc in remaining
    )

    return f"""{page_hero(
        "oUr Services",
        C.SERVICES_PAGE_TITLE,
        C.MISSION,
        trail=[("Home", "index.html"), ("Services", None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Start a conversation {I["arrow"]}</a><a class="btn btn--outline-light" href="portfolio.html">See our work</a></div>',
    )}

<section class="section section--tight">
  <div class="wrap">
    {jump}
  </div>
</section>

{"".join(sections)}

<section class="section{' section--tint' if len(C.SERVICES_PAGE) % 2 else ''}">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Also from HER Consulting</span>
      <h2>Contracting and speaking services</h2>
    </div>
    <div class="grid grid--3">{more}</div>
  </div>
</section>

{L.stats_section()}
{L.cta_section()}
{L.partners_section()}"""


def grant_readiness() -> str:
    levels = "".join(
        f"""<article class="feature reveal">
      <span class="feature__badge">{idx:02d}</span>
      <h3>{title}</h3>
      <p style="margin-bottom:1.15rem">{sub}</p>
      {ticks(items)}
    </article>"""
        for idx, (title, sub, items) in enumerate(C.GRANT_LEVELS, start=1)
    )

    return f"""{page_hero(
        "oUr Services",
        "Getting Grant-Ready",
        "To Secure Grant Funding and Build Sustainable Programs",
        trail=[("Home", "index.html"), ("Services", "services.html"), ("Getting Grant-Ready", None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Contact us {I["arrow"]}</a></div>',
    )}

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Getting Grant Ready</span>
      <h2>Increasing Community Organizations&rsquo; Chances of Securing Grant Funding and Building Sustainable Programs</h2>
      <p>{C.GRANT_READY_INTRO}</p>
    </div>
    <div class="grid grid--2">{levels}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap wrap--narrow center reveal">
    <span class="eyebrow" style="justify-content:center">Getting Grant-Ready</span>
    <h2>Not sure what level you are?</h2>
    <p class="lede" style="margin-top:1rem">See more details in our resources&hellip;</p>
    <div class="btn-row" style="justify-content:center;margin-top:2rem">
      <a class="btn" href="contact.html">More Details {I['arrow']}</a>
    </div>
  </div>
</section>

{L.cta_section()}
{L.partners_section()}"""


def program_planning() -> str:
    return f"""{page_hero(
        "Our Services",
        "Program Planning &amp; Management",
        "Strategic Approaches for Purpose-Driven Planning and Management&hellip;",
        trail=[("Home", "index.html"), ("Services", "services.html"), ("Program Planning &amp; Management", None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Contact us {I["arrow"]}</a></div>',
    )}

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Program Planning &amp; Management</span>
      <h2>Ensuring programs are planned and managed for impact.</h2>
    </div>
    {feature_cards(C.PLANNING_PILLARS)}
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split split--reverse">
      <div class="stack reveal">
        <span class="eyebrow">Project Management and Evidence-Based Strategies</span>
        <h2>Delivered end to end</h2>
        <p>{C.SERVICES[1]['copy']}</p>
        <div class="btn-row" style="padding-top:0.6rem">
          <a class="btn" href="program-evaluation-impact.html">Program Evaluation &amp; Impact {I['arrow']}</a>
        </div>
      </div>
      <div class="split__media split__media--blob reveal">
        <img src="assets/img/illus-agreement.png" alt="Illustration of two people reaching an agreement" loading="lazy">
      </div>
    </div>
  </div>
</section>

{L.cta_section()}
{L.partners_section()}"""


def program_evaluation() -> str:
    return f"""{page_hero(
        "Our Services",
        "Program Evaluation &amp; Impact",
        "Quantifying and Understanding the &lsquo;Why&rsquo; and &lsquo;How&rsquo; of Program Success",
        trail=[("Home", "index.html"), ("Services", "services.html"), ("Program Evaluation &amp; Impact", None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Contact us {I["arrow"]}</a></div>',
    )}

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Program Evaluation &amp; Impact</span>
      <h2>Measuring, communicating, and amplifying program impact</h2>
    </div>
    {feature_cards(C.EVALUATION_PILLARS)}
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split">
      <div class="stack reveal">
        <span class="eyebrow">Health Services, Program Design, and Evaluation</span>
        <h2>Evidence you can act on</h2>
        <p>{C.SERVICES[2]['copy']}</p>
        <div class="btn-row" style="padding-top:0.6rem">
          <a class="btn" href="portfolio.html">See evaluation projects {I['arrow']}</a>
        </div>
      </div>
      <div class="split__media split__media--blob reveal">
        <img src="assets/img/illus-project-complete.png" alt="Illustration of a completed project" loading="lazy">
      </div>
    </div>
  </div>
</section>

{L.cta_section()}
{L.partners_section()}"""


def contracting_page(kind: str) -> str:
    federal = kind == "federal"
    title = "Federal Government Contracting" if federal else "State Government Contracting"

    caps = "".join(
        f"""<article class="card reveal">
      <span class="card__num">{idx:02d}</span>
      <h3>{name}</h3>
      <p>{body}</p>
    </article>"""
        for idx, (name, body) in enumerate(C.CONTRACTING_CAPABILITIES, start=1)
    )

    if federal:
        rows = "".join(
            f'<div class="code-row reveal"><b>{code}</b><span>{label}</span></div>'
            for code, label in C.NAICS_CODES
        )
        codes_block = f"""<div class="section-head section-head--center reveal">
      <span class="eyebrow">North American Industry Classification System</span>
      <h2>NAIC Codes [Federal]</h2>
    </div>
    <div class="codes">{rows}</div>"""
    else:
        groups = []
        for code, name, items in C.UNSPSC_GROUPS:
            rows = "".join(
                f'<div class="code-row reveal"><b>{c}</b><span>{label}</span></div>'
                for c, label in items
            )
            groups.append(f"""<div class="code-group reveal">
      <div class="code-group__title"><b>{code}:</b> <span>{name}</span></div>
      <div class="codes">{rows}</div>
    </div>""")
        codes_block = f"""<div class="section-head section-head--center reveal">
      <span class="eyebrow">United Nations Standard Products and Services Code</span>
      <h2>Registered UNSPSC Codes [State]</h2>
    </div>
    {"".join(groups)}"""

    slug = "federal-contracting.html" if federal else "state-contracting.html"

    return f"""{page_hero(
        "Our Services",
        title,
        C.SERVICES[4]["copy"] if federal else C.SERVICES[3]["copy"],
        trail=[("Home", "index.html"), ("Services", "services.html"), (title, None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Contact us {I["arrow"]}</a><a class="btn btn--outline-light" href="{"state-contracting.html" if federal else "federal-contracting.html"}">{"State contracting" if federal else "Federal contracting"}</a></div>',
    )}

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Capabilities</span>
      <h2>{title}</h2>
    </div>
    <div class="grid grid--3">{caps}</div>
  </div>
</section>

<section class="section section--tint" id="codes">
  <div class="wrap">
    {codes_block}
  </div>
</section>

{L.cta_section(secondary=(slug + "#codes", "View codes"))}
{L.partners_section()}"""


def speaking() -> str:
    gallery = "".join(
        f"""<figure class="card reveal" style="padding:0;overflow:hidden">
      <img src="assets/img/{img}" alt="{caption}" loading="lazy" style="aspect-ratio:4/3;object-fit:cover;width:100%">
      <figcaption style="padding:1.1rem 1.3rem 1.4rem;font-family:var(--font-display);font-weight:600;color:var(--ink);font-size:0.95rem">{caption}</figcaption>
    </figure>"""
        for img, caption in C.SPEAKING_GALLERY
    )

    types = "".join(
        f"""<article class="feature reveal">
      <span class="feature__badge">{idx:02d}</span>
      <h3>{name}</h3>
      <p>{body}</p>
    </article>"""
        for idx, (name, body) in enumerate(C.SPEAKING_TYPES, start=1)
    )

    return f"""{page_hero(
        "Our Services",
        "Speaking Engagement Services",
        "Amplifying Equity, Leadership, and Impact&mdash;One Stage at a Time",
        trail=[("Home", "index.html"), ("Services", "services.html"), ("Speaking Engagement Services", None)],
        actions=f'<div class="btn-row"><a class="btn" href="contact.html">Book Dr. Olatunde {I["arrow"]}</a></div>',
        extra=f'<p style="margin-top:1.4rem">{C.SERVICES[5]["copy"]}</p>',
    )}

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">On Stage</span>
      <h2>Speaking Engagement Services</h2>
      <p>{C.SPEAKING_TYPES[0][1]}</p>
    </div>
    <div class="grid grid--3">{gallery}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Formats</span>
      <h2>Ways to work together</h2>
    </div>
    <div class="grid grid--2">{types}</div>
  </div>
</section>

<section class="section section--deep">
  <div class="wrap wrap--narrow center reveal">
    <span class="eyebrow" style="justify-content:center">Signature Talk</span>
    <h2>{C.SIGNATURE_TALK}</h2>
    <p class="lede" style="margin-top:1.4rem;color:#b3c9db">{C.SIGNATURE_QUOTE}</p>
    <div class="btn-row" style="justify-content:center;margin-top:2.2rem">
      <a class="btn btn--light" href="contact.html">Invite Dr. Olatunde to speak {I['arrow']}</a>
    </div>
  </div>
</section>

{L.partners_section()}"""


def portfolio_hub() -> str:
    sections = []
    for href, label, icon, key in C.PORTFOLIO_CATEGORIES:
        tint = ' section--tint' if len(sections) % 2 else ""
        sections.append(f"""<section class="section{tint}" id="{key}">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{label}</span>
      <h2>{label}</h2>
    </div>
    {project_cards(key)}
    <div class="btn-row reveal" style="margin-top:clamp(1.6rem,3vw,2.4rem)">
      <a class="btn btn--ghost" href="{href}">All {label.lower()} projects {I['arrow']}</a>
    </div>
  </div>
</section>""")

    return f"""{page_hero(
        "our Portfolio",
        "our Portfolio",
        C.PORTFOLIO_INTRO_BODY,
        trail=[("Home", "index.html"), ("Portfolio", None)],
    )}

{portfolio_intro_section()}

<section class="section section--tight section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Browse by sector</span>
      <h2>Who we work with</h2>
    </div>
    {category_nav()}
  </div>
</section>

{"".join(sections)}

{similar_projects_cta()}
{L.stats_section()}
{L.partners_section()}"""


def portfolio_category(key: str) -> str:
    label = next(l for _, l, _, k in C.PORTFOLIO_CATEGORIES if k == key)
    return f"""{page_hero(
        "our Portfolio",
        label,
        C.PORTFOLIO_INTRO_BODY,
        trail=[("Home", "index.html"), ("Portfolio", "portfolio.html"), (label, None)],
    )}

<section class="section section--tight section--tint">
  <div class="wrap">
    {category_nav(active=key)}
  </div>
</section>

{portfolio_intro_section()}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{C.PORTFOLIO_INTRO_TITLE}</span>
      <h2>{C.PORTFOLIO_INTRO_LEAD}</h2>
    </div>
    {project_cards(key)}
  </div>
</section>

{similar_projects_cta()}
{L.stats_section()}
{L.partners_section()}"""


def contact() -> str:
    fields = "".join(
        f"""<div class="field">
      <label for="{fid}">{label}</label>
      <input id="{fid}" name="{fid}" type="{ftype}" placeholder="{label}"{" required" if req else ""}>
      <span class="err">Please enter a valid {"email address" if ftype == "email" else label.lower()}.</span>
    </div>"""
        for fid, label, ftype, req in C.CONTACT_FIELDS
    )

    return f"""{page_hero(
        "contact us",
        C.CONTACT_HEADING,
        C.MISSION,
        trail=[("Home", "index.html"), ("Contact Us", None)],
    )}

<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <form class="form-card reveal" data-contact-form novalidate>
        <span class="eyebrow">contact us</span>
        <h2 style="font-size:clamp(1.5rem,1.2rem+1.4vw,2rem);margin-bottom:1.6rem">{C.CONTACT_HEADING}</h2>
        {fields}
        <div class="field">
          <label for="message">Your message (optional)</label>
          <textarea id="message" name="message" placeholder="Your message (optional)"></textarea>
          <span class="err">Please add a message.</span>
        </div>
        <button class="btn" type="submit" style="width:100%">Send message {I['arrow']}</button>
        <p class="form-note" data-form-status>Your message opens in your email app addressed to {L.EMAIL}.</p>
      </form>

      <div class="stack reveal">
        <span class="eyebrow">Reach us directly</span>
        <h2 style="font-size:clamp(1.5rem,1.2rem+1.4vw,2rem)">{L.SITE_NAME}</h2>
        <ul class="info-list" style="margin-top:1.6rem">
          <li class="info-item">
            <span class="info-item__icon">{I['mail']}</span>
            <a href="mailto:{L.EMAIL}"><b>Email address</b><span>{L.EMAIL}</span></a>
          </li>
          <li class="info-item">
            <span class="info-item__icon">{I['badge']}</span>
            <div><b>Certification</b><span>{L.CERT}</span></div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Our Services</span>
      <h2>We Help in&hellip;</h2>
      <p>{C.MISSION_POINTS[1]}</p>
    </div>
    {service_cards()}
  </div>
</section>

{L.cta_section(primary=("services.html", "Our services"), secondary=("portfolio.html", "Our portfolio"))}
{L.partners_section()}"""


# ==========================================================================
# Registry
# ==========================================================================
PAGES = [
    ("index.html", "home", "HER Consulting LLC — Public Health Awareness. Action. Impact.",
     "HER Consulting LLC strengthens Public Health Awareness, Access, and Action by partnering with organizations and individuals dedicated to these goals.", home),

    ("about.html", "about", "About Us — HER Consulting LLC",
     "HER Consulting LLC provides expert consultation in strategic planning, project administration, and program evaluation. Meet founder Dr. Omolola (Lola) Olatunde and our subject matter experts.", about),

    ("services.html", "services", "Our Services — HER Consulting LLC",
     "Grant readiness, program planning and management, evaluation and impact, federal and state contracting, and speaking engagements.", services),

    ("grant-readiness.html", "services", "Getting Grant-Ready — HER Consulting LLC",
     "Training workshops, advisory, coaching, and technical assistance to secure grant funding and build sustainable programs.", grant_readiness),

    ("program-planning-management.html", "services", "Program Planning & Management — HER Consulting LLC",
     "Strategic approaches for purpose-driven planning and management, ensuring programs are planned and managed for impact.", program_planning),

    ("program-evaluation-impact.html", "services", "Program Evaluation & Impact — HER Consulting LLC",
     "Quantifying and understanding the why and how of program success — measuring, communicating, and amplifying program impact.", program_evaluation),

    ("federal-contracting.html", "services", "Federal Government Contracting — HER Consulting LLC",
     "Federal contracting capabilities and registered NAICS codes for HER Consulting LLC.", lambda: contracting_page("federal")),

    ("state-contracting.html", "services", "State Government Contracting — HER Consulting LLC",
     "State contracting capabilities and registered UNSPSC codes for HER Consulting LLC.", lambda: contracting_page("state")),

    ("speaking-engagement.html", "services", "Speaking Engagement Services — HER Consulting LLC",
     "Engaging keynotes, community talks, and panel discussions rooted in public health, entrepreneurship, and identity.", speaking),

    ("portfolio.html", "portfolio", "Our Portfolio — HER Consulting LLC",
     "A trusted partner for global organizations, federal and local agencies, and non-profits. Browse projects across sectors.", portfolio_hub),

    ("portfolio-global.html", "portfolio", "Portfolio: Global Organizations — HER Consulting LLC",
     "Global organization projects in Nigeria and the Democratic Republic of Congo.", lambda: portfolio_category("global")),

    ("portfolio-federal.html", "portfolio", "Portfolio: Federal Agencies — HER Consulting LLC",
     "Federal agency projects with the CDC, NIH, NIMHD, and the NACDS Foundation.", lambda: portfolio_category("federal")),

    ("portfolio-local.html", "portfolio", "Portfolio: Local Government Agencies — HER Consulting LLC",
     "Local government projects with the Indiana Department of Health, FSSA, and Marion County Public Health Department.", lambda: portfolio_category("local")),

    ("portfolio-nonprofits.html", "portfolio", "Portfolio: Non-Profits — HER Consulting LLC",
     "Non-profit projects with CICOA Aging and In-Home Services and Direct Relief.", lambda: portfolio_category("nonprofits")),

    ("contact.html", "contact", "Contact Us — HER Consulting LLC",
      "Contact HER Consulting LLC to discuss public health consulting, program evaluation, and community impact.", contact),
]


def main() -> None:
    for slug, active, title, description, builder in PAGES:
        html = L.DOCUMENT.format(
            title=title,
            description=description,
            slug="" if slug == "index.html" else slug,
            site_url=L.SITE_URL,
            site_name=L.SITE_NAME,
            email=L.EMAIL,
            header=L.header(active),
            body=builder(),
            footer=L.footer(),
        )
        with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"  built {slug:36} {len(html) // 1024:>4} KB")

    # sitemap.xml
    today = datetime.date.today().isoformat()
    urls = []
    for slug, *_ in PAGES:
        loc = L.SITE_URL + "/" + ("" if slug == "index.html" else slug)
        priority = "1.0" if slug == "index.html" else "0.8"
        urls.append(
            f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod>"
            f"<changefreq>monthly</changefreq><priority>{priority}</priority></url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap)
    print("  built sitemap.xml")

    print(f"\n{len(PAGES)} pages written to {ROOT}")


if __name__ == "__main__":
    main()
