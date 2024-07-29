import pytest 

from fastapi.testclient import TestClient
from app.main import app 
from pydantic import BaseModel

client = TestClient(app)


def test_ola_mundo_status_code():
    response =  client.get("/")
    assert response.status_code == 200 
    
def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"Olá":"Mundo"}
    

def test_listar_produtos_status_code():
    response =  client.get("/produtos")
    assert response.status_code == 200 
    

def test_tamanho_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 5     
    
def test_pega_produto():
    response = client.get("/produtos/3")
    assert response.json() == {
        "id": 3,
        "nome": "Mouse Sem Fio",
        "descricao": "Mouse com sensor de alta precisão e conexão sem fio.",
        "preco": 149.99
    }
    
