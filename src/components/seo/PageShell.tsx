import type { ReactNode } from "react";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale, PageSlug } from "@/i18n/config";
import { JsonLd } from "@/components/seo/JsonLd";
import { Breadcrumbs } from "@/components/seo/Breadcrumbs";
import { InternalLinks } from "@/components/seo/InternalLinks";
import { localizedPath } from "@/i18n/routing";

interface PageShellProps {
  locale: Locale;
  dict: Dictionary;
  slug: PageSlug;
  breadcrumbLabel?: string;
  children: ReactNode;
  showFaqSchema?: boolean;
}

export function PageShell({
  locale,
  dict,
  slug,
  breadcrumbLabel,
  children,
}: PageShellProps) {
  return (
    <>
      <JsonLd
        locale={locale}
        dict={dict}
        slug={slug}
        breadcrumbLabels={breadcrumbLabel ? [breadcrumbLabel] : []}
      />
      {breadcrumbLabel && (
        <Breadcrumbs
          locale={locale}
          dict={dict}
          items={[{ label: breadcrumbLabel }]}
        />
      )}
      {children}
      <InternalLinks locale={locale} dict={dict} current={slug || undefined} />
    </>
  );
}

export function insightArticleUrl(locale: Locale, slug: string) {
  return `${localizedPath(locale, "/insights")}#${slug}`;
}
