#!/usr/bin/env python3
"""Build all app-i18n locale JSON files for TVK Partner Portal."""

import json
from pathlib import Path

OUT = Path(__file__).parent / "app-i18n"
OUT.mkdir(parents=True, exist_ok=True)

HREFS = ["/energy-systems", "/infrastructure", "/strategic-partnerships", "/insights"]
EMAILS = ["partners@tvk.group", "invest@tvk.group", "support@tvk.group", "contact@tvk.group"]
STAGE_KEYS = ["development", "development", "active"]


def make_docs(items):
    return [{"title": t, "description": d, "href": h} for (t, d), h in zip(items, HREFS)]


def make_channels(items):
    return [{"title": t, "description": d, "email": e} for (t, d), e in zip(items, EMAILS)]


def make_projects(items):
    return [
        {"title": t, "stage": s, "stageKey": k, "description": d}
        for (t, s, d), k in zip(items, STAGE_KEYS)
    ]


def bundle(header_pp, header_app, footer_pp, app):
    return {
        "header": {"partnerPortal": header_pp, "getApp": header_app},
        "footer": {"partnerPortal": footer_pp},
        "app": app,
    }


LOCALES = {}

LOCALES["en"] = bundle(
    "Partner Portal",
    "Get the App",
    "Partner Portal App →",
    {
        "meta": {
            "title": "Partner Portal",
            "description": "TVK Infrastructure & Energy Systems partner portal — apply for strategic partnerships, track development initiatives, and access capability documents.",
        },
        "brand": "TVK Partner Portal",
        "tagline": "Infrastructure & Energy Systems",
        "backToSite": "Website",
        "navAria": "Partner portal navigation",
        "nav": {"dashboard": "Dashboard", "apply": "Apply", "projects": "Projects", "documents": "Documents", "support": "Support"},
        "dashboard": {
            "title": "Partner Dashboard",
            "subtitle": "Track your partnership inquiry, development initiatives, and next actions within the TVK ecosystem.",
            "stats": [
                {"label": "Partnership Stage", "value": "Development"},
                {"label": "Active Initiatives", "value": "6 Areas"},
                {"label": "Inquiry Status", "value": "Open"},
                {"label": "Portal Languages", "value": "25"},
            ],
            "partnershipStatus": {
                "title": "Strategic Partnership Pipeline",
                "badge": "In Development",
                "description": "TVK Infrastructure & Energy Systems is in a research, development, and partnership-building stage. Submit an application to begin a structured collaboration conversation.",
            },
            "nextSteps": {
                "title": "Recommended Next Steps",
                "items": [
                    "Submit a strategic partnership application with your organization details",
                    "Review capability areas across energy systems and infrastructure technologies",
                    "Explore active development initiatives in the projects section",
                    "Contact our partnerships team for pilot or collaboration opportunities",
                ],
            },
            "cta": "Submit Partnership Application →",
        },
        "apply": {
            "title": "Partnership Application",
            "subtitle": "Apply for strategic collaboration with TVK Infrastructure & Energy Systems.",
            "intro": "Complete this form to introduce your organization and describe your partnership interest. Our team reviews all applications and responds to qualified inquiries.",
            "disclaimer": "This application does not constitute a binding agreement. TVK Infrastructure & Energy Systems LTD is in a development stage — information describes capability areas, not operational commitments.",
        },
        "applyForm": {
            "interestAreas": [
                "Energy Systems", "Infrastructure Technologies", "Industrial Solutions",
                "Energy Intelligence", "AI Infrastructure", "Strategic Partnerships", "General Inquiry",
            ],
            "success": {
                "title": "Application Received",
                "message": "Thank you for your partnership interest. Our team will review your application and respond within 5–10 business days.",
            },
            "fields": {
                "name": "Full Name", "company": "Organization", "role": "Role / Title", "country": "Country",
                "email": "Email", "interest": "Partnership Area",
                "allocation": "Indicative Scope (USD or description)", "message": "Partnership Proposal", "required": "*",
            },
            "placeholders": {
                "name": "Your full name", "company": "Organization name", "role": "Your position",
                "country": "Country of operation", "email": "professional@company.com", "interest": "Select an area",
                "allocation": "e.g. Pilot project, $500K collaboration, technology integration",
                "message": "Describe your organization, strategic fit, and proposed collaboration...",
            },
            "submit": "Submit Partnership Application",
        },
        "projects": {
            "title": "Development Initiatives",
            "subtitle": "Current capability areas and development-stage initiatives within the TVK ecosystem.",
            "items": make_projects([
                ("Energy Systems Integration", "In Development", "Renewable integration, industrial energy solutions, and intelligent energy management frameworks."),
                ("Smart Infrastructure Technologies", "Research", "Digital infrastructure systems, monitoring platforms, and critical infrastructure technology development."),
                ("Industrial AI & Analytics", "Active Research", "Industrial AI, infrastructure analytics, and intelligent automation research for complex operational environments."),
            ]),
        },
        "documents": {
            "title": "Capability Documents",
            "subtitle": "Official capability briefs and reference materials from the corporate website.",
            "openLabel": "Open document",
            "items": make_docs([
                ("Energy Systems Capabilities", "Overview of energy systems development, renewable integration, and energy intelligence."),
                ("Infrastructure Technologies", "Smart infrastructure, digital systems, and critical infrastructure technology development."),
                ("Strategic Partnerships", "Partnership models, collaboration frameworks, and engagement process."),
                ("Insights & Research", "Industry perspectives on energy, infrastructure, and industrial technology."),
            ]),
        },
        "support": {
            "title": "Partner Support",
            "subtitle": "Contact the TVK Infrastructure & Energy Systems team for partnership, technical, and general inquiries.",
            "disclaimer": "For urgent operational matters, contact your assigned partnership representative. Response times: 1–2 business days for general inquiries.",
            "channels": make_channels([
                ("Partnership Inquiries", "Strategic collaboration, pilot opportunities, and long-term partnership development."),
                ("Investor Relations", "Capital formation and strategic investment discussions within the TVK ecosystem."),
                ("Technical Support", "Portal access, application status, and technical questions."),
                ("General Contact", "General inquiries about TVK Infrastructure & Energy Systems."),
            ]),
        },
        "install": {
            "eyebrow": "Partner Portal App",
            "title": "Get the TVK Partner Portal app",
            "subtitle": "Install the partnership portal on your phone — apply, track initiatives, and access capability documents from a home-screen icon. Works today via Add to Home Screen; App Store listing planned for Phase 2.",
            "openApp": "Open Partner Portal",
            "howToInstall": "How to install",
            "iphone": {"title": "iPhone / iPad", "steps": "Safari → Open Partner Portal → Share → Add to Home Screen"},
            "android": {"title": "Android", "steps": "Chrome → Open Partner Portal → menu → Install app or Add to Home screen"},
            "desktop": {"title": "Desktop", "steps": "Chrome or Edge → install icon in the address bar, or bookmark the Partner Portal"},
        },
    },
)

# Remaining locales loaded from data module
from app_i18n_data import LOCALE_BUNDLES  # noqa: E402

LOCALES.update(LOCALE_BUNDLES)

ORDER = [
    "en", "tr", "de", "fr", "es", "it", "pt", "nl", "ar", "ru",
    "zh-cn", "zh-tw", "ja", "ko", "hi", "ur", "pl", "ro", "el",
    "sv", "no", "da", "fi", "he", "id",
]


def main():
    created = []
    for locale in ORDER:
        if locale not in LOCALES:
            raise KeyError(f"Missing locale: {locale}")
        path = OUT / f"{locale}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(LOCALES[locale], f, ensure_ascii=False, indent=2)
            f.write("\n")
        with path.open(encoding="utf-8") as f:
            json.load(f)
        created.append(str(path))
    print(f"Validated {len(created)} JSON files:")
    for p in created:
        print(p)


if __name__ == "__main__":
    main()
