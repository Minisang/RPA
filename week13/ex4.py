import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ff = np.fromfile(r'sample_img2222.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2,5)
print(faces)
i=1
black=(0,0,0)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    #인식 얼굴에 번호 표시하기
    cv2.putText(img, "%d" % (i), (x,y), cv2.FONT_HERSHEY_PLAIN,2,black,1,cv2.LINE_AA)
    #자신의 얼굴 번호 모자이크 처리
    if i==2 :
        face_img = img[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, dsize=(0,0), fx=0.1, fy=0.1)
        face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
        img[y:y+h, x:x+w] = face_img
    i+=1

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

