#!/usr/bin/env python3
"""Merge SEO meta fields and seo section into locale message files."""

import json
import sys
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_locale_seo_data import SEO_DATA  # noqa: E402

MESSAGES_DIR = Path("/workspace/messages")
LOCALES = ["de", "fr", "es", "it", "pt", "nl", "pl", "ro", "el", "sv", "no", "da", "fi"]
PAGE_KEYS = [
    "home",
    "about",
    "energySystems",
    "infrastructure",
    "technology",
    "projects",
    "strategicPartnerships",
    "insights",
    "contact",
]
INSIGHT_SLUGS = [
    {"slug": "insight-1", "datePublished": "2026-01-15"},
    {"slug": "insight-2", "datePublished": "2026-01-15"},
    {"slug": "insight-3", "datePublished": "2026-01-15"},
    {"slug": "insight-4", "datePublished": "2026-01-15"},
    {"slug": "insight-5", "datePublished": "2026-01-15"},
    {"slug": "insight-6", "datePublished": "2026-01-15"},
    {"slug": "insight-7", "datePublished": "2026-01-15"},
    {"slug": "insight-8", "datePublished": "2026-01-15"},
]
SAME_AS = ["https://github.com/tvk-group/TVK-Infrastructure-Energy-Systems"]


def deep_keys(d, prefix=""):
    keys = set()
    if isinstance(d, dict):
        for k, v in d.items():
            p = f"{prefix}.{k}" if prefix else k
            keys.add(p)
            keys |= deep_keys(v, p)
    elif isinstance(d, list):
        for i, item in enumerate(d):
            p = f"{prefix}[{i}]"
            if isinstance(item, (dict, list)):
                keys |= deep_keys(item, p)
    return keys


def apply_locale(locale: str) -> None:
    path = MESSAGES_DIR / f"{locale}.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    seo = SEO_DATA[locale]

    for page in PAGE_KEYS:
        data[page]["meta"] = deepcopy(seo[page])

    for i, slug_data in enumerate(INSIGHT_SLUGS):
        data["insights"]["topics"]["items"][i].update(slug_data)

    seo_section = deepcopy(seo["seo"])
    seo_section["organization"]["sameAs"] = SAME_AS
    data["seo"] = seo_section

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validate(locale: str) -> tuple[int, int]:
    with (MESSAGES_DIR / "en.json").open(encoding="utf-8") as f:
        en = json.load(f)
    with (MESSAGES_DIR / f"{locale}.json").open(encoding="utf-8") as f:
        loc = json.load(f)
    missing = deep_keys(en) - deep_keys(loc)
    extra = deep_keys(loc) - deep_keys(en)
    return len(missing), len(extra)


def main() -> None:
    for locale in LOCALES:
        if locale not in SEO_DATA:
            raise KeyError(f"Missing SEO data for {locale}")
        apply_locale(locale)
        missing, extra = validate(locale)
        status = "OK" if missing == 0 and extra == 0 else "MISMATCH"
        print(f"{locale}: {status} (missing={missing}, extra={extra})")


if __name__ == "__main__":
    main()
