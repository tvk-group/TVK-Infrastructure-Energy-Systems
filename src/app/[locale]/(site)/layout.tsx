import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import type { Locale } from "@/i18n/config";
import { getDictionary } from "@/i18n/get-dictionary";

export default async function SiteLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const dict = await getDictionary(locale as Locale);

  return (
    <>
      <Header locale={locale as Locale} dict={dict} />
      <main className="flex-grow">{children}</main>
      <Footer locale={locale as Locale} dict={dict} />
    </>
  );
}
