<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFunctions.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class mainFunctions(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 567)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("Background-Color: #363636;")
        self.frameBigUtilities = QtWidgets.QFrame(self.frame)
        self.frameBigUtilities.setGeometry(QtCore.QRect(500, 0, 551, 531))
        self.frameBigUtilities.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBigUtilities.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBigUtilities.setObjectName("frameBigUtilities")
        self.frameBtns = QtWidgets.QFrame(self.frameBigUtilities)
        self.frameBtns.setGeometry(QtCore.QRect(20, 170, 501, 50))
        self.frameBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBtns.setObjectName("frameBtns")
        self.frameBtns.setStyleSheet("Background-color: #423C3C;")
        self.radioBtnDetect = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnDetect.setGeometry(QtCore.QRect(170, 20, 141, 21))
        self.radioBtnDetect.setObjectName("radioBtnDetect")
        self.radioBtnDetect.setStyleSheet("Color: White;")
        self.frameUseMode = QtWidgets.QFrame(self.frameBtns)
        self.frameUseMode.setGeometry(QtCore.QRect(10, -10, 151, 91))
        self.frameUseMode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameUseMode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUseMode.setObjectName("frameUseMode")
        self.frameUseMode.setStyleSheet("Color: White;")
        self.label = QtWidgets.QLabel(self.frameUseMode)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.label.setObjectName("label")
        self.radioBtnSearch = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnSearch.setGeometry(QtCore.QRect(350, 20, 121, 21))
        self.radioBtnSearch.setObjectName("radioBtnSearch")
        self.radioBtnSearch.setStyleSheet("Color: White;")
        self.btnConfirm = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnConfirm.setGeometry(QtCore.QRect(160, 320, 93, 28))
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnConfirm.setStyleSheet("Background-color: #4D4845;" "Color:White;")
        self.btnCancel = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnCancel.setGeometry(QtCore.QRect(320, 320, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.btnCancel.setStyleSheet("Background-color: #4D4845;" "Color:White;")
        self.video = QtWidgets.QLabel(self.frame)
        self.video.setGeometry(QtCore.QRect(0, 0, 481, 531))
        self.video.setText("")
        self.video.setObjectName("video")
        self.video.setFrameShape(QtWidgets.QFrame.Box)
        self.video.setFrameShadow(QtWidgets.QFrame.Raised)
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
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFunctions.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.frameBigUtilities.setGeometry(QtCore.QRect(480, 10, 551, 531))
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
        self.groupBox = QtWidgets.QGroupBox(self.frameBtns)
        self.groupBox.setGeometry(QtCore.QRect(40, 100, 451, 31))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 10, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(310, 10, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.btnConfirm = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnConfirm.setGeometry(QtCore.QRect(160, 320, 93, 28))
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnCancel = QtWidgets.QPushButton(self.frameBigUtilities)
        self.btnCancel.setGeometry(QtCore.QRect(320, 320, 93, 28))
        self.btnCancel.setObjectName("btnCancel")
        self.video = QtWidgets.QLabel(self.frame)
        self.video.setGeometry(QtCore.QRect(0, 0, 481, 531))
        self.video.setText("")
        self.video.setObjectName("video")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioBtnDetect.setText(_translate("Dialog", "Detectar rostros"))
        self.label.setText(_translate("Dialog", "Modo de uso"))
        self.radioBtnSearch.setText(_translate("Dialog", "Buscar rostro"))
        self.radioButton.setText(_translate("Dialog", "Algoritmo 1"))
        self.radioButton_2.setText(_translate("Dialog", "Algoritmo 2"))
        self.radioButton_3.setText(_translate("Dialog", "Algoritmo 3"))
        self.btnConfirm.setText(_translate("Dialog", "Iniciar"))
        self.btnCancel.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
>>>>>>> origin/test
