""" ORMs models for registry tables. """

import enum
from typing import Optional
from datetime import date
from dataclasses import dataclass
from sqlalchemy import Integer, String, Text, ForeignKey, Enum, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, composite, MappedAsDataclass

from src.db.connection import Base

# ------------------- Personalized exceptions -------------------
class RegistryTablesBaseError(Exception):
    """ Base for Registry table errors. """

class AttributesMissingError(RegistryTablesBaseError):
    """ At least one of the attributes must be infromed. """

# ------------------- Enum models -------------------
class EPITypes(enum.Enum):
    """ Just generic examples, I still don't know what types of EPIs the client would like to put. """
    TYPE1 = "TYPE1"
    TYPE2 = "TYPE2"
    TYPE3 = "TYPE3"

class UnitTypes(enum.Enum):
    LITER: str = "Litro (L)"
    MILLILITER: str = "Mililitro (ml)"
    KILOGRAM: str = "Quilograma (kg)"
    GRAM: str = "Grama (g)"
    UNIT: str = "Unidade"

# ------------------- DTO models -------------------
@dataclass
class BaseRegistryDTO:
    id: Optional[int] = None
    name: str
    current_quantity: int

@dataclass
class EpiRegistryDTO(BaseRegistryDTO):
    ca_number: str
    id_batch: str
    type: EPITypes
    category: str
    validity: date

@dataclass
class InsumosRegistryDTO(BaseRegistryDTO):
    measure_unit: UnitTypes
    category: str

@dataclass
class ProdutosRegistryDTO(BaseRegistryDTO):
    id_formula: int
    category: str
    tag: str

@dataclass
class SuppliersIdentifersDTO:
    name: str
    cnpj: Optional[str] = None
    cpf: Optional[str] = None
    
    def __post_init__(self) -> None:
        self._has_identifier()
    
    def _has_identifier(self) -> None:
        if not any((self.cnpj, self.cpf)):
            raise AttributesMissingError("At least CNPJ or CPF must be included.")

@dataclass
class SuppliersContactsDTO:
    number: Optional[str] = None
    email: Optional[str] = None
    another_contact: Optional[str] = None
    
    def __post_init__(self) -> None:
        self._has_contact()
    
    def _has_contact(self) -> None:
        if not any((self.numero, self.email, self.outros_contatos)):
            raise AttributesMissingError("At least one of the contact ways must be informed.")

@dataclass
class SuppliersRegistryDTO:
    id: Optional[int]
    identfiers: SuppliersIdentifersDTO
    contact: SuppliersContactsDTO


# ------------------- ORM models -------------------
class BaseRegistryORM(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    quantidade_atual: Mapped[int] = mapped_column(Integer)
    
    def to_dto(self):
        """ Converts ORM to DTO with proper typing. """
        raise NotImplementedError("This method must be overwrited.")

@dataclass
class EpiRegistryORM(BaseRegistryORM):
    __tablename__ = "epi_registro"
    
    ca_numero: Mapped[str] = mapped_column(String(16), index=True)
    id_lote: Mapped[str] = mapped_column(String(16), index=True)
    tipo: Mapped[EPITypes] = mapped_column(Enum(EPITypes))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("epi_categoria.nome"))
    validade: Mapped[date] = mapped_column(Date, index=True)
    
    def to_dto(self) -> EpiRegistryDTO:
        return EpiRegistryDTO(
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
class InsumosRegistryORM(BaseRegistryORM):
    __tablename__ = "insumos_registro"
    
    unidade_medida: Mapped[UnitTypes] = mapped_column(Enum(UnitTypes))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("insumo_categoria.nome"))
    
    def to_dto(self) -> InsumosRegistryDTO:
        return InsumosRegistryDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            measure_unit=self.unidade_medida,
            category=self.categoria
        )

@dataclass
class ProdutosRegistryORM(BaseRegistryORM):
    __tablename__ = "produtos_registro"
    
    id_formula: Mapped[int] = mapped_column(Integer, ForeignKey("formula.id"))
    categoria: Mapped[str] = mapped_column(String(64), ForeignKey("produto_categoria.nome"))
    tag: Mapped[str] = mapped_column(Text)
    
    def to_dto(self) -> ProdutosRegistryDTO:
        return ProdutosRegistryDTO(
            id=self.id,
            name=self.nome,
            current_quantity=self.quantidade_atual,
            id_formula=self.id_formula,
            category=self.categoria,
            tag=self.tag
        )

@dataclass
class FornecedoresRegistryORM(Base):
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
    
    def to_dto(self) -> SuppliersRegistryDTO:
        return SuppliersRegistryDTO(
            id=self.id,
            identfiers=self.identfiers,
            contact=self.contact
        )
