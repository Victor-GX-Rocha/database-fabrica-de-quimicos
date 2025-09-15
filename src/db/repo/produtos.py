""" Repository for "prouto" tables. """

from src.db.connection import session_scope
from .models import ProdutoORM, ProdutoDTO

class ProdutoRepository:
    """ Repository for table produtos. """
    
    def register_new_product(self, product: ProdutoDTO) -> None:
        with session_scope() as session:
            session.add(ProdutoORM(
                nome=product.name,
                quantidade_atual=product.current_quantity,
                categoria=product.category,
                tags=product.tags
            ))
    
    def register_many_new_product(self, products: list[ProdutoDTO]) -> None:
        with session_scope() as session:
            session.add_all([ProdutoORM(
                nome=product.name,
                quantidade_atual=product.current_quantity,
                categoria=product.category,
                tags=product.tags
            ) for product in products])

__all__ = [
    "ProdutoRepository"
]
