from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.information_window import InformationForm

class InformationGenotypeWindow(QWidget, InformationForm):
    # Constructor
    def __init__(self, parent = None): 
        super().__init__(parent)
        self.setupUi(self)
        # Crea una nueva ventana, diferente a la de la clase padre
        self.setWindowFlag(Qt.Window)