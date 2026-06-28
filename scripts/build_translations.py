#!/usr/bin/env python3
"""Build and update TVK Infrastructure locale message files."""
import copy
import json
import re
from pathlib import Path

try:
    from opencc import OpenCC
except ImportError:
    OpenCC = None

MESSAGES = Path(__file__).resolve().parent.parent / "messages"
EN_PATH = MESSAGES / "en.json"

PRESERVE_KEYS = {"href", "slug", "datePublished", "step", "sameAs", "required"}
PRESERVE_PATTERNS = [
    re.compile(r"^https?://"),
    re.compile(r"^insight-\d+$"),
    re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    re.compile(r"^professional@"),
    re.compile(r"^%s \|"),
    re.compile(r"^© \{year\}"),
    re.compile(r"^TVK Infrastructure"),
    re.compile(r"^& Energy Systems"),
    re.compile(r"^EnergieMIND"),
]


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def deep_merge_structure(template: dict, translated: dict) -> dict:
    """Merge translated content onto en structure, preserving structural keys."""
    if isinstance(template, list):
        result = []
        for i, t_item in enumerate(template):
            tr_item = translated[i] if i < len(translated) else t_item
            if isinstance(t_item, dict):
                result.append(deep_merge_structure(t_item, tr_item if isinstance(tr_item, dict) else {}))
            else:
                result.append(tr_item if i < len(translated) else t_item)
        return result
    if isinstance(template, dict):
        result = {}
        for key, t_val in template.items():
            tr_val = translated.get(key, t_val)
            if key in PRESERVE_KEYS:
                result[key] = t_val
            elif isinstance(t_val, dict) and isinstance(tr_val, dict):
                result[key] = deep_merge_structure(t_val, tr_val)
            elif isinstance(t_val, list):
                result[key] = deep_merge_structure(t_val, tr_val if isinstance(tr_val, list) else [])
            else:
                result[key] = tr_val if key in translated else t_val
        return result
    return translated


def merge_insight_slugs(data: dict, template: dict) -> None:
    for i, item in enumerate(data.get("insights", {}).get("topics", {}).get("items", [])):
        tpl = template["insights"]["topics"]["items"][i]
        item["slug"] = tpl["slug"]
        item["datePublished"] = tpl["datePublished"]


