#https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/back_projection/back_projection.html


import numpy as np
import cv2 as cv

target = cv.imread('Resources/messi5.jpg')
hsvt = cv.cvtColor(target,cv.COLOR_BGR2HSV)

# cv.imshow('target', target)
# cv.waitKey(0)

roi = target[280:300,40:80]
hsv = cv.cvtColor(roi,cv.COLOR_BGR2HSV)

# calculating object histogram
# roihist = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
# # normalize histogram and apply backprojection
# cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
# dst = cv.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
# # Now convolute with circular disc
# disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
# cv.filter2D(dst,-1,disc,dst)
# # threshold and binary AND
# ret,thresh = cv.threshold(dst,50,255,0)
# thresh = cv.merge((thresh,thresh,thresh))
# res = cv.bitwise_and(target,thresh)
# res = np.vstack((target,thresh,res))
# cv.imshow('res',res)
# cv.waitKey(0)
# cv.imwrite('res.jpg',res)


#algorithm using numpy
# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
R = M/I;
h,s,v = cv.split(hsvt)
h_test = h.ravel()
s_test = s.ravel()

# filter array
#filter 1d array
# arr = np.array([41,42,43,44])
# x = [3,2,1,0]
# y = arr[x]

#filter 2d array
arr = np.array([[41,42,43,44],[45,46,47,48],[49,50,51,52],[53,54,55,56]])
x = [0,1,2,3]
y = [0,1,2,3]
z = arr[x,y]

B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])
# cv.imshow('current filter', B)
# cv.waitKey(0)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv.normalize(B,B,0,255,cv.NORM_MINMAX)

ret,thresh = cv.threshold(B,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(target,thresh)
res = np.vstack((target,thresh,res))
cv.imshow('res',res)
cv.waitKey(0)


