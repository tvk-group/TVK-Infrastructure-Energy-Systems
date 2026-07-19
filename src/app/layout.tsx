import type { Metadata } from "next";
import { IBM_Plex_Sans, Source_Sans_3 } from "next/font/google";
import { SITE_URL } from "@/i18n/config";
import { BRAND } from "@/lib/brand-assets";
import "./globals.css";

const ibmPlex = IBM_Plex_Sans({
  variable: "--font-ibm-plex",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const sourceSans = Source_Sans_3({
  variable: "--font-source-sans",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: "TVK Infrastructure & Energy Systems LTD",
  description:
    "TVK Infrastructure & Energy Systems develops future-focused initiatives across energy, infrastructure, industrial systems and strategic technologies.",
  robots: { index: true, follow: true },
  manifest: "/manifest.webmanifest",
  icons: BRAND.favicon
    ? {
        icon: [{ url: "/favicon.ico" }],
        apple: BRAND.appleTouchIcon
          ? [{ url: "/apple-icon.png", sizes: "180x180", type: "image/png" }]
          : undefined,
      }
    : undefined,
  appleWebApp: {
    capable: true,
    statusBarStyle: "black-translucent",
    title: "TVK",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html suppressHydrationWarning className={`${ibmPlex.variable} ${sourceSans.variable} h-full antialiased`}>
      <head>
        <link rel="manifest" href="/manifest.webmanifest" />
        <meta name="theme-color" content="#0057b8" />
      </head>
      <body className="min-h-full flex flex-col font-sans">{children}</body>
    </html>
  );
}