# --- Enhanced page meta overlays ---
META_OVERLAYS = {
    "tr": {
        "home": {
            "title": "Altyapı ve Enerji Sistemleri | TVK",
            "description": "TVK Infrastructure & Energy Systems, geleceğe yönelik enerji, altyapı, endüstriyel ve stratejik teknoloji girişimleri geliştirmektedir. Araştırma, geliştirme ve ortaklık oluşturma aşaması.",
            "keywords": "altyapı şirketi, enerji sistemleri, endüstriyel teknoloji, TVK Infrastructure, stratejik enerji ortaklıkları",
            "ogTitle": "Altyapıya Güç Veriyoruz. Geleceği Şekillendiriyoruz. | TVK",
            "ogDescription": "Yenilenebilir entegrasyon, akıllı altyapı, endüstriyel yapay zekâ ve stratejik ortaklıklar kapsamında kurumsal altyapı ve enerji sistemleri geliştirme.",
            "twitterTitle": "TVK Infrastructure & Energy Systems",
            "twitterDescription": "Altyapı, enerji ve endüstriyel teknoloji girişimleri — TVK ekosisteminin parçası.",
        },
        "about": {
            "title": "TVK Infrastructure & Energy Systems Hakkında",
            "description": "TVK Infrastructure & Energy Systems misyonu, vizyonu ve uzun vadeli endüstriyel stratejisi — TVK ekosisteminde mühendislik odaklı altyapı ve enerji geliştirme.",
            "keywords": "TVK hakkında, altyapı stratejisi, enerji şirketi misyonu, endüstriyel gelişim",
            "ogTitle": "TVK Infrastructure & Energy Systems Hakkında",
            "ogDescription": "Uzun vadeli endüstriyel stratejiyle altyapı ve enerjinin geleceğini mühendislikle şekillendiriyoruz.",
            "twitterTitle": "TVK Infrastructure & Energy Systems Hakkında",
            "twitterDescription": "Misyon, vizyon ve uzun vadeli altyapı ile enerji stratejisi.",
        },
        "energySystems": {
            "title": "Enerji Sistemleri ve Enerji Zekâsı",
            "description": "Yenilenebilir enerji entegrasyonu, enerji izleme, optimizasyon, endüstriyel enerji çözümleri ve TVK Infrastructure & Energy Systems bünyesinde EnergieMIND araştırması.",
            "keywords": "enerji sistemleri, yenilenebilir enerji, enerji zekâsı, endüstriyel enerji, enerji izleme",
            "ogTitle": "Enerji Sistemleri | TVK Infrastructure & Energy Systems",
            "ogDescription": "Endüstriyel ortamlar için akıllı enerji çerçeveleri — izleme, optimizasyon ve yenilenebilir entegrasyon.",
            "twitterTitle": "Enerji Sistemleri | TVK",
            "twitterDescription": "Yenilenebilir entegrasyon, enerji zekâsı ve endüstriyel enerji çözümleri.",
        },
        "infrastructure": {
            "title": "Altyapı Teknolojileri ve Akıllı Altyapı",
            "description": "Akıllı altyapı, dijital altyapı, kritik altyapı dayanıklılığı ve gelecek altyapı platformları — TVK Infrastructure & Energy Systems.",
            "keywords": "altyapı teknolojisi, akıllı altyapı, dijital altyapı, kritik altyapı",
            "ogTitle": "Altyapı Teknolojileri | TVK",
            "ogDescription": "Akıllı, dijital ve dayanıklı altyapı sistemleri için ileri teknolojiler.",
            "twitterTitle": "Altyapı Teknolojileri | TVK",
            "twitterDescription": "Akıllı, dijital ve kritik altyapı teknolojisi geliştirme.",
        },
        "technology": {
            "title": "Endüstriyel Teknoloji, Yapay Zekâ ve Otomasyon",
            "description": "Endüstriyel yapay zekâ, altyapı analitiği, izleme sistemleri, otomasyon ve enerji zekâsı araştırması — TVK Infrastructure & Energy Systems.",
            "keywords": "endüstriyel yapay zekâ, altyapı analitiği, otomasyon, izleme sistemleri, endüstriyel teknoloji",
            "ogTitle": "Teknoloji ve İnovasyon | TVK",
            "ogDescription": "Altyapı ve enerji için endüstriyel yapay zekâ, analitik, otomasyon ve akıllı izleme.",
            "twitterTitle": "Teknoloji ve İnovasyon | TVK",
            "twitterDescription": "Altyapı ve enerji için endüstriyel yapay zekâ, analitik ve otomasyon.",
        },
        "projects": {
            "title": "Geliştirme Aşamasındaki Projeler ve Araştırma Girişimleri",
            "description": "TVK Infrastructure & Energy Systems bünyesinde geliştirilmekte olan enerji, altyapı, endüstriyel ve araştırma girişimleri. Şeffaf geliştirme aşaması proje kategorileri.",
            "keywords": "enerji projeleri, altyapı projeleri, endüstriyel projeler, araştırma girişimleri, pilot programlar",
            "ogTitle": "Geliştirme Aşamasındaki Projeler | TVK",
            "ogDescription": "TVK ekosisteminde geliştirme aşamasındaki enerji, altyapı ve endüstriyel girişimler.",
            "twitterTitle": "Projeler | TVK Infrastructure & Energy Systems",
            "twitterDescription": "Geliştirme aşamasındaki enerji, altyapı ve endüstriyel girişimler.",
        },
        "strategicPartnerships": {
            "title": "Stratejik Ortaklıklar ve İş Birliği",
            "description": "TVK Infrastructure & Energy Systems, enerji şirketleri, altyapı işletmecileri, endüstriyel gruplar ve teknoloji sağlayıcılarıyla stratejik ortaklıklar aramaktadır.",
            "keywords": "stratejik ortaklıklar, enerji iş birliği, altyapı ortaklıkları, endüstriyel ortaklıklar",
            "ogTitle": "Stratejik Ortaklıklar | TVK",
            "ogDescription": "Enerji, altyapı ve endüstriyel kuruluşlarla iş birliği ve pilot fırsatları.",
            "twitterTitle": "Stratejik Ortaklıklar | TVK",
            "twitterDescription": "Enerji, altyapı ve endüstriyel ortaklarla iş birliği arayışı.",
        },
        "insights": {
            "title": "Görüşler — Enerji, Altyapı ve Endüstriyel Teknoloji",
            "description": "TVK Infrastructure & Energy Systems'ten enerji, altyapı, endüstriyel teknoloji, yapay zekâ altyapısı, sürdürülebilirlik ve mühendislik konularında sektör perspektifleri.",
            "keywords": "enerji görüşleri, altyapı trendleri, endüstriyel teknoloji, mühendislik perspektifleri",
            "ogTitle": "Sektör Görüşleri | TVK Infrastructure & Energy Systems",
            "ogDescription": "Enerji, altyapı ve endüstriyel teknoloji konularında düşünce liderliği.",
            "twitterTitle": "Görüşler | TVK Infrastructure & Energy Systems",
            "twitterDescription": "Enerji, altyapı ve endüstriyel sistemler üzerine araştırma perspektifleri.",
        },
        "contact": {
            "title": "İletişim — Altyapı ve Enerji Fırsatları",
            "description": "Altyapı, enerji sistemleri, endüstriyel çözümler ve stratejik ortaklık fırsatlarını görüşmek için TVK Infrastructure & Energy Systems ile iletişime geçin.",
            "keywords": "TVK iletişim, altyapı talebi, enerji ortaklığı iletişim, endüstriyel iş birliği",
            "ogTitle": "İletişim | TVK Infrastructure & Energy Systems",
            "ogDescription": "TVK Infrastructure & Energy Systems ile altyapı ve enerji fırsatlarını görüşün.",
            "twitterTitle": "İletişim | TVK Infrastructure & Energy Systems",
            "twitterDescription": "Altyapı, enerji ve ortaklık fırsatları hakkında bizimle iletişime geçin.",
        },
    },
    "zh-cn": {
        "home": {
            "title": "基础设施与能源系统 | TVK",
            "description": "TVK Infrastructure & Energy Systems 开发面向未来的能源、基础设施、工业和战略技术举措。处于研究、开发和合作伙伴建设阶段。",
            "keywords": "基础设施公司, 能源系统, 工业技术, TVK Infrastructure, 战略能源合作",
            "ogTitle": "驱动基础设施。赋能未来。 | TVK",
            "ogDescription": "涵盖可再生能源集成、智能基础设施、工业 AI 和战略合作伙伴关系的企业级基础设施与能源系统开发。",
            "twitterTitle": "TVK Infrastructure & Energy Systems",
            "twitterDescription": "基础设施、能源和工业技术举措 — TVK Ecosystem 的一部分。",
        },
        "about": {
            "title": "关于 TVK Infrastructure & Energy Systems",
            "description": "TVK Infrastructure & Energy Systems 的使命、愿景和长期工业战略 — 在 TVK Ecosystem 内以工程为导向的基础设施与能源开发。",
            "keywords": "关于 TVK, 基础设施战略, 能源公司使命, 工业发展",
            "ogTitle": "关于 TVK Infrastructure & Energy Systems",
            "ogDescription": "以长期工业战略塑造基础设施与能源的未来。",
            "twitterTitle": "关于 TVK Infrastructure & Energy Systems",
            "twitterDescription": "使命、愿景和长期基础设施与能源战略。",
        },
        "energySystems": {
            "title": "能源系统与能源智能",
            "description": "可再生能源集成、能源监控、优化、工业能源解决方案以及 TVK Infrastructure & Energy Systems 的 EnergieMIND 研究。",
            "keywords": "能源系统, 可再生能源, 能源智能, 工业能源, 能源监控",
            "ogTitle": "能源系统 | TVK Infrastructure & Energy Systems",
            "ogDescription": "面向工业环境的智能能源框架 — 监控、优化与可再生能源集成。",
            "twitterTitle": "能源系统 | TVK",
            "twitterDescription": "可再生能源集成、能源智能与工业能源解决方案。",
        },
        "infrastructure": {
            "title": "基础设施技术与智能基础设施",
            "description": "智能基础设施、数字基础设施、关键基础设施韧性及未来基础设施平台 — TVK Infrastructure & Energy Systems。",
            "keywords": "基础设施技术, 智能基础设施, 数字基础设施, 关键基础设施",
            "ogTitle": "基础设施技术 | TVK",
            "ogDescription": "推进智能、数字和韧性基础设施系统技术。",
            "twitterTitle": "基础设施技术 | TVK",
            "twitterDescription": "智能、数字和关键基础设施技术开发。",
        },
        "technology": {
            "title": "工业技术、AI 与自动化",
            "description": "工业 AI、基础设施分析、监控系统、自动化及能源智能研究 — TVK Infrastructure & Energy Systems。",
            "keywords": "工业 AI, 基础设施分析, 自动化, 监控系统, 工业技术",
            "ogTitle": "技术与创新 | TVK",
            "ogDescription": "面向基础设施与能源的工业 AI、分析、自动化与智能监控。",
            "twitterTitle": "技术与创新 | TVK",
            "twitterDescription": "面向基础设施与能源的工业 AI、分析与自动化。",
        },
        "projects": {
            "title": "开发中的项目与研究举措",
            "description": "TVK Infrastructure & Energy Systems 正在开发的能源、基础设施、工业和研究举措。透明的开发阶段项目分类。",
            "keywords": "能源项目, 基础设施项目, 工业项目, 研究举措, 试点项目",
            "ogTitle": "开发中的项目 | TVK",
            "ogDescription": "TVK Ecosystem 内处于开发阶段的能源、基础设施与工业举措。",
            "twitterTitle": "项目 | TVK Infrastructure & Energy Systems",
            "twitterDescription": "开发中的能源、基础设施与工业举措。",
        },
        "strategicPartnerships": {
            "title": "战略合作伙伴与协作",
            "description": "TVK Infrastructure & Energy Systems 寻求与能源企业、基础设施运营商、工业集团和技术供应商建立战略合作伙伴关系。",
            "keywords": "战略合作, 能源协作, 基础设施合作, 工业合作",
            "ogTitle": "战略合作伙伴 | TVK",
            "ogDescription": "与能源、基础设施和工业机构的协作与试点机会。",
            "twitterTitle": "战略合作伙伴 | TVK",
            "twitterDescription": "寻求与能源、基础设施和工业合作伙伴协作。",
        },
        "insights": {
            "title": "行业洞察 — 能源、基础设施与工业技术",
            "description": "TVK Infrastructure & Energy Systems 关于能源、基础设施、工业技术、AI 基础设施、可持续发展与工程的行业观点。",
            "keywords": "能源洞察, 基础设施趋势, 工业技术, 工程观点",
            "ogTitle": "行业洞察 | TVK Infrastructure & Energy Systems",
            "ogDescription": "关于能源、基础设施与工业技术的思想领导力。",
            "twitterTitle": "行业洞察 | TVK Infrastructure & Energy Systems",
            "twitterDescription": "关于能源、基础设施与工业系统的研究观点。",
        },
        "contact": {
            "title": "联系我们 — 基础设施与能源合作机会",
            "description": "联系 TVK Infrastructure & Energy Systems，探讨基础设施、能源系统、工业解决方案和战略合作伙伴机会。",
            "keywords": "联系 TVK, 基础设施咨询, 能源合作联系, 工业协作",
            "ogTitle": "联系 TVK Infrastructure & Energy Systems",
            "ogDescription": "与 TVK Infrastructure & Energy Systems 探讨基础设施与能源合作机会。",
            "twitterTitle": "联系我们 | TVK Infrastructure & Energy Systems",
            "twitterDescription": "就基础设施、能源和合作机会与我们联系。",
        },
    },
}


