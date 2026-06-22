import type { Metadata } from "next";
import type { Locale, PageSlug } from "@/i18n/config";
import { pageDictKeys, locales } from "@/i18n/config";
import { getDictionary, type Dictionary } from "@/i18n/get-dictionary";
import { buildPageMetadata } from "@/lib/seo/metadata";

export function localeStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export async function loadPage(locale: string): Promise<{ dict: Dictionary; locale: Locale }> {
  const validLocale = locale as Locale;
  const dict = await getDictionary(validLocale);
  return { dict, locale: validLocale };
}

export async function buildMetadataForPage(
  locale: string,
  slug: PageSlug
): Promise<Metadata> {
  const { dict, locale: validLocale } = await loadPage(locale);
  const dictKey = pageDictKeys[slug] as keyof Dictionary;
  const page = dict[dictKey] as { meta: Dictionary["home"]["meta"] };
  return buildPageMetadata(validLocale, slug, page.meta, dict);
}
