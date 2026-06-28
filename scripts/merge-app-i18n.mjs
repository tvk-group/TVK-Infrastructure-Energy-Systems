#!/usr/bin/env node
import fs from "fs";
import path from "path";

const locales = [
  "en", "de", "fr", "es", "it", "pt", "nl", "pl", "ru", "ar", "zh", "ja", "ko", "hi", "tr",
  "sv", "no", "da", "fi", "cs", "ro", "hu", "el", "id", "vi",
];

const messagesDir = path.join(process.cwd(), "messages");
const appI18nDir = path.join(process.cwd(), "scripts/app-i18n");

for (const locale of locales) {
  const appFile = path.join(appI18nDir, `${locale}.json`);
  const msgFile = path.join(messagesDir, `${locale}.json`);

  if (!fs.existsSync(appFile)) {
    console.error(`Missing app i18n: ${locale}`);
    process.exit(1);
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