SEO_SECTIONS = {
    "tr": {
        "siteName": "TVK Infrastructure & Energy Systems",
        "websiteDescription": "TVK ekosisteminde kurumsal altyapı, enerji sistemleri, endüstriyel teknoloji ve stratejik yatırım girişimleri.",
        "ogImageAlt": "TVK Infrastructure & Energy Systems — Altyapıya Güç Veriyoruz. Geleceği Şekillendiriyoruz.",
        "defaultKeywords": "altyapı, enerji sistemleri, endüstriyel teknoloji, akıllı altyapı, enerji zekâsı, TVK, stratejik ortaklıklar",
        "breadcrumbAria": "İçerik haritası navigasyonu",
        "internalLinksTitle": "Altyapı ve Enerji Yetkinliklerini Keşfedin",
        "legalDisclaimer": "TVK Infrastructure & Energy Systems LTD araştırma, geliştirme ve ortaklık oluşturma aşamasındadır. Bu web sitesindeki bilgiler yetkinlik alanlarını ve geliştirme girişimlerini açıklamaktadır — operasyonel proje taahhütleri değildir. TVK Ekosisteminin parçasıdır.",
        "organization": {
            "name": "TVK Infrastructure & Energy Systems",
            "legalName": "TVK Infrastructure & Energy Systems LTD",
            "description": "TVK ekosisteminde altyapı, enerji, endüstriyel sistemler ve stratejik teknoloji yatırım şirketi.",
            "sameAs": ["https://github.com/tvk-group/TVK-Infrastructure-Energy-Systems"],
            "areaServed": "Dünya geneli",
            "knowsAbout": [
                "Enerji Sistemleri",
                "Altyapı Teknolojileri",
                "Endüstriyel Yapay Zekâ",
                "Enerji Zekâsı",
                "Stratejik Ortaklıklar",
            ],
        },
        "faq": [
            {
                "question": "TVK Infrastructure & Energy Systems ne yapmaktadır?",
                "answer": "TVK Infrastructure & Energy Systems, TVK ekosisteminde enerji sistemleri, altyapı teknolojileri, endüstriyel çözümler, enerji zekâsı, yapay zekâ altyapısı ve stratejik yatırımlar alanında girişimler geliştirmektedir.",
            },
            {
                "question": "Şirket şu anda hangi aşamadadır?",
                "answer": "Şirket araştırma, geliştirme, proje oluşturma, stratejik ortaklık geliştirme ve pilot hazırlık aşamalarındadır.",
            },
            {
                "question": "TVK Infrastructure & Energy Systems ortaklık arıyor mu?",
                "answer": "Evet. Enerji şirketleri, altyapı işletmecileri, endüstriyel gruplar, teknoloji sağlayıcıları ve mühendislik firmalarıyla iş birliği ve pilot fırsatları için aktif olarak görüşmeler yürütüyoruz.",
            },
            {
                "question": "TVK Infrastructure & Energy Systems daha geniş bir ekosistemin parçası mı?",
                "answer": "Evet. TVK Infrastructure & Energy Systems, teknoloji, endüstriyel ve stratejik yatırım perspektiflerini entegre eden daha geniş TVK ekosisteminin bir parçasıdır.",
            },
        ],
    },
    "zh-cn": {
        "siteName": "TVK Infrastructure & Energy Systems",
        "websiteDescription": "TVK Ecosystem 内的企业级基础设施、能源系统、工业技术与战略投资举措。",
        "ogImageAlt": "TVK Infrastructure & Energy Systems — 驱动基础设施。赋能未来。",
        "defaultKeywords": "基础设施, 能源系统, 工业技术, 智能基础设施, 能源智能, TVK, 战略合作",
        "breadcrumbAria": "面包屑导航",
        "internalLinksTitle": "探索基础设施与能源核心能力",
        "legalDisclaimer": "TVK Infrastructure & Energy Systems LTD 目前处于研究、开发和合作伙伴建设阶段。本网站信息描述的是能力领域和开发举措，而非运营项目承诺。TVK Ecosystem 的一部分。",
        "organization": {
            "name": "TVK Infrastructure & Energy Systems",
            "legalName": "TVK Infrastructure & Energy Systems LTD",
            "description": "TVK Ecosystem 内的基础设施、能源、工业系统与战略技术投资公司。",
            "sameAs": ["https://github.com/tvk-group/TVK-Infrastructure-Energy-Systems"],
            "areaServed": "全球",
            "knowsAbout": [
                "能源系统",
                "基础设施技术",
                "工业 AI",
                "能源智能",
                "战略合作伙伴",
            ],
        },
        "faq": [
            {
                "question": "TVK Infrastructure & Energy Systems 做什么？",
                "answer": "TVK Infrastructure & Energy Systems 在 TVK Ecosystem 内开发涵盖能源系统、基础设施技术、工业解决方案、能源智能、AI 基础设施和战略投资的举措。",
            },
            {
                "question": "公司目前处于什么阶段？",
                "answer": "公司处于研究、开发、项目形成、战略合作伙伴关系发展和试点准备阶段。",
            },
            {
                "question": "TVK Infrastructure & Energy Systems 是否寻求合作伙伴？",
                "answer": "是的。我们积极与能源企业、基础设施运营商、工业集团、技术供应商和工程公司接洽，寻求协作与试点机会。",
            },
            {
                "question": "TVK Infrastructure & Energy Systems 是否属于更大的生态系统？",
                "answer": "是的。TVK Infrastructure & Energy Systems 是更广泛的 TVK Ecosystem 的一部分，整合技术、工业和战略投资视角。",
            },
        ],
    },
}


