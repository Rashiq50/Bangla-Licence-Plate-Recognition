import cv2

image = cv2.imread("Inputs/lc10.jpg")

#blur = cv2.GaussianBlur(image, (11, 11), 0)

he = cv2.equalizeHist(image)
#cv2.imwrite("he.png", he)

#clh = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
#clahe = clh.apply(image)
#cv2.imwrite("clahe.png", clahe)

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
                a = cv2.resize(roi, (90, 90))
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