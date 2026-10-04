from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from app import database, utils
from app.render import flash, render

router = APIRouter()


@router.get("/")
def index(request: Request, page: int = 1, status: str = "all"):
    assignments = utils.filter_assignments(
        utils.sort_assignments(database.fetch_all()), status
    )

    per_page = 5
    start = (page - 1) * per_page
    items = assignments[start : start + per_page]

    return render(
        request,
        "index.html",
        {
            "assignments": items,
            "subjects": database.SUBJECTS,
            "page": page,
            "total_pages": max(1, -(-len(assignments) // per_page)),
            "total": len(assignments),
            "status": status,
        },
    )


@router.get("/difficulty/{level}")
def difficulty(request: Request, level: int):
    rows = [a for a in database.fetch_all() if a["difficulty"] == level]
    rows.sort(key=lambda a: a["id"])
    return render(
        request, "difficulty.html", {"assignments": rows, "level": level}
    )


@router.get("/subject/{subject}")
def subject(request: Request, subject: str):
    rows = [
        a
        for a in database.fetch_all()
        if a["subject"].lower() == subject.lower()
    ]
    rows.sort(key=lambda a: (a["difficulty"], a["id"]))
    return render(
        request,
        "subject.html",
        {"assignments": rows, "subject": subject, "subjects": database.SUBJECTS},
    )


@router.post("/assignments")
def create_assignment(
    request: Request,
    title: str = Form(...),
    subject: str = Form("Math"),
    difficulty: int = Form(2),
):
    database.create_assignment(title, subject, difficulty)
    flash("Assignment added")
    return RedirectResponse(url="/", status_code=303)


@router.get("/assignments/{assignment_id}/edit")
def edit_form(request: Request, assignment_id: int):
    assignment = database.fetch_one(assignment_id)
    if assignment is None:
        return RedirectResponse(url="/", status_code=303)
    return render(
        request,
        "edit.html",
        {"assignment": assignment, "subjects": database.SUBJECTS},
    )


@router.post("/assignments/{assignment_id}/edit")
def edit_save(
    assignment_id: int,
    title: str = Form(...),
    subject: str = Form("Math"),
    difficulty: int = Form(2),
):
    database.update_assignment(assignment_id, title, subject, difficulty)
    return RedirectResponse(url="/", status_code=303)


@router.post("/assignments/{assignment_id}/toggle")
def toggle(assignment_id: int):
    database.toggle_submitted(assignment_id)
    return RedirectResponse(url="/", status_code=303)


@router.post("/assignments/{assignment_id}/delete")
def delete(assignment_id: int):
    database.delete_assignment(assignment_id)
    return RedirectResponse(url="/", status_code=303)


@router.get("/api/assignments")
async def api_assignments():
    return await database.fetch_all_async()
