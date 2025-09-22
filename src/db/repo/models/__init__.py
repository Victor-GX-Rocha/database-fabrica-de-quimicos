""" Models for repositories. """

from .produtos import ProdutoDTO, ProdutoMovDTO, ProdutoORM, ProdutoMovORM
from .insumos import InsumoDTO, InsumoMovDTO, InsumoORM, InsumoMovORM
from .epi import EpiDTO, EpiMovDTO, EpiORM, EpiMovORM
from src.db.connection import create_tables

create_tables()

__version__ = "v.0.0.1"
__all__ = [
    "__version__",
    "ProdutoDTO", "ProdutoMovDTO", "ProdutoORM", "ProdutoMovORM",
    "InsumoDTO", "InsumoMovDTO", "InsumoORM","InsumoMovORM",
    "EpiDTO", "EpiMovDTO", "EpiORM", "EpiMovORM"
]