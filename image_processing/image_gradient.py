#concept: https://aishack.in/tutorials/sobel-laplacian-edge-detectors/
# https://stackoverflow.com/questions/4483502/edge-detection-techniques#:~:text=Sobel%2FPrewitt%20measure%20the%20slope,the%20change%20of%20the%20slope.&text=The%20result%20of%20a%20lapace,because%20the%20slope%20is%20constant.&text=Also%2C%20a%20Laplace%20filter%20is,noise%20than%20Sobel%20or%20Prewitt.


#1. Sobel and Scharr Derivatives
# Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. You can specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder respectively). You can also specify the size of kernel by the argument ksize. If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter. Please see the docs for kernels used.

# 2. Laplacian Derivatives
# It calculates the Laplacian of the image given by the relation, Δsrc=∂2src∂x2+∂2src∂y2 where each derivative is found using Sobel derivatives. If ksize = 1, then following kernel is used for filtering:

import cv2
import numpy as np
from matplotlib import pyplot as plt

ddepth = cv2.CV_64F
img = cv2.imread('Resources/sudoku.png')

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,ddepth,1,0,ksize=5)
sobely = cv2.Sobel(img,ddepth,0,1,ksize=5)

#Black-to-White transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken as a Negative slope (It has negative value).
abs_sobel_x = cv2.convertScaleAbs(sobelx)
abs_sobel_y = cv2.convertScaleAbs(sobely)

grad = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(abs_sobel_x,cmap = 'gray')
plt.title('abs_sobel_x'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6),plt.imshow(abs_sobel_y,cmap = 'gray')
plt.title('abs_sobel_y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7),plt.imshow(grad,cmap = 'gray')
plt.title('grad'), plt.xticks([]), plt.yticks([])

plt.show()

# img = cv2.imread('Resources/box.png',0)

# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)

# plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,4,4),plt.imshow(sobelx64f,cmap = 'gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.show()