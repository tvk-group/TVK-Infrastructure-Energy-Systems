#!/usr/bin/env node
import fs from "fs";
import path from "path";

const locales = [
  "en", "tr", "de", "fr", "es", "it", "pt", "nl", "ar", "ru", "zh-cn", "zh-tw", "ja", "ko", "hi", "ur",
  "pl", "ro", "el", "sv", "no", "da", "fi", "he", "id",
];

const messagesDir = path.join(process.cwd(), "messages");
const appI18nDir = path.join(process.cwd(), "scripts/app-i18n");

for (const locale of locales) {
  const appFile = path.join(appI18nDir, `${locale}.json`);
  const msgFile = path.join(messagesDir, `${locale}.json`);

  if (!fs.existsSync(msgFile)) {
    console.error(`Missing messages file: ${locale}`);
    process.exit(1);
  }

  if (!fs.existsSync(appFile)) {
    console.warn(`Skipping merge (no app i18n yet): ${locale}`);
    continue;
  }

  const appData = JSON.parse(fs.readFileSync(appFile, "utf8"));
  const messages = JSON.parse(fs.readFileSync(msgFile, "utf8"));

  if (appData.header) {
    messages.header = { ...messages.header, ...appData.header };
  }
  if (appData.footer) {
    messages.footer = { ...messages.footer, ...appData.footer };
  }
  messages.app = appData.app;

  fs.writeFileSync(msgFile, JSON.stringify(messages, null, 2) + "\n");
  console.log(`Merged app i18n → messages/${locale}.json`);
}
