import sys
from UsuarioController import UsuarioController
from mainFunctionsController import mainFunctionsController
from UsuarioController import UsuarioController
from view.login import Ui_Dialog
from view.mainFunctions import mainFunctions
from PyQt5.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui
        self.BtnActions()
        self.show()
    
    def BtnActions(self):
        self.ui.btnConfirm.clicked.connect(self.btnConfirmAction)
        self.ui.pushButton.clicked.connect(self.pushBtnConfirmAction)
        

   
    def btnConfirmAction(self):
        self.close()
        startMainFunctionsController = mainFunctionsController()
        startMainFunctionsController.exec_()

    def pushBtnConfirmAction(self):
        startUsuario = UsuarioController()
        startUsuario.exec_()





if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        
        