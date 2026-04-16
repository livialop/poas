from pydantic import BaseModel

class CPFRequest(BaseModel):
    cpf: str