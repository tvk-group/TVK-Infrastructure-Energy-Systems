import { SITE_URL } from "@/i18n/config";
import type { Locale } from "@/i18n/config";
import { localizedPath } from "@/i18n/routing";

export const APP_PATH = "/app";

export function appPath(locale: Locale, subpath: string = ""): string {
  const normalized = subpath.startsWith("/") ? subpath : subpath ? `/${subpath}` : "";
  return localizedPath(locale, `${APP_PATH}${normalized}`);
}

export function appAbsoluteUrl(locale: Locale, subpath: string = ""): string {
  const path = appPath(locale, subpath);
  return `${SITE_URL}${path.endsWith("/") ? path : `${path}/`}`;
}

/** Public app entry — use /en/app/ as default install target */
export const APP_DEFAULT_URL = `${SITE_URL}/en/app/`;
