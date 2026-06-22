import type en from "../../messages/en.json";
import type { Locale } from "./config";

export type Dictionary = typeof en;

const dictionaries: Record<Locale, () => Promise<Dictionary>> = {
  en: () => import("../../messages/en.json").then((m) => m.default),
  de: () => import("../../messages/de.json").then((m) => m.default),
  fr: () => import("../../messages/fr.json").then((m) => m.default),
  es: () => import("../../messages/es.json").then((m) => m.default),
  it: () => import("../../messages/it.json").then((m) => m.default),
  pt: () => import("../../messages/pt.json").then((m) => m.default),
  nl: () => import("../../messages/nl.json").then((m) => m.default),
  pl: () => import("../../messages/pl.json").then((m) => m.default),
  ru: () => import("../../messages/ru.json").then((m) => m.default),
  ar: () => import("../../messages/ar.json").then((m) => m.default),
  zh: () => import("../../messages/zh.json").then((m) => m.default),
  ja: () => import("../../messages/ja.json").then((m) => m.default),
  ko: () => import("../../messages/ko.json").then((m) => m.default),
  hi: () => import("../../messages/hi.json").then((m) => m.default),
  tr: () => import("../../messages/tr.json").then((m) => m.default),
  sv: () => import("../../messages/sv.json").then((m) => m.default),
  no: () => import("../../messages/no.json").then((m) => m.default),
  da: () => import("../../messages/da.json").then((m) => m.default),
  fi: () => import("../../messages/fi.json").then((m) => m.default),
  cs: () => import("../../messages/cs.json").then((m) => m.default),
  ro: () => import("../../messages/ro.json").then((m) => m.default),
  hu: () => import("../../messages/hu.json").then((m) => m.default),
  el: () => import("../../messages/el.json").then((m) => m.default),
  id: () => import("../../messages/id.json").then((m) => m.default),
  vi: () => import("../../messages/vi.json").then((m) => m.default),
};

export async function getDictionary(locale: Locale): Promise<Dictionary> {
  return dictionaries[locale]();
}
