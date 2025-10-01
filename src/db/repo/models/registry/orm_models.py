""" ORM models for registry tables. """

from datetime import date
from dataclasses import dataclass
from sqlalchemy import Integer, String, Text, ForeignKey, Enum, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, composite, MappedAsDataclass

from src.db.connection import Base
from .types_models import EPITypes, UnitTypes
from .dto_models import (
    RegistryEPIDTO,
    RegistryInputDTO, 
    RegistryProductDTO,
    
    SuppliersIdentifersDTO,
    SuppliersContactsDTO,
    RegistrySuplierDTO
)


class BaseRegistryORM(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    quantidade_atual: Mapped[int] = mapped_column(Integer)
    
    def to_dto(self):
        """ Converts ORM to DTO with proper typing. """
        raise NotImplementedError("This method must be overwrited.")

@dataclass
class RegistryEPIORM(BaseRegistryORM):
    __tablename__ = "epi_registro"
    
    ca_numero: Mapped[str] = mapped_column(String(16), index=True)
    id_lote: Mapped[str] = mapped_column(String(16), index=True)
    tipo: Mapped[EPITypes] = mapped_column(Enum(EPITypes))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("epi_categoria.nome"))
    validade: Mapped[date] = mapped_column(Date, index=True)
    
    def to_dto(self) -> RegistryEPIDTO:
        return RegistryEPIDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            ca_number=self.ca_numero,
            id_batch=self.id_lote,
            type=self.tipo,
            category=self.categoria,
            validity=self.validade
        )

@dataclass
class RegistryInputORM(BaseRegistryORM):
    __tablename__ = "insumos_registro"
    
    unidade_medida: Mapped[UnitTypes] = mapped_column(Enum(UnitTypes))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("insumo_categoria.nome"))
    
    def to_dto(self) -> RegistryInputDTO:
        return RegistryInputDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            measure_unit=self.unidade_medida,
            category=self.categoria
        )

@dataclass
class RegistryProductORM(BaseRegistryORM):
    __tablename__ = "produtos_registro"
    
    id_formula: Mapped[int] = mapped_column(Integer, ForeignKey("formula.id"))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("produto_categoria.nome"))
    tag: Mapped[str] = mapped_column(Text)
    
    def to_dto(self) -> RegistryProductDTO:
        return RegistryProductDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            id_formula=self.id_formula,
            category=self.categoria,
            tag=self.tag
        )

@dataclass
class RegistrySuplierORM(Base):
    __tablename__ = "fornecedores_registro"
    
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
