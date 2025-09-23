""" ORMs models for category tables. """

from typing import Optional, ClassVar, Type
from dataclasses import dataclass
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


@dataclass
class CategoriaBaseDTO:
    """
    Base to represents a category table.
    Args:
        id (int): Line ID.
        name (str): Category name.
        comment (str | None): Extra information about the category.
    """
    id: Optional[int] = None
    name: str
    comment: Optional[str] = None

class EPICategoriaDTO(CategoriaBaseDTO):...
class InsumoCategoriaDTO(CategoriaBaseDTO):...
class ProdutoCategoriaDTO(CategoriaBaseDTO):...


class CategoriaBaseORM(DeclarativeBase):
    __abstract__ = True
    __DTO__: ClassVar[Type[CategoriaBaseDTO]] = CategoriaBaseDTO
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    comentario: Mapped[str] = mapped_column(Text, default=None)
    
    def to_dto(self):
        """ Converts ORM to DTO with proper typing. """
        return self.__DTO__(
            id=self.id,
            name=self.nome,
            comment=self.comentario,
        )

@dataclass
class EPICategoriaORM(CategoriaBaseORM):
    __tablename__ = "epi_categoria"
    __DTO__ = EPICategoriaDTO

@dataclass
class InsumoCategoriaORM(CategoriaBaseORM):
    __tablename__ = "insumo_categoria"
    __DTO__ = InsumoCategoriaDTO

@dataclass
class ProdutoCategoriaORM(CategoriaBaseORM):
    __tablename__ = "produto_categoria"
    __DTO__ = ProdutoCategoriaDTO

__all__ = [
    "CategoriaBaseDTO",
    "EPICategoriaDTO",
    "InsumoCategoriaDTO",
    "ProdutoCategoriaDTO",
    
    "CategoriaBaseORM",
    "EPICategoriaORM",
    "InsumoCategoriaORM",
    "ProdutoCategoriaORM"
]
