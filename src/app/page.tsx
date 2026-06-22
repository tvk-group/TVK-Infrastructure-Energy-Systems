import { Hero, CoreAreas } from "@/components/HomeSections";
import { Section } from "@/components/ui";
import { CTABanner } from "@/components/ui";
import { developmentStages } from "@/lib/navigation";

export default function HomePage() {
  return (
    <>
      <Hero />

      <Section
        title="Core Areas of Focus"
        subtitle="TVK Infrastructure & Energy Systems operates across six interconnected capability areas, supporting long-term industrial and energy initiatives within the TVK ecosystem."
        className="bg-white"
      >
        <CoreAreas />
      </Section>

      <section className="bg-silver industrial-grid">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <div className="section-divider mb-6" />
              <h2 className="font-display text-3xl sm:text-4xl font-semibold text-navy">
                Building Industrial Capability for the Long Term
              </h2>
              <p className="mt-6 text-lg text-steel leading-relaxed">
                We are developing the foundations for energy systems, infrastructure
                technologies, and industrial solutions that address the demands of
                modern economies. Our work spans research, development, and strategic
                partnership formation.
              </p>
              <p className="mt-4 text-steel leading-relaxed">
                As part of the broader TVK ecosystem, we bring together engineering
                expertise, technology research, and strategic investment perspectives
                to support sustainable industrial growth.
              </p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {developmentStages.map((stage) => (
                <div
                  key={stage}
                  className="border border-silver-dark/50 bg-white p-6 flex items-center gap-4"
                >
                  <div className="w-2 h-2 rounded-full bg-accent-green shrink-0" />
                  <span className="text-sm font-medium text-navy">{stage}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="bg-white">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                stat: "Energy",
                label: "Systems & Intelligence",
                desc: "Renewable integration, monitoring, and optimization frameworks.",
              },
              {
                stat: "Infrastructure",
                label: "Technologies & Platforms",
                desc: "Smart, digital, and critical infrastructure development.",
              },
              {
                stat: "Industrial",
                label: "Solutions & Innovation",
                desc: "Automation, analytics, and next-generation industrial systems.",
              },
            ].map((item) => (
              <div key={item.stat} className="text-center p-8 border border-silver">
                <p className="font-display text-4xl font-semibold text-energy mb-2">
                  {item.stat}
                </p>
                <p className="text-sm font-semibold uppercase tracking-wider text-navy mb-3">
                  {item.label}
                </p>
                <p className="text-sm text-steel">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <CTABanner
        title="Explore Strategic Collaboration"
        description="We are actively engaging with energy companies, infrastructure operators, industrial groups, and technology providers to develop pilot programs and long-term partnerships."
        primaryLabel="Strategic Partnership Inquiry"
        primaryHref="/strategic-partnerships"
        secondaryLabel="Contact Us"
        secondaryHref="/contact"
      />
    </>
  );
}
