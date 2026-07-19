import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale, PageSlug } from "@/i18n/config";
import { SITE_URL, hreflangMap } from "@/i18n/config";
import { BRAND } from "@/lib/brand-assets";
import { absoluteUrl } from "@/lib/seo/metadata";
import { localizedPath } from "@/i18n/routing";

interface JsonLdProps {
  locale: Locale;
  dict: Dictionary;
  slug: PageSlug;
  breadcrumbLabels?: string[];
  article?: {
    title: string;
    description: string;
    slug: string;
    datePublished: string;
  };
}

function JsonLdScript({ data }: { data: Record<string, unknown> }) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}

export function JsonLd({ locale, dict, slug, breadcrumbLabels = [], article }: JsonLdProps) {
  const org = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": `${SITE_URL}/#organization`,
    name: dict.seo.organization.name,
    legalName: dict.seo.organization.legalName,
    url: SITE_URL,
    logo: BRAND.headerLogo
      ? `${SITE_URL}${BRAND.headerLogo}`
      : `${SITE_URL}/og-image.svg`,
    description: dict.seo.organization.description,
    sameAs: dict.seo.organization.sameAs,
    areaServed: dict.seo.organization.areaServed,
    knowsAbout: dict.seo.organization.knowsAbout,
  };

  const website = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": `${SITE_URL}/#website`,
    url: SITE_URL,
    name: dict.seo.siteName,
    description: dict.seo.websiteDescription,
    publisher: { "@id": `${SITE_URL}/#organization` },
    inLanguage: hreflangMap[locale],
    potentialAction: {
      "@type": "SearchAction",
      target: `${SITE_URL}/${locale}/insights/?q={search_term_string}`,
      "query-input": "required name=search_term_string",
    },
  };

  const breadcrumbItems = [
    { label: dict.nav.home, path: "" },
    ...breadcrumbLabels.map((label, i) => ({
      label,
      path: i === breadcrumbLabels.length - 1 ? slug : slug,
    })),
  ];

  const breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: breadcrumbItems.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.label,
      item: absoluteUrl(locale, index === 0 ? "" : slug),
    })),
  };

  const faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: dict.seo.faq.map((item) => ({
      "@type": "Question",
      name: item.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: item.answer,
      },
    })),
  };

  const schemas: Record<string, unknown>[] = [org, website, breadcrumb];

  if (slug === "") {
    schemas.push(faq);
  }

  if (article) {
    schemas.push({
      "@context": "https://schema.org",
      "@type": "Article",
      headline: article.title,
      description: article.description,
      url: `${SITE_URL}${localizedPath(locale, `/insights#${article.slug}`)}`,
      datePublished: article.datePublished,
      author: { "@id": `${SITE_URL}/#organization` },
      publisher: { "@id": `${SITE_URL}/#organization` },
      inLanguage: hreflangMap[locale],
      image: `${SITE_URL}/og-image.svg`,
    });
  }

  return (
    <>
      {schemas.map((schema, i) => (
        <JsonLdScript key={i} data={schema} />
      ))}
    </>
  );
}
