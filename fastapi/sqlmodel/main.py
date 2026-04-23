from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends
from model import Tarefa
from database import create_db, get_session
from contextlib import asynccontextmanager

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/tarefas')
def listar(session: SessionDep) -> list[Tarefa]:
    tarefas = session.exec(select(Tarefa)).all()
    return tarefas