import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { getNavItems } from "@/i18n/navigation";
import { localizedPath } from "@/i18n/routing";
import { appPath } from "@/lib/app-config";
import { BRAND } from "@/lib/brand-assets";
import { Logo } from "./Logo";

interface FooterProps {
  locale: Locale;
  dict: Dictionary;
}

export function Footer({ locale, dict }: FooterProps) {
  const navItems = getNavItems(locale, dict);
  const currentYear = new Date().getFullYear();
  const companyKeys = ["about", "projects", "strategicPartnerships", "insights"] as const;

  return (
    <footer className="bg-navy text-white mt-auto">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-4">
          <div className="lg:col-span-1">
            <div className="mb-6 max-w-full overflow-hidden">
              {BRAND.footerLogo ? (
                <Logo variant="footer" dict={dict} />
              ) : BRAND.headerLogo ? (
                <Logo variant="header" dict={dict} />
              ) : (
                <div>
                  <span className="font-display text-xl font-semibold tracking-tight">
                    {dict.header.brandMain}
                  </span>
                  <span className="block text-xs font-medium uppercase tracking-[0.2em] text-silver-dark mt-1">
                    {dict.header.brandSub}
                  </span>
                </div>
              )}
            </div>
            <p className="text-sm text-white/60 leading-relaxed max-w-xs">
              {dict.footer.description}
            </p>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              {dict.footer.capabilities}
            </h3>
            <ul className="space-y-2">
              {navItems.slice(2, 6).map((item) => (
                <li key={item.href}>
                  <Link href={item.href} className="text-sm text-white/60 hover:text-white transition-colors">
                    {item.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              {dict.footer.company}
            </h3>
            <ul className="space-y-2">
              {companyKeys.map((key) => (
                <li key={key}>
                  <Link
                    href={localizedPath(locale, `/${key === "strategicPartnerships" ? "strategic-partnerships" : key}`)}
                    className="text-sm text-white/60 hover:text-white transition-colors"
                  >
                    {dict.nav[key]}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              {dict.footer.connect}
            </h3>
            <p className="text-sm text-white/60 mb-4">{dict.footer.connectDescription}</p>
            <div className="space-y-3">
              <Link
                href={appPath(locale)}
                className="inline-flex items-center text-sm font-semibold text-energy-light hover:text-white transition-colors"
              >
                {dict.footer.partnerPortal}
              </Link>
              <Link
                href={localizedPath(locale, "/contact")}
                className="block text-sm font-semibold text-energy-light hover:text-white transition-colors"
              >
                {dict.footer.discussOpportunities}
              </Link>
            </div>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-white/10 flex flex-col sm:flex-row justify-between items-center gap-4">
          <p className="text-xs text-white/40">
            {dict.footer.copyright.replace("{year}", String(currentYear))}
          </p>
          <p className="text-xs text-white/40">{dict.footer.ecosystem}</p>
        </div>
      </div>
    </footer>
  );
}
