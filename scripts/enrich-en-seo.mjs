#!/usr/bin/env node
import fs from "fs";
import path from "path";

const enPath = path.join(process.cwd(), "messages/en.json");
const en = JSON.parse(fs.readFileSync(enPath, "utf8"));

en.seo = {
  siteName: "TVK Infrastructure & Energy Systems",
  websiteDescription:
    "Enterprise infrastructure, energy systems, industrial technology and strategic investment initiatives within the TVK ecosystem.",
  ogImageAlt: "TVK Infrastructure & Energy Systems — Powering Infrastructure. Enabling the Future.",
  defaultKeywords:
    "infrastructure, energy systems, industrial technology, smart infrastructure, energy intelligence, TVK, strategic partnerships",
  breadcrumbAria: "Breadcrumb navigation",
  internalLinksTitle: "Explore Infrastructure & Energy Capabilities",
  legalDisclaimer:
    "TVK Infrastructure & Energy Systems LTD is in a research, development and partnership-building stage. Information on this website describes capability areas and development initiatives — not operational project commitments. Part of the TVK Ecosystem.",
  organization: {
    name: "TVK Infrastructure & Energy Systems",
    legalName: "TVK Infrastructure & Energy Systems LTD",
    description:
      "Infrastructure, energy, industrial systems and strategic technology investment company within the TVK ecosystem.",
    sameAs: ["https://github.com/tvk-group/TVK-Infrastructure-Energy-Systems"],
    areaServed: "Worldwide",
    knowsAbout: [
      "Energy Systems",
      "Infrastructure Technologies",
      "Industrial AI",
      "Energy Intelligence",
      "Strategic Partnerships",
    ],
  },
  faq: [
    {
      question: "What does TVK Infrastructure & Energy Systems do?",
      answer:
        "TVK Infrastructure & Energy Systems develops initiatives across energy systems, infrastructure technologies, industrial solutions, energy intelligence, AI infrastructure and strategic investments within the TVK ecosystem.",
    },
    {
      question: "What stage is the company currently in?",
      answer:
        "The company is in research, development, project formation, strategic partnership development and pilot preparation stages.",
    },
    {
      question: "Does TVK Infrastructure & Energy Systems seek partnerships?",
      answer:
        "Yes. We actively engage energy companies, infrastructure operators, industrial groups, technology providers and engineering firms for collaboration and pilot opportunities.",
    },
    {
      question: "Is TVK Infrastructure & Energy Systems part of a larger ecosystem?",
      answer:
        "Yes. TVK Infrastructure & Energy Systems is part of the broader TVK ecosystem, integrating technology, industrial and strategic investment perspectives.",
    },
  ],
};

