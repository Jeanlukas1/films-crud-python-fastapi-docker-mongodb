# 🎬 Films CRUD - FastAPI + Docker + MongoDB

Uma aplicação CRUD completa para gerenciamento de filmes, desenvolvida com **FastAPI**, containerizada com **Docker** e utilizando **MongoDB** como banco de dados.

## 📋 Sobre o Projeto

Este projeto é uma API RESTful robusta para criar, ler, atualizar e deletar informações de filmes. A aplicação segue as melhores práticas de desenvolvimento, com arquitetura modular, validação de dados e fácil deploy via Docker.

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e de alto desempenho
- **Python 3** - Linguagem de programação
- **MongoDB** - Banco de dados NoSQL
- **Docker & Docker Compose** - Containerização e orquestração
- **Pydantic** - Validação de dados
- **PyMongo** - Driver MongoDB para Python
- **Uvicorn** - Servidor ASGI

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.8+ (opcional, apenas se executar sem Docker)
- [Git](https://git-scm.com/)

## 📁 Estrutura do Projeto

```
films-crud-python-fastapi-docker-mongodb/
├── src/
│   ├── db/
│   │   ├── __init__.py
│   │   └── film_db.py          # Configuração do MongoDB com variáveis de ambiente
│   ├── routes/
│   │   ├── __init__.py
│   │   └── film_route.py       # Endpoints da API
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── film_schema.py      # Modelo de dados (Pydantic)
│   └── docker/
│       └── docker-compose.yml  # Configuração Docker
├── doc/
│   └── EndPoints.postman_collection.json  # Coleção Postman com todos endpoints
├── main.py                      # Aplicação FastAPI principal (raiz)
├── requirements.txt             # Dependências Python (raiz)
├── .env                         # Variáveis de ambiente (não commit)
├── venv/                        # Ambiente virtual Python
├── .gitignore
├── README.md
└── .git/
```

## 🔧 Instalação

### Opção 1: Com Docker (Recomendado)

1. **Clone o repositório:**
```bash
git clone https://github.com/Jeanlukas1/films-crud-python-fastapi-docker-mongodb.git
cd films-crud-python-fastapi-docker-mongodb
```

2. **Navegue até a pasta src (onde está o docker-compose):**
```bash
cd src/docker
```

3. **Inicie os contêineres:**
```bash
docker-compose up -d
```

4. **Volte à raiz do projeto:**
```bash
cd ../..
```

5. **A aplicação estará disponível em:**
```
http://localhost:8000
```

### Opção 2: Instalação Local

1. **Clone o repositório:**
```bash
git clone https://github.com/Jeanlukas1/films-crud-python-fastapi-docker-mongodb.git
cd films-crud-python-fastapi-docker-mongodb
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Copie o arquivo `.env.example` como referência e crie um arquivo `.env` na raiz do projeto:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Depois edite o arquivo `.env` com suas configurações (se necessário):

```env
# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27018/
MONGODB_DATABASE=film_database
MONGODB_COLLECTION=films

# FastAPI Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Environment
ENVIRONMENT=development
```

5. **Inicie a aplicação:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 Endpoints da API

### 1. Criar um Filme

**POST** `/filmes`

**Status Code:** 201 Created

**Request Body:**
```json
{
  "title": "Inception",
  "description": "Um ladrão que rouba segredos corporativos através de tecnologia de sonhos compartilhados",
  "genre": "Ficção Científica",
  "year": 2010
}
```

**Response:**
```json
{
  "message": "Film Created",
  "id": "507f1f77bcf86cd799439011"
}
```

---

### 2. Listar Todos os Filmes

**GET** `/filmes`

**Status Code:** 200 OK

**Response:**
```json
{
  "films": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "title": "Inception",
      "description": "Um ladrão que rouba segredos corporativos através de tecnologia de sonhos compartilhados",
      "genre": "Ficção Científica",
      "year": 2010
    },
    {
      "_id": "507f1f77bcf86cd799439012",
      "title": "The Matrix",
      "description": "Um hacker descobre que a realidade em que vive é uma simulação",
      "genre": "Ficção Científica",
      "year": 1999
    }
  ],
  "length": 2
}
```

---

### 3. Atualizar um Filme

**PUT** `/filmes/{_id}`

**Status Code:** 200 OK

**Request Body:**
```json
{
  "title": "Inception (Atualizado)",
  "description": "Um ladrão que rouba segredos corporativos através de tecnologia de sonhos compartilhados",
  "genre": "Ficção Científica",
  "year": 2010
}
```

**Response:**
```json
{
  "message": "Film updated succefully!"
}
```

**Error (404):**
```json
{
  "detail": "Film not found"
}
```

---

### 4. Deletar um Filme

**DELETE** `/filmes/{_id}`

**Status Code:** 200 OK

**Response:**
```json
{
  "message": "Film deleted successfully!"
}
```

---

## 🧪 Exemplos de Uso

### Com cURL

**Criar um filme:**
```bash
curl -X POST http://localhost:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Avatar",
    "description": "Um soldado paralítico se oferece para controlar um avatar biologicamente compatível",
    "genre": "Ficção Científica",
    "year": 2009
  }'
