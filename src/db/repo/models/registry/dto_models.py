""" DTO models for registry tables. """

from typing import Optional
from datetime import date
from dataclasses import dataclass

from .types_models import EPITypes, UnitTypes
from .exceptions import AttributesMissingError


@dataclass
class RegistryBaseDTO:
    id: Optional[int] = None
    name: str = None
    current_quantity: int = None

@dataclass
class RegistryEPIDTO(RegistryBaseDTO):
    ca_number: str = None
    id_batch: str = None
    type: EPITypes = None
    id_category: int = None
    # validity: date = None

@dataclass
class RegistryInputDTO(RegistryBaseDTO):
    measure_unit: UnitTypes = None
    id_category: int = None

@dataclass
class RegistryProductDTO(RegistryBaseDTO):
    id_formula: int = None
    id_category: int = None
    tag: str = None

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
        if not any((self.number, self.email, self.another_contact)):
            raise AttributesMissingError("At least one of the contact ways must be informed.")

@dataclass
class RegistrySuplierDTO:
    id: Optional[int] = None
    identfiers: SuppliersIdentifersDTO = None
    contact: SuppliersContactsDTO = None


__all__ = [
    "RegistryBaseDTO",
    
    "RegistryEPIDTO",
    "RegistryInputDTO", 
    "RegistryProductDTO",
    
    "SuppliersIdentifersDTO",
    "SuppliersContactsDTO",
    "RegistrySuplierDTO"
]
