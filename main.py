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
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
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
        
        
