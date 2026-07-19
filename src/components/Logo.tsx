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
  header: {
    src: "headerLogo",
    className: "h-[5.5rem] w-auto max-w-full sm:h-24",
    width: 1040,
    height: 152,
  },
  footer: {
    src: "footerLogo",
    className: "h-48 w-auto max-w-full",
    width: 1280,
    height: 280,
  },
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
      <Link href={href} className="group flex min-w-0 max-w-full shrink items-center">
        {image}
      </Link>
    );
  }

  return image;
}
