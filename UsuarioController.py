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
        self.image = None
        self.show()