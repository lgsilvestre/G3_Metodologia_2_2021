import sys
from UsuarioController import UsuarioController
from mainFunctionsController import mainFunctionsController
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
        with open("Cuentas.txt","r") as f:
            for line in f:
                if "," in line:
                    separacion = line.split(",")
                    User = separacion[0]
                    final_User = User.translate({ord("\n"):None})
                    compUser = self.ui.lineEditUser.text()
                    compPass = self.ui.lineEditPass.text()
                    if compUser == final_User:
                        with open("Cuentas.txt","r") as h:
                            for line in h:
                                if "," in line:
                                    separacion = line.split(",")
                                    Pass = separacion[1]
                                    final_Pass = Pass.translate({ord("\n"):None})
                                    compPass = self.ui.lineEditPass.text()
                                    if compPass == final_Pass:
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
        
        