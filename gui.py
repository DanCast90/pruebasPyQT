import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the label
        self.label = QLabel("Hello, world!")

        # Create the button
        self.button = QPushButton("Click me!")

        # Set the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # Set the central widget
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)

        # Connect the button to the click event
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("You clicked the button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MainWindow()

    # Show the main window
    main_window.show()

    sys.exit(app.exec_())
