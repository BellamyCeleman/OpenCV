import cv2

image = cv2.imread("Images/MainBefore.jpg")

# new_img = cv2.resize(image, (100, 100))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("ff", image)

image = cv2.Canny(image, 10, 10)

print(image.shape)
cv2.waitKey(2000)

