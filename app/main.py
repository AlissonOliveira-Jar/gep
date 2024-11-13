from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import unvalidated, validated, register

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.include_router(validated.router, prefix="/validated", tags=["Validated"])
app.include_router(unvalidated.router, prefix="/unvalidated", tags=["Unvalidated"])
app.include_router(register.router, prefix="/register", tags=["Register"])

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"message": None})

@app.get("/validated", response_class=HTMLResponse)
async def validated_form(request: Request):
    return templates.TemplateResponse(request, "validated_form.html", {"message": None})

@app.get("/unvalidated", response_class=HTMLResponse)
async def unvalidated_form(request: Request):
    return templates.TemplateResponse(request, "unvalidated_form.html", {"message": None})
