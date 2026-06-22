import type { Metadata } from "next";
import { PageHero, Section, FeatureCard, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Energy Systems",
  description:
    "Renewable energy, energy intelligence, monitoring, optimization, and industrial energy solutions.",
};

export default function EnergySystemsPage() {
  return (
    <>
      <PageHero
        eyebrow="Capabilities"
        title="Energy Systems"
        subtitle="Developing intelligent energy frameworks for industrial environments — from renewable integration to advanced monitoring and optimization."
      />

      <Section
        title="Energy Capability Areas"
        subtitle="Our energy systems work spans the full spectrum of modern energy management, with a focus on industrial applications and intelligent operations."
      >
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <FeatureCard
            title="Renewable Energy"
            description="Research and development of renewable energy integration strategies for industrial and infrastructure applications."
            items={[
              "Renewable integration frameworks",
              "Hybrid energy system design",
              "Industrial renewable applications",
              "Grid-interactive energy solutions",
            ]}
          />
          <FeatureCard
            title="Energy Intelligence"
            description="Advanced analytics and intelligence capabilities for understanding and optimizing complex energy environments."
            items={[
              "Energy data analytics",
              "Predictive energy modeling",
              "Demand forecasting",
              "Intelligent energy decision support",
            ]}
          />
          <FeatureCard
            title="Energy Monitoring"
            description="Comprehensive monitoring systems for real-time visibility across energy assets and consumption patterns."
            items={[
              "Real-time energy monitoring",
              "Asset performance tracking",
              "Consumption pattern analysis",
              "Multi-site energy visibility",
            ]}
          />
          <FeatureCard
            title="Energy Optimization"
            description="Systematic approaches to improving energy efficiency, reducing waste, and optimizing operational energy performance."
            items={[
              "Operational efficiency optimization",
              "Load management strategies",
              "Energy cost reduction frameworks",
              "Continuous improvement systems",
            ]}
          />
          <FeatureCard
            title="Industrial Energy Solutions"
            description="Tailored energy solutions designed for the specific demands of industrial operations and manufacturing environments."
            items={[
              "Industrial energy management",
              "Process energy optimization",
              "Facility-level energy systems",
              "Industrial decarbonization pathways",
            ]}
          />
          <FeatureCard
            title="Future EnergieMIND Integration"
            description="Planned integration with EnergieMIND energy intelligence capabilities as part of the broader TVK technology ecosystem."
            items={[
              "Energy intelligence platform research",
              "Cross-system integration planning",
              "Unified energy analytics vision",
              "Ecosystem technology alignment",
            ]}
          />
        </div>
      </Section>

      <Section
        title="Development Approach"
        subtitle="Our energy systems initiatives are currently in research and development, with pilot program preparation underway."
        className="bg-silver"
      >
        <div className="max-w-3xl">
          <p className="text-steel leading-relaxed mb-4">
            We are building the technical and partnership foundations required to
            deliver meaningful energy solutions. This includes engaging with energy
            technology providers, industrial operators, and research institutions
            to validate concepts and prepare for future pilot deployments.
          </p>
          <p className="text-steel leading-relaxed">
            All energy initiatives are developed with a long-term perspective —
            prioritizing reliability, scalability, and industrial-grade performance
            over short-term outcomes.
          </p>
        </div>
      </Section>

      <CTABanner
        title="Energy Systems Collaboration"
        description="Interested in energy intelligence, monitoring, or industrial energy solutions? We welcome partnership discussions."
        primaryLabel="Discuss Energy Opportunities"
        primaryHref="/contact"
      />
    </>
  );
}
