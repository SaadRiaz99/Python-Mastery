# Debug Todo App

A small FastAPI + Jinja2 todo app that was shipped intentionally broken, so it can be
used to practise finding bugs the way an engineer would: reproduce, isolate, root cause,
smallest fix, re-test.

## Run it

```bash
cd debugging
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000>. Demo login: `admin` / `admin123`.

Verify the whole app:

```bash
python _smoke.py
```

The script prints `PASS`/`FAIL` for every behaviour and exits non-zero if anything regressed.

## Layout

| Path | Purpose |
|---|---|
| `app/main.py` | App factory, static mount, router registration, lifespan DB init |
| `app/database.py` | SQLite access layer for the `todos` table (seeded on first run) |
| `app/render.py` | Jinja2 `TemplateResponse` helper and one-shot flash messages |
| `app/utils.py` | Sorting, status filtering and title formatting helpers |
| `app/routers/todos.py` | List/create/edit/toggle/delete routes and the JSON API |
| `app/routers/pages.py` | `/about` visit counter and `/stats` (login required) |
| `app/routers/login.py` | Cookie-based demo login |
| `app/templates/` | Jinja2 templates, `app/static/style.css` for styling |
| `_smoke.py` | End-to-end smoke test driven by `fastapi.testclient` |

## Bugs that were found and fixed

Each entry is the *root cause*, not the symptom.

1. **`utils.sort_todos(todos, result=[])`** — mutable default argument. The list is
   created once at import time, so every call appended onto the same list and the page
   showed duplicated todos that grew on every request. Fixed by defaulting to `None`
   and copying the input.
2. **`utils.filter_todos` compared `todo["done"] == "1"`** — SQLite returns `done` as an
   `int`, so the `done`/`pending` filters always returned an empty list. Compare with `0`/`1`.
3. **`utils.format_title` had no `return`** — the function computed `title.strip().title()`
   and threw it away, so `/about` rendered `None`.
4. **`pages.about` did `visits += 1` without `global visits`** — assigning to a module
   name inside a function makes it local, so `/about` raised `UnboundLocalError` (500).
5. **Cookie name mismatch** — `login` set `token`, but `/stats` read `session_user`, so
   `/stats` redirected to `/login` even after a successful login. Both now use `session_user`.
6. **`pages.stats` percentage** — `done / total` produced a 0-1 fraction that the template
   printed after a `%` sign, and divided by zero when the table was empty. Now
   `round(done / total * 100, 1)` with a `total` guard.
7. **`todos.index` pagination off by one** — `todos[start : start + per_page - 1]` showed
   4 items on page 1 and 4 on page 2 (the skipped row simply vanished). Slice now ends at
   `start + per_page`.
8. **`todos.priority` compared `todo["priority"] == str(level)`** — priority is an `int`
   column, so every priority page was empty. Compare against the `int`.
9. **Create form field name mismatch** — the route declared `name: str = Form("")` while
   the form posts `name="title"`, so every new todo was saved with an empty title. The
   parameter is now `title: str = Form(...)`.
10. **`RedirectResponse(..., status_code=307)` after `POST /todos`** — a 307 tells the
    client to repeat the *POST* on `/`, which has no POST route (405) and never showed the
    flash message. Redirects after form posts are now `303 See Other`.
11. **`database.create_todo` never called `commit()`** — `conn.close()` discards the
    pending transaction, so new todos disappeared. Added the commit.
12. **`database.update_todo` parameter order** — the SQL is
    `SET title = ?, priority = ? WHERE id = ?` but the values were bound
    `(title, todo_id, priority)`, so saving an edit wrote the todo *id* into `priority`.
    Bound as `(title, priority, todo_id)`.
13. **`todos.api_todos` returned a coroutine** — `return database.fetch_all_async()`
    without `await` made `GET /api/todos` fail to serialize. Now `return await ...`.
14. **`render.flash` used a mutable default and never cleared** — once one todo was added,
    `Todo added` was rendered on every page forever. The store is module-level and is
    drained by `render()`, so a flash message is shown exactly once.
15. **`stats.html` used a JavaScript ternary** — `{{ todo.done ? 'Done' : 'Pending' }}`
    raised `jinja2.exceptions.TemplateSyntaxError` (500). Jinja uses
    `{{ 'Done' if todo.done else 'Pending' }}`.
16. **`login_submit` used `password is stored`** — `is` compares object identity, so a
    correct password arriving from the parsed form body did not reliably match the
    literal. Replaced with `==`.

## Prevention

- `_smoke.py` exercises every route (filters, pagination, auth, CRUD, flash, health) and
  is safe to run repeatedly — it deletes the todo it creates.
- `todos.db` and `__pycache__/` are ignored by the root `.gitignore`, so the seeded
  database never lands in a commit.
