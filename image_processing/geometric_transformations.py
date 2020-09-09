import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#scaling
img = cv.imread('Resources/messi5.jpg',0)
print(img.shape)
res1 = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res2 = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

#translation
M = np.float32([[1,0,-100],[0,1,-50]])
rows,cols = img.shape
dst_translation = cv.warpAffine(img,M,(cols,rows))


#rotation
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst_rotation = cv.warpAffine(img,M,(cols,rows))

# plt.subplot(221),plt.imshow(res1, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(222),plt.imshow(res2, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(223),plt.imshow(dst_translation, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(224),plt.imshow(dst_rotation, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

#affline transform
# img = cv.imread('drawing.png')
# rows,cols,ch = img.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

#perspective transform
img = cv.imread('Resources/sudoku.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[375,160],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()