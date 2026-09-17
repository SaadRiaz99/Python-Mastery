"""Day 21 — Data lifecycle and resource lookup

Expected:
- POST /tasks twice creates IDs 1 and 2.
- DELETE /tasks/1 removes only task 1.
- Next POST creates ID 3, never reuses an existing ID.
- GET missing task returns 404, not 200/null.

Learning tip:
Separate storage behavior from HTTP behavior. Trace who owns the state, how IDs
are generated, and what a missing lookup returns. A broad except hides evidence.

For this lesson the in-memory store is intentional; do not add a database yet.
"""

from fastapi import FastAPI

app = FastAPI()
tasks: list[dict] = []


@app.post("/tasks")
def create_task(payload: dict):
    task = {"id": len(tasks) + 1, "title": payload["title"]}
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return next(task for task in tasks if task["id"] == task_id)
    except:
        return None


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id)
    return {"deleted": True}
