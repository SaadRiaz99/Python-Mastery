from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from config import DEBUG, HOST, PORT, STATIC_DIR
from routes.pages import router as pages_router
from routes.api import router as api_router

app = FastAPI(title="WeddingInvite", debug=DEBUG)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.include_router(pages_router)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=DEBUG)
