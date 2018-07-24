import cv2
import numpy as np

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

data = []

while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(gray, 1.3)
        for x, y, w, h in face:
            faceComponent = img[y:y+h, x:x+w, :]
            faceComp = cv2.resize(faceComponent, (50,50))
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)

            if len(data) <= 20:
                data.append(faceComp)

        cv2.imshow('result', img)
        if cv2.waitKey(1) == 27 or len(data) >= 20:
            break
    else:
        print("Some Error")

data = np.asarray(data)
np.save('face_1.npy', data)

cv2.destroyAllWindows()
capture.release()
