import manifest from "../../public/brand/manifest.json";

export interface BrandManifest {
  headerLogo: string | null;
  footerLogo: string | null;
  mark: string | null;
  favicon: string | null;
  appleTouchIcon: string | null;
  icon192: string | null;
  icon512: string | null;
  ogImage: string | null;
}

const brand = manifest as BrandManifest;

function brandUrl(filename: string | null): string | null {
  return filename ? `/brand/${filename}` : null;
}

export const BRAND = {
  headerLogo: brandUrl(brand.headerLogo),
  footerLogo: brandUrl(brand.footerLogo),
  mark: brandUrl(brand.mark),
  favicon: brandUrl(brand.favicon),
  appleTouchIcon: brandUrl(brand.appleTouchIcon),
  icon192: brandUrl(brand.icon192),
  icon512: brandUrl(brand.icon512),
  ogImage: brandUrl(brand.ogImage),
} as const;
