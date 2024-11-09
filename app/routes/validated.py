from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, EmailStr
import re

router = APIRouter()

# Regex para validar a senha
password_regex = re.compile(
    r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
)


# Modelo de entrada com validação forte
class UserData(BaseModel):
    email: EmailStr  # Validação automática de email usando Pydantic
    password: str = Field(
        ...,
        min_length=8,
        description="Password must be at least 8 characters long"
    )


# Função para validar a força da senha
def validate_password(password: str):
    if not password_regex.match(password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one letter, one number, and one special character"
        )


# Rota corrigida com validação de email e senha
@router.post("/login")
async def login(data: UserData):
    # Validação da senha com regex
    validate_password(data.password)

    return {"message": f"Successfully logged in with {data.email}"}


# Rota corrigida com tratamento de saída
def escape_output(value: str) -> str:
    return (
        value.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#x27;")
    )


@router.get("/greet")
async def greet(name: str):
    safe_name = escape_output(name)
    return {"message": f"Olá, {safe_name}"}
