import type { Metadata } from "next";
import { AppShell } from "@/components/app/AppShell";
import { loadPage, localeStaticParams, pageTitle } from "@/lib/page-utils";
import type { Locale } from "@/i18n/config";

export function generateStaticParams() {
  return localeStaticParams();
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const { dict } = await loadPage(locale);
  return {
    title: pageTitle(dict, dict.app.meta.title),
    description: dict.app.meta.description,
    manifest: "/manifest.webmanifest",
    appleWebApp: {
      capable: true,
      statusBarStyle: "black-translucent",
      title: dict.app.brand,
    },
    other: {
      "mobile-web-app-capable": "yes",
    },
  };
}

export default async function AppLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const { dict, locale: validLocale } = await loadPage(locale);

  return (
    <AppShell locale={validLocale as Locale} dict={dict}>
      {children}
    </AppShell>
  );
}
