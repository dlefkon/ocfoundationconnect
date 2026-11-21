/* =====================================================================
   Orange County Foundation & Basement Connect — shared site script
   No external dependencies. Plain JavaScript.
   ===================================================================== */

/* ---------------------------------------------------------------------
   CONFIG — go-live placeholders (David's go required for each)

   TRACKING_PHONE: Twilio call-tracking number, not yet purchased.
     - While empty: every "call" button links to the request form
       (/get-help/) instead of dialing, and no phone number is shown
       anywhere on the site. Button text stays "Call for a free estimate".
     - When set (e.g. "+18455550100"): call buttons become tel: links
       and the number is displayed next to the button text.

   FORM_ENDPOINT: form backend URL (FormSubmit AJAX endpoint, wired
     Nov 21, 2026). Submissions are emailed to CONTACT_EMAIL.
     - If emptied again: submitting a form shows an honest notice that
       online requests are not live yet. Nothing is sent, nothing is
       faked, and the visitor is pointed to the contact email.

   CONTACT_EMAIL: contact@ocfoundationconnect.com — to be activated
     when the domain's mail is set up at deploy time.
   --------------------------------------------------------------------- */
var CONFIG = {
  TRACKING_PHONE: "",
  FORM_ENDPOINT: "https://formsubmit.co/ajax/contact@ocfoundationconnect.com",
  CONTACT_EMAIL: "contact@ocfoundationconnect.com"
};

/* ---------------------------------------------------------------------
   Orange County, NY ZIP codes — service area for the ZIP checker.
   Source (verified Nov 18, 2026): ZIP-Codes.com, "ZIP Codes for
   Orange County, NY" (56 ZIPs; data from U.S. Census Bureau ACS 2024
   5-Year Estimates, updated Nov 1, 2026) —
   https://www.zip-codes.com/county/ny-orange.asp
   Includes standard and PO Box ZIPs assigned to Orange County.
   Note: a few of these ZIPs also reach across county lines; the
   contractor confirms the exact address when they call.
   --------------------------------------------------------------------- */
var ORANGE_COUNTY_ZIPS = [
  "10910", "10912", "10914", "10915", "10916", "10917", "10918", "10919",
  "10921", "10922", "10924", "10925", "10926", "10928", "10930", "10932",
  "10933", "10940", "10941", "10949", "10950", "10953", "10958", "10959",
  "10963", "10969", "10973", "10975", "10979", "10981", "10985", "10987",
  "10988", "10990", "10992", "10996", "10997", "10998",
  "12518", "12520", "12543", "12549", "12550", "12551", "12552", "12553",
  "12555", "12566", "12575", "12577", "12584", "12586",
  "12729", "12746", "12771", "12780"
];

/* Problem tags shared by the symptom picker and the lead form. */
var PROBLEM_INFO = {
  en: {
    cracks: {
      label: "Wall cracks",
      text: "Cracks in a foundation wall often come from the concrete curing, the house settling, or pressure from wet soil outside the wall. A crack that leaks, keeps growing, or runs horizontally is the kind a specialist should look at in person."
    },
    water: {
      label: "Water in the basement",
      text: "Water after rain usually means groundwater is pushing through the floor or wall joints, or surface water is getting in around the foundation. The fix depends on where it enters, which is why an in-person look matters before anyone quotes a price."
    },
    bowing: {
      label: "Bowing or leaning walls",
      text: "A basement wall that bows inward is usually being pushed by saturated soil outside it — common after wet springs and freeze-thaw cycles here. This is a structural issue, not a cosmetic one, and it does not fix itself."
    },
    mold: {
      label: "Musty smell or mold",
      text: "A musty basement almost always means moisture is getting in somewhere, even if you never see standing water. The lasting fix is stopping the water first; in New York, mold assessment and remediation itself must be done by a licensed mold professional."
    },
    floors: {
      label: "Sloping or uneven floors",
      text: "Floors that slope, bounce, or pull away from the wall can mean the foundation or the supports under the house are settling unevenly. It can also be ordinary aging in an older home — only an in-person check can tell the difference."
    }
  },
  es: {
    cracks: {
      label: "Grietas en las paredes",
      text: "Las grietas en una pared de cimientos suelen venir del curado del concreto, del asentamiento de la casa o de la presión del suelo mojado contra la pared. Una grieta que filtra agua, sigue creciendo o va en horizontal es de las que un especialista debe ver en persona."
    },
    water: {
      label: "Agua en el sótano",
      text: "El agua después de la lluvia suele significar que el agua subterránea entra por el piso o las juntas de la pared, o que el agua de la superficie entra junto a los cimientos. La solución depende de por dónde entra, y por eso hace falta una visita en persona antes de dar un precio."
    },
    bowing: {
      label: "Paredes combadas o inclinadas",
      text: "Una pared del sótano que se comba hacia adentro suele estar empujada por el suelo saturado de afuera, algo común tras primaveras lluviosas y ciclos de hielo y deshielo aquí. Es un problema estructural, no cosmético, y no se arregla solo."
    },
    mold: {
      label: "Olor a humedad o moho",
      text: "Un sótano con olor a humedad casi siempre significa que el agua entra por algún sitio, aunque nunca se vea agua estancada. La solución duradera es detener el agua primero; en Nueva York, la evaluación y la remediación del moho deben hacerlas un profesional con licencia para moho."
    },
    floors: {
      label: "Pisos inclinados o desnivelados",
      text: "Los pisos que se inclinan, rebotan o se separan de la pared pueden indicar que los cimientos o los apoyos bajo la casa se están asentando de forma desigual. También puede ser el envejecimiento normal de una casa vieja: solo una revisión en persona puede notar la diferencia."
    }
  }
};

