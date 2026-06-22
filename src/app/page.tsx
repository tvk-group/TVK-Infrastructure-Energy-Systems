"use client";

import { useEffect } from "react";
import Link from "next/link";

export default function RootPage() {
  useEffect(() => {
    window.location.replace("/en/");
  }, []);

  return (
    <div className="flex min-h-screen items-center justify-center bg-navy text-white">
      <p>
        Redirecting to{" "}
        <Link href="/en/" className="text-energy-light underline">
          TVK Infrastructure &amp; Energy Systems
        </Link>
        ...
      </p>
    </div>
  );
}
