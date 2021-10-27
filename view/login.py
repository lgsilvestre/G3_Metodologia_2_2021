# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 519)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frameLogin_2 = QtWidgets.QFrame(self.frame)
        self.frameLogin_2.setGeometry(QtCore.QRect(20, 60, 581, 431))
        self.frameLogin_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLogin_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLogin_2.setObjectName("frameLogin_2")
        self.btnConfirm = QtWidgets.QPushButton(self.frameLogin_2)
        self.btnConfirm.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.btnConfirm.setObjectName("btnConfirm")        
        self.frameLogin = QtWidgets.QFrame(self.frameLogin_2)
        self.frameLogin.setGeometry(QtCore.QRect(100, 120, 371, 101))
        self.frameLogin.setAutoFillBackground(True)
        self.frameLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLogin.setObjectName("frameLogin")
        self.label = QtWidgets.QLabel(self.frameLogin)
        self.label.setGeometry(QtCore.QRect(100, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frameLogin)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditUser = QtWidgets.QLineEdit(self.frameLogin)
        self.lineEditUser.setGeometry(QtCore.QRect(160, 30, 131, 20))
        self.lineEditUser.setObjectName("lineEditUser")
        self.lineEditPass = QtWidgets.QLineEdit(self.frameLogin)
        self.lineEditPass.setGeometry(QtCore.QRect(160, 60, 131, 20))
        self.lineEditPass.setObjectName("lineEditPass")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 581, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.superAdminBtn = QtWidgets.QPushButton(self.frame_2)
        self.superAdminBtn.setGeometry(QtCore.QRect(110, 10, 121, 23))
        self.superAdminBtn.setObjectName("superAdminBtn")
        self.userBtn = QtWidgets.QPushButton(self.frame_2)
        self.userBtn.setGeometry(QtCore.QRect(240, 10, 75, 23))
        self.userBtn.setObjectName("userBtn")
        self.adminBtn = QtWidgets.QPushButton(self.frame_2)
        self.adminBtn.setGeometry(QtCore.QRect(0, 10, 91, 23))
        self.adminBtn.setObjectName("adminBtn")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnConfirm.setText(_translate("Dialog", "Confirmar"))
        self.label.setText(_translate("Dialog", "Usuario:"))
        self.label_2.setText(_translate("Dialog", "Contraseña:"))
        self.superAdminBtn.setText(_translate("Dialog", "SuperAdministrador"))
        self.userBtn.setText(_translate("Dialog", "Usuario"))
        self.adminBtn.setText(_translate("Dialog", "Administrador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




