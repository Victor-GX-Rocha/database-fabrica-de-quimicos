""" Repository for "category" tables. """

from typing import Generic, TypeVar, Iterable
from src.db.connection import session_scope
from .models import (
    CategoriaBaseDTO, EPICategoriaDTO, InsumoCategoriaDTO, ProdutoCategoriaDTO,
    CategoriaBaseORM, EPICategoriaORM, InsumoCategoriaORM, ProdutoCategoriaORM
)


CategoriaORMType = TypeVar("CategoriaORMType", bound="CategoriaBaseDTO")
CategoriaDTOType = TypeVar("CategoriaDTOType", bound="CategoriaBaseORM")

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

class CategoryEPIRepository(CategoryRepositoryBase[EPICategoriaDTO, EPICategoriaORM]):
    def __init__(self) -> None:
        super().__init__(EPICategoriaORM)

class CategoryInsumoRepository(CategoryRepositoryBase[InsumoCategoriaDTO, InsumoCategoriaORM]):
    def __init__(self) -> None:
        super().__init__(InsumoCategoriaORM)

class CategoryProdutoRepository(CategoryRepositoryBase[ProdutoCategoriaDTO, ProdutoCategoriaORM]):
    def __init__(self) -> None:
        super().__init__(ProdutoCategoriaORM)
