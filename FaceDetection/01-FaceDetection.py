import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('image_2.jpg', cv2.COLOR_BGR2GRAY)

# print(image)

faces = dataset.detectMultiScale(image)
# print(faces)
for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 4)

cv2.imwrite('result_2.jpg', image)