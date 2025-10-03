""" Bases for models. """

import enum


class MovementType(enum.Enum):
    """ Defines the moviment types. """
    INBOUND = "entrada"
    OUTBOUND = "saida"

class PackagingTypes(enum.Enum):
    BOX: str = "Caixa"
    Fitage: str = "Fitagem"

class SpecificationTypes(enum.Enum):
    POWDER: str = "Pó"
    LIQUID: str = "Líquido"
    GRANULAR: str = "Granulado"

__all__ = [
    "MovementType",
    "PackagingTypes",
    "SpecificationTypes"
]
