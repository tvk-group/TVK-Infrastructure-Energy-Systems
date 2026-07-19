#!/usr/bin/env node
/**
 * Import official logo PNG and generate all web assets.
 *
 * Usage:
 *   node scripts/import-official-logo.mjs path/to/official-logo.png
 *
 * Expects a horizontal logo image (icon + wordmark). Generates:
 *   - public/logo/official/logo-full.png
 *   - public/logo/official/logo-mark.png (cropped icon area)
 *   - All favicon/PWA sizes via generate-icons.mjs
 */
import { copyFile, mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
const officialDir = join(root, "public/logo/official");

const inputPath = process.argv[2];
if (!inputPath) {
  console.error("Usage: node scripts/import-official-logo.mjs <path-to-logo.png>");
  process.exit(1);
}

async function main() {
  await mkdir(officialDir, { recursive: true });
  const input = await readFile(inputPath);
  const meta = await sharp(input).metadata();

  // Save full logo at multiple widths for responsive use
  const widths = [320, 640, 1280];
  for (const w of widths) {
    const out = join(officialDir, `logo-full-${w}.png`);
    await sharp(input).resize(w, null, { fit: "inside" }).png().toFile(out);
    console.log(`Generated ${out}`);
  }

  await copyFile(
    join(officialDir, `logo-full-${widths[1]}.png`),
    join(officialDir, "logo-full.png")
  );

  // Extract icon mark (left ~18% of image) for favicon source
  const markWidth = Math.round((meta.width ?? 640) * 0.18);
  const markHeight = meta.height ?? 200;
  const markOut = join(officialDir, "logo-mark.png");
  await sharp(input)
    .extract({ left: 0, top: 0, width: markWidth, height: markHeight })
    .resize(512, 512, { fit: "contain", background: "#0d1117" })
    .png()
    .toFile(markOut);
  console.log(`Generated ${markOut}`);

  // Copy mark to icons source
  await copyFile(markOut, join(root, "public/icons/icon-source.png"));
  console.log("Official logo imported. Run: node scripts/generate-icons.mjs");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
