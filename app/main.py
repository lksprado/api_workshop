import sys 
import os 
# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI
from app.schema import ProdutosSchema
from app.data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/")
def ola_mundo(): # Response
    return {"Olá":"Mundo"}

@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()


@app.get("/produtos/{id}", response_model=ProdutosSchema)
def buscar_produto(id: int):
    return lista_de_produtos.buscar_produto(id)
    
@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produtos(produto:ProdutosSchema):
    return lista_de_produtos.adicionar_produtos(produto.model_dump())