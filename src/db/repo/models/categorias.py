""" Models for categorias (classification of items). """

from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from dataclasses import dataclass

from src.db.connection import Base


@dataclass
class CategoriaDTO:
    nome: str
    descricao: Optional[str]


@dataclass
class CategoriaORM(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True)
    descricao: Mapped[Optional[str]] = mapped_column(String(256))

    def to_dto(self) -> CategoriaDTO:
        return CategoriaDTO(
            nome=self.nome,
            descricao=self.descricao,
        )
