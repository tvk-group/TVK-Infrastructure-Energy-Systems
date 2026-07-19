import Image from "next/image";
import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import { BRAND } from "@/lib/brand-assets";

type LogoVariant = "header" | "footer" | "mark";

interface LogoProps {
  variant?: LogoVariant;
  href?: string;
  className?: string;
  dict?: Dictionary;
  priority?: boolean;
}

const VARIANT_CONFIG: Record<
  LogoVariant,
  { src: keyof typeof BRAND; className: string; width: number; height: number }
> = {
  header: { src: "headerLogo", className: "h-11 w-auto sm:h-12", width: 520, height: 76 },
  footer: { src: "footerLogo", className: "h-24 w-auto max-w-full", width: 640, height: 140 },
  mark: { src: "mark", className: "h-9 w-9", width: 48, height: 48 },
};

export function Logo({
  variant = "header",
  href,
  className = "",
  dict,
  priority = false,
}: LogoProps) {
  const config = VARIANT_CONFIG[variant];
  const src = BRAND[config.src];

  if (!src) return null;

  const alt =
    dict?.seo?.ogImageAlt ??
    "TVK Infrastructure & Energy Systems LTD";

  const image = (
    <Image
      src={src}
      alt={alt}
      width={config.width}
      height={config.height}
      className={`${config.className} ${className}`.trim()}
      priority={priority}
      unoptimized
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
