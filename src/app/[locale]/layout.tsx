import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { LocaleAttributes } from "@/components/LocaleAttributes";
import { locales, isValidLocale, type Locale } from "@/i18n/config";
import { getDictionary } from "@/i18n/get-dictionary";

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

  const dict = await getDictionary(locale as Locale);

  return (
    <>
      <LocaleAttributes locale={locale as Locale} />
      <Header locale={locale as Locale} dict={dict} />
      <main className="flex-grow">{children}</main>
      <Footer locale={locale as Locale} dict={dict} />
    </>
  );
}
