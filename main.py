import cv2
import numpy as np
import face_recognition

imgEmerald = face_recognition.load_image_file('imagesBasic/Emerald.jpg')
imgEmerald = cv2.cvtColor(imgEmerald,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imagesBasic/Emerald Test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgEmerald)[0]
encodeEmerald = face_recognition.face_encodings(imgEmerald)[0]
cv2.rectangle(imgEmerald,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeEmerald],encodeTest)
faceDis = face_recognition.face_distance([encodeEmerald],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)

cv2.imshow('Emerald',imgEmerald)
cv2.imshow('Emerald Test',imgTest)
cv2.waitKey(0)
