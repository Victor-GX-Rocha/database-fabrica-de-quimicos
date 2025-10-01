""" ORM models for registry tables. """

from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date
from dataclasses import dataclass
from sqlalchemy import Integer, String, Text, ForeignKey, Enum, Date
from sqlalchemy.orm import Mapped, mapped_column, composite, MappedAsDataclass, relationship

from src.db.connection import Base
if TYPE_CHECKING:
    from src.db.repo.models import CategoryEPIORM, CategoryInputORM, CategoryProductORM
# from src.db.repo.models import CategoryEPIORM, CategoryInputORM, CategoryProductORM
from src.db.repo.models.formula import Formule
from .types_models import EPITypes, UnitTypes
from .dto_models import (
    RegistryEPIDTO,
    RegistryInputDTO, 
    RegistryProductDTO,
    
    SuppliersIdentifersDTO,
    SuppliersContactsDTO,
    RegistrySuplierDTO
)


class BaseRegistryORM(Base):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    quantidade_atual: Mapped[int] = mapped_column(Integer)
    
    def to_dto(self):
        """ Converts ORM to DTO with proper typing. """
        raise NotImplementedError("This method must be overwrited.")

@dataclass
class RegistryEPIORM(BaseRegistryORM):
    __tablename__ = "registro_epi"
    
    ca_numero: Mapped[str] = mapped_column(String(16), index=True)
    id_lote: Mapped[str] = mapped_column(String(16), index=True)
    tipo: Mapped[EPITypes] = mapped_column(Enum(EPITypes))
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categoria_epi.id"), nullable=False)
    validade: Mapped[date] = mapped_column(Date, index=True)
    
    categoria_orm: Mapped["CategoryEPIORM"] = relationship(
        "CategoryEPIORM",
        back_populates="registro",
        lazy="joined"
    )
    
    def to_dto(self) -> RegistryEPIDTO:
        return RegistryEPIDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            ca_number=self.ca_numero,
            id_batch=self.id_lote,
            type=self.tipo,
            category=self.categoria_id,
            validity=self.validade
        )

@dataclass
class RegistryInputORM(BaseRegistryORM):
    __tablename__ = "registro_insumos"
    
    unidade_medida: Mapped[UnitTypes] = mapped_column(Enum(UnitTypes))
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categoria_insumo.id"), nullable=False)
    
    categoria_orm: Mapped["CategoryInputORM"] = relationship(
        "CategoryInputORM",
        back_populates="registro",
        lazy="joined"
    )
    
    def to_dto(self) -> RegistryInputDTO:
        return RegistryInputDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            measure_unit=self.unidade_medida,
            category=self.categoria_id
        )

@dataclass
class RegistryProductORM(BaseRegistryORM):
    __tablename__ = "registro_produtos"
    
    id_formula: Mapped[int] = mapped_column(Integer, ForeignKey("formulas.id"))
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categoria_produto.id"), nullable=False) 
    tag: Mapped[str] = mapped_column(Text)
    
    formula_orm: Mapped["Formule"] = relationship(
        "Formule",
        back_populates="formula_orm",
        lazy="joined"
    )
    
    categoria_orm: Mapped["CategoryProductORM"] = relationship(
        "CategoryProductORM",
        back_populates="registro",
        lazy="joined"
    )
    
    def to_dto(self) -> RegistryProductDTO:
        return RegistryProductDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            id_formula=self.id_formula,
            category=self.categoria_id,
            tag=self.tag
        )

@dataclass
class RegistrySuplierORM(Base):
    __tablename__ = "registro_fornecedores"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(16), nullable=True)
    cpf: Mapped[str] = mapped_column(String(16), nullable=True)
    numero: Mapped[str] = mapped_column(String(16), nullable=True)
    email: Mapped[str] = mapped_column(String(128), nullable=True)
    outros_contatos: Mapped[str] = mapped_column(String(256), nullable=True)
    
    identfiers = composite(
        SuppliersIdentifersDTO,
        "nome", "cnpj", "cpf"
    )
    
    contact = composite(
        SuppliersContactsDTO,
        "numero", "email", "outros_contatos"
    )
    
    
    def to_dto(self) -> RegistrySuplierDTO:
        return RegistrySuplierDTO(
            id=self.id,
            identfiers=self.identfiers,
            contact=self.contact
        )

__all__ = [
    "BaseRegistryORM",
    
    "RegistryEPIORM",
    "RegistryInputORM",
    "RegistryProductORM",
    "RegistrySuplierORM",
]
