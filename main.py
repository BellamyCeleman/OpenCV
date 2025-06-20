import cv2
import numpy as np
#
# img = cv2.imread("Images/skr.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# model = cv2.CascadeClassifier('faces.xml')
#
# results = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)
#
# for (x, y, w, h) in results:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

video = cv2.VideoCapture(0)
model = cv2.CascadeClassifier('faces.xml')

while True:
    res, img = video.read()

    if not res:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    results = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15)

    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("p", img)
