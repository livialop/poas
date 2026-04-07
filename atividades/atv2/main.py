from fastapi import FastAPI
from models import Usuario, Livro, Emprestimo
from typing import List

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
emprestimo: List[Emprestimo] = []

'''CRUD Usuários'''

'''CRUD Livros'''
@app.get('/livro', response_model=List[Livro])
def listar_livros() -> List[Livro]:
    return livros


@app.post('/livro', response_model=Livro)
def adicionar_livro(livro: Livro) -> Livro:
    livros.append(livro)

    return livro


@app.delete('/livro/{isbn}')
def deletar_livro(isbn: str):
    for livro in range(len(livros)):
        if livros[livro].isbn == isbn:
            if not livros[livro].emprestado:
                livros.pop(livro)
            else:
                return {'msg': 'livro está emprestado e não pode ser deletado.'}
    
    return {'msg': 'não existe livro com esse isbn'}


@app.put('/livro/{isbn}', response_model=List[Livro])
def editar_livro(isbn: str):
    for livro in range(len(livros)):
        if livros[livro].isbn == isbn:
            livros[livro] = livro
            return livros
    
    return {'msg': 'não existe livro com esse isbn'}

'''Empréstimo'''