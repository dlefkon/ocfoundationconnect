#!/usr/bin/env python3
"""Build the Wave 1 static site for Orange County Foundation & Basement Connect.
Static output only — no build tools needed at deploy time."""
import os

BASE = os.path.expanduser(
    "~/workspace/goals/become-a-billionaire/files/ocfoundationconnect-site")
BIZ = "Orange County Foundation &amp; Basement Connect"
BIZ_PLAIN = "Orange County Foundation & Basement Connect"
EMAIL = "contact@ocfoundationconnect.com"

DISCLOSURE_EN = (
    "<strong>Please read:</strong> Orange County Foundation &amp; Basement Connect is a "
    "<strong>referral service, not a contractor</strong>. We connect Orange County homeowners "
    "with <strong>one</strong> independent local foundation and basement waterproofing specialist. "
    "We do not perform foundation or waterproofing work ourselves, we are not the contractor who "
    "will contact you, and we are not affiliated with that contractor beyond sending them your request."
)
DISCLOSURE_ES = (
    "<strong>Importante:</strong> Orange County Foundation &amp; Basement Connect es un "
    "<strong>servicio de referidos, no un contratista</strong>. Conectamos a propietarios del condado "
    "de Orange con <strong>un</strong> especialista local independiente en cimientos y en "
    "impermeabilización de sótanos. No hacemos el trabajo de cimientos ni de impermeabilización, "
    "no somos el contratista que lo contactará y no tenemos otra relación con ese contratista que "
    "la de enviarle su solicitud."
)

PROBLEM_OPTIONS_EN = [
    ("", "Choose the closest match"),
    ("cracks", "Wall cracks"),
    ("water", "Water in the basement"),
    ("bowing", "Bowing or leaning walls"),
    ("mold", "Musty smell or mold"),
    ("floors", "Sloping or uneven floors"),
    ("sump", "Sump pump problem"),
    ("crawl", "Crawl space moisture"),
    ("other", "Something else / not sure"),
]
PROBLEM_OPTIONS_ES = [
    ("", "Elija la opción más parecida"),
    ("cracks", "Grietas en las paredes"),
    ("water", "Agua en el sótano"),
    ("bowing", "Paredes combadas o inclinadas"),
    ("mold", "Olor a humedad o moho"),
    ("floors", "Pisos inclinados o desnivelados"),
    ("sump", "Problema con la bomba de sumidero"),
    ("crawl", "Humedad en el espacio de acceso (crawl space)"),
    ("other", "Otra cosa / no estoy seguro"),
]

TCPA_EN = (
    "By checking this box, I agree to be contacted by phone call or text message about my request "
    "by the one independent local contractor my request is sent to, and by this referral service "
    "about my request. Calls and texts may be recorded. Consent is not a condition of receiving "
    "service, and I can opt out at any time."
)
TCPA_ES = (
    "Al marcar esta casilla, acepto que me contacten por llamada o mensaje de texto sobre mi "
    "solicitud el contratista local independiente al que se envíe mi solicitud, y este servicio de "
    "referidos. Las llamadas y los mensajes pueden grabarse. El consentimiento no es condición "
    "para recibir el servicio y puedo cancelarlo en cualquier momento."
)

TRUSTEDFORM_COMMENT = """    <!-- TrustedForm Certify integration point (account pending):
         when the ActiveProspect TrustedForm account is active, add the
         Certify script here and capture the certificate URL into the
         hidden field below, one certificate per submitted lead.
         <input type="hidden" name="tf_cert_url" value=""> -->"""

HONEYPOT = """    <div class="hp" aria-hidden="true">
      <label>Company website <input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
    </div>"""


def header(lang, toggle_href):
    if lang == "es":
        nav = [
            ("/es/reparacion-de-cimientos/", "Reparación de cimientos"),
            ("/es/impermeabilizacion-de-sotanos/", "Impermeabilización"),
            ("/es/agua-en-el-sotano-despues-de-la-lluvia/", "Agua tras la lluvia"),
            ("/contact/", "Contacto"),
        ]
        tag = "Servicio de referidos para propietarios del condado de Orange, NY"
        help_text, call_text, toggle_text = "Pedir ayuda", "Llame para una cotización gratuita", "English"
        home = "/es/impermeabilizacion-de-sotanos/"
        skip = "Saltar al contenido principal"
    else:
        nav = [
            ("/", "Home"),
            ("/foundation-repair-orange-county-ny/", "Foundation Repair"),
            ("/basement-waterproofing-orange-county-ny/", "Waterproofing"),
            ("/how-it-works/", "How It Works"),
            ("/contact/", "Contact"),
        ]
        tag = "A referral service for Orange County, NY homeowners"
        help_text, call_text, toggle_text = "Get Help", "Call for a free estimate", "Español"
        home = "/"
        skip = "Skip to main content"
    items = "\n          ".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in nav)
    return f"""<a class="skip-link" href="#main">{skip}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{home}">
      <span class="brand-name">{BIZ}</span>
      <span class="brand-tag">{tag}</span>
    </a>
    <nav class="main-nav" aria-label="Main">
      <ul>
          {items}
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn-ghost call-btn" href="/get-help/">{call_text}</a>
      <a class="btn btn-accent" href="/get-help/">{help_text}</a>
      <a class="btn btn-ghost" href="{toggle_href}" hreflang="{'en' if lang == 'es' else 'es'}">{toggle_text}</a>
    </div>
  </div>
</header>"""


def footer(lang):
    if lang == "es":
        disc = ("Orange County Foundation &amp; Basement Connect es un servicio de referidos. "
                "No somos contratistas, no hacemos trabajos de cimientos ni de impermeabilización "
                "y no estamos afiliados con el especialista independiente que recibe su solicitud.")
        links = [("/privacy-policy/", "Privacidad"), ("/terms/", "Términos"),
                 ("/accessibility/", "Accesibilidad"), ("/contact/", "Contacto"),
                 ("/how-it-works/", "Cómo funciona")]
        wrong = "¿Algo salió mal con su solicitud o con este sitio?"
        write = "Escríbanos a"
        fine = "Un servicio de referidos con base en Newburgh, NY. Atendemos a propietarios en todo el condado de Orange, NY."
    else:
        disc = ("Orange County Foundation &amp; Basement Connect is a referral service. "
                "We are not a contractor, we do not perform foundation or waterproofing work, "
                "and we are not affiliated with the independent specialist who receives your request.")
        links = [("/privacy-policy/", "Privacy Policy"), ("/terms/", "Terms"),
                 ("/accessibility/", "Accessibility"), ("/contact/", "Contact"),
                 ("/how-it-works/", "How It Works")]
        wrong = "Something wrong with your request or this site?"
        write = "Email us at"
        fine = "A referral service based in Newburgh, NY. Serving homeowners across Orange County, NY."
    items = "\n        ".join(f'<li><a href="{h}">{t}</a></li>' for h, t in links)
    return f"""<footer class="site-footer">
  <div class="wrap footer-inner">
    <p class="footer-name">{BIZ}</p>
    <p>{disc}</p>
    <ul class="footer-links">
        {items}
    </ul>
    <p>{wrong} {write} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <p class="footer-fine">&copy; <span data-year>2026</span> {BIZ}. {fine}</p>
  </div>
</footer>"""


def disclosure(lang):
    return f'<div class="disclosure" role="note"><p>{DISCLOSURE_ES if lang == "es" else DISCLOSURE_EN}</p></div>'


def next_strip(lang):
    if lang == "es":
        return ('<div class="next-strip"><strong>Qué sigue:</strong> un contratista local recibe su '
                'solicitud &rarr; lo llama a usted &rarr; cotización gratuita, sin compromiso.</div>')
    return ('<div class="next-strip"><strong>What happens next:</strong> one local contractor gets '
            'your request &rarr; they call you &rarr; free estimate, no obligation.</div>')


def options_html(lang, default):
    opts = PROBLEM_OPTIONS_ES if lang == "es" else PROBLEM_OPTIONS_EN
    out = []
    for val, label in opts:
        sel = " selected" if val == default and val != "" else ""
        dis = " disabled" if val == "" and not default else ""
        if val == "" and default:
            continue
        out.append(f'<option value="{val}"{sel}{dis}>{label}</option>')
    return "\n              ".join(out)


