""" DTO models for registry tables. """

from typing import Optional
from datetime import date
from dataclasses import dataclass

from .types_models import EPITypes, UnitTypes
from .exceptions import AttributesMissingError


@dataclass
class RegistryBaseDTO:
    id: Optional[int] = None
    name: str
    current_quantity: int

@dataclass
class RegistryEPIDTO(RegistryBaseDTO):
    ca_number: str
    id_batch: str
    type: EPITypes
    category: str
    validity: date

@dataclass
class RegistryInputDTO(RegistryBaseDTO):
    measure_unit: UnitTypes
    category: str

@dataclass
class RegistryProductDTO(RegistryBaseDTO):
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
class RegistrySuplierDTO:
    id: Optional[int]
    identfiers: SuppliersIdentifersDTO
    contact: SuppliersContactsDTO


__all__ = [
    "RegistryBaseDTO",
    
    "RegistryEPIDTO",
    "RegistryInputDTO", 
    "RegistryProductDTO",
    
    "SuppliersIdentifersDTO",
    "SuppliersContactsDTO",
    "RegistrySuplierDTO"
]
