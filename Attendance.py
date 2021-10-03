import sys
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from more_itertools import unique_everseen


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#function to mark attendance and time
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readline()
        nameList = []
        #Go through list one by one
        for line in myDataList:
            #find entry for each attendee
            entry = line.split(',')
            #list of names in the list
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateString = now.strftime('%d:%m:%Y')
            timeString = now.strftime('%H:%M')
            f.writelines(f'\n{name},{dateString},{timeString}')


def main():
    print("--"*20)

    path = 'ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg =  cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    #webcam initialization
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        #Since we take real-time data, resizing done to maximize speed
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        #Find location of faces on webcam
        faceCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

        #Find location of each face and get encoded value
        for encodeFace,faceLoc in zip(encodesCurFrame,faceCurFrame):
            #Compare known face with real time encoded face
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #if faceDis.any() > 0.4:
            #print(faceDis)

        #Smallest value of faceDis is the closest match
            matchIndex = np.argmin(faceDis)
        #if matchIndex.any() > 0.5:
            #print("Unknown")
        #print(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]
            #print(name)
            #To create rectangular bounding box
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,255),2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (255, 255, 255), cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
                markAttendance(name)

            with open('Attendance.csv', 'r') as f, open('FinalAttendance.csv', 'w') as out_file:
                out_file.writelines(unique_everseen(f))
            #marking real time attendance
            #markAttendance(name)

        cv2.imshow('Webcam',img)
        cv2.waitKey(1)




    #This program currently executes once every second. We intend to make this program execute once
    # every 15 minutes but we still have to figure out the best way to do this.