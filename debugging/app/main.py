from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import database
from app.routers import login, pages, todos

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init_db()
    yield


app = FastAPI(title="Debug Todo App (intentionally buggy)", lifespan=lifespan)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(todos.router)
app.include_router(login.router)
app.include_router(pages.router)


@app.get("/health")
def health():
    return {"status": "ok"}