def apply_meta_overlays(data: dict, locale: str) -> None:
    overlays = META_OVERLAYS.get(locale, {})
    for page_key, meta_fields in overlays.items():
        if page_key in data and "meta" in data[page_key]:
            data[page_key]["meta"].update(meta_fields)


def apply_seo(data: dict, locale: str, template: dict) -> None:
    seo = copy.deepcopy(SEO_SECTIONS[locale])
    seo["organization"]["sameAs"] = template["seo"]["organization"]["sameAs"]
    data["seo"] = seo


def convert_to_traditional(simplified_data: dict) -> dict:
    if OpenCC is None:
        raise RuntimeError("opencc-python-reimplemented is required for zh-tw conversion")
    converter = OpenCC("s2t")

    def convert_value(val):
        if isinstance(val, str):
            protected = []
            def protect(m):
                protected.append(m.group(0))
                return f"__PROT{len(protected)-1}__"
            text = val
            for pat in [
                r"TVK Infrastructure & Energy Systems LTD",
                r"TVK Infrastructure & Energy Systems",
                r"TVK Ecosystem",
                r"TVK Infrastructure",
                r"EnergieMIND",
                r"& Energy Systems LTD",
                r"professional@company\.com",
                r"insight-\d+",
                r"https?://\S+",
                r"%s \| TVK Infrastructure & Energy Systems",
            ]:
                text = re.sub(pat, protect, text)
            converted = converter.convert(text)
            for i, orig in enumerate(protected):
                converted = converted.replace(f"__PROT{i}__", orig)
            return converted
        if isinstance(val, list):
            return [convert_value(v) for v in val]
        if isinstance(val, dict):
            return {k: convert_value(v) for k, v in val.items()}
        return val

    return convert_value(simplified_data)


def update_locale(locale: str, source_path: Path, en: dict) -> dict:
    source = load_json(source_path)
    data = deep_merge_structure(en, source)
    apply_meta_overlays(data, locale)
    apply_seo(data, locale, en)
    merge_insight_slugs(data, en)
    return data


def main():
    en = load_json(EN_PATH)

    tr_data = update_locale("tr", MESSAGES / "tr.json", en)
    save_json(MESSAGES / "tr.json", tr_data)

    zhcn_data = update_locale("zh-cn", MESSAGES / "zh-cn.json", en)
    save_json(MESSAGES / "zh-cn.json", zhcn_data)

    zhtw_data = convert_to_traditional(copy.deepcopy(zhcn_data))
    save_json(MESSAGES / "zh-tw.json", zhtw_data)

    for obsolete in ("cs.json", "hu.json", "vi.json", "zh.json"):
        path = MESSAGES / obsolete
        if path.exists():
            path.unlink()
            print(f"Deleted {obsolete}")

    print("Updated tr.json, zh-cn.json, zh-tw.json")


if __name__ == "__main__":
    main()
