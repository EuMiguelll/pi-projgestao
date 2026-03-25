from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class TipoPagamento(str, Enum):
    PIX = "PIX"
    CREDITO = "Crédito"


class PagamentoCreate(BaseModel):
    cliente_id: str
    codigo: str
    valor_total: float = Field(gt=0)
    tipo: TipoPagamento
    parcelas: int = Field(ge=1)
    data_pagamento: date


class PagamentoResponse(BaseModel):
    id: str
    cliente_id: str
    cliente_email: str
    codigo: str
    valor_total: float
    tipo: TipoPagamento
    parcelas: int
    valor_parcela: float
    data_pagamento: date
