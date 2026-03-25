from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import connect_db, close_db
from app.routes.pagamento import router as pagamento_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()


app = FastAPI(title="API de Pagamentos", lifespan=lifespan)
app.include_router(pagamento_router)