var STRINGS = {
  en: {
    zipInvalid: "Please enter a 5-digit ZIP code.",
    zipIn: function (zip) {
      return "Good news — ZIP " + zip + " is in our Orange County service area. " +
        "Fill out the request form and one independent local specialist will get it.";
    },
    zipOut: function (zip) {
      return "ZIP " + zip + " is outside the Orange County, NY area this service covers, " +
        "so we can't route a request for it. If the home is actually in Orange County, " +
        "double-check the ZIP — a few ZIP codes cross county lines.";
    },
    formNotLive: "Online requests open soon — this form is not yet live, and nothing was sent. " +
      "Please check back shortly, or reach us at " + CONFIG.CONTACT_EMAIL + ".",
    formSending: "Sending your request…",
    formSuccess: "Thank you — your request was sent. One independent local specialist will " +
      "call you back at the number you gave. If you don't hear back within one business day, " +
      "reach us at " + CONFIG.CONTACT_EMAIL + ".",
    formError: "Something went wrong and your request was not sent. Please try again, " +
      "or reach us at " + CONFIG.CONTACT_EMAIL + ".",
    pickerCta: "Request a free estimate for this problem",
    taggedAs: "Problem selected:"
  },
  es: {
    zipInvalid: "Ingrese un código postal de 5 dígitos.",
    zipIn: function (zip) {
      return "Buenas noticias: el código " + zip + " está dentro de nuestra zona de servicio del condado de Orange. " +
        "Complete el formulario de solicitud y lo recibirá un especialista local independiente.";
    },
    zipOut: function (zip) {
      return "El código " + zip + " está fuera de la zona del condado de Orange, NY que cubre este servicio, " +
        "así que no podemos enviar una solicitud para esa zona. Si la casa sí está en el condado de Orange, " +
        "revise el código: algunos códigos postales cruzan los límites del condado.";
    },
    formNotLive: "Las solicitudes en línea abren pronto: este formulario aún no está activo y no se envió nada. " +
      "Vuelva a intentarlo en breve o escríbanos a " + CONFIG.CONTACT_EMAIL + ".",
    formSending: "Enviando su solicitud…",
    formSuccess: "Gracias: su solicitud fue enviada. Un especialista local independiente le " +
      "llamará al número que indicó. Si no recibe respuesta en un día hábil, " +
      "escríbanos a " + CONFIG.CONTACT_EMAIL + ".",
    formError: "Algo salió mal y su solicitud no fue enviada. Inténtelo de nuevo " +
      "o escríbanos a " + CONFIG.CONTACT_EMAIL + ".",
    pickerCta: "Pedir una cotización gratuita para este problema",
    taggedAs: "Problema seleccionado:"
  }
};

