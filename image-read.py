import cv2 as cv

# taking input photo as a matrix of different pixels
# img = cv.imread("data/images/cat/0b54dde5f5.jpg")
img = cv.imread("data/images/large.jpg")

# Check if the image was successfully read
    # showing the image in a new window
cv.imshow('cat', img)

    # keyboard binding function - wait for a key press indefinitely
cv.waitKey(0)

    # destroy all the windows
cv.destroyAllWindows()
