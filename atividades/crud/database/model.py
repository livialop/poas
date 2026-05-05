from sqlmodel import SQLModel, Field, Relationship
import datetime
from decimal import Decimal
from typing import Optional


# Tabelas de conexão

class UsuarioPapeis(SQLModel, table=True):
    __tablename__ = "usuario_papeis"

    usuario_id: int | None = Field(
        default=None, 
        foreign_key="usuarios.id", 
        primary_key=True
    )
    papel_id: int | None = Field(
        default=None, 
        foreign_key="papeis.id", 
        primary_key=True
    )


class ProdutoCategorias(SQLModel, table=True):
    __tablename__ = "produto_categorias"

    produto_id: int | None = Field(
        default=None,
        foreign_key="produtos.id",
        primary_key=True
    )
    categoria_id: int | None = Field(
        default=None,
        foreign_key="categorias.id",
        primary_key=True
    )



# Tabelas de usuários e papeis

class Usuarios(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)
    email: str = Field(unique=True, max_length=120, index=True)
    senha_hash: str = Field(max_length=255)
    criado_em: datetime.datetime = Field(default=datetime.datetime.now(datetime.timezone.utc))

    papeis: list[Papeis] = Relationship(
        back_populates="usuarios",
        link_model=UsuarioPapeis
    )

class Papeis(SQLModel, table=True):
    __tablename__ = "papeis"
    
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(unique=True, max_length=50)

    usuarios: list[Usuarios] = Relationship(
        back_populates="papeis",
        link_model=UsuarioPapeis
    )


# Tabelas de produtos e categoria

class Produtos(SQLModel, table=True):
    __tablename__ = "produtos"
    
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=150)
    descricao: str | None
    preco: Decimal = Field(max_digits=10, decimal_places=2) # mesma coisa que DECIMAL(10,2)
    criado_em: datetime = Field(default=datetime.datetime.now(datetime.timezone.utc))

class Categorias(SQLModel, table=True):
    __tablename__ = "categorias"

    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)




# =========================
# TABELAS
# =========================

'''
CREATE TABLE usuarios ( =================================== FEITO
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    senha_hash VARCHAR(255),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE papeis ( =================================== FEITO
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) UNIQUE
);

CREATE TABLE usuario_papeis ( =================================== FEITO
    usuario_id INT,
    papel_id INT,
    PRIMARY KEY (usuario_id, papel_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (papel_id) REFERENCES papeis(id)
);

CREATE TABLE produtos ( =================================== FEITO
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150),
    descricao TEXT,
    preco DECIMAL(10,2),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categorias ( =================================== FEITO
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE produto_categorias ( =================================== FEITO
    produto_id INT,
    categoria_id INT,
    PRIMARY KEY (produto_id, categoria_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    total DECIMAL(10,2),
    status VARCHAR(50),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE itens_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    preco DECIMAL(10,2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    valor DECIMAL(10,2),
    metodo VARCHAR(50),
    status VARCHAR(50),
    pago_em TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

CREATE TABLE enderecos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    rua VARCHAR(150),
    cidade VARCHAR(100),
    estado VARCHAR(100),
    cep VARCHAR(20),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    produto_id INT,
    nota INT,
    comentario TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE TABLE estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT UNIQUE,
    quantidade INT,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
'''