""" Bases for models. """

import enum


class MovementType(enum.Enum):
    """ Defines the moviment types. """
    INBOUND = "entrada"
    OUTBOUND = "saida"

__all__ = [
    "MovementType"
]
