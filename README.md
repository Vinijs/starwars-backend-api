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

## 🚀 Status de Implantação (Google Cloud Platform)

Este projeto foi desenvolvido para ser executado como uma **Google Cloud Function (2ª Geração)** integrada ao **API Gateway**.

### Relatório de Infraestrutura e Obstáculos
O código-fonte está 100% operacional e preparado para o ambiente de produção. Durante a fase de deploy, foi identificado um impedimento externo relacionado às políticas de faturamento (Billing) da plataforma Google Cloud para contas individuais no Brasil:

* **Diagnóstico:** O projeto está configurado e vinculado ao SDK (`gcloud`), mas a ativação das APIs necessárias (`Cloud Functions`, `Cloud Build`, `Artifact Registry`) requer uma conta de faturamento ativa.
* **Impedimento Técnico:** As políticas atuais do GCP para perfis CPF exigem um aporte inicial pré-pago (via Pix) ou validação de cartão internacional. Devido a instabilidades na comunicação entre o gateway de pagamento do Google e a operadora do cartão (Erro `OR_MIVEM_02`), o provisionamento dos recursos de nuvem foi interrompido.
* **Solução Local:** Para garantir a avaliação da lógica e funcionalidade, o projeto pode ser executado localmente via Docker ou ambiente virtual Python (ver instruções abaixo). O código está pronto para deploy imediato assim que um ambiente com Billing ativo for fornecido.

---

## 🛠️ Como executar localmente

Caso deseje validar a API sem o ambiente GCP, siga os passos:

1. **Clonar o repositório:**
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd starwars-backend-api
   ```
