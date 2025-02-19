from pydantic import BaseModel
from datetime import date
from typing import Optional

class CiclistaBase(BaseModel):
    nome: str
    email: str
    data_nascimento: date
    nivel_experiencia: str
    tipo_bicicleta: str

class CiclistaCreate(CiclistaBase):
    pass

class Ciclista(CiclistaBase):
    id: int
    ativo: bool = True

    class Config:
        from_attributes = True
