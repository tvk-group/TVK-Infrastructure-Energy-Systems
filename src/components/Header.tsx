import Link from "next/link";
import { navItems } from "@/lib/navigation";

export function Header() {
  return (
    <header className="sticky top-0 z-50 bg-navy border-b border-white/10">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-20 items-center justify-between gap-8">
          <Link href="/" className="flex shrink-0 flex-col group">
            <span className="font-display text-lg font-semibold tracking-tight text-white sm:text-xl">
              TVK Infrastructure
            </span>
            <span className="text-[10px] font-medium uppercase tracking-[0.2em] text-silver-dark sm:text-xs">
              & Energy Systems LTD
            </span>
          </Link>

          <nav
            className="hidden xl:flex items-center gap-1"
            aria-label="Main navigation"
          >
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="px-3 py-2 text-sm font-medium text-white/80 transition-colors hover:text-white hover:bg-white/5 rounded"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          <Link
            href="/contact"
            className="hidden sm:inline-flex items-center justify-center rounded bg-energy px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
          >
            Contact
          </Link>
        </div>

        <nav
          className="xl:hidden flex gap-1 overflow-x-auto pb-3 -mx-4 px-4 scrollbar-hide"
          aria-label="Mobile navigation"
        >
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="shrink-0 px-3 py-1.5 text-xs font-medium text-white/80 transition-colors hover:text-white hover:bg-white/5 rounded whitespace-nowrap"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
