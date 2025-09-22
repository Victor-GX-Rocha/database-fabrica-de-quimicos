""" Models for tables about insumos (raw materials). """

from typing import Optional
from datetime import datetime
from sqlalchemy import String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dataclasses import dataclass

from src.db.connection import Base
from .base import MovementType


# ---------------- DTOs ----------------
@dataclass
class InsumoDTO:
    nome: str
    unidade_medida: str
    quantidade_atual: int


@dataclass
class InsumoMovDTO:
    insumo_id: int
    tipo_movimentacao: MovementType
    quantidade_movimentada: int
    data_hora: datetime


# ---------------- ORM ----------------
@dataclass
class InsumoORM(Base):
    __tablename__ = "insumos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(128), nullable=False, unique=True, index=True)
    unidade_medida: Mapped[str] = mapped_column(String(32), nullable=False)
    quantidade_atual: Mapped[int] = mapped_column(Integer, default=0)

    movimentacoes: Mapped[list["InsumoMovORM"]] = relationship(
        "InsumoMovORM", back_populates="insumo", lazy="selectin"
    )

    def to_dto(self) -> InsumoDTO:
        return InsumoDTO(
            nome=self.nome,
            unidade_medida=self.unidade_medida,
            quantidade_atual=self.quantidade_atual,
        )


@dataclass
class InsumoMovORM(Base):
    __tablename__ = "mov_insumos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    insumo_id: Mapped[int] = mapped_column(Integer, ForeignKey("insumos.id"))
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False)
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    insumo: Mapped["InsumoORM"] = relationship(
        "InsumoORM", back_populates="movimentacoes", lazy="joined"
    )

    def to_dto(self) -> InsumoMovDTO:
        return InsumoMovDTO(
            insumo_id=self.insumo_id,
            tipo_movimentacao=self.tipo_movimentacao,
            quantidade_movimentada=self.quantidade_movimentada,
            data_hora=self.data_hora,
        )
