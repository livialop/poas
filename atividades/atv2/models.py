from pydantic import BaseModel, EmailStr, Field, field_validator

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    __values__: set = set()

    @field_validator('email')
    @classmethod
    def validate_unique_email(cls, value):
        if value in cls.__values__:
            raise ValueError("Não pode email repetido.")
        cls.__values__.add(value)
        return value


class Livro(BaseModel):
    titulo: str
    isbn: str
    preco: float
    autor: str
    editora: str
    emprestado: bool = Field(default=False)  # Se estiver emprestado, validar com True
    __values__: set = set()

    @field_validator('isbn')
    @classmethod
    def validate_unique_isbn(cls, value):
        if value in cls.__values__:
            raise ValueError("Não pode ISBN repetido.")
        cls.__values__.add(value)
        return value
    
    @field_validator('preco')
    def validate_preco(cls, value):
        if value <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        return value

class Emprestimo(BaseModel):
    isbn: str
    usuario: EmailStr