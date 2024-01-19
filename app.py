from PySide2.QtWidgets import QApplication
from controllers.main_window import ListGenotypeWindow
from qt_material import apply_stylesheet



if __name__ == "__main__":

    app = QApplication()
    window = ListGenotypeWindow()
    apply_stylesheet(app, theme = "light_blue.xml")
    window.show()
    app.exec_()