import cv2
import numpy as np

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

face_1 = np.load('face_1.npy').reshape((20,50*50*3))
face_2 = np.load('face_1.npy').reshape((20,50*50*3))

users = {
    0 : 'Ravi',
    1 : 'Raman'
}

labels = np.zeros([40,1])
labels[:20,:] = 0.0
labels[20:,:] = 1.0

data = np.concatenate([face_1, face_2])

# print(data.shape)
# print(labels.shape)

def distance(x1,x2):
    return np.sqrt(((x2 - x1) ** 2).sum())

def knn(train,x, k=5):
    m = train.shape[0]
    dist = []

    for i in range(m):
        dist.append([train[i], x])

    dist = np.asarray(dist)
    index = np.argsort(dist)
    sorted_labels = labels[index][:k]
    counts = np.unique(sorted_labels, return_counts=True)
    return counts[0][np.argmax(counts[1])]

while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(gray, 1.3)
        for x, y, w, h in face:
            faceComponent = img[y:y+h, x:x+w, :]
            faceComp = cv2.resize(faceComponent, (50,50))
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)

            label = knn(data,faceComp.flatten())
            username = users.get(int(label))
            cv2.putText(img, username,(x,y),font,1,(255,0,0),2)

        cv2.imshow('result', img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Some Error")

cv2.destroyAllWindows()
capture.release()