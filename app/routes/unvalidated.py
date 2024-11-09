from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


# Modelo de entrada sem validação adequada
class UserData(BaseModel):
    email: str
    password: str


# Rota vulnerável que aceita email e senha sem validação
@router.post("/login")
async def login(data: UserData):
    # Valida se o email está no formato correto ou se a senha é forte
    return {"message": f"Logado como {data.email}"}


# Rota vulnerável com XSS (continua igual ao exemplo anterior)
@router.get("/greet")
async def greet(name: str):
    return {"message": f"Olá, {name}"}
