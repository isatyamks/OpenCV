import cv2 as cv
import numpy as np

image = np.zeros((400, 400, 3), dtype=np.uint8)  # Create a black image

cv.rectangle(image, (50, 50), (300, 200), (0, 255, 0), thickness=2)
cv.circle(image, (200, 250), 30, (0, 0, 255), thickness=-1)
cv.putText(image, 'OpenCV', (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=2)

cv.imshow('Drawing', image)
cv.waitKey(0)
cv.destroyAllWindows()
