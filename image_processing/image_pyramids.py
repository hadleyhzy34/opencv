# Load the image
import cv2 as cv 
    
src = cv.imread('Resources/messi5.jpg', 0)
    
while 1:
    #if grayscale image, then unpack to get two values: row, col; 
    #if color image, then unpack to get three values: row, col, channels;
    rows, cols = map(int, src.shape)
        
    cv.imshow('Pyramids Demo', src)
        
    k = cv.waitKey(0)
    if k == 27:
        break
            
    elif chr(k) == 'i':
        src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))
        print ('** Zoom In: Image x 2')
            
    elif chr(k) == 'o':
        #// operator floor division
        src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))
        print ('** Zoom Out: Image / 2')
            
cv.destroyAllWindows()