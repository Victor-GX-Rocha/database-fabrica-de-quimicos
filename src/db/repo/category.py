""" Repository for "category" tables. """

from typing import Generic, TypeVar, Iterable
from src.db.connection import session_scope
from .models import (
    CategoryBaseDTO, CategoryEPIDTO, CategoryInputDTO, CategoryProductDTO,
    CategoryBaseORM, CategoryEPIORM, CategoryInputORM, CategoryProductORM
)


CategoriaORMType = TypeVar("CategoriaORMType", bound="CategoryBaseDTO")
CategoriaDTOType = TypeVar("CategoriaDTOType", bound="CategoryBaseORM")

class CategoryRepositoryBase(Generic[CategoriaORMType, CategoriaDTOType]):
    """ Base repository for category tables with shared structure. """
    def __init__(self, orm_class: type[CategoriaORMType]) -> None:
        self.orm_class = orm_class
    
    def create(self, dto: CategoriaDTOType) -> None:
        """ Creates a category register. """
        with session_scope() as session:
            session.add(self.orm_class(
                nome=dto.name,
                comentario=dto.comment
            ))
    
    def bulk_create(self, dtos: Iterable[CategoriaDTOType]) -> None:
        """ Creates multilple category registers. """
        with session_scope() as session:
            session.add_all([self.orm_class(
                nome=dto.name,
                comentario=dto.comment
            ) for dto in dtos])

class CategoryEPIRepository(CategoryRepositoryBase):
    def __init__(self) -> None:
        super().__init__(CategoryEPIORM)

class CategoryInputRepository(CategoryRepositoryBase[CategoryInputDTO, CategoryInputORM]):
    def __init__(self) -> None:
        super().__init__(CategoryInputORM)

class CategoryProductRepository(CategoryRepositoryBase[CategoryProductDTO, CategoryProductORM]):
    def __init__(self) -> None:
        super().__init__(CategoryProductORM)

__all__ = [
    "CategoryEPIRepository",
    "CategoryInputRepository",
    "CategoryProductRepository"
]
