import type { Metadata } from "next";
import { PageHero, Section, FeatureCard, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Technology",
  description:
    "Industrial AI, infrastructure analytics, monitoring systems, automation, and energy intelligence research.",
};

export default function TechnologyPage() {
  return (
    <>
      <PageHero
        eyebrow="Capabilities"
        title="Technology & Innovation"
        subtitle="Applying advanced technology to industrial and infrastructure challenges — from AI and analytics to automation and intelligent monitoring."
      />

      <Section
        title="Technology Focus Areas"
        subtitle="Our technology research supports the operational needs of energy systems and infrastructure — with an emphasis on industrial-grade reliability and long-term applicability."
      >
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <FeatureCard
            title="Industrial AI"
            description="Artificial intelligence applications designed for industrial environments — where accuracy, reliability, and operational safety are paramount."
            items={[
              "Industrial machine learning research",
              "AI-driven process optimization",
              "Predictive maintenance intelligence",
              "Industrial decision support systems",
            ]}
          />
          <FeatureCard
            title="Infrastructure Analytics"
            description="Advanced analytics platforms for understanding infrastructure performance, utilization, and operational efficiency."
            items={[
              "Infrastructure performance analytics",
              "Operational data intelligence",
              "Trend analysis and forecasting",
              "Cross-asset analytics frameworks",
            ]}
          />
          <FeatureCard
            title="Monitoring Systems"
            description="Comprehensive monitoring solutions for energy assets, infrastructure systems, and industrial operations."
            items={[
              "Multi-parameter monitoring systems",
              "Distributed sensor networks",
              "Alert and notification frameworks",
              "Historical data management",
            ]}
          />
          <FeatureCard
            title="Automation"
            description="Research into automation technologies that improve operational efficiency while maintaining human oversight and safety."
            items={[
              "Process automation research",
              "Control system integration",
              "Automated response frameworks",
              "Human-machine collaboration systems",
            ]}
          />
          <FeatureCard
            title="Energy Intelligence"
            description="Intelligent systems that transform energy data into actionable insights for operational and strategic decision-making."
            items={[
              "Energy analytics platforms",
              "Intelligent load management",
              "Energy pattern recognition",
              "Strategic energy planning tools",
            ]}
          />
          <FeatureCard
            title="Future Research Initiatives"
            description="Forward-looking research into emerging technologies with potential application in energy and infrastructure domains."
            items={[
              "Emerging technology assessment",
              "Applied research programs",
              "Academic and industry collaboration",
              "Technology readiness evaluation",
            ]}
          />
        </div>
      </Section>

      <Section
        title="Technology Philosophy"
        className="bg-silver"
      >
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-4">
            Technology in energy and infrastructure must meet the highest standards
            of reliability and operational fitness. We do not pursue technology for
            its own sake — every research initiative is evaluated against its
            potential to deliver measurable industrial value.
          </p>
          <p className="text-steel leading-relaxed">
            Our technology development is currently in the research and partnership
            formation stage, with pilot program concepts under development across
            multiple capability areas.
          </p>
        </div>
      </Section>

      <CTABanner
        title="Technology Collaboration"
        description="We welcome engagement from technology providers, research institutions, and industrial organizations."
        primaryLabel="Discuss Technology Opportunities"
        primaryHref="/contact"
      />
    </>
  );
}
