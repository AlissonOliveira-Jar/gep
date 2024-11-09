from fastapi import FastAPI
from app.routes import unvalidated, validated

app = FastAPI()

app.include_router(
    unvalidated.router,
    prefix="/unvalidated",
    tags=["Unvalidated"]
)

app.include_router(
    validated.router,
    prefix="/validated",
    tags=["Validated"]
)


@app.get("/")
async def root():
    return {"message": "Bem vindo ao Unvalidated vs Validated Input/Output"}
