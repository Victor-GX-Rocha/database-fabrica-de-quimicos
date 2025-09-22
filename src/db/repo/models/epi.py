""" Models for tables about EPIs (safety equipment). """

from typing import Optional
from datetime import datetime
from sqlalchemy import String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dataclasses import dataclass

from src.db.connection import Base
from .base import MovementType


# ---------------- DTOs ----------------
@dataclass
class EpiDTO:
    nome: str
    quantidade: int
    categoria: Optional[str]
    validade: Optional[datetime]


@dataclass
class EpiMovDTO:
    epi_id: int
    tipo_movimentacao: MovementType
    quantidade_movimentada: int
    data_hora: datetime


# ---------------- ORM ----------------
@dataclass
class EpiORM(Base):
    __tablename__ = "epis"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(128), nullable=False, unique=True, index=True)
    quantidade: Mapped[int] = mapped_column(Integer, default=0)
    categoria: Mapped[Optional[str]] = mapped_column(String(64))
    validade: Mapped[Optional[datetime]] = mapped_column(DateTime)

    movimentacoes: Mapped[list["EpiMovORM"]] = relationship(
        "EpiMovORM", back_populates="epi", lazy="selectin"
    )

    def to_dto(self) -> EpiDTO:
        return EpiDTO(
            nome=self.nome,
            quantidade=self.quantidade,
            categoria=self.categoria,
            validade=self.validade,
        )


@dataclass
class EpiMovORM(Base):
    __tablename__ = "mov_epis"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    epi_id: Mapped[int] = mapped_column(Integer, ForeignKey("epis.id"))
    tipo_movimentacao: Mapped[MovementType] = mapped_column(Enum(MovementType), nullable=False)
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    epi: Mapped["EpiORM"] = relationship(
        "EpiORM", back_populates="movimentacoes", lazy="joined"
    )

    def to_dto(self) -> EpiMovDTO:
        return EpiMovDTO(
            epi_id=self.epi_id,
            tipo_movimentacao=self.tipo_movimentacao,
            quantidade_movimentada=self.quantidade_movimentada,
            data_hora=self.data_hora,
        )

__all__ = [
    "__version__",
    "EpiDTO", "EpiMovDTO", 
    "EpiORM", "EpiMovORM"
]
