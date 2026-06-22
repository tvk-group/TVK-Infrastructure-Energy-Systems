export const navItems = [
  { label: "Home", href: "/" },
  { label: "About", href: "/about" },
  { label: "Energy Systems", href: "/energy-systems" },
  { label: "Infrastructure", href: "/infrastructure" },
  { label: "Technology", href: "/technology" },
  { label: "Projects", href: "/projects" },
  { label: "Strategic Partnerships", href: "/strategic-partnerships" },
  { label: "Insights", href: "/insights" },
  { label: "Contact", href: "/contact" },
] as const;

export const coreAreas = [
  {
    title: "Energy Systems",
    description:
      "Renewable integration, industrial energy solutions, and intelligent energy management frameworks.",
    href: "/energy-systems",
    icon: "energy",
  },
  {
    title: "Infrastructure Technologies",
    description:
      "Smart infrastructure, digital systems, and critical infrastructure technology development.",
    href: "/infrastructure",
    icon: "infrastructure",
  },
  {
    title: "Energy Intelligence",
    description:
      "Monitoring, analytics, and optimization capabilities for complex energy environments.",
    href: "/energy-systems",
    icon: "intelligence",
  },
  {
    title: "Industrial Innovation",
    description:
      "Advanced industrial systems, automation, and next-generation operational technologies.",
    href: "/technology",
    icon: "industrial",
  },
  {
    title: "AI Infrastructure",
    description:
      "Industrial AI, infrastructure analytics, and intelligent automation research.",
    href: "/technology",
    icon: "ai",
  },
  {
    title: "Strategic Investments",
    description:
      "Long-term strategic technology and industrial capability investments within the TVK ecosystem.",
    href: "/strategic-partnerships",
    icon: "investment",
  },
] as const;

export const developmentStages = [
  "Research",
  "Development",
  "Project Formation",
  "Strategic Partnership Development",
  "Pilot Preparation",
] as const;
