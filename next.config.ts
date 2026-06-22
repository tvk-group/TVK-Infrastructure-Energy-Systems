import type { NextConfig } from "next";

const isStaticExport = process.env.STATIC_EXPORT === "true";
const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

const nextConfig: NextConfig = {
  ...(isStaticExport ? { output: "export" as const } : {}),
  ...(basePath
    ? { basePath, assetPrefix: basePath }
    : {}),
  ...(isStaticExport ? { trailingSlash: true } : {}),
  images: {
    unoptimized: isStaticExport,
  },
};

export default nextConfig;
