
import cv2
import face_recognition
 
imgAngela = face_recognition.load_image_file('tryImages/Angela Bassett.jpeg')
imgAngela = cv2.cvtColor(imgAngela,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('tryImages/Angela Test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgAngela)[0]
encodeAngela = face_recognition.face_encodings(imgAngela)[0]
cv2.rectangle(imgAngela,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodeAngela],encodeTest)
faceDis = face_recognition.face_distance([encodeAngela],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('Angela Bassett',imgAngela)
cv2.imshow('Angela Test',imgTest)
cv2.waitKey(0)