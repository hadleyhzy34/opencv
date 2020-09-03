import cv2
import numpy as np


path = 'Resources/'
img = cv2.imread(path+'base.jpeg')


#print current pixel color BGR values
px = img[200,200]
print(px)

#accessing certain B value
blue = img[200, 200, 0]

#accessing certain G value
green = img[200, 200, 1]

#accessing certain R value
red = img[200, 200, 2]

print(blue)
print(green)
print(red)


#using array item for individual access
print(img.item(200,200,0))
print(img.item(200,200,1))
print(img.item(200,200,2))

#modifying BGR value
img.itemset((200,200,2), 100)
print(img.item(200,200,2))

#accessing image properties
print(img.shape)

#total number of pixels is accessed by:
print(img.size)

#image datatype is obtained:
print(img.dtype)

#image ROI
area_to_be_copied = img[280:340, 330:390]
img[273:333, 100:160] = area_to_be_copied
cv2.imshow("test", img)
cv2.waitKey(0)

#splitting and merging image channels
#B,G,R channels of an image can be split into their individual planes
b, g, r = cv2.split(img)
img = cv2.merge(b,g,r)
#making all red channels to be zero
img[:,:,2] = 0
remember that cv2.split() is a costly operation so use it if necessary

#padding
from matplotlib import pyplot as plt

BLUE = [255,0,0]

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()


