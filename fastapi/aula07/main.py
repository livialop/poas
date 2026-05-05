#main.py
from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends
from model import Tarefa
from database import create_db, get_session
from contextlib import asynccontextmanager

SessionDep = Annotated[Session,Depends(get_session)]

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/tarefas')
def listar(session:SessionDep)->list[Tarefa]:
    tarefas = session.exec(select(Tarefa)).all()
    return tarefas

@app.post('/tarefas')
def cadastrar(session:SessionDep, tarefa:Tarefa) -> Tarefa:
    session.add(tarefa)
    session.commit()
    session.refresh(tarefa)
    return tarefa

@app.delete('/tarefas/{id}')
def excluir(session:SessionDep, id:int):
    tarefa = session.get(Tarefa, id)
    session.delete(tarefa)
    session.commit()
    
@app.put('tarefas/{id}')
def editar(session:SessionDep, id:int, tarefa:Tarefa) -> Tarefa:
    tarefaUpdate = session.grt(Tarefa, id)
    tarefaUpdate.descricao = tarefa.descricao
    tarefaUpdate.nome = tarefa.nome
    tarefaUpdate.status = tarefa.status
    session.add(tarefaUpdate)
    session.commit()
    session.refresh(tarefaUpdate)
    return tarefaUpdate
    
       