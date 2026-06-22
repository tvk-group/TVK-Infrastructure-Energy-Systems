import type { Metadata } from "next";
import Link from "next/link";
import { PageHero, Section, CTABanner } from "@/components/ui";

export const metadata: Metadata = {
  title: "Insights",
  description:
    "Perspectives on energy, infrastructure, industrial technology, AI infrastructure, and engineering from TVK Infrastructure & Energy Systems.",
};

const insightTopics = [
  {
    topic: "Energy",
    title: "The Evolution of Industrial Energy Management",
    excerpt:
      "How intelligent energy systems are transforming the way industrial operations monitor, optimize, and strategize around energy consumption.",
    date: "Development Perspective",
  },
  {
    topic: "Infrastructure",
    title: "Smart Infrastructure: Beyond Connectivity",
    excerpt:
      "True smart infrastructure goes beyond sensors and networks — it requires integrated analytics, adaptive management, and long-term system thinking.",
    date: "Research Note",
  },
  {
    topic: "Industrial Technology",
    title: "Industrial Innovation in a Transforming Economy",
    excerpt:
      "The industrial sector faces unprecedented demands for efficiency, sustainability, and technological modernization. Strategic approaches matter.",
    date: "Industry Perspective",
  },
  {
    topic: "AI Infrastructure",
    title: "Industrial AI: Requirements for Real-World Deployment",
    excerpt:
      "Artificial intelligence in industrial environments demands a fundamentally different approach than consumer or enterprise software applications.",
    date: "Technology Brief",
  },
  {
    topic: "Digital Transformation",
    title: "Digital Infrastructure as Industrial Foundation",
    excerpt:
      "Digital infrastructure platforms are becoming the operational backbone of modern energy systems and industrial facilities worldwide.",
    date: "Development Perspective",
  },
  {
    topic: "Sustainability",
    title: "Sustainable Operations in Energy & Infrastructure",
    excerpt:
      "Long-term sustainability in energy and infrastructure requires integrated approaches that balance environmental responsibility with operational performance.",
    date: "Research Note",
  },
  {
    topic: "Engineering",
    title: "Engineering Excellence in Infrastructure Development",
    excerpt:
      "The infrastructure projects that endure are built on engineering rigor, thorough planning, and commitment to operational reliability.",
    date: "Engineering Perspective",
  },
  {
    topic: "Energy Intelligence",
    title: "From Energy Data to Strategic Intelligence",
    excerpt:
      "The transition from raw energy data to actionable intelligence represents one of the most significant opportunities in modern energy management.",
    date: "Technology Brief",
  },
];

const topicFilters = [
  "All",
  "Energy",
  "Infrastructure",
  "Industrial Technology",
  "AI Infrastructure",
  "Digital Transformation",
  "Sustainability",
  "Engineering",
];

export default function InsightsPage() {
  return (
    <>
      <PageHero
        eyebrow="Insights"
        title="Industry Perspectives"
        subtitle="Thought leadership and research perspectives on energy, infrastructure, industrial technology, and the future of industrial systems."
      />

      <Section
        title="Topics We Cover"
        subtitle="Our insights reflect the core areas of TVK Infrastructure & Energy Systems — informed by research, industry analysis, and strategic development work."
      >
        <div className="flex flex-wrap gap-2 mb-12">
          {topicFilters.map((topic) => (
            <span
              key={topic}
              className={`px-4 py-2 text-sm font-medium border ${
                topic === "All"
                  ? "bg-navy text-white border-navy"
                  : "bg-white text-steel border-silver-dark hover:border-energy hover:text-energy transition-colors"
              }`}
            >
              {topic}
            </span>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {insightTopics.map((insight) => (
            <article
              key={insight.title}
              className="group border border-silver bg-white p-8 transition-shadow hover:shadow-lg"
            >
              <div className="flex items-center gap-3 mb-4">
                <span className="text-xs font-semibold uppercase tracking-wider text-energy">
                  {insight.topic}
                </span>
                <span className="text-xs text-steel/60">·</span>
                <span className="text-xs text-steel/60">{insight.date}</span>
              </div>
              <h3 className="font-display text-xl font-semibold text-navy mb-3 group-hover:text-energy transition-colors">
                {insight.title}
              </h3>
              <p className="text-steel text-sm leading-relaxed">
                {insight.excerpt}
              </p>
            </article>
          ))}
        </div>

        <p className="mt-12 text-sm text-steel/70 text-center max-w-2xl mx-auto">
          Insights represent development-stage perspectives and research notes.
          Full publications will be released as our research programs advance.
        </p>
      </Section>

      <Section
        title="Stay Informed"
        className="bg-silver"
      >
        <div className="max-w-2xl mx-auto text-center">
          <p className="text-steel leading-relaxed mb-6">
            Interested in our perspectives on energy, infrastructure, and industrial
            technology? Connect with us to discuss research areas and industry developments.
          </p>
          <Link
            href="/contact"
            className="inline-flex items-center justify-center rounded bg-energy px-8 py-3.5 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
          >
            Get in Touch
          </Link>
        </div>
      </Section>

      <CTABanner
        title="Explore Our Capabilities"
        description="Learn more about our work in energy systems, infrastructure technologies, and industrial innovation."
        primaryLabel="Explore Capabilities"
        primaryHref="/energy-systems"
        secondaryLabel="About Us"
        secondaryHref="/about"
      />
    </>
  );
}
