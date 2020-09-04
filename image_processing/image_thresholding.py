# threshold types

# Enumerator
# THRESH_BINARY 
# Python: cv.THRESH_BINARY
# 𝚍𝚜𝚝(x,y)={𝚖𝚊𝚡𝚟𝚊𝚕0if 𝚜𝚛𝚌(x,y)>𝚝𝚑𝚛𝚎𝚜𝚑otherwise

# THRESH_BINARY_INV 
# Python: cv.THRESH_BINARY_INV
# 𝚍𝚜𝚝(x,y)={0𝚖𝚊𝚡𝚟𝚊𝚕if 𝚜𝚛𝚌(x,y)>𝚝𝚑𝚛𝚎𝚜𝚑otherwise

# THRESH_TRUNC 
# Python: cv.THRESH_TRUNC
# 𝚍𝚜𝚝(x,y)={𝚝𝚑𝚛𝚎𝚜𝚑𝚘𝚕𝚍𝚜𝚛𝚌(x,y)if 𝚜𝚛𝚌(x,y)>𝚝𝚑𝚛𝚎𝚜𝚑otherwise

# THRESH_TOZERO 
# Python: cv.THRESH_TOZERO
# 𝚍𝚜𝚝(x,y)={𝚜𝚛𝚌(x,y)0if 𝚜𝚛𝚌(x,y)>𝚝𝚑𝚛𝚎𝚜𝚑otherwise

# THRESH_TOZERO_INV 
# Python: cv.THRESH_TOZERO_INV
# 𝚍𝚜𝚝(x,y)={0𝚜𝚛𝚌(x,y)if 𝚜𝚛𝚌(x,y)>𝚝𝚑𝚛𝚎𝚜𝚑otherwise

# THRESH_MASK 
# Python: cv.THRESH_MASK

# THRESH_OTSU 
# Python: cv.THRESH_OTSU
# flag, use Otsu algorithm to choose the optimal threshold value

# THRESH_TRIANGLE 
# Python: cv.THRESH_TRIANGLE
# flag, use Triangle algorithm to choose the optimal threshold value
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resources/gradient.png', 0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#adaptive thresholding
# img = cv.imread('sudoku.png',0)
# img = cv.medianBlur(img,5)
# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#             cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in xrange(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()


#otsu's binarization
# for more details, check Otsu's method https://en.wikipedia.org/wiki/Otsu%27s_method
# In order to do so, the cv.threshold() function is used, where cv.THRESH_OTSU is passed as an extra flag. The threshold value can be chosen arbitrary. The algorithm then finds the optimal threshold value which is returned as the first output.
img = cv.imread('noisy2.png',0)
blur = cv.GaussianBlur(img,(5,5),0)
# find normalized_histogram, and its cumulative distribution function
hist = cv.calcHist([blur],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.sum()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in xrange(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
    q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    b1,b2 = np.hsplit(bins,[i]) # weights
    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print( "{} {}".format(thresh,ret) )

