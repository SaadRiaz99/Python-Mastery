from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from app.render import render

router = APIRouter()

USERS = {"admin": "admin123"}


@router.get("/login")
def login_form(request: Request):
    return render(request, "login.html")


@router.post("/login")
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    stored = USERS.get(username)
    if stored is not None and password == stored:
        response = RedirectResponse(url="/stats", status_code=303)
        response.set_cookie("session_user", username)
        return response
    return render(
        request, "login.html", {"error": "Invalid username or password"}
    )
