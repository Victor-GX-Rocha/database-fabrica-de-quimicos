""" Models for repositories. """

from src.db.connection import create_tables

from .base import MovementType, PackagingTypes, SpecificationTypes
from .formule import FormuleORM, FormuleDTO
from .category import (
    CategoryBaseDTO, CategoryEPIDTO, CategoryInputDTO, CategoryProductDTO,
    CategoryBaseORM, CategoryEPIORM, CategoryInputORM, CategoryProductORM
)
from .registry import (
    BaseRegistryORM, RegistryEPIORM, RegistryInputORM, RegistryProductORM, RegistrySuplierORM,
    RegistryBaseDTO, RegistryEPIDTO, RegistryInputDTO,  RegistryProductDTO, RegistrySuplierDTO,
    SuppliersIdentifersDTO, SuppliersContactsDTO,
    EPITypes, UnitTypes
)
from .movement import (
    MovInputDTO, MovProductDTO, MovEPIDTO,
    MovInputORM, MovProductORM, MovEPIORM
)


create_tables()

__version__ = "v.0.0.1"
__all__ = [
    "__version__",
    
    "MovementType", "PackagingTypes", "SpecificationTypes",
    
    "FormuleORM", "FormuleDTO",
    
    "CategoryBaseDTO", "CategoryEPIDTO", "CategoryInputDTO", "CategoryProductDTO",
    "CategoryBaseORM", "CategoryEPIORM", "CategoryInputORM", "CategoryProductORM",
    
    "BaseRegistryORM", "RegistryEPIORM", "RegistryInputORM", "RegistryProductORM", "RegistrySuplierORM",
    "RegistryBaseDTO", "RegistryEPIDTO", "RegistryInputDTO", "RegistryProductDTO", "RegistrySuplierDTO",
    "SuppliersIdentifersDTO", "SuppliersContactsDTO",
    "EPITypes", "UnitTypes",
    
    "MovInputDTO", "MovProductDTO", "MovEPIDTO",
    "MovInputORM", "MovProductORM", "MovEPIORM"
]
