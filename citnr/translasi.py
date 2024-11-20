# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:34:24 2024

@author: k-ruko
"""

import cv2
import numpy as np
img = cv2.imread("C:/Users/k-ruko/Downloads/dancing_cow.webp")
print(img.shape)

baris, coloms, ghgh = img.shape

MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

print(MTranslasi, '\n')



dst = cv2.warpAffine (img, MTranslasi, (coloms, baris))
cv2.imshow("title", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()