import type { NextConfig } from "next";

/** Used only by the GitHub Pages CI workflow. */
const nextConfig: NextConfig = {
  output: "export",
  basePath: "/TVK-Infrastructure-Energy-Systems",
  assetPrefix: "/TVK-Infrastructure-Energy-Systems",
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
