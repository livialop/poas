# pip install fastapi uvicorn
# uvicorn main:app -- reload
# 127.0.0.1:8000/docs -> para ver a doc. do swagger

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"messagem": "Olá mundo!"}

@app.get("/nome")
def nome(nome: str):
    return {"nome": nome}