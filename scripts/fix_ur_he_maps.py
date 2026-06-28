#!/usr/bin/env python3
"""Fix proper nouns and improve key translations in ur/he maps."""
import json
import re
from pathlib import Path

MAPS_PATH = Path(__file__).parent / "ur_he_maps.json"

PROPER_ORDERED = [
    "TVK Infrastructure & Energy Systems LTD",
    "TVK Infrastructure & Energy Systems",
    "TVK Infrastructure",
    "TVK Ecosystem",
    "EnergieMIND",
    "TVK",
]

UR_OVERRIDES = {
    "TVK Infrastructure & Energy Systems develops future-focused initiatives across energy, infrastructure, industrial systems and strategic technologies.": "TVK Infrastructure & Energy Systems توانائی، انفراسٹرکچر، صنعتی نظام اور اسٹریٹجک ٹیکنالوجیز میں مستقبل پر مبنی اقدامات تیار کرتی ہے۔",
    "Part of the TVK Ecosystem": "TVK Ecosystem کا حصہ",
    "Home": "ہوم",
    "About": "ہمارے بارے میں",
    "About Us": "ہمارے بارے میں",
    "Contact": "رابطہ",
    "Contact Us": "ہم سے رابطہ کریں",
    "Learn more →": "مزید جانیں ←",
    "Explore Capabilities": "صلاحیتیں دریافت کریں",
    "Get in Touch": "رابطہ کریں",
    "In Development": "ترقی کے مرحلے میں",
    "Active": "فعال",
    "Preparation": "تیاری",
    "Powering Infrastructure.": "انفراسٹرکچر کو طاقت دینا۔",
    "Enabling the Future.": "مستقبل کو فعال بنانا۔",
    "Future EnergieMIND Integration": "مستقبل میں EnergieMIND انضمام",
    "Main navigation": "مرکزی نیویگیشن",
    "Mobile navigation": "موبائل نیویگیشن",
    "All rights reserved.": "جملہ حقوق محفوظ ہیں۔",
    "TVK Infrastructure & Energy Systems operates across six interconnected capability areas, supporting long-term industrial and energy initiatives within the TVK ecosystem.": "TVK Infrastructure & Energy Systems چھ باہم مربوط صلاحیت کے شعبوں میں کام کرتی ہے، TVK Ecosystem میں طویل مدتی صنعتی اور توانائی کے اقدامات کی حمایت کرتی ہے۔",
    "TVK Infrastructure & Energy Systems LTD represents the infrastructure, energy, industrial systems and strategic technology investment activities of the TVK ecosystem.": "TVK Infrastructure & Energy Systems LTD TVK Ecosystem میں انفراسٹرکچر، توانائی، صنعتی نظام اور اسٹریٹجک ٹیکنالوجی سرمایہ کاری کی سرگرمیوں کی نمائندگی کرتی ہے۔",
    "TVK Infrastructure & Energy Systems is actively forming projects across energy, infrastructure, and industrial domains. All initiatives are currently in research, development, or pilot preparation stages.": "TVK Infrastructure & Energy Systems توانائی، انفراسٹرکچر اور صنعتی شعبوں میں فعال طور پر منصوبے تشکیل دے رہی ہے۔ تمام اقدامات فی الحال تحقیق، ترقی یا پائلٹ تیاری کے مراحل میں ہیں۔",
    "We envision TVK Infrastructure & Energy Systems as a recognized contributor to the global energy and infrastructure landscape — supporting intelligent systems, sustainable operations, and strategic industrial partnerships across markets.": "ہم TVK Infrastructure & Energy Systems کو عالمی توانائی اور انفراسٹرکچر کے منظرنامے میں ایک تسلیم شدہ شراکت دار کے طور پر دیکھتے ہیں — جو مارکیٹوں میں ذہین نظام، پائیدار آپریشنز اور اسٹریٹجک صنعتی شراکت داری کی حمایت کرتی ہے۔",
    "TVK Infrastructure & Energy Systems is currently in an active development and partnership-building phase. We are conducting research, forming project concepts, and engaging with potential strategic partners across the energy and infrastructure sectors.": "TVK Infrastructure & Energy Systems فی الحال فعال ترقی اور شراکت داری کی تعمیر کے مرحلے میں ہے۔ ہم تحقیق کر رہے ہیں، منصوبوں کے تصورات تشکیل دے رہے ہیں، اور توانائی و انفراسٹرکچر کے شعبوں میں ممکنہ اسٹریٹجک شراکت داروں سے رابطہ کر رہے ہیں۔",
    "Infrastructure is the backbone of industrial economies. TVK Infrastructure & Energy Systems approaches infrastructure technology with the rigor and long-term perspective required for systems that must perform reliably over decades.": "انفراسٹرکچر صنعتی معیشتوں کی ریڑھ کی ہڈی ہے۔ TVK Infrastructure & Energy Systems انفراسٹرکچر ٹیکنالوجی کو اس سختگی اور طویل مدتی نقطہ نظر کے ساتھ اپناتی ہے جو دہائیوں تک قابل اعتماد کارکردگی کے نظاموں کے لیے ضروری ہے۔",
    "TVK Infrastructure & Energy Systems is in an active development phase. We do not present completed or operational projects at this stage — all initiatives listed represent genuine work in progress across research, development, and partnership formation.": "TVK Infrastructure & Energy Systems فعال ترقی کے مرحلے میں ہے۔ ہم اس مرحلے میں مکمل یا آپریشنل منصوبے پیش نہیں کرتے — درج تمام اقدامات تحقیق، ترقی اور شراکت داری کی تشکیل میں جاری اصل کام کی نمائندگی کرتے ہیں۔",
    "TVK Infrastructure & Energy Systems is in a partnership-building phase. We welcome engagement from organizations that can contribute technical expertise, market access, operational capability, or strategic alignment to our developing initiatives.": "TVK Infrastructure & Energy Systems شراکت داری کی تعمیر کے مرحلے میں ہے۔ ہم ان اداروں کی شراکت کا خیرمقدم کرتے ہیں جو ہماری ترقی پذیر اقدامات میں تکنیکی مہارت، مارکیٹ تک رسائی، آپریشنل صلاحیت یا اسٹریٹجک ہم آہنگی فراہم کر سکتے ہیں۔",
    "Our insights reflect the core areas of TVK Infrastructure & Energy Systems — informed by research, industry analysis, and strategic development work.": "ہماری بصیرتیں TVK Infrastructure & Energy Systems کے بنیادی شعبوں کی عکاسی کرتی ہیں — تحقیق، صنعتی تجزیہ اور اسٹریٹجک ترقیاتی کام سے مطلع۔",
    "Questions about TVK Infrastructure & Energy Systems, our capabilities, or the broader TVK ecosystem.": "TVK Infrastructure & Energy Systems، ہماری صلاحیتوں یا وسیع TVK Ecosystem کے بارے میں سوالات۔",
    "Thank you for your interest in TVK Infrastructure & Energy Systems. Our team will review your inquiry and respond accordingly.": "TVK Infrastructure & Energy Systems میں آپ کی دلچسپی کا شکریہ۔ ہماری ٹیم آپ کے استفسار کا جائزہ لے گی اور مناسب جواب دے گی۔",
    "© {year} TVK Infrastructure & Energy Systems LTD. All rights reserved.": "© {year} TVK Infrastructure & Energy Systems LTD۔ جملہ حقوق محفوظ ہیں۔",
}

