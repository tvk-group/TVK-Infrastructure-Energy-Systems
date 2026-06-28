import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { appPath } from "@/lib/app-config";

interface PartnerAppSectionProps {
  locale: Locale;
  dict: Dictionary;
}

export function PartnerAppSection({ locale, dict }: PartnerAppSectionProps) {
  const t = dict.app.install;

  return (
    <section className="bg-navy text-white">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-energy-light mb-4">
              {t.eyebrow}
            </p>
            <h2 className="font-display text-3xl sm:text-4xl font-semibold leading-tight">{t.title}</h2>
            <p className="mt-6 text-lg text-white/75 leading-relaxed">{t.subtitle}</p>
            <div className="mt-8 flex flex-col sm:flex-row gap-4">
              <Link
                href={appPath(locale)}
                className="inline-flex items-center justify-center rounded bg-energy px-8 py-4 text-sm font-semibold text-white hover:bg-energy-light transition-colors"
              >
                {t.openApp} →
              </Link>
              <a
                href="#install-instructions"
                className="inline-flex items-center justify-center rounded border border-white/30 px-8 py-4 text-sm font-semibold text-white hover:bg-white/10 transition-colors"
              >
                {t.howToInstall}
              </a>
            </div>
          </div>

          <div id="install-instructions" className="space-y-4">
            {(
              [
                { title: t.iphone.title, steps: t.iphone.steps, icon: "📱" },
                { title: t.android.title, steps: t.android.steps, icon: "🤖" },
                { title: t.desktop.title, steps: t.desktop.steps, icon: "🖥" },
              ] as const
            ).map((item) => (
              <div key={item.title} className="border border-white/15 bg-white/5 p-6">
                <div className="flex items-start gap-4">
                  <span className="text-2xl" aria-hidden="true">
                    {item.icon}
                  </span>
                  <div>
                    <h3 className="font-display text-base font-semibold text-white">{item.title}</h3>
                    <p className="mt-2 text-sm text-white/65 leading-relaxed">{item.steps}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