def short_form(lang, default_problem="", fid="sf"):
    es = lang == "es"
    name_l = "Nombre completo" if es else "Full name"
    phone_l = "Teléfono" if es else "Phone number"
    zip_l = "Código postal" if es else "ZIP code"
    prob_l = "¿Cuál es el problema?" if es else "What's the problem?"
    submit = "Pedir mi cotización gratuita" if es else "Request my free estimate"
    heading = "Pida una cotización gratuita" if es else "Request a free estimate"
    tcpa = TCPA_ES if es else TCPA_EN
    return f"""<form class="lead-form" method="post" action="" novalidate>
    <h3>{heading}</h3>
{TRUSTEDFORM_COMMENT}
{HONEYPOT}
    <div class="field">
      <label for="{fid}-name">{name_l}</label>
      <input type="text" id="{fid}-name" name="name" autocomplete="name" required>
    </div>
    <div class="field">
      <label for="{fid}-phone">{phone_l}</label>
      <input type="tel" id="{fid}-phone" name="phone" autocomplete="tel" required>
    </div>
    <div class="field">
      <label for="{fid}-zip">{zip_l}</label>
      <input type="text" id="{fid}-zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" required>
    </div>
    <div class="field">
      <label for="{fid}-problem">{prob_l}</label>
      <select id="{fid}-problem" name="problem" required>
              {options_html(lang, default_problem)}
      </select>
    </div>
    <div class="check">
      <input type="checkbox" id="{fid}-consent" name="consent" required>
      <label for="{fid}-consent">{tcpa}</label>
    </div>
    <button class="btn btn-accent" type="submit">{submit}</button>
    {next_strip(lang)}
  </form>"""


def full_form(lang="en"):
    es = lang == "es"
    tcpa = TCPA_ES if es else TCPA_EN
    return f"""<form class="lead-form" method="post" action="" novalidate>
{TRUSTEDFORM_COMMENT}
{HONEYPOT}
    <p class="problem-tag" hidden></p>
    <div class="field">
      <label for="gf-name">Full name</label>
      <input type="text" id="gf-name" name="name" autocomplete="name" required>
    </div>
    <div class="field">
      <label for="gf-phone">Phone number <span class="hint">(the contractor will call this number)</span></label>
      <input type="tel" id="gf-phone" name="phone" autocomplete="tel" required>
    </div>
    <div class="field">
      <label for="gf-email">Email <span class="hint">(optional)</span></label>
      <input type="email" id="gf-email" name="email" autocomplete="email">
    </div>
    <div class="field">
      <label for="gf-zip">ZIP code of the home</label>
      <input type="text" id="gf-zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" required>
    </div>
    <div class="field">
      <label for="gf-problem">What's the problem?</label>
      <select id="gf-problem" name="problem" required>
              {options_html(lang, "")}
      </select>
    </div>
    <div class="check">
      <input type="checkbox" id="gf-own" name="own_home" required>
      <label for="gf-own">I own the home at this address, or I am the owner's spouse or authorized decision-maker.</label>
    </div>
    <fieldset class="field">
      <legend>Best time to call you back</legend>
      <div class="radio-row">
        <label><input type="radio" name="callback" value="morning"> Morning</label>
        <label><input type="radio" name="callback" value="afternoon"> Afternoon</label>
        <label><input type="radio" name="callback" value="evening"> Evening</label>
      </div>
    </fieldset>
    <div class="field">
      <label for="gf-message">Anything else the specialist should know? <span class="hint">(optional)</span></label>
      <textarea id="gf-message" name="message"></textarea>
    </div>
    <div class="check">
      <input type="checkbox" id="gf-consent" name="consent" required>
      <label for="gf-consent">{tcpa}</label>
    </div>
    <button class="btn btn-accent" type="submit">Request my free estimate</button>
    {next_strip(lang)}
  </form>"""


def zip_checker(lang, cid="zc"):
    es = lang == "es"
    if es:
        h = "Revise si su casa está en la zona de servicio"
        p = ("Este servicio cubre casas en el condado de Orange, NY. Ingrese su código postal "
             "para confirmarlo antes de enviar una solicitud.")
        label, btn = "Su código postal", "Revisar mi código"
    else:
        h = "Check whether your home is in the service area"
        p = ("This service covers homes in Orange County, NY. Enter your ZIP code to confirm "
             "before you send a request.")
        label, btn = "Your ZIP code", "Check my ZIP"
    return f"""<div class="tool">
  <h2>{h}</h2>
  <p>{p}</p>
  <form class="zip-checker" novalidate>
    <div class="tool-row">
      <div class="field">
        <label for="{cid}-zip">{label}</label>
        <input type="text" id="{cid}-zip" name="zip" inputmode="numeric" autocomplete="postal-code" maxlength="5" required>
      </div>
      <button class="btn" type="submit">{btn}</button>
    </div>
  </form>
  <div class="tool-result" aria-live="polite"></div>
</div>"""


def symptom_picker(lang):
    es = lang == "es"
    items = [
        ("cracks", "Grietas en las paredes" if es else "Wall cracks"),
        ("water", "Agua en el sótano" if es else "Water in the basement"),
        ("bowing", "Paredes combadas o inclinadas" if es else "Bowing or leaning walls"),
        ("mold", "Olor a humedad o moho" if es else "Musty smell or mold"),
        ("floors", "Pisos inclinados" if es else "Sloping floors"),
    ]
    h = "¿Qué está viendo?" if es else "What are you seeing?"
    btns = "\n      ".join(
        f'<button type="button" class="picker-btn" data-symptom="{k}" aria-pressed="false">{v}</button>'
        for k, v in items)
    return f"""<div class="tool symptom-picker">
  <h2>{h}</h2>
  <div class="picker-options" role="group" aria-label="{h}">
      {btns}
  </div>
  <div class="picker-output" aria-live="polite"></div>
</div>"""


def render(lang, title, desc, toggle_href, body, hero_h1=None, hero_lede=None):
    hero = ""
    if hero_h1:
        hero = (f'<div class="hero"><div class="wrap"><h1>{hero_h1}</h1>'
                f'<p class="lede">{hero_lede or ""}</p></div></div>')
        main_open = '<main id="main"><div class="wrap">'
    else:
        main_open = '<main id="main"><div class="wrap">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
{header(lang, toggle_href)}
{hero}
{main_open}
{body}
</div>
</main>
{footer(lang)}
<script src="/assets/site.js"></script>
<script data-goatcounter="https://ocfoundationconnect.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
"""

PAGES = []  # (path, html)

# =====================================================================
# CORE PAGES (English)
# =====================================================================

TOWNS = ["Newburgh", "Middletown", "Monroe", "New Windsor", "Warwick", "Goshen",
         "Washingtonville", "Montgomery", "Walden", "Pine Bush", "Port Jervis",
         "Chester", "Florida", "Cornwall", "Cornwall-on-Hudson", "Highland Falls",
         "Highland Mills", "Central Valley", "Harriman", "Greenwood Lake",
         "Otisville", "Maybrook", "Campbell Hall", "Circleville", "Bullville",
         "Salisbury Mills", "Rock Tavern", "Vails Gate", "Slate Hill", "Westtown",
         "Tuxedo", "Tuxedo Park", "Southfields", "Cuddebackville", "Huguenot",
         "Sparrow Bush", "Pine Island", "New Hampton", "Arden", "Bellvale"]
town_list_html = "\n        ".join(f"<li>{t}</li>" for t in TOWNS)

home_body = f"""
{disclosure("en")}
<section>
  <h2>Start with what you're seeing</h2>
  <p>Most people don't search for "foundation repair." They search for the thing they just
  found: a crack, a puddle, a wall that doesn't look straight anymore. Pick the closest match
  and we'll explain what it usually means.</p>
  {symptom_picker("en")}
</section>
<section>
  <h2>How this service works</h2>
  <ol class="steps">
    <li><strong>You send one request.</strong> Tell us the problem and your ZIP code. Your
    request goes to exactly one independent local specialist — never a list of companies.</li>
    <li><strong>The specialist calls you.</strong> They'll ask a few questions and, if it's a
    fit, schedule a visit at a time that works for you.</li>
    <li><strong>You get a free estimate.</strong> The contractor inspects in person and quotes
    the work. No obligation — the decision is yours.</li>
  </ol>
  <p><a href="/how-it-works/">Read more about how it works</a></p>
</section>
<section>
  <h2>What we can connect you for</h2>
  <div class="cards">
    <div class="card"><h3><a href="/foundation-repair-orange-county-ny/">Foundation repair</a></h3>
    <p>Cracks, bowing walls, settling — the structural side of the house.</p></div>
    <div class="card"><h3><a href="/basement-waterproofing-orange-county-ny/">Basement waterproofing</a></h3>
    <p>Water in the basement, interior drainage, and sump pumps.</p></div>
    <div class="card"><h3><a href="/basement-water-after-rain/">Water after rain</a></h3>
    <p>The basement was dry until the storm. Here's what that usually means.</p></div>
    <div class="card"><h3><a href="/foundation-crack-repair-cost/">What does it cost?</a></h3>
    <p>Honest, typical price ranges for crack repair and waterproofing — and what moves them.</p></div>
  </div>
