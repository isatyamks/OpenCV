import cv2 as cv

image = cv.imread('image.jpg')
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('Gray Image', gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
