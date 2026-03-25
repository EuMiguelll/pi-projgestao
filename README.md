# API de Pagamentos

Uma API RESTful para gerenciamento de pagamentos desenvolvida com **FastAPI** e **MongoDB**, projetada para ser rápida, assíncrona e fácil de escalar. Esta API se comunica internamente com um serviço de usuários para validar a existência do cliente antes de processar um pagamento.

## 🚀 Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem principal.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web assíncrono de alto desempenho.
- **[MongoDB (Motor)](https://motor.readthedocs.io/)**: Banco de dados NoSQL com driver assíncrono oficial.
- **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados genéricos baseada em annotations do Python.
- **[Docker / Docker Compose](https://www.docker.com/)**: Containerização e orquestração local.
- **[HTTPX](https://www.python-httpx.org/)**: Cliente HTTP assíncrono para comunicação entre serviços.

---

## ⚙️ Funcionalidades

- **`GET /pagamento`**: Lista todos os pagamentos. Permite filtragem por `cliente_id`.
- **`POST /pagamento`**: Cria um novo registro de pagamento. Valida se o cliente existe em um serviço externo (User Service) antes da criação.
- **`DELETE /pagamento/{pagamento_id}`**: Remove um pagamento existente da base de dados.

---

## 📂 Estrutura do Projeto

```text
├── app/
│   ├── models/           # Definição e schemas do Pydantic (ex: PagamentoCreate)
│   ├── routes/           # Rotas/Endpoints da API (ex: pagamento.py)
│   ├── services/         # Lógica de negócio e comunicação externa (pagamento_service, user_service)
│   ├── config.py         # Configurações de ambiente
│   ├── database.py       # Conexão e fechamento do banco MongoDB
│   └── main.py           # Ponto de entrada (Entrypoint) do FastAPI
├── Dockerfile            # Configuração de container da aplicação
├── docker-compose.yml    # Orquestração do banco e da aplicação
└── requirements.txt      # Dependências do Python
```

---

## 🛠️ Como Executar

### Pré-requisitos
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados (Recomendado).
- Alternativamente, Python 3.10+ para rodar localmente sem Docker (requer uma instância do MongoDB acessível).

### 🐳 Via Docker (Recomendado)

A forma mais simples de subir a aplicação e suas dependências (MongoDB) é através do Docker.

1. Na raiz do projeto, execute o comando:
   ```bash
   docker-compose up --build
   ```
2. A API estará disponível em: `http://localhost:8000`

### 🖥️ Localmente (Ambiente Virtual Python)

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou no Windows: venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Defina as variáveis de ambiente necessárias (como a URI do MongoDB, caso exigido pelo `app/config.py`).
4. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📖 Documentação da API

O FastAPI gera a documentação interativa automaticamente (Swagger e ReDoc). Assim que a API estiver rodando, acesse em seu navegador:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Lá você poderá testar todas as rotas diretamente pela interface!