const pageSeo = {
  home: {
    title: "Infrastructure & Energy Systems | TVK",
    description:
      "TVK Infrastructure & Energy Systems develops future-focused energy, infrastructure, industrial and strategic technology initiatives. Research, development and partnership-building stage.",
    keywords: "infrastructure company, energy systems, industrial technology, TVK Infrastructure, strategic energy partnerships",
    ogTitle: "Powering Infrastructure. Enabling the Future. | TVK",
    ogDescription: "Enterprise infrastructure and energy systems development across renewable integration, smart infrastructure, industrial AI and strategic partnerships.",
    twitterTitle: "TVK Infrastructure & Energy Systems",
    twitterDescription: "Infrastructure, energy and industrial technology initiatives — part of the TVK ecosystem.",
  },
  about: {
    title: "About TVK Infrastructure & Energy Systems",
    description: "Mission, vision and long-term industrial strategy of TVK Infrastructure & Energy Systems — engineering-focused infrastructure and energy development within the TVK ecosystem.",
    keywords: "about TVK, infrastructure strategy, energy company mission, industrial development",
    ogTitle: "About TVK Infrastructure & Energy Systems",
    ogDescription: "Engineering the future of infrastructure and energy with long-term industrial strategy.",
    twitterTitle: "About TVK Infrastructure & Energy Systems",
    twitterDescription: "Mission, vision and long-term infrastructure & energy strategy.",
  },
  energySystems: {
    title: "Energy Systems & Energy Intelligence",
    description: "Renewable energy integration, energy monitoring, optimization, industrial energy solutions and EnergieMIND research at TVK Infrastructure & Energy Systems.",
    keywords: "energy systems, renewable energy, energy intelligence, industrial energy, energy monitoring",
    ogTitle: "Energy Systems | TVK Infrastructure & Energy Systems",
    ogDescription: "Intelligent energy frameworks for industrial environments — monitoring, optimization and renewable integration.",
    twitterTitle: "Energy Systems | TVK",
    twitterDescription: "Renewable integration, energy intelligence and industrial energy solutions.",
  },
  infrastructure: {
    title: "Infrastructure Technologies & Smart Infrastructure",
    description: "Smart infrastructure, digital infrastructure, critical infrastructure resilience and future infrastructure platforms — TVK Infrastructure & Energy Systems.",
    keywords: "infrastructure technology, smart infrastructure, digital infrastructure, critical infrastructure",
    ogTitle: "Infrastructure Technologies | TVK",
    ogDescription: "Advancing technologies for smart, digital and resilient infrastructure systems.",
    twitterTitle: "Infrastructure Technologies | TVK",
    twitterDescription: "Smart, digital and critical infrastructure technology development.",
  },
  technology: {
    title: "Industrial Technology, AI & Automation",
    description: "Industrial AI, infrastructure analytics, monitoring systems, automation and energy intelligence research at TVK Infrastructure & Energy Systems.",
    keywords: "industrial AI, infrastructure analytics, automation, monitoring systems, industrial technology",
    ogTitle: "Technology & Innovation | TVK",
    ogDescription: "Industrial AI, analytics, automation and intelligent monitoring for infrastructure and energy.",
    twitterTitle: "Technology & Innovation | TVK",
    twitterDescription: "Industrial AI, analytics and automation for infrastructure and energy.",
  },
  projects: {
    title: "Projects & Research Initiatives in Development",
    description: "Energy, infrastructure, industrial and research initiatives in development at TVK Infrastructure & Energy Systems. Transparent development-stage project categories.",
    keywords: "energy projects, infrastructure projects, industrial projects, research initiatives, pilot programs",
    ogTitle: "Projects in Development | TVK",
    ogDescription: "Development-stage energy, infrastructure and industrial initiatives within the TVK ecosystem.",
    twitterTitle: "Projects | TVK Infrastructure & Energy Systems",
    twitterDescription: "Energy, infrastructure and industrial initiatives in development.",
  },
  strategicPartnerships: {
    title: "Strategic Partnerships & Collaboration",
    description: "TVK Infrastructure & Energy Systems seeks strategic partnerships with energy companies, infrastructure operators, industrial groups and technology providers.",
    keywords: "strategic partnerships, energy collaboration, infrastructure partnerships, industrial partnerships",
    ogTitle: "Strategic Partnerships | TVK",
    ogDescription: "Collaboration and pilot opportunities with energy, infrastructure and industrial organizations.",
    twitterTitle: "Strategic Partnerships | TVK",
    twitterDescription: "Seeking collaboration with energy, infrastructure and industrial partners.",
  },
  insights: {
    title: "Insights — Energy, Infrastructure & Industrial Technology",
    description: "Industry perspectives on energy, infrastructure, industrial technology, AI infrastructure, sustainability and engineering from TVK Infrastructure & Energy Systems.",
    keywords: "energy insights, infrastructure trends, industrial technology, engineering perspectives",
    ogTitle: "Industry Insights | TVK Infrastructure & Energy Systems",
    ogDescription: "Thought leadership on energy, infrastructure and industrial technology.",
    twitterTitle: "Insights | TVK Infrastructure & Energy Systems",
    twitterDescription: "Research perspectives on energy, infrastructure and industrial systems.",
  },
  contact: {
    title: "Contact — Infrastructure & Energy Opportunities",
    description: "Contact TVK Infrastructure & Energy Systems to discuss infrastructure, energy systems, industrial solutions and strategic partnership opportunities.",
    keywords: "contact TVK, infrastructure inquiry, energy partnership contact, industrial collaboration",
    ogTitle: "Contact TVK Infrastructure & Energy Systems",
    ogDescription: "Discuss infrastructure and energy opportunities with TVK Infrastructure & Energy Systems.",
    twitterTitle: "Contact | TVK Infrastructure & Energy Systems",
    twitterDescription: "Get in touch about infrastructure, energy and partnership opportunities.",
  },
};

for (const [key, seo] of Object.entries(pageSeo)) {
  if (en[key]?.meta) en[key].meta = { ...en[key].meta, ...seo };
}

if (en.insights?.topics?.items) {
  en.insights.topics.items = en.insights.topics.items.map((item, i) => ({
    ...item,
    slug: item.slug ?? `insight-${i + 1}`,
    datePublished: item.datePublished ?? "2026-01-15",
  }));
}

fs.writeFileSync(enPath, JSON.stringify(en, null, 2) + "\n");
console.log("Updated en.json with SEO metadata");
