import cv2 as cv

#img = cv.imread('images/me.jpg')
#cv.imshow('Wincel', img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos, and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live Videos
    capture.set(3,width)
    capture.set(4,height)
# Reading Videos
capture = cv.VideoCapture('video/cat.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()