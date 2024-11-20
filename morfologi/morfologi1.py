# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:50:05 2024

@author: k-ruko
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/k-ruko/Downloads/download.jfif',0 )
imgO = cv2.imread('C:/Users/k-ruko/Downloads/dancing_cow.webp', )
imgC = cv2.imread('C:/Users/k-ruko/Downloads/sucipto.jfif', )



kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(imgO, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)

titles = ['Normal Image', 'Erosion',
          'Dilation', 'Before Opening', 
          'Opening', 'Before Closing', 'Closing']

images = [img, erosion, dilation, imgO, opening, imgC, closing]

cv2.imshow("normal", imgO)
cv2.imshow("default image",imgC)
cv2.imshow("normal", img)
cv2.imshow("erosion", img)
cv2.imshow("dilation", img)

cv2.waitKey(0)
cv2.destroyAllWIndows ()
""""
for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()"""