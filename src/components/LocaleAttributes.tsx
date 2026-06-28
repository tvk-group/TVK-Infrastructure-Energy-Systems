"use client";

import { useEffect } from "react";
import { hreflangMap, rtlLocales, type Locale } from "@/i18n/config";

export function LocaleAttributes({ locale }: { locale: Locale }) {
  useEffect(() => {
    document.documentElement.lang = hreflangMap[locale];
    document.documentElement.dir = rtlLocales.includes(locale) ? "rtl" : "ltr";
  }, [locale]);

  return null;
}
