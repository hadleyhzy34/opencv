import cv2
print ("package improted")

print('Opencv version {0}'.format(cv2.__version__))

path = 'Resources/'

# reading and showing images that stored in current project folder Resources
img = cv2.imread("Resources/base.jpeg")

# imread second argument could be cv2.IMREAD_COLOR, cv2.IMREAD_COLOR, cv2.IMREAD_UNCHANGED
# instead of using three flags, you can simply pass integers 1, 0, -1 respectively

img = cv2.imread('Resources/base.jpeg',0)

# first argument is a window name which is a string
cv2.imshow("Output",img)
# if 0 is passed, it waits indefinitely for a key stroke, for specified milliseconds
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): #wait for 's' key to save adn exit
    # write an image
    cv2.imwrite(path+'newWritten2.jpeg', img)
    cv2.destroyAllWindows()


##using matplotlib
from matplotlib import pyplot as plt

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#warning: color image loaded by opencv is in BGR mode while Matplotlib displays in RGB mode, is ti will not be displayed 