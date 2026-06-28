"use client";

import { useState } from "react";
import type { Dictionary } from "@/i18n/get-dictionary";

interface AppApplyFormProps {
  dict: Dictionary;
}

export function AppApplyForm({ dict }: AppApplyFormProps) {
  const t = dict.app.apply;
  const f = dict.app.applyForm;
  const [submitted, setSubmitted] = useState(false);

  if (submitted) {
    return (
      <div className="rounded-lg border border-accent-green/30 bg-white p-8 text-center">
        <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-accent-green/10 text-accent-green">
          <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" />
          </svg>
        </div>
        <h2 className="font-display text-lg font-semibold text-navy">{f.success.title}</h2>
        <p className="mt-2 text-sm text-steel">{f.success.message}</p>
      </div>
    );
  }

  return (
    <form
      className="space-y-4"
      onSubmit={(e) => {
        e.preventDefault();
        setSubmitted(true);
      }}
    >
      <p className="text-sm text-steel">{t.intro}</p>
      {(
        [
          ["name", f.fields.name, f.placeholders.name, "text"],
          ["company", f.fields.company, f.placeholders.company, "text"],
          ["role", f.fields.role, f.placeholders.role, "text"],
          ["country", f.fields.country, f.placeholders.country, "text"],
          ["email", f.fields.email, f.placeholders.email, "email"],
        ] as const
      ).map(([id, label, placeholder, type]) => (
        <div key={id}>
          <label htmlFor={id} className="block text-xs font-semibold uppercase tracking-wider text-navy mb-1.5">
            {label} {f.fields.required}
          </label>
          <input
            id={id}
            name={id}
            type={type}
            required
            placeholder={placeholder}
            className="w-full rounded border border-silver bg-white px-3 py-2.5 text-sm text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
          />
        </div>
      ))}
      <div>
        <label htmlFor="interest" className="block text-xs font-semibold uppercase tracking-wider text-navy mb-1.5">
          {f.fields.interest} {f.fields.required}
        </label>
        <select
          id="interest"
          name="interest"
          required
          className="w-full rounded border border-silver bg-white px-3 py-2.5 text-sm text-navy focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
        >
          <option value="">{f.placeholders.interest}</option>
          {f.interestAreas.map((area) => (
            <option key={area} value={area}>
              {area}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label htmlFor="allocation" className="block text-xs font-semibold uppercase tracking-wider text-navy mb-1.5">
          {f.fields.allocation} {f.fields.required}
        </label>
        <input
          id="allocation"
          name="allocation"
          type="text"
          required
          placeholder={f.placeholders.allocation}
          className="w-full rounded border border-silver bg-white px-3 py-2.5 text-sm text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy"
        />
      </div>
      <div>
        <label htmlFor="message" className="block text-xs font-semibold uppercase tracking-wider text-navy mb-1.5">
          {f.fields.message} {f.fields.required}
        </label>
        <textarea
          id="message"
          name="message"
          required
          rows={4}
          placeholder={f.placeholders.message}
          className="w-full rounded border border-silver bg-white px-3 py-2.5 text-sm text-navy placeholder:text-steel/50 focus:border-energy focus:outline-none focus:ring-1 focus:ring-energy resize-none"
        />
      </div>
      <p className="text-xs text-steel/80">{t.disclaimer}</p>
      <button
        type="submit"
        className="w-full rounded bg-energy px-4 py-3 text-sm font-semibold text-white hover:bg-energy-light transition-colors"
      >
        {f.submit}
      </button>
    </form>
  );
}
