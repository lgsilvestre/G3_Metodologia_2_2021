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
        Dialog.resize(1109, 559)
        Dialog.setMinimumSize(QtCore.QSize(1109, 0))
        Dialog.setStyleSheet("Background-Color: rgb(0, 0, 0);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("Background-Color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frameBigUtilities = QtWidgets.QFrame(self.frame)
        self.frameBigUtilities.setGeometry(QtCore.QRect(480, 0, 611, 541))
        self.frameBigUtilities.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frameBigUtilities.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBigUtilities.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBigUtilities.setObjectName("frameBigUtilities")
        self.frameBtns = QtWidgets.QFrame(self.frameBigUtilities)
        self.frameBtns.setGeometry(QtCore.QRect(30, 0, 571, 531))
        self.frameBtns.setStyleSheet("QFrame {\n"
"    Background-color:rgb(25, 25, 25);\n"
"    border-style: outset;\n"
"    border-radius: 15px;\n"
"\n"
"    \n"
"}")
        self.frameBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBtns.setObjectName("frameBtns")
        self.radioBtnDetect = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnDetect.setGeometry(QtCore.QRect(50, 120, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioBtnDetect.setFont(font)
        self.radioBtnDetect.setStyleSheet("QRadioButton {\n"
"    Color: White;\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/ui/images/detectar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioBtnDetect.setIcon(icon)
        self.radioBtnDetect.setObjectName("radioBtnDetect")
        self.frameUseMode = QtWidgets.QFrame(self.frameBtns)
        self.frameUseMode.setGeometry(QtCore.QRect(30, 20, 511, 71))
        self.frameUseMode.setStyleSheet("QFrame\n"
"{\n"
"    background-color:qlineargradient(spread:pad, x1:1, y1:0.733318, x2:1, y2:0, stop:0.380682 rgba(152, 22, 22, 255), stop:1 rgba(77, 0, 0, 255));\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"\n"
"}")
        self.frameUseMode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameUseMode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUseMode.setObjectName("frameUseMode")
        self.label = QtWidgets.QLabel(self.frameUseMode)
        self.label.setGeometry(QtCore.QRect(10, 0, 260,81))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("Color: rgb(176, 176, 176);")
        self.label.setObjectName("label")
        self.radioBtnSearch = QtWidgets.QRadioButton(self.frameBtns)
        self.radioBtnSearch.setGeometry(QtCore.QRect(50, 170, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioBtnSearch.setFont(font)
        self.radioBtnSearch.setStyleSheet("Color: White;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/ui/images/reconocer.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioBtnSearch.setIcon(icon1)
        self.radioBtnSearch.setObjectName("radioBtnSearch")
        self.groupBox = QtWidgets.QGroupBox(self.frameBtns)
        self.groupBox.setGeometry(QtCore.QRect(40, 240, 600, 81))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"        border-radius: 10px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("Color: White;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 30, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("Color: White;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(390, 30, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("Color: White;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.btnConfirm = QtWidgets.QPushButton(self.frameBtns)
        self.btnConfirm.setGeometry(QtCore.QRect(60, 400, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.btnConfirm.setFont(font)
        self.btnConfirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirm.setStyleSheet("QPushButton \n"
"{\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    background-color:rgb(24, 127, 49);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(113, 226, 96);\n"
"}\n"
"    ")
        self.btnConfirm.setObjectName("btnConfirm")
        self.btnCancel = QtWidgets.QPushButton(self.frameBtns)
        self.btnCancel.setGeometry(QtCore.QRect(370, 400, 142, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnCancel.setFont(font)
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("QPushButton \n"
"{\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"   background-color:rgb(152, 22, 22);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgb(255, 103, 105);\n"
"}\n"
"\n"
"    ")
        self.btnCancel.setObjectName("btnCancel")
        self.video = QtWidgets.QLabel(self.frame)
        self.video.setGeometry(QtCore.QRect(-10, 0, 511, 541))
        self.video.setText("")
        self.video.setPixmap(QtGui.QPixmap("view/ui/images/fondo.jpg"))
        self.video.setScaledContents(True)
        self.video.setWordWrap(False)
        self.video.setObjectName("video")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioBtnDetect.setText(_translate("Dialog", "Detectar rostros con busqueda de patrones"))
        self.label.setText(_translate("Dialog", "Seleccione una acción:"))
        self.radioBtnSearch.setText(_translate("Dialog", "Buscar rostro"))
        self.radioButton.setText(_translate("Dialog", "IA"))
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
