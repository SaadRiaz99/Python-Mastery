from pydantic import BaseModel


class WeddingCreate(BaseModel):
    bride_name: str
    groom_name: str
    event_type: str
    date: str
    time: str
    venue: str
    venue_address: str = ""
    theme: str
    message: str = ""


class Wedding(BaseModel):
    id: str
    user_id: str
    bride_name: str
    groom_name: str
    event_type: str
    date: str
    time: str
    venue: str
    venue_address: str
    theme: str
    message: str
    created_at: str


class Guest(BaseModel):
    id: str
    wedding_id: str
    name: str
    contact: str
    unique_slug: str
    created_at: str


class GuestCreate(BaseModel):
    name: str
    contact: str


class CSVGuestRow(BaseModel):
    name: str
    contact: str