</section>
<section>
  {zip_checker("en", "zc-home")}
</section>
<section>
  <h2>Orange County homes, Orange County problems</h2>
  <p>Orange County sits between the Hudson River and the Delaware, and its basements feel it.
  Spring thaw and snowmelt push water against foundation walls from March through May. Summer
  thunderstorms and fall nor'easters soak already-wet soil. Older homes in Newburgh, Middletown,
  and Port Jervis often sit on stone or block foundations; the post-war ranches and split-levels
  in New Windsor, Monroe, and Middletown's suburbs are mostly block or poured concrete — and
  both kinds crack, leak, and bow when the soil around them stays wet.</p>
  <h3>Towns we serve</h3>
  <ul class="town-list">
        {town_list_html}
  </ul>
  <p>Don't see your town? If your home is in Orange County, NY, you're in the service area —
  use the ZIP checker above to confirm.</p>
</section>
<section>
  <h2>Common questions</h2>
  <dl class="faq">
    <dt>Does the estimate cost anything?</dt>
    <dd>No. The specialists we connect you with offer free estimates. You pay nothing to this
    service, and nothing to the contractor unless you hire them for work.</dd>
    <dt>Who will call me?</dt>
    <dd>One independent local foundation and waterproofing contractor — the single specialist
    your request is sent to. Not a call center, and not a string of companies.</dd>
    <dt>How many companies get my number?</dt>
    <dd>One. Your request is sent to a single contractor. We do not sell your information to
    multiple companies.</dd>
    <dt>What if nobody calls me?</dt>
    <dd>Tell us. Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we'll look into what happened
    with your request.</dd>
    <dt>Are you the contractor?</dt>
    <dd>No. We are a referral service based in Newburgh, NY. We don't do the work, and we don't
    set the contractor's prices or schedule.</dd>
  </dl>
</section>
"""
PAGES.append(("index.html", render(
    "en",
    "Foundation Repair &amp; Basement Waterproofing Referrals in Orange County, NY | " + BIZ_PLAIN,
    "Free referral service connecting Orange County, NY homeowners with one independent local foundation repair and basement waterproofing specialist. Free estimates.",
    "/es/impermeabilizacion-de-sotanos/",
    home_body,
    hero_h1="Water in the basement? Cracks in the foundation?",
    hero_lede=("Tell us what you're seeing. We'll connect you with one independent local "
               "specialist in Orange County, NY — free estimate, no obligation, and your "
               "request goes to one contractor, not a list."))))

how_body = f"""
{disclosure("en")}
<section>
  <h2>The short version</h2>
  <ol class="steps">
    <li><strong>You send one request.</strong> Use the form or start with the ZIP checker.
    Tell us what you're seeing at the house.</li>
    <li><strong>One local specialist gets it.</strong> Your request goes to a single
    independent foundation and waterproofing contractor who serves Orange County.</li>
    <li><strong>They call you.</strong> The contractor calls at the time you picked, asks
    about the problem, and can schedule a free in-person estimate.</li>
  </ol>
