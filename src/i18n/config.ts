export const locales = [
  "en", "de", "fr", "es", "it", "pt", "nl", "pl", "ru",
  "ar", "zh", "ja", "ko", "hi", "tr", "sv", "no", "da",
  "fi", "cs", "ro", "hu", "el", "id", "vi",
] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "en";

export const localeNames: Record<Locale, string> = {
  en: "English",
  de: "Deutsch",
  fr: "Français",
  es: "Español",
  it: "Italiano",
  pt: "Português",
  nl: "Nederlands",
  pl: "Polski",
  ru: "Русский",
  ar: "العربية",
  zh: "中文",
  ja: "日本語",
  ko: "한국어",
  hi: "हिन्दी",
  tr: "Türkçe",
  sv: "Svenska",
  no: "Norsk",
  da: "Dansk",
  fi: "Suomi",
  cs: "Čeština",
  ro: "Română",
  hu: "Magyar",
  el: "Ελληνικά",
  id: "Bahasa Indonesia",
  vi: "Tiếng Việt",
};

export const rtlLocales: Locale[] = ["ar"];

export function isValidLocale(locale: string): locale is Locale {
  return locales.includes(locale as Locale);
}
