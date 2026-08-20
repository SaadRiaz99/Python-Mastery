from pydantic import BaseModel


class WeddingCreate(BaseModel):
    bride_name: str
    groom_name: str
    event_type: str
    date: str
    time: str
    venue: str
    venue_address: str = ""
    theme: str = "royal"
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
    with_family: bool = False
    rsvp_status: str = "pending"
    rsvp_note: str = ""
    created_at: str


class WeddingUpdate(BaseModel):
    bride_name: str | None = None
    groom_name: str | None = None
    event_type: str | None = None
    date: str | None = None
    time: str | None = None
    venue: str | None = None
    venue_address: str | None = None
    theme: str | None = None
    message: str | None = None


class GuestCreate(BaseModel):
    name: str
    contact: str


class RSVPUpdate(BaseModel):
    status: str
    note: str = ""


class CSVGuestRow(BaseModel):
    name: str
    contact: str
