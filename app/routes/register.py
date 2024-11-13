from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr

router = APIRouter()

users_db = {}

templates = Jinja2Templates(directory="app/templates")

class RegisterData(BaseModel):
    email: EmailStr
    password: str

@router.get("/", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse(request, "register.html")

@router.post("/", response_class=HTMLResponse)
async def register_user(request: Request, email: str = Form(...), password: str = Form(...)):
    if email in users_db:
        message = "Usuário já registrado"
        raise HTTPException(status_code=400, detail=message)

    users_db[email] = password
    message = "Usuário registrado com sucesso!"
    return templates.TemplateResponse(request, "register.html", {"message": message})