</section>
<section>
  <h2>What makes a request work</h2>
  <ul>
    <li><strong>Homeowners.</strong> This service is for the owner of the home (or a spouse or
    authorized decision-maker). If you rent, the fastest route is your landlord — and landlords
    are welcome to send a request for a property they own.</li>
    <li><strong>Orange County, NY.</strong> The home must be in Orange County. The ZIP checker
    on the <a href="/">home page</a> confirms your area instantly.</li>
    <li><strong>A real, current problem.</strong> Active water, cracks, bowing walls,
    settling, crawl-space moisture, or a failed sump pump. (General price shopping with no
    property or problem isn't something a specialist can act on.)</li>
  </ul>
</section>
<section>
  <h2>What we are — and what we aren't</h2>
  <p>We are a referral service run under the name {BIZ}, based in Newburgh, NY. We built this
  site to route Orange County homeowners to a local specialist without the usual lead-mill
  runaround: one request, one contractor, no bidding war over your phone number.</p>
  <p>We are <strong>not</strong> a contractor. We don't inspect homes, we don't quote prices
  for work, we don't schedule the contractor's crews, and we don't guarantee any contractor's
  work. The estimate, the contract, and the work itself are between you and the contractor.
  Before you hire anyone, check their insurance and references the way you would with any
  contractor you found on your own.</p>
</section>
<section>
  <h2>Your information</h2>
  <p>When you send a request, we record what you entered, when you sent it, and your consent
  to be contacted — and we pass the request to one contractor. Calls may be recorded so both
  sides have a record of the conversation. The full details are in our
  <a href="/privacy-policy/">privacy policy</a>.</p>
  <p><a class="btn btn-accent" href="/get-help/">Request a free estimate</a></p>
</section>
"""
PAGES.append(("how-it-works/index.html", render(
    "en", "How It Works | " + BIZ_PLAIN,
    "How the referral works: send one request, one independent local specialist receives it and calls you, free estimate with no obligation.",
    "/es/impermeabilizacion-de-sotanos/", how_body,
    hero_h1="How it works",
    hero_lede="One request. One local contractor. A free estimate. Here's the whole process, in plain language.")))

contact_body = f"""
{disclosure("en")}
<section>
  <h2>Reach the service</h2>
  <p><strong>Business:</strong> {BIZ}<br>
  <strong>Based in:</strong> Newburgh, NY — serving homeowners across Orange County, NY<br>
  <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Email is the best way to reach us. We review messages during regular business hours and
  reply as soon as we can. If you're trying to reach the contractor about an estimate or a
  scheduled visit, contact them directly — they're the ones doing the work.</p>
</section>
<section>
  <h2>Want a free estimate?</h2>
  <p>The fastest route is the request form — it goes straight into the referral process:</p>
  <p><a class="btn btn-accent" href="/get-help/">Go to the request form</a></p>
</section>
<section>
  <h2>Something wrong with your request or this site?</h2>
  <p>If you sent a request and never heard back, if you want your information removed, or if
  something on this site is broken or wrong, email
  <a href="mailto:{EMAIL}">{EMAIL}</a> and tell us. We'd rather hear it from you than read it
  in a public complaint.</p>
</section>
"""
PAGES.append(("contact/index.html", render(
    "en", "Contact | " + BIZ_PLAIN,
    "Contact Orange County Foundation & Basement Connect — a referral service based in Newburgh, NY serving Orange County homeowners.",
    "/es/impermeabilizacion-de-sotanos/", contact_body,
    hero_h1="Contact us",
    hero_lede="Questions about a request, your information, or this site — here's how to reach the referral service.")))

privacy_body = f"""
{disclosure("en")}
<section>
  <p><em>Last updated: November 2026.</em></p>
  <h2>Who we are</h2>
  <p>{BIZ} is a referral service based in Newburgh, NY. We connect homeowners in Orange
  County, NY with one independent local foundation and basement waterproofing contractor.
  This policy explains what information we collect when you use this site, and what happens
  to it.</p>
  <h2>What we collect</h2>
  <ul>
    <li><strong>What you type into a request form:</strong> your name, phone number, optional
    email, the home's ZIP code, the type of problem, whether you own the home, your preferred
    callback time, and anything you add in the message box.</li>
    <li><strong>Consent records:</strong> when you submit a request, we record the date and
    time, the consent language you agreed to, and a consent certificate for the submission.</li>
    <li><strong>Call records:</strong> if you call our phone number, the call may be recorded,
    and we keep the number, time, and length of the call.</li>
    <li><strong>Basic technical data:</strong> standard server logs (such as IP address and
    browser type) needed to run and protect the site. This site does not use advertising
    trackers.</li>
  </ul>
  <h2>Who receives your information</h2>
  <p>When you send a request, your information goes to <strong>one</strong> independent local
  foundation and waterproofing contractor so they can contact you about a free estimate. We
  do not sell your request to multiple companies, and we do not share it with anyone else
  except service providers who help us operate (for example, phone and form processing), who
  may only use it to run this service.</p>
  <h2>How the contractor may contact you</h2>
  <p>By submitting a request with the consent box checked, you agree to be contacted by phone
  call or text message by the contractor your request was sent to, and by us about your
  request. Calls and texts may be recorded. Consent is not a condition of receiving service.
  You can opt out of texts at any time by replying STOP, and out of calls by telling us or
  the contractor.</p>
  <h2>How long we keep it</h2>
  <p>We keep request and consent records for as long as needed to operate the service and to
  document consent — consent certificates are retained for up to five years. You can ask us
  what we hold about you, or ask us to delete it, at any time.</p>
  <h2>Your choices</h2>
  <ul>
    <li>Ask what information we hold about you.</li>
    <li>Ask us to correct or delete it.</li>
    <li>Withdraw consent to be contacted.</li>
  </ul>
  <p>For any of these, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Changes to this policy</h2>
  <p>If this policy changes, the new version will be posted on this page with a new date.
  The policy that applies to your request is the one in effect when you sent it.</p>
</section>
"""
PAGES.append(("privacy-policy/index.html", render(
    "en", "Privacy Policy | " + BIZ_PLAIN,
    "Privacy policy for Orange County Foundation & Basement Connect: what the request form collects, who receives it (one contractor), and how consent is recorded.",
    "/es/impermeabilizacion-de-sotanos/", privacy_body,
    hero_h1="Privacy policy",
    hero_lede="What we collect, who gets it (one contractor), and how to get it back or delete it.")))

terms_body = f"""
{disclosure("en")}
<section>
  <p><em>Last updated: November 2026.</em></p>
  <h2>What this service is</h2>
  <p>{BIZ} operates this website as a <strong>referral (connection) service</strong>. We
  connect homeowners in Orange County, NY with one independent local foundation and basement
  waterproofing contractor. We are not a contractor. We do not perform, supervise, price, or
  guarantee any foundation, waterproofing, or other construction work.</p>
  <h2>No affiliation</h2>
  <p>The contractor who receives your request is an independent business. Nothing on this site
  means we are partners, agents, employers, or affiliates of that contractor, and the
  contractor is not our agent. Any estimate, contract, warranty, or work is solely between
  you and the contractor.</p>
  <h2>Estimates and prices</h2>
  <p>Price ranges mentioned on this site are typical market ranges published for general
  information. They are not quotes, offers, or promises. Only the contractor can price your
  job, after seeing your home.</p>
  <h2>Eligibility</h2>
  <p>The referral service is intended for homeowners (or their spouses or authorized
  decision-makers) whose property is in Orange County, NY. Submitting a request does not
  guarantee that a contractor will contact you or offer an estimate.</p>
  <h2>Your responsibilities</h2>
  <p>Give accurate information in a request, and do your own diligence before hiring any
  contractor — including verifying insurance and references. If a situation is an emergency
  (for example, active flooding near electrical equipment), contact emergency services or a
  licensed electrician first; this site is not an emergency service.</p>
  <h2>Site content</h2>
  <p>Content on this site is general information about foundation and basement problems, not
  professional engineering or construction advice for your specific home.</p>
  <h2>Contact</h2>
  <p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a>. These terms are
  governed by the laws of the State of New York.</p>
</section>
"""
PAGES.append(("terms/index.html", render(
    "en", "Terms of Use | " + BIZ_PLAIN,
    "Terms of use for Orange County Foundation & Basement Connect: a connection service, not the contractor; no affiliation; estimates come from the contractor.",
    "/es/impermeabilizacion-de-sotanos/", terms_body,
    hero_h1="Terms of use",
    hero_lede="Plain terms for a plain service: we connect, the contractor does the work.")))

access_body = f"""
{disclosure("en")}
<section>
  <h2>Our commitment</h2>
  <p>We want every Orange County homeowner to be able to use this site, including people who
  use screen readers, keyboards, or other assistive technology. We build and check this site
  against the Web Content Accessibility Guidelines (WCAG) 2.1 at the AA level.</p>
  <h2>What we've done</h2>
  <ul>
    <li>Every form field has a visible label; the ZIP checker and symptom picker work with a
    keyboard alone and announce their results to assistive technology.</li>
    <li>Text and background colors are chosen for sufficient contrast, and links and buttons
    show a clear focus outline.</li>
    <li>Pages use semantic headings and landmarks, a skip-to-content link, and text that
    stays readable when zoomed.</li>
    <li>No information on this site is conveyed by color alone, and nothing here requires a
    mouse.</li>
  </ul>
  <h2>Tell us if something doesn't work</h2>
  <p>Accessibility is ongoing work, and this statement describes the site as it stands today.
  If any part of this site is hard for you to use, email
  <a href="mailto:{EMAIL}">{EMAIL}</a> and tell us what page and what went wrong. We'll fix
  it as quickly as we can — and if you need the information another way in the meantime, ask
  and we'll provide it.</p>
</section>
"""
PAGES.append(("accessibility/index.html", render(
    "en", "Accessibility Statement | " + BIZ_PLAIN,
    "Accessibility statement for Orange County Foundation & Basement Connect: WCAG 2.1 AA target, labeled forms, keyboard-operable tools, and how to report a barrier.",
    "/es/impermeabilizacion-de-sotanos/", access_body,
    hero_h1="Accessibility statement",
    hero_lede="How this site is built to be usable by everyone — and how to tell us when it isn't.")))

gethelp_body = f"""
{disclosure("en")}
<section>
  <h2>First — is the home in Orange County?</h2>
  {zip_checker("en", "zc-gethelp")}
</section>
<section>
  <h2>Request a free estimate</h2>
  <p>Fill this out and your request goes to one independent local foundation and waterproofing
  specialist — not a list of companies. The estimate is free and there's no obligation.</p>
  {full_form("en")}
  <p>This service is for homeowners. If you rent, your landlord is the person who can request
  work on the property — landlords are welcome to use this form for a home they own.</p>
</section>
"""
PAGES.append(("get-help/index.html", render(
    "en", "Request a Free Estimate | " + BIZ_PLAIN,
    "Request a free foundation or basement waterproofing estimate in Orange County, NY. One request goes to one independent local specialist.",
    "/es/impermeabilizacion-de-sotanos/", gethelp_body,
    hero_h1="Request a free estimate",
    hero_lede="One form, one local specialist, one call back. Here's exactly what we ask and why.")))

# =====================================================================
# WAVE 1 SERVICE / PROBLEM PAGES (English)
# =====================================================================

def svc_page(path, title, desc, h1, lede, sections, default_problem, form_intro,
             toggle="/es/impermeabilizacion-de-sotanos/"):
    body = f"""
{disclosure("en")}
{sections}
<section>
  <h2>{form_intro}</h2>
  {short_form("en", default_problem, "sf-" + path.split("/")[0][:12])}
</section>
"""
    return (path + "/index.html", render("en", title, desc,
            toggle, body, hero_h1=h1, hero_lede=lede))

# --- 1. Foundation repair hub ---
s = """
<section>
  <h2>Foundation problems don't heal</h2>
  <p>A foundation crack, a bowing wall, a floor that's started to slope — these are the house
  telling you something changed underneath it. In Orange County, the usual drivers are water
  and soil: heavy spring rain and snowmelt saturate the ground, clay-heavy soils in parts of
  the county swell and push, and freeze-thaw cycles work cracks wider year after year.</p>
  <p>The housing stock here spans a wide range. Homes in Newburgh, Middletown, and Port Jervis
  often stand on stone or concrete-block foundations that are a century old. Post-war homes in
  New Windsor, Monroe, and the Middletown suburbs are block or poured concrete. The repair
  approach is different for each — which is why a real fix starts with someone looking at your
  actual foundation, not a phone quote.</p>
</section>
<section>
  <h2>Signs worth acting on</h2>
  <div class="cards">
    <div class="card"><h3><a href="/foundation-crack-repair/">Foundation cracks</a></h3>
    <p>Vertical, horizontal, and stair-step cracks — and which ones are structural.</p></div>
    <div class="card"><h3><a href="/bowing-basement-walls/">Bowing basement walls</a></h3>
    <p>A wall curving inward under soil pressure is a structural problem, not a cosmetic one.</p></div>
    <div class="card"><h3><a href="/signs-of-foundation-settling/">Settling and sloping floors</a></h3>
    <p>Sticking doors, cracked drywall, floors that slope — the classic settling checklist.</p></div>
    <div class="card"><h3><a href="/foundation-crack-repair-cost/">Crack repair costs</a></h3>
    <p>Typical ranges for crack injection, and when a crack points to a bigger job.</p></div>
  </div>
</section>
<section>
  <h2>What a foundation specialist does</h2>
  <p>Depending on what they find, a foundation contractor may seal and inject cracks, stabilize
  a bowing wall with anchors or reinforcement, or support a settling section of the house.
  The right method depends on your foundation type, the soil, and how far the problem has gone.
  That's the contractor's call after an in-person inspection — and the inspection and estimate
  are free through this service.</p>
</section>
"""
PAGES.append(svc_page("foundation-repair-orange-county-ny",
    "Foundation Repair in Orange County, NY | " + BIZ_PLAIN,
    "Get connected with one independent local foundation repair specialist in Orange County, NY. Cracks, bowing walls, settling — free in-person estimates.",
    "Foundation repair in Orange County, NY",
    "Cracks, bowing walls, or a house that's settling? We connect Orange County homeowners with one independent local foundation specialist for a free estimate.",
    s, "cracks", "Request a free foundation estimate",
    toggle="/es/reparacion-de-cimientos/"))

# --- 2. Waterproofing hub ---
s = """
<section>
  <h2>Why Orange County basements get wet</h2>
  <p>Most wet basements here aren't a mystery. The county gets heavy spring rain on top of
  snowmelt, summer downpours, and fall nor'easters — and a lot of that water ends up against
  foundation walls. Homes near the Wallkill River, Moodna Creek, and the low ground along the
  Hudson and Delaware corridors deal with high water tables on top of it. When the soil around
  your foundation is saturated, water finds the easiest way in: floor-wall joints, cracks,
  and porous block.</p>
</section>
<section>
  <h2>What waterproofing actually involves</h2>
  <p>Real basement waterproofing is usually an <strong>interior drainage system</strong>: a
  channel installed along the inside perimeter of the foundation that collects water before
  it spreads across the floor and routes it to a <a href="/sump-pump-installation-repair/">sump
  pump</a>, which sends it outside and away from the house. Exterior grading, gutters, and
  downspout extensions matter too — a good contractor will tell you if part of your problem
  can be solved from outside before selling you a system.</p>
  <div class="cards">
    <div class="card"><h3><a href="/basement-water-after-rain/">Water after rain</a></h3>
    <p>Dry basement, big storm, wet floor. What that pattern usually means.</p></div>
    <div class="card"><h3><a href="/sump-pump-installation-repair/">Sump pumps</a></h3>
    <p>Installation, replacement, battery backups, and what failure looks like.</p></div>
    <div class="card"><h3><a href="/wet-basement-smell-mold/">Musty smell or mold</a></h3>
    <p>The smell is a moisture symptom. The moisture is the problem.</p></div>
    <div class="card"><h3><a href="/basement-waterproofing-cost/">Waterproofing costs</a></h3>
    <p>Typical ranges for interior drainage systems and what changes the price.</p></div>
  </div>
</section>
<section>
  <h2>When to act</h2>
  <p>Water that shows up once after a freak storm is worth watching. Water that shows up every
  spring, puddles that keep coming back to the same corner, efflorescence (white crust) on the
  walls, or a sump pit that runs constantly — that's a pattern, and patterns get worse, not
  better. A free estimate costs you an hour and tells you which one you're dealing with.</p>
</section>
"""
PAGES.append(svc_page("basement-waterproofing-orange-county-ny",
    "Basement Waterproofing in Orange County, NY | " + BIZ_PLAIN,
    "Wet basement in Orange County, NY? Get connected with one independent local waterproofing specialist. Interior drainage, sump pumps, free estimates.",
    "Basement waterproofing in Orange County, NY",
    "A basement that floods every spring isn't bad luck — it's water doing what water does. We connect you with one independent local waterproofing specialist for a free estimate.",
    s, "water", "Request a free waterproofing estimate"))

# --- 3. Foundation crack repair ---
s = """
<section>
  <h2>Not all cracks are equal</h2>
  <p><strong>Vertical cracks</strong> are the most common. Many are simple shrinkage cracks from
  the concrete curing, and a dry, hairline vertical crack that hasn't changed in years is often
  more nuisance than emergency. <strong>Horizontal cracks</strong> are different: they usually
  mean pressure from the soil outside is bending the wall — that's structural. <strong>Stair-step
  cracks</strong> through block or mortar joints often point to uneven settling.</p>
  <p>The cracks that deserve a prompt look: any crack that <strong>leaks water</strong>, is
  <strong>wider than a pencil line</strong>, is <strong>growing</strong>, runs
  <strong>horizontal</strong>, or comes with a wall that's starting to bow or floors that are
  starting to slope.</p>
</section>
<section>
  <h2>How leaking cracks are usually fixed</h2>
  <p>For a non-structural leaking crack in poured concrete, the standard repair is
  <strong>crack injection</strong> — the crack is sealed and filled from the inside with a
  material that bonds through the wall and stops the water path. It's a targeted fix for a
  targeted problem. If the crack is a symptom of movement — bowing, settling, pressure — the
  specialist will tell you that sealing it alone won't hold, and explain what will.</p>
  <p>Wondering about price first? See <a href="/foundation-crack-repair-cost/">what crack
  repair typically costs</a>.</p>
</section>
"""
PAGES.append(svc_page("foundation-crack-repair",
    "Foundation Crack Repair in Orange County, NY | " + BIZ_PLAIN,
    "Foundation crack repair referrals in Orange County, NY: leaking cracks, horizontal cracks, stair-step cracks. Free estimate from one local specialist.",
    "Foundation crack repair",
    "Some cracks are cosmetic. Some are the first sign of a wall in trouble. Get one local specialist to look at yours — free.",
    s, "cracks", "Request a free crack repair estimate"))

# --- 4. Bowing basement walls ---
s = """
<section>
  <h2>What's pushing your wall in</h2>
  <p>A basement wall bows inward when the soil outside pushes harder than the wall can resist.
  In Orange County that pressure builds when soil gets saturated — spring thaw, long wet
  stretches, poor drainage against the house — and clay-heavy soil swells as it takes on water.
  Freeze-thaw cycles add to it: water in the soil freezes, expands, and leans on the wall a
  little more each winter.</p>
</section>
<section>
  <h2>Signs a wall is bowing</h2>
  <ul>
    <li>A visible inward curve in the wall, easiest to see sighting along it</li>
    <li>Horizontal cracking, often near the middle height of the wall</li>
    <li>The top of the wall tipping in, or gaps opening where wall meets floor joists</li>
    <li>Stair-step cracks near the corners of a block wall</li>
  </ul>
  <p>A bowing wall does not straighten itself out, and it doesn't stop where it is — the same
  pressure keeps working. Left long enough, a wall can fail. This is one problem where "wait
  and see" is genuinely the expensive option.</p>
</section>
<section>
  <h2>How specialists stabilize a bowing wall</h2>
  <p>Depending on how far the wall has moved, contractors commonly stabilize it with
  <strong>wall anchors</strong> tied into stable soil outside, or <strong>reinforcement
  straps/beams</strong> that brace the wall from inside. Severe walls sometimes need partial
  rebuilding. Which one fits depends on the wall's material (block vs. poured vs. stone — all
  three are common in this county), how far it's moved, and access outside. Only an in-person
  inspection can answer that.</p>
