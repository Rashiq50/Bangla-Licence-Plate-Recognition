import cv2
import process as s
import numpy as np
import os

main = s.getimage("lc/5.jpg")
resize = cv2.resize(main, (960, 720))

gray = s.grayscale(resize, 0.1, 0.4, 0.2)  # standard = [0.114, 0.587, 0.299]
equ = s.equalize(gray, 5.0, 8)
blur = s.blur(equ, 9)
threshold = s.threshold(blur, 167, 250)
canny = s.canny(threshold)

cv2.imshow("Threshold", threshold)
cv2.imshow("Canny", canny)

s.process(canny, 1, resize, threshold, 1, 1)  # (imagetoprocess, contourtype, main image, crop image, write roi, show roi)
cv2.waitKey(0)
stack = np.hstack((threshold, canny, equ))
cv2.imwrite("Dataset//info.png", stack)
