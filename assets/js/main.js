/* HER Consulting LLC — site interactions */
(function () {
  "use strict";

  /* ---------- Sticky header shadow ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.querySelector(".nav__menu");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    });

    // Accordion behaviour for dropdowns on small screens
    menu.querySelectorAll(".nav__item--has-menu > .nav__link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (window.matchMedia("(max-width: 1020px)").matches) {
          e.preventDefault();
          link.parentElement.classList.toggle("is-open");
        }
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealables = document.querySelectorAll(".reveal");
  if (revealables.length) {
    if (!("IntersectionObserver" in window)) {
      revealables.forEach(function (el) { el.classList.add("is-visible"); });
    } else {
      var revealObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry, i) {
            if (!entry.isIntersecting) return;
            var el = entry.target;
            var delay = parseInt(el.dataset.delay || "0", 10) || i * 70;
            setTimeout(function () { el.classList.add("is-visible"); }, delay);
            revealObserver.unobserve(el);
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
      );
      revealables.forEach(function (el) { revealObserver.observe(el); });
    }
  }

  /* ---------- Subject expert bios: scroll-activated typing ---------- */
  var expertBios = document.querySelectorAll("[data-expert-bio]");
  if (expertBios.length) {
    document.documentElement.classList.add("has-team-scroll");

    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var highlightTerms = [
        "community engagement", "qualitative methodologies", "thematic analysis",
        "health communication products", "public health programs", "population health research",
        "statistical modeling", "demographic methods", "data management", "research capacity",
        "health promotion", "program development", "applied research", "reproductive justice",
        "behavioral health", "health disparities", "community planning", "data analytics",
        "quality-of-life improvements", "quantitative analyst", "evidence-based results",
        "strategic planning", "cybersecurity", "eDiscovery", "epidemiology"
      ];
      highlightTerms.sort(function (a, b) { return b.length - a.length; });
      var termPattern = new RegExp("(" + highlightTerms.join("|") + ")", "gi");

      expertBios.forEach(function (bio) {
        var fullText = bio.textContent;
        var charIndex = 0;
        bio.setAttribute("aria-label", fullText);
        bio.textContent = "";

        fullText.split(termPattern).forEach(function (chunk) {
          var isHighlight = highlightTerms.some(function (term) {
            return term.toLowerCase() === chunk.toLowerCase();
          });
          var container = bio;
          if (isHighlight) {
            container = document.createElement("mark");
            container.className = "expert-highlight";
            container.style.setProperty("--highlight-index", String(charIndex));
            bio.appendChild(container);
          }

          Array.from(chunk).forEach(function (character) {
            if (/\s/.test(character)) {
              container.appendChild(document.createTextNode(character));
            } else {
              var letter = document.createElement("span");
              letter.className = "expert-char";
              letter.style.setProperty("--char-index", String(charIndex));
              letter.textContent = character;
              container.appendChild(letter);
            }
            charIndex += 1;
          });
        });
      });

      if ("IntersectionObserver" in window) {
        var expertObserver = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-typing");
            expertObserver.unobserve(entry.target);
          });
        }, { threshold: 0.2, rootMargin: "0px 0px -30px 0px" });
        expertBios.forEach(function (bio) { expertObserver.observe(bio); });
      } else {
        expertBios.forEach(function (bio) { bio.classList.add("is-typing"); });
      }
    }
  }

  /* ---------- Animated counters ---------- */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    var runCount = function (el) {
      var target = parseFloat(el.dataset.count) || 0;
      var duration = 1600;
      var start = null;
      var step = function (ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased).toLocaleString("en-US");
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    if (!("IntersectionObserver" in window)) {
      counters.forEach(runCount);
    } else {
      var countObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            runCount(entry.target);
            countObserver.unobserve(entry.target);
          });
        },
        { threshold: 0.5 }
      );
      counters.forEach(function (el) { countObserver.observe(el); });
    }
  }

  /* ---------- Partner marquee: duplicate track for a seamless loop ---------- */
  document.querySelectorAll(".marquee__track").forEach(function (track) {
    if (track.dataset.cloned === "true") return;
    track.dataset.cloned = "true";
    track.innerHTML += track.innerHTML;
  });

  /* ---------- Back to top ---------- */
  var toTop = document.querySelector(".to-top");
  if (toTop) {
    var toggleTop = function () {
      toTop.classList.toggle("is-visible", window.scrollY > 700);
    };
    toggleTop();
    window.addEventListener("scroll", toggleTop, { passive: true });
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- Contact form ---------- */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var setError = function (field, on) {
      field.classList.toggle("is-invalid", on);
    };

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;

      form.querySelectorAll("[required]").forEach(function (input) {
        var field = input.closest(".field");
        var ok = input.value.trim() !== "" && (input.type !== "email" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim()));
        setError(field, !ok);
        if (!ok) valid = false;
      });

      if (!valid) {
        form.querySelector(".is-invalid input, .is-invalid textarea").focus();
        return;
      }

      var name = form.elements.name.value.trim();
      var email = form.elements.email.value.trim();
      var subject = form.elements.subject.value.trim();
      var message = form.elements.message.value.trim();

      var body =
        "Name / Company: " + name + "\n" +
        "Email: " + email + "\n\n" +
        (message || "(no message provided)");

      window.location.href =
        "mailto:lola@herconsultingbiz.com" +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent =
          "Opening your email app with the message ready to send. If nothing happens, email lola@herconsultingbiz.com directly.";
      }
    });

    form.querySelectorAll("input, textarea").forEach(function (input) {
      input.addEventListener("input", function () {
        var field = input.closest(".field");
        if (field.classList.contains("is-invalid")) setError(field, false);
      });
    });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