</section>
"""
PAGES.append(svc_page("bowing-basement-walls",
    "Bowing Basement Walls in Orange County, NY | " + BIZ_PLAIN,
    "Basement wall bowing or leaning inward in Orange County, NY? Causes, warning signs, and a free estimate from one independent local specialist.",
    "Bowing basement walls",
    "A basement wall that curves inward is under pressure it can't hold forever. Get it looked at while stabilization is still an option.",
    s, "bowing", "Request a free wall inspection estimate"))

# --- 5. Crawl space encapsulation ---
s = """
<section>
  <h2>The smaller slice of Orange County homes</h2>
  <p>Most homes in Orange County sit on full basements or slabs, but plenty of older farmhouses,
  cottages around Greenwood Lake and the county's rural towns, and additions of every era are
  built over crawl spaces. A dirt-floor crawl space pulls ground moisture up into the house
  around the clock — feeding musty smells, cupping floors, and higher humidity in the rooms
  above.</p>
</section>
<section>
  <h2>What encapsulation means</h2>
  <p>Encapsulation seals the crawl space off from the ground and the outside air: a heavy
  vapor barrier over the floor and up the walls, sealed vents, and often drainage or a small
  sump and dehumidifier where conditions call for it. Done right, the space under the house
  stays dry instead of cycling with every wet Hudson Valley spring.</p>
  <p>Signs your crawl space needs a look: a musty smell that won't leave, floors that feel
  spongy or are starting to cup, visible moisture or standing water under the house, and
  insulation hanging down or soaked.</p>
</section>
"""
PAGES.append(svc_page("crawl-space-encapsulation",
    "Crawl Space Encapsulation in Orange County, NY | " + BIZ_PLAIN,
    "Crawl space moisture problems in Orange County, NY? Encapsulation referrals and free estimates from one independent local specialist.",
    "Crawl space encapsulation",
    "A damp crawl space doesn't stay under the house — it becomes the air your house breathes. Get a free estimate from one local specialist.",
    s, "crawl", "Request a free crawl space estimate"))

# --- 6. Sump pump installation & repair ---
s = """
<section>
  <h2>The hardest-working appliance in the basement</h2>
  <p>A sump pump sits in a pit at the lowest point of your basement, collects the water your
  drainage system gathers, and pumps it outside — away from the foundation. When it works,
  you never think about it. When it fails during a storm, a basement can take on water fast.</p>
