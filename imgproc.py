import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from PIL import Image


print(cv2.__version__)

source = cv2.imread("Inputs//lc_plate2p.jpg")
mser = cv2.MSER_create()

grayim = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)



#hulls.append(cv2.convexHull())
save = source.copy()
regions, _ = mser.detectRegions(grayim)
#print(regions)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

cv2.polylines(save, hulls, 1, (0, 0, 255))

#mask image
mask = np.ones((grayim.shape[0], grayim.shape[1], 1), dtype=np.uint8)


#draw contour
for contour in hulls:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

invrt = cv2.bitwise_not(grayim, grayim)
thres = cv2.threshold(invrt, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#temp file
cv2.imwrite("processed.png",thres)

#tesseract
text = pytesseract.image_to_string(Image.open("processed.png"))

print(text)
cv2.imshow("image", save)
cv2.imshow("threshold image", thres)
cv2.waitKey(0)

#print(img)
#cv2.imshow("image",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()