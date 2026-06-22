import type { Dictionary } from "./get-dictionary";
import type { Locale } from "./config";
import { localizedPath } from "./routing";

const icons = ["energy", "infrastructure", "intelligence", "industrial", "ai", "investment"] as const;

export function getNavItems(locale: Locale, dict: Dictionary) {
  const items = [
    { key: "home", path: "" },
    { key: "about", path: "/about" },
    { key: "energySystems", path: "/energy-systems" },
    { key: "infrastructure", path: "/infrastructure" },
    { key: "technology", path: "/technology" },
    { key: "projects", path: "/projects" },
    { key: "strategicPartnerships", path: "/strategic-partnerships" },
    { key: "insights", path: "/insights" },
    { key: "contact", path: "/contact" },
  ] as const;

  return items.map((item) => ({
    label: dict.nav[item.key],
    href: localizedPath(locale, item.path),
  }));
}

export function getCoreAreas(locale: Locale, dict: Dictionary) {
  return dict.coreAreas.map((area, index) => ({
    ...area,
    href: localizedPath(locale, area.href),
    icon: icons[index] ?? "energy",
  }));
}
