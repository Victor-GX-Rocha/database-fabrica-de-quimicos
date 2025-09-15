""" App to controls the main interface of the program. """

import sys
from PySide6.QtWidgets import QApplication

from src.gui import IMainWindow

class DatabaseAplication:
    @staticmethod
    def execute():
        app = QApplication(sys.argv)
        win = IMainWindow()
        win.show()
        sys.exit(app.exec())

__all__ = [
    "DatabaseAplication"
]
