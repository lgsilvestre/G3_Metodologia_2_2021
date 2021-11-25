from view.user import user
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog


class UsuarioController(QDialog):
    def __init__(self):
        super(UsuarioController, self).__init__()
        self.ui = user()
        self.ui.setupUi(self)
        self.btnActions()
        self.show()

    def btnActions(self):
        self.ui.pushButton.clicked.connect(self.pushAction)

    def pushAction(self):
        User = self.ui.lineEdit_2.text()
        Pass = self.ui.lineEdit.text()
        if (User and Pass):
            with open('Cuentas.txt','a') as f:
                f.write(User)
                f.write(",")
                f.write(Pass)
                f.write('\n')
                f.close()
        self.close()
