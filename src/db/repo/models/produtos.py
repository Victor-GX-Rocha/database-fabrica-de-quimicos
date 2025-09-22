""" Models for tables about a product. """

from typing import Optional
from datetime import datetime
from sqlalchemy import String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dataclasses import dataclass

from src.db.connection import Base
from .base import MovementType


@dataclass
class ProdutoDTO:
    """
    Dataclass to stores the "produtos" table data.
    Args:
        name (str): 
        current_quantity (int): 
        category (str): 
        tags (str): 
    """
    name: str
    current_quantity: int
    category: Optional[str] = None
    tags: Optional[str] = None

@dataclass
class ProdutoMovDTO:
    """
    Dataclass to stores the "produtos_movimentacoes" table data.
    Args:
        product_id (int): 
        movement_type (MovementType): 
        qtd_moved (int): 
        datatime (datetime): 
    """
    product_id: int
    movement_type: MovementType
    qtd_moved: int
    datatime: datetime


@dataclass
class ProdutoORM(Base):
    """ ORM table produtos. """
    __tablename__ = "produtos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)
    # sku: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    quantidade_atual: Mapped[int] = mapped_column(Integer, default=0)
    categoria: Mapped[Optional[str]] = mapped_column(String(64))
    lote_id: Mapped[str] = mapped_column(String(256), nullable=False)
    tags: Mapped[Optional[str]] = mapped_column(String(256))
    
    movimentacoes: Mapped[list["ProdutoMovORM"]] = relationship(
        "ProdutoMovORM",
        back_populates="produto",
        lazy="selectin"
    )
    
    def to_dto(self) -> ProdutoDTO:
        """ Converts the orm produto model to a dataclass and stores the information. """
        return ProdutoDTO(
            name=self.nome,
            current_quantity=self.quantidade_atual,
            category=self.categoria,
            tags=self.tags,
        )

@dataclass
class ProdutoMovORM(Base):
    """ Register for produtos movimentations. """
    __tablename__ = "produtos_movimentacoes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    produto_id: Mapped[str] = mapped_column(Integer, ForeignKey("produtos.id"))
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False)
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    data_hora: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    produto: Mapped["ProdutoORM"] = relationship(
        "ProdutoORM",
        back_populates="movimentacoes",
        lazy="joined" # Calls the product with the query.
    )
    
    def to_dto(self) -> ProdutoMovDTO:
        return ProdutoMovDTO(
            product_id=self.produto_id,
            movement_type=self.tipo_movimentacao,
            qtd_moved=self.quantidade_movimentada,
            datatime=self.data_hora,
        )

__all__ = [
    "ProdutoDTO", "ProdutoMovDTO",
    "ProdutoORM", "ProdutoMovORM"
]
