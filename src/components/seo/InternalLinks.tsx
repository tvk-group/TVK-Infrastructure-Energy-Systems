import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { localizedPath } from "@/i18n/routing";

interface InternalLinksProps {
  locale: Locale;
  dict: Dictionary;
  current?: string;
}

const linkKeys = [
  { key: "energySystems" as const, slug: "energy-systems" },
  { key: "infrastructure" as const, slug: "infrastructure" },
  { key: "technology" as const, slug: "technology" },
  { key: "projects" as const, slug: "projects" },
  { key: "strategicPartnerships" as const, slug: "strategic-partnerships" },
  { key: "insights" as const, slug: "insights" },
  { key: "contact" as const, slug: "contact" },
];

export function InternalLinks({ locale, dict, current }: InternalLinksProps) {
  const links = linkKeys.filter((l) => l.slug !== current);

  return (
    <section className="border-t border-silver bg-white">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
        <h2 className="font-display text-lg font-semibold text-navy mb-6">
          {dict.seo.internalLinksTitle}
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
          {links.map((link) => (
            <Link
              key={link.slug}
              href={localizedPath(locale, `/${link.slug}`)}
              className="text-sm text-steel hover:text-energy border border-silver px-4 py-3 transition-colors hover:border-energy/30"
            >
              {dict.nav[link.key]}
            </Link>
          ))}
        </div>
        <p className="mt-8 text-xs text-steel/70">{dict.seo.legalDisclaimer}</p>
      </div>
    </section>
  );
}
