""" UI interface for produtos. """

from PySide6.QtWidgets import (
    QVBoxLayout, QPushButton,
    QDialog, QTableWidget, QTableWidgetItem, 
    QAbstractItemView, QHBoxLayout, QMessageBox,
    QHeaderView
)

from src.db.repo import ProdutoRepository
from src.db.repo.models import (
    ProdutoDTO, ProdutoORM, 
    ProdutoMovDTO, ProdutoMovORM
)


class IProductRegister(QDialog):
    def __init__(self, parent=None) -> None:
        self.repo = ProdutoRepository()
        self.coluns: list[str] = ["Nome", "Quantidade inicial", "Categoria", "lote_id", "Tags"]
        
        super().__init__(parent)
        # self.resize(450, 300)
        # self.setMinimumSize(400, 300)
        self.setWindowTitle("Registrar produto")
        self._build_ui()
    
    def _build_ui(self) -> None:
        # Layouts
        layout = QVBoxLayout()
        self._add_table_widget(layout)
        self._add_buttons(layout)
        # self.showEvent()
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
        
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
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
        self._adjust_window_size()
    
    def _remove_row(self):
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)
        self._adjust_window_size()
    
    def _save_rows(self):
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
    
    def _adjust_window_size(self):
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        # Calculate the total size of a table
        width = self.table.verticalHeader().width() + sum([self.table.columnWidth(i) for i in range(self.table.columnCount())])
        height = self.table.horizontalHeader().height() + sum([self.table.rowHeight(i) for i in range(self.table.rowCount())])
        
        # Adds a margin to layout and buttons  
        height += 150  # Space to buttons
        width += 70    # Space horizontal margins
        
        # Ajust the size of the window withot exced the maximum allowed
        self.resize(min(width, 700), min(height, 600))

__all__ = [ 
    "IProductRegister"
]
