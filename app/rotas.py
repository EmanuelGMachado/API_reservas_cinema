import asyncio
from fastapi import APIRouter, HTTPException
from app import regras

trava_reservas = asyncio.Lock()
router = APIRouter()

@router.get("/sessoes")
def get_sessoes():
    return regras.listar_sessoes()

@router.get("/sessoes/{id_sessao}/assentos")
def get_assentos(id_sessao: int):

    assentos = regras.listar_assentos_vagos(id_sessao)

    if assentos is None:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    return assentos

@router.post("/reservar")
async def post_reserva(id_sessao: int, id_assento: str):

    async with trava_reservas:
        resultado = regras.reservar_assento(id_sessao, id_assento)

    if resultado == "sucesso":
        return {"status": "reserva confirmada"}
    elif resultado == "sessao_inexistente":
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    elif resultado == "assento_inexistente":
        raise HTTPException(status_code=404, detail="Assento não encontrado na sessão")
    elif resultado == "assento_ocupado":
        raise HTTPException(status_code=409, detail="Assento já reservado")
    else:
        raise HTTPException(status_code=400, detail="Erro desconhecido")