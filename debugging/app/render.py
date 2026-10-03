from pathlib import Path

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=Path(__file__).resolve().parent / "templates")

_STORE = {"message": ""}


def flash(message=None):
    if message is not None:
        _STORE["message"] = message
        return dict(_STORE)
    pending = _STORE["message"]
    _STORE["message"] = ""
    return {"message": pending}


def render(request, name, context=None):
    ctx = dict(context or {})
    ctx.update(flash())
    ctx["request"] = request
    return templates.TemplateResponse(request, name, ctx)
