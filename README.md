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
│   │   └── film_db.py              # Configuração do MongoDB
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── film_repository.py      # Acesso ao banco de dados
│   ├── services/
│   │   ├── __init__.py
│   │   └── film_service.py         # Lógica de negócio
│   ├── routes/
│   │   ├── __init__.py
│   │   └── film_route.py           # Endpoints da API
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── film_schema.py          # Modelos de dados (Pydantic)
│   └── docker/
│       └── docker-compose.yml      # Configuração Docker Compose
├── doc/
│   └── EndPoints.postman_collection.json  # Coleção Postman
├── main.py                          # Aplicação FastAPI principal
├── requirements.txt                 # Dependências Python
├── .env                             # Variáveis de ambiente (não commit)
├── venv/                            # Ambiente virtual Python
├── .gitignore
├── README.md
└── .git/
```

## 🏗️ Arquitetura em Camadas

O projeto segue o padrão de **arquitetura em camadas**:

```
┌─────────────────────────────────┐
│      Routes (Endpoints)         │  ← Recebe requisições HTTP
├─────────────────────────────────┤
│      Services (Lógica)          │  ← Processa dados e validações
├─────────────────────────────────┤
│    Repositories (Dados)         │  ← Acessa o banco de dados
├─────────────────────────────────┤
│      Database (MongoDB)         │  ← Armazena dados
└─────────────────────────────────┘
```

### Responsabilidades de cada camada:

- **Routes** (`film_route.py`): Define os endpoints HTTP, valida entrada com Pydantic e orquestra chamadas aos serviços
- **Services** (`film_service.py`): Implementa a lógica de negócio, validações de dados (ObjectId), tratamento de exceções e formatação de respostas
- **Repositories** (`film_repository.py`): Acessa exclusivamente a base de dados, executando operações CRUD diretas na coleção MongoDB
- **Schemas** (`film_schema.py`): Define os modelos Pydantic para validação automática de tipos e estrutura dos dados
- **Database** (`film_db.py`): Configura e gerencia a conexão com MongoDB, exporta a instância da coleção para uso nos repositórios

### Fluxo de uma Requisição:

```
1. Cliente faz requisição HTTP POST /filmes
           ↓
2. film_route.py recebe a requisição e valida o JSON (Pydantic)
           ↓
3. film_service.py processa e converte dados (model_dump), valida ObjectId
           ↓
4. film_repository.py insere no MongoDB
           ↓
5. Serviço formata a resposta (converte _id para string)
           ↓
6. Resposta é retornada ao cliente
```

## 📋 Detalhes da Implementação

### Validação de Dados

- **Nível de Routes**: Pydantic valida automaticamente o corpo da requisição contra o modelo `Film`
- **Nível de Services**: Validação adicional de ObjectId e verificação de existência de registros

### Tratamento de Erros

Todos os serviços implementam tratamento robusto de exceções:

```python
try:
    # Operação
except HTTPException:
    raise  # Re-lança exceções HTTP (status 400, 404, etc)
except Exception as e:
    raise HTTPException(status_code=500, detail="Internal server error")
```

### Conversão de Dados

- **Entrada**: JSON → Modelo Pydantic (Film) → Dict (para MongoDB)
- **Saída**: Documento MongoDB → Dict → JSON (com _id convertido para string)

### Padrão Repository

O padrão Repository isola a lógica de acesso a dados:
- `create_repository()`: Insere novo documento
- `get_by_id_repository()`: Busca por ID do MongoDB
- `list_repository()`: Lista todos os documentos
- `update_repository()`: Atualiza um documento
- `delete_repository()`: Deleta um documento

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
  "message": "Film updated successfully!"
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

### Com Python/Requests

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
# {'message': 'Film Created', 'id': '...'}

# Listar filmes
response = requests.get(f"{BASE_URL}/filmes")
films = response.json()
print(f"Total de filmes: {films['length']}")

# Atualizar um filme
film_id = films['films'][0]['_id']
updated_film = {
    "title": "Interstellar - Atualizado",
    "description": "Descrição atualizada",
    "genre": "Ficção Científica",
    "year": 2014
}
response = requests.put(f"{BASE_URL}/filmes/{film_id}", json=updated_film)
print(response.json())

# Deletar um filme
response = requests.delete(f"{BASE_URL}/filmes/{film_id}")
print(response.json())
```

