import uuid
import csv
import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from database import get_supabase
from models import WeddingCreate, WeddingUpdate, GuestCreate, RSVPUpdate
from utils import generate_slug

router = APIRouter(prefix='/api', tags=['api'])

def _handle_error(e):
    return JSONResponse(status_code=500, content={'detail': str(e)})

@router.post('/weddings')
async def create_wedding(data: WeddingCreate):
    try:
        supabase = get_supabase()
        user_id = str(uuid.uuid4())
        result = supabase.table('weddings').insert({
            'bride_name': data.bride_name, 'groom_name': data.groom_name,
            'event_type': data.event_type, 'date': data.date, 'time': data.time,
            'venue': data.venue, 'venue_address': data.venue_address,
            'theme': data.theme, 'message': data.message, 'user_id': user_id,
        }).execute()
        if not result.data:
            raise Exception('Failed to create wedding')
        return {'id': result.data[0]['id'], 'message': 'Wedding created successfully'}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)

@router.get('/weddings/{wedding_id}')
async def get_wedding(wedding_id: str):
    try:
        supabase = get_supabase()
        result = supabase.table('weddings').select('*').eq('id', wedding_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail='Wedding not found')
        return result.data[0]
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)

@router.patch('/weddings/{wedding_id}')
async def update_wedding(wedding_id: str, data: WeddingUpdate):
    try:
        supabase = get_supabase()
        existing = supabase.table('weddings').select('id').eq('id', wedding_id).execute()
        if not existing.data:
            raise HTTPException(status_code=404, detail='Wedding not found')
        update_fields = {k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None}
        supabase.table('weddings').update(update_fields).eq('id', wedding_id).execute()
        return {'message': 'Wedding updated successfully'}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)

@router.get('/weddings/{wedding_id}/guests')
async def get_guests(wedding_id: str):
    try:
        supabase = get_supabase()
        result = supabase.table('guests').select('*').eq('wedding_id', wedding_id).execute()
        return result.data or []
    except Exception as e:
        return _handle_error(e)

@router.post('/weddings/{wedding_id}/guests')
async def add_guests(wedding_id: str, guests: list[GuestCreate]):
    try:
        supabase = get_supabase()
        existing = supabase.table('guests').select('contact').eq('wedding_id', wedding_id).execute()
        existing_contacts = {g['contact'] for g in (existing.data or [])}
        new_guests = []
        for guest in guests:
            if guest.contact in existing_contacts:
                continue
            existing_contacts.add(guest.contact)
            new_guests.append({'wedding_id': wedding_id, 'name': guest.name, 'contact': guest.contact, 'unique_slug': generate_slug()})
        if new_guests:
            supabase.table('guests').insert(new_guests).execute()
        return {'imported': len(new_guests)}
    except HTTPException:
        raise
    except Exception as e:
        return _handle_error(e)

@router.delete('/guests/{guest_id}')
async def delete_guest(guest_id: str):
    try:
        supabase = get_supabase()
        supabase.table('guests').delete().eq('id', guest_id).execute()
        return {'message': 'Guest deleted'}
    except Exception as e:
        return _handle_error(e)

@router.patch('/guests/{guest_id}/rsvp')
async def update_rsvp(guest_id: str, data: RSVPUpdate):
    try:
        supabase = get_supabase()
        supabase.table('guests').update({'rsvp_status': data.status, 'rsvp_note': data.note}).eq('id', guest_id).execute()
        return {'message': 'RSVP updated'}
    except Exception as e:
        return _handle_error(e)
