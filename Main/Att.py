import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from datetime import date
import time
import requests
pload = {'username':'180030375','password':'Starz&1a'}
r = requests.post('http://95.217.217.134:2824/auth/',data = pload)
print(r.text)
url='http://95.217.217.134:2824/api/master/mget/'



path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    #print(encodeList)
    return encodeList
def parse(a):
    face_id=str(a)
    payload = {
    "rfid_id" : face_id
    }
    headers={"Authorization" : "Token fe4463f5170d2c8e8bec72e870483b7eeea03a12"}
    r = requests.post(url, data=payload, headers=headers)
    print(r.content)
    time.delay(30)
    
def mark(name):
    return parse(name)
    
'''def markAttendance(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            parse(entry[0])
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                da= date.today()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{da},{dtString}')
                time.sleep(30)'''

encodeListKnown = findEncodings(images)
print('Encoding complete')
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            mark(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
