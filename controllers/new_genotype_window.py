from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.new_genotype_window import NewGenotypeForm

# Importamos la función que ejecuta el query para insertar una nueva muestra
from db.genotype import insert_genotype

# Mensajes de alerta
from pys2_msgboxes import msg_boxes

class NewGenotypeWindow(QWidget, NewGenotypeForm):
    # Constructor
    def __init__(self, parent = None): 
        super().__init__(parent)
        self.setupUi(self)
        # Crea una nueva ventana, diferente a la de la clase padre
        self.setWindowFlag(Qt.Window)

        # Enlazamos el botón de "Agregar" muestra con la función 'add_genotype'
        self.addButton.clicked.connect(self.add_genotype)

        # Enlazamos el botón de "Cancelar" con una función por defecto (de la ventana) que se llama 'close'
        self.cancelButton.clicked.connect(self.close)

    # Función que se encarga de validar la entrada de datos del usuario
    def check_inputs(self):
        temperature_melting_2016 = self.temperature1016LineEdit.text()
        temperature_melting_1543 = self.temperature1534LineEdit.text()
        temperature_melting_2016_SS = self.temperature1016SSLineEdit.text()
        temperature_melting_2016_SR = self.temperature1016SRLineEdit.text()
        temperature_melting_2016_RR = self.temperature1016RRLineEdit.text()
        temperature_melting_1543_SS = self.temperature1534SSLineEdit.text()
        temperature_melting_1543_SR = self.temperature1534SRLineEdit.text()
        temperature_melting_1543_RR = self.temperature1534RRLineEdit.text()

        errors_count = 0

        if temperature_melting_2016 == "":
            print("El campo temperature_melting_2016 es obligatorio")
            errors_count +=1

        if temperature_melting_1543 == "":
            print("El campo temperature_melting_1543 es obligatorio")
            errors_count +=1

        if temperature_melting_2016_SS == "":
            print("El campo temperature_melting_2016_SS es obligatorio")
            errors_count +=1

        if temperature_melting_2016_SR == "":
            print("El campo temperature_melting_2016_SR es obligatorio")
            errors_count +=1

        if temperature_melting_2016_RR == "":
            print("El campo temperature_melting_2016_RR es obligatorio")
            errors_count +=1

        if temperature_melting_1543_SS == "":
            print("El campo temperature_melting_1543_SS es obligatorio")
            errors_count +=1

        if temperature_melting_1543_SR == "":
            print("El campo temperature_melting_1543_SR es obligatorio")
            errors_count +=1

        if temperature_melting_1543_RR == "":
            print("El campo temperature_melting_1543_RR es obligatorio")
            errors_count +=1

        if errors_count == 0:
            return True
        else: 
            msg_boxes.input_error_msgbox("Error", "Todos los campos son obligatorios")

    # Función que agrega una nueva muestra
    def add_genotype(self):
        temperature_melting_2016 = self.temperature1016LineEdit.text()
        temperature_melting_1543 = self.temperature1534LineEdit.text()
        temperature_melting_1016_SS = self.temperature1016SSLineEdit.text()
        temperature_melting_1016_SR = self.temperature1016SRLineEdit.text()
        temperature_melting_1016_RR = self.temperature1016RRLineEdit.text()
        temperature_melting_1543_SS = self.temperature1534SSLineEdit.text()
        temperature_melting_1543_SR = self.temperature1534SRLineEdit.text()
        temperature_melting_1543_RR = self.temperature1534RRLineEdit.text()

        if self.check_inputs(): 
            # Si la función retorna True, entonces significa que no hay errores 
            # (se completaron todos los parámetros obligatorios)
            data = (temperature_melting_2016, temperature_melting_1543, temperature_melting_1016_SS, temperature_melting_1016_SR, temperature_melting_1016_RR, temperature_melting_1543_SS, temperature_melting_1543_SR, temperature_melting_1543_RR)
            # Pasamos los datos para insertar una nueva muestra a la función perteneciente al archivo genotype.py
            if insert_genotype(data):
                # Si la muestra se insertó en la BD correctamente, ejecutamos la función que me limpias las cajas de texto
                self.clean_inputs()
                msg_boxes.correct_msgbox("Información", "Correcta inserción de una muestra")
            else: # Si ocurre algún error en la inserción de la muestra
                msg_boxes.input_error_msgbox("Error", "Error en la inserción de una muestra")

    # Función que, luego de agregar una muestra, "limpia" los inputs
    def clean_inputs(self):
        self.temperature1016LineEdit.clear()
        self.temperature1534LineEdit.clear()
        self.temperature1016SSLineEdit.clear()
        self.temperature1016SRLineEdit.clear()
        self.temperature1016RRLineEdit.clear()
        self.temperature1534SSLineEdit.clear()
        self.temperature1534SRLineEdit.clear()
        self.temperature1534RRLineEdit.clear()

    # Función que ejecuta la ventana para seleccionar el archivo
    def select_file(self):
        pass
    #     # Almacenamos el path del archivo seleccionado
    #     file_path = QFileDialog.getOpenFileName()[0]
    #     # La función anterior retorna una lista. Dicha lista contiene dos elementos: El primer elemento es el Path.
    #     # Se envía el Path a la caja de textos, para que el usuario sepa que el archivo se seleccionó correctamente.
    #     self.filePathLineEdit.setText(file_path)