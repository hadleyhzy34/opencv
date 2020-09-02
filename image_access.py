import cv2
# print ("package improted")

# print('Opencv version {0}'.format(cv2.__version__))

# reading and showing images that stored in current project folder Resources
# img = cv2.imread("Resources/base.jpeg")

# cv2.imshow("Output",img)
# cv2.waitKey(0)

# capturing videos
# cap = cv2.VideoCapture("Resources/oldFriend.mp4")

# while True:
# # img stores all img frames of the video, success tells if it reads video successfully or not
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# using webcam
# 0 represent default webcam of your pc
cap = cv2.VideoCapture(0)
# 3 represent x
cap.set(3,640)
# 4 represent y
cap.set(4,480)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

