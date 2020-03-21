import cv2
import process as s

main = s.getimage("lc/4.jpg")

gray = s.grayscale(main, 0.1, 0.4, 0.2)  # standard = [0.114, 0.587, 0.299]
blur = s.blur(gray, 9)
threshold = s.threshold(blur, 88, 250)
canny = s.canny(threshold)

cv2.imshow("Threshold", threshold)
cv2.imshow("Canny", canny)

s.process(canny, 1, main, threshold, 0, 1)  # (imagetoprocess, contourtype, main image, crop image, write roi, show roi)
cv2.waitKey(0)
