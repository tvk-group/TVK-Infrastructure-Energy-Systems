import { InfrastructureView } from "@/views/pages";
import { loadPage, localeStaticParams, pageTitle } from "@/lib/page-utils";
import type { Metadata } from "next";

export function generateStaticParams() {
  return localeStaticParams();
}

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params;
  const { dict } = await loadPage(locale);
  const meta = dict.infrastructure.meta;
  return {
    title: pageTitle(dict, meta.title),
    description: meta.description,
  };
}

export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <InfrastructureView dict={dict} locale={validLocale} />;
}