(function () {
  "use strict";

  var lang = (document.documentElement.lang || "en").toLowerCase().indexOf("es") === 0 ? "es" : "en";
  var S = STRINGS[lang];
  var GET_HELP = lang === "es" ? "/get-help/" : "/get-help/";

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  /* ---------- Call buttons (tracking number pending) ---------- */
  $$(".call-btn").forEach(function (btn) {
    if (CONFIG.TRACKING_PHONE) {
      btn.setAttribute("href", "tel:" + CONFIG.TRACKING_PHONE);
      var num = document.createElement("span");
      num.className = "call-num";
      num.textContent = " — " + CONFIG.TRACKING_PHONE;
      btn.appendChild(num);
    } else {
      btn.setAttribute("href", GET_HELP);
    }
  });

  /* ---------- Footer year ---------- */
  var yr = $("[data-year]");
  if (yr) { yr.textContent = String(new Date().getFullYear()); }

  /* ---------- Service-area ZIP checker ---------- */
  $$(".zip-checker").forEach(function (form) {
    var input = $("input[name='zip']", form);
    var result = $(".tool-result", form.parentNode) || $(".tool-result", form);
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!input || !result) { return; }
      var zip = (input.value || "").replace(/\D/g, "").slice(0, 5);
      result.innerHTML = "";
      var box = document.createElement("div");
      if (!/^\d{5}$/.test(zip)) {
        box.className = "result-out";
        box.textContent = S.zipInvalid;
      } else if (ORANGE_COUNTY_ZIPS.indexOf(zip) !== -1) {
        box.className = "result-ok";
        var p = document.createElement("p");
        p.textContent = S.zipIn(zip);
        box.appendChild(p);
        var a = document.createElement("a");
        a.className = "btn btn-accent";
        a.href = GET_HELP + "?zip=" + encodeURIComponent(zip);
        a.textContent = S.pickerCta;
        box.appendChild(a);
      } else {
        box.className = "result-out";
        box.textContent = S.zipOut(zip);
      }
      result.appendChild(box);
      box.setAttribute("tabindex", "-1");
      box.focus({ preventScroll: false });
    });
  });

  /* ---------- Symptom picker ---------- */
  $$(".symptom-picker").forEach(function (picker) {
    var buttons = $$(".picker-btn", picker);
    var out = $(".picker-output", picker);
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
        btn.setAttribute("aria-pressed", "true");
        var key = btn.getAttribute("data-symptom");
        var info = PROBLEM_INFO[lang][key];
        if (!info || !out) { return; }
        out.innerHTML = "";
        var h = document.createElement("h3");
        h.textContent = info.label;
        var p = document.createElement("p");
        p.textContent = info.text;
        var a = document.createElement("a");
        a.className = "btn btn-accent";
        a.href = GET_HELP + "?problem=" + encodeURIComponent(key);
        a.textContent = S.pickerCta;
        out.appendChild(h);
        out.appendChild(p);
        out.appendChild(a);
      });
    });
  });

  /* ---------- Lead forms ---------- */
  $$(".lead-form").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      /* Honeypot: a filled honeypot means a bot — quietly stop. */
      var hp = $("input[name='company_website']", form);
      if (hp && hp.value) { ev.preventDefault(); return; }
      ev.preventDefault();
      var notice = $(".form-notice", form);
      if (!notice) {
        notice = document.createElement("div");
        notice.className = "form-notice";
        notice.setAttribute("role", "status");
        form.appendChild(notice);
      }
      function showNotice(text) {
        notice.textContent = text;
        notice.setAttribute("tabindex", "-1");
        notice.focus({ preventScroll: false });
      }
      if (!CONFIG.FORM_ENDPOINT) {
        showNotice(S.formNotLive);
        return;
      }
      /* Post the lead to the form backend (FormSubmit AJAX) as JSON and
         keep the visitor on the page. TrustedForm certificate URL (see
         the commented placeholder in the form markup) joins the payload
         when that account is active. */
      var data = {};
      new FormData(form).forEach(function (value, key) {
        if (key === "company_website") { return; }
        data[key] = value;
      });
      data._subject = "New estimate request — ocfoundationconnect.com";
      data._template = "table";
      data._captcha = "false";
      var btn = $("button[type='submit']", form);
      if (btn) { btn.disabled = true; }
      showNotice(S.formSending);
      fetch(CONFIG.FORM_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (res) {
        if (!res.ok) { throw new Error("form backend " + res.status); }
        form.reset();
        showNotice(S.formSuccess);
      }).catch(function () {
        showNotice(S.formError);
      }).then(function () {
        if (btn) { btn.disabled = false; }
      });
    });
  });

  /* ---------- /get-help/ prefill from ZIP checker / symptom picker --- */
  var params = new URLSearchParams(window.location.search);
  var zipParam = params.get("zip");
  var problemParam = params.get("problem");
  if (zipParam || problemParam) {
    $$(".lead-form").forEach(function (form) {
      if (zipParam) {
        var z = $("input[name='zip']", form);
        if (z) { z.value = zipParam.replace(/\D/g, "").slice(0, 5); }
      }
      if (problemParam && PROBLEM_INFO[lang][problemParam]) {
        var sel = $("select[name='problem']", form);
        if (sel) { sel.value = problemParam; }
        var tag = $(".problem-tag", form);
        if (tag) {
          tag.hidden = false;
          tag.innerHTML = "";
          tag.appendChild(document.createTextNode(S.taggedAs + " "));
          var chip = document.createElement("span");
          chip.className = "tag-chip";
          chip.textContent = PROBLEM_INFO[lang][problemParam].label;
          tag.appendChild(chip);
        }
      }
    });
  }
})();
