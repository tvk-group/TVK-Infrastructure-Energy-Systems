"use client";

import { useState, FormEvent } from "react";

const interestAreas = [
  "Energy Systems",
  "Infrastructure Technologies",
  "Industrial Solutions",
  "Energy Intelligence",
  "AI Infrastructure",
  "Strategic Partnerships",
  "General Inquiry",
];

export function ContactForm() {
  const [submitted, setSubmitted] = useState(false);

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setSubmitted(true);
  }

  if (submitted) {
    return (
      <div className="border border-accent-green/30 bg-accent-green/5 p-12 text-center">
        <div className="w-16 h-16 mx-auto mb-6 rounded-full bg-accent-green/10 flex items-center justify-center">
          <svg className="w-8 h-8 text-accent-green" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h3 className="font-display text-2xl font-semibold text-navy mb-3">
          Inquiry Received
        </h3>
        <p className="text-steel max-w-md mx-auto">
          Thank you for your interest in TVK Infrastructure & Energy Systems.
          Our team will review your inquiry and respond accordingly.
        </p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div>
          <label htmlFor="name" className="block text-sm font-medium text-navy mb-2">
            Name <span className="text-energy">*</span>
          </label>
          <input
            type="text"
            id="name"
            name="name"
            required
            className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
            placeholder="Your full name"
          />
        </div>
        <div>
          <label htmlFor="company" className="block text-sm font-medium text-navy mb-2">
            Company <span className="text-energy">*</span>
          </label>
          <input
            type="text"
            id="company"
            name="company"
            required
            className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
            placeholder="Organization name"
          />
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div>
          <label htmlFor="role" className="block text-sm font-medium text-navy mb-2">
            Role <span className="text-energy">*</span>
          </label>
          <input
            type="text"
            id="role"
            name="role"
            required
            className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
            placeholder="Your position"
          />
        </div>
        <div>
          <label htmlFor="country" className="block text-sm font-medium text-navy mb-2">
            Country <span className="text-energy">*</span>
          </label>
          <input
            type="text"
            id="country"
            name="country"
            required
            className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
            placeholder="Country of operation"
          />
        </div>
      </div>

      <div>
        <label htmlFor="email" className="block text-sm font-medium text-navy mb-2">
          Email <span className="text-energy">*</span>
        </label>
        <input
          type="email"
          id="email"
          name="email"
          required
          className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
          placeholder="professional@company.com"
        />
      </div>

      <div>
        <label htmlFor="interest" className="block text-sm font-medium text-navy mb-2">
          Area of Interest <span className="text-energy">*</span>
        </label>
        <select
          id="interest"
          name="interest"
          required
          className="w-full border border-silver-dark bg-white px-4 py-3 text-navy focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
          defaultValue=""
        >
          <option value="" disabled>
            Select an area
          </option>
          {interestAreas.map((area) => (
            <option key={area} value={area}>
              {area}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label htmlFor="message" className="block text-sm font-medium text-navy mb-2">
          Message <span className="text-energy">*</span>
        </label>
        <textarea
          id="message"
          name="message"
          required
          rows={6}
          className="w-full border border-silver-dark bg-white px-4 py-3 text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy resize-y"
          placeholder="Describe your inquiry, partnership interest, or project opportunity..."
        />
      </div>

      <button
        type="submit"
        className="w-full sm:w-auto inline-flex items-center justify-center rounded bg-energy px-10 py-4 text-sm font-semibold text-white transition-colors hover:bg-energy-light"
      >
        Discuss Infrastructure & Energy Opportunities
      </button>
    </form>
  );
}
