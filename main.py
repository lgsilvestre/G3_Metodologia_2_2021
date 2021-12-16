from os import truncate
import sys
from UsuarioController import UsuarioController
from mainFunctionsController import mainFunctionsController
import sys, os
from controllers.mainFunctionsController import mainFunctionsController
from view.login import Ui_Dialog
from view.mainFunctions import mainFunctions
from PyQt5.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
application_path = os.path.dirname(os.path.abspath(sys.executable))

import glob
import os
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller import compat

hiddenimports = ['numpy'] 

# On Windows, make sure that opencv_videoio_ffmpeg*.dll is bundled
binaries = []
if compat.is_win:
    # If conda is active, look for the DLL in its library path
    if compat.is_conda:
        libdir = os.path.join(compat.base_prefix, 'Library', 'bin')
        pattern = os.path.join(libdir, 'opencv_videoio_ffmpeg*.dll')
        for f in glob.glob(pattern):
            binaries.append((f, '.'))

    # Include any DLLs from site-packages/cv2 (opencv_videoio_ffmpeg*.dll
    # can be found there in the PyPI version)
    
    binaries += collect_dynamic_libs('cv2')
    

    
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.BtnActions()
        self.show()
    
    def BtnActions(self):
        self.ui.userBtn.clicked.connect(lambda:self.confirmOption(0))
        self.ui.adminBtn.clicked.connect(lambda:self.confirmOption(1))
        self.ui.superAdminBtn.clicked.connect(lambda:self.confirmOption(2))

        #Creacion de usuario
        self.ui.pushButton.clicked.connect(self.pushBtnConfirmAction)
        

    def confirmOption(self,checked):
        if(checked == 0):
            self.ui.btnConfirm.clicked.connect(self.btnConfirmActionUser)
        elif(checked == 1):
            self.ui.btnConfirm.clicked.connect(self.btnConfirmActionAdmin)
        elif(checked == 2):
            self.ui.btnConfirm.clicked.connect(self.btnConfirmActionSuperAdmin)
   
    def btnConfirmActionUser(self):
        with open("CuentasUser.txt","r") as f:
            for line in f:
                if "," in line:
                    separacion = line.split(",")
                    User = separacion[0]
                    final_User = User.translate({ord("\n"):None})
                    compUser = self.ui.lineEditUser.text()
                    compPass = self.ui.lineEditPass.text()
                    if compUser == final_User:
                        with open("CuentasUser.txt","r") as h:
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

    def btnConfirmActionAdmin(self):
        with open("CuentasAdmin.txt","r") as f:
            for line in f:
                if "," in line:
                    separacion = line.split(",")
                    User = separacion[0]
                    final_User = User.translate({ord("\n"):None})
                    compUser = self.ui.lineEditUser.text()
                    compPass = self.ui.lineEditPass.text()
                    if compUser == final_User:
                        with open("CuentasAdmin.txt","r") as h:
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

    def btnConfirmActionSuperAdmin(self):
        with open("CuentasSuperAdmin.txt","r") as f:
            for line in f:
                if "," in line:
                    separacion = line.split(",")
                    User = separacion[0]
                    final_User = User.translate({ord("\n"):None})
                    compUser = self.ui.lineEditUser.text()
                    compPass = self.ui.lineEditPass.text()
                    if compUser == final_User:
                        with open("CuentasSuperAdmin.txt","r") as h:
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
        
        