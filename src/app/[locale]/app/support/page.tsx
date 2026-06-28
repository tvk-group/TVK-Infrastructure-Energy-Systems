import { AppSupportView } from "@/views/app-pages";
import { loadPage, localeStaticParams } from "@/lib/page-utils";

export function generateStaticParams() {
  return localeStaticParams();
}

export default async function AppSupportPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);
  return <AppSupportView dict={dict} locale={validLocale} />;
}
