''' Faça uma API para uma calculadora com as seguintes rotas e retornos:
- rota: /soma : recebe dois inteiros A e B e retorna o resultado

- rota: /subtracao : recebe dois inteiros A e B e retorna o resultado

- rota: /divisao : recebe dois inteiros A e B e retorna o resultado

- rota: /multiplicacao : recebe dois inteiros A e B e retorna o resultado

- rota: /raiz : recebe um inteiro e retorna o resultado da raiz quadrada '''

from fastapi import FastAPI

app = FastAPI()

@app.get('/soma')
def soma(a: int, b: int):
    return {'resultado': (a+b)}

@app.get('/divisao')
def divisao(a: int, b: int):
    return {'resultado': (a/b)}

@app.get('/multiplicacao')
def multplicacao(a: int, b: int):
    return {'resultado': (a*b)}

@app.get('/raiz')
def raiz(a: int):
    return {'resultado': (a**2)}