</section>
<section>
  <h2>Signs a pump is on its way out</h2>
  <ul>
    <li>It runs constantly, or cycles on and off rapidly</li>
    <li>It makes grinding, rattling, or humming noises without moving water</li>
    <li>The pit fills and the pump doesn't kick on (float or switch trouble)</li>
    <li>It's more than about 7–10 years old and has never been serviced</li>
    <li>It stopped during a power outage and the basement paid for it — a
    <strong>battery backup</strong> pump is the usual answer to that one</li>
  </ul>
</section>
<section>
  <h2>Installation, replacement, and backup</h2>
  <p>A specialist can replace a failed or undersized pump, add a battery backup so a storm
  outage doesn't flood the basement, or install a pump and pit where a waterproofing system
  needs one. If your pump just failed and there's water coming in, see
  <a href="/sump-pump-failure-what-to-do/">what to do when a sump pump fails</a> first.</p>
</section>
"""
PAGES.append(svc_page("sump-pump-installation-repair",
    "Sump Pump Installation &amp; Repair in Orange County, NY | " + BIZ_PLAIN,
    "Sump pump replacement, installation, and battery backup referrals in Orange County, NY. Free estimate from one independent local specialist.",
    "Sump pump installation &amp; repair",
    "The pump you never think about is the one standing between a storm and a flooded basement. Keep it that way.",
    s, "sump", "Request a free sump pump estimate"))

# --- 7. Basement water after rain ---
s = """
<section>
  <h2>First, right now</h2>
  <ul>
    <li><strong>Stay out of standing water</strong> if it may be in contact with electrical
    outlets, appliances, or your panel. Water and electricity together are the real emergency —
    if in doubt, call an electrician or your utility first.</li>
    <li>Move what's salvageable up and off the floor; take photos for your records.</li>
    <li>Check whether your <a href="/sump-pump-installation-repair/">sump pump</a> is running,
    plugged in, and discharging outside.</li>
  </ul>
</section>
<section>
  <h2>Why a dry basement floods after a storm</h2>
  <p>The pattern is familiar across Orange County: the basement is fine for months, then a
  heavy rain — a summer thunderstorm cell, a nor'easter, the spring thaw — and there's water
  on the floor. The usual causes:</p>
  <ul>
    <li><strong>Hydrostatic pressure:</strong> saturated soil pushes groundwater up through
    the floor-wall joint and floor cracks. This is the #1 cause of "it only happens in big
    rain" basements.</li>
    <li><strong>Surface water:</strong> clogged gutters, downspouts dumping at the foundation,
    or soil graded toward the house sending roof water straight down the wall.</li>
    <li><strong>A crack or joint that's opened up</strong> — water takes the path it found
    last time, and widens it.</li>
    <li><strong>Sump pump failure or an overwhelmed pump</strong> — see
    <a href="/sump-pump-failure-what-to-do/">what to do when a sump pump fails</a>.</li>
  </ul>
  <p>Which one you have decides the fix — and the price. Surface-water problems are sometimes
  solved with gutters and grading. Hydrostatic pressure usually calls for an
  <a href="/basement-waterproofing-orange-county-ny/">interior drainage system</a>. An honest
  contractor will tell you which problem you actually have before selling you anything.</p>
</section>
"""
PAGES.append(svc_page("basement-water-after-rain",
    "Basement Water After Rain in Orange County, NY | " + BIZ_PLAIN,
    "Water in the basement after heavy rain in Orange County, NY? What causes it, what to do now, and a free estimate from one local specialist.",
    "Basement water after rain",
    "The storm passed and left water on your basement floor. Here's what that pattern usually means — and what fixes it.",
    s, "water", "Request a free estimate for your wet basement",
    toggle="/es/agua-en-el-sotano-despues-de-la-lluvia/"))

# --- 8. Foundation crack repair cost ---
s = """
<section>
  <h2>The typical range</h2>
  <p>For a standard leaking crack in a poured-concrete wall, <strong>crack injection
  typically runs about $400–$1,500 per crack</strong>. That's a typical market range
  published for this kind of work — not a quote for your house. Only a contractor who has
  seen your crack can price your job.</p>
</section>
<section>
  <h2>What moves the price</h2>
  <ul>
    <li><strong>Crack type:</strong> a single vertical shrinkage crack is the simple end.
    Horizontal or stair-step cracks suggest movement, and movement changes the job.</li>
    <li><strong>Water:</strong> a dry cosmetic crack and a crack that's actively leaking are
    different repairs.</li>
    <li><strong>Access:</strong> finished walls, stored belongings, and tight spaces add labor.</li>
    <li><strong>What's behind it:</strong> if the crack is a symptom of a bowing wall or
    settling, sealing it alone won't hold — the structural work is the real job, and
    structural and waterproofing projects typically run in the <strong>$5,000–$15,000</strong>
    range. A good specialist will tell you plainly which situation you're in.</li>
  </ul>
  <p>The estimate itself is free through this service, so the honest way to price your crack
  is to have it looked at. Read more about the repair itself on our
  <a href="/foundation-crack-repair/">foundation crack repair</a> page.</p>
</section>
"""
PAGES.append(svc_page("foundation-crack-repair-cost",
    "Foundation Crack Repair Cost in Orange County, NY | " + BIZ_PLAIN,
    "What does foundation crack repair cost? Typical crack injection range $400–$1,500 per crack, what moves the price, and when a crack means a bigger job.",
    "Foundation crack repair cost",
    "What crack repair typically costs, what changes the number, and when a cheap crack is actually a symptom of an expensive problem.",
    s, "cracks", "Get your free crack repair estimate",
    toggle="/es/costo-reparacion-de-grietas-en-cimientos/"))

# --- 9. Basement waterproofing cost ---
s = """
<section>
  <h2>The typical range</h2>
  <p>A full interior basement waterproofing system — perimeter drainage channel, sump pit
  and pump, discharge line — <strong>typically runs about $5,000–$15,000</strong> for most
  homes. Structural foundation work falls in a similar band. These are typical market ranges
  for this kind of work, published for general information — not quotes. Your price depends
  on your house, and only an in-person estimate can give it.</p>
</section>
<section>
  <h2>What moves the price</h2>
  <ul>
    <li><strong>Linear feet:</strong> waterproofing is priced largely by how much of the
    perimeter gets the drainage system — one leaking wall costs less than all four.</li>
    <li><strong>The sump setup:</strong> pump size, a second pump, and battery backup add to
    the total — and the backup is what keeps a storm outage from undoing the whole system.</li>
    <li><strong>Foundation type and access:</strong> stone, block, and poured walls each
    change the labor; finished basements cost more to open and restore.</li>
    <li><strong>How much is water, how much is structure:</strong> a drainage problem is one
    job; a drainage problem plus a bowing wall is two.</li>
  </ul>
  <p>One honest note: if a contractor quotes you a full system for a problem that gutters and
  grading would fix, that's the wrong contractor. The specialists we connect you with do free
  in-person estimates — get the diagnosis before you judge the price. More on the work itself:
  <a href="/basement-waterproofing-orange-county-ny/">basement waterproofing</a>.</p>
</section>
"""
PAGES.append(svc_page("basement-waterproofing-cost",
    "Basement Waterproofing Cost in Orange County, NY | " + BIZ_PLAIN,
    "What does basement waterproofing cost? Typical range $5,000–$15,000 for interior drainage systems, what moves the price, and free in-person estimates.",
    "Basement waterproofing cost",
    "Typical ranges for interior drainage and sump systems, the factors that move the number, and how to get a real price for your house: a free estimate.",
    s, "water", "Get your free waterproofing estimate"))

# --- 10. Wet basement smell / mold ---
s = """
<section>
  <h2>The smell is a symptom</h2>
  <p>That musty, earthy smell in a basement almost always means one thing: moisture is getting
  in — through the floor, the walls, a crack, or the air itself in a humid Hudson Valley
  summer. You don't always see standing water. Damp block, a wet floor-wall joint, or a crawl
  space breathing into the house is enough to keep the smell (and the mold growth that comes
  with it) going.</p>
</section>
<section>
  <h2>An honest note about mold itself</h2>
  <p>In New York State, mold assessment and mold remediation must be performed by professionals
  licensed for that work. We are a referral service for foundation and waterproofing — we don't
  assess or remediate mold, and neither does a waterproofing estimate. What a waterproofing
  specialist <em>can</em> do is find and stop the water that's feeding the problem, which is
  the step that keeps mold from coming back after any cleanup.</p>
