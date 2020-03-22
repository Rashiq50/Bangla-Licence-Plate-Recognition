import cv2
import numpy as np


def getimage(path):
    image = cv2.imread(path)
    return image


def resize(image,w,h):
    cv2.resize(image, (w, h))
    return image


def equalize(image, clip, grid):
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(grid, grid))
    cl1 = clahe.apply(image)
    return cl1

def grayscale(image, b, g, r):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coefficients = [b, g, r]
    # standard coefficients = [0.114, 0.587, 0.299]
    m = np.array(coefficients).reshape((1, 3))
    blue = cv2.transform(image, m)
    #equ = cv2.equalizeHist(blue)
    return blue


def blur(image, amount):
    blur = cv2.GaussianBlur(image, (amount, amount), 0)
    return blur


def threshold(image, para1, para2):
    ret, thresh = cv2.threshold(image, para1, para2, cv2.THRESH_BINARY_INV)
    return thresh


def canny(image):
    canny = cv2.Canny(image, 0, 0)
    return canny


#cv2.imshow("CANNY", canny)
#cv2.waitKey(0)


def process(canny, para, main, thresh, write, show):
    if para == 1:
        contours, hier = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    elif para == 0:
        contours, hier = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    for c in contours:

        if cv2.contourArea(c) > 1000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(main, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if show == 1:
                roi = thresh[y:y + h, x:x + w]
                a = cv2.resize(roi, (100, 90))
                # roi2 = thresh[y:(y+h), x:x+w]
                cv2.imshow("crop" + str(i), a)
            if write==1:
                cv2.imwrite("Dataset//crop" + str(i) + ".png", a)
            i = i + 1
            print("crop" + str(i) + "=")
            print(cv2.contourArea(c))
            cv2.waitKey(100)
    cv2.imshow("main", main)
    if write == 1:
        cv2.imwrite("Dataset//marked.png", main)
    cv2.waitKey(0)

#cv2.imshow("canny new",canny)
#cv2.imshow("lap", lp)
#cv2.imshow("erosion", erosion)
#cv2.imshow("dilate", dilation)

# cv2.imshow("X", sbx)
# cv2.imshow("Y", sby)

