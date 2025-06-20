import cv2
import numpy as np

def rotate(frame, angle):
    height, width = frame.shape[:2]
    point = (height // 2, width // 2)
    matrix = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(frame, matrix, (width, height))

def shift(frame, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(frame, matrix, (frame.shape[1], frame.shape[0]))

video = cv2.VideoCapture("../OpenCV/Videos/video.mp4")


while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.GaussianBlur(frame, (7, 7), 2)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = cv2.Canny(frame, 100, 100)

    kernel = np.ones((2, 2), np.uint8)
    frame = cv2.dilate(frame, kernel)
    frame = cv2.erode(frame, kernel)

    print(frame.shape)

    # frame = rotate(frame, 60)
    frame = shift(frame, 100, 50)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()