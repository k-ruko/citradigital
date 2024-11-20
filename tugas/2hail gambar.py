# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:40:17 2024

@author: k-ruko
"""

import cv2
import numpy as np
img= cv2.imread("C:/Users/k-ruko/Downloads/Vestia_Zeta_-_Portrait_01.webp")
cv2.imshow("original", img)
row, col = img.shape [0:2]

for i in range(row):
   for j in range(col):
      img[i, j] = sum(img[i, j]) * 0.33
print (img.shape) 

cv2.imshow("Hasil", img)
cv2.waitKey(0)
cv2.destroyAllWIndows()