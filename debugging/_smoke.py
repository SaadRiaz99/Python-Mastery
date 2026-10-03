"""Smoke test for the Debug Todo App.

Run from this folder:  python _smoke.py
Every check prints PASS or FAIL and the script exits non-zero on failure.
"""

import sys

from fastapi.testclient import TestClient

from app.main import app

c = TestClient(app, raise_server_exceptions=False)

results = []


def check(label, condition, detail=""):
    results.append((label, bool(condition)))
    print(f"{'PASS' if condition else 'FAIL'}  {label}{'  ' + detail if detail else ''}")


def titles(html):
    out, buf = [], ""
    marker = '<span class="title">'
    start = html.find(marker)
    while start != -1:
        start += len(marker)
        end = html.find("</span>", start)
        out.append(html[start:end])
        start = html.find(marker, end)
    return out


with c:
    page1 = titles(c.get("/").text)
    check("index renders 5 todos per page", len(page1) == 5, str(page1))

    check(
        "status=done filter returns only done todos",
        titles(c.get("/?status=done").text) == ["Clean the kitchen", "Learn FastAPI", "Read a book", "Walk the dog"],
    )
    check(
        "status=pending filter returns only pending todos",
        "Buy milk" in titles(c.get("/?status=pending").text)
        and "Walk the dog" not in titles(c.get("/?status=pending").text),
    )
    check("priority 1 filter works", len(titles(c.get("/priority/1").text)) == 4)
    check("priority 2 filter works", len(titles(c.get("/priority/2").text)) == 5)

    page2 = c.get("/?page=2").text
    check("page 2 shows different todos", "Read a book" in page2 and "Buy milk" not in page2)

    check("/about increments visit counter", "visited" in c.get("/about").text)

    check("stats redirects when logged out",
          c.get("/stats", follow_redirects=False).status_code == 303)

    bad = c.post("/login", data={"username": "admin", "password": "wrong"})
    check("bad password shows error", "Invalid username or password" in bad.text)

    ok = c.post("/login", data={"username": "admin", "password": "admin123"}, follow_redirects=False)
    check("good password logs in", ok.status_code == 303 and ok.headers["location"] == "/stats")
    check("login sets session cookie", c.cookies.get("session_user") == "admin")

    stats = c.get("/stats")
    check("/stats works after login", stats.status_code == 200)
    done = sum(1 for t in c.get("/api/todos").json() if t["done"] == 1)
    total = len(c.get("/api/todos").json())
    expected = round(done / total * 100, 1)
    check("stats percentage is 0-100",
          f"<strong>{expected}</strong>% completed" in stats.text,
          f"expected {expected}%")

    created = c.post("/todos", data={"title": "Sticky test", "priority": "2"}, follow_redirects=True)
    check("flash message shown after create", "Todo added" in created.text)
    check("created todo uses the form title",
          any(t["title"] == "Sticky test" for t in c.get("/api/todos").json()))
    check("flash message is cleared on the next page",
          "Todo added" not in c.get("/login").text)

    todo = next(t for t in c.get("/api/todos").json() if t["title"] == "Sticky test")
    c.post(f"/todos/{todo['id']}/edit", data={"title": "Sticky test edited", "priority": "1"})
    edited = next(t for t in c.get("/api/todos").json() if t["id"] == todo["id"])
    check("edit updates title and priority",
          edited["title"] == "Sticky test edited" and edited["priority"] == 1)

    c.post(f"/todos/{todo['id']}/toggle")
    toggled = next(t for t in c.get("/api/todos").json() if t["id"] == todo["id"])
    check("toggle flips done flag", toggled["done"] == 1)

    c.post(f"/todos/{todo['id']}/delete")
    check("delete removes the todo",
          all(t["id"] != todo["id"] for t in c.get("/api/todos").json()))

    check("GET /api/todos returns JSON list", isinstance(c.get("/api/todos").json(), list))
    check("GET /health returns ok", c.get("/health").json() == {"status": "ok"})
    check("unknown path returns 404", c.get("/nope").status_code == 404)

failed = [label for label, passed in results if not passed]
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
if failed:
    print("Failed:", *failed, sep="\n  - ")
    sys.exit(1)
