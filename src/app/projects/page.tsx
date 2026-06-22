import type { Metadata } from "next";
import { PageHero, Section, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Projects",
  description:
    "Energy, infrastructure, industrial, and research initiatives in development at TVK Infrastructure & Energy Systems.",
};

const projectCategories = [
  {
    category: "Energy Projects",
    status: "In Development",
    description:
      "Initiatives focused on renewable energy integration, energy intelligence platforms, and industrial energy management frameworks.",
    areas: [
      "Renewable energy integration research",
      "Energy monitoring system development",
      "Industrial energy optimization frameworks",
      "EnergieMIND integration planning",
    ],
  },
  {
    category: "Infrastructure Projects",
    status: "In Development",
    description:
      "Projects addressing smart infrastructure, digital platforms, and critical infrastructure technology requirements.",
    areas: [
      "Smart infrastructure system research",
      "Digital infrastructure platform concepts",
      "Critical infrastructure resilience studies",
      "Infrastructure analytics development",
    ],
  },
  {
    category: "Industrial Projects",
    status: "In Development",
    description:
      "Industrial solutions spanning automation, monitoring, and next-generation operational technology research.",
    areas: [
      "Industrial automation research",
      "Process monitoring system development",
      "Industrial AI application studies",
      "Operational technology integration",
    ],
  },
  {
    category: "Research Initiatives",
    status: "Active",
    description:
      "Ongoing research programs exploring emerging technologies and their application in energy and infrastructure contexts.",
    areas: [
      "Energy intelligence research",
      "Infrastructure technology assessment",
      "Industrial AI feasibility studies",
      "Sustainability and efficiency research",
    ],
  },
  {
    category: "Future Pilot Programs",
    status: "Preparation",
    description:
      "Pilot program concepts under development in partnership with potential collaborators across energy and infrastructure sectors.",
    areas: [
      "Pilot scope definition",
      "Partner identification and engagement",
      "Technical feasibility validation",
      "Deployment planning frameworks",
    ],
  },
];

export default function ProjectsPage() {
  return (
    <>
      <PageHero
        eyebrow="Projects"
        title="Initiatives in Development"
        subtitle="TVK Infrastructure & Energy Systems is actively forming projects across energy, infrastructure, and industrial domains. All initiatives are currently in research, development, or pilot preparation stages."
      />

      <Section
        title="Project Categories"
        subtitle="We organize our work into five interconnected categories, each representing a distinct area of capability development within the TVK ecosystem."
      >
        <div className="space-y-8">
          {projectCategories.map((project) => (
            <div
              key={project.category}
              className="border border-silver bg-white overflow-hidden"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-navy px-8 py-5">
                <h3 className="font-display text-xl font-semibold text-white">
                  {project.category}
                </h3>
                <span className="inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-energy-light">
                  <span className="h-2 w-2 rounded-full bg-accent-green-light animate-pulse" />
                  {project.status}
                </span>
              </div>
              <div className="p-8">
                <p className="text-steel leading-relaxed mb-6">
                  {project.description}
                </p>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {project.areas.map((area) => (
                    <div
                      key={area}
                      className="flex items-start gap-3 text-sm text-steel bg-silver/50 px-4 py-3"
                    >
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-energy" />
                      {area}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </Section>

      <Section
        title="Development Transparency"
        className="bg-silver"
      >
        <div className="max-w-3xl">
          <p className="text-lg text-steel leading-relaxed mb-4">
            TVK Infrastructure & Energy Systems is in an active development phase.
            We do not present completed or operational projects at this stage — all
            initiatives listed represent genuine work in progress across research,
            development, and partnership formation.
          </p>
          <p className="text-steel leading-relaxed">
            As projects advance through pilot preparation and operational deployment,
            this page will be updated to reflect meaningful progress and outcomes.
          </p>
        </div>
      </Section>

      <CTABanner
        title="Collaborate on Future Projects"
        description="We are seeking partners to co-develop pilot programs and long-term initiatives in energy and infrastructure."
        primaryLabel="Strategic Partnership Inquiry"
        primaryHref="/strategic-partnerships"
        secondaryLabel="Contact Us"
        secondaryHref="/contact"
      />
    </>
  );
}
