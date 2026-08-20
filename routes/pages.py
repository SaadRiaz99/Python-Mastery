from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_supabase
from utils import get_theme, get_template_for_theme, generate_slug, format_date, format_time, get_whatsapp_url

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request, "home.html")


@router.get("/create", response_class=HTMLResponse)
async def create_page(request: Request):
    return templates.TemplateResponse(request, "create.html")


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request, wedding: str = ""):
    return templates.TemplateResponse(
        request, "dashboard.html", {"wedding_id": wedding}
    )


@router.get("/check", response_class=HTMLResponse)
async def check_invitation_page(request: Request):
    return templates.TemplateResponse(request, "check.html")


@router.get("/invite/{slug}", response_class=HTMLResponse)
async def invite_page(request: Request, slug: str):
    supabase = get_supabase()

    guest_result = (
        supabase.table("guests").select("*").eq("unique_slug", slug).execute()
    )

    if not guest_result.data:
        return templates.TemplateResponse(
            request,
            "invite_royal.html",
            {"not_found": True, "guest": None, "wedding": None},
        )

    guest = guest_result.data[0]

    wedding_result = (
        supabase.table("weddings")
        .select("*")
        .eq("id", guest["wedding_id"])
        .execute()
    )

    wedding_data = wedding_result.data[0] if wedding_result.data else None
    theme_id = wedding_data["theme"] if wedding_data else "royal"
    theme_data = get_theme(theme_id)
    template_name = get_template_for_theme(theme_id)

    return templates.TemplateResponse(
        request,
        template_name,
        {
            "not_found": False,
            "guest": guest,
            "wedding": wedding_data,
            "theme": theme_data,
            "formatted_date": format_date(wedding_data["date"]) if wedding_data else "",
            "formatted_time": format_time(wedding_data["time"]) if wedding_data else "",
        },
    )
