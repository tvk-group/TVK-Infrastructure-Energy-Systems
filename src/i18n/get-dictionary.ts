import type en from "../../messages/en.json";
import type { Locale } from "./config";

export type Dictionary = typeof en;

export type PageMeta = {
  title: string;
  description: string;
  keywords?: string;
  ogTitle?: string;
  ogDescription?: string;
  twitterTitle?: string;
  twitterDescription?: string;
};

const dictionaries: Record<Locale, () => Promise<Dictionary>> = {
  en: () => import("../../messages/en.json").then((m) => m.default),
  tr: () => import("../../messages/tr.json").then((m) => m.default),
  de: () => import("../../messages/de.json").then((m) => m.default),
  fr: () => import("../../messages/fr.json").then((m) => m.default),
  es: () => import("../../messages/es.json").then((m) => m.default),
  it: () => import("../../messages/it.json").then((m) => m.default),
  pt: () => import("../../messages/pt.json").then((m) => m.default),
  nl: () => import("../../messages/nl.json").then((m) => m.default),
  ar: () => import("../../messages/ar.json").then((m) => m.default),
  ru: () => import("../../messages/ru.json").then((m) => m.default),
  "zh-cn": () => import("../../messages/zh-cn.json").then((m) => m.default),
  "zh-tw": () => import("../../messages/zh-tw.json").then((m) => m.default),
  ja: () => import("../../messages/ja.json").then((m) => m.default),
  ko: () => import("../../messages/ko.json").then((m) => m.default),
  hi: () => import("../../messages/hi.json").then((m) => m.default),
  ur: () => import("../../messages/ur.json").then((m) => m.default),
  pl: () => import("../../messages/pl.json").then((m) => m.default),
  ro: () => import("../../messages/ro.json").then((m) => m.default),
  el: () => import("../../messages/el.json").then((m) => m.default),
  sv: () => import("../../messages/sv.json").then((m) => m.default),
  no: () => import("../../messages/no.json").then((m) => m.default),
  da: () => import("../../messages/da.json").then((m) => m.default),
  fi: () => import("../../messages/fi.json").then((m) => m.default),
  he: () => import("../../messages/he.json").then((m) => m.default),
  id: () => import("../../messages/id.json").then((m) => m.default),
};

export async function getDictionary(locale: Locale): Promise<Dictionary> {
  return dictionaries[locale]();
}
