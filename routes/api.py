import uuid
import csv
import io
from fastapi import APIRouter, HTTPException
from database import get_supabase
from models import WeddingCreate, GuestCreate
from utils import generate_slug

router = APIRouter(prefix="/api", tags=["api"])


@router.post("/weddings")
async def create_wedding(data: WeddingCreate):
    supabase = get_supabase()
    user_id = str(uuid.uuid4())

    result = (
        supabase.table("weddings")
        .insert(
            {
                "bride_name": data.bride_name,
                "groom_name": data.groom_name,
                "event_type": data.event_type,
                "date": data.date,
                "time": data.time,
                "venue": data.venue,
                "venue_address": data.venue_address,
                "theme": data.theme,
                "message": data.message,
                "user_id": user_id,
            }
        )
        .execute()
    )

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create wedding")

    return {"id": result.data[0]["id"], "message": "Wedding created successfully"}


@router.get("/weddings/{wedding_id}")
async def get_wedding(wedding_id: str):
    supabase = get_supabase()
    result = (
        supabase.table("weddings").select("*").eq("id", wedding_id).execute()
    )

    if not result.data:
        raise HTTPException(status_code=404, detail="Wedding not found")

    return result.data[0]


@router.get("/weddings/{wedding_id}/guests")
async def get_guests(wedding_id: str):
    supabase = get_supabase()
    result = (
        supabase.table("guests")
        .select("*")
        .eq("wedding_id", wedding_id)
        .order("created_at", desc=True)
        .execute()
    )

    return result.data or []


@router.post("/weddings/{wedding_id}/guests")
async def add_guests(wedding_id: str, guests: list[GuestCreate]):
    supabase = get_supabase()

    existing = (
        supabase.table("guests")
        .select("contact")
        .eq("wedding_id", wedding_id)
        .execute()
    )
    existing_contacts = {g["contact"] for g in (existing.data or [])}

    new_guests = []
    duplicates = 0
    for guest in guests:
        if guest.contact in existing_contacts:
            duplicates += 1
            continue
        existing_contacts.add(guest.contact)
        new_guests.append(
            {
                "wedding_id": wedding_id,
                "name": guest.name,
                "contact": guest.contact,
                "unique_slug": generate_slug(),
            }
        )

    if not new_guests:
        raise HTTPException(
            status_code=400, detail="All guests already exist or are duplicates"
        )

    result = supabase.table("guests").insert(new_guests).execute()

    return {
        "imported": len(new_guests),
        "duplicates_skipped": duplicates,
        "message": f"{len(new_guests)} guests imported successfully",
    }


@router.post("/weddings/{wedding_id}/guests/upload-csv")
async def upload_csv_guests(wedding_id: str, csv_content: str):
    supabase = get_supabase()

    try:
        reader = csv.DictReader(io.StringIO(csv_content))
        rows = list(reader)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid CSV format")

    if not rows:
        raise HTTPException(status_code=400, detail="CSV file is empty")

    headers = [h.strip().lower() for h in rows[0].keys()]
    if "name" not in headers or "contact" not in headers:
        raise HTTPException(
            status_code=400,
            detail=f"CSV must have 'name' and 'contact' columns. Found: {', '.join(headers)}",
        )

    existing = (
        supabase.table("guests")
        .select("contact")
        .eq("wedding_id", wedding_id)
        .execute()
    )
    existing_contacts = {g["contact"] for g in (existing.data or [])}

    new_guests = []
    duplicates = 0
    for row in rows:
        name = (row.get("name", "") or "").strip()
        contact = (row.get("contact", "") or "").strip()
        if not name or not contact:
            continue
        if contact in existing_contacts:
            duplicates += 1
            continue
        existing_contacts.add(contact)
        new_guests.append(
            {
                "wedding_id": wedding_id,
                "name": name,
                "contact": contact,
                "unique_slug": generate_slug(),
            }
        )

    if not new_guests:
        raise HTTPException(
            status_code=400, detail="All guests already exist or are duplicates"
        )

    supabase.table("guests").insert(new_guests).execute()

    return {
        "imported": len(new_guests),
        "duplicates_skipped": duplicates,
        "message": f"{len(new_guests)} guests imported successfully",
    }


@router.delete("/guests/{guest_id}")
async def delete_guest(guest_id: str):
    supabase = get_supabase()
    supabase.table("guests").delete().eq("id", guest_id).execute()
    return {"message": "Guest deleted successfully"}
