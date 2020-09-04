#tutorial for smoothing images:
#https://docs.opencv.org/master/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html
#median filter: https://en.wikipedia.org/wiki/Median_filter#:~:text=The%20median%20filter%20is%20a,edge%20detection%20on%20an%20image).
#range filter and spatial domain filter:
#https://dsp.stackexchange.com/questions/56431/what-is-the-difference-between-domain-and-range-filtering
#https://reference.wolfram.com/language/ref/RangeFilter.html?view=all
#https://www.mathworks.com/help/images/ref/rangefilt.html
#https://users.soe.ucsc.edu/~manduchi/Papers/ICCV98.pdf

# The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. 
# bilateral filtering using matlab: https://github.com/GKalliatakis/Bilateral-Filtering
# bilateral filtering using python and c++:https://github.com/anlcnydn/bilateral
# bilateral tutorial reference: https://www.csie.ntu.edu.tw/~cyy/courses/vfx/10spring/lectures/handouts/lec14_bilateral_4up.pdf


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('Resources/messi5.jpg')

blur = cv2.blur(img, (5,5))

#third argument represents variance, if it's zero, then it will be set depending on size of kernel
gaussian_filter = cv2.GaussianBlur(img, (5,5), 0)

median = cv2.medianBlur(img, 5)

bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)


titles = ['Original Image','averaging','guassian_blur','median','bilateral']
images = [img, blur, gaussian_filter, median, bilateral_filter]
for i in range(5):
    plt.subplot(1,5,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
