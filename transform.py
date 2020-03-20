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

image=cv2.imread("lc//2.jpg")

#hist= cv2.calcHist(image,[0],None,[256],[0,256])
#plt.hist(image.ravel(),256,[0,256]); plt.show()
cv2.imshow("input",image)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)