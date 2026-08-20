"use client";

import { motion } from "framer-motion";
import Link from "next/link";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-amber-50 to-rose-50">
      <nav className="flex items-center justify-between px-6 py-4 md:px-12">
        <div className="flex items-center gap-2">
          <div className="h-8 w-8 rounded-full bg-gradient-to-br from-amber-500 to-rose-600" />
          <span className="font-[family-name:var(--font-playfair)] text-xl font-bold text-gray-900">
            WeddingInvite
          </span>
        </div>
        <Link
          href="/create"
          className="rounded-full bg-gradient-to-r from-amber-600 to-rose-600 px-6 py-2.5 text-sm font-semibold text-white shadow-lg transition-all hover:shadow-xl hover:scale-105"
        >
          Create Invitation
        </Link>
      </nav>

      <main className="mx-auto max-w-6xl px-6 py-12 md:py-24">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center"
        >
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.6 }}
            className="mb-6 inline-flex items-center gap-2 rounded-full border border-amber-200 bg-amber-50 px-4 py-1.5 text-sm text-amber-700"
          >
            <span>&#127800;</span>
            <span>Modern Pakistani Wedding Invitations</span>
          </motion.div>

          <h1 className="mb-6 text-4xl font-bold leading-tight text-gray-900 md:text-7xl">
            Create Beautiful{" "}
            <span className="bg-gradient-to-r from-amber-600 via-rose-600 to-purple-600 bg-clip-text text-transparent">
              Personalized
            </span>
            <br />
            Wedding Invitations
          </h1>

          <p className="mx-auto mb-10 max-w-2xl text-lg text-gray-600 md:text-xl">
            Upload your guest list, generate unique invitation links for each
            guest, and share via WhatsApp. Elegant Pakistani themes with modern
            luxury design.
          </p>

          <div className="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
            <Link
              href="/create"
              className="w-full rounded-full bg-gradient-to-r from-amber-600 to-rose-600 px-8 py-4 text-lg font-semibold text-white shadow-xl transition-all hover:shadow-2xl hover:scale-105 sm:w-auto"
            >
              Start Creating
            </Link>
            <Link
              href="#features"
              className="w-full rounded-full border-2 border-gray-200 px-8 py-4 text-lg font-semibold text-gray-700 transition-all hover:border-amber-300 hover:text-amber-700 sm:w-auto"
            >
              Learn More
            </Link>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5, duration: 0.8 }}
          className="mt-16 md:mt-24"
        >
          <div className="mx-auto grid max-w-4xl grid-cols-2 gap-4 md:grid-cols-4">
            {[
              { icon: "&#128197;", label: "Multiple Themes", count: "4" },
              { icon: "&#128100;", label: "Guest Management", count: "100+" },
              { icon: "&#128279;", label: "Unique Links", count: "Auto" },
              { icon: "&#128172;", label: "WhatsApp Sharing", count: "Instant" },
            ].map((stat, i) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.7 + i * 0.1 }}
                className="rounded-2xl border border-amber-100 bg-white/80 p-4 text-center shadow-sm backdrop-blur-sm md:p-6"
              >
                <div
                  className="mb-2 text-2xl md:text-3xl"
                  dangerouslySetInnerHTML={{ __html: stat.icon }}
                />
                <div className="text-2xl font-bold text-gray-900 md:text-3xl">
                  {stat.count}
                </div>
                <div className="text-sm text-gray-500">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          id="features"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="mt-24 md:mt-32"
        >
          <h2 className="mb-4 text-center text-3xl font-bold text-gray-900 md:text-4xl">
            How It Works
          </h2>
          <p className="mb-12 text-center text-gray-500">
            Three simple steps to share your wedding joy
          </p>

          <div className="grid gap-8 md:grid-cols-3">
            {[
              {
                step: "01",
                title: "Create Wedding",
                description:
                  "Fill in your wedding details, select a beautiful Pakistani theme, and personalize your invitation message.",
                gradient: "from-emerald-500 to-green-600",
              },
              {
                step: "02",
                title: "Upload Guests",
                description:
                  "Upload a CSV file with your guest list. We'll validate the data and generate unique invitation links for each guest.",
                gradient: "from-amber-500 to-orange-600",
              },
              {
                step: "03",
                title: "Share & Celebrate",
                description:
                  "Send personalized invitations via WhatsApp. Each guest gets their own beautiful, personalized wedding card.",
                gradient: "from-rose-500 to-purple-600",
              },
            ].map((feature, i) => (
              <motion.div
                key={feature.step}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.2 }}
                className="group relative overflow-hidden rounded-3xl border border-gray-100 bg-white p-8 shadow-sm transition-all hover:shadow-xl"
              >
                <div
                  className={`mb-6 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br ${feature.gradient} text-lg font-bold text-white`}
                >
                  {feature.step}
                </div>
                <h3 className="mb-3 text-xl font-bold text-gray-900">
                  {feature.title}
                </h3>
                <p className="text-gray-500">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          className="mt-24 text-center md:mt-32"
        >
          <h2 className="mb-4 text-3xl font-bold text-gray-900 md:text-4xl">
            Beautiful Pakistani Themes
          </h2>
          <p className="mb-12 text-gray-500">
            Choose from four elegant cultural themes
          </p>

          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {[
              {
                name: "Mehndi",
                colors: "from-green-700 via-green-600 to-amber-500",
                desc: "Elegant green with floral patterns",
              },
              {
                name: "Barat",
                colors: "from-red-900 via-red-800 to-amber-500",
                desc: "Deep maroon with royal gold",
              },
              {
                name: "Nikah",
                colors: "from-gray-800 via-gray-600 to-amber-500",
                desc: "Ivory and white minimalism",
              },
              {
                name: "Walima",
                colors: "from-purple-800 via-purple-600 to-purple-300",
                desc: "Pastel modern luxury",
              },
            ].map((theme, i) => (
              <motion.div
                key={theme.name}
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="group cursor-pointer"
              >
                <div
                  className={`mb-4 aspect-[3/4] rounded-2xl bg-gradient-to-br ${theme.colors} p-6 shadow-lg transition-transform group-hover:scale-105`}
                >
                  <div className="flex h-full flex-col items-center justify-center text-white">
                    <div className="mb-2 text-4xl">&#127800;</div>
                    <div className="font-[family-name:var(--font-playfair)] text-2xl font-bold">
                      {theme.name}
                    </div>
                  </div>
                </div>
                <h3 className="font-semibold text-gray-900">{theme.name}</h3>
                <p className="text-sm text-gray-500">{theme.desc}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          className="mt-24 rounded-3xl bg-gradient-to-br from-amber-600 via-rose-600 to-purple-600 p-12 text-center text-white md:mt-32"
        >
          <h2 className="mb-4 text-3xl font-bold md:text-4xl">
            Ready to Create Your Invitation?
          </h2>
          <p className="mb-8 text-lg text-white/80">
            Start building your beautiful wedding invitation in minutes
          </p>
          <Link
            href="/create"
            className="inline-block rounded-full bg-white px-8 py-4 text-lg font-semibold text-gray-900 shadow-xl transition-all hover:shadow-2xl hover:scale-105"
          >
            Get Started Now
          </Link>
        </motion.div>
      </main>

      <footer className="mt-24 border-t border-gray-100 bg-gray-50 py-8">
        <div className="mx-auto max-w-6xl px-6 text-center text-sm text-gray-400">
          &copy; {new Date().getFullYear()} WeddingInvite. Made with love for
          beautiful celebrations.
        </div>
      </footer>
    </div>
  );
}
