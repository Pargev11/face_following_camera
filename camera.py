import cv2
import serial

#arduin = serial.Serial("com4", 9600)
x = 0
y = 0
w = 0
h = 0
faces = 0

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x,y,w,h) in faces: 
         
        x = int(x+w/2)
        
        cv2.rectangle(img, (x,0), (x,480), (0,255,0),2)
        if _map(x, 0, 635, 0, 180) <100 and _map(x, 0, 635, 0, 180)>80:
            koxm = "Stop"
        elif _map(x, 0, 635, 0, 180) >100:
            koxm = "Left"
        elif _map(x, 0, 635, 0, 180) <80:
            koxm = "Right"
            print(koxm[0:1])
        #arduin.write(koxm[0:1].encode())
        cv2.putText(img, str(_map(x, 0, 635, 0, 180)), (x+5,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)  
        cv2.putText(img, koxm, (x+5,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        x = _map(x, 0, 635, 0, 180)
    if (x,y,w,h) in faces: 
        a = 1
    else:
        koxm = "Stop"
        #arduin.write(koxm[0:1].encode())
        cv2.putText(img, koxm, (80,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
    cv2.imshow('rez', img)
        
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()