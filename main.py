import sys
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
        self.BtnActions()
        self.show()
    
    def BtnActions(self):
        self.ui.btnConfirm.clicked.connect(self.btnConfirmAction)

    #Call new QDialog called mainFunctions.py and show it to the user
    def btnConfirmAction(self):
        self.close()
        startMainFunctionsController = mainFunctionsController()
        startMainFunctionsController.exec_()

    

        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
        
        