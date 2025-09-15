from sqlalchemy import Text, String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from src.db.connection import Base

import enum

class MovementType(enum.Enum):
    INBOUND = "entrada"
    OUTBOUND = "saida"

@dataclass
class ProdutoDTO:
    name: str
    current_quantity: int
    category: Optional[str] = None
    tags: Optional[str] = None

@dataclass
class ProdutoMovDTO:
    produto_id: int
    tipo_movimentacao: MovementType
    quantidade_movimentada: int
    data_hora: datetime

class ProdutoORM(Base):
    __tablename__ = "produtos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)
    quantidade_atual: Mapped[int] = mapped_column(Integer, default=0)
    categoria: Mapped[Optional[str]] = mapped_column(String(64))
    tags: Mapped[Optional[str]] = mapped_column(String(256))
    
    # Relacionamento com movimentações
    movimentacoes: Mapped[List["ProdutoMovORMORM"]] = relationship(
        "ProdutoMovORMORM", 
        back_populates="produto",
        lazy="select"  # ou "joined", "subquery", etc.
    )
    
    def to_dto(self) -> ProdutoDTO:
        return ProdutoDTO(
            name=self.nome,
            current_quantity=self.quantidade_atual,
            category=self.categoria,
            tags=self.tags,
        )

class ProdutoMovORMORM(Base):
    __tablename__ = "produtos_movimentacoes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    produto_id: Mapped[int] = mapped_column(Integer, ForeignKey("produtos.id"))
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False)
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    data_hora: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    # Relacionamento com produto
    produto: Mapped["ProdutoORM"] = relationship(
        "ProdutoORM", 
        back_populates="movimentacoes",
        lazy="joined"  # Carrega o produto junto na consulta
    )
    
    def to_dto(self) -> ProdutoMovDTO:
        return ProdutoMovDTO(
            produto_id=self.produto_id,
            tipo_movimentacao=self.tipo_movimentacao,
            quantidade_movimentada=self.quantidade_movimentada,
            data_hora=self.data_hora,
        )