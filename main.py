import cv2
import process as s
import numpy as np
import os

main = s.getimage("lc/8.jpg")

resize = cv2.resize(main, (960, 720))
cv2.imwrite("resize.png", resize)

gray = s.grayscale(resize, 0.1, 0.4, 0.2)  # standard = [0.114, 0.587, 0.299]
cv2.imwrite("gray.png", gray)

blur = s.blur(gray, 5)
cv2.imwrite("blur.png", blur)

equ = s.equalize(gray, 3.0, 50)
cv2.imwrite("wb equalize.png", equ)

threshold = s.threshold(equ, 80, 250)
cv2.imwrite("wb threshold.png", threshold)

canny = s.canny(threshold)
cv2.imwrite("wb canny.png", canny)

#cv2.imshow("Threshold", threshold)
#cv2.imshow("Canny", canny)

s.process(canny, 1, resize, threshold, 0, 1)  # (imagetoprocess, contourtype, main image, crop image, write roi, show roi)
cv2.waitKey(0)
stack = np.hstack((threshold, canny, equ))
cv2.imwrite("Dataset//info.png", stack)
