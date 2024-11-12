import re
from fastapi import APIRouter, HTTPException, Form
from pydantic import BaseModel, Field, EmailStr
from app.routes.register import users_db

router = APIRouter()

# Regex para validar a senha
password_regex = re.compile(
    r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
)

# Modelo de entrada com validação forte
class UserData(BaseModel):
    email: EmailStr
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


# Rota com validação de email e senha
@router.post("/login")
async def validated_login(email: str = Form(...), password: str = Form(...)):
    # Verificar se o usuário existe no banco de dados
    if email not in users_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Validar a senha forte
    validate_password(password)

    # Verificar se a senha está correta
    if users_db[email] != password:
        raise HTTPException(status_code=400, detail="Senha incorreta")

    return {"message": "Login bem-sucedido!"}


# Função para tratar a saída, escapando caracteres perigosos
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
