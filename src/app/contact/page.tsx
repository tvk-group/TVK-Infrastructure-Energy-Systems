import type { Metadata } from "next";
import { PageHero, Section } from "@/components/ui";
import { ContactForm } from "@/components/ContactForm";

export const metadata: Metadata = {
  title: "Contact",
  description:
    "Contact TVK Infrastructure & Energy Systems to discuss infrastructure and energy opportunities.",
};

export default function ContactPage() {
  return (
    <>
      <PageHero
        eyebrow="Contact"
        title="Discuss Infrastructure & Energy Opportunities"
        subtitle="We welcome inquiries from organizations interested in energy systems, infrastructure technologies, industrial solutions, and strategic partnerships."
      />

      <Section title="Get in Touch">
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-12">
          <div className="lg:col-span-2">
            <p className="text-steel leading-relaxed mb-8">
              Whether you represent an energy company, infrastructure operator,
              industrial group, technology provider, or engineering firm — we
              invite you to share your interest and begin a conversation.
            </p>

            <div className="space-y-6">
              {[
                {
                  title: "Partnership Inquiries",
                  description:
                    "Organizations seeking strategic collaboration, pilot opportunities, or long-term partnership development.",
                },
                {
                  title: "Technology Discussions",
                  description:
                    "Technology providers and research institutions interested in energy intelligence, infrastructure analytics, or industrial AI.",
                },
                {
                  title: "General Inquiries",
                  description:
                    "Questions about TVK Infrastructure & Energy Systems, our capabilities, or the broader TVK ecosystem.",
                },
              ].map((item) => (
                <div key={item.title} className="border-l-4 border-energy pl-5">
                  <h3 className="font-display text-sm font-semibold text-navy mb-1">
                    {item.title}
                  </h3>
                  <p className="text-sm text-steel">{item.description}</p>
                </div>
              ))}
            </div>

            <div className="mt-10 p-6 bg-silver border border-silver-dark/30">
              <p className="text-xs font-semibold uppercase tracking-wider text-steel mb-2">
                TVK Infrastructure & Energy Systems LTD
              </p>
              <p className="text-sm text-steel">
                Part of the TVK Ecosystem
              </p>
            </div>
          </div>

          <div className="lg:col-span-3">
            <ContactForm />
          </div>
        </div>
      </Section>
    </>
  );
}
