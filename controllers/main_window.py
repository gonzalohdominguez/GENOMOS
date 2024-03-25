# Importamos clase Widget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
# Importamos clase del View
from views.main_window import ListGenotypeForm
# Importamos la función de /db/genotype.py que consulta por todas las muestras y las retorna
from db.genotype import select_all_genotypes
# Importamos la función que elimina todos los datos de la tabla
from db.genotype import delete_all_genotypes
# Importamos la función que incorpora todos los datos de la tabla
from db.genotype import insert_genotype
# Importamos la función que elimina una muestra determinada
from db.genotype import delete_genotype

# Uso de dataframes y series
import pandas as pd
import openpyxl
# Para importar o exportar archivos
from PySide2.QtWidgets import QFileDialog

# Scripts para búsquedas
from db.genotype import select_genotype_by_id, select_genotype_by_temperature_melting_1016, select_genotype_by_temperature_melting_1534

# Mensajes de alerta
from pys2_msgboxes import msg_boxes

# Icono
from PySide2.QtGui import QIcon

class ListGenotypeWindow(QWidget,ListGenotypeForm):
    # Constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Configuración del ícono
        icono_ventana = 'pys2_msgboxes/icons/icono.png'
        q_icon = QIcon(icono_ventana)
        self.setWindowIcon(q_icon)

        # Configurar tamaño mínimo y máximo
        self.setMinimumSize(1098, 664)
        self.setMaximumSize(1098, 664)

        # Enlazamos la señal "clicked" del botón "Nueva Muestra" con la función open_new_genotype_window
        self.open_new_button.clicked.connect(self.open_new_genotype_window)
        # Enlazamos la señal "clicked" del botón "Editar Muestra" con la función open_edit_genotype_window
        self.open_edit_button.clicked.connect(self.open_edit_genotype_window)
        # Enlazamos la señal "clicked" del botón "Resultados" con la función results_genotype_window
        self.tabla_resultante_button.clicked.connect(self.results_genotype_window)
        # Eliminamos los valores actuales de la tabla, tanto en la base de datos como en listGenotypeTable
        self.remove_all_genotypes()
        # Enlazamos la señal "clicked" del botón "Eliminar datos" con la función remove_all_genotypes
        self.delete_datos.clicked.connect(self.remove_all_genotypes)
        # Configuración de la tabla de entrada
        self.table_config()
        # Enlazamos la función 'populate_table' con la función que se encuentra en la carpeta /db/genotype.py que consulta por todas las muestras y retorna todas
        self.populate_table(select_all_genotypes())
        # Enlazamos 'populate_combobox' con las opciones de búsqueda determinada por el Combobox 1
        self.populate_combobox()
        # Actualiza la tabla
        self.refreshButton.clicked.connect(lambda: self.populate_table(select_all_genotypes()))
        # Enlazamos la función open_data_file con el botón "Agregar datos"
        self.abrir_archivo_excel.clicked.connect(self.open_data_file)
        # Enlazamos el botón de exportar datos con la función 'export_table'
        self.guardar_archivo_excel.clicked.connect(self.export_table)
        # Enlazamos la función 'search' con el botón "Buscar"
        self.searchButton.clicked.connect(self.search)
        # Enlazamos la función 'remove_genotype' con el botón "Eliminar"
        self.delete_genotype_button.clicked.connect(self.remove_genotype)
        # Enlazamos la función 'open_informacion_window' con el botón "Información"
        self.info_genotype_button.clicked.connect(self.open_informacion_window)

    # Ventana de Información
    def open_informacion_window(self):
        from controllers.information_window import InformationGenotypeWindow
        window = InformationGenotypeWindow(self)
        window.show()

    # Nueva Muestra
    def open_new_genotype_window(self):
        # Creamos y mostramos NewGenotypeWindow cuando se hace clic en el botón
        from controllers.new_genotype_window import NewGenotypeWindow
        window = NewGenotypeWindow(self)
        window.show()

    # Resultados
    def results_genotype_window(self):
        # Creamos y mostramos NewGenotypeWindow cuando se hace clic en el botón
        from controllers.results_window import ResultsGenotypeWindow
        # Obtén los datos de la tabla
        table_data = self.get_table_data()
        # Creamos y mostramos ResultsGenotypeWindow cuando se hace clic en el botón
        if table_data:
            window = ResultsGenotypeWindow(self, table_data)
            window.show()
        else:
            msg_boxes.input_error_msgbox("Error", "Results cannot be displayed because the table is empty.")

    # Agrega una función para obtener los datos de la tabla
    def get_table_data(self):
        # Verifica que haya datos en la tabla
        table_data = []
        for row in range(self.listGenotypeTable.rowCount()):
            row_data = [self.listGenotypeTable.item(row, col).text() for col in range(self.listGenotypeTable.columnCount())]
            table_data.append(row_data)

        return table_data

    # Editar Muestra
    def open_edit_genotype_window(self):
        # Creamos y mostramos EditGenotypeWindow cuando se hace clic en el botón
        from controllers.edit_genotype_window import EditGenotypeWindow

        # Obtenemos los datos de la fila seleccionada
        selected_row = self.listGenotypeTable.selectedItems()
        if selected_row: # Si hay una fila seleccionada
            genotype_id = int(selected_row[0].text()) # Almacena el ID de la muestra
            # Abre la ventana sólo si se selecciona una fila
            window = EditGenotypeWindow(self, genotype_id)
            window.show()
        else:
            msg_boxes.input_error_msgbox("Error", "The sample to edit was not selected.")

        # Luego de editar, se deselecciona la fila que anteriormente estaba selecciona 
        self.listGenotypeTable.clearSelection()


    # Eliminar Muestra
    def remove_genotype(self):
        selected_row = self.listGenotypeTable.selectedItems()
        resp = msg_boxes.warging_msgbox("Delete Sample", "Are you sure you want to delete this sample?")
        if resp == QMessageBox.Yes:
            if selected_row: # Si hay alguna fila seleccionada
                genotype_id = int(selected_row[0].text())
                # Obtiene el objeto de la fila seleccionada
                row = selected_row[0].row()

                # Eliminamos la muestra de la base de datos
                if delete_genotype(genotype_id):
                    # Eliminamos la fila de la tabla
                    self.listGenotypeTable.removeRow(row)

            self.records_qty()

    # Eliminar todos los datos de la tabla
    def remove_all_genotypes(self):
        # Eliminar todos los datos de la base de datos
        delete_all_genotypes()
        # Limpiar el contenido de las celdas en la tabla
        self.listGenotypeTable.clearContents()
        # Establecer el número de filas en 0
        self.listGenotypeTable.setRowCount(0)        

    # Configuración de la tabla de entrada
    def table_config(self):
        column_headers = ("ID", "Temp 1016", "Temp 1534", "Temp 1016 SS", "Temp 1016 SR", "Temp 1016 RR", "Temp 1534 SS", "Temp 1534 SR", "Temp 1534 RR")
        self.listGenotypeTable.setColumnCount(len(column_headers))
        self.listGenotypeTable.setHorizontalHeaderLabels(column_headers)

        # Cuando se selecciona una celda, se selecciona toda la fila
        self.listGenotypeTable.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Incorporar datos a la tabla
    def populate_table(self, data):
        self.listGenotypeTable.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listGenotypeTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

        self.listGenotypeTable.setSortingEnabled(True)
        self.records_qty()

    # Cuantificar registros
    def records_qty(self):
        # Retorna la cantidad de registros de la tabla 'listGenotypeTable'
        qty_rows = str(self.listGenotypeTable.rowCount())
        # Lo convertimos a string para poder enviar este valor al label 
        self.genotypesQtyLabel.setText(qty_rows)

    # Importación de un archivo Excel o CSV para cargar en la tabla
    def open_data_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open data file", "", "Excel files (*.xlsx);;CSV files (*.csv)", options=options)

        if file_name:
            # Verificar el tipo de archivo
            if file_name.endswith('.xlsx'):
                # Leer datos desde el archivo Excel
                data = pd.read_excel(file_name)
            elif file_name.endswith('.csv'):
                # Leer datos desde el archivo CSV
                data = pd.read_csv(file_name)
            else:
                msg_boxes.input_error_msgbox("Unsupported file format", "Please use Excel files (.xlsx) or CSV files (.csv).")
                return

            # Verificar exactamente ocho columnas y los nombres de las columnas
            expected_columns = [
                "temperature_melting_1016",
                "temperature_melting_1534",
                "temperature_melting_1016_SS",
                "temperature_melting_1016_SR",
                "temperature_melting_1016_RR",
                "temperature_melting_1534_SS",
                "temperature_melting_1534_SR",
                "temperature_melting_1534_RR"
            ]

            if len(data.columns) == len(expected_columns) and all(data.columns == expected_columns):
                # Limpiar la tabla actual
                self.remove_all_genotypes()
                # Configurar la tabla
                self.table_config()
                # Mostrar datos en la tabla
                self.show_data_in_table(data)
                # Almacenar datos en la base de datos
                self.store_data_in_database(data)
                msg_boxes.correct_msgbox("Verification","Data stored correctly")

            else:
                msg_boxes.input_error_msgbox("Error", "The file must contain exactly eight columns with the correct names.")

    def show_data_in_table(self, data):
        # Llenar la tabla con los nuevos datos
        self.populate_table(data)

    # Acceder a la base de datos y almacenar los datos
    def store_data_in_database(self, data):
        # Eliminar todos los datos de la base de datos antes de insertar los nuevos datos
        delete_all_genotypes()
        for _, row in enumerate(data.iterrows(), start=1):
            # Obtener los valores de todas las columnas como lista
            values_list = list(row[1])

            # Convertir la lista a tupla
            values = tuple(values_list)

            # Llamada a la función para insertar en la base de datos
            insert_genotype(values)

        # Obtener los datos actualizados después de la inserción
        updated_data = select_all_genotypes()

        # Llenar la tabla con los nuevos datos
        self.populate_table(updated_data)

    # Exportación de un archivo Excel o CSV de los datos de la tabla
    def export_table(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save file", "", "Excel files (*.xlsx);;CSV files (*.csv)", options=options
        )

        if file_name:
            # Verificar el tipo de archivo seleccionado
            if file_name.endswith('.xlsx'):
                self.export_to_excel(file_name)
                msg_boxes.correct_msgbox("Verification","Excel file exported successfully.")
            elif file_name.endswith('.csv'):
                self.export_to_csv(file_name)
                msg_boxes.correct_msgbox("Verification","CSV file exported successfully.")
            else:
                msg_boxes.input_error_msgbox("Unsupported file format.", "Please use Excel files (.xlsx) or CSV files (.csv).")

    def export_to_excel(self, file_name):
        # Obtener datos de la tabla
        data = []
        for row in range(self.listGenotypeTable.rowCount()):
            data.append([self.listGenotypeTable.item(row, col).text() for col in range(self.listGenotypeTable.columnCount())])

        # Crear un DataFrame de Pandas
        df = pd.DataFrame(data, columns=["ID", "Temp 1016", "Temp 1534", "Temp 1016 SS", "Temp 1016 SR", "Temp 1016 RR", "Temp 1534 SS", "Temp 1534 SR", "Temp 1534 RR"])

        # Escribir el DataFrame en un archivo Excel
        df.to_excel(file_name, index=False)

    def export_to_csv(self, file_name):
        # Obtener datos de la tabla
        data = []
        for row in range(self.listGenotypeTable.rowCount()):
            data.append([self.listGenotypeTable.item(row, col).text() for col in range(self.listGenotypeTable.columnCount())])

        # Crear un DataFrame de Pandas
        df = pd.DataFrame(data, columns=["ID", "Temp 1016", "Temp 1534", "Temp 1016 SS", "Temp 1016 SR", "Temp 1016 RR", "Temp 1534 SS", "Temp 1534 SR", "Temp 1534 RR"])

        # Escribir el DataFrame en un archivo CSV
        df.to_csv(file_name, index=False)

    # ---------------------------------------------- Búsquedas ----------------------------------------------
    def populate_combobox(self):
        cb_options = ("", "ID", "Temperature 1016", "Temperature 1534")
        self.searchByCombobox.addItems(cb_options)

    def search_genotype_by_id(self, _id):
        data = select_genotype_by_id(_id)
        # Incorporar datos filtrados a la tabla
        self.populate_table(data)

    def search_genotype_by_temperature_melting_1016(self, temperature):
        data = select_genotype_by_temperature_melting_1016(temperature)
        # Incorporar datos filtrados a la tabla
        self.populate_table(data)

    def search_genotype_by_temperature_melting_1534(self, temperature):
        data = select_genotype_by_temperature_melting_1534(temperature)
        # Incorporar datos filtrados a la tabla
        self.populate_table(data)

    def search(self):
        # Obtenemos el dato que actualmente está seleccionado en el objeto searchByCombobox
        option_selected = self.searchByCombobox.currentText()
        # Obtenemos el parámetro por el cual el usuario quiere buscar
        parameter = self.parameterLineEdit.text()
        if option_selected == "":
            msg_boxes.input_error_msgbox("Error", "You must select an option.")
        else:
            if parameter == "":
                msg_boxes.input_error_msgbox("Error", "You must write what you want to inquire.")
            else: 
                # Si searchByCombobox no está vacio ni parameterLineEdit está vacio
                if option_selected == "ID":
                    self.search_genotype_by_id(parameter)
                elif option_selected == "Temperature 1016":
                    self.search_genotype_by_temperature_melting_1016(parameter)
                elif option_selected == "Temperature 1534":
                    self.search_genotype_by_temperature_melting_1534(parameter)
