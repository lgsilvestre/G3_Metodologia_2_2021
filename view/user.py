# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class user(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        #self.pushButton = QtWidgets.QPushButton(Dialog)
        #self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        #self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 130, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 101, 20))
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.superAdminBtn = QtWidgets.QPushButton(Dialog)
        self.superAdminBtn.setGeometry(QtCore.QRect(150,200, 75, 23))
        self.superAdminBtn.setObjectName("superAdminBtn")
        self.userBtn = QtWidgets.QPushButton(Dialog)
        self.userBtn.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.userBtn.setObjectName("userBtn")
        self.adminBtn = QtWidgets.QPushButton(Dialog)
        self.adminBtn.setGeometry(QtCore.QRect(70, 200, 75, 23))
        self.adminBtn.setObjectName("adminBtn")
        self.userBtn.setText("Usuario")
        self.adminBtn.setText("Admin")
        self.superAdminBtn.setText("SuperAdmin")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Crear Usuario:"))
        self.label_2.setText(_translate("Dialog", "Crear Contraseña:"))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = user()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
