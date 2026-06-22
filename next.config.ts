import type { NextConfig } from "next";

/**
 * Static export — produces /out for Vercel and static hosts.
 * GitHub Pages uses next.config.pages.ts via npm run build:pages.
 */
const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
