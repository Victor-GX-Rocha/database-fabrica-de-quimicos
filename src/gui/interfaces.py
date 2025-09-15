""" UIs for user. """

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton

from .produtos import IProductRegister


class IMainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Banco de dados 🏭")
        self._build_ui()
    
    def _build_ui(self) -> None:
        """ Builds the interface. """
        w = QWidget()
        layout = QVBoxLayout()
        
        # Buttons
        btn_add_product = QPushButton("Registrar novo produto")
        btn_add_product.clicked.connect(self.__open_product_register)
        layout.addWidget(btn_add_product)
        
        w.setLayout(layout)
        self.setCentralWidget(w)
    
    def __open_product_register(self) -> None:
        dlg = IProductRegister(parent=self)
        dlg.exec()

__all__ = [
    "IMainWindow"
]

# # Testes
# if __name__ == "__main__":
#     def main():
#         from PySide6.QtWidgets import QApplication
#         import sys
        
#         app = QApplication(sys.argv)
#         win = IMainWindow()
#         win.show()
#         sys.exit(app.exec())
    
#     main()