HE_OVERRIDES = {
    "Part of the TVK Ecosystem": "חלק מ-TVK Ecosystem",
    "Home": "בית",
    "About": "אודות",
    "About Us": "אודות",
    "Contact": "יצירת קשר",
    "Contact Us": "צרו קשר",
    "Learn more →": "למידע נוסף ←",
    "Explore Capabilities": "גלה יכולות",
    "Get in Touch": "צרו קשר",
    "In Development": "בפיתוח",
    "Active": "פעיל",
    "Preparation": "הכנה",
    "Powering Infrastructure.": "מניעים תשתיות.",
    "Enabling the Future.": "מאפשרים את העתיד.",
    "Main navigation": "ניווט ראשי",
    "Mobile navigation": "ניווט נייד",
    "© {year} TVK Infrastructure & Energy Systems LTD. All rights reserved.": "© {year} TVK Infrastructure & Energy Systems LTD. כל הזכויות שמורות.",
    "Ecosystem Integration": "שילוב ב-TVK Ecosystem",
}


def protect_proper(text: str) -> tuple[str, dict[str, str]]:
    placeholders = {}
    result = text
    for i, proper in enumerate(PROPER_ORDERED):
        if proper in result:
            key = f"@@PN{i}@@"
            placeholders[key] = proper
            result = result.replace(proper, key)
    return result, placeholders


def restore_proper(text: str, placeholders: dict[str, str]) -> str:
    result = text
    for key, proper in placeholders.items():
        result = result.replace(key, proper)
    # Fix common mistranslations
    replacements = [
        (r"ٹی\s*وی\s*کے\s*انفراسٹرکچر\s*اور\s*انرجی\s*سسٹمز\s*لمیٹڈ", "TVK Infrastructure & Energy Systems LTD"),
        (r"ٹی\s*وی\s*کے\s*انفراسٹرکچر\s*اور\s*انرجی\s*سسٹمز", "TVK Infrastructure & Energy Systems"),
        (r"ٹی\s*وی\s*کے\s*انفراسٹرکچر", "TVK Infrastructure"),
        (r"ٹی\s*وی\s*کے\s*ایکو\s*سسٹم", "TVK Ecosystem"),
        (r"ٹی\s*وی\s*کے", "TVK"),
        (r"انرجی\s*مائنڈ", "EnergieMIND"),
        (r"אנרגי\s*מיינד", "EnergieMIND"),
        (r"TVK Ecosystem", "TVK Ecosystem"),
        (r"TVKE Infrastructure", "TVK Infrastructure"),
    ]
    for pattern, repl in replacements:
        result = re.sub(pattern, repl, result, flags=re.IGNORECASE)
    return result


def fix_map_entry(original: str, translated: str) -> str:
    _, placeholders = protect_proper(original)
    return restore_proper(translated, placeholders)


def main():
    maps = json.loads(MAPS_PATH.read_text(encoding="utf-8"))
    for locale, overrides in [("ur", UR_OVERRIDES), ("he", HE_OVERRIDES)]:
        for en, tr in list(maps[locale].items()):
            maps[locale][en] = fix_map_entry(en, tr)
        maps[locale].update(overrides)
    MAPS_PATH.write_text(json.dumps(maps, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Fixed ur_he_maps.json")


if __name__ == "__main__":
    main()
