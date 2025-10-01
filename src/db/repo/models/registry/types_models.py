""" Enum models for especify oblied value types. """

import enum

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

__all__ = [
    "EPITypes",
    "UnitTypes"
]
