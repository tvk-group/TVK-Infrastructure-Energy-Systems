import { AppApplyView } from "@/views/app-pages";
import { loadPage, localeStaticParams } from "@/lib/page-utils";

export function generateStaticParams() {
  return localeStaticParams();
}

export default async function AppApplyPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <AppApplyView dict={dict} locale={validLocale} />;
}
