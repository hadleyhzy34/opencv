import cv2

path = 'Resources/'

# playing videos
cap = cv2.VideoCapture("Resources/oldFriend.mp4")

# while True:
# # img stores all img frames of the video, success tells if it reads video successfully or not
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# saving a video
# fourcc = cv2.VideoWriter_fourcc("Re")

# # using webcam, remember running this part of code directly will result in python crash, runnign this python file from terminal to get full access from laptop
# # 0 represent default webcam of your pc
# cap = cv2.VideoCapture(0)
# # 3 represent x
# cap.set(3,640)
# # 4 represent y
# cap.set(4,480)
# #change birghtness of webcam using parameter 10
# cap.set(10,100)

# while True:
#     #success shows if cap succesfully or not, img represent frames of video
#     success, img = cap.read()
#       #convert it into grey scale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # gray = cv2.imread(img,0)

#     # cv2.imshow("Video", img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if not cap.isOpened(): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# keep in mind video writer has to keep original video size otherwise video will be corrupted, you could resize every frame later on
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(path+'outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))
 
while True:
  ret, frame = cap.read()
 
  if ret: 
     
    frame = cv2.flip(frame, 0)
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
