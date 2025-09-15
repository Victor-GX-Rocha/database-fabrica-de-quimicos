""" UI interface for produtos. """

from PySide6.QtWidgets import (
    QVBoxLayout, QPushButton,
    QDialog, QTableWidget, QTableWidgetItem, 
    QAbstractItemView, QHBoxLayout, QMessageBox
)

from src.db.repo import ProdutoRepository
from src.db.repo.models import (
    ProdutoDTO, ProdutoORM, 
    ProdutoMovDTO, ProdutoMovORM
)


class IProductRegister(QDialog):
    def __init__(self, parent=None) -> None:
        self.repo = ProdutoRepository()
        
        super().__init__(parent)
        self.setWindowTitle("Registrar produto")
        self.coluns: list[str] = ["Nome", "Quantidade inicial", "Categoria", "Tags"]
        self._build_ui()
    
    def _build_ui(self) -> None:
        # Layouts
        layout = QVBoxLayout()
        self._add_table_widget(layout)
        self._add_buttons(layout)
        self.setLayout(layout)
    
    def _add_table_widget(self, layout: QVBoxLayout):
        """ Constructs a table to add products """
        
        qtd_initial_lines: int = 0
        qtd_initial_coluns: int = len(self.coluns)
        
        self.table = QTableWidget(qtd_initial_lines, qtd_initial_coluns)
        self.table.setHorizontalHeaderLabels(self.coluns)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        
        self.table.setDragEnabled(False)
        self.table.setDragDropOverwriteMode(False)
        
        layout.addWidget(self.table)
    
    def _add_buttons(self, layout: QVBoxLayout) -> None:
        """ Constructs the buttons to interface. """
        
        btn_add = QPushButton("Adicionar produto")
        btn_remove = QPushButton("Remover produto selecionado")
        btn_register = QPushButton("Registrar adição")
        btn_add.clicked.connect(self._add_row)
        btn_remove.clicked.connect(self._remove_row)
        btn_register.clicked.connect(self._save_rows)
        
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_remove)
        
        layout.addLayout(btn_layout)
        layout.addWidget(btn_register)
    
    def _add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col in range(len(self.coluns)):
            self.table.setItem(row, col, QTableWidgetItem(""))
    
    def _remove_row(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
    
    def _save_rows(self):
        # "Nome", "Quantidade inicial", "Categoria", "Tags"
        for row in range(self.table.rowCount()):
            name: str = self.table.item(row, 0).text().strip()
            category: str = self.table.item(row, 2).text().strip()
            tags: str = self.table.item(row, 3).text().strip()
            
            try:
                qtd_initial = int(self.table.item(row, 1).text().strip())
            except:
                QMessageBox.warning(self, "Erro", f"Quantidade inválida na linha {row + 1}. \nInsira um número inteiro!")
                continue
            
            self.repo.register_new_product(ProdutoDTO(
                name=name,
                current_quantity=qtd_initial,
                category=category,
                tags=tags
            ))
        
        QMessageBox.information(self, "Sucesso", "Produtos adicionados com sucesso!")

__all__ = [ 
    "IProductRegister"
]
