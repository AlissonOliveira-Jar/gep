from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter()

# Modelo de entrada sem validação adequada
class UserData(BaseModel):
    email: str
    password: str

# Rota vulnerável que aceita email e senha sem validação
@router.post("/login")
async def unvalidated_login(email: str = Form(...), password: str = Form(...)):
    return {"message": f"Login aceito sem validação: {email}"}

# Rota vulnerável com XSS (continua igual ao exemplo anterior)
@router.get("/greet")
async def greet(name: str):
    return {"message": f"Olá, {name}"}
