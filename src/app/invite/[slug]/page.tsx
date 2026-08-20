"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { getSupabase } from "@/lib/supabase";
import { getTheme, formatDate, formatTime } from "@/lib/themes";
import type { Wedding, Guest } from "@/types";

export default function InvitePage() {
  const params = useParams();
  const slug = params.slug as string;

  const [guest, setGuest] = useState<Guest | null>(null);
  const [wedding, setWedding] = useState<Wedding | null>(null);
  const [loading, setLoading] = useState(true);
  const [notFound, setNotFound] = useState(false);

  useEffect(() => {
    const loadInvitation = async () => {
      const { data: guestData } = await getSupabase()
        .from("guests")
        .select("*")
        .eq("unique_slug", slug)
        .single();

      if (!guestData) {
        setNotFound(true);
        setLoading(false);
        return;
      }

      setGuest(guestData);

      const { data: weddingData } = await getSupabase()
        .from("weddings")
        .select("*")
        .eq("id", guestData.wedding_id)
        .single();

      setWedding(weddingData);
      setLoading(false);
    };

    loadInvitation();
  }, [slug]);

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-amber-50 to-rose-50">
        <div className="text-center">
          <div className="mx-auto mb-4 h-12 w-12 animate-spin rounded-full border-4 border-amber-200 border-t-amber-600" />
          <p className="text-gray-400">Loading your invitation...</p>
        </div>
      </div>
    );
  }

  if (notFound || !guest || !wedding) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-amber-50 to-rose-50">
        <div className="text-center">
          <div className="mb-6 text-6xl">Invalid</div>
          <h1 className="mb-2 text-2xl font-bold text-gray-900">
            Invitation Not Found
          </h1>
          <p className="text-gray-500">
            This invitation link is invalid or has expired.
          </p>
        </div>
      </div>
    );
  }

  const theme = getTheme(wedding.theme);
  const formattedDate = formatDate(wedding.date);
  const formattedTime = formatTime(wedding.time);

  return (
    <div
      className="invitation-pattern min-h-screen"
      style={{ background: theme.colors.background }}
    >
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="mx-auto min-h-screen max-w-lg px-4 py-8"
      >
        <motion.div
          initial={{ scale: 0.95, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.6 }}
          className="overflow-hidden rounded-3xl shadow-2xl"
          style={{ background: theme.colors.cardBg }}
        >
          {/* Header */}
          <div
            className="px-6 py-10 text-center"
            style={{ background: theme.colors.gradient }}
          >
            <motion.div
              initial={{ y: -20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.4 }}
              className="mb-2 text-4xl"
            >
              {wedding.theme === "mehndi" && "🌸"}
              {wedding.theme === "barat" && "💎"}
              {wedding.theme === "nikah" && "☪"}
              {wedding.theme === "walima" && "🌸"}
            </motion.div>

            <motion.div
              initial={{ y: -10, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.5 }}
              className="mb-1 text-sm font-medium uppercase tracking-widest text-white/70"
            >
              {wedding.event_type} Invitation
            </motion.div>

            <motion.div
              initial={{ y: 10, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.6 }}
            >
              <div className="font-[family-name:var(--font-playfair)] text-3xl font-bold text-white drop-shadow-lg md:text-4xl">
                {wedding.groom_name}
              </div>
              <div className="my-2 text-2xl text-white/80">&</div>
              <div className="font-[family-name:var(--font-playfair)] text-3xl font-bold text-white drop-shadow-lg md:text-4xl">
                {wedding.bride_name}
              </div>
            </motion.div>
          </div>

          {/* Guest Greeting */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.8 }}
            className="border-b px-6 py-6 text-center"
            style={{ borderColor: `${theme.colors.primary}15` }}
          >
            <div
              className="mb-1 text-sm uppercase tracking-wider"
              style={{ color: theme.colors.primary }}
            >
              Assalam-o-Alaikum
            </div>
            <div
              className="font-[family-name:var(--font-playfair)] text-2xl font-bold"
              style={{ color: theme.colors.text }}
            >
              {guest.name}!
            </div>
          </motion.div>

          {/* Message */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 1.0 }}
            className="px-6 py-6 text-center"
          >
            <p
              className="leading-relaxed"
              style={{ color: `${theme.colors.text}cc` }}
            >
              {wedding.message}
            </p>
          </motion.div>

          {/* Details */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 1.2 }}
            className="mx-4 mb-6 space-y-4 rounded-2xl p-6"
            style={{
              background: `${theme.colors.primary}08`,
              border: `1px solid ${theme.colors.primary}15`,
            }}
          >
            <div className="flex items-center gap-4">
              <div
                className="flex h-12 w-12 items-center justify-center rounded-xl text-xl"
                style={{ background: `${theme.colors.primary}15` }}
              >
                📅
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-gray-400">
                  Date
                </div>
                <div
                  className="font-medium"
                  style={{ color: theme.colors.text }}
                >
                  {formattedDate}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div
                className="flex h-12 w-12 items-center justify-center rounded-xl text-xl"
                style={{ background: `${theme.colors.primary}15` }}
              >
                🕖
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-gray-400">
                  Time
                </div>
                <div
                  className="font-medium"
                  style={{ color: theme.colors.text }}
                >
                  {formattedTime}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div
                className="flex h-12 w-12 items-center justify-center rounded-xl text-xl"
                style={{ background: `${theme.colors.primary}15` }}
              >
                📍
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-gray-400">
                  Venue
                </div>
                <div
                  className="font-medium"
                  style={{ color: theme.colors.text }}
                >
                  {wedding.venue}
                </div>
                {wedding.venue_address && (
                  <div className="text-sm text-gray-400">
                    {wedding.venue_address}
                  </div>
                )}
              </div>
            </div>
          </motion.div>

          {/* Closing */}
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 1.4 }}
            className="px-6 pb-8 text-center"
          >
            <p
              className="mb-1 text-sm font-medium"
              style={{ color: theme.colors.text }}
            >
              Your presence will make our special day even more memorable.
            </p>
            <p className="text-xs text-gray-400">
              We look forward to celebrating with you!
            </p>
          </motion.div>

          {/* Footer decoration */}
          <div className="h-2" style={{ background: theme.colors.gradient }} />
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.8 }}
          className="mt-6 text-center text-xs text-gray-400"
        >
          WeddingInvite &middot; Share the joy of love
        </motion.div>
      </motion.div>
    </div>
  );
}
