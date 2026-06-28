import { AppDocumentsView } from "@/views/app-pages";
import { loadPage, localeStaticParams } from "@/lib/page-utils";

export function generateStaticParams() {
  return localeStaticParams();
}

export default async function AppDocumentsPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <AppDocumentsView dict={dict} locale={validLocale} />;
}
