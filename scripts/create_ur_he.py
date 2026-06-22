#!/usr/bin/env python3
"""Generate ur.json and he.json from English master with full professional translations."""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_translations import save_json, deep_merge_structure, merge_insight_slugs, MESSAGES, EN_PATH

PRESERVE = {
    "%s | TVK Infrastructure & Energy Systems",
    "& Energy Systems LTD",
    "*",
    "/energy-systems",
    "/infrastructure",
    "/strategic-partnerships",
    "/technology",
    "01",
    "02",
    "03",
    "2026-01-15",
    "insight-1",
    "insight-2",
    "insight-3",
    "insight-4",
    "insight-5",
    "insight-6",
    "insight-7",
    "insight-8",
    "https://github.com/tvk-group/TVK-Infrastructure-Energy-Systems",
    "professional@company.com",
    "© {year} TVK Infrastructure & Energy Systems LTD. All rights reserved.",
    "TVK Infrastructure",
    "TVK Infrastructure & Energy Systems",
    "TVK Infrastructure & Energy Systems LTD",
    "EnergieMIND",
}


def apply_string_map(obj, mapping):
    if isinstance(obj, str):
        if obj in PRESERVE:
            return obj
        return mapping.get(obj, obj)
    if isinstance(obj, list):
        return [apply_string_map(x, mapping) for x in obj]
    if isinstance(obj, dict):
        return {k: apply_string_map(v, mapping) for k, v in obj.items()}
    return obj


def load_maps():
    maps_path = Path(__file__).parent / "ur_he_maps.json"
    return json.loads(maps_path.read_text(encoding="utf-8"))


