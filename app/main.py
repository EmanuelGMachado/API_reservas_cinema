from fastapi import FastAPI
from app.rotas import router as rotas_cinema

app = FastAPI(
    title="API de reservas de cinema",
    description="Sistema de reserva de assentos e consulta de sessões",
    version="1.0.0",
)

app.include_router(rotas_cinema)

@app.get("/")
def root():
    return {"mensagem": "API de Cinema funcionando!", "docs": "/docs"}