export interface WeddingFormData {
  bride_name: string;
  groom_name: string;
  event_type: EventType;
  date: string;
  time: string;
  venue: string;
  venue_address: string;
  theme: EventType;
  message: string;
}

import { EventType } from "@/types";
