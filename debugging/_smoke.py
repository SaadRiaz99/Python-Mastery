"""Smoke test for the Debug School App.

Run from this folder:  python _smoke.py
Every check prints PASS or FAIL and the script exits non-zero on failure.

The database file is deleted first so every run starts from the same seed data.
"""

import sys

from fastapi.testclient import TestClient

from app import database

database.DB_FILE.unlink(missing_ok=True)

from app.main import app  # noqa: E402  (import after the DB reset)

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
    check(
        "index renders 5 assignments per page",
        page1
        == [
            "Algebra worksheet",
            "History timeline",
            "Map skills quiz",
            "Essay outline",
            "Book report",
        ],
        str(page1),
    )

    check(
        "status=submitted filter returns only submitted assignments",
        titles(c.get("/?status=submitted").text)
        == [
            "Algebra worksheet",
            "Map skills quiz",
            "Geometry problems",
            "Statistics homework",
            "Lab safety quiz",
        ],
        str(titles(c.get("/?status=submitted").text)),
    )
    check(
        "status=pending filter returns only pending assignments",
        "History timeline" in titles(c.get("/?status=pending").text)
        and "Algebra worksheet" not in titles(c.get("/?status=pending").text),
    )

    check("difficulty 1 filter works", len(titles(c.get("/difficulty/1").text)) == 4)
    check("difficulty 2 filter works", len(titles(c.get("/difficulty/2").text)) == 4)
    check(
        "subject filter works",
        titles(c.get("/subject/Math").text)
        == ["Algebra worksheet", "Geometry problems", "Statistics homework"],
        str(titles(c.get("/subject/Math").text)),
    )

    page2 = c.get("/?page=2").text
    check(
        "page 2 shows different assignments",
        "Geometry problems" in page2 and "Algebra worksheet" not in page2,
    )

    check("/about increments visit counter", "visited" in c.get("/about").text)
    check(
        "about shows the debugging tip",
        "reproduce it before you change anything" in c.get("/about").text.lower(),
    )

    check(
        "stats redirects when logged out",
        c.get("/stats", follow_redirects=False).status_code == 303,
    )

    bad = c.post("/login", data={"username": "admin", "password": "wrong"})
    check("bad password shows error", "Invalid username or password" in bad.text)

    ok = c.post(
        "/login",
        data={"username": "admin", "password": "admin123"},
        follow_redirects=False,
    )
    check(
        "good password logs in",
        ok.status_code == 303 and ok.headers["location"] == "/stats",
    )
    check("login sets session cookie", c.cookies.get("session_user") == "admin")

    stats = c.get("/stats")
    check("/stats works after login", stats.status_code == 200)
    data = c.get("/api/assignments").json()
    submitted = sum(1 for a in data if a["submitted"] == 1)
    expected = round(submitted / len(data) * 100, 1)
    check(
        "stats percentage is 0-100",
        f"<strong>{expected}</strong>% submitted" in stats.text,
        f"expected {expected}%",
    )

    created = c.post(
        "/assignments",
        data={"title": "Sticky test", "subject": "Science", "difficulty": "2"},
        follow_redirects=True,
    )
    check("flash message shown after create", "Assignment added" in created.text)
    check(
        "created assignment uses the form title",
        any(a["title"] == "Sticky test" for a in c.get("/api/assignments").json()),
    )
    check(
        "flash message is cleared on the next page",
        "Assignment added" not in c.get("/login").text,
    )

    assignment = next(
        a for a in c.get("/api/assignments").json() if a["title"] == "Sticky test"
    )

    edit_page = c.get(f"/assignments/{assignment['id']}/edit")
    check(
        "edit form renders the current assignment",
        edit_page.status_code == 200 and "Sticky test" in edit_page.text,
        f"status {edit_page.status_code}",
    )

    c.post(
        f"/assignments/{assignment['id']}/edit",
        data={"title": "Sticky test edited", "subject": "History", "difficulty": "1"},
    )
    edited = next(
        a for a in c.get("/api/assignments").json() if a["id"] == assignment["id"]
    )
    check(
        "edit updates title, subject and difficulty",
        edited["title"] == "Sticky test edited"
        and edited["subject"] == "History"
        and edited["difficulty"] == 1,
    )

    c.post(f"/assignments/{assignment['id']}/toggle")
    toggled = next(
        a for a in c.get("/api/assignments").json() if a["id"] == assignment["id"]
    )
    check("toggle flips the submitted flag", toggled["submitted"] == 1)

    c.post(f"/assignments/{assignment['id']}/delete")
    check(
        "delete removes the assignment",
        all(
            a["id"] != assignment["id"] for a in c.get("/api/assignments").json()
        ),
    )

    check(
        "GET /api/assignments returns JSON list",
        isinstance(c.get("/api/assignments").json(), list),
    )
    check("GET /health returns ok", c.get("/health").json() == {"status": "ok"})
    check("unknown path returns 404", c.get("/nope").status_code == 404)

failed = [label for label, passed in results if not passed]
print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
if failed:
    print("Failed:", *failed, sep="\n  - ")
    sys.exit(1)
