import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QVBoxLayout
import csv

def main(args):
    app = QApplication(args)
    window = App()
    window.show()
    sys.exit(app.exec_())

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Reader")

        # Create a file selection box
        self.file_box = QLineEdit()
        self.file_box.setPlaceholderText("Select a CSV file")

        # Create a button to open the file selection dialog
        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_file)

        # Create a table to display the data
        self.table = QTableWidget()
        self.table.setColumnCount(0)

        # Layout the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.file_box)
        layout.addWidget(self.open_button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def open_file(self):
        # Get the filename from the file selection box
        filename, _ = QFileDialog.getOpenFileName(self, "Open CSV file", "", "CSV files (*.csv)")

        # If the user selected a file, read it and populate the table
        if filename:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                data = list(reader)

                if not data:
                    return

                # Limpiar la tabla antes de cargar nuevos datos
                self.table.setRowCount(0)
                self.table.setColumnCount(len(data[0]))

                # Configurar los nombres de las columnas usando la primera fila del CSV
                headers = data[0]
                self.table.setHorizontalHeaderLabels(headers)

                # Agregar los datos a la tabla, omitiendo la primera fila (encabezados)
                for row in data[1:]:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)

                    for col, item in enumerate(row):
                        self.table.setItem(row_position, col, QTableWidgetItem(item))

if __name__ == "__main__":
    main(sys.argv)
