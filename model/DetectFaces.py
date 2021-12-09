import cv2;
# Deteccion facial
#Crea una ventana donde reconoce el rostro y dibuja un rectangulo 
def detectFaces ():
    face_cascade = cv2.CascadeClassifier('model/dataSet.xml')

    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame,
                                            scaleFactor=1.1, minNeighbors=5)
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

        cv2.imshow('Detectando rostro', frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        
        if cv2.getWindowProperty('Detectando rostro',cv2.WND_PROP_VISIBLE) < 1:        
            break 
        
    video.release()

    
    

     
    # Deteccion facial
    #Crea una ventana donde reconoce el rostro y dibuja un rectangulo 
     
    # Deteccion facial
    #Crea una ventana donde reconoce el rostro y dibuja un rectangulo 
