""" Models for formule tables. """

from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.connection import Base
if TYPE_CHECKING:
    from .registry.orm_models import RegistryProductORM

class Formule(Base):
    __tablename__ = "formulas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), unique=True, index=True)
    funcao: Mapped[str] = mapped_column(String(256))
    cod_cas: Mapped[str] = mapped_column(String(128))
    qtd_base: Mapped[float] = mapped_column(Float, index=True)
    
    formula_orm: Mapped[List["RegistryProductORM"]] = relationship(
        "Formule",
        back_populates="formula_orm",
        lazy="selectin"
    )

__all__ = [
    "Formule"
]
