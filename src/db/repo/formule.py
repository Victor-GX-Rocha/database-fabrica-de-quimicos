
from typing import Iterable

from src.db.connection import session_scope
from .models.formule import FormuleORM, FormuleDTO

class FormuleRepository:
    def create(self, dto: FormuleDTO) -> None:
        """ Registrates a formule. """
        with session_scope() as session:
            session.add(FormuleORM(
                nome=dto.name,
                funcao=dto.function,
                cod_cas=dto.cod_cas,
                qtd_base=dto.qtd_base
            ))
    
    def bulk_create(self, dtos: Iterable) -> None:
        """ Registrate multiples formules. """
        with session_scope() as session:
            session.add_all([FormuleORM(
                nome=dto.name,
                funcao=dto.function,
                cod_cas=dto.cod_cas,
                qtd_base=dto.qtd_base
            ) for dto in dtos])

__all__ = [
    "FormuleRepository"
]
