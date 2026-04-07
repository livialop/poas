from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class Livro(BaseModel):
    titulo: str
    isbn: str
    preco: float
    autor: str
    editora: str
    emprestado: bool # Se estiver emprestado, validar com True

class Emprestimo(BaseModel):
    isbn: str
    usuario: EmailStr