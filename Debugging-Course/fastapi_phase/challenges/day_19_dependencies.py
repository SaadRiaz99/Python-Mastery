"""Day 19 — Dependencies, headers and authentication errors

Expected:
- Missing Authorization header -> 401
- Wrong token -> 401
- Header 'Authorization: Bearer learning-token' -> 200
- Route should receive the authenticated user returned by the dependency

Learning tip:
Dependencies execute before the route. If the route breakpoint is never reached,
debug the dependency input, Header declaration, return value and exception.

Never print or commit real secrets. This challenge uses a fake learning token.
"""

from fastapi import Depends, FastAPI

app = FastAPI()


def get_current_user(authorization: str = ""):
    if authorization == "learning-token":
        return {"username": "saad"}
    return None


@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return {"user": user, "private": True}
