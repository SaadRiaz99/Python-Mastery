"use client";

import { Suspense, useState, useEffect, useCallback } from "react";
import { useSearchParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import Papa from "papaparse";
import { getSupabase } from "@/lib/supabase";
import { getTheme, getWhatsAppUrl, getBaseDomain, generateSlug } from "@/lib/themes";
import type { Wedding, Guest } from "@/types";

function DashboardContent() {
  const searchParams = useSearchParams();
  const weddingId = searchParams.get("wedding");

  const [wedding, setWedding] = useState<Wedding | null>(null);
  const [guests, setGuests] = useState<Guest[]>([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const [csvError, setCsvError] = useState("");
  const [csvSuccess, setCsvSuccess] = useState("");
  const [copiedSlug, setCopiedSlug] = useState<string | null>(null);

  const loadWedding = useCallback(async () => {
    if (!weddingId) return;
    const { data } = await getSupabase()
      .from("weddings")
      .select("*")
      .eq("id", weddingId)
      .single();
    setWedding(data);
  }, [weddingId]);

  const loadGuests = useCallback(async () => {
    if (!weddingId) return;
    const { data } = await getSupabase()
      .from("guests")
      .select("*")
      .eq("wedding_id", weddingId)
      .order("created_at", { ascending: false });
    setGuests(data || []);
    setLoading(false);
  }, [weddingId]);

  useEffect(() => {
    loadWedding();
    loadGuests();
  }, [loadWedding, loadGuests]);

  const handleCsvUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setCsvError("");
    setCsvSuccess("");
    setUploading(true);

    Papa.parse(file, {
      header: true,
      skipEmptyLines: true,
      complete: async (results) => {
        const data = results.data as Record<string, string>[];

        if (data.length === 0) {
          setCsvError("CSV file is empty");
          setUploading(false);
          return;
        }

        const headers = Object.keys(data[0]).map((h) => h.trim().toLowerCase());
        if (!headers.includes("name") || !headers.includes("contact")) {
          setCsvError(
            "CSV must have 'name' and 'contact' columns. Found: " +
              headers.join(", ")
          );
          setUploading(false);
          return;
        }

        const existingContacts = new Set(guests.map((g) => g.contact));
        const newGuests: {
          wedding_id: string;
          name: string;
          contact: string;
          unique_slug: string;
        }[] = [];
        let duplicates = 0;

        for (const row of data) {
          const name = (row.name || "").trim();
          const contact = (row.contact || "").trim();

          if (!name || !contact) continue;
          if (existingContacts.has(contact)) {
            duplicates++;
            continue;
          }

          existingContacts.add(contact);
          newGuests.push({
            wedding_id: weddingId!,
            name,
            contact,
            unique_slug: generateSlug(),
          });
        }

        if (newGuests.length === 0) {
          setCsvError("All guests already exist or are duplicates");
          setUploading(false);
          return;
        }

        const { error } = await getSupabase().from("guests").insert(newGuests);

        if (error) {
          setCsvError("Failed to save guests: " + error.message);
        } else {
          setCsvSuccess(
            `${newGuests.length} guests imported successfully!${
              duplicates > 0 ? ` ${duplicates} duplicates skipped.` : ""
            }`
          );
          loadGuests();
        }

        setUploading(false);
      },
      error: () => {
        setCsvError("Failed to parse CSV file");
        setUploading(false);
      },
    });
  };

  const deleteGuest = async (id: string) => {
    await getSupabase().from("guests").delete().eq("id", id);
    loadGuests();
  };

  const copyLink = (slug: string) => {
    const domain = getBaseDomain();
    navigator.clipboard.writeText(`${domain}/invite/${slug}`);
    setCopiedSlug(slug);
    setTimeout(() => setCopiedSlug(null), 2000);
  };

  const filteredGuests = guests.filter(
    (g) =>
      g.name.toLowerCase().includes(search.toLowerCase()) ||
      g.contact.includes(search)
  );

  const theme = wedding ? getTheme(wedding.theme) : null;

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-amber-200 border-t-amber-600" />
      </div>
    );
  }

  if (!wedding) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4">
        <p className="text-gray-500">No wedding found</p>
        <a
          href="/create"
          className="rounded-xl bg-gradient-to-r from-amber-600 to-rose-600 px-6 py-3 font-semibold text-white"
        >
          Create Wedding
        </a>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="border-b border-gray-100 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-full bg-gradient-to-br from-amber-500 to-rose-600" />
            <span className="font-[family-name:var(--font-playfair)] text-lg font-bold text-gray-900">
              Dashboard
            </span>
          </div>
          <div className="flex items-center gap-4">
            <span className="hidden text-sm text-gray-500 sm:inline">
              {wedding.groom_name} & {wedding.bride_name}
            </span>
            <div
              className="h-3 w-3 rounded-full"
              style={{ background: theme?.colors.primary }}
            />
          </div>
        </div>
      </nav>

      <main className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
        <div className="mb-8 grid gap-4 sm:grid-cols-3">
          <div className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
            <div className="text-sm text-gray-400">Total Guests</div>
            <div className="mt-1 text-3xl font-bold text-gray-900">
              {guests.length}
            </div>
          </div>
          <div className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
            <div className="text-sm text-gray-400">Event</div>
            <div className="mt-1 text-2xl font-bold capitalize text-gray-900">
              {wedding.event_type}
            </div>
          </div>
          <div className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
            <div className="text-sm text-gray-400">Date</div>
            <div className="mt-1 text-2xl font-bold text-gray-900">
              {wedding.date}
            </div>
          </div>
        </div>

        <div className="mb-6 rounded-2xl border border-gray-100 bg-white p-6 shadow-sm">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h2 className="text-lg font-bold text-gray-900">
                Wedding Details
              </h2>
              <p className="text-sm text-gray-500">
                {wedding.groom_name} & {wedding.bride_name} &middot;{" "}
                {wedding.venue}
              </p>
            </div>
            <div
              className="h-12 w-32 rounded-xl"
              style={{ background: theme?.colors.gradient }}
            />
          </div>
        </div>

        <div className="mb-6 rounded-2xl border border-dashed border-amber-300 bg-amber-50/50 p-6">
          <h3 className="mb-2 font-semibold text-gray-900">
            Upload Guest List (CSV)
          </h3>
          <p className="mb-4 text-sm text-gray-500">
            CSV must have <code>name</code> and <code>contact</code> columns
          </p>
          <label className="inline-flex cursor-pointer items-center gap-2 rounded-xl bg-white px-6 py-3 font-medium text-gray-700 shadow-sm transition-all hover:shadow-md">
            <svg
              className="h-5 w-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>
            {uploading ? "Uploading..." : "Choose CSV File"}
            <input
              type="file"
              accept=".csv"
              onChange={handleCsvUpload}
              className="hidden"
              disabled={uploading}
            />
          </label>
          <AnimatePresence>
            {csvError && (
              <motion.p
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0 }}
                className="mt-3 text-sm text-red-600"
              >
                {csvError}
              </motion.p>
            )}
            {csvSuccess && (
              <motion.p
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0 }}
                className="mt-3 text-sm text-green-600"
              >
                {csvSuccess}
              </motion.p>
            )}
          </AnimatePresence>
        </div>

        <div className="rounded-2xl border border-gray-100 bg-white shadow-sm">
          <div className="border-b border-gray-100 p-6">
            <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
              <h3 className="text-lg font-bold text-gray-900">
                Guest List ({filteredGuests.length})
              </h3>
              <div className="relative">
                <svg
                  className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
                <input
                  type="text"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  placeholder="Search guests..."
                  className="w-full rounded-xl border border-gray-200 py-2.5 pl-10 pr-4 text-sm focus:border-amber-400 focus:outline-none focus:ring-2 focus:ring-amber-100 sm:w-72"
                />
              </div>
            </div>
          </div>

          {filteredGuests.length === 0 ? (
            <div className="p-12 text-center">
              <div className="mb-4 text-4xl">&#128100;</div>
              <p className="text-gray-400">
                {guests.length === 0
                  ? "No guests yet. Upload a CSV to get started."
                  : "No guests match your search."}
              </p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b border-gray-100 text-left text-sm text-gray-400">
                    <th className="px-6 py-3">Name</th>
                    <th className="px-6 py-3">Contact</th>
                    <th className="hidden px-6 py-3 sm:table-cell">Invitation</th>
                    <th className="px-6 py-3">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredGuests.map((guest) => (
                    <tr
                      key={guest.id}
                      className="border-b border-gray-50 transition-colors hover:bg-gray-50/50"
                    >
                      <td className="px-6 py-4 font-medium text-gray-900">
                        {guest.name}
                      </td>
                      <td className="px-6 py-4 text-sm text-gray-500">
                        {guest.contact}
                      </td>
                      <td className="hidden px-6 py-4 sm:table-cell">
                        <span className="inline-flex items-center gap-1 rounded-full bg-green-50 px-3 py-1 text-xs font-medium text-green-700">
                          Generated
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex flex-wrap gap-2">
                          <button
                            onClick={() => copyLink(guest.unique_slug)}
                            className="inline-flex items-center gap-1 rounded-lg border border-gray-200 px-3 py-1.5 text-xs font-medium text-gray-600 transition-colors hover:bg-gray-50"
                          >
                            {copiedSlug === guest.unique_slug ? (
                              "Copied!"
                            ) : (
                              <>
                                <svg
                                  className="h-3 w-3"
                                  fill="none"
                                  stroke="currentColor"
                                  viewBox="0 0 24 24"
                                >
                                  <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth={2}
                                    d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"
                                  />
                                </svg>
                                Copy
                              </>
                            )}
                          </button>
                          <a
                            href={getWhatsAppUrl(
                              guest.name,
                              guest.contact,
                              `${getBaseDomain()}/invite/${guest.unique_slug}`
                            )}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex items-center gap-1 rounded-lg bg-green-600 px-3 py-1.5 text-xs font-medium text-white transition-colors hover:bg-green-700"
                          >
                            <svg
                              className="h-3 w-3"
                              fill="currentColor"
                              viewBox="0 0 24 24"
                            >
                              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                            </svg>
                            WhatsApp
                          </a>
                          <button
                            onClick={() => deleteGuest(guest.id)}
                            className="inline-flex items-center gap-1 rounded-lg border border-red-200 px-3 py-1.5 text-xs font-medium text-red-600 transition-colors hover:bg-red-50"
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        <div className="mt-6 text-center">
          <a
            href={`/invite/${guests[0]?.unique_slug || ""}`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-xl border border-gray-200 px-6 py-3 text-sm font-medium text-gray-600 transition-colors hover:bg-gray-50"
          >
            Preview Invitation
            <svg
              className="h-4 w-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </a>
        </div>
      </main>
    </div>
  );
}

export default function DashboardPage() {
  return (
    <Suspense
      fallback={
        <div className="flex min-h-screen items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-amber-200 border-t-amber-600" />
        </div>
      }
    >
      <DashboardContent />
    </Suspense>
  );
}
