import cv2
import numpy as np

#create a black image
img = np.zeros((512,512,3), np.uint8)

#draw a diagonal blue line with thickness of 5px
img = cv2.line(img, (0,0), (511,511), (0,0,255), 5)


#drawing a rectangle
img = cv2.rectangle(img, (240,234), (280,423),(0,255,0),3)

#drawing circle, thickness -1 means to fill color to cover the whole circle
img = cv2.circle(img, (447,63), 63, (255,0,0), -1)

# drawing ellipse
img = cv2.ellipse(img,(256,256),(100,50),180,0,180,(255,0,0),-1)

#drawing polygon
pts = np.array([[101,15],[220,130],[370,220],[420,110]], np.int32)
pts = pts.reshape((-1, 2))
#If third argument is False, you will get a polylines joining all the points, not a closed shape.
img = cv2.polylines(img,[pts],True,(0,255,255))


#adding text to images
cv2.putText(img,'OpenCV', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)


cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()