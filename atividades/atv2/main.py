from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Emprestimo
from typing import List

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
emprestimo: List[Emprestimo] = []

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
def atualizar(email: str, usuario: Usuario):
    for i, u in enumerate(usuarios):
        if u.email == email:
            # manter email original (não alteramos identificador aqui)
            usuarios[i] = Usuario(nome=usuario.nome, email=email, senha=usuario.senha)
            return usuarios[i]
    raise HTTPException(status_code=404, detail="Usuario não encontrado")


@app.delete("/usuario/{email}", status_code=204)
def deletar(email: str):
    for i, u in enumerate(usuarios):
        if u.email == email:
            usuarios.pop(i)
            return
    raise HTTPException(status_code=404, detail="Usuario não encontrado")


'''CRUD Livros'''
@app.get('/livro', response_model=List[Livro])
def listar_livros() -> List[Livro]:
    return livros


@app.post('/livro', response_model=Livro)
def adicionar_livro(livro: Livro) -> Livro:
    livros.append(livro)

    return livro

# rotas de put estao dando conflito com o field_validator

@app.delete('/livro/{isbn}')
def deletar_livro(isbn: str) -> dict:
    for livro in range(len(livros)):
        if livros[livro].isbn == isbn:
            if not livros[livro].emprestado:
                livros.pop(livro)
                Livro.__values__.remove(isbn)
                print(Livro.__values__)
                return {'msg': 'livro deletado'}
            else:
                return {'msg': 'livro está emprestado e não pode ser deletado.'}
    
    return {'msg': 'não existe livro com esse isbn'}

# descricao do erro: ao atualizar a lista com o novo objeto, ele conflita com o field_validator como se o isbn fosse um novo valor repetido. 
# talvez fazer as mudanças manualmente inves de mudar o objeto inteiro resolva, assim o isbn nao muda.
# muda os outros campos, mantem o isbn igual.

@app.put('/livro/{isbn}', response_model=List[Livro])
def editar_livro(livro_edit: Livro) -> List[Livro]:
    for livro in range(len(livros)):
        if livros[livro].isbn == livro_edit.isbn:
            livros[livro] = livro
            return livros
    
    return {'msg': 'não existe livro com esse isbn'}

'''Empréstimo'''