import type { Locale } from "@/i18n/config";
import { locales } from "@/i18n/config";
import { getDictionary } from "@/i18n/get-dictionary";
import type { Dictionary } from "@/i18n/get-dictionary";

export function localeStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export async function loadPage(locale: string): Promise<{ dict: Dictionary; locale: Locale }> {
  const validLocale = locale as Locale;
  const dict = await getDictionary(validLocale);
  return { dict, locale: validLocale };
}

export function pageTitle(dict: Dictionary, title: string) {
  return dict.meta.titleTemplate.replace("%s", title);
}
