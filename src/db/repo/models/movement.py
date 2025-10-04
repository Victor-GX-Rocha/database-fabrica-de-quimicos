"""  """

from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass
from datetime import datetime, date
from sqlalchemy import Integer, String, ForeignKey, Enum, Numeric, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.connection import Base
from src.db.repo.models import MovementType, PackagingTypes, SpecificationTypes

if TYPE_CHECKING:
    from src.db.repo.models.registry import RegistryInputORM, RegistrySuplierORM, RegistryProductORM, RegistryEPIORM


@dataclass
class MovInputDTO:
    """
    DTO model to represents "movimentacao_insumos" table.
    
    Args:
        id (int): Movement ID.
        id_input (int): Input ID.
        id_supplier (int): Supplier ID.
        movement_type (MovementType):
        qtd_moved (int): Quatityy moved.
        packaging_type (PackagingTypes): Package type (box or fitage)
        input_value (float): Input price.
        specification_type (SpecificationTypes): Specification of input (powder, solid, liquid...)
        datetime_buy (datetime): Purchase date.
        datetime_arrival (datetime): Arrivale date.
    """
    id: int = None
    id_input: int = None
    id_suplier: int = None
    movement_type: MovementType = None
    qtd_moved: int = None
    packaging_type: PackagingTypes = None
    input_value: float = None
    specification_type: SpecificationTypes = None
    datetime_buy: datetime = None
    datetime_arrival: datetime = None

@dataclass
class MovProductDTO:
    """
    DTO model to represents "movimentacoes_produtos" table.
    Args:
        id (int): Movement ID.
        product_id (int): Product ID.
        movement_type (MovementType): Movement type.
        litrage (float): Total quantity in litres.
        packaging_types (PackagingTypes): Package type (box or fitage)
        stacking_maxim (int): Maximum empile of materials.
        surplus (float): Product surplus litres.
        validity (date): Validity.
        datetime_inbound (datetime): Input date.
        datetime_outbound (datetime): Output date.
    """
    id: int = None
    product_id: int = None
    movement_type: MovementType = None
    litrage: float = None
    packaging_types: PackagingTypes = None
    stacking_maxim: int = None
    surplus: float = None
    validity: date = None
    datetime_inbound: datetime = None
    datetime_outbound: datetime = None

@dataclass
class MovEPIDTO:
    """
    DTO model to represents "movimentacoes_epi" table.
    Args:
        id (int): Movement ID.
        id_epi (int): EPI ID.
        datetime_buy (datetime): Purchase date.
        datetime_delivery (datetime): Delivery date.
        datetime_return (datetime): Return date.
    """
    id: int = None
    id_epi: int = None
    datetime_buy: datetime = None
    datetime_delivery: datetime = None
    datetime_return: datetime = None

class MovInputORM(Base):
    """ ORM model to represents "movimentacoes_insumos" table. """
    
    __tablename__ = "movimentacoes_insumos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_insumo: Mapped[int] = mapped_column(Integer, ForeignKey("registro_insumos.id"), nullable=False)
    id_fornecedor: Mapped[int] = mapped_column(Integer, ForeignKey("registro_fornecedores.id"), nullable=False)
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False, index=True)
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, index=True)
    tipo_embalagem: Mapped[PackagingTypes] = mapped_column(Enum(PackagingTypes), nullable=False)
    valor_insumo: Mapped[float] = mapped_column(Numeric(10, 2))
    especificacao_tipo: Mapped[SpecificationTypes] = mapped_column(Enum(SpecificationTypes))
    data_hora_compra: Mapped[datetime] = mapped_column(DateTime)
    data_hora_chegada: Mapped[datetime] = mapped_column(DateTime)
    
    registro_insumo: Mapped["RegistryInputORM"] = relationship(
        "RegistryInputORM",
        back_populates="movimentacoes_insumos",
        lazy="joined"
    )
    
    registro_fornecedor: Mapped["RegistrySuplierORM"] = relationship(
        "RegistrySuplierORM",
        back_populates="movimentacoes_insumos",
        lazy="joined"
    )
    
    def to_dto(self) -> MovInputDTO:
        return MovInputDTO(
            id=self.id,
            id_input=self.id_insumo,
            id_suplier=self.id_fornecedor,
            movement_type=self.tipo_movimentacao,
            qtd_moved=self.quantidade_movimentada,
            packaging_type=self.tipo_embalagem,
            input_value=self.valor_insumo,
            specification_type=self.especificacao_tipo,
            datetime_buy=self.data_hora_compra,
            datetime_arrival=self.data_hora_chegada,
        )

class MovProductORM(Base):
    """ ORM model to represents "movimentacao_produto" table. """
    
    __tablename__ = "movimentacoes_produtos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_produto: Mapped[int] = mapped_column(Integer, ForeignKey("registro_produtos.id"))
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False)
    litragem: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, index=True) 
    tipo_embalagem: Mapped[PackagingTypes] = mapped_column(Enum(PackagingTypes), nullable=False)
    empilhagem_maxima: Mapped[int] = mapped_column(Integer, nullable=False)
    sobra: Mapped[float] = mapped_column(Numeric(10, 2))
    validade: Mapped[date] = mapped_column(Date)
    data_hora_entrada: Mapped[datetime] = mapped_column(DateTime)
    data_hora_saida: Mapped[datetime] = mapped_column(DateTime)
    
    registro_produto: Mapped["RegistryProductORM"] = relationship(
        "RegistryProductORM",
        back_populates="movimentacoes_produto",
        lazy="joined"
    )
    
    def to_dto(self) -> MovProductDTO:
        return MovProductDTO(
            id=self.id,
            product_id=self.id_produto,
            movement_type=self.tipo_movimentacao,
            litrage=self.litragem,
            packaging_types=self.tipo_embalagem,
            stacking_maxim=self.empilhagem_maxima,
            surplus=self.sobra,
            validity=self.validade,
            datetime_inbound=self.data_hora_entrada,
            datetime_outbound=self.data_hora_saida
        )

class MovEPIORM(Base):
    """ ORM model to represents "movimentacoes_epi" table. """
    
    __tablename__ = "movimentacoes_epi"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_epi: Mapped[int] = mapped_column(Integer, ForeignKey("registro_epi.id"))
    data_hora_compra: Mapped[datetime] = mapped_column(DateTime)
    data_hora_entrega: Mapped[datetime] = mapped_column(DateTime)
    data_hora_devolucao: Mapped[datetime] = mapped_column(DateTime)
    
    registro_epi: Mapped["RegistryEPIORM"] = relationship(
        "RegistryEPIORM",
        back_populates="movimentacoes_epi",
        lazy="joined"
    )
    
    def to_dto(self) -> MovEPIDTO:
        return MovEPIDTO(
            id=self.id,
            id_epi=self.id_epi,
            datetime_buy=self.data_hora_compra,
            datetime_delivery=self.data_hora_entrega,
            datetime_return=self.data_hora_devolucao
        )


__all__ = [
    "MovInputDTO", "MovProductDTO", "MovEPIDTO",
    "MovInputORM", "MovProductORM", "MovEPIORM"
]
