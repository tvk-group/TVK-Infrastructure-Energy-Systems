import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { appPath } from "@/lib/app-config";
import { localizedPath } from "@/i18n/routing";
import { AppApplyForm } from "@/components/app/AppApplyForm";

type PageProps = { dict: Dictionary; locale: Locale };

function StatusBadge({ label, variant }: { label: string; variant: "pending" | "active" | "development" }) {
  const colors = {
    pending: "bg-amber-100 text-amber-800 border-amber-200",
    active: "bg-accent-green/10 text-accent-green border-accent-green/20",
    development: "bg-energy/10 text-energy border-energy/20",
  };
  return (
    <span className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium ${colors[variant]}`}>
      {label}
    </span>
  );
}

export function AppDashboardView({ dict, locale }: PageProps) {
  const t = dict.app.dashboard;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold text-navy">{t.title}</h1>
        <p className="mt-2 text-sm text-steel">{t.subtitle}</p>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {t.stats.map((item) => (
          <div key={item.label} className="rounded-lg border border-silver bg-white p-4">
            <p className="text-xs font-medium uppercase tracking-wider text-steel">{item.label}</p>
            <p className="mt-1 font-display text-xl font-semibold text-navy">{item.value}</p>
          </div>
        ))}
      </div>

      <div className="rounded-lg border border-silver bg-white p-5">
        <div className="flex items-center justify-between gap-3 mb-4">
          <h2 className="font-display text-base font-semibold text-navy">{t.partnershipStatus.title}</h2>
          <StatusBadge label={t.partnershipStatus.badge} variant="development" />
        </div>
        <p className="text-sm text-steel">{t.partnershipStatus.description}</p>
      </div>

      <div className="rounded-lg border border-silver bg-white p-5">
        <h2 className="font-display text-base font-semibold text-navy mb-4">{t.nextSteps.title}</h2>
        <ol className="space-y-3">
          {t.nextSteps.items.map((step, i) => (
            <li key={step} className="flex gap-3 text-sm text-steel">
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-energy/10 text-xs font-semibold text-energy">
                {i + 1}
              </span>
              {step}
            </li>
          ))}
        </ol>
      </div>

      <Link
        href={appPath(locale, "apply")}
        className="block w-full rounded-lg bg-energy px-4 py-3.5 text-center text-sm font-semibold text-white hover:bg-energy-light transition-colors"
      >
        {t.cta}
      </Link>
    </div>
  );
}

export function AppApplyView({ dict }: PageProps) {
  const t = dict.app.apply;
  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold text-navy">{t.title}</h1>
        <p className="mt-2 text-sm text-steel">{t.subtitle}</p>
      </div>
      <div className="rounded-lg border border-silver bg-white p-5">
        <AppApplyForm dict={dict} />
      </div>
    </div>
  );
}

export function AppProjectsView({ dict }: PageProps) {
  const t = dict.app.projects;
  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold text-navy">{t.title}</h1>
        <p className="mt-2 text-sm text-steel">{t.subtitle}</p>
      </div>
      <div className="space-y-3">
        {t.items.map((item) => (
          <div key={item.title} className="rounded-lg border border-silver bg-white p-5">
            <div className="flex items-start justify-between gap-3 mb-2">
              <h2 className="font-display text-base font-semibold text-navy">{item.title}</h2>
              <StatusBadge
                label={item.stage}
                variant={item.stageKey === "active" ? "active" : "development"}
              />
            </div>
            <p className="text-sm text-steel">{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export function AppDocumentsView({ dict, locale }: PageProps) {
  const t = dict.app.documents;
  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold text-navy">{t.title}</h1>
        <p className="mt-2 text-sm text-steel">{t.subtitle}</p>
      </div>
      <div className="space-y-3">
        {t.items.map((item) => (
          <Link
            key={item.title}
            href={localizedPath(locale, item.href)}
            className="block rounded-lg border border-silver bg-white p-5 hover:border-energy/30 transition-colors"
          >
            <h2 className="font-display text-base font-semibold text-navy">{item.title}</h2>
            <p className="mt-1 text-sm text-steel">{item.description}</p>
            <span className="mt-3 inline-block text-xs font-semibold text-energy">{t.openLabel} →</span>
          </Link>
        ))}
      </div>
    </div>
  );
}

export function AppSupportView({ dict }: PageProps) {
  const t = dict.app.support;
  return (
    <div className="space-y-6">
      <div>
        <h1 className="font-display text-2xl font-semibold text-navy">{t.title}</h1>
        <p className="mt-2 text-sm text-steel">{t.subtitle}</p>
      </div>
      <div className="space-y-3">
        {t.channels.map((channel) => (
          <div key={channel.email} className="rounded-lg border border-silver bg-white p-5">
            <h2 className="font-display text-base font-semibold text-navy">{channel.title}</h2>
            <p className="mt-1 text-sm text-steel">{channel.description}</p>
            <a href={`mailto:${channel.email}`} className="mt-3 inline-block text-sm font-semibold text-energy">
              {channel.email}
            </a>
          </div>
        ))}
      </div>
      <p className="text-xs text-steel/70">{t.disclaimer}</p>
    </div>
  );
}
