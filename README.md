# API de Gerenciamento de Ciclistas

Uma API RESTful desenvolvida com FastAPI para gerenciar cadastros de ciclistas.

## Tecnologias Utilizadas

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL

## Configuração do Ambiente

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Scalar FastAPI

O `scalar_fastapi` é uma extensão para o FastAPI que permite a definição de scalars personalizados para validação e serialização de dados.

### Instalação

Para instalar o `scalar_fastapi`, adicione-o ao seu arquivo `requirements.txt` ou instale-o diretamente usando pip:

```bash
pip install scalar #testar se esse comando é necessário
pip install scalar-fastapi
```

## Modelos de Dados

### Ciclista

- `id`: Int (Identificador único)
- `nome`: String
- `email`: String
- `data_nascimento`: Date
- `nivel_experiencia`: String
- `tipo_bicicleta`: String
- `ativo`: Boolean

## Endpoints da API

### GET /ciclistas/
- Retorna lista de todos os ciclistas cadastrados

### GET /ciclistas/{id}
- Retorna detalhes de um ciclista específico

### POST /ciclistas/
- Cria um novo cadastro de ciclista

### PUT /ciclistas/{id}
- Atualiza dados de um ciclista existente

### DELETE /ciclistas/{id}
- Desativa um cadastro de ciclista

## Como Executar

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

Documentação scalar-fastapi UI: `http://localhost:8000/scalar`