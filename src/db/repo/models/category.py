""" ORMs models for category tables. """

from __future__ import annotations
from typing import Optional, ClassVar, Type, List, TYPE_CHECKING
from dataclasses import dataclass
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.connection import Base

if TYPE_CHECKING:
    from .registry import RegistryEPIORM, RegistryInputORM, RegistryProductORM

@dataclass
class CategoryBaseDTO:
    """
    Base to represents a category table.
    Args:
        id (int): Line ID.
        name (str): Category name.
        comment (str | None): Extra information about the category.
    """
    id: Optional[int] = None
    name: str = None
    comment: Optional[str] = None

class CategoryEPIDTO(CategoryBaseDTO):...
class CategoryInputDTO(CategoryBaseDTO):...
class CategoryProductDTO(CategoryBaseDTO):...


class CategoryBaseORM(Base):
    __abstract__ = True
    __DTO__: ClassVar[Type[CategoryBaseDTO]] = CategoryBaseDTO
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False, index=True, unique=True)
    comentario: Mapped[str] = mapped_column(Text, default=None)
    
    def to_dto(self):
        """ Converts ORM to DTO with proper typing. """
        return self.__DTO__(
            id=self.id,
            name=self.nome,
            comment=self.comentario,
        )

@dataclass
class CategoryEPIORM(CategoryBaseORM):
    __tablename__ = "categoria_epi"
    __DTO__ = CategoryEPIDTO
    registro: Mapped[List["RegistryEPIORM"]] = relationship(
        "RegistryEPIORM",
        back_populates="categoria_orm",
        lazy="selectin"
    )

@dataclass
class CategoryInputORM(CategoryBaseORM):
    __tablename__ = "categoria_insumo"
    __DTO__ = CategoryInputDTO
    registro: Mapped[List["RegistryInputORM"]] = relationship(
        "RegistryInputORM",
        back_populates="categoria_orm",
        lazy="selectin"
    )

@dataclass
class CategoryProductORM(CategoryBaseORM):
    __tablename__ = "categoria_produto"
    __DTO__ = CategoryProductDTO
    registro: Mapped[List["RegistryProductORM"]] = relationship(
        "RegistryProductORM",
        back_populates="categoria_orm",
        lazy="selectin"
    )

__all__ = [
    "CategoryBaseDTO", "CategoryEPIDTO", "CategoryInputDTO", "CategoryProductDTO",
    "CategoryBaseORM", "CategoryEPIORM", "CategoryInputORM", "CategoryProductORM"
]
