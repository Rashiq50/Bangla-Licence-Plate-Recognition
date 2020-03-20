#cv2.imshow("initial thresh", thresh)
#cv2.waitKey(0)
# sbx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
# sby = cv2.Sobel(image, cv2.CV_64F, 0, 1)
#lp = cv2.Laplacian(thresh, cv2.CV_64F, ksize=15)


#erosion = cv2.erode(canny, kernel, 1)
#dilation = cv2.dilate(erosion, kernel,0)
#kernel = np.ones((5, 5), np.uint8)
# kernel_length = np.array(image).shape[1]//80
#
# vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
# hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#
# img_temp1 = cv2.erode(canny, vertical_kernel, iterations=3)
# verticle_lines_img = cv2.dilate(img_temp1, vertical_kernel, iterations=3)
# cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
#
# img_temp2 = cv2.erode(canny, hori_kernel, iterations=3)
# horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
# cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)
#
# alpha = 0.15
# beta = 1.0 - alpha

# img_final_bin = cv2.addWeighted(horizontal_lines_img, alpha, verticle_lines_img, beta, 0.0)
#img_final_bin = cv2.erode(img_final_bin, kernel, iterations=2)

#thresh, img_final_bin = cv2.threshold(img_final_bin, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imwrite("img_final_bin.jpg", img_final_bin)

#cv2.imwrite("dilation_tmp.png",erosion)

#d2 = cv2.imread("dilation_tmp.png",cv2.IMREAD_GRAYSCALE)