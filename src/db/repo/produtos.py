""" Repository for "prouto" tables. """

from src.db.connection import session_scope
from .models import ProdutoORM, ProdutoDTO
from src.db.repo.models.produtos import ProdutoMovORM, ProdutoDTO

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


class ProdutoMovRepository:
    """ Repository for table produtos. """
    
    def add_new_mov(self, mov: ProdutoDTO) -> None:
        with session_scope() as session:
            session.add(ProdutoMovORM(
                produto_id = mov.product_id,
                tipo_movimentacao = mov.movement_type,
                quantidade_movimentada = mov.qtd_moved
            ))


__all__ = [
    "ProdutoRepository"
]
