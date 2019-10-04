import sys
iunc=sys.argv[1]
iname=iunc.split(".")[0]
iext=iunc.split(".")[1]

import cv2 as cv

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) 
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1) 
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    cv.imwrite(iname+"-canny."+iext, edge_output)
    dst = cv.bitwise_and(image, image, mask= edge_output)
    cv.imshow("Color Edge", dst)
    # cv.imwrite(iname+"-color."+iext, image, mask= edge_output)
src = cv.imread(iunc)
cv.namedWindow('input_image', cv.WINDOW_NORMAL) 
cv.imshow('input_image', src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
