# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:25:16 2024

@author: k-ruko
"""

import cv2

img = cv2.imread("C:/Users/k-ruko/Downloads/dancing_cow.webp")

dstSkala = cv2.resize(img, None, fx=2.5, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow("ori",img)
cv2.imshow("scale",dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()