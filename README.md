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