### Com requests e tratamento de erro

```python
import requests
from requests.exceptions import RequestException

try:
    response = requests.get("http://localhost:8000/filmes")
    response.raise_for_status()  # Levanta exceção para status != 2xx
    data = response.json()
    print(f"Filmes encontrados: {data['length']}")
except requests.exceptions.ConnectionError:
    print("Erro: Não foi possível conectar ao servidor")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e.response.status_code} - {e.response.json()}")
except RequestException as e:
    print(f"Erro na requisição: {e}")
```

## 📖 Documentação Interativa

A FastAPI fornece documentação interativa automática! Após iniciar a aplicação, acesse:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Na documentação interativa você pode:
- Visualizar todos os endpoints disponíveis
- Ver os schemas de requisição e resposta
- Testar os endpoints diretamente do navegador

## 🧪 Testando a API

### Com Swagger UI (Recomendado)

1. Acesse http://localhost:8000/docs
2. Clique em qualquer endpoint
3. Clique em "Try it out"
4. Preencha os parâmetros necessários
5. Clique em "Execute"

### Com cURL em diferentes cenários

**Cenário 1 - Criar múltiplos filmes:**
```bash
# Filme 1
curl -X POST http://localhost:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{"title":"Avatar","description":"Ficção científica","genre":"Sci-Fi","year":2009}'

# Filme 2
curl -X POST http://localhost:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{"title":"Dune","description":"Épico de ficção científica","genre":"Sci-Fi","year":2021}'
```

**Cenário 2 - Listar e depois atualizar:**
```bash
# 1. Listar todos os filmes (pegue o _id do filme desejado)
curl -X GET http://localhost:8000/filmes

# 2. Atualizar usando o _id obtido
curl -X PUT http://localhost:8000/filmes/[ID_OBTIDO] \
  -H "Content-Type: application/json" \
  -d '{"title":"Avatar Remastered","description":"Versão remasterizada","genre":"Sci-Fi","year":2009}'

# 3. Deletar
curl -X DELETE http://localhost:8000/filmes/[ID_OBTIDO]
```

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

### Iniciar os contêineres:
```bash
cd src/docker
docker-compose up -d
```

### Parar os contêineres:
```bash
docker-compose down
```

### Remover volumes (apaga dados do MongoDB):
```bash
docker-compose down -v
```

### Ver logs:
```bash
docker-compose logs -f
```

## 🔐 Variáveis de Ambiente

O projeto utiliza o **python-dotenv** para gerenciar variáveis de ambiente. Um arquivo `.env` é automaticamente carregado na inicialização da aplicação.

### Arquivo `.env.example`

Um arquivo `.env.example` é fornecido como template. Copie-o para criar seu próprio `.env`:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

### Variáveis Disponíveis

```env
# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27018/      # URL de conexão do MongoDB
MONGODB_DATABASE=film_database              # Nome do banco de dados
MONGODB_COLLECTION=films                    # Nome da coleção

# FastAPI Configuration
API_HOST=0.0.0.0                           # Host do servidor
API_PORT=8000                              # Porta do servidor
DEBUG=True                                 # Modo debug (True/False)

# Environment
ENVIRONMENT=development                     # Ambiente (development/production)
```

### ⚠️ Segurança

**IMPORTANTE:** Adicione `.env` ao seu `.gitignore` para evitar expor dados sensíveis:

```gitignore
# .gitignore
.env
```

O arquivo `.env.example` pode ser compartilhado no repositório como referência de configuração.

## 📝 Modelo de Dados (Schema)

### Esquema Principal - Film

```python
class Film(BaseModel):
    title: str          # Título do filme (obrigatório)
    description: str    # Descrição/sinopse (obrigatório)
    genre: str         # Gênero do filme (obrigatório)
    year: int          # Ano de lançamento (obrigatório)
```

