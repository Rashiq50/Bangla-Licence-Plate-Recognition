import cv2
import numpy as np
import matplotlib.pyplot as plt

#im = cv2.imread("lc//1.jpg")

#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#coefficients = [0,1,0]
# for standard gray conversion, coefficients = [0.114, 0.587, 0.299]
#m = np.array(coefficients).reshape((1,3))
#blue = cv2.transform(im, m)
#cv2.imshow("im", blue)
#cv2.imshow("gray", gray)

#cv2.waitKey(0)

image=cv2.imread("lc//10.jpg")
image = cv2.resize(image, (960, 720))


def equalize_light(image, limit=3, grid=(7, 7), gray=False):

    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        gray = True

    clahe = cv2.createCLAHE(clipLimit=limit, tileGridSize=grid)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))

    image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    if gray:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return np.uint8(image)
eq = equalize_light(image)
cv2.imshow("asd",eq)
cv2.waitKey(0)