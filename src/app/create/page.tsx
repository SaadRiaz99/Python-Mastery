"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { useRouter } from "next/navigation";
import { getSupabase } from "@/lib/supabase";
import { themes, getTheme } from "@/lib/themes";
import { generateSlug } from "@/lib/themes";
import type { EventType } from "@/types";

export default function CreatePage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [form, setForm] = useState({
    groom_name: "",
    bride_name: "",
    event_type: "barat" as EventType,
    date: "",
    time: "",
    venue: "",
    venue_address: "",
    theme: "barat" as EventType,
    message:
      "With great happiness, you are warmly invited to celebrate our special day. Your presence will make this occasion even more memorable.",
  });

  const selectedTheme = getTheme(form.theme);

  const updateForm = (field: string, value: string) => {
    setForm((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async () => {
    setError("");
    setLoading(true);

    try {
      const { data, error: insertError } = await getSupabase()
        .from("weddings")
        .insert({
          bride_name: form.bride_name,
          groom_name: form.groom_name,
          event_type: form.event_type,
          date: form.date,
          time: form.time,
          venue: form.venue,
          venue_address: form.venue_address,
          theme: form.theme,
          message: form.message,
          user_id: crypto.randomUUID(),
        })
        .select()
        .single();

      if (insertError) throw insertError;

      router.push(`/dashboard?wedding=${data.id}`);
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "Failed to create wedding";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-amber-50/30">
      <nav className="border-b border-gray-100 bg-white/80 backdrop-blur-sm">
        <div className="mx-auto flex max-w-4xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-full bg-gradient-to-br from-amber-500 to-rose-600" />
            <span className="font-[family-name:var(--font-playfair)] text-lg font-bold text-gray-900">
              WeddingInvite
            </span>
          </div>
          <div className="text-sm text-gray-400">Step {step} of 3</div>
        </div>
      </nav>

      <div className="mx-auto max-w-4xl px-6 py-8">
        <div className="mb-8">
          <div className="flex gap-2">
            {[1, 2, 3].map((s) => (
              <div
                key={s}
                className={`h-1.5 flex-1 rounded-full transition-colors ${
                  s <= step
                    ? "bg-gradient-to-r from-amber-500 to-rose-500"
                    : "bg-gray-200"
                }`}
              />
            ))}
          </div>
        </div>

        <AnimatePresence mode="wait">
          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-6"
            >
              <div>
                <h2 className="mb-2 text-2xl font-bold text-gray-900">
                  Wedding Details
                </h2>
                <p className="text-gray-500">
                  Enter the names of the couple and event details
                </p>
              </div>

              <div className="grid gap-6 sm:grid-cols-2">
                <div>
                  <label className="mb-2 block text-sm font-medium text-gray-700">
                    Groom&apos;s Name *
                  </label>
                  <input
                    type="text"
                    value={form.groom_name}
                    onChange={(e) => updateForm("groom_name", e.target.value)}
                    className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors placeholder:text-gray-300 focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                    placeholder="Muhammad Ali"
                  />
                </div>
                <div>
                  <label className="mb-2 block text-sm font-medium text-gray-700">
                    Bride&apos;s Name *
                  </label>
                  <input
                    type="text"
                    value={form.bride_name}
                    onChange={(e) => updateForm("bride_name", e.target.value)}
                    className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors placeholder:text-gray-300 focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                    placeholder="Fatima Ahmed"
                  />
                </div>
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium text-gray-700">
                  Event Type *
                </label>
                <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
                  {(["mehndi", "barat", "nikah", "walima"] as EventType[]).map(
                    (type) => (
                      <button
                        key={type}
                        onClick={() => {
                          updateForm("event_type", type);
                          updateForm("theme", type);
                        }}
                        className={`rounded-xl border-2 p-3 text-center font-medium capitalize transition-all ${
                          form.event_type === type
                            ? "border-amber-400 bg-amber-50 text-amber-700"
                            : "border-gray-200 text-gray-600 hover:border-gray-300"
                        }`}
                      >
                        {type}
                      </button>
                    )
                  )}
                </div>
              </div>

              <div className="grid gap-6 sm:grid-cols-2">
                <div>
                  <label className="mb-2 block text-sm font-medium text-gray-700">
                    Date *
                  </label>
                  <input
                    type="date"
                    value={form.date}
                    onChange={(e) => updateForm("date", e.target.value)}
                    className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                  />
                </div>
                <div>
                  <label className="mb-2 block text-sm font-medium text-gray-700">
                    Time *
                  </label>
                  <input
                    type="time"
                    value={form.time}
                    onChange={(e) => updateForm("time", e.target.value)}
                    className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                  />
                </div>
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium text-gray-700">
                  Venue Name *
                </label>
                <input
                  type="text"
                  value={form.venue}
                  onChange={(e) => updateForm("venue", e.target.value)}
                  className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors placeholder:text-gray-300 focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                  placeholder="Pearl Continental"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium text-gray-700">
                  Venue Address
                </label>
                <input
                  type="text"
                  value={form.venue_address}
                  onChange={(e) => updateForm("venue_address", e.target.value)}
                  className="w-full rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors placeholder:text-gray-300 focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                  placeholder="Karachi, Pakistan"
                />
              </div>

              <div>
                <label className="mb-2 block text-sm font-medium text-gray-700">
                  Personal Message
                </label>
                <textarea
                  value={form.message}
                  onChange={(e) => updateForm("message", e.target.value)}
                  rows={3}
                  className="w-full resize-none rounded-xl border border-gray-200 px-4 py-3 text-gray-900 transition-colors placeholder:text-gray-300 focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100"
                />
              </div>
            </motion.div>
          )}

          {step === 2 && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-6"
            >
              <div>
                <h2 className="mb-2 text-2xl font-bold text-gray-900">
                  Choose Theme
                </h2>
                <p className="text-gray-500">
                  Select a beautiful Pakistani wedding theme
                </p>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                {themes.map((theme) => (
                  <button
                    key={theme.id}
                    onClick={() => updateForm("theme", theme.id)}
                    className={`group overflow-hidden rounded-2xl border-2 transition-all ${
                      form.theme === theme.id
                        ? "border-amber-400 shadow-lg ring-2 ring-amber-100"
                        : "border-gray-200 hover:border-gray-300"
                    }`}
                  >
                    <div
                      className="h-32"
                      style={{ background: theme.colors.gradient }}
                    >
                      <div className="flex h-full items-center justify-center">
                        <span className="font-[family-name:var(--font-playfair)] text-3xl font-bold text-white drop-shadow-lg">
                          {theme.name}
                        </span>
                      </div>
                    </div>
                    <div className="p-4 text-left">
                      <h3 className="font-semibold text-gray-900">
                        {theme.name} Theme
                      </h3>
                      <p className="text-sm text-gray-500">
                        {theme.description}
                      </p>
                    </div>
                  </button>
                ))}
              </div>

              <div className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
                <h3 className="mb-4 font-semibold text-gray-900">
                  Preview
                </h3>
                <div
                  className="overflow-hidden rounded-xl p-6 text-center"
                  style={{
                    background: selectedTheme.colors.gradient,
                  }}
                >
                  <div className="mb-2 text-sm text-white/80">
                    {form.event_type.charAt(0).toUpperCase() +
                      form.event_type.slice(1)}{" "}
                    Invitation
                  </div>
                  <div className="font-[family-name:var(--font-playfair)] text-2xl font-bold text-white md:text-3xl">
                    {form.groom_name || "Groom"} &{" "}
                    {form.bride_name || "Bride"}
                  </div>
                </div>
              </div>
            </motion.div>
          )}

          {step === 3 && (
            <motion.div
              key="step3"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="space-y-6"
            >
              <div>
                <h2 className="mb-2 text-2xl font-bold text-gray-900">
                  Review & Create
                </h2>
                <p className="text-gray-500">
                  Review your wedding details before creating
                </p>
              </div>

              <div className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
                <div className="grid gap-4 sm:grid-cols-2">
                  <div>
                    <span className="text-sm text-gray-400">Groom</span>
                    <p className="font-medium text-gray-900">
                      {form.groom_name}
                    </p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-400">Bride</span>
                    <p className="font-medium text-gray-900">
                      {form.bride_name}
                    </p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-400">Event</span>
                    <p className="font-medium capitalize text-gray-900">
                      {form.event_type}
                    </p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-400">Theme</span>
                    <p className="font-medium capitalize text-gray-900">
                      {form.theme}
                    </p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-400">Date</span>
                    <p className="font-medium text-gray-900">{form.date}</p>
                  </div>
                  <div>
                    <span className="text-sm text-gray-400">Time</span>
                    <p className="font-medium text-gray-900">{form.time}</p>
                  </div>
                  <div className="sm:col-span-2">
                    <span className="text-sm text-gray-400">Venue</span>
                    <p className="font-medium text-gray-900">
                      {form.venue}
                      {form.venue_address && `, ${form.venue_address}`}
                    </p>
                  </div>
                </div>
              </div>

              <div
                className="overflow-hidden rounded-2xl p-8 text-center"
                style={{ background: selectedTheme.colors.gradient }}
              >
                <div className="mb-4 text-4xl">&#127800;</div>
                <div className="font-[family-name:var(--font-playfair)] text-3xl font-bold text-white drop-shadow-lg md:text-4xl">
                  {form.groom_name} & {form.bride_name}
                </div>
                <div className="mt-4 text-lg text-white/80">{form.message}</div>
              </div>

              {error && (
                <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-600">
                  {error}
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        <div className="mt-8 flex justify-between">
          <button
            onClick={() => step > 1 && setStep(step - 1)}
            className={`rounded-xl px-6 py-3 font-medium transition-colors ${
              step > 1
                ? "text-gray-600 hover:bg-gray-100"
                : "invisible"
            }`}
          >
            Back
          </button>

          {step < 3 ? (
            <button
              onClick={() => {
                if (step === 1) {
                  if (!form.groom_name || !form.bride_name || !form.date || !form.time || !form.venue) {
                    setError("Please fill in all required fields");
                    return;
                  }
                }
                setError("");
                setStep(step + 1);
              }}
              className="rounded-xl bg-gradient-to-r from-amber-600 to-rose-600 px-8 py-3 font-semibold text-white shadow-lg transition-all hover:shadow-xl"
            >
              Continue
            </button>
          ) : (
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="rounded-xl bg-gradient-to-r from-amber-600 to-rose-600 px-8 py-3 font-semibold text-white shadow-lg transition-all hover:shadow-xl disabled:opacity-50"
            >
              {loading ? "Creating..." : "Create Wedding"}
            </button>
          )}
        </div>

        {error && step === 1 && (
          <div className="mt-4 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-600">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
