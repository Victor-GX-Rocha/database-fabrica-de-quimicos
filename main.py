from src.db.repo.models import Produto, ProdutoDTO
from src.db.repo.repo_temp import ProdutoRepository


def main():
    # Teste - adicionar um produto
    produto = ProdutoDTO(
        name="Detergente",
        current_quantity=100,
        category="Limpeza",
        tags="sla"
    )
    repo = ProdutoRepository()
    repo.register_new_product(produto)

if __name__ == "__main__":
    main()
