# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:08:51 2024

@author: k-ruko
"""

import cv2
import numpy as np
img = cv2.imread("C:/Users/k-ruko/Downloads/Vestia_Zeta_-_Portrait_01.webp")
gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
(thresh,BW) = cv2.threshold(gray,100, 155,cv2.THRESH_BINARY)
row, col = img.shape [0:2]
cv2.imshow("original", img)
for i in range(row):
   for j in range(col):
      img[i, j] = sum(img[i, j]) * -0.33
print (img.shape) 
print ("original = ", img.shape)
print ("gray = ", gray.shape)
print ("BW = ", BW.shape)
print (BW)

cv2.imshow("img", img)
cv2.imshow("Gray", gray)
cv2.imshow("BW", BW)
cv2.waitKey(0)
cv2.destroyAllWIndows()