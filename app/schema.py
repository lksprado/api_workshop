import sys 
import os 
# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    id: int 
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat  