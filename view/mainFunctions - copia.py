# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capturar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class mainFunctions(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1109, 567)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frameBigUtilities = QtWidgets.QFrame(self.frame)
        self.frameBigUtilities.setGeometry(QtCore.QRect(500, 0, 551, 531))
        self.frameBigUtilities.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBigUtilities.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBigUtilities.setObjectName("frameBigUtilities")
        self.frameBtns = QtWidgets.QFrame(self.frameBigUtilities)
        self.frameBtns.setGeometry(QtCore.QRect(20, 170, 501, 131))
        self.frameBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBtns.setObjectName("frameBtns")
        self.radioBtnDetect = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnDetect.setGeometry(QtCore.QRect(170, 50, 141, 21))
        self.radioBtnDetect.setObjectName("radioBtnDetect")
        self.frameUseMode = QtWidgets.QFrame(self.frameBtns)
        self.frameUseMode.setGeometry(QtCore.QRect(10, 20, 151, 91))
        self.frameUseMode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameUseMode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUseMode.setObjectName("frameUseMode")
        self.label = QtWidgets.QLabel(self.frameUseMode)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.label.setObjectName("label")
        self.radioBtnSearch = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnSearch.setGeometry(QtCore.QRect(350, 50, 121, 21))
        self.radioBtnSearch.setObjectName("radioBtnSearch")
        self.btnConfirm = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnConfirm.setGeometry(QtCore.QRect(160, 320, 93, 28))
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnCancel = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnCancel.setGeometry(QtCore.QRect(320, 320, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.frameCamera = QtWidgets.QFrame(self.frame)
        self.frameCamera.setGeometry(QtCore.QRect(10, 0, 491, 521))
        self.frameCamera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCamera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCamera.setObjectName("frameCamera")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioBtnDetect.setText(_translate("Dialog", "Detectar rostros"))
        self.label.setText(_translate("Dialog", "Modo de uso"))
        self.radioBtnSearch.setText(_translate("Dialog", "Buscar rostro"))
        self.btnConfirm.setText(_translate("Dialog", "Iniciar"))
        self.btnCancel.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = mainFunctions()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
