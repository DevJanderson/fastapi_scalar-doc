from fastapi import FastAPI, HTTPException
from typing import List
from models import Ciclista, CiclistaCreate
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title="Clube de Ciclistas API")

# Simulando um banco de dados
db_ciclistas = []
contador_id = 1

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Clube de Ciclistas API"}

@app.get("/scalar", include_in_schema=False)
async def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title + " - Scalar"
    )

@app.post("/ciclistas/", response_model=Ciclista)
def criar_ciclista(ciclista: CiclistaCreate):
    global contador_id
    novo_ciclista = Ciclista(
        id=contador_id,
        **ciclista.dict()
    )
    db_ciclistas.append(novo_ciclista)
    contador_id += 1
    return novo_ciclista

@app.get("/ciclistas/", response_model=List[Ciclista])
def listar_ciclistas():
    return db_ciclistas

@app.get("/ciclistas/{ciclista_id}", response_model=Ciclista)
def obter_ciclista(ciclista_id: int):
    ciclista = next((c for c in db_ciclistas if c.id == ciclista_id), None)
    if not ciclista:
        raise HTTPException(status_code=404, detail="Ciclista não encontrado")
    return ciclista

@app.put("/ciclistas/{ciclista_id}", response_model=Ciclista)
def atualizar_ciclista(ciclista_id: int, ciclista_atualizado: CiclistaCreate):
    for i, ciclista in enumerate(db_ciclistas):
        if ciclista.id == ciclista_id:
            db_ciclistas[i] = Ciclista(id=ciclista_id, **ciclista_atualizado.dict())
            return db_ciclistas[i]
    raise HTTPException(status_code=404, detail="Ciclista não encontrado")

@app.delete("/ciclistas/{ciclista_id}")
def deletar_ciclista(ciclista_id: int):
    for i, ciclista in enumerate(db_ciclistas):
        if ciclista.id == ciclista_id:
            del db_ciclistas[i]
            return {"message": "Ciclista removido com sucesso"}
    raise HTTPException(status_code=404, detail="Ciclista não encontrado")