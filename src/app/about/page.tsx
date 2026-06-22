import type { Metadata } from "next";
import { PageHero, Section, InfoBlock, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "About",
  description:
    "Learn about TVK Infrastructure & Energy Systems — our mission, vision, and long-term industrial strategy.",
};

export default function AboutPage() {
  return (
    <>
      <PageHero
        eyebrow="About Us"
        title="Engineering the Future of Infrastructure & Energy"
        subtitle="TVK Infrastructure & Energy Systems LTD represents the infrastructure, energy, industrial systems and strategic technology investment activities of the TVK ecosystem."
      />

      <Section
        title="Our Mission"
        subtitle="To develop and support initiatives that strengthen energy systems, advance infrastructure technologies, and enable long-term industrial capability."
      >
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <InfoBlock
            label="Mission"
            title="Powering Sustainable Industrial Growth"
            description="We focus on the research, development, and strategic formation of energy and infrastructure initiatives that serve industrial economies. Our mission is grounded in engineering excellence, technological rigor, and long-term value creation."
          />
          <InfoBlock
            label="Vision"
            title="A Global Infrastructure & Energy Platform"
            description="We envision TVK Infrastructure & Energy Systems as a recognized contributor to the global energy and infrastructure landscape — supporting intelligent systems, sustainable operations, and strategic industrial partnerships across markets."
          />
        </div>
      </Section>

      <Section
        title="Long-Term Industrial Strategy"
        subtitle="Our approach is defined by patience, technical depth, and strategic alignment with industrial partners."
        className="bg-silver"
      >
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {[
            {
              title: "Technology & Infrastructure Focus",
              description:
                "We concentrate on areas where technology directly enables infrastructure performance — energy intelligence, monitoring systems, automation, and digital infrastructure platforms.",
            },
            {
              title: "International Perspective",
              description:
                "Our strategic outlook encompasses global energy markets, cross-border infrastructure development, and international partnership opportunities with industrial and governmental organizations.",
            },
            {
              title: "Ecosystem Integration",
              description:
                "As part of the TVK ecosystem, we leverage collective expertise across technology, investment, and industrial domains to pursue opportunities that require multidisciplinary capability.",
            },
            {
              title: "Research-Led Development",
              description:
                "Current activities are centered on research, development, and project formation — building the technical and organizational foundations for future operational initiatives.",
            },
            {
              title: "Partnership-First Approach",
              description:
                "We prioritize strategic partnerships with established energy companies, infrastructure operators, and engineering firms to accelerate capability development and pilot preparation.",
            },
            {
              title: "Sustainable Operations",
              description:
                "Environmental responsibility and operational efficiency are embedded in our approach to energy systems and infrastructure technology development.",
            },
          ].map((item) => (
            <div key={item.title} className="bg-white border border-silver-dark/50 p-8">
              <div className="w-12 h-1 bg-energy mb-6" />
              <h3 className="font-display text-lg font-semibold text-navy mb-3">
                {item.title}
              </h3>
              <p className="text-steel text-sm leading-relaxed">{item.description}</p>
            </div>
          ))}
        </div>
      </Section>

      <Section title="Current Development Stage">
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-6">
            TVK Infrastructure & Energy Systems is currently in an active development
            and partnership-building phase. We are conducting research, forming project
            concepts, and engaging with potential strategic partners across the energy
            and infrastructure sectors.
          </p>
          <p className="text-steel leading-relaxed">
            This stage reflects our commitment to building capability thoughtfully —
            ensuring that each initiative is technically sound, strategically aligned,
            and positioned for long-term industrial impact.
          </p>
        </div>
      </Section>

      <CTABanner
        title="Partner With Us"
        description="We welcome inquiries from organizations interested in energy systems, infrastructure technologies, and industrial collaboration."
        primaryLabel="Contact Us"
        primaryHref="/contact"
        secondaryLabel="Strategic Partnerships"
        secondaryHref="/strategic-partnerships"
      />
    </>
  );
}
