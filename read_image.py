import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Borboleta linda", img)

print(img)

img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Borboleta triste", img_cinza)

print(img_cinza)

cv2.waitKey(0)