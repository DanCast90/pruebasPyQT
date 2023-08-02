import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QVBoxLayout,QTextEdit
import pandas as pd

def main(args):
    app = QApplication(args)
    window = App()
    window.show()
    sys.exit(app.exec_())

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lector de CSV")

        # Crear una caja de selección de archivos
        self.file_box = QLineEdit()
        self.file_box.setPlaceholderText("Selecciona un archivo CSV")

        # Crear un botón para abrir el cuadro de diálogo de selección de archivos
        self.open_button = QPushButton("Abrir")
        self.open_button.clicked.connect(self.open_file)

        # Crear un cuadro de texto para mostrar el JSON
        self.json_box = QTextEdit()
        self.json_box.setReadOnly(True)

        # Crear una tabla para mostrar los datos
        self.table = QTableWidget()
        self.table.setColumnCount(0)

        # Diseñar los widgets en la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.file_box)
        layout.addWidget(self.open_button)
        layout.addWidget(self.table)
        layout.addWidget(self.json_box)
        self.setLayout(layout)

    def open_file(self):
        # Obtener el nombre del archivo desde la caja de selección de archivos
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir archivo CSV", "", "Archivos CSV (*.csv)")

        # Si el usuario seleccionó un archivo, leerlo y mostrar los datos en la tabla
        if filename:
            try:
                # Especificar la codificación (por ejemplo, "Latin-1") utilizada en el archivo CSV
                data = pd.read_csv(filename, encoding="Latin-1")


                if data.empty:
                    return

                data.to_json("text.json",orient="records")
                # Limpiar la tabla antes de cargar nuevos datos
                self.table.setRowCount(0)
                self.table.setColumnCount(len(data.columns))

                # Configurar los nombres de las columnas usando las cabeceras del CSV
                headers = data.columns.tolist()
                self.table.setHorizontalHeaderLabels(headers)

                # Agregar datos a la tabla
                for row in data.values:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)

                    for col, item in enumerate(row):
                        self.table.setItem(row_position, col, QTableWidgetItem(str(item)))

                # Convertir los datos a JSON
                json_data = data.to_json(orient="records")

                # Mostrar los datos JSON en el cuadro de texto
                self.json_box.setPlainText(json_data)

            except Exception as e:
                print(f"Error al leer el archivo CSV: {e}")

if __name__ == "__main__":
    main(sys.argv)
