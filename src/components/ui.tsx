import Link from "next/link";

interface PageHeroProps {
  title: string;
  subtitle: string;
  eyebrow?: string;
}

export function PageHero({ title, subtitle, eyebrow }: PageHeroProps) {
  return (
    <section className="relative bg-navy overflow-hidden">
      <div
        className="absolute inset-0 opacity-20"
        style={{
          backgroundImage:
            "url('https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1920&q=80')",
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
        aria-hidden="true"
      />
      <div className="hero-overlay absolute inset-0" aria-hidden="true" />
      <div className="industrial-grid absolute inset-0 opacity-30" aria-hidden="true" />

      <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-20 sm:py-28">
        {eyebrow && (
          <p className="text-sm font-semibold uppercase tracking-[0.2em] text-energy-light mb-4">
            {eyebrow}
          </p>
        )}
        <h1 className="font-display text-4xl sm:text-5xl lg:text-6xl font-semibold text-white max-w-4xl leading-tight">
          {title}
        </h1>
        <p className="mt-6 text-lg sm:text-xl text-white/75 max-w-3xl leading-relaxed">
          {subtitle}
        </p>
      </div>
    </section>
  );
}

interface CTABannerProps {
  title: string;
  description: string;
  primaryLabel: string;
  primaryHref: string;
  secondaryLabel?: string;
  secondaryHref?: string;
}

export function CTABanner({
  title,
  description,
  primaryLabel,
  primaryHref,
  secondaryLabel,
  secondaryHref,
}: CTABannerProps) {
  return (
    <section className="bg-navy-mid">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-8">
          <div className="max-w-2xl">
            <h2 className="font-display text-2xl sm:text-3xl font-semibold text-white">
              {title}
            </h2>
            <p className="mt-4 text-white/70 leading-relaxed">{description}</p>
          </div>
          <div className="flex flex-col sm:flex-row gap-4 shrink-0">
            <Link
              href={primaryHref}
              className="inline-flex items-center justify-center rounded bg-energy px-8 py-3.5 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
            >
              {primaryLabel}
            </Link>
            {secondaryLabel && secondaryHref && (
              <Link
                href={secondaryHref}
                className="inline-flex items-center justify-center rounded border border-white/30 px-8 py-3.5 text-sm font-semibold text-white transition-colors hover:bg-white/10"
              >
                {secondaryLabel}
              </Link>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

interface SectionProps {
  title: string;
  subtitle?: string;
  children: React.ReactNode;
  className?: string;
  id?: string;
}

export function Section({ title, subtitle, children, className = "", id }: SectionProps) {
  return (
    <section id={id} className={`py-16 sm:py-20 ${className}`}>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="mb-12">
          <div className="section-divider mb-6" />
          <h2 className="font-display text-3xl sm:text-4xl font-semibold text-navy">
            {title}
          </h2>
          {subtitle && (
            <p className="mt-4 text-lg text-steel max-w-3xl leading-relaxed">
              {subtitle}
            </p>
          )}
        </div>
        {children}
      </div>
    </section>
  );
}

interface FeatureCardProps {
  title: string;
  description: string;
  items?: string[];
}

export function FeatureCard({ title, description, items }: FeatureCardProps) {
  return (
    <div className="group border border-silver bg-white p-8 transition-shadow hover:shadow-lg">
      <div className="w-12 h-1 bg-energy mb-6 group-hover:bg-accent-green transition-colors" />
      <h3 className="font-display text-xl font-semibold text-navy mb-3">
        {title}
      </h3>
      <p className="text-steel leading-relaxed mb-4">{description}</p>
      {items && (
        <ul className="space-y-2">
          {items.map((item) => (
            <li
              key={item}
              className="flex items-start gap-2 text-sm text-steel"
            >
              <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-accent-green" />
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

interface InfoBlockProps {
  label: string;
  title: string;
  description: string;
}

export function InfoBlock({ label, title, description }: InfoBlockProps) {
  return (
    <div className="border-l-4 border-energy pl-6 py-2">
      <p className="text-xs font-semibold uppercase tracking-wider text-energy mb-2">
        {label}
      </p>
      <h3 className="font-display text-xl font-semibold text-navy mb-2">
        {title}
      </h3>
      <p className="text-steel leading-relaxed mt-2">{description}</p>
    </div>
  );
}
