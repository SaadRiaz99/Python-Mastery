from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from app import database, utils
from app.render import flash, render

router = APIRouter()


@router.get("/")
def index(request: Request, page: int = 1, status: str = "all"):
    todos = utils.filter_todos(utils.sort_todos(database.fetch_all()), status)

    per_page = 5
    start = (page - 1) * per_page
    items = todos[start : start + per_page]

    return render(
        request,
        "index.html",
        {
            "todos": items,
            "page": page,
            "total_pages": max(1, -(-len(todos) // per_page)),
            "total": len(todos),
            "status": status,
        },
    )


@router.get("/priority/{level}")
def priority(request: Request, level: int):
    todos = [todo for todo in database.fetch_all() if todo["priority"] == level]
    return render(request, "priority.html", {"todos": todos, "level": level})


@router.post("/todos")
def create_todo(
    request: Request,
    title: str = Form(...),
    priority: int = Form(2),
):
    database.create_todo(title, priority)
    flash("Todo added")
    return RedirectResponse(url="/", status_code=303)


@router.get("/todos/{todo_id}/edit")
def edit_form(request: Request, todo_id: int):
    todo = database.fetch_one(todo_id)
    if todo is None:
        return RedirectResponse(url="/", status_code=303)
    return render(request, "edit.html", {"item": todo})


@router.post("/todos/{todo_id}/edit")
def edit_save(
    todo_id: int,
    title: str = Form(...),
    priority: int = Form(2),
):
    database.update_todo(todo_id, title, priority)
    return RedirectResponse(url="/", status_code=303)


@router.post("/todos/{todo_id}/toggle")
def toggle(todo_id: int):
    database.toggle_done(todo_id)
    return RedirectResponse(url="/", status_code=303)


@router.post("/todos/{todo_id}/delete")
def delete(todo_id: int):
    database.delete_todo(todo_id)
    return RedirectResponse(url="/", status_code=303)


@router.get("/api/todos")
async def api_todos():
    return await database.fetch_all_async()
