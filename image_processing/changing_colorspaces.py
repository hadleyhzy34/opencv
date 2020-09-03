import cv2
import numpy as np
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)

# #object tracking
# cap = cv2.VideoCapture(0)
# while(1):
#     # Take each frame
#     _, frame = cap.read()
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50])
#     upper_blue = np.array([130,255,255])
#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame,frame, mask= mask)
#     cv2.imshow('frame',frame)
#     cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()

# ## cv::inRange()
# void cv::inRange	(	InputArray 	src,
# InputArray 	lowerb,
# InputArray 	upperb,
# OutputArray 	dst 
# )		
# Python:
# dst	=	cv.inRange(	src, lowerb, upperb[, dst]	)
# #include <opencv2/core.hpp>

# Checks if array elements lie between the elements of two other arrays.

# The function checks the range as follows:

# For every element of a single-channel input array:
# 𝚍𝚜𝚝(I)=𝚕𝚘𝚠𝚎𝚛𝚋(I)0≤𝚜𝚛𝚌(I)0≤𝚞𝚙𝚙𝚎𝚛𝚋(I)0
# For two-channel arrays:
# 𝚍𝚜𝚝(I)=𝚕𝚘𝚠𝚎𝚛𝚋(I)0≤𝚜𝚛𝚌(I)0≤𝚞𝚙𝚙𝚎𝚛𝚋(I)0∧𝚕𝚘𝚠𝚎𝚛𝚋(I)1≤𝚜𝚛𝚌(I)1≤𝚞𝚙𝚙𝚎𝚛𝚋(I)1
# and so forth.
# That is, dst (I) is set to 255 (all 1 -bits) if src (I) is within the specified 1D, 2D, 3D, ... box and 0 otherwise.

# When the lower and/or upper boundary parameters are scalars, the indexes (I) at lowerb and upperb in the above formulas should be omitted.

# Parameters
# src	first input array.
# lowerb	inclusive lower boundary array or a scalar.
# upperb	inclusive upper boundary array or a scalar.
# dst	output array of the same size as src and CV_8U type.
# Examples:
# samples/cpp/camshiftdemo.cpp.


#method to find HSV values to track
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print( hsv_green )

#track multiple colored object
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # define range of blue color in HSV
    lower_green = np.array([40,50,50])
    upper_green = np.array([80,255,255])
    # Threshold the HSV image to get only blue colors
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    #mask that mark more than one color
    mask = cv2.bitwise_or(mask_green, mask_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()