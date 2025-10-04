""" Repository for movement tables. """

from typing import Protocol, Iterable, TypeVar

from src.db.connection import session_scope
from .models.movement import (
    MovInputDTO, MovProductDTO, MovEPIDTO,
    MovInputORM, MovProductORM, MovEPIORM
)

MovDTO = TypeVar("MovDTO")

class MovRepositoryProtocol(Protocol):
    """ Protocol for movement repositories.  """
    
    def create(self, dto: MovDTO) -> None:
        """ Creates a sigle register. """
    
    def bulk_create(self, dtos: Iterable[MovDTO]) -> None:
        """ Creates multiple registers. """

class MovInputRepository(MovRepositoryProtocol):
    """ Repository for movimentacao_insumos table. """
    def create(self, dto: MovInputDTO) -> None:
        """ Creates a register for movimentacao_insumos table. """
        with session_scope() as session:
            session.add(MovInputORM(
                id=dto.id,
                id_insumo=dto.id_input,
                id_fornecedor=dto.id_suplier,
                tipo_movimentacao=dto.movement_type,
                quantidade_movimentada=dto.qtd_moved,
                tipo_embalagem=dto.packaging_type,
                valor_insumo=dto.input_value,
                especificacao_tipo=dto.specification_type,
                data_hora_compra=dto.datetime_buy,
                data_hora_chegada=dto.datetime_arrival
            ))
    
    def bulk_create(self, dtos: Iterable[MovInputDTO]) -> None:
        """ Creates multiples registers for movimentacao_insumos table. """
        with session_scope() as session:
            session.add_all([MovInputORM(
                id=dto.id,
                id_insumo=dto.id_input,
                id_fornecedor=dto.id_suplier,
                tipo_movimentacao=dto.movement_type,
                quantidade_movimentada=dto.qtd_moved,
                tipo_embalagem=dto.packaging_type,
                valor_insumo=dto.input_value,
                especificacao_tipo=dto.specification_type,
                data_hora_compra=dto.datetime_buy,
                data_hora_chegada=dto.datetime_arrival
            ) for dto in dtos])

class MovProductRepository(MovRepositoryProtocol):
    """ Repository for movimentacao_produto table. """
    def create(self, dto: MovProductDTO) -> None:
        """ Creates a register for movimentacao_produto table. """
        with session_scope() as session:
            session.add(MovProductORM(
                id=dto.id,
                id_produto=dto.product_id,
                tipo_movimentacao=dto.movement_type,
                litragem=dto.litrage,
                tipo_embalagem=dto.packaging_types,
                empilhagem_maxima=dto.stacking_maxim,
                sobra=dto.surplus,
                validade=dto.validity,
                data_hora_entrada=dto.datetime_inbound,
                data_hora_saida=dto.datetime_outbound
            ))
    
    def bulk_create(self, dtos: Iterable[MovProductDTO]) -> None:
        """ Creates multiples registers for movimentacao_produto table. """
        with session_scope() as session:
            session.add_all([MovProductORM(
                id=dto.id,
                id_produto=dto.product_id,
                tipo_movimentacao=dto.movement_type,
                litragem=dto.litrage,
                tipo_embalagem=dto.packaging_types,
                empilhagem_maxima=dto.stacking_maxim,
                sobra=dto.surplus,
                validade=dto.validity,
                data_hora_entrada=dto.datetime_inbound,
                data_hora_saida=dto.datetime_outbound
            ) for dto in dtos])

class MovEPIRepository(MovRepositoryProtocol):
    """ Repository for movimentacoes_epi table. """
    def create(self, dto: MovEPIDTO) -> None:
        """ Creates a register for movimentacoes_epi table. """
        with session_scope() as session:
            session.add(MovEPIORM(
                id=dto.id,
                id_epi=dto.id_epi,
                data_hora_compra=dto.datetime_buy,
                data_hora_entrega=dto.datetime_delivery,
                data_hora_devolucao=dto.datetime_return
            ))
    
    def bulk_create(self, dtos: Iterable[MovEPIDTO]) -> None:
        """ Creates multiples registers for movimentacoes_epi table. """
        with session_scope() as session:
            session.add_all([MovEPIORM(
                id=dto.id,
                id_epi=dto.id_epi,
                data_hora_compra=dto.datetime_buy,
                data_hora_entrega=dto.datetime_delivery,
                data_hora_devolucao=dto.datetime_return
            ) for dto in dtos])

__all__ = [
    "MovInputRepository",
    "MovProductRepository",
    "MovEPIRepository"
]
