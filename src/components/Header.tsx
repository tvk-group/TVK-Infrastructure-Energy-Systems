import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { getNavItems } from "@/i18n/navigation";
import { localizedPath } from "@/i18n/routing";
import { appPath } from "@/lib/app-config";
import { BRAND } from "@/lib/brand-assets";
import { LanguageSwitcher } from "./LanguageSwitcher";
import { Logo } from "./Logo";

interface HeaderProps {
  locale: Locale;
  dict: Dictionary;
}

export function Header({ locale, dict }: HeaderProps) {
  const navItems = getNavItems(locale, dict);

  return (
    <header className="sticky top-0 z-50 overflow-x-clip border-b border-white/10 bg-navy">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex min-h-36 items-center justify-between gap-3 py-2 sm:min-h-40">
          <div className="min-w-0 max-w-[min(48%,21rem)] shrink sm:max-w-[min(52%,24rem)] xl:max-w-[27rem]">
            {BRAND.headerLogo ? (
              <Logo variant="header" href={localizedPath(locale)} dict={dict} priority />
            ) : (
              <Link href={localizedPath(locale)} className="group flex shrink-0 flex-col">
                <span className="font-display text-lg font-semibold tracking-tight text-white sm:text-xl">
                  {dict.header.brandMain}
                </span>
                <span className="text-[10px] font-medium uppercase tracking-[0.2em] text-silver-dark sm:text-xs">
                  {dict.header.brandSub}
                </span>
              </Link>
            )}
          </div>

          <nav
            className="hidden min-w-0 flex-1 items-center justify-center gap-0.5 overflow-x-auto scrollbar-hide xl:flex"
            aria-label={dict.header.mainNavAria}
          >
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="shrink rounded px-2 py-2 text-xs font-medium text-white/80 transition-colors hover:bg-white/5 hover:text-white 2xl:px-3 2xl:text-sm"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          <div className="flex shrink-0 items-center gap-2 sm:gap-3">
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
          className="flex max-w-full gap-1 overflow-x-auto pb-3 scrollbar-hide xl:hidden"
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