### Modelos de Resposta

```python
class CreateFilmResponseModel(BaseModel):
    message: str  # "Film Created"
    id: str       # ID do documento inserido

class ListFilmResponseModel(BaseModel):
    films: list[Film]  # Lista de filmes
    length: int        # Quantidade de filmes

class UpdateFilmRespondeModel(BaseModel):
    message: str  # "Film updated successfully!"

class DeleteFilmResponseModel(BaseModel):
    message: str  # "Film deleted successfully!"
    id: str       # ID do documento deletado
```

### Campos no MongoDB

O MongoDB adiciona automaticamente o campo `_id` (ObjectId) para cada documento:

```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "title": "Inception",
  "description": "...",
  "genre": "Ficção Científica",
  "year": 2010
}
```

**Nota:** O `_id` é convertido para string (format_id) antes de retornar ao cliente.

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
docker-compose ps
docker-compose logs mongodb
```

### Erro ao conectar com MongoDB

Certifique-se de que:
- O contêiner do MongoDB está rodando (`docker-compose ps`)
- A URL de conexão está correta no arquivo `.env`
- A porta MongoDB (27018) não está bloqueada

### Erro: "ModuleNotFoundError"

Se receber erro de módulos não encontrados:

```bash
# Ativar o ambiente virtual e reinstalar dependências
pip install -r requirements.txt
```

### Erro de permissão no Docker

No Linux, execute com `sudo`:
```bash
sudo docker-compose up -d
```

No Windows, execute o PowerShell como administrador.

## � Adicionando Novas Funcionalidades

Para adicionar um novo campo ao modelo ou uma nova entidade, siga o padrão de camadas:

### Exemplo: Adicionar campo "director" ao Film

1. **Atualize o Schema** (`film_schema.py`):
```python
class Film(BaseModel):
    title: str
    description: str
    genre: str
    year: int
    director: str  # ← Novo campo
```

2. **Nenhuma mudança necessária no Repository** - ele já trabalha com dicts

3. **O Service funcionará automaticamente** - pydantic já faz a validação

4. **O Route funcionará automaticamente** - FastAPI já valida contra o novo schema

### Exemplo: Adicionar filtro por gênero

1. **Atualize o Repository**:
```python
def list_by_genre_repository(genre: str):
    return film_collection.find({"genre": genre})
```

2. **Atualize o Service**:
```python
def list_by_genre_service(genre: str) -> dict:
    try:
        films = [format_id(film) for film in list_by_genre_repository(genre)]
        return {"films": films, "length": len(films)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
```

3. **Atualize o Route**:
```python
@router.get("/filmes/genre/{genre}", response_model=ListFilmResponseModel)
def list_films_by_genre(genre: str):
    return list_by_genre_service(genre)
```

## 💡 Boas Práticas

### Validação de Entrada

- ✅ Deixar o Pydantic validar tipos no Route
- ✅ Validar ObjectId no Service antes de usar
- ✅ Verificar existência de registros antes de atualizar/deletar

### Tratamento de Erros

- ✅ Sempre capturar exceções genéricas e retornar status 500
- ✅ Relançar HTTPException para respeitar o tratamento específico
- ✅ Logar erros para debug (`print("error: ", e)` ou melhor ainda, usar logging)

### Estrutura de Código

- ✅ Manter cada camada com responsabilidade única
- ✅ Não misturar lógica de banco de dados com lógica de negócio
- ✅ Usar type hints em todos os parâmetros e retornos
- ✅ Documentar funções complexas com docstrings

## � Recursos Úteis

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Documentação oficial do FastAPI
- [Pydantic Documentation](https://docs.pydantic.dev/) - Validação de dados
- [PyMongo Documentation](https://pymongo.readthedocs.io/) - Driver MongoDB
- [MongoDB Documentation](https://docs.mongodb.com/) - Banco de dados
- [Docker Documentation](https://docs.docker.com/) - Containerização
- [RESTful API Best Practices](https://restfulapi.net/) - Padrões REST

## �📜 Licença

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
