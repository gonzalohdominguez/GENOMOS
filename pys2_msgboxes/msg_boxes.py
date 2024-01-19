from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon

class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        icono_ventana = 'pys2_msgboxes/icons/icono.png'
        q_icon = QIcon(icono_ventana)
        self.setWindowIcon(q_icon)

    def set_custom_icon(self, icon):
        self.setIconPixmap(icon)
    
    def set_yes_no_buttons(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

def correct_msgbox(title, text):
    msg_box = MsgBox(title, text)
    icon = 'pys2_msgboxes/icons/correct.png'
    msg_box.set_custom_icon(icon)
    msg_box.exec_()
  
def input_error_msgbox(title, text):
    msg_box = MsgBox(title, text)
    icon = 'pys2_msgboxes/icons/input_error.png'
    msg_box.set_custom_icon(icon)
    msg_box.exec_()

def warging_msgbox(title, text):
    msg_box = MsgBox(title, text)
    icon = 'pys2_msgboxes/icons/warning.png'
    msg_box.set_custom_icon(icon)
    msg_box.set_yes_no_buttons()
    resp = msg_box.exec_()
    return resp

def information_msgbox(title, text):
    msg_box = MsgBox(title, text)
    icon = 'pys2_msgboxes/icons/information.png'
    msg_box.set_custom_icon(icon)
    msg_box.exec_()
