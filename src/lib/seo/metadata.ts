import type { Metadata } from "next";
import {
  SITE_URL,
  hreflangMap,
  locales,
  type Locale,
  type PageSlug,
  pageSlugs,
} from "@/i18n/config";
import { BRAND } from "@/lib/brand-assets";
import type { Dictionary, PageMeta } from "@/i18n/get-dictionary";
import { localizedPath } from "@/i18n/routing";

const OG_IMAGE = BRAND.ogImage ? `${SITE_URL}${BRAND.ogImage}` : `${SITE_URL}/og-image.svg`;
const TWITTER_HANDLE = "@TVKInfraEnergy";

export function absoluteUrl(locale: Locale, slug: PageSlug = ""): string {
  const path = localizedPath(locale, slug ? `/${slug}` : "");
  return `${SITE_URL}${path.endsWith("/") ? path : `${path}/`}`;
}

export function buildAlternateLanguages(slug: PageSlug): Record<string, string> {
  const languages: Record<string, string> = {};
  for (const locale of locales) {
    languages[hreflangMap[locale]] = absoluteUrl(locale, slug);
  }
  languages["x-default"] = absoluteUrl("en", slug);
  return languages;
}

export function buildPageMetadata(
  locale: Locale,
  slug: PageSlug,
  meta: PageMeta,
  dict: Dictionary
): Metadata {
  const url = absoluteUrl(locale, slug);
  const title = meta.title;
  const description = meta.description;
  const ogTitle = meta.ogTitle ?? title;
  const ogDescription = meta.ogDescription ?? description;
  const twitterTitle = meta.twitterTitle ?? ogTitle;
  const twitterDescription = meta.twitterDescription ?? ogDescription;
  const keywords = meta.keywords ?? dict.seo.defaultKeywords;

  return {
    title,
    description,
    keywords,
    alternates: {
      canonical: url,
      languages: buildAlternateLanguages(slug),
    },
    openGraph: {
      type: slug === "insights" ? "article" : "website",
      locale: hreflangMap[locale].replace("-", "_"),
      url,
      title: ogTitle,
      description: ogDescription,
      siteName: dict.seo.siteName,
      images: [
        {
          url: OG_IMAGE,
          width: 1200,
          height: 630,
          alt: dict.seo.ogImageAlt,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      site: TWITTER_HANDLE,
      title: twitterTitle,
      description: twitterDescription,
      images: [OG_IMAGE],
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-image-preview": "large",
        "max-snippet": -1,
      },
    },
    other: {
      "bingbot": "index,follow",
      "yandex": "index,follow",
      "baiduspider": "index,follow",
    },
  };
}

export function getAllPageUrls(): { locale: Locale; slug: PageSlug; url: string }[] {
  const urls: { locale: Locale; slug: PageSlug; url: string }[] = [];
  for (const locale of locales) {
    for (const slug of pageSlugs) {
      urls.push({ locale, slug, url: absoluteUrl(locale, slug) });
    }
  }
  return urls;
}