```

**Listar filmes:**
```bash
curl -X GET http://localhost:8000/filmes
```

**Atualizar um filme:**
```bash
curl -X PUT http://localhost:8000/filmes/507f1f77bcf86cd799439011 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Avatar",
    "description": "Um soldado paralítico",
    "genre": "Ficção Científica",
    "year": 2009
  }'
```

**Deletar um filme:**
```bash
curl -X DELETE http://localhost:8000/filmes/507f1f77bcf86cd799439011
```

### Com Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Criar um filme
film_data = {
    "title": "Interstellar",
    "description": "Exploradores viajam através de um buraco de minhoca",
    "genre": "Ficção Científica",
    "year": 2014
}
response = requests.post(f"{BASE_URL}/filmes", json=film_data)
print(response.json())

# Listar filmes
response = requests.get(f"{BASE_URL}/filmes")
print(response.json())
```

## 📖 Documentação Interativa

A FastAPI fornece documentação interativa automática! Após iniciar a aplicação, acesse:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📮 Coleção Postman

Importe a coleção Postman com todos os endpoints já configurados:

**[Abrir Coleção Postman Online](https://www.postman.com/lukasjean745-1800510/workspace/filme-crud-fastapi-docker-mongodb)**

Ou importe localmente a coleção em `doc/EndPoints.postman_collection.json`:

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo `doc/EndPoints.postman_collection.json`
4. A coleção será adicionada com todos os endpoints configurados

A coleção inclui exemplos de requisições para todos os endpoints da API, facilitando os testes e a integração com outros serviços.

## 🐳 Gerenciando Docker
O projeto utiliza o **python-dotenv** para gerenciar variáveis de ambiente. Um arquivo `.env` é automaticamente carregado na inicialização da aplicação.

### Arquivo `.env.example`

Um arquivo `.env.example` é fornecido como template. Copie-o para criar seu próprio `.env`:

```bash
cp .env.example .env
```

### Variáveis Disponíveis

```env
# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27018/      # URL de conexão do MongoDB
MONGODB_DATABASE=film_database              # Nome do banco de dados
MONGODB_COLLECTION=films                    # Nome da coleção

# FastAPI Configuration
API_HOST=0.0.0.0                           # Host do servidor (0.0.0.0 para aceitar conexões externas)
API_PORT=8000                              # Porta do servidor
DEBUG=True                                 # Modo debug (True/False)

# Environment
ENVIRONMENT=development                     # Ambiente (development/production)
```

### Segurança

⚠️ **IMPORTANTE:** Adicione `.env` ao seu `.gitignore` para evitar expor dados sensíveis:

```gitignore
# .gitignore
.env
```

O arquivo `.env.example` pode ser compartilhado no repositório como referência de configuração.arar os contêineres:**
```bash
docker-compose down
```

**Remover volumes (apaga dados do MongoDB):**
```bash
docker-compose down -v
```

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (opcional):

```env
# MongoDB
MONGODB_URL=mongodb://mongodb:27017/
DATABASE_NAME=filmes_db
COLLECTION_NAME=filmes

# FastAPI
API_HOST=0.0.0.0
API_PORT=8000
```

## 📝 Modelo de Dados (Schema)

```python
class Film(BaseModel):
    title: str          # Título do filme
    description: str    # Descrição/sinopse
    genre: str         # Gênero do filme
    year: int          # Ano de lançamento
```

## 🆘 Troubleshooting

### Porta já está em uso

Se a porta 8000 já está em uso:

```bash
# Mudar a porta na inicialização
uvicorn main:app --port 8001
```

### MongoDB não conecta

Verificar se o contêiner está rodando:
```bash
docker-compose logs mongodb
```

### Erro de permissão no Docker

Execute com `sudo` no Linux ou execute o PowerShell como administrador no Windows

## 🚀 Deploy

### Deploy no Heroku

1. Criar um `Procfile`:
```
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

2. Fazer push para Heroku:
```bash
git push heroku main
```

### Deploy com AWS/Google Cloud

Consulte a documentação oficial de Deploy do FastAPI.

## 📜 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através do GitHub ou abra uma issue.

---

**Desenvolvido com ❤️ usando FastAPI**
