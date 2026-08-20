export type EventType = "mehndi" | "barat" | "nikah" | "walima";

export type Theme = {
  id: EventType;
  name: string;
  description: string;
  colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    text: string;
    cardBg: string;
    gradient: string;
  };
};

export interface Wedding {
  id: string;
  user_id: string;
  bride_name: string;
  groom_name: string;
  event_type: EventType;
  date: string;
  time: string;
  venue: string;
  venue_address: string;
  theme: EventType;
  message: string;
  created_at: string;
}

export interface Guest {
  id: string;
  wedding_id: string;
  name: string;
  contact: string;
  unique_slug: string;
  created_at: string;
}

export interface CSVRow {
  name: string;
  contact: string;
}
