#!/usr/bin/env node
import fs from "fs";
import path from "path";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://tvk-infrastructure-energy-systems.vercel.app";
const locales = ["en","tr","de","fr","es","it","pt","nl","ar","ru","zh-cn","zh-tw","ja","ko","hi","ur","pl","ro","el","sv","no","da","fi","he","id"];
const hreflangMap = { en:"en",tr:"tr",de:"de",fr:"fr",es:"es",it:"it",pt:"pt",nl:"nl",ar:"ar",ru:"ru","zh-cn":"zh-Hans","zh-tw":"zh-Hant",ja:"ja",ko:"ko",hi:"hi",ur:"ur",pl:"pl",ro:"ro",el:"el",sv:"sv",no:"no",da:"da",fi:"fi",he:"he",id:"id" };
const pages = ["","about","energy-systems","infrastructure","technology","projects","strategic-partnerships","insights","contact"];
const publicDir = path.join(process.cwd(), "public");
const sitemapDir = path.join(publicDir, "sitemaps");
fs.mkdirSync(sitemapDir, { recursive: true });
const url = (locale, slug) => `${SITE_URL}/${locale}${slug ? `/${slug}` : ""}/`;
const sitemapFiles = [];
for (const locale of locales) {
  let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n`;
  for (const slug of pages) {
    xml += `  <url>\n    <loc>${url(locale, slug)}</loc>\n`;
    for (const l of locales) xml += `    <xhtml:link rel="alternate" hreflang="${hreflangMap[l]}" href="${url(l, slug)}"/>\n`;
    xml += `    <xhtml:link rel="alternate" hreflang="x-default" href="${url("en", slug)}"/>\n    <changefreq>weekly</changefreq>\n    <priority>${slug === "" ? "1.0" : "0.8"}</priority>\n  </url>\n`;
  }
  xml += "</urlset>\n";
  const filename = `sitemap-${locale}.xml`;
  fs.writeFileSync(path.join(sitemapDir, filename), xml);
  sitemapFiles.push(filename);
}
let index = `<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;
for (const f of sitemapFiles) index += `  <sitemap><loc>${SITE_URL}/sitemaps/${f}</loc></sitemap>\n`;
index += "</sitemapindex>\n";
fs.writeFileSync(path.join(publicDir, "sitemap-index.xml"), index);
fs.writeFileSync(path.join(publicDir, "sitemap.xml"), index);
fs.writeFileSync(path.join(publicDir, "robots.txt"), `User-agent: *\nAllow: /\n\nUser-agent: Googlebot\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\nUser-agent: Yandex\nAllow: /\n\nUser-agent: Baiduspider\nAllow: /\n\nSitemap: ${SITE_URL}/sitemap-index.xml\n`);
console.log(`Generated ${sitemapFiles.length} sitemaps`);
