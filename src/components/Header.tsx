import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { getNavItems } from "@/i18n/navigation";
import { localizedPath } from "@/i18n/routing";
import { appPath } from "@/lib/app-config";
import { LanguageSwitcher } from "./LanguageSwitcher";
import { Logo } from "./Logo";

interface HeaderProps {
  locale: Locale;
  dict: Dictionary;
}

export function Header({ locale, dict }: HeaderProps) {
  const navItems = getNavItems(locale, dict);

  return (
    <header className="sticky top-0 z-50 bg-navy border-b border-white/10">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-20 items-center justify-between gap-4">
          <Logo
            variant="full-white"
            href={localizedPath(locale)}
            dict={dict}
            priority
          />

          <nav
            className="hidden xl:flex items-center gap-1"
            aria-label={dict.header.mainNavAria}
          >
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="px-3 py-2 text-sm font-medium text-white/80 transition-colors hover:text-white hover:bg-white/5 rounded"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          <div className="flex items-center gap-3 shrink-0">
            <LanguageSwitcher currentLocale={locale} label={dict.header.mainNavAria} />
            <Link
              href={appPath(locale)}
              className="hidden lg:inline-flex items-center justify-center rounded border border-white/25 px-4 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-white/10"
            >
              {dict.header.getApp}
            </Link>
            <Link
              href={localizedPath(locale, "/contact")}
              className="hidden sm:inline-flex items-center justify-center rounded bg-energy px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
            >
              {dict.header.contact}
            </Link>
          </div>
        </div>

        <nav
          className="xl:hidden flex gap-1 overflow-x-auto pb-3 -mx-4 px-4 scrollbar-hide"
          aria-label={dict.header.mobileNavAria}
        >
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="shrink-0 px-3 py-1.5 text-xs font-medium text-white/80 transition-colors hover:text-white hover:bg-white/5 rounded whitespace-nowrap"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
