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
const FAVICON_SVG = join(root, "public/icons/icon-favicon.svg");
const MARK_SVG = join(root, "public/logo/tvk-mark.svg");

const PNG_SIZES = [16, 32, 48, 72, 96, 128, 144, 152, 180, 192, 256, 384, 512];
const SMALL_SIZES = new Set([16, 32, 48]);

async function svgToPng(svgPath, size, outputPath) {
  const svg = await readFile(svgPath);
  const density = SMALL_SIZES.has(size) ? 512 : Math.min(384, Math.max(144, size * 2));
  await sharp(svg, { density })
    .resize(size, size, { kernel: sharp.kernel.lanczos3 })
    .png({ compressionLevel: 9, adaptiveFiltering: true })
    .toFile(outputPath);
}

async function renderSvg(svgPath, size) {
  const svg = await readFile(svgPath);
  const density = size <= 48 ? 512 : Math.min(384, Math.max(192, size * 2));
  return sharp(svg, { density })
    .resize(size, size, { kernel: sharp.kernel.lanczos3 })
    .png({ compressionLevel: 9 })
    .toBuffer();
}

async function main() {
  const iconsDir = join(root, "public/icons");
  const appDir = join(root, "src/app");

  await mkdir(iconsDir, { recursive: true });

  for (const size of PNG_SIZES) {
    const out = join(iconsDir, `icon-${size}.png`);
    const src = SMALL_SIZES.has(size) ? FAVICON_SVG : ICON_SVG;
    await svgToPng(src, size, out);
    console.log(`Generated ${out} (from ${SMALL_SIZES.has(size) ? "favicon" : "full"} source)`);
  }

  await svgToPng(ICON_SVG, 180, join(appDir, "apple-icon.png"));
  console.log("Generated src/app/apple-icon.png");

  const icoBuffers = await Promise.all(
    [16, 32, 48].map((size) => renderSvg(FAVICON_SVG, size))
  );
  const ico = await pngToIco(icoBuffers);
  await writeFile(join(appDir, "favicon.ico"), ico);
  await writeFile(join(root, "public/favicon.ico"), ico);
  console.log("Generated favicon.ico");

  const maskableSize = 512;
  const maskableBuf = await sharp(await readFile(MARK_SVG), { density: 288 })
    .resize(Math.round(maskableSize * 0.55), Math.round(maskableSize * 0.55), {
      kernel: sharp.kernel.lanczos3,
    })
    .extend({
      top: Math.round(maskableSize * 0.225),
      bottom: Math.round(maskableSize * 0.225),
      left: Math.round(maskableSize * 0.225),
      right: Math.round(maskableSize * 0.225),
      background: { r: 14, g: 20, b: 28, alpha: 1 },
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
