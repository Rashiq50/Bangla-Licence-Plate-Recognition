import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('lc//7.jpg', 0)
resize = cv.resize(img, (960, 720))

equ = cv.equalizeHist(resize)

# img = cv.imread('tsukuba_l.png',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=100.0, tileGridSize=(10, 10))
cl1 = clahe.apply(resize)
cv.imwrite('balanced.png', cl1)
res = np.hstack((resize, equ, cl1)) #stacking images side-by-side
cv.imwrite('all.png', res)
