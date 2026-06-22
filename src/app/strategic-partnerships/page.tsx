import type { Metadata } from "next";
import { PageHero, Section, FeatureCard, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Strategic Partnerships",
  description:
    "Seeking collaboration with energy companies, infrastructure operators, industrial groups, and technology providers.",
};

const partnerTypes = [
  {
    title: "Energy Companies",
    description:
      "Utilities, renewable energy developers, and energy technology firms seeking collaboration on intelligent energy systems and optimization.",
  },
  {
    title: "Infrastructure Operators",
    description:
      "Organizations managing critical infrastructure, transportation networks, and urban systems interested in smart infrastructure technologies.",
  },
  {
    title: "Industrial Groups",
    description:
      "Manufacturing and industrial enterprises exploring energy efficiency, automation, and next-generation operational technologies.",
  },
  {
    title: "Government-Linked Organizations",
    description:
      "Public sector entities and government-affiliated organizations involved in infrastructure development and energy policy implementation.",
  },
  {
    title: "Technology Providers",
    description:
      "Technology companies with solutions applicable to energy systems, infrastructure analytics, monitoring, and industrial automation.",
  },
  {
    title: "Engineering Firms",
    description:
      "Engineering consultancies and EPC firms with expertise in energy systems, infrastructure design, and industrial project delivery.",
  },
  {
    title: "Investment Partners",
    description:
      "Strategic investors and industrial investment groups aligned with long-term infrastructure and energy technology development.",
  },
];

const collaborationAreas = [
  "Joint research and development programs",
  "Pilot project co-development",
  "Technology integration partnerships",
  "Market access and distribution collaboration",
  "Knowledge sharing and technical exchange",
  "Long-term strategic alliance formation",
];

export default function StrategicPartnershipsPage() {
  return (
    <>
      <PageHero
        eyebrow="Partnerships"
        title="Strategic Partnerships"
        subtitle="We are actively seeking collaboration, pilot opportunities, and strategic partnerships with organizations across the energy, infrastructure, and industrial sectors."
      />

      <Section
        title="Partnership Objectives"
        subtitle="Our partnership approach is focused on building long-term industrial relationships — not investment solicitation. We seek collaborators who share our commitment to infrastructure and energy excellence."
      >
        <div className="max-w-3xl mb-12">
          <p className="text-steel leading-relaxed">
            TVK Infrastructure & Energy Systems is in a partnership-building phase.
            We welcome engagement from organizations that can contribute technical
            expertise, market access, operational capability, or strategic alignment
            to our developing initiatives.
          </p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {collaborationAreas.map((area) => (
            <div
              key={area}
              className="flex items-start gap-4 border border-silver bg-white p-6"
            >
              <div className="w-8 h-8 shrink-0 rounded bg-energy/10 flex items-center justify-center">
                <svg className="w-4 h-4 text-energy" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span className="text-sm font-medium text-navy">{area}</span>
            </div>
          ))}
        </div>
      </Section>

      <Section
        title="Target Partner Organizations"
        className="bg-silver"
      >
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {partnerTypes.map((partner) => (
            <FeatureCard
              key={partner.title}
              title={partner.title}
              description={partner.description}
            />
          ))}
        </div>
      </Section>

      <Section title="How to Engage">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {[
            {
              step: "01",
              title: "Initial Inquiry",
              description:
                "Submit a partnership inquiry through our contact form, outlining your organization, area of interest, and collaboration objectives.",
            },
            {
              step: "02",
              title: "Assessment & Alignment",
              description:
                "Our team reviews the inquiry and assesses strategic alignment with our developing initiatives and capability areas.",
            },
            {
              step: "03",
              title: "Collaboration Discussion",
              description:
                "Aligned partners are invited to structured discussions to explore specific collaboration models, pilot opportunities, and long-term partnership frameworks.",
            },
          ].map((item) => (
            <div key={item.step} className="relative border border-silver bg-white p-8">
              <span className="font-display text-5xl font-bold text-silver-dark/50 absolute top-4 right-6">
                {item.step}
              </span>
              <h3 className="font-display text-lg font-semibold text-navy mb-3 relative">
                {item.title}
              </h3>
              <p className="text-sm text-steel leading-relaxed relative">
                {item.description}
              </p>
            </div>
          ))}
        </div>
      </Section>

      <CTABanner
        title="Begin a Partnership Discussion"
        description="We welcome inquiries from organizations interested in energy systems, infrastructure technologies, and industrial collaboration."
        primaryLabel="Strategic Partnership Inquiry"
        primaryHref="/contact"
      />
    </>
  );
}
