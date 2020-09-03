import cv2
import numpy as np

path = 'Resources/'
#get number of clock-cycles used to excute a function
img1 = cv2.imread(path+'messi5.jpg')

e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

# Result I got is 0.521107655 seconds
# pip install ipython 
# type ipython to start ipython console

# In [10]: x = 5

# In [11]: %timeit y=x**2
# 10000000 loops, best of 3: 73 ns per loop

# In [12]: %timeit y=x*x
# 10000000 loops, best of 3: 58.3 ns per loop

# In [15]: z = np.uint8([5])

# In [17]: %timeit y=z*z
# 1000000 loops, best of 3: 1.25 us per loop

# In [19]: %timeit y=np.square(z)
# 1000000 loops, best of 3: 1.16 us per loop

