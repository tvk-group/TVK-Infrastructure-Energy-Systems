import { hreflangMap } from "@/i18n/config";
import { SITE_URL } from "@/i18n/config";
import type { Locale } from "@/i18n/config";
import { localizedPath } from "@/i18n/routing";

interface ArticleJsonLdProps {
  locale: Locale;
  title: string;
  description: string;
  slug: string;
  datePublished: string;
}

export function ArticleJsonLd({
  locale,
  title,
  description,
  slug,
  datePublished,
}: ArticleJsonLdProps) {
  const data = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: title,
    description,
    url: `${SITE_URL}${localizedPath(locale, "/insights")}#${slug}`,
    datePublished,
    author: { "@id": `${SITE_URL}/#organization` },
    publisher: { "@id": `${SITE_URL}/#organization` },
    inLanguage: hreflangMap[locale],
    image: `${SITE_URL}/og-image.svg`,
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}
