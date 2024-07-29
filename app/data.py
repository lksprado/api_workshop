from typing import List, Dict

class Produtos:
    produtos: List[Dict[str, any]] = [
            {
            "id": 1,
            "nome": "Cadeira Gamer",
            "descricao": "Cadeira ergonômica com apoio para os braços e ajuste de altura.",
            "preco": 499.99,
            "disponivel": True
        },
        {
            "id": 2,
            "nome": "Teclado Mecânico",
            "descricao": "Teclado com switches mecânicos e retroiluminação RGB.",
            "preco": 299.99,
            "disponivel": True
        },
        {
            "id": 3,
            "nome": "Mouse Sem Fio",
            "descricao": "Mouse com sensor de alta precisão e conexão sem fio.",
            "preco": 149.99,
            "disponivel": False
        },
        {
            "id": 4,
            "nome": "Monitor 4K",
            "descricao": "Monitor com resolução 4K e 27 polegadas.",
            "preco": 1199.99,
            "disponivel": True
        },
        {
            "id": 5,
            "nome": "Fone de Ouvido",
            "descricao": "Fone de ouvido com cancelamento de ruído e áudio de alta fidelidade.",
            "preco": 399.99,
            "disponivel": True
        }
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self,id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto 
        return {"Status":404, "Mensagem": "Produto não encontrato"}
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto