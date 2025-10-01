""" Repositories for registry tables. """

from typing import Protocol, Iterable
from src.db.connection import session_scope
from .models import (
    RegistryEPIORM, RegistryInputORM, RegistryProductORM, RegistrySuplierORM,
    RegistryEPIDTO, RegistryInputDTO,  RegistryProductDTO, RegistrySuplierDTO,
    SuppliersIdentifersDTO, SuppliersContactsDTO
)

class RegistryRepositoryProtocol(Protocol):
    def create(self, dto) -> None:
        """ Creates a register. """
    def bulk_create(self, dtos) -> None:
        """ Creates multiples registers. """

class RegistryEPIRepository(RegistryRepositoryProtocol):
    def create(self, dto: RegistryEPIDTO):
        with session_scope() as session:
            session.add(RegistryEPIORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                ca_numero=dto.ca_number,
                id_lote=dto.id_batch,
                tipo=dto.type,
                categoria_id=dto.id_category
                # validade=dto.validity
            ))
    
    def bulk_create(self, dtos: Iterable):
        with session_scope() as session:
            session.add_all([RegistryEPIORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                ca_numero=dto.ca_number,
                id_lote=dto.id_batch,
                tipo=dto.type,
                categoria_id=dto.id_category
                # validade=dto.validity
            ) for dto in dtos])

class RegistryInputRepository(RegistryRepositoryProtocol):
    def create(self, dto: RegistryInputDTO):
        with session_scope() as session:
            session.add(RegistryInputORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                unidade_medida=dto.measure_unit,
                categoria_id=dto.id_category
            ))
    
    def bulk_create(self, dtos: Iterable):
        with session_scope() as session:
            session.add_all([RegistryInputORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                unidade_medida=dto.measure_unit,
                categoria_id=dto.id_category
            ) for dto in dtos])

class RegistryProductRepository(RegistryRepositoryProtocol):
    def create(self, dto: RegistryProductDTO):
        with session_scope() as session:
            session.add(RegistryProductORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                id_formula=dto.id_formula,
                categoria_id=dto.id_category,
                tag=dto.tag
            ))
    
    def bulk_create(self, dtos: Iterable):
        with session_scope() as session:
            session.add_all([RegistryProductORM(
                nome=dto.name,
                quantidade_atual=dto.current_quantity,
                id_formula=dto.id_formula,
                categoria_id=dto.id_category,
                tag=dto.tag
            ) for dto in dtos])

class RegistrySuplierRepository(RegistryRepositoryProtocol):
    def create(self, dto: RegistrySuplierDTO):
        with session_scope() as session:
            session.add(RegistrySuplierORM(
                nome=dto.identfiers.name,
                cnpj=dto.identfiers.cnpj,
                cpf=dto.identfiers.cpf,
                numero=dto.contact.number,
                email=dto.contact.email,
                outros_contatos=dto.contact.another_contact
            ))
    
    def bulk_create(self, dtos: Iterable):
        with session_scope() as session:
            session.add_all([RegistrySuplierORM(
                nome=dto.identfiers.name,
                cnpj=dto.identfiers.cnpj,
                cpf=dto.identfiers.cpf,
                numero=dto.contact.number,
                email=dto.contact.email,
                outros_contatos=dto.contact.another_contact
            ) for dto in dtos])


__all__ = [
    "RegistryEPIRepository",
    "RegistryInputRepository",
    "RegistryProductRepository",
    "RegistrySuplierRepository"
]
