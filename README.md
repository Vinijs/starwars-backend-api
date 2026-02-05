# Star Wars Backend API

API desenvolvida em Python com Flask para consumir e organizar dados do universo Star Wars.

## Tecnologias
- Python 3
- Flask
- API SWAPI

## Como rodar o projeto

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
flask --app app.main run
```

## Endpoints disponíveis

### 🎬 Filmes

- **GET /films**  
  Retorna todos os filmes da saga Star Wars.

- **GET /films?search=hope**  
  Retorna filmes filtrados pelo título.

#### Respostas possíveis
- `200 OK` — sucesso
- `404 Not Found` — filme não encontrado

## Exemplos de uso

GET /films
GET /films?search=hope
GET /people?page=2
GET /people?order=name

## Arquitetura

- `main.py`: definição das rotas HTTP
- `services/`: integração com APIs externas (SWAPI)
- `helpers/`: funções reutilizáveis de filtros e regras comuns

O projeto foi refatorado para evitar duplicação de código, utilizando helpers reutilizáveis para filtros e serviços dedicados para integração com a SWAPI.

### Ativando o ambiente virtual

#### Windows (Git Bash)
source venv/Scripts/activate

#### Linux / macOS
source venv/bin/activate

## Rodando os testes

Com o ambiente virtual ativo:

```bash
pytest
```

### Autenticação

As rotas protegidas exigem autenticação via Bearer Token.

Exemplo de header:

Authorization: Bearer SEU_TOKEN_FIXO

Ferramentas compatíveis:
- Postman
- Insomnia
- curl
- HTTP clients em geral

Obs: navegadores não permitem envio de headers customizados diretamente.

### Rotas protegidas

As seguintes rotas exigem autenticação:

- GET /people
- GET /planets
- GET /starships

## Exemplos de uso

```http
GET /films
GET /films?search=hope
GET /people?page=2
GET /people?order=name
```

## Deploy

A aplicação foi preparada para deploy serverless no Google Cloud Platform (GCP),
utilizando Cloud Functions e API Gateway.

O deploy será realizado utilizando Python 3.11 e arquitetura serverless.
