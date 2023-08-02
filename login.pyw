from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog

import sys
from database_instance import *

class login(object):
    def setup_ui(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(309, 335)
        self.login_window = QtWidgets.QWidget(MainWindow)
        self.login_window.setObjectName("login_window")
        self.gridLayoutWidget = QtWidgets.QWidget(self.login_window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 271, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.input_usuario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_usuario.setObjectName("input_usuario")
        self.gridLayout.addWidget(self.input_usuario, 0, 1, 1, 1)
        self.input_pass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass.setObjectName("input_pass")
        self.gridLayout.addWidget(self.input_pass, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.login_window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 9, 211, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.login_window)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 200, 231, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_ingresar = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.gridLayout_2.addWidget(self.btn_ingresar, 0, 1, 1, 1)
        MainWindow.setWindowTitle("MainWindow")
        self.label_2.setText("Usuario")
        self.label_3.setText("Contraseña")
        self.label.setText("Inicio de Sesión")
        self.btn_ingresar.setText("Ingresar")
    
        self.btn_ingresar.clicked.connect(self.on_btn_ingresar_clicked)

    def on_btn_ingresar_clicked(self):
        db=database_conection()
        connector=db.connect()
        servs_login=login_db_services()
        flag_login=servs_login.check_user(connector,self.input_usuario.text(),self.input_pass.text())
        connector.close()
        if(flag_login):
            QtWidgets.QMessageBox.information(self.MainWindow, "Ingreso", "Ingreso exitoso")
            self.input_usuario.clear()
            self.input_pass.clear()
            sys.path.append(".")
            self.MainWindow.close()
            from main_window import MainWindowApp
            # Abrir ventana principal (MainWindow)
            self.main_window = MainWindowApp(self.dialog)
            self.main_window.show()
        else:
            QtWidgets.QMessageBox.information(self.MainWindow, "Error", "Usuario y/o contraseña no validos")
    
    def show_login(self):
        self.dialog = QDialog()  # Mantenemos una referencia al diálogo
        self.setup_ui(self.dialog)
        self.dialog.show()
        
class login_db_services():

    def check_user(self,connector,username,password):
        rows=connector.execute("SELECT * FROM user WHERE username = ? and password = ?", (username,password)).fetchall()
        if(len(rows)==0):
            return False
        else:
            return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = login()
    login_ui.show_login()
    sys.exit(app.exec_())