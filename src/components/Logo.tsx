import Image from "next/image";
import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import { LOGO_ASSETS } from "@/lib/logo-config";

type LogoVariant = "full-white" | "full" | "full-tagline" | "mark-white" | "mark";

interface LogoProps {
  variant?: LogoVariant;
  href?: string;
  className?: string;
  dict?: Dictionary;
  priority?: boolean;
}

const VARIANT_MAP: Record<
  LogoVariant,
  { srcKey: keyof typeof LOGO_ASSETS; widthKey: keyof typeof LOGO_ASSETS; heightKey?: keyof typeof LOGO_ASSETS; className: string }
> = {
  "full-white": { srcKey: "header", widthKey: "headerWidth", heightKey: "headerHeight", className: "h-11 w-auto sm:h-12" },
  "full-tagline": { srcKey: "footer", widthKey: "footerWidth", heightKey: "footerHeight", className: "h-24 w-auto max-w-full" },
  full: { srcKey: "header", widthKey: "headerWidth", heightKey: "headerHeight", className: "h-11 w-auto sm:h-12" },
  "mark-white": { srcKey: "mark", widthKey: "markSize", className: "h-9 w-9" },
  mark: { srcKey: "markDark", widthKey: "markSize", className: "h-9 w-9" },
};

const SVG_FALLBACK: Record<LogoVariant, { src: string; width: number; height: number; className: string }> = {
  "full-white": { src: "/logo/logo-full-white.svg", width: 520, height: 76, className: "h-11 w-auto sm:h-12" },
  "full-tagline": { src: "/logo/logo-full-tagline.svg", width: 620, height: 120, className: "h-24 w-auto max-w-full" },
  full: { src: "/logo/logo-full.svg", width: 520, height: 76, className: "h-11 w-auto sm:h-12" },
  "mark-white": { src: "/logo/logo-mark-white.svg", width: 48, height: 48, className: "h-9 w-9" },
  mark: { src: "/logo/logo-mark.svg", width: 48, height: 48, className: "h-9 w-9" },
};

export function Logo({
  variant = "full-white",
  href,
  className = "",
  dict,
  priority = false,
}: LogoProps) {
  const mapping = VARIANT_MAP[variant];
  const fallback = SVG_FALLBACK[variant];
  const useOfficial = LOGO_ASSETS.useOfficial;

  const src = useOfficial
    ? (LOGO_ASSETS[mapping.srcKey] as string)
    : fallback.src;
  const width = useOfficial
    ? (LOGO_ASSETS[mapping.widthKey] as number)
    : fallback.width;
  const height = useOfficial && mapping.heightKey
    ? (LOGO_ASSETS[mapping.heightKey] as number)
    : fallback.height;
  const sizeClass = useOfficial ? mapping.className : fallback.className;

  const alt =
    dict?.seo?.ogImageAlt ??
    "TVK Infrastructure & Energy Systems LTD";

  const image = (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height ?? width}
      className={`${sizeClass} ${className}`.trim()}
      priority={priority}
      unoptimized={useOfficial}
    />
  );

  if (href) {
    return (
      <Link href={href} className="flex shrink-0 items-center group">
        {image}
      </Link>
    );
  }

  return image;
}
