from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.pagamento import PagamentoCreate, PagamentoResponse
from app.services import pagamento_service, user_service

router = APIRouter()


@router.get("/pagamento", response_model=list[PagamentoResponse])
async def list_pagamentos(cliente_id: Optional[str] = Query(None)):
    return await pagamento_service.list_pagamentos(cliente_id)


@router.post("/pagamento", response_model=PagamentoResponse, status_code=201)
async def create_pagamento(data: PagamentoCreate):
    user = await user_service.get_user_by_id(data.cliente_id)
    if not user:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return await pagamento_service.create_pagamento(data, cliente_email=user["email"])


@router.delete("/pagamento/{pagamento_id}")
async def delete_pagamento(pagamento_id: str):
    deleted = await pagamento_service.delete_pagamento(pagamento_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return {"detail": "Pagamento removido com sucesso"}
