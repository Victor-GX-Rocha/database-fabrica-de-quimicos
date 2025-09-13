from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, Mapped

from src.db.connection import Base

class Produto(Base):
    __tablename__ = "produto"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), index=True, unique=True, nullable=False)
    sku: Mapped[str] = mapped_column(String(64), unique=True)
    quantidade_atual: Mapped[int] = mapped_column(Integer)
    # unidade_medida: Mapped[str] = mapped_column(String(8))
    categoria: Mapped[str] = mapped_column(String(64))
    tags: Mapped[str] = mapped_column(String(256))


class Fornecedor(Base):...
class Insumo(Base):...
class Formula(Base):...
class EPI(Base):...

import enum
class MovementType(enum.Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"

class Movimentacao(Base):
    """ Em teoria, o certo seria eu criar tipos diferentes de movimentações. Ex.:
    Movimentações de Insumos (Materia prima):
        - Insumos são os materiais utilizados para fazer um produto.
        - Precisam ser contados por quantidade, litros, quilos, etc.
    Produtos:
        - Produtos são "matéria prima pós processamento".
        - Podem ser contados por unidade (diferente de litros ou quilos)
    Enfim, o certo é eu separar, pelo menos por enquanto.
    """

class MovInsumo(Base):
    
    __tablename__ = "movimentacoes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tipo: Mapped[str] = mapped_column(Enum(MovementType), nullable=False)
    insumo: Mapped[int] = mapped_column(Integer, )
    quantidade_movimentada: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    
    
    data_hora: Mapped[str] = mapped_column(DateTime)


# entrada
# saida

# Ok, bora começar fazendo alguma coisa, nem que simples.
