# https://www.youtube.com/watch?v=LdOnanfc5TM
# https://julie-jiang.github.io/image-segmentation/
# https://www.geeksforgeeks.org/max-flow-problem-introduction/
# http://theory.stanford.edu/~tim/w16/l/l1.pdf
# https://www.youtube.com/watch?v=oHy3ddI9X3o
# https://www.cs.princeton.edu/courses/archive/spring06/cos226/lectures/maxflow.pdf


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('Resources/messi5.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,450,290)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()