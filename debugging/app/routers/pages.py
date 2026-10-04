from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app import database, utils
from app.render import render

router = APIRouter()

visits = 0


@router.get("/about")
def about(request: Request):
    global visits
    visits += 1
    return render(
        request,
        "about.html",
        {
            "visits": visits,
            "summary": utils.format_title("  welcome to the debug school app  "),
        },
    )


@router.get("/stats")
def stats(request: Request):
    if not request.cookies.get("session_user"):
        return RedirectResponse(url="/login", status_code=303)

    assignments = database.fetch_all()
    submitted = sum(1 for a in assignments if a["submitted"] == 1)
    total = len(assignments)
    percent = round(submitted / total * 100, 1) if total else 0.0

    return render(
        request,
        "stats.html",
        {
            "assignments": assignments,
            "submitted": submitted,
            "total": total,
            "percent": percent,
        },
    )