</section>
<section>
  <h2>Where to start</h2>
  <p>Start with the water. If the basement smells musty, check for the usual sources: water
  stains at the floor line, white efflorescence crust on walls, a sump pit that's always wet,
  damp cardboard and stored items. Then get the moisture source diagnosed — that's the free
  estimate this service connects you with.</p>
</section>
"""
PAGES.append(svc_page("wet-basement-smell-mold",
    "Wet Basement Smell &amp; Mold in Orange County, NY | " + BIZ_PLAIN,
    "Musty basement smell in Orange County, NY? It's a moisture problem first. What causes it, the NY mold licensing rule, and a free waterproofing estimate.",
    "Wet basement smell &amp; mold",
    "A musty basement is telling you water is getting in somewhere. Find the water first — here's how that works.",
    s, "mold", "Request a free moisture diagnosis estimate"))

# --- 11. Sump pump failure ---
s = """
<section>
  <h2>While it's failing</h2>
  <ol>
    <li><strong>Mind the electricity.</strong> Don't stand in water to reach plugs or the
    panel. If water is near outlets or appliances, treat it as an electrical hazard first.</li>
    <li><strong>Check the simple things</strong> (from dry footing): is the pump plugged in?
    Did the breaker or GFCI trip? Is the float switch stuck against the pit wall or tangled?</li>
    <li><strong>Check the discharge:</strong> is the outside line blocked, frozen, or
    disconnected — pumping water right back against the house?</li>
    <li><strong>Bail or borrow time:</strong> a utility pump or a wet/dry vacuum can hold the
    line while you get help; move valuables and storage up off the floor.</li>
  </ol>
</section>
<section>
  <h2>Why pumps fail at the worst moment</h2>
  <p>Pumps fail during storms because storms are when they work hardest — and when power
  flickers. The common causes: a worn-out switch (the part that fails most), a pump at the
  end of its roughly 7–10 year life, a clogged intake, or an outage with no battery backup.
  If yours failed in the last storm, the pattern will repeat in the next one.</p>
  <p>A specialist can replace the pump, fix the discharge, and — the upgrade that prevents
  the repeat — add a <a href="/sump-pump-installation-repair/">battery backup pump</a> that
  keeps working when the power doesn't.</p>
</section>
"""
PAGES.append(svc_page("sump-pump-failure-what-to-do",
    "Sump Pump Failure: What To Do | Orange County, NY | " + BIZ_PLAIN,
    "Sump pump failed during a storm in Orange County, NY? Immediate steps, common causes, and a free estimate for replacement or battery backup.",
    "Sump pump failure: what to do",
    "The pump quit mid-storm and the water is rising. Do these things first — then fix it so the next storm goes differently.",
    s, "sump", "Request a free sump pump estimate"))

# --- 12. Signs of foundation settling ---
s = """
<section>
  <h2>The classic settling checklist</h2>
  <ul>
    <li>Doors and windows that suddenly stick, or won't latch</li>
    <li>Cracks in drywall, especially diagonal ones running from door and window corners</li>
    <li>Floors that slope, or gaps opening between the floor and the baseboards</li>
    <li>Stair-step cracks in exterior brick or block, and cracks in the foundation itself</li>
    <li>A chimney or porch pulling away from the house</li>
    <li>Nails popping and trim separating in rooms that were fine before</li>
  </ul>
</section>
<section>
  <h2>Settling vs. a house just being old</h2>
  <p>Almost every house settles a little in its first years, and old houses in Newburgh,
  Middletown, and Port Jervis have had a century to find their level — a hairline crack that
  hasn't moved in a decade is usually just history. Settling that matters is
  <strong>uneven and ongoing</strong>: one corner dropping, cracks that keep growing, doors
  that get worse season by season. The pattern to respect is change.</p>
  <p>Orange County's mix of soils — including clay that swells when wet and shrinks in dry
  spells — can move a foundation a little every year. A specialist can measure whether your
  house is still moving and, if it is, explain the support options. The inspection and
  estimate are free.</p>
</section>
"""
PAGES.append(svc_page("signs-of-foundation-settling",
    "Signs of Foundation Settling | Orange County, NY | " + BIZ_PLAIN,
    "Signs of foundation settling: sticking doors, sloping floors, stair-step cracks. What matters, what doesn't, and a free estimate in Orange County, NY.",
    "Signs of foundation settling",
    "Sticking doors, sloping floors, cracks that keep growing — how to tell normal aging from a foundation that's still moving.",
    s, "floors", "Request a free settling inspection estimate"))

# =====================================================================
# SPANISH PAGES (full translations of the corresponding English pages)
# =====================================================================

def svc_page_es(path, title, desc, h1, lede, sections, default_problem,
                form_intro, en_counterpart):
    body = f"""
{disclosure("es")}
{sections}
<section>
  <h2>{form_intro}</h2>
  {short_form("es", default_problem, "sf-es-" + path.split("/")[-1][:10])}
</section>
"""
    return (path + "/index.html", render("es", title, desc, en_counterpart,
            body, hero_h1=h1, hero_lede=lede))

# --- ES 1. Reparación de cimientos (= foundation repair hub) ---
s = """
<section>
  <h2>Los problemas de cimientos no se curan solos</h2>
  <p>Una grieta en los cimientos, una pared que se comba, un piso que empezó a inclinarse: es la
  casa avisando que algo cambió debajo de ella. En el condado de Orange, las causas habituales son
  el agua y el suelo: la lluvia fuerte de primavera y el deshielo saturan la tierra, los suelos con
  mucha arcilla en partes del condado se hinchan y empujan, y los ciclos de hielo y deshielo abren
  las grietas un poco más cada año.</p>
  <p>Las casas aquí son muy variadas. En Newburgh, Middletown y Port Jervis muchas casas se apoyan
  en cimientos de piedra o de bloques de concreto de hace un siglo. Las casas de la posguerra en
  New Windsor, Monroe y los suburbios de Middletown son de bloques o de concreto vaciado. La
  reparación correcta es distinta en cada caso, y por eso una reparación seria empieza con alguien
  que vea sus cimientos en persona, no con un precio por teléfono.</p>
</section>
<section>
  <h2>Señales que merecen atención</h2>
  <ul>
    <li><strong>Grietas en los cimientos:</strong> verticales, horizontales o en escalera — y cuáles
    son estructurales.</li>
    <li><strong>Paredes del sótano combadas:</strong> una pared que se curva hacia adentro por la
    presión del suelo es un problema estructural, no cosmético.</li>
    <li><strong>Asentamiento y pisos inclinados:</strong> puertas que se atascan, grietas en el
    yeso, pisos que se inclinan.</li>
  </ul>
</section>
<section>
  <h2>Qué hace un especialista en cimientos</h2>
  <p>Según lo que encuentre, un contratista de cimientos puede sellar e inyectar grietas, estabilizar
  una pared combada con anclajes o refuerzos, o apoyar una sección de la casa que se está asentando.
  El método correcto depende del tipo de cimiento, del suelo y de cuánto ha avanzado el problema.
  Esa es la decisión del contratista tras una inspección en persona — y la inspección y la
  cotización son gratuitas a través de este servicio.</p>
</section>
"""
PAGES.append(svc_page_es("es/reparacion-de-cimientos",
    "Reparación de Cimientos en el Condado de Orange, NY | " + BIZ_PLAIN,
    "Conéctese con un especialista local independiente en reparación de cimientos en el condado de Orange, NY. Grietas, paredes combadas, asentamiento. Cotización gratuita.",
    "Reparación de cimientos en el condado de Orange, NY",
    "¿Grietas, paredes combadas o una casa que se está asentando? Conectamos a propietarios del condado de Orange con un especialista local independiente para una cotización gratuita.",
    s, "cracks", "Pida una cotización gratuita de cimientos",
    "/foundation-repair-orange-county-ny/"))

# --- ES 2. Impermeabilización de sótanos (= waterproofing hub / ES hub) ---
s = f"""
<section>
  <h2>Por qué se mojan los sótanos del condado de Orange</h2>
  <p>La mayoría de los sótanos mojados aquí no son un misterio. El condado recibe lluvia fuerte de
  primavera sobre el deshielo, aguaceros de verano y tormentas del noreste en otoño, y mucha de esa
  agua termina contra las paredes de los cimientos. Las casas cerca del río Wallkill, del arroyo
  Moodna y de las zonas bajas junto al Hudson y al Delaware además lidian con niveles altos de agua
  subterránea. Cuando el suelo alrededor de sus cimientos está saturado, el agua busca la entrada
  más fácil: las juntas entre el piso y la pared, las grietas y los bloques porosos.</p>
