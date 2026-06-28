import Link from "next/link";
import type { Dictionary } from "@/i18n/get-dictionary";
import type { Locale } from "@/i18n/config";
import { localizedPath } from "@/i18n/routing";
import { Hero, CoreAreas } from "@/components/HomeSections";
import { PartnerAppSection } from "@/components/app/PartnerAppSection";
import { ContactForm } from "@/components/ContactForm";
import { PageHero, Section, FeatureCard, CTABanner, InfoBlock } from "@/components/ui";

type PageProps = { dict: Dictionary; locale: Locale };

export function HomeView({ dict, locale }: PageProps) {
  const t = dict.home;
  return (
    <>
      <Hero locale={locale} dict={dict} />
      <Section title={t.coreAreas.title} subtitle={t.coreAreas.subtitle} className="bg-white">
        <CoreAreas locale={locale} dict={dict} />
      </Section>
      <section className="bg-silver industrial-grid">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <div className="section-divider mb-6" />
              <h2 className="font-display text-3xl sm:text-4xl font-semibold text-navy">{t.longTerm.title}</h2>
              <p className="mt-6 text-lg text-steel leading-relaxed">{t.longTerm.paragraph1}</p>
              <p className="mt-4 text-steel leading-relaxed">{t.longTerm.paragraph2}</p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {dict.developmentStages.map((stage) => (
                <div key={stage} className="border border-silver-dark/50 bg-white p-6 flex items-center gap-4">
                  <div className="w-2 h-2 rounded-full bg-accent-green shrink-0" />
                  <span className="text-sm font-medium text-navy">{stage}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
      <section className="bg-white">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {t.stats.map((item) => (
              <div key={item.stat} className="text-center p-8 border border-silver">
                <p className="font-display text-4xl font-semibold text-energy mb-2">{item.stat}</p>
                <p className="text-sm font-semibold uppercase tracking-wider text-navy mb-3">{item.label}</p>
                <p className="text-sm text-steel">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
      <CTABanner
        title={t.cta.title}
        description={t.cta.description}
        primaryLabel={t.cta.primaryLabel}
        primaryHref={localizedPath(locale, "/strategic-partnerships")}
        secondaryLabel={t.cta.secondaryLabel}
        secondaryHref={localizedPath(locale, "/contact")}
      />
      <PartnerAppSection locale={locale} dict={dict} />
    </>
  );
}

export function AboutView({ dict, locale }: PageProps) {
  const t = dict.about;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.mission.title} subtitle={t.mission.subtitle}>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <InfoBlock label={t.mission.missionLabel} title={t.mission.missionTitle} description={t.mission.missionDescription} />
          <InfoBlock label={t.mission.visionLabel} title={t.mission.visionTitle} description={t.mission.visionDescription} />
        </div>
      </Section>
      <Section title={t.strategy.title} subtitle={t.strategy.subtitle} className="bg-silver">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {t.strategy.items.map((item) => (
            <div key={item.title} className="bg-white border border-silver-dark/50 p-8">
              <div className="w-12 h-1 bg-energy mb-6" />
              <h3 className="font-display text-lg font-semibold text-navy mb-3">{item.title}</h3>
              <p className="text-steel text-sm leading-relaxed">{item.description}</p>
            </div>
          ))}
        </div>
      </Section>
      <Section title={t.developmentStage.title}>
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-6">{t.developmentStage.paragraph1}</p>
          <p className="text-steel leading-relaxed">{t.developmentStage.paragraph2}</p>
        </div>
      </Section>
      <CTABanner
        title={t.cta.title}
        description={t.cta.description}
        primaryLabel={t.cta.primaryLabel}
        primaryHref={localizedPath(locale, "/contact")}
        secondaryLabel={t.cta.secondaryLabel}
        secondaryHref={localizedPath(locale, "/strategic-partnerships")}
      />
    </>
  );
}

export function EnergySystemsView({ dict, locale }: PageProps) {
  const t = dict.energySystems;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.capabilityAreas.title} subtitle={t.capabilityAreas.subtitle}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {t.capabilityAreas.cards.map((card) => (
            <FeatureCard key={card.title} title={card.title} description={card.description} items={card.items} />
          ))}
        </div>
      </Section>
      <Section title={t.approach.title} subtitle={t.approach.subtitle} className="bg-silver">
        <div className="max-w-3xl">
          <p className="text-steel leading-relaxed mb-4">{t.approach.paragraph1}</p>
          <p className="text-steel leading-relaxed">{t.approach.paragraph2}</p>
        </div>
      </Section>
      <CTABanner title={t.cta.title} description={t.cta.description} primaryLabel={t.cta.primaryLabel} primaryHref={localizedPath(locale, "/contact")} />
    </>
  );
}

export function InfrastructureView({ dict, locale }: PageProps) {
  const t = dict.infrastructure;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.focusAreas.title} subtitle={t.focusAreas.subtitle}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {t.focusAreas.cards.map((card) => (
            <FeatureCard key={card.title} title={card.title} description={card.description} items={card.items} />
          ))}
        </div>
      </Section>
      <Section title={t.vision.title} className="bg-silver">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          <div>
            <p className="text-lg text-steel leading-relaxed mb-4">{t.vision.paragraph1}</p>
            <p className="text-steel leading-relaxed">{t.vision.paragraph2}</p>
          </div>
          <div className="border border-silver-dark/50 bg-white p-8">
            <h3 className="font-display text-lg font-semibold text-navy mb-4">{dict.common.currentStage}</h3>
            <ul className="space-y-3">
              {t.vision.currentStageItems.map((item) => (
                <li key={item} className="flex items-start gap-3 text-sm text-steel">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-energy" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </Section>
      <CTABanner title={t.cta.title} description={t.cta.description} primaryLabel={t.cta.primaryLabel} primaryHref={localizedPath(locale, "/contact")} />
    </>
  );
}

export function TechnologyView({ dict, locale }: PageProps) {
  const t = dict.technology;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.focusAreas.title} subtitle={t.focusAreas.subtitle}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {t.focusAreas.cards.map((card) => (
            <FeatureCard key={card.title} title={card.title} description={card.description} items={card.items} />
          ))}
        </div>
      </Section>
      <Section title={t.philosophy.title} className="bg-silver">
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-4">{t.philosophy.paragraph1}</p>
          <p className="text-steel leading-relaxed">{t.philosophy.paragraph2}</p>
        </div>
      </Section>
      <CTABanner title={t.cta.title} description={t.cta.description} primaryLabel={t.cta.primaryLabel} primaryHref={localizedPath(locale, "/contact")} />
    </>
  );
}

export function ProjectsView({ dict, locale }: PageProps) {
  const t = dict.projects;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.categories.title} subtitle={t.categories.subtitle}>
        <div className="space-y-8">
          {t.categories.items.map((project) => (
            <div key={project.category} className="border border-silver bg-white overflow-hidden">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-navy px-8 py-5">
                <h3 className="font-display text-xl font-semibold text-white">{project.category}</h3>
                <span className="inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-energy-light">
                  <span className="h-2 w-2 rounded-full bg-accent-green-light animate-pulse" />
                  {project.status}
                </span>
              </div>
              <div className="p-8">
                <p className="text-steel leading-relaxed mb-6">{project.description}</p>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {project.areas.map((area) => (
                    <div key={area} className="flex items-start gap-3 text-sm text-steel bg-silver/50 px-4 py-3">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-energy" />
                      {area}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </Section>
      <Section title={t.transparency.title} className="bg-silver">
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-4">{t.transparency.paragraph1}</p>
          <p className="text-steel leading-relaxed">{t.transparency.paragraph2}</p>
        </div>
      </Section>
      <CTABanner
        title={t.cta.title}
        description={t.cta.description}
        primaryLabel={t.cta.primaryLabel}
        primaryHref={localizedPath(locale, "/strategic-partnerships")}
        secondaryLabel={t.cta.secondaryLabel}
        secondaryHref={localizedPath(locale, "/contact")}
      />
    </>
  );
}

export function PartnershipsView({ dict, locale }: PageProps) {
  const t = dict.strategicPartnerships;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.objectives.title} subtitle={t.objectives.subtitle}>
        <div className="max-w-3xl mb-12">
          <p className="text-steel leading-relaxed">{t.objectives.intro}</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {t.objectives.collaborationAreas.map((area) => (
            <div key={area} className="flex items-start gap-4 border border-silver bg-white p-6">
              <div className="w-8 h-8 shrink-0 rounded bg-energy/10 flex items-center justify-center">
                <svg className="w-4 h-4 text-energy" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span className="text-sm font-medium text-navy">{area}</span>
            </div>
          ))}
        </div>
      </Section>
      <Section title={t.partners.title} className="bg-silver">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {t.partners.items.map((partner) => (
            <FeatureCard key={partner.title} title={partner.title} description={partner.description} />
          ))}
        </div>
      </Section>
      <Section title={t.engage.title}>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {t.engage.steps.map((item) => (
            <div key={item.step} className="relative border border-silver bg-white p-8">
              <span className="font-display text-5xl font-bold text-silver-dark/50 absolute top-4 right-6">{item.step}</span>
              <h3 className="font-display text-lg font-semibold text-navy mb-3 relative">{item.title}</h3>
              <p className="text-sm text-steel leading-relaxed relative">{item.description}</p>
            </div>
          ))}
        </div>
      </Section>
      <CTABanner title={t.cta.title} description={t.cta.description} primaryLabel={t.cta.primaryLabel} primaryHref={localizedPath(locale, "/contact")} />
    </>
  );
}

export function InsightsView({ dict, locale }: PageProps) {
  const t = dict.insights;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.topics.title} subtitle={t.topics.subtitle}>
        <div className="flex flex-wrap gap-2 mb-12">
          {t.topics.filters.map((topic, i) => (
            <span
              key={topic}
              className={`px-4 py-2 text-sm font-medium border ${
                i === 0 ? "bg-navy text-white border-navy" : "bg-white text-steel border-silver-dark"
              }`}
            >
              {topic}
            </span>
          ))}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {t.topics.items.map((insight) => (
            <article key={insight.title} className="group border border-silver bg-white p-8 transition-shadow hover:shadow-lg">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-xs font-semibold uppercase tracking-wider text-energy">{insight.topic}</span>
                <span className="text-xs text-steel/60">·</span>
                <span className="text-xs text-steel/60">{insight.date}</span>
              </div>
              <h3 className="font-display text-xl font-semibold text-navy mb-3 group-hover:text-energy transition-colors">{insight.title}</h3>
              <p className="text-steel text-sm leading-relaxed">{insight.excerpt}</p>
            </article>
          ))}
        </div>
        <p className="mt-12 text-sm text-steel/70 text-center max-w-2xl mx-auto">{t.topics.disclaimer}</p>
      </Section>
      <Section title={t.stayInformed.title} className="bg-silver">
        <div className="max-w-2xl mx-auto text-center">
          <p className="text-steel leading-relaxed mb-6">{t.stayInformed.description}</p>
          <Link href={localizedPath(locale, "/contact")} className="inline-flex items-center justify-center rounded bg-energy px-8 py-3.5 text-sm font-semibold text-white transition-colors hover:bg-energy-light">
            {t.stayInformed.button}
          </Link>
        </div>
      </Section>
      <CTABanner
        title={t.cta.title}
        description={t.cta.description}
        primaryLabel={t.cta.primaryLabel}
        primaryHref={localizedPath(locale, "/energy-systems")}
        secondaryLabel={t.cta.secondaryLabel}
        secondaryHref={localizedPath(locale, "/about")}
      />
    </>
  );
}

export function ContactView({ dict }: PageProps) {
  const t = dict.contact;
  return (
    <>
      <PageHero eyebrow={t.hero.eyebrow} title={t.hero.title} subtitle={t.hero.subtitle} />
      <Section title={t.section.title}>
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-12">
          <div className="lg:col-span-2">
            <p className="text-steel leading-relaxed mb-8">{t.section.intro}</p>
            <div className="space-y-6">
              {t.section.inquiryTypes.map((item) => (
                <div key={item.title} className="border-l-4 border-energy pl-5">
                  <h3 className="font-display text-sm font-semibold text-navy mb-1">{item.title}</h3>
                  <p className="text-sm text-steel">{item.description}</p>
                </div>
              ))}
            </div>
            <div className="mt-10 p-6 bg-silver border border-silver-dark/30">
              <p className="text-xs font-semibold uppercase tracking-wider text-steel mb-2">{t.section.companyName}</p>
              <p className="text-sm text-steel">{t.section.ecosystem}</p>
            </div>
          </div>
          <div className="lg:col-span-3">
            <ContactForm dict={dict} />
          </div>
        </div>
      </Section>
    </>
  );
}
