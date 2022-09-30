import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint Image Certain Color
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Red', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# 3. Draw A Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# Draw A Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

cv.waitKey(0)