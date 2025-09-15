""" Models for repositories. """

from .orms_temp import Produto, ProdutoDTO
from src.db.connection import create_tables

create_tables()

__version__ = "v.0.0.1"
__all__ = [
    "__version__",
    "Produto",
    "ProdutoDTO"
]
