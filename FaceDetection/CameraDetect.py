import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()
    # ret - True or False
    #       True - camera is working properly
    #       False - camera is not working properly
    # img - whatever your camera is viweing
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(gray)
        for x, y, w, h in face:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)
        cv2.imshow('result', img)
        # delay = 1 ms
        # waitKey - opencv will wait every millisecond unitll
        # we press esc(27)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Some Error")

cv2.destroyAllWindows()
capture.release()