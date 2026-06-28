import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { getCoreAreas } from "@/i18n/navigation";
import { localizedPath } from "@/i18n/routing";
import { appPath } from "@/lib/app-config";

const icons: Record<string, React.ReactNode> = {
  energy: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
    </svg>
  ),
  infrastructure: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008z" />
    </svg>
  ),
  intelligence: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" />
    </svg>
  ),
  industrial: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M11.42 15.17L17.25 21A2.652 2.652 0 0021 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 11-3.586-3.586l6.837-5.51m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 004.486-6.336l-3.276 3.277a3.004 3.004 0 01-2.25-2.25l3.276-3.276a4.5 4.5 0 00-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085m-1.745 1.437L5.909 7.5H4.5L2.25 3.75l1.5-1.5L7.5 4.5v1.409l4.26 4.26m-1.745 1.437l1.37-1.37a2.25 2.25 0 013.182 0l2.829 2.829a2.25 2.25 0 010 3.182l-1.37 1.37" />
    </svg>
  ),
  ai: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
    </svg>
  ),
  investment: (
    <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" />
    </svg>
  ),
};

interface HomeSectionsProps {
  locale: Locale;
  dict: Dictionary;
}

export function CoreAreas({ locale, dict }: HomeSectionsProps) {
  const areas = getCoreAreas(locale, dict);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {areas.map((area) => (
        <Link
          key={area.title}
          href={area.href}
          className="group flex flex-col border border-silver bg-white p-8 transition-all hover:border-energy/30 hover:shadow-lg"
        >
          <div className="text-energy group-hover:text-accent-green transition-colors mb-6">
            {icons[area.icon]}
          </div>
          <h3 className="font-display text-xl font-semibold text-navy mb-3 group-hover:text-energy transition-colors">
            {area.title}
          </h3>
          <p className="text-steel leading-relaxed flex-grow">{area.description}</p>
          <span className="mt-6 text-sm font-semibold text-energy group-hover:text-energy-light transition-colors">
            {dict.common.learnMore}
          </span>
        </Link>
      ))}
    </div>
  );
}

export function Hero({ locale, dict }: HomeSectionsProps) {
  const t = dict.home.hero;

  return (
    <section className="relative min-h-[85vh] flex items-center overflow-hidden bg-navy">
      <div
        className="absolute inset-0"
        style={{
          backgroundImage: "url('https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1920&q=80')",
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
        aria-hidden="true"
      />
      <div className="hero-overlay absolute inset-0" aria-hidden="true" />
      <div className="industrial-grid absolute inset-0 opacity-20" aria-hidden="true" />

      <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-24 sm:py-32 w-full">
        <div className="max-w-3xl">
          <p className="text-sm font-semibold uppercase tracking-[0.25em] text-energy-light mb-6">{t.eyebrow}</p>
          <h1 className="font-display text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-semibold text-white leading-[1.1]">
            {t.titleLine1}
            <br />
            <span className="text-energy-light">{t.titleLine2}</span>
          </h1>
          <p className="mt-8 text-lg sm:text-xl text-white/80 leading-relaxed max-w-2xl">{t.subtitle}</p>
          <div className="mt-10 flex flex-col sm:flex-row gap-4">
            <Link
              href={localizedPath(locale, "/energy-systems")}
              className="inline-flex items-center justify-center rounded bg-energy px-8 py-4 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
            >
              {t.exploreCapabilities}
            </Link>
            <Link
              href={localizedPath(locale, "/strategic-partnerships")}
              className="inline-flex items-center justify-center rounded border border-white/40 px-8 py-4 text-sm font-semibold text-white transition-colors hover:bg-white/10"
            >
              {t.strategicPartnershipInquiry}
            </Link>
            <Link
              href={appPath(locale)}
              className="inline-flex items-center justify-center rounded border border-energy/50 bg-energy/20 px-8 py-4 text-sm font-semibold text-white transition-colors hover:bg-energy/30"
            >
              {dict.header.getApp}
            </Link>
          </div>
        </div>

        <div className="mt-16 grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-4xl">
          {t.tags.map((label) => (
            <div key={label} className="border border-white/20 bg-white/5 backdrop-blur-sm px-4 py-3 text-center">
              <span className="text-xs font-medium uppercase tracking-wider text-white/70">{label}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
