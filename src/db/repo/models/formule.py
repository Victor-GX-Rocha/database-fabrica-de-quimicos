""" Models for formule tables. """

from __future__ import annotations
from dataclasses import dataclass
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.connection import Base
if TYPE_CHECKING:
    from .registry.orm_models import RegistryProductORM

@dataclass
class FormuleDTO:
    id: int = None
    name: str = None
    function: str = None
    cod_cas: str = None
    qtd_base: float = None

class FormuleORM(Base):
    __tablename__ = "formulas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), unique=True, index=True)
    funcao: Mapped[str] = mapped_column(String(256))
    cod_cas: Mapped[str] = mapped_column(String(128))
    qtd_base: Mapped[float] = mapped_column(Float, index=True)
    
    produto_registro: Mapped[List["RegistryProductORM"]] = relationship(
        "RegistryProductORM",
        back_populates="formula_orm",
        lazy="selectin"
    )
    
    def to_dto(self) -> FormuleDTO:
        return FormuleDTO(
            id=self.id,
            name=self.nome,
            function=self.funcao,
            cod_cas=self.cod_cas,
            qtd_base=self.qtd_base
        )

__all__ = [
    "FormuleORM",
    "FormuleDTO"
]
