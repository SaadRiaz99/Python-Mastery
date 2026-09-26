"""Day 17 — Routing, HTTP 404/405 and route order

Expected:
- GET /users/me -> 200 and {"id": "me", "name": "Saad"}
- POST /users with {"name": "Ali"} -> 201
- GET /users/99 -> 404

Learning tips:
- 404: inspect the URL, router prefix and resource lookup.
- 405: the path exists, but the HTTP method is wrong.
- Static routes such as /users/me must not be swallowed by dynamic routes.

Preserve the expected requests.
"""

from fastapi import FastAPI , status , HTTPException
from pydantic import Field , BaseModel
app = FastAPI()
users = {1: {"id": 1, "name": "Saad"}}

class Createuser(BaseModel):
    name :str
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="Avvount Not Found"
        )
    return users[user_id]


@app.get("/users/me")
def current_user():
    return {"id": "me", "name": "Saad"}


@app.post("/users" , status_code= status.HTTP_201_CREATED)
def create_user(payload: Createuser):
    return payload
