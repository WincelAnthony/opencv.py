import cv2 as cv

# img = cv. imread('images/me.jpg')

# cv.imshow('Wincel', img)

# Reading Videos
capture = cv.VideoCapture('video/cat.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




# cv.waitKey(0)