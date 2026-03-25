# 💳 API de Pagamentos

API REST para gerenciamento de pagamentos, feita com **FastAPI** + **MongoDB**.

Valida clientes em um serviço externo antes de registrar pagamentos, calcula parcelas automaticamente e expõe documentação interativa via Swagger.

---

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/pagamento` | Lista pagamentos (filtro opcional por `cliente_id`) |
| `POST` | `/pagamento` | Cria um pagamento (valida cliente no serviço externo) |
| `DELETE` | `/pagamento/{id}` | Remove um pagamento |

---

## Tech Stack

- **FastAPI** — framework web assíncrono
- **MongoDB** via **Motor** — driver assíncrono
- **Pydantic** — validação de dados
- **HTTPX** — comunicação com serviço de usuários
- **Docker Compose** — orquestração local

---

## Como rodar

### Com Docker (recomendado)

```bash
# 1. Configure as credenciais do MongoDB
cp .env.example .env

# 2. Suba os containers
docker-compose up --build
```

A API fica disponível em **http://localhost:8080**

### Sem Docker

```bash
# 1. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure o .env com suas credenciais MongoDB
cp .env.example .env

# 4. Rode o servidor
uvicorn app.main:app --reload
```

A API fica disponível em **http://localhost:8000**

---

## Variáveis de ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `MONGO_USER` | Usuário do MongoDB | — |
| `MONGO_PASS` | Senha do MongoDB | — |
| `MONGO_HOST` | Host do MongoDB | `mongodb` |
| `MONGO_PORT` | Porta do MongoDB | `27017` |
| `MONGO_DB` | Nome do banco | `pagamentos_db` |
| `USERS_API_BASE` | URL do serviço de usuários | `http://18.228.48.67` |

---

## Estrutura

```
app/
├── main.py              # Entrypoint do FastAPI
├── config.py            # Variáveis de ambiente (Pydantic Settings)
├── database.py          # Conexão MongoDB
├── models/
│   └── pagamento.py     # Schemas Pydantic (create/response)
├── routes/
│   └── pagamento.py     # Endpoints da API
└── services/
    ├── pagamento_service.py   # CRUD de pagamentos
    └── user_service.py        # Consulta ao serviço de usuários
```

---

## Documentação interativa

Com a API rodando, acesse:

- **Swagger UI** → [localhost:8080/docs](http://localhost:8080/docs)
- **ReDoc** → [localhost:8080/redoc](http://localhost:8080/redoc)
