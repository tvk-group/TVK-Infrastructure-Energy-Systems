#!/usr/bin/env node
/**
 * Installs uploaded brand assets into site paths (byte-for-byte copy, no modification).
 * Reads filenames from public/brand/manifest.json — set each value to your uploaded filename.
 */
import { copyFile, mkdir, readFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
const brandDir = join(root, "public/brand");
const manifestPath = join(brandDir, "manifest.json");

const INSTALL_MAP = {
  favicon: [join(root, "public/favicon.ico")],
  appleTouchIcon: [join(root, "src/app/apple-icon.png")],
  icon192: [
    join(root, "public/icons/icon-192.png"),
    join(root, "src/app/icon.png"),
  ],
  icon512: [join(root, "public/icons/icon-512.png")],
  ogImage: [join(root, "public/og-image.png")],
};

async function copyIfPresent(key, filename) {
  if (!filename) return;
  const src = join(brandDir, filename);
  const targets = INSTALL_MAP[key];
  if (!targets) return;
  try {
    await readFile(src);
  } catch {
    console.warn(`Skipping ${key}: ${filename} not found in public/brand/`);
    return;
  }
  for (const dest of targets) {
    await mkdir(dirname(dest), { recursive: true });
    await copyFile(src, dest);
    console.log(`Installed ${filename} → ${dest.replace(root, "")}`);
  }
}

async function main() {
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  for (const [key, filename] of Object.entries(manifest)) {
    if (key.startsWith("_")) continue;
    await copyIfPresent(key, filename);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
