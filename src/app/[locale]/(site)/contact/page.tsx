import { ContactView } from "@/views/pages";
import { loadPage, localeStaticParams, buildMetadataForPage } from "@/lib/page-utils";

export function generateStaticParams() {
  return localeStaticParams();
}

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  return buildMetadataForPage(locale, "contact");
}

export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <ContactView dict={dict} locale={validLocale} />;
}
