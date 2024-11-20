import cv2
import numpy as np
img0 = cv2.imread("C:/Users/k-ruko/Downloads/Vestia_Zeta_-_Portrait_01.webp")
img  = cv2.cvtColor (img0, cv2.COLOR_BGR2GRAY)

lowBlue = np.array ([30, 10 ,10])
highBlue = np.array([255, 225, 255])
mask = cv2.inRange (img, lowBlue, highBlue)
cv2.imshow("img0",img0)

img,img
print (img.shape)
cv2.waitKey(0)
cv2.destroyAllWIndows ()