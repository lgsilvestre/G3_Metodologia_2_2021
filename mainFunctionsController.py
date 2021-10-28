import sys
import cv2
import face_recognition
import numpy as np
import datetime
import os
import CamaraTest, recognition
from view.mainFunctions import mainFunctions
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog

cancel = False

class mainFunctionsController(QDialog):
    def __init__(self):
        super(mainFunctionsController, self).__init__()
        self.ui = mainFunctions()
        self.ui.setupUi(self)
        self.ui.video.setPixmap(QPixmap("default.jpg"))
        self.image = None
        self.BtnActions()
        self.show()
    
    def BtnActions(self):   
        self.ui.btnConfirm.clicked.connect(self.btnConfirmAction)
        self.ui.btnCancel.clicked.connect(self.btnCancelAction)        
        
    def btnConfirmAction(self):
        self.cancel = False
        self.startVideo("0")
        
    def btnCancelAction(self):
        print("cancel")        
        self.cancel = True
        self.ui.video.setPixmap(QPixmap("default.jpg"))
        
        
        
        
        
    def startVideo(self, camera_name):
        selfAux = self
        self = self.ui
        
        """
        Busca las camaras disponibles
        """
        print("Buscando camara")
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
            print("camara default")
        else:
            self.capture = cv2.VideoCapture(camera_name)
            print("camara usb")
        timer = QTimer(selfAux)  # Create Timer
        path = 'img'
        if not os.path.exists(path):
            os.mkdir(path)
            print("Folder created")
        # Reconoce el rostro de las imagenes guardadas en img
        print("Ansalizando imagenes guardadas")
        images = []
        self.class_names = []
        self.encode_list = []
        attendance_list = os.listdir(path)
        print(attendance_list)
        for cl in attendance_list:
            cur_img = cv2.imread(f'{path}/{cl}')
            images.append(cur_img)
            self.class_names.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            # encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encodes_cur_frame)
        timer.timeout.connect(selfAux.update_frame)  # Conecta una funcion al timer con 40 ms
        timer.start(20)  
            
        print("fin reconocimiento de imagenes guardadas")

    def face_rec_(self, frame, encode_list_known, class_names):
        """
        :param frame: frame from camera
        :param encode_list_known: known face encoding
        :param class_names: known face names
        """
        # csv
        def mark_attendance(name):
            """
            Registra la asistencia en un archivo csv con el nombre de la persona
            """
            with open('Attendance.csv', 'a') as f:
                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                f.writelines(f'\n{name},{date_time_string}')
        # face recognition
        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
        # count = 0
        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            name = "unknown"
            best_match_index = np.argmin(face_dis)
            # print("s",best_match_index)
            if match[best_match_index]:
                name = class_names[best_match_index].upper()
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            mark_attendance(name)
        return frame

    def update_frame(self):
        selfUi = self.ui
        ret, self.image = selfUi.capture.read()
        self.displayImage(self.image, selfUi.encode_list, selfUi.class_names, 1)

    def displayImage(self, image, encode_list, class_names, window=1):
        """
        :param image: frame from camera
        :param encode_list: known face encoding list
        :param class_names: known face names
        :param window: number of window
        :return:
        """
        selfUi = self.ui
        image = cv2.resize(image, (640, 480))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1 and self.cancel == False:
            #print("Mostrando imagen")
            selfUi.video.setPixmap(QPixmap.fromImage(outImage))
            selfUi.video.setScaledContents(True)

        
        
        
        
        