UR_META = {
    "home": {
        "title": "انفراسٹرکچر اور توانائی کے نظام | TVK",
        "description": "TVK Infrastructure & Energy Systems مستقبل پر مبنی توانائی، انفراسٹرکچر، صنعتی اور اسٹریٹجک ٹیکنالوجی کے اقدامات تیار کرتی ہے۔ تحقیق، ترقی اور شراکت داری کی تعمیر کا مرحلہ۔",
        "keywords": "انفراسٹرکچر کمپنی، توانائی کے نظام، صنعتی ٹیکنالوجی، TVK Infrastructure، اسٹریٹجک توانائی شراکت داری",
        "ogTitle": "انفراسٹرکچر کو طاقت دینا۔ مستقبل کو فعال بنانا۔ | TVK",
        "ogDescription": "قابل تجدید انضمام، سمارٹ انفراسٹرکچر، صنعتی AI اور اسٹریٹجک شراکت داری میں انٹرپرائز انفراسٹرکچر اور توانائی کے نظام کی ترقی۔",
        "twitterTitle": "TVK Infrastructure & Energy Systems",
        "twitterDescription": "انفراسٹرکچر، توانائی اور صنعتی ٹیکنالوجی کے اقدامات — TVK Ecosystem کا حصہ۔",
    },
    "about": {
        "title": "TVK Infrastructure & Energy Systems کے بارے میں",
        "description": "TVK Infrastructure & Energy Systems کا مشن، وژن اور طویل مدتی صنعتی حکمت عملی — TVK Ecosystem میں انجینئرنگ پر مبنی انفراسٹرکچر اور توانائی کی ترقی۔",
        "keywords": "TVK کے بارے میں، انفراسٹرکچر حکمت عملی، توانائی کمپنی کا مشن، صنعتی ترقی",
        "ogTitle": "TVK Infrastructure & Energy Systems کے بارے میں",
        "ogDescription": "طویل مدتی صنعتی حکمت عملی کے ساتھ انفراسٹرکچر اور توانائی کا مستقبل تشکیل دینا۔",
        "twitterTitle": "TVK Infrastructure & Energy Systems کے بارے میں",
        "twitterDescription": "مشن، وژن اور طویل مدتی انفراسٹرکچر و توانائی کی حکمت عملی۔",
    },
    "energySystems": {
        "title": "توانائی کے نظام اور توانائی انٹیلی جنس",
        "description": "قابل تجدید توانائی کا انضمام، توانائی کی نگرانی، بہتری، صنعتی توانائی کے حل اور TVK Infrastructure & Energy Systems میں EnergieMIND تحقیق۔",
        "keywords": "توانائی کے نظام، قابل تجدید توانائی، توانائی انٹیلی جنس، صنعتی توانائی، توانائی کی نگرانی",
        "ogTitle": "توانائی کے نظام | TVK Infrastructure & Energy Systems",
        "ogDescription": "صنعتی ماحول کے لیے ذہین توانائی کے فریم ورک — نگرانی، بہتری اور قابل تجدید انضمام۔",
        "twitterTitle": "توانائی کے نظام | TVK",
        "twitterDescription": "قابل تجدید انضمام، توانائی انٹیلی جنس اور صنعتی توانائی کے حل۔",
    },
    "infrastructure": {
        "title": "انفراسٹرکچر ٹیکنالوجیز اور سمارٹ انفراسٹرکچر",
        "description": "سمارٹ انفراسٹرکچر، ڈیجیٹل انفراسٹرکچر، اہم انفراسٹرکچر کی لچک اور مستقبل کے انفراسٹرکچر پلیٹ فارم — TVK Infrastructure & Energy Systems۔",
        "keywords": "انفراسٹرکچر ٹیکنالوجی، سمارٹ انفراسٹرکچر، ڈیجیٹل انفراسٹرکچر، اہم انفراسٹرکچر",
        "ogTitle": "انفراسٹرکچر ٹیکنالوجیز | TVK",
        "ogDescription": "سمارٹ، ڈیجیٹل اور لچکدار انفراسٹرکچر نظاموں کے لیے جدید ٹیکنالوجیز۔",
        "twitterTitle": "انفراسٹرکچر ٹیکنالوجیز | TVK",
        "twitterDescription": "سمارٹ، ڈیجیٹل اور اہم انفراسٹرکچر ٹیکنالوجی کی ترقی۔",
    },
    "technology": {
        "title": "صنعتی ٹیکنالوجی، AI اور آٹومیشن",
        "description": "صنعتی AI، انفراسٹرکچر تجزیات، نگرانی کے نظام، آٹومیشن اور توانائی انٹیلی جنس تحقیق — TVK Infrastructure & Energy Systems۔",
        "keywords": "صنعتی AI، انفراسٹرکچر تجزیات، آٹومیشن، نگرانی کے نظام، صنعتی ٹیکنالوجی",
        "ogTitle": "ٹیکنالوجی اور جدت | TVK",
        "ogDescription": "انفراسٹرکچر اور توانائی کے لیے صنعتی AI، تجزیات، آٹومیشن اور ذہین نگرانی۔",
        "twitterTitle": "ٹیکنالوجی اور جدت | TVK",
        "twitterDescription": "انفراسٹرکچر اور توانائی کے لیے صنعتی AI، تجزیات اور آٹومیشن۔",
    },
    "projects": {
        "title": "ترقی کے مرحلے میں منصوبے اور تحقیقی اقدامات",
        "description": "TVK Infrastructure & Energy Systems میں ترقی کے مرحلے میں توانائی، انفراسٹرکچر، صنعتی اور تحقیقی اقدامات۔ شفاف ترقیاتی مرحلے کی منصوبہ بندی کی اقسام۔",
        "keywords": "توانائی کے منصوبے، انفراسٹرکچر منصوبے، صنعتی منصوبے، تحقیقی اقدامات، پائلٹ پروگرام",
        "ogTitle": "ترقی کے مرحلے میں منصوبے | TVK",
        "ogDescription": "TVK Ecosystem میں ترقی کے مرحلے میں توانائی، انفراسٹرکچر اور صنعتی اقدامات۔",
        "twitterTitle": "منصوبے | TVK Infrastructure & Energy Systems",
        "twitterDescription": "ترقی کے مرحلے میں توانائی، انفراسٹرکچر اور صنعتی اقدامات۔",
    },
    "strategicPartnerships": {
        "title": "اسٹریٹجک شراکت داری اور تعاون",
        "description": "TVK Infrastructure & Energy Systems توانائی کمپنیوں، انفراسٹرکچر آپریٹرز، صنعتی گروپس اور ٹیکنالوجی فراہم کنندگان کے ساتھ اسٹریٹجک شراکت داری تلاش کرتی ہے۔",
        "keywords": "اسٹریٹجک شراکت داری، توانائی تعاون، انفراسٹرکچر شراکت داری، صنعتی شراکت داری",
        "ogTitle": "اسٹریٹجک شراکت داری | TVK",
        "ogDescription": "توانائی، انفراسٹرکچر اور صنعتی اداروں کے ساتھ تعاون اور پائلٹ کے مواقع۔",
        "twitterTitle": "اسٹریٹجک شراکت داری | TVK",
        "twitterDescription": "توانائی، انفراسٹرکچر اور صنعتی شراکت داروں کے ساتھ تعاون کی تلاش۔",
    },
    "insights": {
        "title": "بصیرت — توانائی، انفراسٹرکچر اور صنعتی ٹیکنالوجی",
        "description": "TVK Infrastructure & Energy Systems سے توانائی، انفراسٹرکچر، صنعتی ٹیکنالوجی، AI انفراسٹرکچر، پائیداری اور انجینئرنگ پر صنعتی نقطہ نظر۔",
        "keywords": "توانائی بصیرت، انفراسٹرکچر رجحانات، صنعتی ٹیکنالوجی، انجینئرنگ نقطہ نظر",
        "ogTitle": "صنعتی بصیرت | TVK Infrastructure & Energy Systems",
        "ogDescription": "توانائی، انفراسٹرکچر اور صنعتی ٹیکنالوجی پر فکری قیادت۔",
        "twitterTitle": "بصیرت | TVK Infrastructure & Energy Systems",
        "twitterDescription": "توانائی، انفراسٹرکچر اور صنعتی نظاموں پر تحقیقی نقطہ نظر۔",
    },
    "contact": {
        "title": "رابطہ — انفراسٹرکچر اور توانائی کے مواقع",
        "description": "انفراسٹرکچر، توانائی کے نظام، صنعتی حل اور اسٹریٹجک شراکت داری کے مواقع پر بات چیت کے لیے TVK Infrastructure & Energy Systems سے رابطہ کریں۔",
        "keywords": "TVK رابطہ، انفراسٹرکچر استفسار، توانائی شراکت داری رابطہ، صنعتی تعاون",
        "ogTitle": "TVK Infrastructure & Energy Systems سے رابطہ",
        "ogDescription": "TVK Infrastructure & Energy Systems کے ساتھ انفراسٹرکچر اور توانائی کے مواقع پر بات چیت کریں۔",
        "twitterTitle": "رابطہ | TVK Infrastructure & Energy Systems",
        "twitterDescription": "انفراسٹرکچر، توانائی اور شراکت داری کے مواقع کے بارے میں رابطہ کریں۔",
    },
}

