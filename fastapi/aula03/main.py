# uvicorn main:app --reload
# pip install email-validator

from fastapi import FastAPI
from models import Aluno
from typing import List

app = FastAPI()

# O tipo List define uma lista tipada, ele só aceita objetos que sejam do tipo Aluno.
# Se fosse um vetor normal, ele poderia adicionar objetos de qualquer tipo.
alunos: List[Aluno] = []

@app.post('/aluno', response_model=Aluno) # O response_model diz que a rota vai retornar um JSON com informação do aluno cadastrado.
def cadastrar(aluno: Aluno) -> Aluno:
    matricula = str(len(alunos)+1)
    aluno.matricula = matricula
    alunos.append(aluno)

    return aluno

@app.get('/aluno', response_model=List[Aluno])
def listar() -> List[Aluno]:
    return alunos

@app.put('/aluno/{matricula}', response_model=List[Aluno])
def editar(aluno_edit: Aluno) -> List[Aluno]:
    # percorre a lista de alunos usando o indice
    for aluno in range(len(alunos)):
        # checa se a matricula de determinada pos na lista eh igual a matricula fornecida
        if alunos[aluno].matricula == aluno_edit.matricula:
            # substitui o antigo aluno do indice pelo novo aluno
            alunos[aluno] = aluno_edit
            return alunos
    
    return {'msg': 'matricula não existente'}

@app.delete('/aluno/{matricula}')
def deletar(matricula: str):
    # mesma lógica do edit, mas fornece apenas a matrícula e deleta
    for aluno in range(len(alunos)):
       if alunos[aluno].matricula == matricula:
            alunos.pop(aluno)
            return {'msg': 'aluno deletado'}
    
    return {'msg': 'não existe aluno com essa matrícula'}