</section>
<section>
  <h2>En qué consiste la impermeabilización de verdad</h2>
  <p>La impermeabilización real de un sótano suele ser un <strong>sistema de drenaje interior</strong>:
  un canal instalado a lo largo del perímetro interior de los cimientos que recoge el agua antes de
  que se extienda por el piso y la lleva a una <strong>bomba de sumidero</strong>, que la saca fuera
  y lejos de la casa. La nivelación del terreno, las canaletas y las extensiones de los bajantes
  también importan: un buen contratista le dirá si parte de su problema se puede resolver desde
  afuera antes de venderle un sistema.</p>
</section>
<section>
  <h2>Por dónde empezar</h2>
  <div class="cards">
    <div class="card"><h3><a href="/es/agua-en-el-sotano-despues-de-la-lluvia/">Agua después de la lluvia</a></h3>
    <p>Sótano seco, tormenta grande, piso mojado. Qué suele significar ese patrón.</p></div>
    <div class="card"><h3><a href="/es/costo-reparacion-de-grietas-en-cimientos/">Costo de reparar grietas</a></h3>
    <p>Rangos de precios típicos y honestos para la reparación de grietas.</p></div>
    <div class="card"><h3><a href="/es/reparacion-de-cimientos/">Reparación de cimientos</a></h3>
    <p>Grietas, paredes combadas, asentamiento: el lado estructural de la casa.</p></div>
    <div class="card"><h3><a href="/get-help/">Pedir ayuda</a></h3>
    <p>El formulario de solicitud: una solicitud, un contratista local, una cotización gratuita.</p></div>
  </div>
</section>
<section>
  <h2>Cuándo actuar</h2>
  <p>Que entre agua una vez tras una tormenta excepcional merece observación. Que entre agua cada
  primavera, charcos que vuelven siempre a la misma esquina, eflorescencia (la costra blanca) en las
  paredes o un sumidero que trabaja sin parar: eso es un patrón, y los patrones empeoran, no mejoran.
  Una cotización gratuita le cuesta una hora y le dice a cuál de los dos casos se enfrenta.</p>
  {zip_checker("es", "zc-es-hub")}
</section>
"""
PAGES.append(svc_page_es("es/impermeabilizacion-de-sotanos",
    "Impermeabilización de Sótanos en el Condado de Orange, NY | " + BIZ_PLAIN,
    "¿Sótano mojado en el condado de Orange, NY? Conéctese con un especialista local independiente en impermeabilización. Drenaje interior, bombas de sumidero, cotización gratuita.",
    "Impermeabilización de sótanos en el condado de Orange, NY",
    "Un sótano que se inunda cada primavera no es mala suerte: es el agua haciendo lo que hace el agua. Le conectamos con un especialista local independiente para una cotización gratuita.",
    s, "water", "Pida una cotización gratuita de impermeabilización",
    "/basement-waterproofing-orange-county-ny/"))

# --- ES 3. Agua en el sótano después de la lluvia (= basement water after rain) ---
s = """
<section>
  <h2>Primero, ahora mismo</h2>
  <ul>
    <li><strong>No se meta en agua estancada</strong> si puede estar en contacto con enchufes,
    electrodomésticos o su panel eléctrico. El agua y la electricidad juntas sí son la verdadera
    emergencia: ante la duda, llame primero a un electricista o a su compañía eléctrica.</li>
    <li>Suba lo que se pueda salvar y sáquelo del piso; tome fotos para su registro.</li>
    <li>Revise si su bomba de sumidero está funcionando, enchufada y descargando hacia afuera.</li>
  </ul>
</section>
<section>
  <h2>Por qué un sótano seco se inunda tras una tormenta</h2>
  <p>El patrón es conocido en todo el condado de Orange: el sótano está bien durante meses y, tras
  una lluvia fuerte — una tormenta de verano, una tormenta del noreste, el deshielo de primavera —
  hay agua en el piso. Las causas habituales:</p>
  <ul>
    <li><strong>Presión hidrostática:</strong> el suelo saturado empuja el agua subterránea hacia
    arriba por la junta entre el piso y la pared y por las grietas del piso. Es la causa número uno
    de los sótanos que "solo se mojan con lluvias grandes".</li>
    <li><strong>Agua de superficie:</strong> canaletas tapadas, bajantes que descargan junto a los
    cimientos o tierra nivelada hacia la casa llevan el agua del techo directo contra la pared.</li>
    <li><strong>Una grieta o junta que se abrió:</strong> el agua toma el camino que encontró la
    última vez, y lo ensancha.</li>
    <li><strong>Falla de la bomba de sumidero o una bomba sobrepasada</strong> por el volumen de agua.</li>
  </ul>
  <p>Cuál de estas causas tenga decide la solución — y el precio. Los problemas de agua de superficie
  a veces se resuelven con canaletas y nivelación. La presión hidrostática suele requerir un sistema
  de drenaje interior. Un contratista honesto le dirá qué problema tiene usted en realidad antes de
  venderle nada.</p>
</section>
"""
PAGES.append(svc_page_es("es/agua-en-el-sotano-despues-de-la-lluvia",
    "Agua en el Sótano Después de la Lluvia | Condado de Orange, NY | " + BIZ_PLAIN,
    "¿Agua en el sótano después de una lluvia fuerte en el condado de Orange, NY? Causas, qué hacer ahora y una cotización gratuita de un especialista local.",
    "Agua en el sótano después de la lluvia",
    "La tormenta pasó y dejó agua en el piso de su sótano. Esto es lo que suele significar ese patrón, y lo que lo soluciona.",
    s, "water", "Pida una cotización gratuita para su sótano mojado",
    "/basement-water-after-rain/"))

# --- ES 4. Costo reparación de grietas en cimientos (= crack repair cost) ---
s = """
<section>
  <h2>El rango típico</h2>
  <p>Para una grieta estándar que filtra agua en una pared de concreto vaciado, <strong>la inyección
  de grietas suele costar entre $400 y $1,500 por grieta</strong>. Es un rango típico de mercado
  publicado para este tipo de trabajo, no una cotización para su casa. Solo un contratista que haya
  visto su grieta puede ponerle precio a su trabajo.</p>
</section>
<section>
  <h2>Qué cambia el precio</h2>
  <ul>
    <li><strong>Tipo de grieta:</strong> una sola grieta vertical por contracción es el caso simple.
    Las grietas horizontales o en escalera sugieren movimiento, y el movimiento cambia el trabajo.</li>
    <li><strong>Agua:</strong> una grieta cosmética y seca y una grieta que filtra agua activamente
    son reparaciones distintas.</li>
    <li><strong>Acceso:</strong> paredes acabadas, cosas almacenadas y espacios estrechos añaden mano
    de obra.</li>
    <li><strong>Lo que hay detrás:</strong> si la grieta es síntoma de una pared combada o de
    asentamiento, sellarla sola no aguantará: el trabajo estructural es el trabajo real, y los
    proyectos estructurales y de impermeabilización suelen estar en el rango de
    <strong>$5,000 a $15,000</strong>. Un buen especialista le dirá con claridad en qué situación
    está usted.</li>
  </ul>
  <p>La cotización en sí es gratuita a través de este servicio, así que la manera honesta de saber el
  precio de su grieta es que alguien la vea. Lea más sobre la reparación en nuestra página de
  <a href="/es/reparacion-de-cimientos/">reparación de cimientos</a>.</p>
</section>
"""
PAGES.append(svc_page_es("es/costo-reparacion-de-grietas-en-cimientos",
    "Costo de Reparación de Grietas en Cimientos | Condado de Orange, NY | " + BIZ_PLAIN,
    "¿Cuánto cuesta reparar una grieta en los cimientos? Rango típico de inyección: $400–$1,500 por grieta. Qué cambia el precio y cuándo una grieta indica un trabajo mayor.",
    "Costo de reparación de grietas en cimientos",
    "Lo que suele costar reparar una grieta, qué cambia el número y cuándo una grieta barata es en realidad el síntoma de un problema caro.",
    s, "cracks", "Pida su cotización gratuita de reparación de grietas",
    "/foundation-crack-repair-cost/"))

# =====================================================================
# WRITE OUT
# =====================================================================

count = 0
for rel, html in PAGES:
    dest = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print("wrote", rel)

with open(os.path.join(BASE, "CNAME"), "w", encoding="utf-8") as f:
    f.write("ocfoundationconnect.com\n")

print("TOTAL PAGES:", count)
