"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { localeNames, type Locale } from "@/i18n/config";
import { switchLocalePath } from "@/i18n/routing";

interface LanguageSwitcherProps {
  currentLocale: Locale;
  label: string;
}

export function LanguageSwitcher({ currentLocale, label }: LanguageSwitcherProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  const pathname = usePathname();

  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClick);
    return () => document.removeEventListener("mousedown", handleClick);
  }, []);

  return (
    <div className="relative" ref={ref}>
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className="inline-flex items-center gap-2 rounded border border-white/20 bg-white/5 px-3 py-2 text-sm font-medium text-white/90 hover:bg-white/10 transition-colors"
        aria-expanded={open}
        aria-haspopup="listbox"
        aria-label={label}
      >
        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418" />
        </svg>
        <span className="uppercase">{currentLocale}</span>
        <svg className={`w-3 h-3 transition-transform ${open ? "rotate-180" : ""}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {open && (
        <ul
          role="listbox"
          className="absolute right-0 top-full z-50 mt-2 max-h-80 w-56 overflow-y-auto rounded border border-silver-dark/30 bg-white shadow-xl"
        >
          {(Object.entries(localeNames) as [Locale, string][]).map(([code, name]) => (
            <li key={code} role="option" aria-selected={code === currentLocale}>
              <Link
                href={switchLocalePath(pathname, code)}
                onClick={() => setOpen(false)}
                className={`flex items-center justify-between px-4 py-2.5 text-sm transition-colors hover:bg-silver ${
                  code === currentLocale
                    ? "bg-energy/10 text-energy font-semibold"
                    : "text-navy"
                }`}
              >
                <span>{name}</span>
                <span className="text-xs uppercase text-steel">{code}</span>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
