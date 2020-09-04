import cv2
import numpy as np
from matplotlib import pyplot as plt

#erosion
#A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
img = cv2.imread('Resources/j.png', 0)
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

#dilation Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’.
dilation = cv2.dilate(img, kernel, iterations = 1)

#Opening is just another name of erosion followed by dilation.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


#closing Closing is reverse of Opening, Dilation followed by Erosion.
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#morphological gradient
#It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#top hat
#It is the difference between input image and Opening of the image.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

#Black Hat
#It is the difference between the closing of the input image and input image.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)



titles = ['Original Image','erosion', 'dilation', 'opening','closing','gradient','tophat', 'blackhat']
images = [img, erosion,dilation,opening,closing,gradient,tophat,blackhat]
for i in range(8):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()