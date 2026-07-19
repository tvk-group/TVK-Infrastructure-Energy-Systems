#!/usr/bin/env node
/**
 * Generates PNG favicons and PWA icons from SVG sources.
 * Run: node scripts/generate-icons.mjs
 */
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";
import pngToIco from "png-to-ico";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");

const ICON_SVG = join(root, "public/icons/icon-512.svg");
const MARK_SVG = join(root, "public/logo/tvk-mark.svg");

const PNG_SIZES = [16, 32, 48, 72, 96, 128, 144, 152, 180, 192, 256, 384, 512];

async function svgToPng(svgPath, size, outputPath) {
  const svg = await readFile(svgPath);
  await sharp(svg, { density: Math.max(72, Math.ceil((size / 512) * 300)) })
    .resize(size, size)
    .png()
    .toFile(outputPath);
}

async function main() {
  const iconsDir = join(root, "public/icons");
  const appDir = join(root, "src/app");

  await mkdir(iconsDir, { recursive: true });

  const generatedPngs = [];

  for (const size of PNG_SIZES) {
    const out = join(iconsDir, `icon-${size}.png`);
    await svgToPng(ICON_SVG, size, out);
    generatedPngs.push({ size, path: out });
    console.log(`Generated ${out}`);
  }

  // Apple touch icon (180x180)
  await svgToPng(ICON_SVG, 180, join(appDir, "apple-icon.png"));
  console.log("Generated src/app/apple-icon.png");

  // Favicon ICO (16, 32, 48)
  const icoBuffers = await Promise.all(
    [16, 32, 48].map(async (size) => {
      const buf = await sharp(await readFile(ICON_SVG))
        .resize(size, size)
        .png()
        .toBuffer();
      return buf;
    })
  );
  const ico = await pngToIco(icoBuffers);
  await writeFile(join(appDir, "favicon.ico"), ico);
  await writeFile(join(root, "public/favicon.ico"), ico);
  console.log("Generated favicon.ico");

  // Maskable icon with safe zone padding
  const maskableSize = 512;
  const maskableSvg = await readFile(MARK_SVG);
  const maskableBuf = await sharp(maskableSvg)
    .resize(Math.round(maskableSize * 0.6), Math.round(maskableSize * 0.6))
    .extend({
      top: Math.round(maskableSize * 0.2),
      bottom: Math.round(maskableSize * 0.2),
      left: Math.round(maskableSize * 0.2),
      right: Math.round(maskableSize * 0.2),
      background: { r: 10, g: 15, b: 27, alpha: 1 },
    })
    .png()
    .toBuffer();
  await writeFile(join(iconsDir, "icon-maskable-512.png"), maskableBuf);
  console.log("Generated icon-maskable-512.png");

  console.log("Icon generation complete.");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
