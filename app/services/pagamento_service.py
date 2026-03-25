from typing import Optional

from bson import ObjectId

from app.database import get_db
from app.models.pagamento import PagamentoCreate, PagamentoResponse

COLLECTION = "pagamentos"


def _doc_to_response(doc: dict) -> PagamentoResponse:
    return PagamentoResponse(
        id=str(doc["_id"]),
        cliente_id=doc["cliente_id"],
        cliente_email=doc["cliente_email"],
        codigo=doc["codigo"],
        valor_total=doc["valor_total"],
        tipo=doc["tipo"],
        parcelas=doc["parcelas"],
        valor_parcela=doc["valor_parcela"],
        data_pagamento=doc["data_pagamento"],
    )


async def create_pagamento(data: PagamentoCreate, cliente_email: str) -> PagamentoResponse:
    db = get_db()
    valor_parcela = round(data.valor_total / data.parcelas, 2)
    doc = {
        "cliente_id": data.cliente_id,
        "cliente_email": cliente_email,
        "codigo": data.codigo,
        "valor_total": data.valor_total,
        "tipo": data.tipo.value,
        "parcelas": data.parcelas,
        "valor_parcela": valor_parcela,
        "data_pagamento": data.data_pagamento.isoformat(),
    }
    result = await db[COLLECTION].insert_one(doc)
    doc["_id"] = result.inserted_id
    return _doc_to_response(doc)


async def list_pagamentos(cliente_id: Optional[str] = None) -> list[PagamentoResponse]:
    db = get_db()
    query = {}
    if cliente_id:
        query["cliente_id"] = cliente_id
    cursor = db[COLLECTION].find(query)
    return [_doc_to_response(doc) async for doc in cursor]


async def delete_pagamento(pagamento_id: str) -> bool:
    db = get_db()
    try:
        oid = ObjectId(pagamento_id)
    except Exception:
        return False
    result = await db[COLLECTION].delete_one({"_id": oid})
    return result.deleted_count == 1
