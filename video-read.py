import cv2 as cv



#reading from camera 

# capture = cv.videocapture(n)

# if n = 0 (webcame)
# if n = 1 (first connected camera)


capture = cv.VideoCapture('data/videos/meme.mp4')


#just like we read image bt pixel by pixel we also read the videos by frame by frame and so we use loop


while True:
    isTrue,frame = capture.read()

    cv.imshow('video',frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()

cv.destroyAllWindows()












