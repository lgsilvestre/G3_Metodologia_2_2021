import sys
from view.mainFunctions import mainFunctions
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import CamaraTest 

class mainFunctionsController(QDialog):
    def __init__(self):
        super(mainFunctionsController, self).__init__()
        self.ui = mainFunctions()
        self.ui.setupUi(self)
        self.BtnActions()
        self.show()
    
    def BtnActions(self):
        self.ui.btnConfirm.clicked.connect(self.btnConfirmAction)
        self.ui.btnCancel.clicked.connect(self.btnCancelAction)

        
    def btnConfirmAction(self):
        print("confirm")
        CamaraTest.iniciarCaptura(True)
        print("sexual prodigy")
       
       
        
    def btnCancelAction(self):
        print("cancel")

        
      
       

