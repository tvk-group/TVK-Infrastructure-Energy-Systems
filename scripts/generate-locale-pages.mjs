import fs from 'fs';
import path from 'path';

const pages = [
  { slug: '', view: 'HomeView', dictKey: 'home' },
  { slug: 'about', view: 'AboutView', dictKey: 'about' },
  { slug: 'energy-systems', view: 'EnergySystemsView', dictKey: 'energySystems' },
  { slug: 'infrastructure', view: 'InfrastructureView', dictKey: 'infrastructure' },
  { slug: 'technology', view: 'TechnologyView', dictKey: 'technology' },
  { slug: 'projects', view: 'ProjectsView', dictKey: 'projects' },
  { slug: 'strategic-partnerships', view: 'PartnershipsView', dictKey: 'strategicPartnerships' },
  { slug: 'insights', view: 'InsightsView', dictKey: 'insights' },
  { slug: 'contact', view: 'ContactView', dictKey: 'contact' },
];

const appDir = '/workspace/src/app/[locale]';

for (const page of pages) {
  const dir = page.slug ? path.join(appDir, page.slug) : appDir;
  fs.mkdirSync(dir, { recursive: true });
  const content = `import { ${page.view} } from "@/views/pages";
import { loadPage, localeStaticParams, pageTitle } from "@/lib/page-utils";
import type { Metadata } from "next";

export function generateStaticParams() {
  return localeStaticParams();
}

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params;
  const { dict } = await loadPage(locale);
  const meta = dict.${page.dictKey}.meta;
  return {
    title: pageTitle(dict, meta.title),
    description: meta.description,
  };
}

export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <${page.view} dict={dict} locale={validLocale} />;
}
`;
  fs.writeFileSync(path.join(dir, 'page.tsx'), content);
}
console.log('Generated', pages.length, 'locale pages');
