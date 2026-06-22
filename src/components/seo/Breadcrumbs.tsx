import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { localizedPath } from "@/i18n/routing";

interface BreadcrumbsProps {
  locale: Locale;
  dict: Dictionary;
  items: { label: string; href?: string }[];
}

export function Breadcrumbs({ locale, dict, items }: BreadcrumbsProps) {
  return (
    <nav aria-label={dict.seo.breadcrumbAria} className="bg-silver/50 border-b border-silver">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-3">
        <ol className="flex flex-wrap items-center gap-2 text-sm text-steel">
          <li>
            <Link href={localizedPath(locale)} className="hover:text-energy transition-colors">
              {dict.nav.home}
            </Link>
          </li>
          {items.map((item, index) => (
            <li key={`${item.label}-${index}`} className="flex items-center gap-2">
              <span aria-hidden="true">/</span>
              {item.href ? (
                <Link href={item.href} className="hover:text-energy transition-colors">
                  {item.label}
                </Link>
              ) : (
                <span className="text-navy font-medium" aria-current="page">
                  {item.label}
                </span>
              )}
            </li>
          ))}
        </ol>
      </div>
    </nav>
  );
}