HE_META = {
    "home": {
        "title": "תשתיות ומערכות אנרגיה | TVK",
        "description": "TVK Infrastructure & Energy Systems מפתחת יוזמות עתידיות באנרגיה, תשתיות, טכנולוגיה תעשייתית ואסטרטגית. שלב מחקר, פיתוח ובניית שותפויות.",
        "keywords": "חברת תשתיות, מערכות אנרגיה, טכנולוגיה תעשייתית, TVK Infrastructure, שותפויות אנרגיה אסטרטגיות",
        "ogTitle": "מניעים תשתיות. מאפשרים את העתיד. | TVK",
        "ogDescription": "פיתוח תשתיות ומערכות אנרגיה ארגוניות — שילוב אנרגיה מתחדשת, תשתיות חכמות, AI תעשייתי ושותפויות אסטרטגיות.",
        "twitterTitle": "TVK Infrastructure & Energy Systems",
        "twitterDescription": "יוזמות תשתיות, אנרגיה וטכנולוגיה תעשייתית — חלק מ-TVK Ecosystem.",
    },
    "about": {
        "title": "אודות TVK Infrastructure & Energy Systems",
        "description": "משימה, חזון ואסטרטגיה תעשייתית ארוכת טווח של TVK Infrastructure & Energy Systems — פיתוח תשתיות ואנרגיה מונחה הנדסה ב-TVK Ecosystem.",
        "keywords": "אודות TVK, אסטרטגיית תשתיות, משימת חברת אנרגיה, פיתוח תעשייתי",
        "ogTitle": "אודות TVK Infrastructure & Energy Systems",
        "ogDescription": "הנדסת עתיד התשתיות והאנרגיה עם אסטרטגיה תעשייתית ארוכת טווח.",
        "twitterTitle": "אודות TVK Infrastructure & Energy Systems",
        "twitterDescription": "משימה, חזון ואסטרטגיית תשתיות ואנרגיה ארוכת טווח.",
    },
    "energySystems": {
        "title": "מערכות אנרגיה ואינטליגנציה אנרגטית",
        "description": "שילוב אנרגיה מתחדשת, ניטור אנרגיה, אופטימיזציה, פתרונות אנרגיה תעשייתיים ומחקר EnergieMIND ב-TVK Infrastructure & Energy Systems.",
        "keywords": "מערכות אנרגיה, אנרגיה מתחדשת, אינטליגנציה אנרגטית, אנרגיה תעשייתית, ניטור אנרגיה",
        "ogTitle": "מערכות אנרגיה | TVK Infrastructure & Energy Systems",
        "ogDescription": "מסגרות אנרגיה חכמות לסביבות תעשייתיות — ניטור, אופטימיזציה ושילוב מתחדש.",
        "twitterTitle": "מערכות אנרגיה | TVK",
        "twitterDescription": "שילוב מתחדש, אינטליגנציה אנרגטית ופתרונות אנרגיה תעשייתיים.",
    },
    "infrastructure": {
        "title": "טכנולוגיות תשתית ותשתית חכמה",
        "description": "תשתית חכמה, תשתית דיגיטלית, חוסן תשתית קריטית ופלטפורמות תשתית עתידיות — TVK Infrastructure & Energy Systems.",
        "keywords": "טכנולוגיית תשתית, תשתית חכמה, תשתית דיגיטלית, תשתית קריטית",
        "ogTitle": "טכנולוגיות תשתית | TVK",
        "ogDescription": "קידום טכנולוגיות למערכות תשתית חכמות, דיגיטליות ועמידות.",
        "twitterTitle": "טכנולוגיות תשתית | TVK",
        "twitterDescription": "פיתוח טכנולוגיית תשתית חכמה, דיגיטלית וקריטית.",
    },
    "technology": {
        "title": "טכנולוגיה תעשייתית, AI ואוטומציה",
        "description": "AI תעשייתי, אנליטיקת תשתיות, מערכות ניטור, אוטומציה ומחקר אינטליגנציה אנרגטית ב-TVK Infrastructure & Energy Systems.",
        "keywords": "AI תעשייתי, אנליטיקת תשתיות, אוטומציה, מערכות ניטור, טכנולוגיה תעשייתית",
        "ogTitle": "טכנולוגיה וחדשנות | TVK",
        "ogDescription": "AI תעשייתי, אנליטיקה, אוטומציה וניטור חכם לתשתיות ואנרגיה.",
        "twitterTitle": "טכנולוגיה וחדשנות | TVK",
        "twitterDescription": "AI תעשייתי, אנליטיקה ואוטומציה לתשתיות ואנרגיה.",
    },
    "projects": {
        "title": "פרויקטים ויוזמות מחקר בפיתוח",
        "description": "יוזמות אנרגיה, תשתיות, תעשייה ומחקר בפיתוח ב-TVK Infrastructure & Energy Systems. קטגוריות פרויקטים שקופות בשלב הפיתוח.",
        "keywords": "פרויקטי אנרגיה, פרויקטי תשתית, פרויקטים תעשייתיים, יוזמות מחקר, תוכניות פיילוט",
        "ogTitle": "פרויקטים בפיתוח | TVK",
        "ogDescription": "יוזמות אנרגיה, תשתיות ותעשייה בשלב פיתוח ב-TVK Ecosystem.",
        "twitterTitle": "פרויקטים | TVK Infrastructure & Energy Systems",
        "twitterDescription": "יוזמות אנרגיה, תשתיות ותעשייה בפיתוח.",
    },
    "strategicPartnerships": {
        "title": "שותפויות אסטרטגיות ושיתוף פעולה",
        "description": "TVK Infrastructure & Energy Systems מחפשת שותפויות אסטרטגיות עם חברות אנרגיה, מפעילי תשתיות, קבוצות תעשייתיות וספקי טכנולוגיה.",
        "keywords": "שותפויות אסטרטגיות, שיתוף פעולה באנרגיה, שותפויות תשתית, שותפויות תעשייתיות",
        "ogTitle": "שותפויות אסטרטגיות | TVK",
        "ogDescription": "שיתוף פעולה והזדמנויות פיילוט עם ארגוני אנרגיה, תשתיות ותעשייה.",
        "twitterTitle": "שותפויות אסטרטגיות | TVK",
        "twitterDescription": "מחפשים שיתוף פעולה עם שותפי אנרגיה, תשתיות ותעשייה.",
    },
    "insights": {
        "title": "תובנות — אנרגיה, תשתיות וטכנולוגיה תעשייתית",
        "description": "פרספקטיבות תעשייתיות על אנרגיה, תשתיות, טכנולוגיה תעשייתית, תשתית AI, קיימות והנדסה מ-TVK Infrastructure & Energy Systems.",
        "keywords": "תובנות אנרגיה, מגמות תשתית, טכנולוגיה תעשייתית, פרספקטיבות הנדסיות",
        "ogTitle": "תובנות תעשייתיות | TVK Infrastructure & Energy Systems",
        "ogDescription": "מנהיגות מחשבה באנרגיה, תשתיות וטכנולוגיה תעשייתית.",
        "twitterTitle": "תובנות | TVK Infrastructure & Energy Systems",
        "twitterDescription": "פרספקטיבות מחקר על אנרגיה, תשתיות ומערכות תעשייתיות.",
    },
    "contact": {
        "title": "יצירת קשר — הזדמנויות תשתית ואנרגיה",
        "description": "צרו קשר עם TVK Infrastructure & Energy Systems לדיון בתשתיות, מערכות אנרגיה, פתרונות תעשייתיים והזדמנויות שותפות אסטרטגית.",
        "keywords": "יצירת קשר TVK, פניית תשתית, קשר שותפות אנרגיה, שיתוף פעולה תעשייתי",
        "ogTitle": "יצירת קשר עם TVK Infrastructure & Energy Systems",
        "ogDescription": "דנו בהזדמנויות תשתית ואנרגיה עם TVK Infrastructure & Energy Systems.",
        "twitterTitle": "יצירת קשר | TVK Infrastructure & Energy Systems",
        "twitterDescription": "צרו קשר לגבי תשתיות, אנרגיה והזדמנויות שותפות.",
    },
}

