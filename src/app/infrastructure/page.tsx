import type { Metadata } from "next";
import { PageHero, Section, FeatureCard, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Infrastructure",
  description:
    "Infrastructure technologies, smart infrastructure, digital systems, and critical infrastructure development.",
};

export default function InfrastructurePage() {
  return (
    <>
      <PageHero
        eyebrow="Capabilities"
        title="Infrastructure Technologies"
        subtitle="Advancing the technologies that underpin modern infrastructure — from smart systems and digital platforms to critical infrastructure resilience."
      />

      <Section
        title="Infrastructure Focus Areas"
        subtitle="We develop and research infrastructure technologies that enable smarter, more resilient, and more efficient operational environments."
      >
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <FeatureCard
            title="Infrastructure Technologies"
            description="Core technology research and development for next-generation infrastructure systems and platforms."
            items={[
              "Infrastructure system architecture",
              "Technology integration frameworks",
              "Modular infrastructure solutions",
              "Cross-sector infrastructure research",
            ]}
          />
          <FeatureCard
            title="Smart Infrastructure"
            description="Intelligent infrastructure systems that leverage connectivity, sensors, and analytics for enhanced operational performance."
            items={[
              "Connected infrastructure systems",
              "Sensor network integration",
              "Real-time infrastructure analytics",
              "Adaptive infrastructure management",
            ]}
          />
          <FeatureCard
            title="Digital Infrastructure"
            description="Digital platforms and systems that support infrastructure operations, management, and strategic decision-making."
            items={[
              "Digital twin research",
              "Infrastructure data platforms",
              "Cloud-edge infrastructure systems",
              "Digital operations management",
            ]}
          />
          <FeatureCard
            title="Critical Infrastructure"
            description="Research and development focused on the security, reliability, and resilience of critical infrastructure systems."
            items={[
              "Infrastructure resilience frameworks",
              "Operational continuity planning",
              "Critical system monitoring",
              "Infrastructure risk management",
            ]}
          />
          <FeatureCard
            title="Future Infrastructure Platforms"
            description="Long-term research into next-generation infrastructure platforms that will define industrial operations in coming decades."
            items={[
              "Platform architecture research",
              "Interoperability standards development",
              "Scalable infrastructure frameworks",
              "Future-ready system design",
            ]}
          />
        </div>
      </Section>

      <Section
        title="Strategic Infrastructure Vision"
        className="bg-silver"
      >
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          <div>
            <p className="text-lg text-steel leading-relaxed mb-4">
              Infrastructure is the backbone of industrial economies. TVK Infrastructure
              & Energy Systems approaches infrastructure technology with the rigor and
              long-term perspective required for systems that must perform reliably
              over decades.
            </p>
            <p className="text-steel leading-relaxed">
              Our current work focuses on identifying the technologies, partnerships,
              and project structures that will enable meaningful infrastructure
              contributions in the years ahead.
            </p>
          </div>
          <div className="border border-silver-dark/50 bg-white p-8">
            <h3 className="font-display text-lg font-semibold text-navy mb-4">
              Current Stage
            </h3>
            <ul className="space-y-3">
              {[
                "Technology research and assessment",
                "Partnership identification and engagement",
                "Project concept development",
                "Pilot program preparation",
              ].map((item) => (
                <li key={item} className="flex items-start gap-3 text-sm text-steel">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-energy" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </Section>

      <CTABanner
        title="Infrastructure Collaboration"
        description="We seek partnerships with infrastructure operators, technology providers, and engineering organizations."
        primaryLabel="Discuss Infrastructure Opportunities"
        primaryHref="/contact"
      />
    </>
  );
}
