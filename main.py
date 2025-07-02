import cv2
import numpy as np
import face_recognition
import os
from datetime import time, datetime

from _dlib_pybind11.image_dataset_metadata import images

path = 'ImagesAttendance'
Images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curIMG = cv2.imread(f'{path}/{cls}')
    Images.append(curIMG)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findencodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def markattendance(name):
    with open('Attendance.csv', 'r+') as f:
        namelist = []
        myDataList = f.readlines()
        # print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            datestring = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(f'\n{name},{datestring}')

encodeListknown = findencodings(Images)

print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25)
    imgSmall = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    face_currFrame = face_recognition.face_locations(imgSmall)
    encode_currFrame = face_recognition.face_encodings(imgSmall,face_currFrame)

    for encodeFace, faceLoc in zip(encode_currFrame, face_currFrame):
        matches = face_recognition.compare_faces(encodeListknown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListknown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            # y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (255, 0, 0), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
            markattendance(name)
    cv2.imshow('Webcam',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