UR_SEO = {
    "siteName": "TVK Infrastructure & Energy Systems",
    "websiteDescription": "TVK Ecosystem میں انٹرپرائز انفراسٹرکچر، توانائی کے نظام، صنعتی ٹیکنالوجی اور اسٹریٹجک سرمایہ کاری کے اقدامات۔",
    "ogImageAlt": "TVK Infrastructure & Energy Systems — انفراسٹرکچر کو طاقت دینا۔ مستقبل کو فعال بنانا۔",
    "defaultKeywords": "انفراسٹرکچر، توانائی کے نظام، صنعتی ٹیکنالوجی، سمارٹ انفراسٹرکچر، توانائی انٹیلی جنس، TVK، اسٹریٹجک شراکت داری",
    "breadcrumbAria": "بریڈ کرمب نیویگیشن",
    "internalLinksTitle": "انفراسٹرکچر اور توانائی کی صلاحیتیں دریافت کریں",
    "legalDisclaimer": "TVK Infrastructure & Energy Systems LTD تحقیق، ترقی اور شراکت داری کی تعمیر کے مرحلے میں ہے۔ اس ویب سائٹ کی معلومات صلاحیت کے شعبوں اور ترقیاتی اقدامات کی وضاحت کرتی ہے — آپریشنل منصوبوں کی وعدے نہیں۔ TVK Ecosystem کا حصہ۔",
    "organization": {
        "name": "TVK Infrastructure & Energy Systems",
        "legalName": "TVK Infrastructure & Energy Systems LTD",
        "description": "TVK Ecosystem میں انفراسٹرکچر، توانائی، صنعتی نظام اور اسٹریٹجک ٹیکنالوجی سرمایہ کاری کمپنی۔",
        "areaServed": "دنیا بھر",
        "knowsAbout": [
            "توانائی کے نظام",
            "انفراسٹرکچر ٹیکنالوجیز",
            "صنعتی AI",
            "توانائی انٹیلی جنس",
            "اسٹریٹجک شراکت داری",
        ],
    },
    "faq": [
        {
            "question": "TVK Infrastructure & Energy Systems کیا کرتی ہے؟",
            "answer": "TVK Infrastructure & Energy Systems TVK Ecosystem میں توانائی کے نظام، انفراسٹرکچر ٹیکنالوجیز، صنعتی حل، توانائی انٹیلی جنس، AI انفراسٹرکچر اور اسٹریٹجک سرمایہ کاری کے اقدامات تیار کرتی ہے۔",
        },
        {
            "question": "کمپنی فی الحال کس مرحلے میں ہے؟",
            "answer": "کمپنی تحقیق، ترقی، منصوبے کی تشکیل، اسٹریٹجک شراکت داری کی ترقی اور پائلٹ تیاری کے مراحل میں ہے۔",
        },
        {
            "question": "کیا TVK Infrastructure & Energy Systems شراکت داری تلاش کرتی ہے؟",
            "answer": "جی ہاں۔ ہم تعاون اور پائلٹ کے مواقع کے لیے توانائی کمپنیوں، انفراسٹرکچر آپریٹرز، صنعتی گروپس، ٹیکنالوجی فراہم کنندگان اور انجینئرنگ فرموں کے ساتھ فعال طور پر رابطہ کرتے ہیں۔",
        },
        {
            "question": "کیا TVK Infrastructure & Energy Systems بڑے ماحولیاتی نظام کا حصہ ہے؟",
            "answer": "جی ہاں۔ TVK Infrastructure & Energy Systems وسیع TVK Ecosystem کا حصہ ہے، جو ٹیکنالوجی، صنعتی اور اسٹریٹجک سرمایہ کاری کے نقطہ نظر کو یکجا کرتا ہے۔",
        },
    ],
}

