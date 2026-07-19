import Image from "next/image";
import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";

type LogoVariant = "full-white" | "full" | "full-tagline" | "mark-white" | "mark";

interface LogoProps {
  variant?: LogoVariant;
  href?: string;
  className?: string;
  dict?: Dictionary;
  priority?: boolean;
}

const LOGO_CONFIG: Record<
  LogoVariant,
  { src: string; width: number; height: number; className: string }
> = {
  "full-white": {
    src: "/logo/logo-full-white.svg",
    width: 520,
    height: 76,
    className: "h-11 w-auto sm:h-12",
  },
  "full-tagline": {
    src: "/logo/logo-full-tagline.svg",
    width: 620,
    height: 120,
    className: "h-24 w-auto max-w-full",
  },
  full: {
    src: "/logo/logo-full.svg",
    width: 520,
    height: 76,
    className: "h-11 w-auto sm:h-12",
  },
  "mark-white": {
    src: "/logo/logo-mark-white.svg",
    width: 48,
    height: 48,
    className: "h-9 w-9",
  },
  mark: {
    src: "/logo/logo-mark.svg",
    width: 48,
    height: 48,
    className: "h-9 w-9",
  },
};

export function Logo({
  variant = "full-white",
  href,
  className = "",
  dict,
  priority = false,
}: LogoProps) {
  const config = LOGO_CONFIG[variant];
  const alt =
    dict?.seo?.ogImageAlt ??
    "TVK Infrastructure & Energy Systems LTD";

  const image = (
    <Image
      src={config.src}
      alt={alt}
      width={config.width}
      height={config.height}
      className={`${config.className} ${className}`.trim()}
      priority={priority}
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
