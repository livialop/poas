# models.py

from pydantic import BaseModel, EmailStr

class Aluno(BaseModel):
    matricula: str 
    nome: str
    curso: str
    email: EmailStr # O EmailStr é uma classe que valida se o email está no formato válido.
    