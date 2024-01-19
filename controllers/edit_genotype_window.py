from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.edit_genotype_window import EditGenotypeForm

# Consulta que devuelve la muestra seleccionada por ID
from db.genotype import select_genotype_by_id
# Consulta que actualiza las muestras editadas en esta ventana
from db.genotype import update_genotype
# Mensajes de alerta
from pys2_msgboxes import msg_boxes

class EditGenotypeWindow(QWidget, EditGenotypeForm):
    def __init__(self, parent = None, _id = None):
        # Variable de la clase que recibe el valor pasado por parámetro "_id" 
        #(para poder usar el parámetro en los métodos dentro de la clase)
        self._id = _id 
        super().__init__(parent)
        self.setupUi(self)
        # Crea una nueva ventana, diferente a la de la clase padre
        self.setWindowFlag(Qt.Window)
        # Ejecuta la función 'populate_inputs' cada vez que se ejecuta la ventana
        self.populate_inputs()
        # Enlazamos la señal "clicked" del botón "Editar" con la función edit_genotype
        self.editButton.clicked.connect(self.edit_genotype)
        # Enlazamos el botón de "Cancelar" con una función por defecto (de la ventana) que se llama 'close'
        self.cancelButton.clicked.connect(self.close)

    # Cuando se seleccione una muestra para edición, abre la ventana de edición y va a llenar los inputs con la información
    # para ser modificada.
    def populate_inputs(self):
        # Retorna los datos de la muestra seleccionada
        data = select_genotype_by_id(self._id)

        self.temperature1016LineEdit.setText(data[0][1])
        self.temperature1534LineEdit.setText(data[0][2])
        self.temperature1016SSLineEdit.setText(data[0][3])
        self.temperature1016SRLineEdit.setText(data[0][4])
        self.temperature1016RRLineEdit.setText(data[0][5])
        self.temperature1534SSLineEdit.setText(data[0][6])
        self.temperature1534SRLineEdit.setText(data[0][7])
        self.temperature1534RRLineEdit.setText(data[0][8])

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

    # Función que tendrá la consulta para editar la muestra en la base de datos
    def edit_genotype(self):
        temperature_melting_2016 = self.temperature1016LineEdit.text()
        temperature_melting_1543 = self.temperature1534LineEdit.text()
        temperature_melting_1016_SS = self.temperature1016SSLineEdit.text()
        temperature_melting_1016_SR = self.temperature1016SRLineEdit.text()
        temperature_melting_1016_RR = self.temperature1016RRLineEdit.text()
        temperature_melting_1543_SS = self.temperature1534SSLineEdit.text()
        temperature_melting_1543_SR = self.temperature1534SRLineEdit.text()
        temperature_melting_1543_RR = self.temperature1534RRLineEdit.text()

        data = (temperature_melting_2016, temperature_melting_1543, temperature_melting_1016_SS, temperature_melting_1016_SR, 
                temperature_melting_1016_RR, temperature_melting_1543_SS, temperature_melting_1543_SR, temperature_melting_1543_RR)

        if self.check_inputs(): 
            # Si la función retorna True, entonces significa que no hay errores 
            # (se completaron todos los parámetros obligatorios)
            
            # Pasamos los datos para modificar la muestra a la función perteneciente al archivo genotype.py
            if update_genotype(self._id, data):
                msg_boxes.correct_msgbox("Información", "Correcta edición de una muestra")
                self.close()