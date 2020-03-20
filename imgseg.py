import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from PIL import Image
import os

img = cv2.imread('Inputs//lc4.jpg')
img2 = cv2.resize(img , (200,90))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)

# image = cv2.imread("Inputs//lc_plate8c.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret,gray_thres = cv2.threshold(gray, 0, 240, cv2.THRESH_OTSU)
# gray_blur = cv2.medianBlur(thresh, 3)
# invert = cv2.bitwise_and(gray_blur, gray_blur, mask=None)

# find contours
ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    print(cv2.contourArea(ctr))
    if 100 < cv2.contourArea(ctr) < 1500:
        # bounding
        x, y, w, h = cv2.boundingRect(ctr)

        roi = thresh[y:y + h, x:x + w]
        a = cv2.resize(roi, (100, 90))
        name = 'character' + str(i)
        dirt = "Dataset//" + name + ".png"
        cv2.imshow(name, a)
        if os.path.exists(dirt):
            name = name + "cpy"
            dirt = "Dataset//" + name + ".png"
        # print(name + " =")
        # print(cv2.contourArea(ctr))
        cv2.imwrite(dirt, a)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 1)
        cv2.waitKey(100)

cv2.imshow('marked areas', img2)
cv2.imshow('Threshold', thresh)
# cv2.imshow('gray blurred', gray_blur)
cv2.imwrite("Dataset//marked.png",img2)
cv2.waitKey(0)
