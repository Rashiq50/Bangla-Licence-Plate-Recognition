import cv2
import process as s
import numpy as np

main = s.getimage("lc/2.jpg")

resize = cv2.resize(main, (960, 720))

gray = s.grayscale(resize, 0.1, 0.4, 0.2)  # standard = [0.114, 0.587, 0.299]

equ = s.equalize(gray, 3.0, 50)

blur = s.blur(equ, 7)

threshold = s.threshold(blur, 82, 250)
adaptive = s.adaptive(blur, 255, 40)

canny = s.canny(threshold)
canny2 = s.canny(adaptive)

cv2.imshow("equalized",equ)
cv2.imshow("Threshold", threshold)
cv2.imshow("Canny", canny)
cv2.imshow("Adaptive canny", canny2)

s.process(canny, 1, resize, threshold, 0, 1)  # (ImageProc, contourType, mainImage, crop image, writeROI, show roi)
cv2.waitKey(0)
# stack = np.hstack((threshold, canny, equ))

# cv2.imwrite("Dataset//info.png", stack)
