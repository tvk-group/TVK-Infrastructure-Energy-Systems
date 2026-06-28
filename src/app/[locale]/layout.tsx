import { notFound } from "next/navigation";
import { LocaleAttributes } from "@/components/LocaleAttributes";
import { PwaRegister } from "@/components/app/PwaRegister";
import { locales, isValidLocale, type Locale } from "@/i18n/config";

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;

  if (!isValidLocale(locale)) {
    notFound();
  }

  return (
    <>
      <LocaleAttributes locale={locale as Locale} />
      <PwaRegister />
      {children}
    </>
  );
}
