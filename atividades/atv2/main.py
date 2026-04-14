from fastapi import FastAPI, HTTPException, Body, status
from models import Usuario, Livro, Emprestimo
from typing import List
from datetime import date

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
emprestimos: List[Emprestimo] = []

'''CRUD Usuários'''
@app.post("/usuario", response_model=Usuario, status_code=201)
def cadastrar(usuario: Usuario):
    # verifica se email já existe
    for u in usuarios:
        if u.email == usuario.email:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
    usuarios.append(usuario)
    return usuario


@app.get("/usuario", response_model=List[Usuario])
def listar():
    return usuarios


@app.put("/usuario/{email}", response_model=Usuario)
def atualizar(email: str, senha: str, nome: str = Body(...)):
    for usuario in usuarios:
        if usuario.email == email:
            # botei que pra fazer a alteracao do nome do usuario precisa validar  c senha
            if usuario.senha != senha:
                raise HTTPException(status_code=404, detail="senha errada")
            usuario.nome = nome
            return usuario

    raise HTTPException(status_code=404, detail='usuario nao encontrado')

@app.delete("/usuario/{email}", status_code=204)
def deletar(email: str):
    for i, u in enumerate(usuarios):
        if u.email == email:
            usuarios.pop(i)
            return
    raise HTTPException(status_code=404, detail="Usuario não encontrado")


'''CRUD Livros'''

# Só retorna livros não emprestados
@app.get('/livro', response_model=List[Livro])
def listar_livros() -> List[Livro]:
    livros_em_dia: List[Livro] = []
    for livro in livros:
        if not livro.emprestado:
            livros_em_dia.append(livro)
    
    return livros_em_dia


@app.post('/livro', response_model=Livro)
def adicionar_livro(livro: Livro) -> Livro:
    livros.append(livro)

    return livro

@app.delete('/livro/{isbn}')
def deletar_livro(isbn: str) -> dict:
    for livro in range(len(livros)):
        if livros[livro].isbn == isbn:
            if not livros[livro].emprestado:
                livros.pop(livro)
                Livro.__values__.discard(isbn) #usei o discard para não ter chance de erro usando o remove/del
                # print(Livro.__values__)
                return {'msg': 'livro deletado'}
            else:
                return {'msg': 'livro está emprestado e não pode ser deletado.'}
    
    return {'msg': 'não existe livro com esse isbn'}


@app.put('/livro/{isbn}', response_model=Livro)
def editar_livro(isbn: str, titulo: str = Body(...), preco: float = Body(...), autor: str = Body(...), editora: str = Body(...)) -> Livro:
    if preco <= 0:
        return {'msg': 'preço deve ser maior que zero.'}
    
    for livro in livros:
        if livro.isbn == isbn:
            livro.titulo = titulo
            livro.preco = preco
            livro.autor = autor
            livro.editora = editora
            return livro

    return {'msg': 'não existe livro com esse isbn'}


'''Empréstimo'''

@app.get('/emprestimos/atrasados', response_model=List[Emprestimo])
def listar_emprestimos_atrasados() -> List[Emprestimo]:
    hoje = date.today()
    emprestimos_atrasados: List[Emprestimo] = []
    for emprestimo in emprestimos:
        if emprestimo.prazo < hoje:
            emprestimos_atrasados.append(emprestimo)
    return emprestimos_atrasados


@app.post('/emprestimo', response_model=Emprestimo)
def criar_emprestimo(emprestimo: Emprestimo):
    # livro existe e nao ta emprestado
    for livro in livros:
        if livro.isbn == emprestimo.isbn:
            if livro.emprestado:
                raise HTTPException(status_code=400, detail='livro ja esta em emprestimo')
            # empresta o livro
            livro.emprestado = True
            emprestimos.append(emprestimo)
            return emprestimo
    raise HTTPException(status_code=404, detail='Livro não encontrado.')

# contando como apagar um emprestimo fosse a devolucao dele
@app.delete('/emprestimo/{isbn}')
def apagar_emprestimo(isbn: str, email_usuario: str):
    for emprestimo in emprestimos:

        if emprestimo.isbn == isbn and emprestimo.usuario == email_usuario:
        
            for livro in livros:
                if livro.isbn == isbn:
                    livro.emprestado = False
                    break
        
            emprestimos.remove(emprestimo)
            return 
    raise HTTPException(status_code=404, detail='emprestimo nao encontrado')