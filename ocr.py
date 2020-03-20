import datetime

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from PIL import Image
import os


image = cv2.imread("Inputs//lc_plate9.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_thres = cv2.threshold(gray, 0, 240,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray_blur = cv2.medianBlur(gray_thres, 3)
invert = cv2.bitwise_not(gray_blur,gray_blur, mask=None)

file = "temp.png"
cv2.imwrite(file, invert)

text = pytesseract.image_to_string(Image.open(file))

txtname = (datetime.datetime.now()).strftime("%H%M")
txt = open("Outputs//"+txtname+".txt", "w", encoding="utf-8")

print(text)

cv2.imshow("Input", image)
cv2.imshow("inverted", invert)
cv2.waitKey(0)
txt.writelines(text)
