from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_supabase
from utils import get_theme, generate_slug, format_date, format_time, get_whatsapp_url

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/create", response_class=HTMLResponse)
async def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, wedding: str = ""):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "wedding_id": wedding}
    )


@router.get("/invite/{slug}", response_class=HTMLResponse)
async def invite_page(request: Request, slug: str):
    supabase = get_supabase()

    guest_result = (
        supabase.table("guests").select("*").eq("unique_slug", slug).execute()
    )

    if not guest_result.data:
        return templates.TemplateResponse(
            "invite.html",
            {"request": request, "not_found": True, "guest": None, "wedding": None},
        )

    guest = guest_result.data[0]

    wedding_result = (
        supabase.table("weddings")
        .select("*")
        .eq("id", guest["wedding_id"])
        .execute()
    )

    wedding_data = wedding_result.data[0] if wedding_result.data else None
    theme_data = get_theme(wedding_data["theme"]) if wedding_data else get_theme("barat")

    return templates.TemplateResponse(
        "invite.html",
        {
            "request": request,
            "not_found": False,
            "guest": guest,
            "wedding": wedding_data,
            "theme": theme_data,
            "formatted_date": format_date(wedding_data["date"]) if wedding_data else "",
            "formatted_time": format_time(wedding_data["time"]) if wedding_data else "",
        },
    )