HE_SEO = {
    "siteName": "TVK Infrastructure & Energy Systems",
    "websiteDescription": "יוזמות תשתיות ארגוניות, מערכות אנרגיה, טכנולוגיה תעשייתית והשקעות אסטרטגיות ב-TVK Ecosystem.",
    "ogImageAlt": "TVK Infrastructure & Energy Systems — מניעים תשתיות. מאפשרים את העתיד.",
    "defaultKeywords": "תשתיות, מערכות אנרגיה, טכנולוגיה תעשייתית, תשתית חכמה, אינטליגנציה אנרגטית, TVK, שותפויות אסטרטגיות",
    "breadcrumbAria": "ניווט פירורי לחם",
    "internalLinksTitle": "גלה יכולות תשתית ואנרגיה",
    "legalDisclaimer": "TVK Infrastructure & Energy Systems LTD נמצאת בשלב מחקר, פיתוח ובניית שותפויות. המידע באתר זה מתאר תחומי יכולת ויוזמות פיתוח — לא התחייבויות לפרויקטים תפעוליים. חלק מ-TVK Ecosystem.",
    "organization": {
        "name": "TVK Infrastructure & Energy Systems",
        "legalName": "TVK Infrastructure & Energy Systems LTD",
        "description": "חברת השקעות בתשתיות, אנרגיה, מערכות תעשייתיות וטכנולוגיה אסטרטגית ב-TVK Ecosystem.",
        "areaServed": "ברחבי העולם",
        "knowsAbout": [
            "מערכות אנרגיה",
            "טכנולוגיות תשתית",
            "AI תעשייתי",
            "אינטליגנציה אנרגטית",
            "שותפויות אסטרטגיות",
        ],
    },
    "faq": [
        {
            "question": "מה עושה TVK Infrastructure & Energy Systems?",
            "answer": "TVK Infrastructure & Energy Systems מפתחת יוזמות במערכות אנרגיה, טכנולוגיות תשתית, פתרונות תעשייתיים, אינטליגנציה אנרגטית, תשתית AI והשקעות אסטרטגיות ב-TVK Ecosystem.",
        },
        {
            "question": "באיזה שלב נמצאת החברה כעת?",
            "answer": "החברה נמצאת בשלבי מחקר, פיתוח, גיבוש פרויקטים, פיתוח שותפויות אסטרטגיות והכנת פיילוט.",
        },
        {
            "question": "האם TVK Infrastructure & Energy Systems מחפשת שותפויות?",
            "answer": "כן. אנו פועלים באופן פעיל עם חברות אנרגיה, מפעילי תשתיות, קבוצות תעשייתיות, ספקי טכנולוגיה וחברות הנדסה לשיתוף פעולה והזדמנויות פיילוט.",
        },
        {
            "question": "האם TVK Infrastructure & Energy Systems היא חלק ממערכת אקולוגית גדולה יותר?",
            "answer": "כן. TVK Infrastructure & Energy Systems היא חלק מ-TVK Ecosystem הרחב, המשלב פרספקטיבות טכנולוגיה, תעשייה והשקעות אסטרטגיות.",
        },
    ],
}


def apply_meta_seo(data, meta_overlay, seo_section, en):
    for page_key, meta_fields in meta_overlay.items():
        if page_key in data and "meta" in data[page_key]:
            data[page_key]["meta"].update(meta_fields)
    seo = copy.deepcopy(seo_section)
    seo["organization"]["sameAs"] = en["seo"]["organization"]["sameAs"]
    data["seo"] = seo


def main():
    en = json.loads(EN_PATH.read_text(encoding="utf-8"))
    maps = load_maps()

    for locale, map_key, meta, seo in [
        ("ur", "ur", UR_META, UR_SEO),
        ("he", "he", HE_META, HE_SEO),
    ]:
        translated = apply_string_map(copy.deepcopy(en), maps[map_key])
        apply_meta_seo(translated, meta, seo, en)
        merge_insight_slugs(translated, en)
        save_json(MESSAGES / f"{locale}.json", translated)
        print(f"Wrote {locale}.json")


if __name__ == "__main__":
    main()
