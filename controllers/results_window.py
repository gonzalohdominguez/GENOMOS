from PySide2.QtWidgets import QWidget, QTableWidgetItem, QFileDialog
from PySide2.QtCore import Qt
import pandas as pd
from views.results_window import ResultsGenotypeForm

from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import matplotlib.pyplot as plt

class ResultsGenotypeWindow(QWidget, ResultsGenotypeForm):
    # Constructor
    def __init__(self, parent = None, table_data=None): 
        super().__init__(parent)
        self.setupUi(self)
        # Crea una nueva ventana, diferente a la de la clase padre
        self.setWindowFlag(Qt.Window)

        # Configurar tamaño mínimo y máximo
        self.setMinimumSize(640, 600)
        self.setMaximumSize(640, 600)

        # Accede a los datos de la tabla en MainWindow
        self.table_data = table_data
        # Llama a la función para convertir a DataFrame
        self.mostrar_resultados_en_tabla()
        # Conectar el botón de descarga con la función 'descargar_resultados'
        self.download_results.clicked.connect(self.descargar_resultados)

    def mostrar_resultados_en_tabla(self):
        # Asumiendo que cada fila de self.table_data representa una fila en la tabla
        # y que la primera fila contiene los encabezados de las columnas
        column_headers = ["ID", "Temp 1016", "Temp 1534", "Temp 1016 SS", "Temp 1016 SR", "Temp 1016 RR", "Temp 1534 SS", "Temp 1534 SR", "Temp 1534 RR"]

        # Crear un DataFrame a partir de los datos de la tabla
        self.df = pd.DataFrame(self.table_data, columns=column_headers)

        # Realizar las operaciones mencionadas
        self.df['Temp 1016'] = pd.to_numeric(self.df['Temp 1016'], errors='coerce')
        self.df['Temp 1534'] = pd.to_numeric(self.df['Temp 1534'], errors='coerce')

        self.df["Temp 1016 SS"] = pd.to_numeric(self.df["Temp 1016 SS"], errors='coerce')
        self.df["Temp 1016 SR"] = pd.to_numeric(self.df["Temp 1016 SR"], errors='coerce')
        self.df["Temp 1016 RR"] = pd.to_numeric(self.df["Temp 1016 RR"], errors='coerce')
        self.df["Temp 1534 SS"] = pd.to_numeric(self.df["Temp 1534 SS"], errors='coerce')
        self.df["Temp 1534 SR"] = pd.to_numeric(self.df["Temp 1534 SR"], errors='coerce')
        self.df["Temp 1534 RR"] = pd.to_numeric(self.df["Temp 1534 RR"], errors='coerce')

        self.df["Resul1016_SS"] = self.df["Temp 1016 SS"] - self.df["Temp 1016"]
        self.df["Resul1016_SR"] = self.df["Temp 1016 SR"] - self.df["Temp 1016"]
        self.df["Resul1016_RR"] = self.df["Temp 1016 RR"] - self.df["Temp 1016"]
        self.df["Resul1534_SS"] = self.df["Temp 1534 SS"] - self.df["Temp 1534"]
        self.df["Resul1534_SR"] = self.df["Temp 1534 SR"] - self.df["Temp 1534"]
        self.df["Resul1534_RR"] = self.df["Temp 1534 RR"] - self.df["Temp 1534"]

        # Eliminar las columnas no necesarias
        self.df.drop(columns=['Temp 1016 SS', 'Temp 1016 SR', 'Temp 1016 RR', 'Temp 1534 SS', 'Temp 1534 SR', 'Temp 1534 RR', 'ID'], inplace=True)

        # Hallar los valores absolutos para cada valor del DataFrame
        df2 = self.df.abs()

        # Crear una lista para almacenar los resultados
        resultados = []
        genotipos_resultantes = []

        # Iterar a través de las filas del DataFrame
        for i,j,SS1016,SR1016,RR1016,SS1534,SR1534,RR1534 in zip(df2['Temp 1016'],df2['Temp 1534'],df2['Resul1016_SS'], df2['Resul1016_SR'], df2['Resul1016_RR'], df2['Resul1534_SS'], df2['Resul1534_SR'], df2['Resul1534_RR']):
            genotipo_1016 = None
            genotipo_1534 = None
            estado_1016 = None
            estado_1534 = None

            if SS1016 < SR1016 and SS1016 < RR1016:
                genotipo_1016 = "Sensitive"
                estado_1016 = "Sensitive"
            elif SR1016 < SS1016 and SR1016 < RR1016:
                genotipo_1016 = "Heterozygous"
                estado_1016 = "Heterozygous"
            elif RR1016 < SS1016 and RR1016 < SR1016:
                genotipo_1016 = "Resistant"
                estado_1016 = "Resistant"

            if SS1534 < SR1534 and SS1534 < RR1534:
                genotipo_1534 = "Sensitive"
                estado_1534 = "Sensitive"
            elif SR1534 < SS1534 and SR1534 < RR1534:
                genotipo_1534 = "Heterozygous"
                estado_1534 = "Heterozygous"
            elif RR1534 < SS1534 and RR1534 < SR1534:
                genotipo_1534 = "Resistant"
                estado_1534 = "Resistant"

            # Resto del código para determinar genotipos y estados

            if genotipo_1016 is not None and genotipo_1534 is not None:
                if genotipo_1016 == "Sensitive" and genotipo_1534 == "Sensitive":
                    genotipo_resultante = "SS"
                elif genotipo_1016 == "Sensitive" and genotipo_1534 == "Heterozygous":
                    genotipo_resultante = "SR1"
                elif genotipo_1016 == "Sensitive" and genotipo_1534 == "Resistant":
                    genotipo_resultante = "R1R1"
                elif genotipo_1016 == "Heterozygous" and genotipo_1534 == "Sensitive":
                    genotipo_resultante = "SR3"
                elif genotipo_1016 == "Heterozygous" and genotipo_1534 == "Heterozygous":
                    genotipo_resultante = "SR2"
                elif genotipo_1016 == "Heterozygous" and genotipo_1534 == "Resistant":
                    genotipo_resultante = "R1R2"
                elif genotipo_1016 == "Resistant" and genotipo_1534 == "Heterozygous":
                    genotipo_resultante = "R2R3"
                elif genotipo_1016 == "Resistant" and genotipo_1534 == "Sensitive":
                    genotipo_resultante = "R3R3"
                elif genotipo_1016 == "Resistant" and genotipo_1534 == "Resistant":
                    genotipo_resultante = "R2R2"
                else:
                    genotipo_resultante = "Unknown"

                resultados.append((i, j, estado_1016, estado_1534, genotipo_resultante))
                genotipos_resultantes.append(genotipo_resultante)
            else:
                resultados.append((i, j, "Could not be determined", "Unknown", "Unknown"))
                genotipos_resultantes.append("Could not be determined")

        # Crear un nuevo DataFrame con los resultados
        resultados_df = pd.DataFrame(resultados, columns=["Tm_1016", "Tm_1534", "Estado_1016", "Estado_1534", "Genotipo_Resultante"])

        # Mostrar el DataFrame en la tabla
        self.mostrar_df_en_tabla(resultados_df)

        # Ver gráficos
        self.generar_grafico(resultados_df, genotipos_resultantes)

    def generar_grafico(self, df, genotipos_resultantes):
        # Lista de genotipos que deseas mostrar en el gráfico de barras
        categorias_especificas = ["SS", "SR1", "SR2", "SR3", "R1R1", "R1R2", "R2R3", "R3R3", "R2R2"]

        # Definir los colores correspondientes a cada genotipo
        colores = ["green", "orange", "darkorange", "blue", "red", "lightcoral", "lightseagreen", "violet", "firebrick"]

        # Obtener las cantidades correspondientes a los genotipos específicos encontrados en los datos
        cantidades_genotipos = [genotipos_resultantes.count(genotipo) for genotipo in categorias_especificas]

        # Filtrar genotipos y cantidades para excluir los que tienen 0 muestras
        genotipos_filtrados = []
        cantidades_filtradas = []
        colores_filtrados = []

        for genotipo, cantidad, color in zip(categorias_especificas, cantidades_genotipos, colores):
            if cantidad > 0:
                genotipos_filtrados.append(genotipo)
                cantidades_filtradas.append(cantidad)
                colores_filtrados.append(color)

        # Crear el gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(genotipos_filtrados, cantidades_filtradas, color=colores_filtrados)
        plt.xlabel("Genotype")
        plt.ylabel("Percentage")
        plt.title("Genotype Distribution")

        # Agregar una leyenda de colores
        handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colores_filtrados]
        plt.legend(handles, genotipos_filtrados, title="Genotypes")

        plt.xticks(rotation=45)

        # Mostrar el gráfico
        plt.show()

        # Definir las sílabas a contar
        sílabas = ["S", "R1", "R2", "R3"]

        # Inicializar un diccionario para almacenar el recuento de sílabas
        recuento_sílabas = {sílaba: [] for sílaba in sílabas}

        # Seleccionar solo la columna "Genotipo_Resultante" de resultados_df
        genotipo_resultante_df = df[["Genotipo_Resultante"]]

        # Iterar a través de las filas de genotipo_resultante_df y contar las sílabas
        for genotipo in genotipo_resultante_df["Genotipo_Resultante"]:
            for sílaba in sílabas:
                recuento_sílabas[sílaba].append(genotipo.count(sílaba))

        # Crear un nuevo DataFrame a partir del diccionario de recuento de sílabas
        recuento_sílabas_df = pd.DataFrame(recuento_sílabas)

        # Crear una lista con los nombres de las columnas de interés
        columnas_interes = ["S", "R1", "R2", "R3"]

        # Inicializar la lista "Suma alelos" como una lista vacía
        suma_alelos = []

        # Iterar a través de las columnas y calcular la suma de cada alelo
        for columna in columnas_interes:
            suma = recuento_sílabas_df[columna].sum()
            suma_alelos.append((columna, suma))  # Agregar el nombre del alelo junto con la suma a la lista

        # Extraer los nombres de los alelos y sus sumas
        nombres_alelos = [alelo[0] for alelo in suma_alelos if alelo[1] > 0]
        sumas = [alelo[1] for alelo in suma_alelos if alelo[1] > 0]

        # Colores correspondientes a cada alelo
        colores = ['green', 'orange', 'red', 'blue']

        # Crear el gráfico de torta con colores personalizados
        plt.figure(figsize=(8, 8))
        plt.pie(sumas, labels=nombres_alelos, colors=colores, autopct='%1.1f%%', startangle=140)
        plt.title('Allele Sum Distribution')
        plt.axis('equal')  # Para que el gráfico sea un círculo perfecto

        # Mostrar el gráfico
        plt.show()


    def mostrar_df_en_tabla(self, df):
        # Limpiar la tabla actual
        self.tableResults.setRowCount(0)
        self.tableResults.setColumnCount(0)

        # Configurar la tabla con las columnas del DataFrame
        self.tableResults.setColumnCount(len(df.columns))
        self.tableResults.setRowCount(len(df))

        # Agregar encabezados
        self.tableResults.setHorizontalHeaderLabels(df.columns)

        # Rellenar la tabla con datos del DataFrame
        for row in range(len(df)):
            for col in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.tableResults.setItem(row, col, item)

    def descargar_resultados(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save file", "", "Excel files (*.xlsx)", options=options
        )

        if file_name:
            # Verificar el tipo de archivo seleccionado
            if file_name.endswith('.xlsx'):
                self.export_to_excel(file_name)
            else:
                print("Unsupported file format. Please use Excel files (.xlsx)")
        
    
    def export_to_excel(self, file_name):
        # Obtener datos de la tabla
        data = []
        for row in range(self.tableResults.rowCount()):
            data.append([self.tableResults.item(row, col).text() for col in range(self.tableResults.columnCount())])

        # Crear un DataFrame de Pandas
        df = pd.DataFrame(data, columns=["Tm_1016", "Tm_1534", "Estado_1016", "Estado_1534", "Genotipo_Resultante"])

        # Escribir el DataFrame en un archivo Excel
        df.to_excel(file_name, index=False)