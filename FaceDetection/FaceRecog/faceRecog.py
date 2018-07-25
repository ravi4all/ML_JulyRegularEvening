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

labels = np.zeros((40,1))
labels[:20,:] = 0.0
labels[20:,:] = 1.0

data = np.concatenate([face_1, face_2])

# print(data.shape)
# print(labels.shape)

def distance(x1,x2):
    return np.sqrt(((x2 - x1) ** 2).sum())

##def knn(train,x, k=5):
##    m = train.shape[0]
##    dist = []
##
##    for i in range(m):
##        dist.append([train[i], x])
##
##    dist = np.asarray(dist)
##    index = np.argsort(dist)
##    sorted_labels = labels[index][:k]
##    counts = np.unique(sorted_labels, return_counts=True)
##    return counts[0][np.argmax(counts[1])]

def knn(train,x, k=5):
    m = train.shape[0]
    dist = []
    for ix in range(m):
        # compute distance from each point and store in dist
        dist.append(distance(x, train[ix]))
    dist = np.asarray(dist)
    indx = np.argsort(dist)
    print("Index...",indx)
    sorted_labels = labels[indx][:k]
    print("Sorted...",sorted_labels)
    counts = np.unique(sorted_labels, return_counts=True)
    print("Count...",counts)
    return counts[0][np.argmax(counts[1])]

while True:
    ret, frame = capture.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_component = frame[y:y + h, x:x + w, :]
            fc = cv2.resize(face_component, (50, 50))
            lab = knn(data,fc.flatten())
            text = users[int(lab)]
            cv2.putText(frame, text, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('face', frame)
        k = cv2.waitKey(33) & 0xFF
        if k == 27:
            break
    else:
        print('Error')

capture.release()
cv2.destroyAllWindows()
