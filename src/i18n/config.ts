export const SITE_URL =
  process.env.NEXT_PUBLIC_SITE_URL ?? "https://tvk-infrastructure-energy-systems.vercel.app";

export const locales = [
  "en",
  "tr",
  "de",
  "fr",
  "es",
  "it",
  "pt",
  "nl",
  "ar",
  "ru",
  "zh-cn",
  "zh-tw",
  "ja",
  "ko",
  "hi",
  "ur",
  "pl",
  "ro",
  "el",
  "sv",
  "no",
  "da",
  "fi",
  "he",
  "id",
] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "en";

/** BCP 47 hreflang values for search engines */
export const hreflangMap: Record<Locale, string> = {
  en: "en",
  tr: "tr",
  de: "de",
  fr: "fr",
  es: "es",
  it: "it",
  pt: "pt",
  nl: "nl",
  ar: "ar",
  ru: "ru",
  "zh-cn": "zh-Hans",
  "zh-tw": "zh-Hant",
  ja: "ja",
  ko: "ko",
  hi: "hi",
  ur: "ur",
  pl: "pl",
  ro: "ro",
  el: "el",
  sv: "sv",
  no: "no",
  da: "da",
  fi: "fi",
  he: "he",
  id: "id",
};

export const localeNames: Record<Locale, string> = {
  en: "English",
  tr: "Türkçe",
  de: "Deutsch",
  fr: "Français",
  es: "Español",
  it: "Italiano",
  pt: "Português",
  nl: "Nederlands",
  ar: "العربية",
  ru: "Русский",
  "zh-cn": "简体中文",
  "zh-tw": "繁體中文",
  ja: "日本語",
  ko: "한국어",
  hi: "हिन्दी",
  ur: "اردو",
  pl: "Polski",
  ro: "Română",
  el: "Ελληνικά",
  sv: "Svenska",
  no: "Norsk",
  da: "Dansk",
  fi: "Suomi",
  he: "עברית",
  id: "Bahasa Indonesia",
};

export const rtlLocales: Locale[] = ["ar", "ur", "he"];

export function isValidLocale(locale: string): locale is Locale {
  return (locales as readonly string[]).includes(locale);
}

export const pageSlugs = [
  "",
  "about",
  "energy-systems",
  "infrastructure",
  "technology",
  "projects",
  "strategic-partnerships",
  "insights",
  "contact",
] as const;

export type PageSlug = (typeof pageSlugs)[number];

export const pageDictKeys: Record<PageSlug, string> = {
  "": "home",
  about: "about",
  "energy-systems": "energySystems",
  infrastructure: "infrastructure",
  technology: "technology",
  projects: "projects",
  "strategic-partnerships": "strategicPartnerships",
  insights: "insights",
  contact: "contact",
};
