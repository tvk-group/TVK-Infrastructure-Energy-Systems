import Link from "next/link";
import { navItems } from "@/lib/navigation";

export function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-navy text-white mt-auto">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-4">
          <div className="lg:col-span-1">
            <div className="mb-4">
              <span className="font-display text-xl font-semibold tracking-tight">
                TVK Infrastructure
              </span>
              <span className="block text-xs font-medium uppercase tracking-[0.2em] text-silver-dark mt-1">
                & Energy Systems LTD
              </span>
            </div>
            <p className="text-sm text-white/60 leading-relaxed max-w-xs">
              Developing future-focused initiatives across energy, infrastructure,
              industrial systems and strategic technologies within the TVK ecosystem.
            </p>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              Capabilities
            </h3>
            <ul className="space-y-2">
              {navItems.slice(2, 6).map((item) => (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    className="text-sm text-white/60 hover:text-white transition-colors"
                  >
                    {item.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              Company
            </h3>
            <ul className="space-y-2">
              {navItems
                .filter((item) =>
                  ["About", "Projects", "Strategic Partnerships", "Insights"].includes(
                    item.label
                  )
                )
                .map((item) => (
                  <li key={item.href}>
                    <Link
                      href={item.href}
                      className="text-sm text-white/60 hover:text-white transition-colors"
                    >
                      {item.label}
                    </Link>
                  </li>
                ))}
            </ul>
          </div>

          <div>
            <h3 className="font-display text-sm font-semibold uppercase tracking-wider text-white/90 mb-4">
              Connect
            </h3>
            <p className="text-sm text-white/60 mb-4">
              Seeking strategic partnerships and collaboration opportunities in
              infrastructure and energy.
            </p>
            <Link
              href="/contact"
              className="inline-flex items-center text-sm font-semibold text-energy-light hover:text-white transition-colors"
            >
              Discuss Opportunities →
            </Link>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-white/10 flex flex-col sm:flex-row justify-between items-center gap-4">
          <p className="text-xs text-white/40">
            © {currentYear} TVK Infrastructure & Energy Systems LTD. All rights
            reserved.
          </p>
          <p className="text-xs text-white/40">
            Part of the TVK Ecosystem
          </p>
        </div>
      </div>
    </footer>
  );
}
