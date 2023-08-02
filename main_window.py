import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow

class Ui_MainWindow(object):
    def setup_main_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        # Agregar menú "pacientes"
        self.menu_pacientes = QtWidgets.QMenu(self.menubar)
        self.menu_pacientes.setObjectName("menu_pacientes")
        self.menubar.addAction(self.menu_pacientes.menuAction())

        # Agregar elemento al menú "pacientes"
        self.action_ver_pacientes = QtWidgets.QAction(MainWindow)
        self.action_ver_pacientes.setObjectName("action_ver_pacientes")
        self.menu_pacientes.addAction(self.action_ver_pacientes)

        # Agregar menú "consultas"
        self.menu_consultas = QtWidgets.QMenu(self.menubar)
        self.menu_consultas.setObjectName("menu_consultas")
        self.menubar.addAction(self.menu_consultas.menuAction())

        # Agregar elemento al menú "consultas"
        self.action_ver_consultas = QtWidgets.QAction(MainWindow)
        self.action_ver_consultas.setObjectName("action_ver_consultas")
        self.menu_consultas.addAction(self.action_ver_consultas)

        # Configurar la barra de menú del MainWindow
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Consultorio")
        self.menu_pacientes.setTitle( "Pacientes")
        self.action_ver_pacientes.setText("Ver Pacientes")
        self.menu_consultas.setTitle("Consultas")
        self.action_ver_consultas.setText("Ver Consultas")
        

    
class MainWindowApp(QMainWindow):
    def __init__(self, login_dialog):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup_main_window(self)
        self.login_dialog = login_dialog

    def closeEvent(self, event):
        from login import login
        self.login_dialog.show()
        event.accept()

    

if __name__ == '__main__':
    from login import login
    app = QApplication(sys.argv)
    login_ui = login()
    login_ui.show_login()
    MainWindow = MainWindowApp(login_ui.dialog)  # Pasamos el diálogo de login a la ventana principal
    MainWindow.show()
    sys.exit(app.exec_())