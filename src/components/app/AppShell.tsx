"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { appPath } from "@/lib/app-config";
import { localizedPath } from "@/i18n/routing";
import { Logo } from "@/components/Logo";

interface AppShellProps {
  locale: Locale;
  dict: Dictionary;
  children: React.ReactNode;
}

const navItems = [
  { key: "dashboard" as const, slug: "", icon: "home" },
  { key: "apply" as const, slug: "apply", icon: "apply" },
  { key: "projects" as const, slug: "projects", icon: "projects" },
  { key: "documents" as const, slug: "documents", icon: "documents" },
  { key: "support" as const, slug: "support", icon: "support" },
];

function NavIcon({ name }: { name: string }) {
  const cls = "w-5 h-5";
  switch (name) {
    case "home":
      return (
        <svg className={cls} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
      );
    case "apply":
      return (
        <svg className={cls} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
        </svg>
      );
    case "projects":
      return (
        <svg className={cls} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z" />
        </svg>
      );
    case "documents":
      return (
        <svg className={cls} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
        </svg>
      );
    default:
      return (
        <svg className={cls} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" />
        </svg>
      );
  }
}

export function AppShell({ locale, dict, children }: AppShellProps) {
  const pathname = usePathname();
  const t = dict.app;

  return (
    <div className="min-h-screen flex flex-col bg-silver/40">
      <header className="sticky top-0 z-40 bg-navy border-b border-white/10 safe-top">
        <div className="mx-auto max-w-lg px-4 h-14 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2.5 min-w-0">
            <Logo variant="mark-white" dict={dict} className="h-8 w-8 shrink-0" />
            <div className="min-w-0">
              <p className="font-display text-sm font-semibold text-white truncate">{t.brand}</p>
              <p className="text-[10px] uppercase tracking-wider text-white/50 truncate">{t.tagline}</p>
            </div>
          </div>
          <Link
            href={localizedPath(locale)}
            className="shrink-0 text-xs font-medium text-white/70 hover:text-white px-2 py-1 rounded hover:bg-white/5"
          >
            {t.backToSite}
          </Link>
        </div>
      </header>

      <main className="flex-1 mx-auto w-full max-w-lg px-4 py-6 pb-28">{children}</main>

      <nav
        className="fixed bottom-0 inset-x-0 z-40 bg-white border-t border-silver safe-bottom"
        aria-label={t.navAria}
      >
        <div className="mx-auto max-w-lg grid grid-cols-5">
          {navItems.map((item) => {
            const href = appPath(locale, item.slug);
            const active = pathname === href || pathname === `${href.slice(0, -1)}`;
            return (
              <Link
                key={item.key}
                href={href}
                className={`flex flex-col items-center gap-1 py-2.5 px-1 text-[10px] font-medium transition-colors ${
                  active ? "text-energy" : "text-steel hover:text-navy"
                }`}
              >
                <NavIcon name={item.icon} />
                <span className="truncate max-w-full">{t.nav[item.key]}</span>
              </Link>
            );
          })}
        </div>
      </nav>
    </div>
  );
}
