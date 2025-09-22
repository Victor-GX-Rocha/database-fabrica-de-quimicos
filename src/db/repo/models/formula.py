""" Models for formulas (chemical formulations). """

from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from dataclasses import dataclass

from src.db.connection import Base


@dataclass
class FormulaDTO:
    nome: str
    funcao: Optional[str]
    cod_cas: Optional[str]
    qtd_base: int


@dataclass
class FormulaORM(Base):
    __tablename__ = "formulas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(128), nullable=False, unique=True, index=True)
    funcao: Mapped[Optional[str]] = mapped_column(String(128))
    cod_cas: Mapped[Optional[str]] = mapped_column(String(64), unique=True)
    qtd_base: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dto(self) -> FormulaDTO:
        return FormulaDTO(
            nome=self.nome,
            funcao=self.funcao,
            cod_cas=self.cod_cas,
            qtd_base=self.qtd_base,
        )
