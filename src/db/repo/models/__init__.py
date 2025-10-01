""" Models for repositories. """

from src.db.connection import create_tables

from .base import MovementType
from .category import (
    CategoriaBaseDTO, EPICategoriaDTO, InsumoCategoriaDTO, ProdutoCategoriaDTO,
    CategoriaBaseORM, EPICategoriaORM, InsumoCategoriaORM, ProdutoCategoriaORM
)
from .registry import (
    BaseRegistryORM, RegistryEPIORM, RegistryInputORM, RegistryProductORM, RegistrySuplierORM,
    RegistryBaseDTO, RegistryEPIDTO, RegistryInputDTO,  RegistryProductDTO, RegistrySuplierDTO,
    SuppliersIdentifersDTO, SuppliersContactsDTO
)

create_tables()

__version__ = "v.0.0.1"
__all__ = [
    "__version__",
    
    "MovementType",
    
    "CategoriaBaseDTO", "EPICategoriaDTO", "InsumoCategoriaDTO", "ProdutoCategoriaDTO",
    "CategoriaBaseORM", "EPICategoriaORM", "InsumoCategoriaORM", "ProdutoCategoriaORM"
    
    "BaseRegistryORM", "RegistryEPIORM", "RegistryInputORM", "RegistryProductORM", "RegistrySuplierORM",
    "RegistryBaseDTO", "RegistryEPIDTO", "RegistryInputDTO",  "RegistryProductDTO", 
    "SuppliersIdentifersDTO", "SuppliersContactsDTO", "RegistrySuplierDTO",
]
