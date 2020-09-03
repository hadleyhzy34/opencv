import cv2
import numpy as np

path = 'Resources/'

# #image addition
# x = np.uint8([250])
# y = np.uint8([10])
# #250+10=260>=255
# print(cv2.add(x, y))
# #250+10%256=4
# print(x+y)

# #iamge blending
# img1 = cv2.imread(path+'base.jpeg')
# img2 = cv2.imread(path + 'github.png')
# #make sure two images are the same size
# img2 = img2[384:768, 435:870]
# print(img1.shape)
# print(img2.shape)

# dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#bitwise operations
# Load two images
img1 = cv2.imread(path+'opencv_logo.jpg')
img2 = cv2.imread(path + 'messi5.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img1.shape
roi = img2[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
#convert opencv image into grayscale iamge
img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imshow('dst', img1gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtain black text 'opencv'
ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)

cv2.imshow('dst', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

#inverse current iamge mask
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)


# Take only region of logo from logo image.
img1_fg = cv2.bitwise_and(img1,img1,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img1_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
