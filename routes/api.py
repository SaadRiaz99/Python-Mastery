import uuid
import csv
import io
import traceback
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from database import get_supabase
from models import WeddingCreate, WeddingUpdate, GuestCreate, RSVPUpdate
from utils import generate_slug

router = APIRouter(prefix="/api", tags=["api"])


def _handle_error(e: Exception):
    tb = traceback.format_exception(type(e), e, e.__traceback__)
    print("API ERROR:", "".join(tb))
    return JSONResponse(
        status_code=500,
        content={"detail": str(e)},
    )


@router.post("/weddings")
async def create_wedding(data: WeddingCreate):
    try:
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
            raise Exception("Failed to create wedding - no data returned")

        return {"id": result.data[0]["id"], "message": "Wedding created successfully"}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.get("/weddings/{wedding_id}")
async def get_wedding(wedding_id: str):
    try:
        supabase = get_supabase()
        result = (
            supabase.table("weddings").select("*").eq("id", wedding_id).execute()
        )

        if not result.data:
            raise HTTPException(status_code=404, detail="Wedding not found")

        return result.data[0]
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.patch("/weddings/{wedding_id}")
async def update_wedding(wedding_id: str, data: WeddingUpdate):
    try:
        supabase = get_supabase()

        existing = supabase.table("weddings").select("id").eq("id", wedding_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail="Wedding not found")

        update_fields = {k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None}
        if not update_fields:
            raise HTTPException(status_code=400, detail="No fields to update")

        supabase.table("weddings").update(update_fields).eq("id", wedding_id).execute()

        return {"message": "Wedding updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.get("/weddings/{wedding_id}/guests")
async def get_guests(wedding_id: str):
    try:
        supabase = get_supabase()
        result = (
            supabase.table("guests")
            .select("*")
            .eq("wedding_id", wedding_id)
            .order("created_at", desc=True)
            .execute()
        )

        return result.data or []
    except Exception as e:
        return _handle_error(e)


@router.post("/weddings/{wedding_id}/guests")
async def add_guests(wedding_id: str, guests: list[GuestCreate]):
    try:
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
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.post("/weddings/{wedding_id}/guests/upload-csv")
async def upload_csv_guests(wedding_id: str, csv_content: str):
    try:
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

        has_family_col = "with_family" in headers

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
            with_family = False
            if has_family_col:
                val = (row.get("with_family", "") or "").strip().lower()
                with_family = val in ("true", "yes", "1", "y", "family")
            new_guests.append(
                {
                    "wedding_id": wedding_id,
                    "name": name,
                    "contact": contact,
                    "unique_slug": generate_slug(),
                    "with_family": with_family,
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
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.delete("/guests/{guest_id}")
async def delete_guest(guest_id: str):
    try:
        supabase = get_supabase()
        supabase.table("guests").delete().eq("id", guest_id).execute()
        return {"message": "Guest deleted successfully"}
    except Exception as e:
        return _handle_error(e)


@router.patch("/guests/{guest_id}/rsvp")
async def update_rsvp(guest_id: str, data: RSVPUpdate):
    try:
        supabase = get_supabase()

        existing = supabase.table("guests").select("*").eq("id", guest_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail="Guest not found")

        supabase.table("guests").update(
            {"rsvp_status": data.status, "rsvp_note": data.note}
        ).eq("id", guest_id).execute()

        return {"message": "RSVP updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)


@router.get("/guests/lookup")
async def lookup_guest(name: str, contact: str = ""):
    try:
        supabase = get_supabase()

        result = supabase.table("guests").select("*").execute()
        guests = result.data or []

        name_lower = name.strip().lower()
        contact_clean = "".join(c for c in contact if c.isdigit() or c == "+").strip()

        matches = []
        for g in guests:
            name_match = name_lower in g["name"].lower() or g["name"].lower() in name_lower
            if not name_match:
                continue
            if contact_clean:
                g_clean = "".join(c for c in g["contact"] if c.isdigit() or c == "+")
                if contact_clean == g_clean or contact_clean.endswith(g_clean[-8:]) or g_clean.endswith(contact_clean[-8:]):
                    matches.append(g)
            else:
                matches.append(g)

        if not matches:
            return {"found": False, "guests": [], "message": "No guest found. You may not be on the invitation list."}

        enriched = []
        for g in matches:
            w_result = supabase.table("weddings").select("*").eq("id", g["wedding_id"]).execute()
            wedding = w_result.data[0] if w_result.data else None
            enriched.append({**g, "wedding": wedding})

        return {"found": True, "guests": enriched, "message": f"Found {len(enriched)} match(es)."}
    except Exception as e:
        return _handle_error(e)
