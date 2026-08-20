import { Theme } from "@/types";

export const themes: Theme[] = [
  {
    id: "mehndi",
    name: "Mehndi",
    description: "Elegant green aesthetic with floral patterns and gold details",
    colors: {
      primary: "#166534",
      secondary: "#15803d",
      accent: "#d4a843",
      background: "#f0fdf4",
      text: "#14532d",
      cardBg: "rgba(255, 255, 255, 0.95)",
      gradient: "linear-gradient(135deg, #166534 0%, #15803d 50%, #d4a843 100%)",
    },
  },
  {
    id: "barat",
    name: "Barat",
    description: "Deep maroon with luxury gold typography and royal elegance",
    colors: {
      primary: "#7f1d1d",
      secondary: "#991b1b",
      accent: "#d4a843",
      background: "#fef2f2",
      text: "#7f1d1d",
      cardBg: "rgba(255, 255, 255, 0.95)",
      gradient: "linear-gradient(135deg, #7f1d1d 0%, #991b1b 50%, #d4a843 100%)",
    },
  },
  {
    id: "nikah",
    name: "Nikah",
    description: "Ivory and white with Islamic geometric patterns, minimal and elegant",
    colors: {
      primary: "#1c1917",
      secondary: "#44403c",
      accent: "#b8860b",
      background: "#fafaf9",
      text: "#1c1917",
      cardBg: "rgba(255, 255, 255, 0.98)",
      gradient: "linear-gradient(135deg, #1c1917 0%, #44403c 50%, #b8860b 100%)",
    },
  },
  {
    id: "walima",
    name: "Walima",
    description: "White and pastel aesthetic with modern luxury design",
    colors: {
      primary: "#5b21b6",
      secondary: "#7c3aed",
      accent: "#c4b5fd",
      background: "#faf5ff",
      text: "#3b0764",
      cardBg: "rgba(255, 255, 255, 0.95)",
      gradient: "linear-gradient(135deg, #5b21b6 0%, #7c3aed 50%, #c4b5fd 100%)",
    },
  },
];

export function getTheme(id: string): Theme {
  return themes.find((t) => t.id === id) || themes[0];
}

export function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export function formatTime(timeStr: string): string {
  const [hours, minutes] = timeStr.split(":");
  const h = parseInt(hours);
  const ampm = h >= 12 ? "PM" : "AM";
  const h12 = h % 12 || 12;
  return `${h12}:${minutes} ${ampm}`;
}

export function generateSlug(): string {
  const chars = "abcdefghijklmnopqrstuvwxyz0123456789";
  let slug = "";
  for (let i = 0; i < 8; i++) {
    slug += chars[Math.floor(Math.random() * chars.length)];
  }
  return slug;
}

export function getWhatsAppUrl(
  guestName: string,
  contact: string,
  invitationLink: string
): string {
  const cleanContact = contact.replace(/[^\d+]/g, "");
  const message = encodeURIComponent(
    `Assalam-o-Alaikum ${guestName}! \n\nYou are warmly invited to celebrate our special day.\n\nView your personal wedding invitation here:\n\n${invitationLink}`
  );
  return `https://wa.me/${cleanContact}?text=${message}`;
}

export function getBaseDomain(): string {
  if (typeof window !== "undefined") {
    return window.location.origin;
  }
  return "https://your-domain.com";
}
